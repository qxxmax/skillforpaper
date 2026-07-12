#!/usr/bin/env python3
"""Render separate landscape, lineage, and audit-funnel literature views."""

from __future__ import annotations

import argparse
import csv
import os
import textwrap
from collections import defaultdict
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-cache")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx


NODE_FIELDS = {
    "NodeID", "Title", "Year", "ShortLabel", "PrimaryDisplayCluster",
    "AllTopicLabels", "EvidenceLevel", "SourceRelation", "ReadingPriority",
    "SourceURL", "PublicGraphStatus",
}
RELATION_FIELDS = {
    "EdgeID", "SourceID", "TargetID", "EdgeType", "DirectlyCited",
    "EvidenceID", "RelationBasis", "Confidence", "HumanReviewStatus",
    "PublicGraphStatus",
}
FUNNEL_FIELDS = {"Stage", "Count", "Meaning", "SourceTable", "DeduplicationKey", "Filter"}

PALETTE = ["#4169A1", "#D05A47", "#3E8B72", "#C28A2B", "#7A5CA8", "#5C667A", "#B65F8E"]
MARKERS = {"metadata": "o", "abstract": "s", "full_text": "D", "claim_anchored": "*"}
LINE_STYLES = {
    "direct_citation": "solid",
    "forward_citation": "solid",
    "method_precedent": "dashed",
    "method_extension": "dashed",
    "baseline_comparison": "dashdot",
    "shared_benchmark": "dashdot",
    "same_author_context": "dotted",
    "conceptual_neighbor": "dotted",
    "external_historical_relation": "dashed",
}


