#!/usr/bin/env python3
"""Build the public SPS case summary and historical SOL comparison tables."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPS = ROOT / "sps"
RUNS = SPS / "runs"
SOL_RUN = RUNS / "gpt-5.6-sol-xhigh-matched"
GOAL_RUN = RUNS / "codex-goal-mode-full-dijkstra-rerun-20260716"
OUT_CSV = SPS / "comparison" / "sol_xhigh_vs_goal_full_rerun_20260716.csv"
OUT_MD = SPS / "comparison" / "sol_xhigh_vs_goal_full_rerun_20260716.md"


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    sol = json.loads((SOL_RUN / "run_metrics.json").read_text(encoding="utf-8"))
    protocol = read_csv(GOAL_RUN / "search_protocol.csv")
    probes = read_csv(GOAL_RUN / "identifier_probes.csv")
    retrieval = read_csv(GOAL_RUN / "retrieval_log_all_rounds.csv")
    route_records = read_csv(GOAL_RUN / "route_results.csv")
    screened = read_csv(GOAL_RUN / "candidate_screening_table.csv")
    selected = read_csv(GOAL_RUN / "selected_fulltexts.csv")
    sources = read_csv(GOAL_RUN / "source_matrix.csv")
    c4 = read_csv(GOAL_RUN / "c4_reading_notes.psv", delimiter="|")
    evidence = read_csv(GOAL_RUN / "evidence_registry.csv")
    claims = read_csv(GOAL_RUN / "claim_source_ledger.csv")
    relations = read_csv(GOAL_RUN / "relation_ledger.csv")
    visual = read_csv(GOAL_RUN / "visual_source_audit.csv")
    nodes = read_csv(GOAL_RUN / "dijkstra_graph_nodes.csv")
    edges = read_csv(GOAL_RUN / "dijkstra_graph_edges.csv")
    replay = {row["budget_papers"]: row for row in read_csv(GOAL_RUN / "dijkstra_selection_comparison.csv")}
    snapshots = {row["snapshot_id"]: row for row in read_csv(GOAL_RUN / "goal_usage_snapshots.csv")}
    validation = json.loads((GOAL_RUN / "final_validation_report.json").read_text(encoding="utf-8"))

    start = snapshots["S00"]
    finish = snapshots["S02"]
    elapsed_delta = int(finish["goal_time_seconds"]) - int(start["goal_time_seconds"])
    token_delta = int(finish["goal_tokens_used"]) - int(start["goal_tokens_used"])
    direct = [row for row in relations if row["relation_type"] == "direct_citation"]
    active = [row for row in screened if row["decision"] in {"include", "candidate"}]
    page_total = sum(int(row["pdf_pages"]) for row in sources)
    passed_checks = sum(row["status"] == "PASS" for row in validation["checks"])
    budget20 = replay["20"]

    comparison = [
        {
            "metric": "Runtime identity",
            "gpt_5_6_sol_xhigh": "gpt-5.6-sol; xhigh; confirmed",
            "goal_full_rerun_20260716": "Codex Goal mode; deployment model and effort not exposed",
            "comparison_status": "Configuration description only",
        },
        {
            "metric": "Search contract",
            "gpt_5_6_sol_xhigh": f"{sol['routes']['fresh_queries']} fresh + {sol['routes']['legacy_concept_queries_executed']} fixed legacy routes",
            "goal_full_rerun_20260716": f"{len(protocol)} L0-L10 queries + {len(probes)} identifier probes; all freshly retrieved",
            "comparison_status": "Different route definitions",
        },
        {
            "metric": "Recorded elapsed time",
            "gpt_5_6_sol_xhigh": f"{sol['timing']['elapsed_seconds']} s (22 min 25 s)",
            "goal_full_rerun_20260716": f"{elapsed_delta} s (49 min 17 s), S00-S02 Goal-counter delta",
            "comparison_status": "Not a speed benchmark; contracts differ",
        },
        {
            "metric": "Recorded tokens",
            "gpt_5_6_sol_xhigh": "Unavailable",
            "goal_full_rerun_20260716": f"{token_delta:,} Goal-counter delta",
            "comparison_status": "No token or price comparison possible",
        },
        {
            "metric": "Deduplicated candidates",
            "gpt_5_6_sol_xhigh": str(sol["coverage"]["deduplicated_route_candidates"]),
            "goal_full_rerun_20260716": str(len(screened)),
            "comparison_status": "Reflects query scope, not model quality",
        },
        {
            "metric": "C3/full-text sources",
            "gpt_5_6_sol_xhigh": f"{sol['coverage']['source_verified_records']} PDFs / {sol['coverage']['local_pdf_pages']} pages",
            "goal_full_rerun_20260716": f"{len(sources)} PDFs / {page_total} pages",
            "comparison_status": "Different reading plans",
        },
        {
            "metric": "Deep reading records",
            "gpt_5_6_sol_xhigh": f"{sol['coverage']['four_dimension_reading_records']} four-dimension records",
            "goal_full_rerun_20260716": f"{len(c4)} C4 claim-anchored records",
            "comparison_status": "Different depth schema",
        },
        {
            "metric": "Evidence / claim rows",
            "gpt_5_6_sol_xhigh": f"{sol['ledgers']['evidence_records']} / {sol['ledgers']['claims']}",
            "goal_full_rerun_20260716": f"{len(evidence)} / {len(claims)}",
            "comparison_status": "Counts follow different output contracts",
        },
        {
            "metric": "Checked direct-citation edges",
            "gpt_5_6_sol_xhigh": str(sol["ledgers"]["direct_citation_edges"]),
            "goal_full_rerun_20260716": str(len(direct)),
            "comparison_status": "Whole-root screen versus selected C4 lineage",
        },
        {
            "metric": "Executable Dijkstra",
            "gpt_5_6_sol_xhigh": "Not part of this run",
            "goal_full_rerun_20260716": f"{len(nodes)} nodes / {len(edges)} edges; budget 20: {budget20['dijkstra_C4_anchors']} vs {budget20['screen_C4_anchors']} C4 anchors",
            "comparison_status": "Current-run navigation diagnostic only",
        },
        {
            "metric": "Key visual source pages",
            "gpt_5_6_sol_xhigh": "Not recorded in run metrics",
            "goal_full_rerun_20260716": str(len(visual)),
            "comparison_status": "Current-run audit feature",
        },
        {
            "metric": "Final validation",
            "gpt_5_6_sol_xhigh": sol["validation"]["final_package"],
            "goal_full_rerun_20260716": f"{validation['overall']} ({passed_checks}/{len(validation['checks'])} checks)",
            "comparison_status": "Both completed their own declared contracts",
        },
    ]
    fields = ["metric", "gpt_5_6_sol_xhigh", "goal_full_rerun_20260716", "comparison_status"]
    write_csv(OUT_CSV, comparison, fields)

    summary = [
        ("Target identity", "arXiv:2606.13790v1; title, authors, and date confirmed by Q01/Q02/P01", "root_identity_check.csv"),
        ("Fresh retrieval", f"{len(retrieval)}/{len(protocol) + len(probes)} routes succeeded", "retrieval_log_all_rounds.csv"),
        ("Candidate funnel", f"{len(route_records)} raw route records -> {len(screened)} unique -> {len(active)} active C0-C2 records", "candidate_screening_table.csv"),
        ("Source gate", f"{len(sources)}/{len(selected)} PDFs passed C3; {page_total} verified pages", "source_matrix.csv"),
        ("Claim gate", f"{len(c4)}/{sum(row['target_level'] == 'C4' for row in selected)} planned core papers reached C4", "c4_reading_notes.psv"),
        ("Audit package", f"{len(evidence)} evidence rows; {len(claims)} claim rows; {len(direct)} direct citations; {len(visual)} visual source pages", "evidence_registry.csv; claim_source_ledger.csv"),
        ("Dijkstra replay", f"{len(nodes)} nodes / {len(edges)} edges; at budget 20, {budget20['dijkstra_C4_anchors']} C4 anchors versus {budget20['screen_C4_anchors']}", "dijkstra_selection_comparison.csv"),
        ("Validation", f"{validation['overall']}: {passed_checks}/{len(validation['checks'])} checks", "final_validation_report.md"),
        ("Observed run delta", f"{elapsed_delta} s; {token_delta:,} Goal-counter tokens", "runtime_accounting.md"),
    ]

    lines = [
        "# SPS Part 1: Case Summary and Historical SOL Comparison",
        "",
        "This page reports the 2026-07-16 fresh Goal-mode rerun and places it beside the earlier identified `gpt-5.6-sol/xhigh` run.",
        "The two runs did **not** use the same search and reading contract, so the second table is a protocol-aware historical comparison, not a model leaderboard.",
        "",
        "## 2026-07-16 case summary",
        "",
        "| Stage | Result | Source artifact |",
        "|---|---|---|",
    ]
    for stage, result, source in summary:
        lines.append(f"| {stage} | {result} | `{source}` |")
    lines += [
        "",
        "The safe conclusion is that this run produced a complete, auditable SPS Part 1 package under its declared scope. It does not establish universal literature completeness or a cost advantage for SPS.",
        "",
        "## Earlier SOL run versus the fresh Goal rerun",
        "",
        "| Metric | `gpt-5.6-sol/xhigh` (earlier) | Goal-mode full rerun (2026-07-16) | How to read it |",
        "|---|---|---|---|",
    ]
    for row in comparison:
        lines.append(
            f"| {row['metric']} | {row['gpt_5_6_sol_xhigh']} | "
            f"{row['goal_full_rerun_20260716']} | {row['comparison_status']} |"
        )
    lines += [
        "",
        "## What this comparison supports",
        "",
        "- The earlier SOL run covered and read a larger pool under its broader frozen contract.",
        "- The fresh Goal rerun added explicit C0-C4 gates, freshly hashed route artifacts, key source-page screenshots, an executable Dijkstra replay, and a declared stopping record.",
        "- Both runs passed their own validators. Because the contracts and exposed runtime metadata differ, neither result establishes that one model is better or cheaper.",
        "",
        "A strict model comparison requires one frozen contract, explicit model and reasoning identifiers, start/stop usage counters, and at least three independent repetitions per configuration.",
        "",
        "## Sources",
        "",
        "- [`gpt-5.6-sol/xhigh` run metrics](../runs/gpt-5.6-sol-xhigh-matched/run_metrics.json)",
        "- [Fresh Goal rerun report](../runs/codex-goal-mode-full-dijkstra-rerun-20260716/run_report.md)",
        "- [Fresh Goal rerun validation](../runs/codex-goal-mode-full-dijkstra-rerun-20260716/final_validation_report.md)",
        "- [Fresh Goal rerun runtime boundary](../runs/codex-goal-mode-full-dijkstra-rerun-20260716/runtime_accounting.md)",
        "- [Machine-readable comparison table](sol_xhigh_vs_goal_full_rerun_20260716.csv)",
        "- [Matched ordinary-run versus Goal-mode comparison](cost_effect_summary.md)",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_CSV.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
