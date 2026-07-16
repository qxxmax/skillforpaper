# Final Validation

Overall: **PASS**

| Check | Status | Detail |
|---|---|---|
| required_artifacts | PASS | all required artifacts present |
| L0_L10_protocol | PASS | 24 configured Q routes |
| identifier_probe_plan | PASS | 12 configured identifier probes |
| fresh_retrievals | PASS | 36 logged routes; statuses={'OK': 36} |
| raw_source_artifacts | PASS | every retrieval row has a current raw response and hash |
| root_identity | PASS | Q01, Q02, and P01 agree on arXiv:2606.13790 and title |
| candidate_pool_size | PASS | raw=371, deduplicated=308 |
| candidate_screening_decisions | PASS | {'include': 94, 'candidate': 57, 'exclude': 157} |
| root_screen_status | PASS | root is included and passes C0-C2 |
| C3_source_integrity | PASS | 21 selected PDFs checksum-rechecked |
| C4_anchor_set | PASS | 14 C4 records for 14 planned sources |
| C4_verification_ledger | PASS | all selected sources pass C3; planned core sources pass C4 |
| evidence_and_claim_ledgers | PASS | evidence=70, claims=14 |
| direct_citation_lineage | PASS | relations=14, direct=10 with explicit physical/printed page anchors |
| key_visual_source_audit | PASS | 7 source-page screenshots registered |
| source_link_ledger | PASS | all C3 links pass; four papers have selected visual anchors |
| dijkstra_input_graph | PASS | nodes=254, edges=464 |
| computed_dijkstra_paths | PASS | 254 reachable nodes and recomputed weighted paths |
| dijkstra_equal_budget_replay | PASS | same candidate pool; at 20-paper budget: 14 C4 anchors vs 8 |
| rendered_graphs | PASS | four nonempty rendered PNG views |
| runtime_accounting | PASS | 3 runtime snapshots; counters labelled separately from API cost |
