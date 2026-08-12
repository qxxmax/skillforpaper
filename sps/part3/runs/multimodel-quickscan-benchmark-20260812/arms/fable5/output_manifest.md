# Output Manifest

Run: multimodel-quickscan-benchmark-20260812 / arm fable5
Scan level: quick
Created: 2026-08-12

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | md | run state | none | on_disk | live run ledger, created first |
| research_state.md | md | round_log.md, candidate_pool.md, evidence_registry.md | budget mirror must match call ledger | on_disk | mode, findings, validator result |
| candidate_pool.md | md | E01 bibliography + E02-E10 verification fetches | every confirmed row has an EvidenceID | on_disk | P00-P10; P06 unconfirmed C1 |
| evidence_registry.md | md | logged web calls (ledger rows 1-10) | every row cites URL actually visited | on_disk | E01-E10 |
| round_log.md | md | web call history | one row per call incl. failures | on_disk | rounds R0001-R0003, ledger 10/10 |
