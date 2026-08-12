# Output Manifest

This file is the live run ledger. Create it **first**, at every scan level
including quick scans, before any other run file. Update a row immediately
after its file lands on disk, never before (see the state write order in
`references/33_literature_intent_modes_and_state_loop.md`).

Status values: `planned` → `in_progress` → `on_disk` → `verified`, plus
`needs_update` when source evidence changes after the file was written.
When resuming an interrupted run, reconcile this table against the disk before
doing any new work.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| research_state.md | markdown | — | mode, scope, budget mirror | verified | mandatory quick; validator CONSISTENT |
| candidate_pool.md | markdown | search rounds | C-level per candidate | verified | P0000–P0009 confirmed; P0010–P0012 unconfirmed |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | verified | E0001–E0022; 10 logged fetches |
| round_log.md | markdown | — | call ledger rows for every web call | verified | ledger 10/10; R0000–R0003 |

## Report Sections

Not required for this quick locate/evaluate scan (no final report requested).

## Export Rules

- Claims without EvidenceID go to notes, not main conclusions.
- C0/C1 papers can be listed but not used as strong claim evidence.
- C3/C4 papers can support substantive claims.
- Paywalled but central papers must be listed in limitations.
