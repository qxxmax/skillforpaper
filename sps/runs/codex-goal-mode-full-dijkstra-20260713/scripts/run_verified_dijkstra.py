#!/usr/bin/env python3
"""Run Dijkstra on the source-verified SPS literature graph."""

from __future__ import annotations

import csv
import heapq
import math
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROOT_ID = "2606.13790"
ROOT_NODE = f"paper:{ROOT_ID}"


def rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def split_authors(value: str) -> list[str]:
    return [re.sub(r"\s+", " ", part).strip()
            for part in re.split(r";|\band\b", value or "")
            if re.sub(r"\s+", " ", part).strip()]


def add_node(nodes: dict[str, dict[str, str]], node_id: str, node_type: str,
             label: str, arxiv_id: str = "", evidence_level: str = "",
             cluster: str = "") -> None:
    nodes.setdefault(node_id, {
        "node_id": node_id,
        "node_type": node_type,
        "label": label,
        "arxiv_id": arxiv_id,
        "evidence_level": evidence_level,
        "cluster": cluster,
    })


def add_edge(graph: dict[str, list[tuple[str, float, str, str]]],
             edges: list[dict[str, object]], source: str, target: str,
             weight: float, relation: str, evidence_kind: str,
             evidence_ref: str) -> None:
    weight = round(weight, 6)
    graph[source].append((target, weight, relation, evidence_ref))
    edges.append({
        "edge_id": f"DE{len(edges)+1:05d}",
        "source": source,
        "target": target,
        "weight": weight,
        "relation": relation,
        "evidence_kind": evidence_kind,
        "evidence_ref": evidence_ref,
    })


