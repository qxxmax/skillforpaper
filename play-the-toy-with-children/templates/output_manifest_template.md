# Output Manifest

This file records generated outputs and their evidence basis.

## Current Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| final_report.md | markdown | confirmed_literature.md, evidence_table.md, missing_risk_report.md | EvidenceID required for substantive claims | planned / generated / needs_update |  |
| final_report.tex | tex | final_report.md, references.bib, screenshots/ | EvidenceID + BibTeX required | planned / generated / needs_update |  |
| final_report.pdf | pdf | final_report.tex | compiled from TeX | planned / generated / needs_update |  |
| literature_graph.json | json | genealogy_graph.md | graph nodes/edges | planned / generated / needs_update |  |
| audit_package.md | markdown | search_log.md, round_log.md, evidence_registry.md | all actions logged | planned / generated / needs_update |  |

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
