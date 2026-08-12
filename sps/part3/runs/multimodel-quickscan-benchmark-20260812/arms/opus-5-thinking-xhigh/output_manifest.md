# Output Manifest

Live run ledger for the quick-level literature scan on the predecessor methods
of "Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790).
Created first, before any other run file, per the Minimal Run Contract and the
state write order in `references/33_literature_intent_modes_and_state_loop.md`.

Run: `multimodel-quickscan-benchmark-20260812` / arm `opus-5-thinking-xhigh`
Scan level: quick. Profile: literature.
Status values: `planned` -> `in_progress` -> `on_disk` -> `verified`,
plus `needs_update` when source evidence changes after the file was written.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| research_state.md | markdown | — | mode, scope, budget mirror of round_log call ledger | verified | quick-scan mandatory file 2; mirrors Used: 5 of 10 |
| candidate_pool.md | markdown | search/fetch rounds | C-level per candidate, no silent deletions | verified | quick-scan mandatory file 3; 19 confirmed, 20 unconfirmed, 4 exclusion groups |
| evidence_registry.md | markdown | fetched sources | EvidenceID + URL actually visited | verified | quick-scan mandatory file 4; E0001-E0027, ERQ0001-ERQ0004 |
| round_log.md | markdown | — | one call-ledger row per web call, running total n/10 | verified | quick-scan mandatory file 5; authoritative budget counter, 5 ledger rows |

Validator run at stop (`scripts/validate_run_state.py`): profile `literature`,
status CONSISTENT, 4 manifest rows, 0 errors, 0 warnings, exit code 0 — which is
why the four rows above are `verified` rather than `on_disk`.

## Not Applicable At This Scan Level

Quick level does not require `search_budget_contract.md`, `search_scope.md`,
`search_route_log.md`, `candidate_screening_table.md`,
`coverage_stopping_report.md`, keyword/query ledgers, graph files, or a final
report artifact. None were requested; none are produced.

## Export Rules

- Claims without an EvidenceID go to notes, not to conclusions.
- C0/C1 papers may be listed but must not carry strong claims.
- Predecessor identity claims (title, authors, arXiv ID) require at least C1
  metadata from an authoritative arXiv/publisher record that was actually
  fetched and logged in the call ledger.
- If budget runs out, remaining candidates stay C0/C1 unverified rather than
  being asserted.
