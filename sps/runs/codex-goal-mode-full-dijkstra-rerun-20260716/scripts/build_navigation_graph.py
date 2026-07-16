#!/usr/bin/env python3
"""Create a current-run navigation graph and display adapters for Part 1."""

from __future__ import annotations

import argparse
import csv
import math
import re
from collections import defaultdict
from pathlib import Path


ROOT_ID = "2606.13790"
ROOT_NODE = f"paper:{ROOT_ID}"


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def author_names(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def display_cluster(cluster: str) -> str:
    groups = {
        "root_sps": "SPS",
        "flow_lattice": "Flow methods",
        "gauge_flow": "Flow methods",
        "flow_overview": "Flow methods",
        "path_control": "Path-space control",
        "optimal_control": "Path-space control",
        "stochastic_flow": "Stochastic flows",
        "annealed_flow": "Stochastic flows",
        "diffusion": "Diffusion",
        "diffusion_lattice": "Diffusion",
        "forward_neighbor": "Diffusion",
        "nonequilibrium_lattice": "Nonequilibrium",
        "evaluation": "Evaluation",
        "autoregressive_lattice": "Autoregressive",
        "critical_sampling": "Multiscale",
        "author_context": "Mechanism audit",
        "failure_mode": "Failure mode",
    }
    return groups.get(cluster, cluster.replace("_", " "))


def short_label(arxiv_id: str, title: str) -> str:
    labels = {
        "2606.13790": "SPS (Chen et al., 2026)",
        "1904.12072": "Flow-based MCMC (2019)",
        "2003.06413": "Gauge-equivariant flow (2020)",
        "2101.08176": "Normalizing-flow overview (2021)",
        "2111.15141": "Path Integral Sampler (2022)",
        "2201.08862": "SNF as nonequilibrium (2022)",
        "2201.13117": "CRAFT (2022)",
        "2210.03139": "SNF for lattice field theory",
        "2211.01364": "Optimal-control diffusion view",
        "2302.13834": "Denoising Diffusion Samplers",
        "2302.14082": "Flow mode-collapse diagnostics",
        "2309.17082": "Diffusion as stochastic quantization",
        "2310.11979": "Out-of-equilibrium topology",
        "2311.03578": "Generative diffusion precursor",
        "2402.06561": "Topological-freezing protocol",
        "2404.09723": "Exact Fourier acceleration",
        "2412.00200": "SNF scaling in SU(3)",
        "2512.19575": "VAN plus MH in phi4",
        "2604.10209": "Multiscale critical sampler",
        "2605.11199": "Operator spectroscopy",
        "2607.08505": "Diffusion near criticality",
    }
    return labels.get(arxiv_id, title[:42])


def round_cost(round_name: str) -> float:
    values = {
        "L0": 0.05, "L1": 0.20, "L2": 0.40, "L3": 0.50, "L4": 0.60,
        "L5": 0.65, "L6": 0.70, "L7": 0.70, "L8": 0.75, "L9": 0.75, "L10": 0.80,
    }
    return values.get(round_name, 1.00)


def add_node(nodes: dict[str, dict[str, object]], node_id: str, node_type: str, label: str, **extra: object) -> None:
    if node_id not in nodes:
        nodes[node_id] = {
            "node_id": node_id,
            "node_type": node_type,
            "label": label,
            "arxiv_id": "",
            "evidence_level": "",
            "cluster": "",
            "screen_decision": "",
            "source_url": "",
        }
    nodes[node_id].update({key: value for key, value in extra.items() if value != ""})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    screen = read_csv(run_dir / "candidate_screening_table.csv")
    selected = read_csv(run_dir / "selected_fulltexts.csv")
    selected_by_id = {row["arxiv_id"]: row for row in selected}
    notes = {row["arxiv_id"]: row for row in read_csv(run_dir / "c4_reading_notes.psv", delimiter="|")}
    protocol = read_csv(run_dir / "search_protocol.csv")
    routes = read_csv(run_dir / "route_results.csv")
    relations = read_csv(run_dir / "relation_ledger.csv")

    active = [row for row in screen if row["decision"] in {"include", "candidate"}]
    active_by_id = {row["arxiv_id"]: row for row in active}
    nodes: dict[str, dict[str, object]] = {}
    edges: list[dict[str, object]] = []

    for row in active:
        arxiv_id = row["arxiv_id"]
        selected_row = selected_by_id.get(arxiv_id)
        evidence_level = "C4" if arxiv_id in notes else ("C3" if selected_row else "C2")
        add_node(
            nodes, f"paper:{arxiv_id}", "paper", row["title"],
            arxiv_id=arxiv_id,
            evidence_level=evidence_level,
            cluster=selected_row["cluster"] if selected_row else "",
            screen_decision=row["decision"],
            source_url=row["canonical_url"],
        )
    if ROOT_NODE not in nodes:
        raise SystemExit("Root paper is not in the screened active candidate set")
    for route in protocol:
        query_node = f"query:{route['query_id']}"
        add_node(nodes, query_node, "query", route["expression"], cluster=route["facet"])
        edges.append({
            "edge_id": f"G{len(edges)+1:04d}",
            "source": ROOT_NODE,
            "target": query_node,
            "weight": round_cost(route["round"]),
            "relation": "root_to_query",
            "evidence": f"search_protocol.csv:{route['query_id']}",
        })
    configured_routes = {route["query_id"] for route in protocol}
    for route_id in sorted({hit["route_id"] for hit in routes if hit["route_id"] not in configured_routes}):
        representative = next(hit for hit in routes if hit["route_id"] == route_id)
        query_node = f"query:{route_id}"
        add_node(nodes, query_node, "query", f"identifier probe {route_id}", cluster="identifier_probe")
        edges.append({
            "edge_id": f"G{len(edges)+1:04d}",
            "source": ROOT_NODE,
            "target": query_node,
            "weight": 0.10 if route_id == "P01" else 0.30,
            "relation": "root_to_identifier_probe",
            "evidence": f"{representative['raw_file']}:{route_id}",
        })
    for hit in routes:
        arxiv_id = hit["arxiv_id"]
        if arxiv_id not in active_by_id:
            continue
        query_node = f"query:{hit['route_id']}"
        paper_node = f"paper:{arxiv_id}"
        weight = 0.25 + math.log1p(max(int(hit["rank"]), 1)) / 2.5
        edges.append({
            "edge_id": f"G{len(edges)+1:04d}",
            "source": query_node,
            "target": paper_node,
            "weight": round(weight, 6),
            "relation": "query_hit",
            "evidence": f"{hit['raw_file']} rank={hit['rank']}",
        })
    for row in selected:
        paper_node = f"paper:{row['arxiv_id']}"
        for author in author_names(row["authors"]):
            author_node = f"author:{norm(author)}"
            add_node(nodes, author_node, "author", author)
            edges.append({
                "edge_id": f"G{len(edges)+1:04d}",
                "source": paper_node,
                "target": author_node,
                "weight": 0.45,
                "relation": "paper_to_author",
                "evidence": f"selected_fulltexts.csv:{row['arxiv_id']}",
            })
            edges.append({
                "edge_id": f"G{len(edges)+1:04d}",
                "source": author_node,
                "target": paper_node,
                "weight": 0.60,
                "relation": "author_to_paper",
                "evidence": f"selected_fulltexts.csv:{row['arxiv_id']}",
            })
        method_node = f"method:{norm(row['cluster'])}"
        add_node(nodes, method_node, "method", row["cluster"], cluster=row["cluster"])
        edges.append({
            "edge_id": f"G{len(edges)+1:04d}",
            "source": paper_node,
            "target": method_node,
            "weight": 0.65,
            "relation": "paper_to_method",
            "evidence": f"selected_fulltexts.csv:{row['arxiv_id']}",
        })
        edges.append({
            "edge_id": f"G{len(edges)+1:04d}",
            "source": method_node,
            "target": paper_node,
            "weight": 0.85,
            "relation": "method_to_paper",
            "evidence": f"selected_fulltexts.csv:{row['arxiv_id']}",
        })
    for relation in relations:
        target = relation["target_arxiv_id"]
        if target not in active_by_id:
            continue
        if relation["relation_type"] == "direct_citation":
            weight = 0.15
            label = "backward_direct_citation"
        else:
            weight = 0.80
            label = "declared_method_neighbor"
        edges.append({
            "edge_id": f"G{len(edges)+1:04d}",
            "source": ROOT_NODE,
            "target": f"paper:{target}",
            "weight": weight,
            "relation": label,
            "evidence": f"relation_ledger.csv:{relation['edge_id']}",
        })

    graph_nodes = list(nodes.values())
    graph_nodes.sort(key=lambda row: str(row["node_id"]))
    write_csv(run_dir / "dijkstra_graph_nodes.csv", graph_nodes, list(graph_nodes[0]))
    write_csv(run_dir / "dijkstra_graph_edges.csv", edges, [
        "edge_id", "source", "target", "weight", "relation", "evidence",
    ])
    policy = [
        "# Dijkstra Weight Policy",
        "",
        "- root-to-query: 0.05 for identity, then 0.20 to 0.80 as expansion rounds move farther from the root.",
        "- query-to-paper: 0.25 + log(1 + arXiv rank) / 2.5.",
        "- checked direct citation: 0.15.",
        "- declared non-citation method neighbor: 0.80.",
        "- paper-author and author-paper: 0.45 and 0.60.",
        "- paper-method and method-paper: 0.65 and 0.85.",
        "",
        "All weights are positive. Distances rank navigation cost only; neither a short",
        "path nor a query hit is scientific evidence.",
    ]
    (run_dir / "dijkstra_weight_policy.md").write_text("\n".join(policy) + "\n", encoding="utf-8")

    relation_by_target = {row["target_arxiv_id"]: row for row in relations}
    display_nodes = []
    for row in selected:
        year = row["published"][:4]
        relation = relation_by_target.get(row["arxiv_id"], {})
        display_nodes.append({
            "NodeID": row["arxiv_id"],
            "Title": row["title"],
            "Year": year,
            "ShortLabel": short_label(row["arxiv_id"], row["title"]),
            "PrimaryDisplayCluster": display_cluster(row["cluster"]),
            "AllTopicLabels": display_cluster(row["cluster"]),
            "EvidenceLevel": "claim_anchored" if row["arxiv_id"] in notes else "full_text",
            "SourceRelation": "root" if row["arxiv_id"] == ROOT_ID else relation.get("relation_type", "selected_context"),
            "ReadingPriority": "P0" if row["target_level"] == "C4" else "P1",
            "SourceURL": row["canonical_url"],
            "PublicGraphStatus": "show" if row["target_level"] == "C4" else "hide",
        })
    display_relations = []
    for relation in relations:
        if relation["target_arxiv_id"] not in selected_by_id:
            continue
        display_relations.append({
            "EdgeID": relation["edge_id"],
            "SourceID": ROOT_ID,
            "TargetID": relation["target_arxiv_id"],
            "EdgeType": "direct_citation" if relation["relation_type"] == "direct_citation" else "conceptual_neighbor",
            "DirectlyCited": "yes" if relation["relation_type"] == "direct_citation" else "no",
            "EvidenceID": relation["evidence_id"],
            "RelationBasis": relation["relation_basis"],
            "Confidence": relation["confidence"],
            "HumanReviewStatus": "reviewed",
            "PublicGraphStatus": "show",
        })
    write_csv(run_dir / "display_graph_nodes.csv", display_nodes, list(display_nodes[0]))
    write_csv(run_dir / "display_graph_relations.csv", display_relations, list(display_relations[0]))
    funnel_rows = [
        ("raw_route_hits", len(routes), "Raw arXiv records across L0-L10", "route_results.csv", "route_id+arxiv_id", "none"),
        ("deduplicated_candidates", len(screen), "Deduplicated C0 candidate records", "candidate_screening_table.csv", "arxiv_id", "deduplicate"),
        ("C0_C2_active", len(active), "Records retained for full-text queue or method adjacency", "candidate_screening_table.csv", "arxiv_id", "decision in include,candidate"),
        ("C3_full_text", len(selected), "Current downloaded PDFs passing integrity and text extraction", "source_matrix.csv", "arxiv_id", "full_text_integrity PASS"),
        ("C4_claim_anchor", len(notes), "Core papers with manual source anchors and boundaries", "native_paper_reading_ledger.csv", "arxiv_id", "reading_level C4"),
    ]
    write_csv(run_dir / "audit_funnel_counts.csv", [
        {"Stage": stage, "Count": count, "Meaning": meaning, "SourceTable": source, "DeduplicationKey": key, "Filter": filter_value}
        for stage, count, meaning, source, key, filter_value in funnel_rows
    ], ["Stage", "Count", "Meaning", "SourceTable", "DeduplicationKey", "Filter"])
    print(f"nodes={len(graph_nodes)} edges={len(edges)} active_papers={len(active)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
