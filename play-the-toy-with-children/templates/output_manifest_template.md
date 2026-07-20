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
| research_state.md | markdown | — | mode, scope, budget mirror | planned |  |
| candidate_pool.md | markdown | search rounds | C-level per candidate | planned |  |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | planned |  |
| round_log.md | markdown | — | call ledger rows for every web call | planned |  |
| final_report.md | markdown | confirmed_literature.md, evidence_table.md, missing_risk_report.md | EvidenceID required for substantive claims | planned |  |
| final_report.tex | tex | final_report.md, references.bib, screenshots/ | EvidenceID + BibTeX required | planned |  |
| final_report.pdf | pdf | final_report.tex | compiled from TeX | planned |  |
| literature_graph.json | json | genealogy_graph.md | graph nodes/edges | planned |  |
| audit_package.md | markdown | search_log.md, round_log.md, evidence_registry.md | all actions logged | planned |  |

## Report Sections

Final report should include:

1. Research question.
2. Intent mode.
3. Scope and inclusion/exclusion criteria.
4. Search strategy summary.
5. Confirmed literature.
6. Unconfirmed but potentially important literature.
7. Evidence table.
8. Genealogy graph summary.
9. Missing risk report.
10. Limitations.
11. Appendix: search log.
12. Appendix: evidence registry.

## Export Rules

- Claims without EvidenceID go to notes, not main conclusions.
- C0/C1 papers can be listed but not used as strong claim evidence.
- C3/C4 papers can support substantive claims.
- Paywalled but central papers must be listed in limitations.
- PDF must preserve evidence status.
