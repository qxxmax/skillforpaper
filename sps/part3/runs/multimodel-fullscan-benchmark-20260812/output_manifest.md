# Output Manifest

Part 3 experiment run E2: multi-model full-scan benchmark (bounded full
contract). Created first, per the state write order law.

Status values: `planned` → `in_progress` → `on_disk` → `verified`, plus
`needs_update` and `blocked`.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| experiment_contract.md | markdown | — | pre-registered before launch | on_disk |  |
| compute_budget.md | markdown | — | planned/actual per arm | on_disk |  |
| env_snapshot.md | markdown | — | harness, model slugs, observability limits | on_disk |  |
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk |  |
| round_log.md | markdown | — | orchestrator call ledger | on_disk |  |
| run_ledger.csv | csv | subagent arms | one row per arm, failures included | on_disk |  |
| claim_promotion_ledger.md | markdown | run_ledger.csv, scoring | levels per claim | on_disk |  |
| scoring_report.md | markdown | arms/*/ vs frozen ground truth | per-arm metrics | planned | after arms complete |
| README.md | markdown | all of the above | — | planned |  |
