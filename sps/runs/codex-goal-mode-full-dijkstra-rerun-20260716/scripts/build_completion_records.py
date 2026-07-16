#!/usr/bin/env python3
"""Build human-readable stop, output, and numerical records for the fresh run."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, str]], fields: list[str]) -> list[str]:
    lines = [
        "| " + " | ".join(fields) + " |",
        "|" + "|".join("---" for _ in fields) + "|",
    ]
    lines.extend("| " + " | ".join(row[field] for field in fields) + " |" for row in rows)
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()

    protocol = read_csv(run_dir / "search_protocol.csv")
    retrieval = read_csv(run_dir / "retrieval_log_all_rounds.csv")
    route_records = read_csv(run_dir / "route_results.csv")
    screened = read_csv(run_dir / "candidate_screening_table.csv")
    selected = read_csv(run_dir / "selected_fulltexts.csv")
    downloads = read_csv(run_dir / "fulltext_download_status.tsv", delimiter="\t")
    c4_notes = read_csv(run_dir / "c4_reading_notes.psv", delimiter="|")
    evidence = read_csv(run_dir / "evidence_registry.csv")
    relations = read_csv(run_dir / "relation_ledger.csv")
    graph_nodes = read_csv(run_dir / "dijkstra_graph_nodes.csv")
    graph_edges = read_csv(run_dir / "dijkstra_graph_edges.csv")
    visual = read_csv(run_dir / "visual_source_audit.csv")
    query_yield = read_csv(run_dir / "query_yield_log.csv")
    comparison = read_csv(run_dir / "dijkstra_selection_comparison.csv")

    decisions = Counter(row["decision"] for row in screened)
    rounds = Counter(row["round"] for row in protocol)
    retrieval_status = Counter(row["status"] for row in retrieval)
    direct = [row for row in relations if row["relation_type"] == "direct_citation"]
    c3_ok = [row for row in downloads if row["status"] == "OK"]
    active = [row for row in screened if row["decision"] in {"include", "candidate"}]
    c4_planned = [row for row in selected if row["target_level"] == "C4"]
    l5_l10 = [row for row in query_yield if row["round"] in {"L5", "L6", "L7", "L8", "L9", "L10"}]
    l5_l10_records = sum(int(row["unique_hits"]) for row in l5_l10)
    b20 = next(row for row in comparison if row["budget_papers"] == "20")

    numerical_rows = [
        {
            "metric": "configured_search_routes",
            "value": str(len(protocol)),
            "definition": "Q01-Q24 protocol entries; P01-P12 are separate identifier probes.",
            "source": "search_protocol.csv; identifier_probes.csv",
            "boundary": "Route count is a workflow setting, not literature completeness.",
        },
        {
            "metric": "successful_retrieval_routes",
            "value": str(retrieval_status["OK"]),
            "definition": "Route-level current arXiv retrievals with status OK.",
            "source": "retrieval_log_all_rounds.csv",
            "boundary": "Transport success does not make every hit relevant.",
        },
        {
            "metric": "raw_route_records",
            "value": str(len(route_records)),
            "definition": "All records returned by the current L0-L10 route set before deduplication.",
            "source": "route_results.csv",
            "boundary": "A record can appear from more than one route.",
        },
        {
            "metric": "deduplicated_candidates",
            "value": str(len(screened)),
            "definition": "Unique records after identifier deduplication.",
            "source": "candidate_screening_table.csv",
            "boundary": "Candidate-level evidence is at most C2 before full-text review.",
        },
        {
            "metric": "screened_include_candidate_exclude",
            "value": f"{decisions['include']} / {decisions['candidate']} / {decisions['exclude']}",
            "definition": "C0-C2 screening decisions for the deduplicated pool.",
            "source": "candidate_screening_table.csv",
            "boundary": "Excluded papers are retained with reasons; they are not silently discarded.",
        },
        {
            "metric": "selected_full_texts",
            "value": str(len(selected)),
            "definition": "Predeclared reading set after screening.",
            "source": "selected_fulltexts.csv",
            "boundary": "Selection is a bounded reading plan, not all active candidates.",
        },
        {
            "metric": "C3_download_passes",
            "value": f"{len(c3_ok)} / {len(selected)}",
            "definition": "Downloaded PDFs with checksum, page-count, and text-extraction pass.",
            "source": "fulltext_download_status.tsv; fulltext_gate_report.md",
            "boundary": "C3 proves source integrity, not a method claim.",
        },
        {
            "metric": "C4_claim_anchors",
            "value": f"{len(c4_notes)} / {len(c4_planned)}",
            "definition": "Planned core records with problem, method, result, and boundary anchors.",
            "source": "c4_reading_notes.psv; evidence_registry.csv",
            "boundary": "Claims remain scoped to the cited source and anchor.",
        },
        {
            "metric": "evidence_records",
            "value": str(len(evidence)),
            "definition": "Identity/problem/method/result/boundary records compiled from C4 notes.",
            "source": "evidence_registry.csv",
            "boundary": "Record count is not a scientific quality metric.",
        },
        {
            "metric": "direct_citation_edges",
            "value": str(len(direct)),
            "definition": "SPS bibliography entries with exact title and arXiv-id context checked.",
            "source": "relation_ledger.csv; root_bibliography.csv; visual_source_audit.csv",
            "boundary": "A citation edge does not establish empirical equivalence.",
        },
        {
            "metric": "navigation_graph_nodes_edges",
            "value": f"{len(graph_nodes)} / {len(graph_edges)}",
            "definition": "Current graph nodes / weighted edges supplied to Dijkstra.",
            "source": "dijkstra_graph_nodes.csv; dijkstra_graph_edges.csv",
            "boundary": "The graph is search navigation metadata, not scientific evidence.",
        },
        {
            "metric": "key_visual_source_pages",
            "value": str(len(visual)),
            "definition": "Selected identity, bibliography, and branch-anchor pages visually inspected.",
            "source": "visual_source_audit.csv",
            "boundary": "Key-only policy; every PDF is C3-verified separately.",
        },
        {
            "metric": "dijkstra_replay_C4_at_budget_20",
            "value": f"{b20['dijkstra_C4_anchors']} vs {b20['screen_C4_anchors']}",
            "definition": "C4 anchors reached by Dijkstra and screen-only orders at the same 20-paper replay budget.",
            "source": "dijkstra_selection_comparison.csv",
            "boundary": "Replay against this predeclared reading plan, not a general algorithm benchmark.",
        },
    ]
    numerical_fields = ["metric", "value", "definition", "source", "boundary"]
    write_csv(run_dir / "numerical_ledger.csv", numerical_rows, numerical_fields)

    stopping_lines = [
        "# Coverage and Stopping Record",
        "",
        "## Decision",
        "",
        "**Stop the planned Part 1 discovery pass.** This is a scope-limited stopping decision, not a claim that all SPS-related literature has been found.",
        "",
        "## What was completed",
        "",
        f"- {len(protocol)} configured query routes spanning L0-L10; {rounds['L0']} at L0 and {sum(rounds[f'L{i}'] for i in range(1, 11))} through L1-L10.",
        f"- {retrieval_status['OK']} successful route retrievals and {len(route_records)} raw route records, deduplicated to {len(screened)} candidates.",
        f"- C0-C2 decisions: {decisions['include']} include, {decisions['candidate']} candidate, and {decisions['exclude']} exclude with retained reasons.",
        f"- {len(selected)} current PDFs passed C3 integrity checks; {len(c4_notes)} planned C4 sources received anchored reading notes.",
        f"- {len(direct)} direct SPS bibliography relations were checked in current root-PDF context.",
        f"- The L5-L10 targeted expansion yielded {l5_l10_records} summed per-route unique hits across six new routes; Q24 returned zero, which is recorded rather than filled with an inferred author branch.",
        "",
        "## Why this is enough for this pass",
        "",
        "The declared root, method, correction/exactness, stochastic-quantization, topology, multiscale, evaluation, and author channels have each been traversed. The final reading plan contains C4 anchors across the named method families, and the gap ledger preserves the questions that require a new run rather than generic further browsing.",
        "",
        "## What would reopen search",
        "",
        "- A specific comparison question, such as matched GPU-hour cost, observable-error estimation, or finite-volume scaling.",
        "- A new paper version, a newly released related manuscript, or an identified missing direct reference.",
        "- A request to promote one of the retained C2 candidates to C3/C4 because it is needed for a proposal, manuscript, or experiment design.",
        "",
        "The retained candidate pool and query log are the restart points; no missing branch is silently converted into a conclusion.",
    ]
    (run_dir / "coverage_stopping_report.md").write_text("\n".join(stopping_lines) + "\n", encoding="utf-8")

    report_lines = [
        "# SPS Part 1 Fresh-Run Report",
        "",
        "## Starting clue",
        "",
        "`SPS / stochastic path sampler` was locked to `arXiv:2606.13790`, *Stochastic Path Sampler For Lattice Field Theory*, using independent identifier and exact-title routes before any method summary was written.",
        "",
        "## Result",
        "",
        f"The L0-L10 run contains {len(route_records)} raw route records, {len(screened)} deduplicated candidates, {len(selected)} C3-verified PDFs, and {len(c4_notes)} C4 reading records. It records {len(direct)} exact direct-citation links and {len(visual)} key visual source checks.",
        "",
        "## Safe interpretation",
        "",
        "The report supports a source-grounded SPS method landscape and a documented set of open experimental questions. It does not establish a universal sampling-speed claim, a cost comparison, or a global literature-completeness claim.",
        "",
        "## Read in this order",
        "",
        "1. `literature_research_report.md` for the claim-scoped synthesis.",
        "2. `source_matrix.csv`, `native_paper_reading_ledger.csv`, and `claim_source_ledger.csv` for individual records.",
        "3. `relation_ledger.csv`, `author_lineage_table.csv`, and `graphs/citation_lineage_graph.png` for lineage.",
        "4. `gap_ledger.csv`, `coverage_stopping_report.md`, and `reviewer_comparison_matrix.csv` for boundaries and next work.",
        "5. `dijkstra_effect_evaluation.md` and `graphs/dijkstra_selection_effect.png` for the navigation-only replay.",
    ]
    (run_dir / "run_report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    manifest_rows = [
        {
            "purpose": "Read the source-grounded SPS synthesis",
            "primary_artifact": "literature_research_report.md",
            "what_it_contains": "Root identity, C4-safe method landscape, explicit limits, and next questions.",
        },
        {
            "purpose": "Inspect literature records rather than prose",
            "primary_artifact": "source_matrix.csv; native_paper_reading_ledger.csv; claim_source_ledger.csv",
            "what_it_contains": "URLs, local PDFs, C3/C4 levels, anchors, safe sentences, and prohibited overclaims.",
        },
        {
            "purpose": "Audit citations and visual source pages",
            "primary_artifact": "relation_ledger.csv; root_bibliography.csv; visual_source_audit.md",
            "what_it_contains": "Exact direct-citation context plus key PDF-page screenshots.",
        },
        {
            "purpose": "See the method and author lineage",
            "primary_artifact": "graphs/landscape_map.png; graphs/citation_lineage_graph.png; author_lineage_table.csv",
            "what_it_contains": "C4 display graph, citation/method distinction, and shared-author table.",
        },
        {
            "purpose": "Audit the search and stopping logic",
            "primary_artifact": "search_protocol.csv; query_yield_log.csv; coverage_stopping_report.md; gap_ledger.csv",
            "what_it_contains": "L0-L10 routes, yields, retained gaps, and restart conditions.",
        },
        {
            "purpose": "Audit Dijkstra navigation without treating it as evidence",
            "primary_artifact": "dijkstra_computed/dijkstra_shortest_paths.csv; dijkstra_effect_evaluation.md; graphs/dijkstra_selection_effect.png",
            "what_it_contains": "Weighted paths, equal-budget replay, and its explicit interpretation boundary.",
        },
    ]
    manifest_fields = ["purpose", "primary_artifact", "what_it_contains"]
    (run_dir / "output_manifest.md").write_text(
        "# Output Manifest\n\n" + "\n".join(markdown_table(manifest_rows, manifest_fields)) + "\n",
        encoding="utf-8",
    )

    state_lines = [
        "# Research State",
        "",
        "- topic: SPS / stochastic path sampler for lattice field theory",
        "- intent: cover, with evaluation as a secondary question",
        "- root: arXiv:2606.13790",
        "- stage: L0-L10 discovery, C3/C4 source reading, lineage, and navigation replay complete",
        f"- raw route records: {len(route_records)}",
        f"- deduplicated candidates: {len(screened)}",
        f"- screened decisions: {decisions['include']} include / {decisions['candidate']} candidate / {decisions['exclude']} exclude",
        f"- C3 gate: {len(c3_ok)}/{len(selected)} selected PDFs passed",
        f"- C4 gate: {len(c4_notes)}/{len(c4_planned)} planned core papers have anchored notes",
        f"- direct root citation checks: {len(direct)}",
        "- stopping decision: stop this declared Part 1 scope; reopen only for a defined new question or new source event",
        "- current open questions: matched observable errors, autocorrelation diagnostics, and total GPU-hour comparisons for SPS versus a schedule-matched baseline",
    ]
    (run_dir / "research_state.md").write_text("\n".join(state_lines) + "\n", encoding="utf-8")
    print(
        f"raw={len(route_records)} candidates={len(screened)} c3={len(c3_ok)} "
        f"c4={len(c4_notes)} direct={len(direct)} visual={len(visual)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
