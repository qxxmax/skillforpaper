# SPS literature-audit case

This is the worked example for **Part 1: understand the toy** in the
[six-part research roadmap](../README.md). It starts from a spoken clue and
ends with checked sources, paper notes, a literature lineage, open questions,
and a short report.

A separate
[Part 2 SPS technical-learning run](part2/runs/sps-goal-mode-rerun-20260716/README.md)
uses the same sources to explain the method, compare predecessor equations,
reconstruct the algorithm through T3, and review its main claims.

## Target paper

- Title: *Stochastic Path Sampler For Lattice Field Theory*
- Authors: Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou
- Identifier: arXiv:2606.13790v1
- Submitted: 2026-06-11
- Canonical page: <https://arxiv.org/abs/2606.13790>

The metadata is recorded separately from interpretation. Numerical and method
claims link to source rows and page-level anchors.

## Latest fresh Part 1 rerun

| Stage | 2026-07-16 result |
|---|---:|
| Fresh route retrievals | 36 / 36 passed |
| Candidate funnel | 371 raw -> 308 unique -> 151 active C0-C2 |
| C3 source gate | 21 / 21 PDFs; 489 pages |
| C4 claim gate | 14 / 14 planned core papers |
| Evidence / claims / direct citations | 70 / 14 / 10 |
| Key visual source pages | 7 |
| Dijkstra graph | 254 nodes / 464 edges |
| Equal-budget replay at 20 papers | 14 C4 anchors vs 8 for screen order |
| Final validation | PASS, 21 / 21 checks |

The compact result and the comparison with the earlier identified
`gpt-5.6-sol/xhigh` run are in
[`sol_xhigh_vs_goal_full_rerun_20260716.md`](comparison/sol_xhigh_vs_goal_full_rerun_20260716.md).
The runs used different contracts, so that page reports a historical workflow
comparison rather than a model ranking.

## What to inspect

| Question | Artifact |
|---|---|
| What papers entered the reviewed set? | [`literature_matrix.md`](runs/codex-goal-mode-cleanroom/literature_matrix.md) |
| Which source supports each sentence? | [`claim_source_ledger.md`](runs/codex-goal-mode-cleanroom/claim_source_ledger.md) |
| Which numbers were retained? | [`numerical_ledger.csv`](runs/codex-goal-mode-cleanroom/numerical_ledger.csv) |
| What was read from each paper? | [`manual_reading_notes.csv`](runs/codex-goal-mode-cleanroom/manual_reading_notes.csv) |
| What does the native SPS reading record contain? | [`native_paper_reading_record_sps.md`](runs/codex-goal-mode-full-dijkstra-20260713/native_paper_reading_record_sps.md) |
| How is one paper represented as a ledger row? | [`native_paper_reading_ledger.csv`](runs/codex-goal-mode-full-dijkstra-20260713/native_paper_reading_ledger.csv) |
| Which claims survive technical review? | [`native_paper_review_gate_sps.md`](runs/codex-goal-mode-full-dijkstra-20260713/native_paper_review_gate_sps.md) |
| How was the search expanded? | [`round_log.md`](runs/codex-goal-mode-cleanroom/round_log.md) |
| What is the method/citation lineage? | [`citation_lineage_graph.png`](runs/codex-goal-mode-cleanroom/graphs/citation_lineage_graph.png) |
| What remains unresolved? | [`gap_ledger.csv`](runs/codex-goal-mode-cleanroom/gap_ledger.csv) |
| Did the package pass validation? | [`final_validation_report.md`](runs/codex-goal-mode-cleanroom/final_validation_report.md) |
| What does the spreadsheet view look like? | [`sps_literature_audit_cleanroom.xlsx`](runs/codex-goal-mode-cleanroom/sps_literature_audit_cleanroom.xlsx) |
| What changed with executable Dijkstra? | [`dijkstra_effect_evaluation.md`](runs/codex-goal-mode-full-dijkstra-20260713/dijkstra_effect_evaluation.md) |
| What did the Dijkstra run cost? | [`runtime_accounting.md`](runs/codex-goal-mode-full-dijkstra-20260713/runtime_accounting.md) |
| What did the fresh 2026-07-16 rerun produce? | [`run_report.md`](runs/codex-goal-mode-full-dijkstra-rerun-20260716/run_report.md) |
| How does it compare with the earlier SOL run? | [`sol_xhigh_vs_goal_full_rerun_20260716.md`](comparison/sol_xhigh_vs_goal_full_rerun_20260716.md) |

## Run packets

| Folder | Purpose |
|---|---|
| [`gpt-5.6-sol-xhigh-matched`](runs/gpt-5.6-sol-xhigh-matched/) | Confirmed model assignment under the matched SPS contract. |
| [`codex-goal-mode-matched`](runs/codex-goal-mode-matched/) | Same contract in Codex goal mode; exact deployment identifier was not exposed. |
| [`codex-goal-mode-cleanroom`](runs/codex-goal-mode-cleanroom/) | From-scratch package with goal-level token snapshot and stricter dependency isolation. |
| [`codex-goal-mode-full-dijkstra-20260713`](runs/codex-goal-mode-full-dijkstra-20260713/) | Executable candidate and verified-graph Dijkstra passes, equal-budget relevance baseline, gap closure, final evidence package, and cost boundary. |
| [`codex-goal-mode-full-dijkstra-rerun-20260716`](runs/codex-goal-mode-full-dijkstra-rerun-20260716/) | Independent L0-L10 rerun with fresh source retrieval, C0-C4 gates, key screenshots, executable Dijkstra replay, stopping record, and 21-check validation. |

## With and without Dijkstra

The controlled comparison uses the same 593-paper candidate pool and the same
30-paper first-reading budget. Dijkstra ranking changes 10 of the 30 papers,
retains 21 exact SPS bibliography papers instead of 19, and leaves the coarse
facet and method-group counts unchanged. See
[`dijkstra_effect_and_cost.md`](comparison/dijkstra_effect_and_cost.md) for the
effect table and recorded cost boundary.

## Public-export boundary

The repository keeps source URLs, bibliographic metadata, short anchored notes,
paraphrased reading records, selected screenshots, generated graphs, and audit
tables. It excludes downloaded third-party PDFs, long source extracts,
full-text caches, arXiv source archives, and raw API payloads. They are not
needed to trace the public claims back to their sources.
