# SPS literature-audit case

## Target paper

- Title: *Stochastic Path Sampler For Lattice Field Theory*
- Authors: Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou
- Identifier: arXiv:2606.13790v1
- Submitted: 2026-06-11
- Canonical page: <https://arxiv.org/abs/2606.13790>

The target identity is separated from interpretation. Every public numerical or
method claim is expected to resolve through a ledger row to a source anchor.

## What to inspect

| Question | Artifact |
|---|---|
| What papers entered the reviewed set? | [`literature_matrix.md`](runs/codex-goal-mode-cleanroom/literature_matrix.md) |
| Which source supports each sentence? | [`claim_source_ledger.md`](runs/codex-goal-mode-cleanroom/claim_source_ledger.md) |
| Which numbers were retained? | [`numerical_ledger.csv`](runs/codex-goal-mode-cleanroom/numerical_ledger.csv) |
| What was read from each paper? | [`manual_reading_notes.csv`](runs/codex-goal-mode-cleanroom/manual_reading_notes.csv) |
| How was the search expanded? | [`round_log.md`](runs/codex-goal-mode-cleanroom/round_log.md) |
| What is the method/citation lineage? | [`citation_lineage_graph.png`](runs/codex-goal-mode-cleanroom/graphs/citation_lineage_graph.png) |
| What remains unresolved? | [`gap_ledger.csv`](runs/codex-goal-mode-cleanroom/gap_ledger.csv) |
| Did the package pass its gates? | [`final_validation_report.md`](runs/codex-goal-mode-cleanroom/final_validation_report.md) |
| What does the spreadsheet view look like? | [`sps_literature_audit_cleanroom.xlsx`](runs/codex-goal-mode-cleanroom/sps_literature_audit_cleanroom.xlsx) |

## Run packets

| Folder | Purpose |
|---|---|
| [`gpt-5.6-sol-xhigh-matched`](runs/gpt-5.6-sol-xhigh-matched/) | Confirmed model assignment under the matched SPS contract. |
| [`codex-goal-mode-matched`](runs/codex-goal-mode-matched/) | Same contract in Codex goal mode; exact deployment identifier was not exposed. |
| [`codex-goal-mode-cleanroom`](runs/codex-goal-mode-cleanroom/) | From-scratch package with goal-level token snapshot and stricter dependency isolation. |

## Public-export boundary

The repository keeps source URLs, bibliographic metadata, short anchored notes,
paraphrased reading records, selected screenshots, generated graphs, and audit
tables. It excludes downloaded third-party PDFs, long source extracts,
full-text caches, arXiv source archives, and raw API payloads. Those files were
useful during the local audit but are not required to show the workflow or
verify where each public claim came from.
