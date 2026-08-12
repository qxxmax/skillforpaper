# Output Manifest

Part 3 experiment run: multi-model quick-scan benchmark of the skill itself.
Created first, per the state write order law.

Status values: `planned` → `in_progress` → `on_disk` → `verified`, plus
`needs_update` and `blocked`.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| experiment_contract.md | markdown | — | pre-registered criteria before any arm launches | on_disk |  |
| compute_budget.md | markdown | — | planned/actual per arm | on_disk |  |
| env_snapshot.md | markdown | — | harness, model slugs, observability limits | on_disk |  |
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk |  |
| round_log.md | markdown | — | call ledger (orchestrator makes no web calls) | on_disk |  |
| run_ledger.csv | csv | subagent arms | one row per arm, failures included | on_disk |  |
| claim_promotion_ledger.md | markdown | run_ledger.csv, scoring | levels per claim; gate notes | on_disk | 2 candidate_claims, 2 observations |
| scoring_report.md | markdown | arms/*/ outputs vs ground truth | per-arm metric table | on_disk | H1 pass; H2 trail-only |
| README.md | markdown | all of the above | — | on_disk |  |
