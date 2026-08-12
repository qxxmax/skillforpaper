# Output Manifest

Part 5 submission-rehearsal run for the SPS paper (arXiv:2606.13790).
Created first, per the state write order law. This run consumes the Part 1
audit and Part 2 learning packages in this repository; it creates no new
scientific evidence.

Status values: `planned` → `in_progress` → `on_disk` → `verified`, plus
`needs_update` and `blocked`.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk |  |
| round_log.md | markdown | — | call ledger rows for every web call | on_disk | 4 calls: 2 blocked fetches, 2 substitute searches |
| claim_evidence_ledger.md | markdown | ../../part2/runs/sps-goal-mode-rerun-20260716/review_core.md | EvidenceID per claim; wording bounds | on_disk | claims from the verified Part 2 review |
| venue_profile_prl.md | markdown | round 1 calls | guideline URL + fetch date | on_disk | official page bot-blocked; substitute channels logged |
| venue_profile_scipost_physics.md | markdown | round 1 calls | guideline URL + fetch date | on_disk | same substitution note |
| submission_package_manifest.md | markdown | claim_evidence_ledger.md, venue profiles | gate table with pass/blocked per item | on_disk | gate result: NOT READY (manuscript source not in this repository) |
| README.md | markdown | all of the above | — | on_disk | scope and honest boundaries of the rehearsal |
