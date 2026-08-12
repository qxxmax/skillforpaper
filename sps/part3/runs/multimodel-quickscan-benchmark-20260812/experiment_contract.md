# Experiment Contract: E1 (multi-model quick-scan benchmark)

Written and frozen before any arm launches (2026-08-12, 14:15 UTC+2).
Amendments go in the log below, never as silent edits.

## Question And Hypothesis

- ExperimentID: E1
- Question: does the skill's quick-scan contract hold across different
  models, and does it measurably beat an uncontracted baseline on evidence
  discipline?
- Hypothesis (falsifiable): (H1) skill arms recover the core predecessors
  and produce zero fabricated citations across models; (H2) the no-skill
  control shows weaker evidence discipline (missing verification trail
  and/or unresolvable citations).

## Design

| item | value |
|---|---|
| independent variables (swept) | model (8 slugs); skill on/off (control arm on `inherit`) |
| controlled variables (fixed) | identical research question; identical 10-call web budget; identical output-file contract per arm type; contamination guard (no reading of `sps/` history or other arms) |
| seed policy | none (LLM arms are single-shot; no repetition budget) |
| metrics measured | (M1) core predecessors recovered, of 4 ground-truth papers; (M2) fabricated/unresolvable citations, count; (M3) quick-set file completeness + `validate_run_state.py` result; (M4) call-ledger discipline (every claim traceable to a logged call); (M5) wall time; (M6) tokens/cost per arm, backfilled from the user's usage dashboard when available |
| evaluation protocol | orchestrator scores each arm against the ground truth after completion; scoring rules below |

## Ground Truth (fixed before launch)

From the verified Part 2 review (`sps/part2/runs/sps-goal-mode-rerun-20260716/`),
the four checked direct-predecessor methods of SPS (arXiv:2606.13790):

| ID | method | identifier |
|---|---|---|
| GT1 | Path Integral Sampler (PIS) | arXiv:2111.15141 |
| GT2 | Denoising Diffusion Samplers (DDS) | arXiv:2302.13834 |
| GT3 | Controlled Monte Carlo Diffusions (CMCD) | arXiv:2307.01050 |
| GT4 | Stochastic Normalizing Flows for lattice field theory (SNF) | arXiv:2201.08862 |

Scoring rules: an arm scores a GT hit only if the paper is identified with a
resolvable identifier. A cited identifier that does not resolve to the named
paper counts as a fabricated citation (M2). Extra correct papers beyond GT
are recorded but do not affect M1.

## Success Criterion (Pre-Registered)

- H1 supported if: mean M1 ≥ 3/4 across skill arms, total M2 = 0 in skill
  arms, and M3 CONSISTENT in ≥ 6/8 skill arms.
- H2 supported if: the control arm scores worse on M2 or lacks a
  reconstructable verification trail (no per-call log, no evidence anchors).
- Any other outcome: report as-is; a negative result is a valid outcome.

## Baselines

| baseline | source | evidence |
|---|---|---|
| no-skill control | own run, arm `control-noskill` | run ledger row E1-R009 |

## Budget And Stop

- Compute budget: see `compute_budget.md`; 10 web calls per arm, 9 arms.
- Stop condition: all 9 arms terminate (completed or failed) and scoring is
  written, or 24 h elapse — unfinished arms are then ledgered as `killed`.

## Outcome Map

- If H1 holds: promote "the quick-scan contract is model-portable at the
  evidence-discipline level" to candidate_claim (single-shot arms: no
  repetition, so validated_claim requires a future repeat).
- If H1 fails on some models: per-model failure rows are findings — record
  which contract element broke (budget, ledger, verification).
- If H2 fails (control is just as disciplined): that weakens the skill's
  value claim and must be reported prominently, not buried.

## Known Limitations (declared up front)

- Single shot per model: no seed/repetition, so no arm-level statistical
  claim; results are existence evidence only.
- Token counters are not observable at the orchestration layer; M6 depends
  on the user's dashboard and may stay `unavailable` (recorded, not
  estimated).
- Model priors may contain SPS knowledge; the contamination guard blocks
  repository leakage but cannot erase pretraining. M2 verification therefore
  checks resolvability of citations, not novelty of discovery.

## Amendment Log

| date | what changed | why | results existed? |
|---|---|---|---|
|  |  |  |  |
