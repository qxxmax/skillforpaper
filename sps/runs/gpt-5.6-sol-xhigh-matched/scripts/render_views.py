#!/usr/bin/env python3
"""Render deterministic landscape, lineage, audit, and author views."""

from __future__ import annotations

import csv
import math
import re
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "graphs"
OUT.mkdir(exist_ok=True)

COLORS = {
    "flow": "#277DA1", "gauge_flow": "#43AA8B", "fermion_flow": "#4D908E",
    "multimodal_flow": "#90BE6D", "continuous_flow": "#577590",
    "path_sampler": "#F9C74F", "stochastic_flow": "#F9844A", "lft_diffusion": "#9B5DE5",
    "gauge_diffusion": "#7B2CBF", "complex_diffusion": "#B56576", "autoregressive": "#F3722C",
    "topology": "#2A9D8F", "multiscale": "#E76F51", "diagnostics": "#6D6875",
    "adversarial": "#D62828", "root_sps": "#111827", "transfer_diffusion": "#00A6A6",
}


def load(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def save(fig, stem: str) -> None:
    fig.savefig(OUT / f"{stem}.png", dpi=220, bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def landscape(papers: list[dict[str, str]]) -> None:
    clusters = sorted({p["Cluster"] for p in papers})
    ypos = {cluster: i for i, cluster in enumerate(clusters)}
    fig, ax = plt.subplots(figsize=(14, 8))
    offsets = Counter()
    for paper in papers:
        cluster = paper["Cluster"]
        year = int(paper["Year"])
        jitter = (offsets[(year, cluster)] % 5 - 2) * 0.065
        offsets[(year, cluster)] += 1
        size = 260 if paper["SourceRelation"] == "root" else (150 if paper["SourceRelation"] == "external_addition" else 90)
        marker = "*" if paper["SourceRelation"] == "root" else ("D" if paper["SourceRelation"] == "external_addition" else "o")
        ax.scatter(year, ypos[cluster] + jitter, s=size, marker=marker, color=COLORS.get(cluster, "#64748B"), edgecolor="white", linewidth=0.9, zorder=3)
        if paper["SourceRelation"] in {"root", "external_addition"} or paper["ArxivID"] in {"2111.15141", "2302.13834", "2410.02711", "2107.00734"}:
            label = "SPS" if paper["SourceRelation"] == "root" else paper["ArxivID"]
            ax.annotate(label, (year, ypos[cluster] + jitter), xytext=(5, 5), textcoords="offset points", fontsize=8, weight="bold" if paper["SourceRelation"] == "root" else "normal")
    ax.set_yticks(range(len(clusters)), [c.replace("_", " ") for c in clusters])
    ax.set_xticks(range(2019, 2027))
    ax.set_xlim(2018.6, 2026.5)
    ax.grid(axis="x", color="#D1D5DB", linewidth=0.7)
    ax.set_title("SPS literature landscape: method families and evidence additions", loc="left", fontsize=17, weight="bold", pad=30)
    ax.text(0, 1.008, "Circle: root bibliography full text   Diamond: closure addition   Star: SPS root", transform=ax.transAxes, fontsize=10, color="#374151")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_xlabel("Publication year")
    fig.tight_layout()
    save(fig, "landscape_map")


def lineage(papers: list[dict[str, str]]) -> None:
    selected_ids = ["1904.12072", "2201.08862", "2111.15141", "2302.13834", "2410.02711", "2604.10209", "2605.12597", "2606.13790", "2607.08505"]
    paper = {p["ArxivID"]: p for p in papers}
    positions = {
        "1904.12072": (2019, 2.7), "2201.08862": (2022, 2.7),
        "2111.15141": (2022, 1.7), "2302.13834": (2023, 1.7), "2410.02711": (2024, 1.7),
        "2604.10209": (2026, 3.6), "2605.12597": (2026, 0.4), "2606.13790": (2026, 2.2), "2607.08505": (2026, 4.5),
    }
    edges = [
        ("1904.12072", "2201.08862", "flow to stochastic flow", False),
        ("2111.15141", "2302.13834", "path-space control", False),
        ("2111.15141", "2606.13790", "root citation", False),
        ("2302.13834", "2606.13790", "root citation", False),
        ("2201.08862", "2606.13790", "root citation", False),
        ("2410.02711", "2606.13790", "root citation", False),
        ("2604.10209", "2606.13790", "external comparison", True),
        ("2605.12597", "2606.13790", "adversarial", True),
        ("2607.08505", "2606.13790", "post-root comparison", True),
    ]
    fig, ax = plt.subplots(figsize=(14, 7.5))
    for src, dst, label, dashed in edges:
        x1, y1 = positions[src]; x2, y2 = positions[dst]
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops={"arrowstyle": "->", "color": "#6B7280", "lw": 1.2, "linestyle": "--" if dashed else "-", "connectionstyle": "arc3,rad=0.08"})
    for arxiv_id in selected_ids:
        p = paper[arxiv_id]
        x, y = positions[arxiv_id]
        color = COLORS.get(p["Cluster"], "#64748B")
        ax.scatter(x, y, s=470 if arxiv_id == "2606.13790" else 250, color=color, edgecolor="white", linewidth=1.3, zorder=4)
        short = "SPS\n2606.13790" if arxiv_id == "2606.13790" else arxiv_id
        ax.text(x, y - 0.23, short, ha="center", va="top", fontsize=9, weight="bold" if arxiv_id == "2606.13790" else "normal")
    ax.text(2024.7, 4.82, "Dashed edges: external conceptual/reviewer comparisons, not direct citations", fontsize=9, color="#374151")
    ax.set_xlim(2018.5, 2026.7); ax.set_ylim(-0.1, 5.1)
    ax.set_xticks(range(2019, 2027)); ax.set_yticks([])
    ax.grid(axis="x", color="#E5E7EB")
    ax.set_title("Citation lineage and reviewer-critical external additions", loc="left", fontsize=17, weight="bold")
    ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
    fig.tight_layout()
    save(fig, "citation_lineage_graph")


def funnel() -> None:
    rows = load("audit_funnel_counts.csv")
    labels = [r["Stage"].replace("_", " ") for r in rows]
    values = [int(r["Count"]) for r in rows]
    colors = ["#277DA1", "#43AA8B", "#F9C74F", "#F9844A", "#9B5DE5"]
    fig, ax = plt.subplots(figsize=(12, 6.8))
    bars = ax.barh(labels[::-1], values[::-1], color=colors[::-1], height=0.58)
    for bar, value in zip(bars, values[::-1]):
        ax.text(bar.get_width() + max(values)*0.012, bar.get_y()+bar.get_height()/2, f"{value:,}", va="center", fontsize=11, weight="bold")
    ax.set_xlim(0, max(values)*1.16)
    ax.set_title("Fresh-run audit funnel", loc="left", fontsize=17, weight="bold", pad=30)
    ax.text(0, 1.008, "Counts reproduce from deduplicated source tables; stages are not a single monotone subset chain.", transform=ax.transAxes, fontsize=10, color="#374151")
    ax.grid(axis="x", color="#E5E7EB")
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.set_xlabel("Records")
    fig.tight_layout()
    save(fig, "audit_funnel")


def author_graph(papers: list[dict[str, str]]) -> None:
    root_authors = {"Shiyang Chen", "Moxian Qian", "Gert Aarts", "Biagio Lucini", "Kai Zhou"}
    graph = nx.Graph()
    for p in papers:
        authors = [a.strip() for a in re.split(r"\s+and\s+", p["Authors"]) if a.strip()]
        keep = [a for a in authors if a in root_authors]
        if not keep:
            continue
        graph.add_node(p["PaperID"], kind="paper", label="SPS" if p["PaperID"] == "P_ROOT" else p["ArxivID"])
        for author in keep:
            graph.add_node(author, kind="author", label=author)
            graph.add_edge(author, p["PaperID"])
    pos = nx.spring_layout(graph, seed=19, k=1.15)
    fig, ax = plt.subplots(figsize=(13, 9))
    author_nodes = [n for n,d in graph.nodes(data=True) if d["kind"] == "author"]
    paper_nodes = [n for n,d in graph.nodes(data=True) if d["kind"] == "paper"]
    nx.draw_networkx_edges(graph, pos, ax=ax, edge_color="#CBD5E1", width=1.0)
    nx.draw_networkx_nodes(graph, pos, nodelist=paper_nodes, node_color="#277DA1", node_size=430, ax=ax, edgecolors="white")
    nx.draw_networkx_nodes(graph, pos, nodelist=author_nodes, node_color="#F9C74F", node_size=1100, ax=ax, node_shape="s", edgecolors="white")
    labels = {n:d["label"] for n,d in graph.nodes(data=True)}
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=8, ax=ax)
    ax.set_title("SPS author and collaborator full-text graph", loc="left", fontsize=17, weight="bold")
    ax.text(0, 0.99, "Edges denote shared authorship only; they do not imply method ancestry.", transform=ax.transAxes, fontsize=10, color="#374151")
    ax.axis("off")
    fig.tight_layout()
    save(fig, "author_collaboration_graph")


def main() -> None:
    papers = load("source_matrix.csv")
    landscape(papers)
    lineage(papers)
    funnel()
    author_graph(papers)


if __name__ == "__main__":
    main()
