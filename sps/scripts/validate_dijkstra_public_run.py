#!/usr/bin/env python3
"""Validate the public SPS Dijkstra packet without requiring local PDFs."""

from __future__ import annotations

import csv
import heapq
import math
import sys
import zipfile
from collections import defaultdict
from pathlib import Path


SPS = Path(__file__).resolve().parents[1]
RUN = SPS / "runs" / "codex-goal-mode-full-dijkstra-20260713"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def rows(name: str) -> list[dict[str, str]]:
    path = RUN / name
    if not path.exists():
        fail(f"missing artifact: {path.relative_to(SPS)}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def build_graph(
    node_rows: list[dict[str, str]], edge_rows: list[dict[str, str]]
) -> tuple[set[str], dict[str, list[tuple[str, float]]], dict[tuple[str, str], list[float]]]:
    nodes = {row["node_id"] for row in node_rows}
    if len(nodes) != len(node_rows):
        fail("duplicate node IDs")
    adjacency: dict[str, list[tuple[str, float]]] = defaultdict(list)
    exact_edges: dict[tuple[str, str], list[float]] = defaultdict(list)
    for index, edge in enumerate(edge_rows, 1):
        source, target = edge["source"], edge["target"]
        if source not in nodes or target not in nodes:
            fail(f"edge {index} has an unknown endpoint: {source} -> {target}")
        weight = float(edge["weight"])
        if not math.isfinite(weight) or weight < 0:
            fail(f"edge {index} has invalid Dijkstra weight: {weight}")
        adjacency[source].append((target, weight))
        exact_edges[(source, target)].append(weight)
    return nodes, adjacency, exact_edges


def shortest_paths(
    adjacency: dict[str, list[tuple[str, float]]], root: str
) -> dict[str, float]:
    distance = {root: 0.0}
    queue = [(0.0, root)]
    while queue:
        current, node = heapq.heappop(queue)
        if current > distance[node] + 1e-12:
            continue
        for target, weight in adjacency.get(node, []):
            proposal = current + weight
            if proposal + 1e-12 < distance.get(target, math.inf):
                distance[target] = proposal
                heapq.heappush(queue, (proposal, target))
    return distance


def split_path(value: str) -> list[str]:
    return [item.strip() for item in value.split(" -> ") if item.strip()]


def split_weights(value: str) -> list[float]:
    return [float(item.strip()) for item in value.split(" + ") if item.strip()]


def validate_reported_paths(
    path_rows: list[dict[str, str]],
    root: str,
    distance: dict[str, float],
    exact_edges: dict[tuple[str, str], list[float]],
    target_column: str,
    distance_column: str,
    path_column: str,
    weights_column: str,
) -> None:
    for row in path_rows:
        if row.get("reachable", "yes") != "yes":
            continue
        target = row[target_column]
        nodes = split_path(row[path_column])
        weights = split_weights(row[weights_column])
        if not nodes or nodes[0] != root or nodes[-1] != target:
            fail(f"invalid path endpoints for {target}")
        if len(nodes) != len(weights) + 1:
            fail(f"path/weight length mismatch for {target}")
        for source, destination, weight in zip(nodes, nodes[1:], weights):
            candidates = exact_edges.get((source, destination), [])
            if not any(abs(candidate - weight) < 1e-8 for candidate in candidates):
                fail(f"reported edge is absent: {source} -> {destination} ({weight})")
        reported = float(row[distance_column])
        if abs(reported - sum(weights)) > 1e-6:
            fail(f"path sum mismatch for {target}")
        if abs(reported - distance.get(target, math.inf)) > 1e-6:
            fail(f"path is not independently shortest for {target}")


required = [
    "README.md",
    "runtime_accounting.md",
    "dijkstra_effect_evaluation.md",
    "dijkstra_selection_comparison.csv",
    "manual_reading_notes.csv",
    "claim_source_ledger.csv",
    "evidence_registry.csv",
    "gap_ledger.csv",
    "literature_research_report.md",
    "final_validation_report.md",
    "sps_literature_audit_full_dijkstra.xlsx",
    "graphs/dijkstra_selection_effect.png",
    "graphs/citation_lineage_graph.png",
]
for relative in required:
    path = RUN / relative
    if not path.exists() or path.stat().st_size == 0:
        fail(f"missing or empty artifact: {path.relative_to(SPS)}")

