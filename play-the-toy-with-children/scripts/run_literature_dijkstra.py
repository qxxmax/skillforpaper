#!/usr/bin/env python3
"""Run auditable single-source Dijkstra on a literature-graph CSV pair."""

from __future__ import annotations

import argparse
import csv
import heapq
import math
from collections import defaultdict
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0]) if rows else []
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nodes", type=Path, required=True)
    parser.add_argument("--edges", type=Path, required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--node-id-column", default="node_id")
    parser.add_argument("--node-type-column", default="node_type")
    parser.add_argument("--label-column", default="label")
    parser.add_argument("--source-column", default="source")
    parser.add_argument("--target-column", default="target")
    parser.add_argument("--weight-column", default="weight")
    parser.add_argument("--edge-id-column", default="edge_id")
    parser.add_argument("--relation-column", default="relation")
    args = parser.parse_args()

    if args.output_dir.exists() and any(args.output_dir.iterdir()):
        raise SystemExit(f"Output directory is not empty: {args.output_dir}")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    node_rows = read_csv(args.nodes)
    edge_rows = read_csv(args.edges)
    node_map = {row[args.node_id_column]: row for row in node_rows}
    if len(node_map) != len(node_rows):
        raise SystemExit("Node table contains duplicate node IDs")
    if args.root not in node_map:
        raise SystemExit(f"Root is absent from node table: {args.root}")

    adjacency: dict[str, list[tuple[str, float, str, str]]] = defaultdict(list)
    for index, row in enumerate(edge_rows, 1):
        source = row[args.source_column]
        target = row[args.target_column]
        if source not in node_map or target not in node_map:
            raise SystemExit(
                f"Edge {index} references an unknown endpoint: {source} -> {target}"
            )
        weight = float(row[args.weight_column])
        if not math.isfinite(weight) or weight < 0:
            raise SystemExit(f"Edge {index} has an invalid Dijkstra cost: {weight}")
        edge_id = row.get(args.edge_id_column, "") or f"edge_{index:06d}"
        relation = row.get(args.relation_column, "")
        adjacency[source].append((target, weight, edge_id, relation))

    distance = {args.root: 0.0}
    previous: dict[str, tuple[str, float, str, str]] = {}
    queue = [(0.0, args.root)]
    while queue:
        current, node = heapq.heappop(queue)
        if current > distance[node] + 1e-12:
            continue
        for target, weight, edge_id, relation in adjacency.get(node, []):
            proposal = current + weight
            if proposal + 1e-12 < distance.get(target, math.inf):
                distance[target] = proposal
                previous[target] = (node, weight, edge_id, relation)
                heapq.heappush(queue, (proposal, target))

    ranked_nodes = sorted(node_map, key=lambda node: (distance.get(node, math.inf), node))
    output_rows = []
    for rank, node in enumerate(ranked_nodes, 1):
        reachable = node in distance
        path_nodes = [node]
        path_weights: list[float] = []
        path_edges: list[str] = []
        path_relations: list[str] = []
        cursor = node
        while reachable and cursor != args.root:
            parent, weight, edge_id, relation = previous[cursor]
            path_nodes.append(parent)
            path_weights.append(weight)
            path_edges.append(edge_id)
            path_relations.append(relation)
            cursor = parent
        path_nodes.reverse()
        path_weights.reverse()
        path_edges.reverse()
        path_relations.reverse()
        recomputed = sum(path_weights) if reachable else ""
        if reachable and abs(float(distance[node]) - float(recomputed)) > 1e-9:
            raise SystemExit(f"Path reconstruction failed for {node}")
        metadata = node_map[node]
        output_rows.append({
            "rank": rank, "node_id": node,
            "node_type": metadata.get(args.node_type_column, ""),
            "label": metadata.get(args.label_column, ""),
            "reachable": "yes" if reachable else "no",
            "dijkstra_distance": round(distance[node], 12) if reachable else "",
            "path_nodes": " -> ".join(path_nodes) if reachable else "",
            "path_edge_ids": " -> ".join(path_edges),
            "path_relations": " -> ".join(path_relations),
            "path_weights": " + ".join(f"{value:.12g}" for value in path_weights),
            "path_cost_recomputed": round(float(recomputed), 12) if reachable else "",
        })

    write_csv(args.output_dir / "dijkstra_shortest_paths.csv", output_rows)
    reachable_count = sum(row["reachable"] == "yes" for row in output_rows)
    report = [
        "# Dijkstra Run Report", "",
        f"- root: `{args.root}`",
        f"- nodes: {len(node_rows)}",
        f"- directed weighted edges: {len(edge_rows)}",
        f"- reachable nodes: {reachable_count}",
        f"- unreachable nodes: {len(node_rows) - reachable_count}",
        "- root distance: 0",
        "", "Distances are navigation costs, not claim evidence or citation proof.",
    ]
    (args.output_dir / "dijkstra_run_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"nodes={len(node_rows)} edges={len(edge_rows)} reachable={reachable_count}")


if __name__ == "__main__":
    main()
