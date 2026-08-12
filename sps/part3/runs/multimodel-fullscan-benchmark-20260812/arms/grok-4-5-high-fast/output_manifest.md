# Output Manifest

Run: `multimodel-fullscan-benchmark-20260812/arms/grok-4-5-high-fast`  
Scan level: **full** | graph_mode: **OFF**  
Seed: Stochastic Path Sampler for Lattice Field Theory (arXiv:2606.13790)  
Created: 2026-08-12

Status values: `planned` → `in_progress` → `on_disk` → `verified`

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk | stopped; 33/40 |
| candidate_pool.md | markdown | search rounds | C-level per candidate | on_disk | 36 rows; 7 C3 |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk | PDF integrity for 7 files under sources/pdfs/ |
| round_log.md | markdown | — | call ledger rows for every web call | on_disk | 33/40 |
| search_budget_contract.md | markdown | — | planned vs actual budgets | on_disk | actual=33 |
| search_scope.md | markdown | — | inclusion/exclusion | on_disk | |
| search_route_log.md | markdown | — | route families executed | on_disk | |
| candidate_screening_table.md | markdown | candidate_pool | screen decisions | on_disk | |
| coverage_stopping_report.md | markdown | route/yield logs | honest stop judgment | on_disk | stopped_with_known_risk |
| keyword_ledger.csv | csv | seed + retained papers | TermIDs with provenance | on_disk | T001–T015 |
| query_matrix.csv | csv | keyword_ledger | axis-crossed queries | on_disk | Q001–Q018 |
| query_yield_log.csv | csv | executed queries | yield per QueryID | on_disk | |
