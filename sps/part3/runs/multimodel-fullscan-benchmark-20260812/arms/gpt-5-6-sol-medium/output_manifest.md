# Output Manifest

Run: `multimodel-fullscan-benchmark-20260812 / gpt-5-6-sol-medium`

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| research_state.md | markdown | run contract | mode, scope, budget mirror | verified | mandatory |
| candidate_pool.md | markdown | search rounds | C-level per candidate | verified | mandatory |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | verified | mandatory |
| round_log.md | markdown | web calls | complete call ledger | verified | mandatory |
| search_budget_contract.md | markdown | budget rules | actuals backfilled at stop | verified | mandatory full scan |
| search_scope.md | markdown | task statement | inclusion/exclusion rules | verified | mandatory full scan |
| search_route_log.md | markdown | query routes | route provenance | verified | mandatory full scan |
| candidate_screening_table.md | markdown | candidate pool | include/exclude/uncertain reasons | verified | mandatory full scan |
| coverage_stopping_report.md | markdown | all search records | honest residual-risk decision | verified | mandatory full scan |
| keyword_ledger.csv | csv | verified source terms | anchored terms | verified | mandatory full set |
| query_matrix.csv | csv | keyword ledger | reproducible queries | verified | mandatory full set |
| query_yield_log.csv | csv | search calls | query yields | verified | mandatory full set |
| relation_ledger.csv | csv | graph validator | header only, graph_mode off | verified | no public graph edges asserted |
| channel_coverage_plan.md | markdown | scope and routes | searched/blocked channels | verified | channel gate |
| citation_generation_log.md | markdown | citation expansion | generation provenance | verified | channel gate |
| cross_validation_matrix.md | markdown | metadata checks | independent confirmations | verified | channel gate |
| missing_risk_report.md | markdown | coverage audit | named blind spots | verified | channel gate |
| source_link_verification_loop.md | markdown | source checks | authoritative URLs | verified | source gate |
| literature_matrix.md | markdown | included papers | correction/mechanism comparison | verified | mandatory full scan |
| reviewer_comparison_matrix.md | markdown | included papers | reviewer-risk contrasts | verified | mandatory full scan |
| lineage_snowball_map.md | markdown | author/method/citation routes | checked lineage notes | verified | mandatory full scan |
| gap_ledger.md | markdown | synthesis | evidence/boundary separation | verified | mandatory full scan |
| claim_evidence_ledger.md | markdown | evidence registry | EvidenceIDs | verified | mandatory full scan |
| literature_snapshot.md | markdown | final state | dated scope freeze | verified | mandatory full scan |
| sentence_result_bank.md | markdown | verified claims | EvidenceIDs | verified | mandatory full scan |
| sources/pdfs/README.md | markdown | core full texts | at least six integrity-noted PDFs | verified | 8 PDFs listed via evidence registry |
| sources/text/README.md | markdown | extracted core PDFs | local claim checking | verified | 8 successful text extractions |

Status values: `planned`, `in_progress`, `on_disk`, `verified`, `needs_update`.
