# Scoring Report: E1 Multi-Model Quick-Scan Benchmark

Date: 2026-08-12. Scored by the orchestrator against the pre-registered
criteria in `experiment_contract.md`, from arm artifacts (not arm
self-reports). Independent re-validation was run on every arm.

## Per-Arm Results

| RunID | arm | M1 GT/4 | M2 fabricated | M3 validator (independent) | M4 call ledger | calls used | ≈wall time |
|---|---|---|---|---|---|---|---|
| E1-R001 | fable5 | 4/4 | 0 | CONSISTENT | yes | 10/10 | ≈8 min |
| E1-R002 | fable5-thinking-max | 4/4 | 0 | CONSISTENT | yes | 2/10 | ≈9 min |
| E1-R003 | opus-4-7-xhigh | 4/4 | 0 | CONSISTENT | yes | 10/10 | ≈10 min |
| E1-R004 | opus-4-8-high | 4/4 | 0 | CONSISTENT | yes | 2/10 | ≈5 min |
| E1-R005 | opus-5-thinking-xhigh | 4/4 | 0 | CONSISTENT | yes | 5/10 | ≈11 min |
| E1-R006 | composer-2-5-fast | 3/4 | 0 | CONSISTENT | yes | 10/10 | ≈2 min |
| E1-R007 | grok-4-5-high-fast | 4/4 ¹ | 0 | CONSISTENT | yes | 10/10 | ≈4 min |
| E1-R008 | gpt-5-6-sol-medium | 3/4 | 0 ² | CONSISTENT | yes | 10/10 | ≈5 min |
| E1-R009 | control-noskill | 4/4 | 0 | n/a (report only) | **none** | 3/10 | ≈3 min |

¹ Grok identified SNF (2201.08862) with the correct title and resolvable ID
but budget ran out before independent verification; it honestly recorded the
row as `unconfirmed C1(bib-of-C4)` with a next-round query. The
pre-registered rule ("identified with a resolvable identifier") scores this
as a hit; the C1 status is preserved here.
² A suspicion against arXiv:2512.19575 ("Variational Autoregressive Networks
Applied to φ⁴...") was raised at intake and **cleared** against a local
bibliography: the arm's record was correct and the orchestrator's prior
recollection was wrong. Recorded as a worked example of
suspicion-then-evidence rather than silent trust either way.

## Pre-Registered Criteria

| criterion | threshold | measured | verdict |
|---|---|---|---|
| H1: mean M1 across skill arms | ≥ 3/4 | 3.75/4 | pass |
| H1: total M2 in skill arms | = 0 | 0 | pass |
| H1: M3 CONSISTENT arms | ≥ 6/8 | 8/8 | pass |
| H2: control worse on M2 | — | no (0 = 0) | **fail** |
| H2: control lacks reconstructable verification trail | — | yes (no call log, no evidence anchors, no per-claim source rows) | pass |

**H1 supported. H2 supported only on the trail dimension, not on accuracy.**
The control arm matched the best skill arms on recall (4/4) at the lowest
cost (3 calls). Reported prominently per the contract's outcome map: on this
task, the skill's measured value was auditability and honest uncertainty
labeling, not recall.

## Findings Beyond The Criteria

1. **Strategy dominated model.** Every arm that fetched the root paper's
   full text first and then batch-verified against the arXiv API reached
   4/4 cheaply (2-5 calls). The two clean misses (composer, gpt) and the
   one C1-only identification (grok) all involve the same paper — SNF
   lattice (2201.08862), the least prominent ground-truth item — and all
   three arms spent their full budget on per-paper lateral searching.
   Implication for the skill: the quick-scan reference should name
   "root-document bibliography first, then batch identity verification" as
   the default opening move.
2. **This task under-tests discipline.** The root paper's bibliography
   contains the answer, so recall is nearly free and the control arm looks
   equal. Discipline differences (C-levels, unverified-candidate labeling,
   call ledgers) would bind on questions without a single root document.
   Declared in the contract's limitations; a follow-up experiment should
   use a question with no bibliography shortcut.
3. **Recurring template friction.** Two arms (fable5, fable5-thinking-max)
   reported that their first `output_manifest.md` table format tripped
   `validate_run_state.py` before they self-corrected. Defect filed against
   the manifest template documentation, not the arms.
4. **Budget-exhaustion behavior was correct everywhere.** Three arms hit
   10/10 and all three degraded honestly (C1 labels, explicit
   next-round queries) instead of asserting unverified claims — the exact
   behavior the contract exists to enforce.

## Cost

Wall times above are approximate (launch-to-completion from orchestrator
notifications). Per-arm token/cost counters were not observable at the
harness level (see `env_snapshot.md`); the `compute_budget.md` token column
is `unavailable` pending the user's dashboard numbers.