def read_csv(path: Path, required: set[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path}: missing columns {sorted(missing)}")
        return list(reader)


def save(fig: plt.Figure, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    png_path = output.with_suffix(".png")
    pdf_path = output.with_suffix(".pdf")
    fig.savefig(png_path, dpi=220, bbox_inches="tight", facecolor="white")
    fig.savefig(pdf_path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    missing = [str(path) for path in (png_path, pdf_path) if not path.exists()]
    if missing:
        raise RuntimeError(f"renderer reported success but files are missing: {missing}")
    print(f"rendered {png_path} and {pdf_path}")


def public_nodes(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in rows if row["PublicGraphStatus"].strip().lower() == "show"]


def cluster_colors(nodes: list[dict[str, str]]) -> dict[str, str]:
    clusters = sorted({row["PrimaryDisplayCluster"].strip() or "unclassified" for row in nodes})
    return {cluster: PALETTE[index % len(PALETTE)] for index, cluster in enumerate(clusters)}


def branch_positions(nodes: list[dict[str, str]], cluster_gap: float = 2.2) -> tuple[dict[str, tuple[float, float]], list[str]]:
    clusters = sorted({row["PrimaryDisplayCluster"].strip() or "unclassified" for row in nodes})
    y_for = {cluster: index * cluster_gap for index, cluster in enumerate(clusters)}
    grouped: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for row in nodes:
        grouped[row["PrimaryDisplayCluster"].strip() or "unclassified"].append(row)
    positions: dict[str, tuple[float, float]] = {}
    lane_pattern = [-0.48, 0.0, 0.48, -0.24, 0.24]
    for cluster, rows in grouped.items():
        ordered = sorted(rows, key=lambda row: (int(row["Year"]), row["NodeID"]))
        same_year_seen: defaultdict[int, int] = defaultdict(int)
        for index, row in enumerate(ordered):
            year = int(row["Year"])
            year_offset = same_year_seen[year]
            same_year_seen[year] += 1
            positions[row["NodeID"]] = (
                year + 0.16 * year_offset,
                y_for[cluster] + lane_pattern[index % len(lane_pattern)],
            )
    return positions, clusters


def add_offset_labels(ax: plt.Axes, nodes: list[dict[str, str]], positions: dict[str, tuple[float, float]]) -> None:
    for index, row in enumerate(sorted(nodes, key=lambda item: item["NodeID"])):
        x, y = positions[row["NodeID"]]
        vertical = 8 if index % 2 == 0 else -14
        ax.annotate(
            textwrap.fill(row["ShortLabel"], 14), (x, y), xytext=(7, vertical),
            textcoords="offset points", fontsize=7.4, ha="left",
            va="bottom" if vertical > 0 else "top",
            bbox={"boxstyle": "square,pad=0.12", "facecolor": "white", "edgecolor": "none", "alpha": 0.82},
            zorder=5,
        )


def render_landscape(nodes: list[dict[str, str]], output_dir: Path) -> None:
    nodes = public_nodes(nodes)
    colors = cluster_colors(nodes)
    positions, clusters = branch_positions(nodes)
    fig, ax = plt.subplots(figsize=(14.2, max(7.0, 0.72 * len(clusters) + 3.0)))
    for row in sorted(nodes, key=lambda item: (int(item["Year"]), item["NodeID"])):
        cluster = row["PrimaryDisplayCluster"].strip() or "unclassified"
        x, y = positions[row["NodeID"]]
        marker = MARKERS.get(row["EvidenceLevel"].strip(), "o")
        size = 220 if row["ReadingPriority"].strip() == "P0" else 150
        ax.scatter(x, y, s=size, marker=marker, color=colors[cluster], edgecolor="#233047", linewidth=0.9)
    add_offset_labels(ax, nodes, positions)
    ax.set_yticks([index * 2.2 for index in range(len(clusters))], [cluster.replace("_", " ") for cluster in clusters])
    ax.set_xlabel("Publication year")
    ax.set_title("Literature landscape: topic coverage and reading depth", loc="left", weight="bold")
    ax.grid(axis="x", alpha=0.18)
    ax.spines[["top", "right", "left"]].set_visible(False)
    save(fig, output_dir / "landscape_map")


def render_lineage(nodes: list[dict[str, str]], relations: list[dict[str, str]], output_dir: Path) -> None:
    public = public_nodes(nodes)
    core = [row for row in public if row["ReadingPriority"].strip() == "P0"]
    shown_nodes = {row["NodeID"]: row for row in (core or public)}
    shown_edges = [
        row for row in relations
        if row["PublicGraphStatus"].strip().lower() == "show"
        and row["HumanReviewStatus"].strip().lower() == "reviewed"
        and row["SourceID"] in shown_nodes and row["TargetID"] in shown_nodes
    ]
    graph = nx.DiGraph()
    graph.add_nodes_from(shown_nodes)
    graph.add_edges_from((row["SourceID"], row["TargetID"], row) for row in shown_edges)
    colors = cluster_colors(list(shown_nodes.values()))
    node_rows = list(shown_nodes.values())
    positions, clusters = branch_positions(node_rows)
    roots = [row for row in node_rows if row["SourceRelation"].strip() == "root"]
    if roots:
        center_y = (len(clusters) - 1) * 2.2 / 2
        right_x = max(int(row["Year"]) for row in node_rows) + 1.8
        for row in roots:
            positions[row["NodeID"]] = (right_x, center_y)
    fig, ax = plt.subplots(figsize=(15.5, max(8.0, 0.72 * len(clusters) + 3.2)))
    for evidence, marker in MARKERS.items():
        subset = [node_id for node_id, row in shown_nodes.items() if row["EvidenceLevel"].strip() == evidence]
        if not subset:
            continue
        nx.draw_networkx_nodes(
            graph, positions, nodelist=subset, node_shape=marker,
            node_color=[colors[shown_nodes[node]["PrimaryDisplayCluster"]] for node in subset],
            edgecolors="#233047", linewidths=0.9, node_size=470 if marker != "*" else 720, ax=ax,
        )
    for edge_type in sorted({row["EdgeType"] for row in shown_edges}):
        subset = [(row["SourceID"], row["TargetID"]) for row in shown_edges if row["EdgeType"] == edge_type]
        nx.draw_networkx_edges(
            graph, positions, edgelist=subset, style=LINE_STYLES.get(edge_type, "dotted"),
            width=1.35, alpha=0.48, edge_color="#526079", arrows=True,
            arrowsize=14, connectionstyle="arc3,rad=0.08", ax=ax,
        )
    add_offset_labels(ax, node_rows, positions)
    ax.set_title("Checked citation and method lineage", loc="left", weight="bold")
    ax.set_xlabel("Publication year; solid = citation, dashed/dotted = declared non-citation relation")
    ax.set_yticks([index * 2.2 for index in range(len(clusters))], [cluster.replace("_", " ") for cluster in clusters])
    ax.grid(axis="x", alpha=0.15)
    ax.spines[["top", "right", "left"]].set_visible(False)
    save(fig, output_dir / "citation_lineage_graph")


def render_funnel(rows: list[dict[str, str]], output_dir: Path) -> None:
    counts = [int(row["Count"]) for row in rows]
    if any(count < 0 for count in counts):
        raise ValueError("audit funnel counts must be non-negative")
    fig, ax = plt.subplots(figsize=(10.8, max(4.8, 0.72 * len(rows) + 1.8)))
    y = list(range(len(rows)))
    bars = ax.barh(y, counts, color="#4169A1", alpha=0.9, height=0.58)
    ax.set_yticks(y, [row["Stage"].replace("_", " ") for row in rows])
    ax.invert_yaxis()
    for bar, row in zip(bars, rows):
        ax.text(bar.get_width() + max(counts or [1]) * 0.015, bar.get_y() + bar.get_height() / 2,
                f"{row['Count']}  {row['Meaning']}", va="center", fontsize=9)
    ax.set_title("Audit funnel: what was found, checked, and used", loc="left", weight="bold")
    ax.set_xlabel("Deduplicated records")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.grid(axis="x", alpha=0.18)
    save(fig, output_dir / "audit_funnel")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", type=Path, required=True)
    parser.add_argument("--relations", type=Path, required=True)
    parser.add_argument("--funnel-counts", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    nodes = read_csv(args.nodes, NODE_FIELDS)
    relations = read_csv(args.relations, RELATION_FIELDS)
    render_landscape(nodes, args.output_dir)
    render_lineage(nodes, relations, args.output_dir)
    if args.funnel_counts:
        render_funnel(read_csv(args.funnel_counts, FUNNEL_FIELDS), args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
