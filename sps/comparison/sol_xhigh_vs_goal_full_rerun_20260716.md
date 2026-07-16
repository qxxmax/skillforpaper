# SPS Part 1: Case Summary and Historical SOL Comparison

This page reports the 2026-07-16 fresh Goal-mode rerun and places it beside the earlier identified `gpt-5.6-sol/xhigh` run.
The two runs did **not** use the same search and reading contract, so the second table is a protocol-aware historical comparison, not a model leaderboard.

## 2026-07-16 case summary

| Stage | Result | Source artifact |
|---|---|---|
| Target identity | arXiv:2606.13790v1; title, authors, and date confirmed by Q01/Q02/P01 | `root_identity_check.csv` |
| Fresh retrieval | 36/36 routes succeeded | `retrieval_log_all_rounds.csv` |
| Candidate funnel | 371 raw route records -> 308 unique -> 151 active C0-C2 records | `candidate_screening_table.csv` |
| Source gate | 21/21 PDFs passed C3; 489 verified pages | `source_matrix.csv` |
| Claim gate | 14/14 planned core papers reached C4 | `c4_reading_notes.psv` |
| Audit package | 70 evidence rows; 14 claim rows; 10 direct citations; 7 visual source pages | `evidence_registry.csv; claim_source_ledger.csv` |
| Dijkstra replay | 254 nodes / 464 edges; at budget 20, 14 C4 anchors versus 8 | `dijkstra_selection_comparison.csv` |
| Validation | PASS: 21/21 checks | `final_validation_report.md` |
| Observed run delta | 2957 s; 806,679 Goal-counter tokens | `runtime_accounting.md` |

The safe conclusion is that this run produced a complete, auditable SPS Part 1 package under its declared scope. It does not establish universal literature completeness or a cost advantage for SPS.

## Earlier SOL run versus the fresh Goal rerun

| Metric | `gpt-5.6-sol/xhigh` (earlier) | Goal-mode full rerun (2026-07-16) | How to read it |
|---|---|---|---|
| Runtime identity | gpt-5.6-sol; xhigh; confirmed | Codex Goal mode; deployment model and effort not exposed | Configuration description only |
| Search contract | 30 fresh + 6 fixed legacy routes | 24 L0-L10 queries + 12 identifier probes; all freshly retrieved | Different route definitions |
| Recorded elapsed time | 1345 s (22 min 25 s) | 2957 s (49 min 17 s), S00-S02 Goal-counter delta | Not a speed benchmark; contracts differ |
| Recorded tokens | Unavailable | 806,679 Goal-counter delta | No token or price comparison possible |
| Deduplicated candidates | 578 | 308 | Reflects query scope, not model quality |
| C3/full-text sources | 27 PDFs / 611 pages | 21 PDFs / 489 pages | Different reading plans |
| Deep reading records | 27 four-dimension records | 14 C4 claim-anchored records | Different depth schema |
| Evidence / claim rows | 108 / 10 | 70 / 14 | Counts follow different output contracts |
| Checked direct-citation edges | 58 | 10 | Whole-root screen versus selected C4 lineage |
| Executable Dijkstra | Not part of this run | 254 nodes / 464 edges; budget 20: 14 vs 8 C4 anchors | Current-run navigation diagnostic only |
| Key visual source pages | Not recorded in run metrics | 7 | Current-run audit feature |
| Final validation | PASS | PASS (21/21 checks) | Both completed their own declared contracts |

## What this comparison supports

- The earlier SOL run covered and read a larger pool under its broader frozen contract.
- The fresh Goal rerun added explicit C0-C4 gates, freshly hashed route artifacts, key source-page screenshots, an executable Dijkstra replay, and a declared stopping record.
- Both runs passed their own validators. Because the contracts and exposed runtime metadata differ, neither result establishes that one model is better or cheaper.

A strict model comparison requires one frozen contract, explicit model and reasoning identifiers, start/stop usage counters, and at least three independent repetitions per configuration.

## Sources

- [`gpt-5.6-sol/xhigh` run metrics](../runs/gpt-5.6-sol-xhigh-matched/run_metrics.json)
- [Fresh Goal rerun report](../runs/codex-goal-mode-full-dijkstra-rerun-20260716/run_report.md)
- [Fresh Goal rerun validation](../runs/codex-goal-mode-full-dijkstra-rerun-20260716/final_validation_report.md)
- [Fresh Goal rerun runtime boundary](../runs/codex-goal-mode-full-dijkstra-rerun-20260716/runtime_accounting.md)
- [Machine-readable comparison table](sol_xhigh_vs_goal_full_rerun_20260716.csv)
- [Matched ordinary-run versus Goal-mode comparison](cost_effect_summary.md)
