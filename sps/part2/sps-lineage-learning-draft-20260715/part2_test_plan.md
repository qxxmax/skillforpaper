# Part 2 SPS Evaluation Plan

## Purpose

Evaluate whether lineage-first reading reaches an accurate technical
explanation faster than a flat paper-by-paper reading order.

## Frozen Input

- Part 1 run: `../../runs/codex-goal-mode-full-dijkstra-20260713`
- Focal paper: P001 / arXiv:2606.13790v1
- Candidate predecessors: P002, P003, P007
- Later comparison node: P031
- No fresh search in this draft

## Checks

| Test | Measurement | Acceptance criterion | Current status |
|---|---|---|---|
| lineage reuse | selected nodes retain checked relation IDs | every displayed edge resolves to `relation_ledger.csv` | pass |
| innovation subtraction | compared dimensions have anchors on both sides | final rows cannot rely on abstract-only evidence | pending detailed predecessor records |
| fast locator | reading order identifies exact sections/equations before prose expansion | P0 path unlocks T2-T3 | draft |
| statement separation | author claim, synthesis, inference, and unresolved are distinct | no inference promoted to author claim | pass structurally |
| competence check | each T0-T3 pass has supporting evidence | no file-existence-only pass | T3 pending |
| export consistency | MD, CSV, TeX, and PDF preserve IDs and boundaries | source changes trigger rebuild | pending final refresh check |
| accounting | elapsed time and token source are declared | unavailable cost is not estimated | to measure in first full Part 2 run |

## Planned Ablations

1. Flat reading order versus prerequisite-aware lineage order.
2. Contribution-paragraph summary versus predecessor subtraction.
3. Technical extraction with versus without the technical review.

Measure time to a correct T2/T3 teach-back, number of unsupported novelty
statements, source-anchor coverage, unresolved questions retained, and token
usage when an observable usage source exists.

## Promotion Rule

This package may become `VERIFIED` only after the three predecessor records
pass R0-R6, the delta rows are rechecked at equation or algorithm level, T3
passes, the TeX/PDF exports are refreshed, and visual QA passes.
