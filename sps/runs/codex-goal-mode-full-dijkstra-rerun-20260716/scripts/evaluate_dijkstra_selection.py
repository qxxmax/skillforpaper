#!/usr/bin/env python3
"""Compare current-run Dijkstra navigation with screen-only ordering."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    screened = [row for row in read_csv(run_dir / "candidate_screening_table.csv") if row["decision"] in {"include", "candidate"}]
    screened.sort(key=lambda row: int(row["screen_rank"]))
    selected = read_csv(run_dir / "selected_fulltexts.csv")
    c4_ids = {row["arxiv_id"] for row in selected if row["target_level"] == "C4"}
    c3_ids = {row["arxiv_id"] for row in selected}
    clusters = {row["arxiv_id"]: row["cluster"] for row in selected}
    direct_ids = {
        row["target_arxiv_id"] for row in read_csv(run_dir / "relation_ledger.csv")
        if row["relation_type"] == "direct_citation"
    }
    dijkstra_rows = [
        row for row in read_csv(run_dir / "dijkstra_computed" / "dijkstra_shortest_paths.csv")
        if row["node_type"] == "paper" and row["node_id"].startswith("paper:")
    ]
    dijkstra = []
    for paper_rank, row in enumerate(dijkstra_rows, 1):
        arxiv_id = row["node_id"].removeprefix("paper:")
        dijkstra.append({**row, "arxiv_id": arxiv_id, "paper_rank": paper_rank})
    dijkstra_by_id = {row["arxiv_id"]: row for row in dijkstra}
    screen_by_id = {row["arxiv_id"]: row for row in screened}

    two_pass = []
    for row in selected:
        did = dijkstra_by_id[row["arxiv_id"]]
        screen = screen_by_id[row["arxiv_id"]]
        two_pass.append({
            "arxiv_id": row["arxiv_id"],
            "title": row["title"],
            "target_level": row["target_level"],
            "cluster": row["cluster"],
            "screen_rank": screen["screen_rank"],
            "screen_score": screen["screen_score"],
            "dijkstra_paper_rank": did["paper_rank"],
            "dijkstra_distance": did["dijkstra_distance"],
            "path_relations": did["path_relations"],
            "path_cost_recomputed": did["path_cost_recomputed"],
            "interpretation": "Dijkstra distance is navigation metadata; source evidence remains in the C4 ledger.",
        })
    two_pass.sort(key=lambda row: int(row["dijkstra_paper_rank"]))
    write_csv(run_dir / "dijkstra_two_pass_comparison.csv", two_pass, list(two_pass[0]))

    budgets = (5, 10, 20, 40, 60)
    metric_rows = []
    for budget in budgets:
        dijkstra_ids = {row["arxiv_id"] for row in dijkstra[:budget]}
        screen_ids = {row["arxiv_id"] for row in screened[:budget]}
        for method, ids in (("dijkstra", dijkstra_ids), ("screen_only", screen_ids)):
            metric_rows.append({
                "budget_papers": budget,
                "method": method,
                "C4_anchors_found": len(ids & c4_ids),
                "C4_anchor_recall": round(len(ids & c4_ids) / len(c4_ids), 6),
                "C3_fulltexts_found": len(ids & c3_ids),
                "C3_fulltext_recall": round(len(ids & c3_ids) / len(c3_ids), 6),
                "direct_citations_found": len(ids & direct_ids),
                "direct_citation_recall": round(len(ids & direct_ids) / len(direct_ids), 6),
                "selected_clusters_found": len({clusters[item] for item in ids if item in clusters}),
            })
    write_csv(run_dir / "dijkstra_effect_metrics.csv", metric_rows, list(metric_rows[0]))
    comparison_rows = []
    for budget in budgets:
        d = next(row for row in metric_rows if row["budget_papers"] == budget and row["method"] == "dijkstra")
        s = next(row for row in metric_rows if row["budget_papers"] == budget and row["method"] == "screen_only")
        comparison_rows.append({
            "budget_papers": budget,
            "dijkstra_C4_anchors": d["C4_anchors_found"],
            "screen_C4_anchors": s["C4_anchors_found"],
            "dijkstra_C3_fulltexts": d["C3_fulltexts_found"],
            "screen_C3_fulltexts": s["C3_fulltexts_found"],
            "dijkstra_direct_citations": d["direct_citations_found"],
            "screen_direct_citations": s["direct_citations_found"],
            "dijkstra_clusters": d["selected_clusters_found"],
            "screen_clusters": s["selected_clusters_found"],
        })
    write_csv(run_dir / "dijkstra_selection_comparison.csv", comparison_rows, list(comparison_rows[0]))
    lines = [
        "# Dijkstra Navigation Evaluation",
        "",
        "The two rankings use the same screened candidate pool. Dijkstra uses only declared",
        "search-route, citation, author, and method edges. The screen-only comparator uses",
        "the C0-C2 screen order. The target set is the current run's predeclared 21-PDF reading",
        "plan, so this is a workflow replay diagnostic rather than a general performance claim.",
        "",
        "| budget | Dijkstra C4 | screen C4 | Dijkstra C3 | screen C3 | Dijkstra cited | screen cited |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in comparison_rows:
        lines.append(
            f"| {row['budget_papers']} | {row['dijkstra_C4_anchors']} | {row['screen_C4_anchors']} | "
            f"{row['dijkstra_C3_fulltexts']} | {row['screen_C3_fulltexts']} | "
            f"{row['dijkstra_direct_citations']} | {row['screen_direct_citations']} |"
        )
    lines += [
        "",
        "## Interpretation boundary",
        "",
        "A shorter Dijkstra path shows that the declared graph reaches a record cheaply. It does",
        "not verify a method claim, establish causal influence, or measure scientific quality.",
    ]
    (run_dir / "dijkstra_effect_evaluation.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"paper_nodes={len(dijkstra)} budgets={len(budgets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