candidate_nodes = rows("dijkstra_candidate_graph_nodes.csv")
candidate_edges = rows("dijkstra_candidate_graph_edges.csv")
candidate_paths = rows("dijkstra_candidate_shortest_paths.csv")
if (len(candidate_nodes), len(candidate_edges), len(candidate_paths)) != (3300, 8187, 593):
    fail("candidate graph counts differ from 3300 / 8187 / 593")
_, candidate_adjacency, candidate_exact = build_graph(candidate_nodes, candidate_edges)
candidate_distance = shortest_paths(candidate_adjacency, "paper:arxiv:2606.13790")
if len(candidate_distance) != 3300:
    fail(f"candidate graph reachable count is {len(candidate_distance)}, expected 3300")
candidate_path_rows = []
for row in candidate_paths:
    copy = dict(row)
    copy["target_node"] = f"paper:{row['candidate_id']}"
    candidate_path_rows.append(copy)
validate_reported_paths(
    candidate_path_rows,
    "paper:arxiv:2606.13790",
    candidate_distance,
    candidate_exact,
    "target_node",
    "dijkstra_distance",
    "path_nodes",
    "path_edge_weights",
)

verified_nodes = rows("dijkstra_graph_nodes.csv")
verified_edges = rows("dijkstra_graph_edges.csv")
verified_paths = rows("dijkstra_shortest_paths.csv")
if (len(verified_nodes), len(verified_edges), len(verified_paths)) != (164, 944, 37):
    fail("verified graph counts differ from 164 / 944 / 37")
_, verified_adjacency, verified_exact = build_graph(verified_nodes, verified_edges)
verified_distance = shortest_paths(verified_adjacency, "paper:2606.13790")
verified_path_rows = []
for row in verified_paths:
    copy = dict(row)
    copy["target_node"] = f"paper:{row['arxiv_id']}"
    verified_path_rows.append(copy)
validate_reported_paths(
    verified_path_rows,
    "paper:2606.13790",
    verified_distance,
    verified_exact,
    "target_node",
    "dijkstra_distance",
    "path_nodes",
    "path_weights",
)

selection = rows("dijkstra_selection_comparison.csv")
baseline = {row["candidate_id"] for row in selection if row["baseline_selected"] == "yes"}
dijkstra = {row["candidate_id"] for row in selection if row["dijkstra_selected"] == "yes"}
if (len(baseline), len(dijkstra), len(baseline & dijkstra)) != (30, 30, 20):
    fail("equal-budget selection invariant differs from 30 / 30 / 20")

selected = rows("selected_fulltexts.csv")
notes = rows("manual_reading_notes.csv")
evidence = rows("evidence_registry.csv")
relations = rows("relation_ledger.csv")
if (len(selected), len(notes), len(evidence), len(relations)) != (37, 37, 185, 199):
    fail("public evidence counts differ from 37 / 37 / 185 / 199")
if not all(
    row.get(f"{role}_anchor", "").strip()
    for row in notes
    for role in ("problem", "method", "result", "limitation")
):
    fail("one or more public reading records lacks a required source anchor")

workbook = RUN / "sps_literature_audit_full_dijkstra.xlsx"
with zipfile.ZipFile(workbook) as archive:
    bad_member = archive.testzip()
    if bad_member:
        fail(f"invalid workbook member: {bad_member}")

report_text = (RUN / "final_validation_report.md").read_text(encoding="utf-8")
if "**Status: PASS**" not in report_text:
    fail("the preserved local full-run validation did not report PASS")

print(
    "PASS: public Dijkstra packet; "
    "candidate graph 3300/8187/593, verified graph 164/944/37, "
    "selection 30/30/20, evidence 37/185/199"
)
