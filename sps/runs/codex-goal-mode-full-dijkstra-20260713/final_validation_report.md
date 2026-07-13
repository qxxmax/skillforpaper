# Final Validation Report

**Status: PASS**

| Gate | Status | Detail |
|---|---|---|
| selected_read_pdf_source_sets | PASS | sets=37/37/37/37 |
| fulltext_count | PASS | count=37 |
| reading_anchors | PASS | all four anchors present per paper |
| pdf_integrity | PASS | pages=776; errors=[] |
| source_links | PASS | verified=37 |
| evidence_registry_shape | PASS | entries=185 expected=185 |
| claim_evidence_links | PASS | claims=10 refs=38 |
| gap_evidence_links | PASS | gaps=9 refs=22 |
| numerical_claims | PASS | numbers=13 |
| direct_citation_relations | PASS | edges=199 unique_pairs=199 |
| candidate_graph_size | PASS | nodes=3300 edges=8187 paths=593 |
| candidate_dijkstra_invariants | PASS | errors=[] |
| verified_graph_size | PASS | nodes=164 edges=944 paths=37 |
| verified_dijkstra_invariants | PASS | errors=[] |
| verified_path_semantics | PASS | {'citation_only': 36, 'root': 1} |
| equal_budget_selection_comparison | PASS | baseline=30 dijkstra=30 overlap=20 |
| required_artifacts | PASS | missing=[] |
| workbook_visual_qa | PASS | previews=16 |
| workbook_formula_scan | PASS | no formula error tokens |

Dijkstra distances are navigation costs. Passing these gates does not convert a path score into scientific evidence.
