# Output Manifest

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | live ledger | on_disk | created first |
| research_state.md | markdown | round_log.md | mode, scope, budget mirror | on_disk | |
| candidate_pool.md | markdown | search rounds | C-level per candidate | on_disk | |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk | |
| round_log.md | markdown | — | call ledger rows | on_disk | |
| search_budget_contract.md | markdown | round_log.md | actual column backfilled | on_disk | |
| search_scope.md | markdown | task brief | inclusion/exclusion | on_disk | |
| search_route_log.md | markdown | query ledgers | channel + route trace | on_disk | |
| candidate_screening_table.md | markdown | candidate_pool.md | include/exclude reasons | on_disk | |
| coverage_stopping_report.md | markdown | route log | honest stop rationale | on_disk | |
| keyword_ledger.csv | csv | seed abstract §1 | TermID provenance | on_disk | |
| query_matrix.csv | csv | keyword_ledger | QueryID routes | on_disk | |
| query_yield_log.csv | csv | round_log | yield per query | on_disk | |
| sources/pdfs/ | directory | arXiv PDF fetch | ≥6 C3 PDFs | planned | 6 PDFs on disk under subdirectory |
