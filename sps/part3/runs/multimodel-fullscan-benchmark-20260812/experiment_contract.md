# Experiment Contract: E2 (multi-model bounded full-scan benchmark)

Written and frozen before any arm launches (2026-08-12, 19:30 UTC+2).
Amendments go in the log below, never as silent edits.

## Question And Hypothesis

- ExperimentID: E2
- Question: does the skill's **full-scan** contract — budget contract,
  multi-channel routes, screening funnel, C3 source gate, keyword/query
  ledgers, coverage stopping report — execute end-to-end on each available
  model inside one subagent context, and what does it cost?
- Hypotheses (falsifiable):
  - H1 (portability at full scale): ≥ 6/8 arms produce the complete full-set
    file contract, pass `validate_run_state.py`, and write an honest
    scope-limited stopping report.
  - H2 (recall at scale): mean recall of the frozen 20-paper verified core
    set is ≥ 60% (≥ 12/20 identified with resolvable identifiers at C1 or
    better), with zero fabricated citations.
  - H3 (cost, observational): calls, wall time, and transcript volume are
    recorded per arm; no threshold.

## Design

| item | value |
|---|---|
| independent variable | model (8 slugs, same as E1; see env_snapshot.md) |
| controlled variables | identical question, budget cap, file contract, contamination guard |
| budget cap per arm | 40 web calls total (searches, fetches, PDF downloads all count) |
| C3 source gate | ≥ 6 PDFs downloaded and integrity-checked into sources/ |
| channel requirement | ≥ 3 distinct channels (e.g., arXiv, Semantic Scholar/INSPIRE, Google Scholar, publisher) |
| graph_mode | off (not requested; Dijkstra out of scope for E2) |
| seed policy | none; single shot per model |
| metrics | M1 recall of frozen core set /20; M2 fabricated citations; M3 full-set file completeness + validator; M4 stopping-report honesty (scope-limited wording, no completeness claim); M5 calls used; M6 wall time; M7 transcript-volume proxy; M8 tokens (dashboard backfill or unavailable) |

## Ground Truth (frozen before launch)

The 21 C3-verified sources of the Part 1 rerun
(`sps/runs/codex-goal-mode-full-dijkstra-rerun-20260716/download_jobs.tsv`),
minus the root paper 2606.13790, give the 20-paper scoring set:

1904.12072, 2003.06413, 2101.08176, 2111.15141, 2201.08862, 2201.13117,
2210.03139, 2211.01364, 2302.13834, 2302.14082, 2309.17082, 2310.11979,
2311.03578, 2402.06561, 2404.09723, 2412.00200, 2512.19575, 2604.10209,
2605.11199, 2607.08505.

Scoring rule: an ID counts if the arm's pool/registry identifies it with a
resolvable identifier (C1 or better). Extra correct papers are recorded but
not scored. An identifier that does not resolve to the named paper is a
fabricated citation.

## Task Given To Every Arm

"Map the predecessor and adjacent-method landscape of *Stochastic Path
Sampler for Lattice Field Theory* (arXiv:2606.13790): learned/neural
samplers for unnormalized targets, learned samplers for lattice field
theory, and the correction/exactness mechanisms they use. Run the skill's
full-scan contract within the stated budget."

## Success Criterion (Pre-Registered)

- H1 pass: ≥ 6/8 arms complete per M3+M4.
- H2 pass: mean M1 ≥ 12/20 and total M2 = 0.
- Partial or failed arms are findings, ledgered as such; a negative result
  is a valid outcome.

## Baselines

E1 (quick-scan benchmark, same day, same models) is the comparison point for
cost and recall scaling; no new control arm (an uncontracted "full scan" is
undefined).

## Budget And Stop

- 8 arms × ≤ 40 calls; see compute_budget.md.
- Stop: all arms terminate or 24 h; unfinished arms ledgered `killed`.

## Outcome Map

- H1+H2 hold: promote "the full-scan contract is executable per subagent
  context across models at 40-call scale" to candidate_claim (single shot).
- Arms fail on file contract: identifies which full-set element is too heavy
  for which model class — direct input for skill simplification.
- Recall collapses under the cap: evidence that full coverage genuinely
  needs the larger budget of the original runs; quantifies the floor.

## Known Limitations (declared up front)

- Bounded at 40 calls: this is the full workflow, not the full original
  scale (36-route, ~1M-token runs); absolute recall is expected lower.
- Single shot per model; no statistical claim.
- Token counters not observable at the harness level (M8 via dashboard).
- Model pretraining may know parts of the landscape; M1 checks resolvable
  identification, not novel discovery.

## Amendment Log

| date | what changed | why | results existed? |
|---|---|---|---|
|  |  |  |  |
