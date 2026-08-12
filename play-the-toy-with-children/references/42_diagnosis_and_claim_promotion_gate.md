# Diagnosis And Claim Promotion Gate

Use this reference when experiment results exist and the user asks what they
mean, whether they are trustworthy, or wants to state a conclusion from them
(Part 3). This gate stands between "the run printed a number" and "the paper
states a claim".

## Claim Levels

Every result-backed statement lives at exactly one level in
`claim_promotion_ledger.md` (from
`templates/claim_promotion_ledger_template.md`):

| level | meaning | minimum evidence |
|---|---|---|
| `observation` | a run produced this output | one run ledger row |
| `candidate_claim` | pattern worth believing provisionally | passes sanity checks below; stated with its scope |
| `validated_claim` | usable in a manuscript's results | promotion gate below passed |
| `retracted` | previously held, now withdrawn | reason + the rows that killed it |

Only `validated_claim` rows may back substantive manuscript sentences
(reference 43). Levels are analogous to Part 1's C-levels for sources: the
level travels with the claim wherever it is quoted.

## Sanity Checks (Observation → Candidate)

Before believing a pattern at all:

- the run's config matches what the contract said would be run (diff the
  ConfigRef, do not trust memory);
- the metric is computed on the right split/sample — check the code path
  once, explicitly;
- the number is not a known degenerate outcome (NaN masked by a default,
  untrained baseline, evaluation on training data);
- an order-of-magnitude cross-check against a known limit, analytic case, or
  literature value, when one exists.

## Promotion Gate (Candidate → Validated)

All items pass, or the claim stays a candidate with the gap recorded:

1. **Pre-registration**: the success criterion in `experiment_contract.md`
   predates the result, or the amendment trail explains why it changed.
2. **Repetition**: the effect survives the contract's seed/repetition policy;
   report spread, not just the best run. If repetition is unaffordable, the
   claim carries an explicit single-run caveat — that caveat is part of the
   claim's wording, not a footnote to drop later.
3. **Baseline**: the comparison baseline ran under the same conditions, or
   the asymmetry is stated (literature number, different hardware).
4. **Failure audit**: the run ledger's failed/discarded rows for this
   experiment were reviewed; none of them contradicts the claim or reveals a
   selection effect (the claim is not "the runs that survived").
5. **Boundary**: the claim states where it was tested (sizes, parameters,
   regimes) and does not extrapolate beyond without "we expect" wording.

## Diagnosis Loop For Failures And Surprises

When a run fails or a result surprises, diagnose before re-running blindly:

1. State the expected behavior and the observed behavior in one sentence
   each, in the run's Note or a diagnosis file.
2. Form the cheapest discriminating test (smaller case, analytic limit,
   single-batch overfit, known-answer input) and run that first.
3. One variable changes per diagnostic run; the run ledger's Note records
   which one and why.
4. A surprise that survives diagnosis is a finding: give it an
   `observation` row in the claim promotion ledger rather than burying it.
   A bug found retroactively invalidates promoted claims — mark them
   `retracted`, and re-check every manuscript sentence that cited them.

## Stop Conditions

A Part 3 phase stops when the contract's stop condition is met, the compute
budget is exhausted (backfill `actual`), or the question is answered —
including answered negatively. "The hypothesis failed and here is the
evidence" is a valid, complete Part 3 outcome; route the negative result to
the boundary/limitation sections of Part 5 rather than to the wastebasket.
Run `scripts/validate_part3_run_package.py <run-directory>` before handing
results to Part 5.