def dijkstra(graph: dict[str, list[tuple[str, float, str, str]]], source: str):
    distances = {source: 0.0}
    previous: dict[str, tuple[str, str, float, str]] = {}
    heap = [(0.0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances[node] + 1e-12:
            continue
        for neighbor, weight, relation, evidence in graph.get(node, []):
            proposed = distance + weight
            if proposed + 1e-12 < distances.get(neighbor, math.inf):
                distances[neighbor] = proposed
                previous[neighbor] = (node, relation, weight, evidence)
                heapq.heappush(heap, (proposed, neighbor))
    return distances, previous


def reconstruct(previous: dict[str, tuple[str, str, float, str]], target: str):
    node_path = [target]
    relations = []
    weights = []
    evidence = []
    cursor = target
    while cursor in previous:
        parent, relation, weight, evidence_ref = previous[cursor]
        node_path.append(parent)
        relations.append(relation)
        weights.append(weight)
        evidence.append(evidence_ref)
        cursor = parent
    return list(reversed(node_path)), list(reversed(relations)), list(reversed(weights)), list(reversed(evidence))


def write(name: str, data: list[dict[str, object]], fields: list[str] | None = None) -> None:
    if fields is None:
        fields = list(data[0]) if data else []
    with (ROOT / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)


def main() -> None:
    selected = rows("selected_fulltexts.csv")
    notes = {row["arxiv_id"]: row for row in rows("manual_reading_notes.csv")}
    relations = rows("relation_ledger.csv")
    selected_by_id = {row["arxiv_id"]: row for row in selected}

    nodes: dict[str, dict[str, str]] = {}
    edges: list[dict[str, object]] = []
    graph: dict[str, list[tuple[str, float, str, str]]] = defaultdict(list)

    for row in selected:
        arxiv_id = row["arxiv_id"]
        note = notes[arxiv_id]
        paper_node = f"paper:{arxiv_id}"
        add_node(nodes, paper_node, "paper", row["title"], arxiv_id,
                 "full_text_rechecked", note["broad_cluster"])
        for author in split_authors(row["authors"]):
            author_node = "author:" + slug(author)
            add_node(nodes, author_node, "author", author)
            add_edge(graph, edges, paper_node, author_node, 0.45,
                     "paper_to_author", "metadata", f"selected_fulltexts.csv:{arxiv_id}")
            add_edge(graph, edges, author_node, paper_node, 0.60,
                     "author_to_paper", "metadata", f"selected_fulltexts.csv:{arxiv_id}")
        groups = [group for group in row["method_groups"].split(";") if group]
        if not groups:
            groups = [slug(note["broad_cluster"])]
        for group in groups:
            method_node = "method:" + slug(group)
            add_node(nodes, method_node, "method", group, cluster=note["broad_cluster"])
            add_edge(graph, edges, paper_node, method_node, 0.65,
                     "paper_to_method", "screened_method_tag", f"candidate_screening_table.csv:{arxiv_id}")
            add_edge(graph, edges, method_node, paper_node, 0.75,
                     "method_to_paper", "screened_method_tag", f"candidate_screening_table.csv:{arxiv_id}")

    for relation in relations:
        ancestor = f"paper:{relation['source_arxiv_id']}"
        descendant = f"paper:{relation['target_arxiv_id']}"
        if relation["source_arxiv_id"] not in selected_by_id or relation["target_arxiv_id"] not in selected_by_id:
            continue
        # Reverse edge from a citing paper to its cited ancestor supports backward lineage search.
        add_edge(graph, edges, descendant, ancestor, 0.20,
                 "backward_direct_citation", "exact_identifier_context", relation["edge_id"])
        # Forward edge follows time/idea flow from cited ancestor to citing descendant.
        add_edge(graph, edges, ancestor, descendant, 0.30,
                 "forward_direct_citation", "exact_identifier_context", relation["edge_id"])

    if ROOT_NODE not in nodes:
        raise SystemExit("SPS root node missing")
    distances, previous = dijkstra(graph, ROOT_NODE)

    paths = []
    for row in selected:
        arxiv_id = row["arxiv_id"]
        node = f"paper:{arxiv_id}"
        reachable = node in distances
        node_path, path_relations, path_weights, evidence = reconstruct(previous, node) if reachable else ([], [], [], [])
        path_kind = "root"
        if path_relations:
            if all("citation" in relation for relation in path_relations):
                path_kind = "citation_only"
            elif any("author" in relation for relation in path_relations):
                path_kind = "author_bridge"
            elif any("method" in relation for relation in path_relations):
                path_kind = "method_bridge"
            else:
                path_kind = "mixed"
        paths.append({
            "arxiv_id": arxiv_id,
            "title": row["title"],
            "year": row["year"],
            "cluster": notes[arxiv_id]["broad_cluster"],
            "reachable": "yes" if reachable else "no",
            "dijkstra_distance": round(distances[node], 6) if reachable else "",
            "path_kind": path_kind,
            "path_nodes": " -> ".join(node_path),
            "path_relations": " -> ".join(path_relations),
            "path_weights": " + ".join(str(value) for value in path_weights),
            "path_cost_recomputed": round(sum(path_weights), 6),
            "evidence_refs": ";".join(evidence),
        })
    paths.sort(key=lambda row: (
        row["reachable"] != "yes",
        float(row["dijkstra_distance"]) if row["dijkstra_distance"] != "" else math.inf,
        int(row["year"] or 9999),
        row["title"],
    ))
    for rank, row in enumerate(paths, 1):
        row["rank"] = rank

    candidate_paths = {row["candidate_id"].removeprefix("arxiv:"): row
                       for row in rows("dijkstra_candidate_shortest_paths.csv")
                       if row["candidate_id"].startswith("arxiv:")}
    comparison = []
    for path in paths:
        candidate = candidate_paths.get(path["arxiv_id"])
        comparison.append({
            "arxiv_id": path["arxiv_id"],
            "title": path["title"],
            "candidate_graph_rank": candidate["dijkstra_rank"] if candidate else "gap_closure",
            "candidate_graph_distance": candidate["dijkstra_distance"] if candidate else "not_in_round1_graph",
            "verified_graph_rank": path["rank"],
            "verified_graph_distance": path["dijkstra_distance"],
            "verified_path_kind": path["path_kind"],
            "interpretation": "search priority versus checked lineage proximity",
        })

    ranked = []
    for path in paths:
        if path["arxiv_id"] == ROOT_ID:
            action = "root anchor"
        elif path["path_kind"] == "citation_only":
            action = "core lineage anchor"
        elif path["path_kind"] == "author_bridge":
            action = "inspect author-lineage bridge"
        elif path["path_kind"] == "method_bridge":
            action = "inspect conceptual bridge; do not call it citation ancestry"
        else:
            action = "inspect mixed path and its evidence types"
        ranked.append({
            "reading_rank": path["rank"],
            "arxiv_id": path["arxiv_id"],
            "title": path["title"],
            "distance": path["dijkstra_distance"],
            "path_kind": path["path_kind"],
            "recommended_audit_action": action,
            "already_full_text_read": "yes",
        })

    write("dijkstra_graph_nodes.csv", list(nodes.values()))
    write("dijkstra_graph_edges.csv", edges)
    write("dijkstra_shortest_paths.csv", paths,
          ["rank", "arxiv_id", "title", "year", "cluster", "reachable",
           "dijkstra_distance", "path_kind", "path_nodes", "path_relations",
           "path_weights", "path_cost_recomputed", "evidence_refs"])
    write("dijkstra_ranked_reading.csv", ranked)
    write("dijkstra_two_pass_comparison.csv", comparison)

    kind_counts = defaultdict(int)
    for path in paths:
        kind_counts[path["path_kind"]] += 1
    report = [
        "# Verified-Graph Dijkstra Run",
        "",
        "This is the second Dijkstra pass. It starts at SPS and traverses checked",
        "direct-citation edges, current metadata authorship edges, and screened",
        "method-membership edges. Evidence types remain explicit in every path.",
        "",
        "## Graph and reachability",
        "",
        f"- nodes: {len(nodes)}",
        f"- directed weighted edges: {len(edges)}",
        f"- selected paper nodes: {len(selected)}",
        f"- reachable paper nodes: {sum(row['reachable']=='yes' for row in paths)}",
        f"- citation-only paths: {kind_counts['citation_only']}",
        f"- author-bridge paths: {kind_counts['author_bridge']}",
        f"- method-bridge paths: {kind_counts['method_bridge']}",
        "",
        "## Shortest paths from SPS",
        "",
        "| rank | paper | distance | path type | shortest path |",
        "|---:|---|---:|---|---|",
    ]
    for row in paths:
        report.append(
            f"| {row['rank']} | {row['title']} | {row['dijkstra_distance']} | "
            f"{row['path_kind']} | `{row['path_nodes']}` |"
        )
    report += [
        "",
        "## Interpretation boundary",
        "",
        "A citation-only path is supported by exact arXiv identifiers in current",
        "full text. Author and method bridges are navigation aids and are never",
        "reported as direct citation ancestry. Dijkstra distance is not evidence",
        "that a scientific claim is true.",
    ]
    (ROOT / "dijkstra_run_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")

    with (ROOT / "dijkstra_weight_policy.md").open("a", encoding="utf-8") as handle:
        handle.write("""

## Verified graph pass

- citing paper to cited ancestor: `0.20` (backward direct-citation traversal);
- cited ancestor to citing paper: `0.30` (forward direct-citation traversal);
- paper to author / author to paper: `0.45 / 0.60`;
- paper to method / method to paper: `0.65 / 0.75`.

Citation edges use exact identifiers extracted from current full text. Author
and method edges are retained as different relation types so that a shortest
path cannot be misreported as citation ancestry.
""")
    print(f"nodes={len(nodes)} edges={len(edges)} papers={len(selected)} reachable={sum(row['reachable']=='yes' for row in paths)} kinds={dict(kind_counts)}")


if __name__ == "__main__":
    main()
