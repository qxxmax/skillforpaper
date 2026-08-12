# Output Manifest

Live run ledger for the quick-level literature scan (arm: opus-4-8-high).
Created first, before any other run file. Status values:
`planned` → `in_progress` → `on_disk` → `verified`, plus `needs_update`.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | this file | on_disk | created first |
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk | findings + validator result |
| candidate_pool.md | markdown | search rounds | C-level per candidate | on_disk | 10 confirmed predecessors (C2) |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk | E0001–E0011 |
| round_log.md | markdown | — | call ledger rows for every web call | on_disk | 2/10 calls logged |

## Scan Level

quick — target identify the key prior methods arXiv:2606.13790 builds on
(learned/neural samplers for unnormalized targets; learned samplers for
lattice field theory), each verified with a logged web call.

## Budget

At most 10 web calls total. Authoritative counter is the call ledger in
round_log.md.
