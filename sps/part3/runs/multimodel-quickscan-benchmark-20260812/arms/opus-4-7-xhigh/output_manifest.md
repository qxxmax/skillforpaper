# Output Manifest

Quick-level literature scan for the Stochastic Path Sampler (SPS,
arXiv:2606.13790) predecessor identification task. This file is the live run
ledger and was created **first**, before any other run file.

Status values: `planned` → `in_progress` → `on_disk` → `verified`, plus
`needs_update` when source evidence changes after the file was written.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | — | verified | this file; created first; reconciled by validator |
| research_state.md | markdown | — | mode, scope, budget mirror | verified | quick scan, evaluate primary; validator CONSISTENT |
| candidate_pool.md | markdown | 10 arXiv fetches (round_log R0001) | C-level per candidate; 9 confirmed C2 + 1 root C3 | verified | 9 predecessors confirmed via own fetches; 5 context refs left at C1(bib-of-C3) |
| evidence_registry.md | markdown | 10 arXiv fetches (round_log R0001) | EvidenceID + anchors; 10 rows E0001–E0010 | verified | 1 E_FULLTEXT (SPS) + 9 E_ABSTRACT (predecessors) |
| round_log.md | markdown | — | call ledger row for every web call; 10 rows totaling 10/10 | verified | authoritative budget counter; exactly at cap |

## Report Sections

Not producing a final report in this quick scan; the deliverable is the
quick-scan file set plus one-paragraph final summary. Substantive claims must
carry an `EvidenceID`; unverified predecessors remain C0/C1 in
`candidate_pool.md`.

## Export Rules

- Claims without EvidenceID go to notes, not main conclusions.
- C0/C1 papers can be listed but not used as strong claim evidence.
- C3/C4 papers can support substantive claims.
- Budget cap: 10 web calls total (searches + fetches).
