# Output Manifest

Live run ledger for the FULL-SCAN benchmark arm `opus-4-8-high`. Created first,
before any other run file. Status values: `planned` → `in_progress` →
`on_disk` → `verified`, plus `needs_update`.

Run: multimodel-fullscan-benchmark-20260812 / arms / opus-4-8-high
Task: predecessor + adjacent-method landscape of "Stochastic Path Sampler for
Lattice Field Theory" (arXiv:2606.13790). Scan level: full. graph_mode: OFF.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | live run ledger | on_disk | this file |
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk | Used: 14 mirrors ledger |
| candidate_pool.md | markdown | search rounds | C-level per candidate | on_disk | 34 records, P0001–P0034 |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk | E0001–E0014 |
| round_log.md | markdown | — | call ledger row per web call | on_disk | 14/40 calls |
| search_budget_contract.md | markdown | — | actual column backfilled at stop | on_disk | actuals = 14 |
| search_scope.md | markdown | — | eligibility + facets + seeds | on_disk | seed recovered |
| search_route_log.md | markdown | round_log.md | route plan + query log | on_disk | RT1–RT6 |
| candidate_screening_table.md | markdown | candidate_pool.md | include/exclude/uncertain/monitor | on_disk | include 19 |
| coverage_stopping_report.md | markdown | all state files | scope-limited, no completeness claim | on_disk | stop under budget |
| keyword_ledger.csv | csv | seed + PDFs | six-axis terms with anchors | on_disk | T001–T014 |
| query_matrix.csv | csv | keyword_ledger.csv | axis-crossed queries | on_disk | Q001–Q008 |
| query_yield_log.csv | csv | round_log.md | per-query yield | on_disk | Q001–Q008 |
| sources/pdfs/ | directory | web downloads | >=6 core PDFs + integrity note | not_applicable | directory (not reconciled as a top-level file); 7 PDFs on disk, sizes logged E0005–E0011 |

## Export Rules

- Claims without EvidenceID go to notes, not main conclusions.
- C0/C1 papers can be listed but not used as strong claim evidence.
- C3/C4 papers can support substantive claims.
- Do not claim absolute completeness; report residual missing risk.
