#!/usr/bin/env python3
"""Build the current candidate graph and run an auditable Dijkstra pass."""

from __future__ import annotations

import csv
import heapq
import math
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROOT_CANDIDATE = "arxiv:2606.13790"
ROOT_NODE = f"paper:{ROOT_CANDIDATE}"

ROUTE_COST = {
    "root": 0.05,
    "backward": 0.20,
    "forward": 0.35,
    "author": 0.45,
    "keyword": 0.65,
    "adjacent": 0.75,
    "adversarial": 0.85,
    "extension": 0.80,
    "evaluation": 0.80,
    "source_link": 0.15,
    "closure": 0.70,
}

SOURCE_PENALTY = {
    "root_bibliography": 0.00,
    "arXiv": 0.00,
    "OpenAlex": 0.08,
    "Crossref": 0.12,
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def candidate_key(row: dict[str, str]) -> str:
    if row.get("arxiv_id"):
        return "arxiv:" + row["arxiv_id"]
    if row.get("doi"):
        return "doi:" + row["doi"].lower()
    return "title:" + norm(row.get("title", ""))


def author_ids(value: str) -> list[tuple[str, str]]:
    result = []
    for raw in re.split(r";|\band\b", value or ""):
        label = re.sub(r"\s+", " ", raw).strip()
        if label:
            result.append(("author:" + norm(label).replace(" ", "_"), label))
    return result


def add_node(nodes: dict[str, dict[str, str]], node_id: str, node_type: str,
             label: str, **extra: str) -> None:
    row = {"node_id": node_id, "node_type": node_type, "label": label,
           "decision": "", "facets": "", "source": ""}
    row.update(extra)
    nodes.setdefault(node_id, row)


def add_edge(graph: dict[str, list[tuple[str, float, str]]],
             edges: list[dict[str, object]], source: str, target: str,
             weight: float, relation: str, evidence: str) -> None:
    weight = round(max(weight, 0.01), 6)
    graph[source].append((target, weight, relation))
    edges.append({
        "edge_id": f"CE{len(edges)+1:05d}",
        "source": source,
        "target": target,
        "weight": weight,
        "relation": relation,
        "evidence": evidence,
    })


def dijkstra(graph: dict[str, list[tuple[str, float, str]]], source: str):
    distances = {source: 0.0}
    previous: dict[str, tuple[str, str, float]] = {}
    heap = [(0.0, source)]
    while heap:
        distance, node = heapq.heappop(heap)
        if distance > distances[node] + 1e-12:
            continue
        for neighbor, weight, relation in graph.get(node, []):
            proposed = distance + weight
            if proposed + 1e-12 < distances.get(neighbor, math.inf):
                distances[neighbor] = proposed
                previous[neighbor] = (node, relation, weight)
                heapq.heappush(heap, (proposed, neighbor))
    return distances, previous


def path_to(previous: dict[str, tuple[str, str, float]], target: str):
    nodes = [target]
    relations = []
    weights = []
    cursor = target
    while cursor in previous:
        parent, relation, weight = previous[cursor]
        nodes.append(parent)
        relations.append(relation)
        weights.append(weight)
        cursor = parent
    nodes.reverse()
    relations.reverse()
    weights.reverse()
    return nodes, relations, weights


def write_csv(name: str, rows: list[dict[str, object]], fields: list[str]) -> None:
    with (ROOT / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    candidates = read_csv("candidate_screening_table.csv")
    routes = read_csv("query_matrix.csv")
    hits = read_csv("route_results.csv")
    by_id = {row["candidate_id"]: row for row in candidates}
    route_by_id = {row["query_id"]: row for row in routes}

    graph: dict[str, list[tuple[str, float, str]]] = defaultdict(list)
    nodes: dict[str, dict[str, str]] = {}
    edges: list[dict[str, object]] = []

    for row in candidates:
        paper_node = "paper:" + row["candidate_id"]
        add_node(nodes, paper_node, "paper", row["title"],
                 decision=row["decision"], facets=row["facets"],
                 source=row["primary_url"])
        for author_node, label in author_ids(row["authors"]):
            add_node(nodes, author_node, "author", label)
            add_edge(graph, edges, paper_node, author_node, 0.55,
                     "paper_to_author", row["candidate_id"])
            add_edge(graph, edges, author_node, paper_node, 0.70,
                     "author_to_paper", row["candidate_id"])
        for facet in filter(None, row["facets"].split(";")):
            facet_node = "facet:" + norm(facet).replace(" ", "_")
            add_node(nodes, facet_node, "facet", facet)
            add_edge(graph, edges, paper_node, facet_node, 0.80,
                     "paper_to_facet", row["candidate_id"])
            add_edge(graph, edges, facet_node, paper_node, 0.95,
                     "facet_to_paper", row["candidate_id"])

    if ROOT_CANDIDATE not in by_id:
        raise SystemExit("Root candidate missing")

    for route in routes:
        query_node = "query:" + route["query_id"]
        add_node(nodes, query_node, "query", route["query"],
                 facets=route["facet"], source=route["source"])
        add_edge(graph, edges, ROOT_NODE, query_node,
                 ROUTE_COST.get(route["family"], 1.0),
                 "root_to_query", f"{route['query_id']}:{route['family']}")

    for hit in hits:
        key = candidate_key(hit)
        if key not in by_id:
            continue
        route = route_by_id[hit["query_id"]]
        query_node = "query:" + hit["query_id"]
        paper_node = "paper:" + key
        rank = max(int(hit["rank"] or 25), 1)
        weight = (0.25 + math.log1p(rank) / 2.5
                  + SOURCE_PENALTY.get(hit["source"], 0.18))
        add_edge(graph, edges, query_node, paper_node, weight,
                 "query_hit", f"{hit['query_id']} rank={rank} source={hit['source']}")

    distances, previous = dijkstra(graph, ROOT_NODE)
    ranked = []
    for row in candidates:
        node = "paper:" + row["candidate_id"]
        reachable = node in distances
        path_nodes, relations, weights = path_to(previous, node) if reachable else ([], [], [])
        distance = distances.get(node, math.inf)
        score = int(row["score"])
        route_occurrences = int(row["route_occurrences"])
        priority = (math.exp(-distance / 3.0) if reachable else 0.0)
        priority += min(max(score, 0), 20) / 100.0
        priority += min(route_occurrences, 8) / 200.0
        ranked.append({
            "candidate_id": row["candidate_id"],
            "title": row["title"],
            "decision": row["decision"],
            "screen_score": score,
            "route_occurrences": route_occurrences,
            "dijkstra_distance": round(distance, 6) if reachable else "",
            "priority_score": round(priority, 6),
            "reachable": "yes" if reachable else "no",
            "path_nodes": " -> ".join(path_nodes),
            "path_relations": " -> ".join(relations),
            "path_edge_weights": " + ".join(str(value) for value in weights),
        })
    ranked.sort(key=lambda row: (
        row["reachable"] != "yes",
        float(row["dijkstra_distance"]) if row["dijkstra_distance"] != "" else math.inf,
        -float(row["priority_score"]),
        row["title"],
    ))
    for rank, row in enumerate(ranked, 1):
        row["dijkstra_rank"] = rank

    write_csv("dijkstra_candidate_graph_nodes.csv", list(nodes.values()),
              ["node_id", "node_type", "label", "decision", "facets", "source"])
    write_csv("dijkstra_candidate_graph_edges.csv", edges,
              ["edge_id", "source", "target", "weight", "relation", "evidence"])
    write_csv("dijkstra_candidate_shortest_paths.csv", ranked,
              ["dijkstra_rank", "candidate_id", "title", "decision", "screen_score",
               "route_occurrences", "dijkstra_distance", "priority_score", "reachable",
               "path_nodes", "path_relations", "path_edge_weights"])

    eligible = [row for row in ranked if row["decision"] == "include"
                and row["candidate_id"].startswith("arxiv:")]
    report = [
        "# Candidate-Graph Dijkstra Run",
        "",
        "This is an actual single-source Dijkstra calculation from the SPS root.",
        "It uses current-run query hits, authorship, and facet membership.",
        "Screen labels are not used as edge weights; they remain an eligibility gate.",
        "",
        "## Graph",
        "",
        f"- nodes: {len(nodes)}",
        f"- edges: {len(edges)}",
        f"- paper candidates: {len(candidates)}",
        f"- reachable paper candidates: {sum(row['reachable'] == 'yes' for row in ranked)}",
        f"- eligible arXiv full texts: {len(eligible)}",
        "",
        "## First 15 eligible reading paths",
        "",
        "| rank | candidate | distance | screen score | path |",
        "|---:|---|---:|---:|---|",
    ]
    for row in eligible[:15]:
        report.append(
            f"| {row['dijkstra_rank']} | {row['title']} | {row['dijkstra_distance']} | "
            f"{row['screen_score']} | `{row['path_nodes']}` |"
        )
    report += [
        "",
        "## Boundary",
        "",
        "The distance is a search-navigation cost, not citation proof or claim evidence.",
    ]
    (ROOT / "dijkstra_candidate_run_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    policy = """# Dijkstra Weight Policy

## Candidate pass

- Root-to-query costs encode route cost: exact/root and backward routes are
  cheaper than keyword, adjacent, adversarial, or extension routes.
- Query-to-paper cost is `0.25 + log(1 + rank)/2.5 + source_penalty`.
- arXiv and the live root bibliography have zero source penalty; OpenAlex and
  Crossref carry small metadata penalties.
- Paper-author and author-paper edges permit auditable coauthor expansion.
- Paper-facet and facet-paper edges permit a higher-cost topic bridge.
- Screening score is not an edge weight. It is used only as a relevance gate
  and a small secondary reading-priority term.

All weights are positive, so ordinary Dijkstra assumptions hold. Distances
rank inspection cost only and cannot promote a candidate to evidence.
"""
    (ROOT / "dijkstra_weight_policy.md").write_text(policy, encoding="utf-8")
    print(f"nodes={len(nodes)} edges={len(edges)} candidates={len(candidates)} reachable={sum(row['reachable']=='yes' for row in ranked)}")


if __name__ == "__main__":
    main()
