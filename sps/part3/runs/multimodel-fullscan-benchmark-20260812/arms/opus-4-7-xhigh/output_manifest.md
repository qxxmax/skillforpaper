# Output Manifest — opus-4-7-xhigh arm

Run: multimodel-fullscan-benchmark-20260812
Arm: opus-4-7-xhigh
Task: Full-scan landscape map of predecessor and adjacent-method literature for
"Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790).
Scan level: full. graph_mode: OFF.

This file is the live run ledger, created first per the state-write-order law
in `references/33_literature_intent_modes_and_state_loop.md`. Rows move
`planned` → `in_progress` → `on_disk` → `verified` only after the underlying
file lands on disk.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | this file | on_disk | created first |
| research_state.md | markdown | round_log.md | mode, scope, budget mirror | on_disk | final: 17/40 calls, 4 channels, stopped_with_known_risk |
| candidate_pool.md | markdown | seed refs + coverage searches | C-level per candidate | on_disk | 47 include + 12 exclude + 15 candidate + 6 monitor + 2 out-of-scope |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk | 19 EvidenceIDs (E0001–E0019); 8 C3 rows for downloaded PDFs |
| round_log.md | markdown | — | call ledger for every web call | on_disk | 17 rows, R0001–R0005 |
| search_budget_contract.md | markdown | round_log.md | full-scan budget contract with backfilled actuals | on_disk | `actual` column filled from ledger |
| search_scope.md | markdown | seed + skill contract | eligibility + facet map + seed set | on_disk | 3 facets each with ≥3 confirmed rows |
| search_route_log.md | markdown | round_log.md | route plan + query log + coverage notes | on_disk | 10 route entries + 17 query rows |
| candidate_screening_table.md | markdown | candidate_pool.md | include/exclude/uncertain/monitor with reason | on_disk | 82 rows spanning P0001–P0082 |
| coverage_stopping_report.md | markdown | route + candidate files | honest scope-limited stop | on_disk | stop=stop; explicit residual risks |
| keyword_ledger.csv | csv | seed sections | six-axis ontology with provenance | on_disk | 34 seed terms (T001–T034) |
| query_matrix.csv | csv | keyword_ledger.csv + routes | axis-crossed queries with TermID linkage | on_disk | 17 queries (Q001–Q017), all with TermID provenance |
| query_yield_log.csv | csv | round executions | per-query raw/dedup/screened/included counts | on_disk | 17 rows matching queries |
| sources/pdfs/1904.12072.pdf | pdf | arXiv | integrity note = 884944 B, ~13 pages | on_disk | Albergo-Kanwar-Shanahan 2019 |
| sources/pdfs/2003.06413.pdf | pdf | arXiv | integrity note = 1017965 B, ~6 pages | on_disk | Kanwar et al. 2020 |
| sources/pdfs/2007.07115.pdf | pdf | arXiv | integrity note = 618576 B, ~13 pages | on_disk | Nicoli et al. 2021 |
| sources/pdfs/2111.15141.pdf | pdf | arXiv | integrity note = 2713763 B, ~26 pages | on_disk | Zhang-Chen PIS |
| sources/pdfs/2201.08862.pdf | pdf | arXiv | integrity note = 899741 B, ~32 pages | on_disk | Caselle SNF 2022 |
| sources/pdfs/2302.13834.pdf | pdf | arXiv | integrity note = 4179526 B, ~30 pages | on_disk | Vargas et al. DDS |
| sources/pdfs/2309.17082.pdf | pdf | arXiv | integrity note = 2486741 B, ~31 pages | on_disk | Wang-Aarts-Zhou 2024 |
| sources/pdfs/2410.02711.pdf | pdf | arXiv | integrity note = 2113233 B, ~31 pages | on_disk | Albergo-Vanden-Eijnden NETS |

## Report Sections (not delivered — landscape-only run)

This run's target is the landscape record for a benchmark; no `final_report.md`
was requested by the task instructions, so the report file is not scheduled.
If the benchmark harness requests a report, use
`templates/literature_research_report_template.md` and cite EvidenceIDs from
`evidence_registry.md`.

## Export Rules

- Substantive claims cite EvidenceID; C0/C1 papers are listed only, never used as strong claim evidence.
- Zero fabricated citations is a scored metric — all confirmed rows have INSPIRE record or PDF on disk; all uncertain rows are explicitly labeled C1 metadata-only with a single-channel provenance note.
- `coverage_stopping_report.md` states scope-limited coverage; absolute completeness is never claimed.
