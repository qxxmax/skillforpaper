# Part 5 Submission Rehearsal (SPS → PRL / SciPost Physics)

First worked exercise of the Part 5 contracts
(`references/43_paper_assembly_from_ledgers.md`,
`references/44_venue_selection_and_submission_gate.md`) on real material: the
SPS paper (arXiv:2606.13790) audited in Part 1 and technically reviewed in
Part 2 of this repository.

## What is real here

- Both venue profiles are built from official guideline content fetched on
  2026-08-12. The direct fetches were bot-blocked, so the blocked-channel
  substitution rule (reference 34) fired for real: failures are in the call
  ledger, substitutes are logged, and the SciPost profile carries an explicit
  weaker-evidence note.
- All four claims in `claim_evidence_ledger.md` come from the verified Part 2
  review core, with its allowed/forbidden wording preserved.
- The submission gate result is honestly NOT READY: the manuscript source and
  a locked code repository do not exist in this repository, and the gate
  reports exactly that instead of pretending.

## What is deliberately absent

- No review-response exercise: no real referee reports exist for this paper,
  and fabricating them would violate the evidence guardrails. Reference 45
  and `validate_review_response.py` are covered by built-in self-test
  fixtures instead.
- No manuscript editing and no venue decision: the selection matrix in
  `research_state.md` records a recommendation; the choice is the authors'.

## Validation

`scripts/validate_run_state.py <this directory>` auto-detects the `part5`
profile and reports CONSISTENT.
