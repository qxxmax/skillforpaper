# Output Manifest

Live run ledger for the full-scan benchmark arm `fable5-thinking-max`.
Created first, before any other run file (state write order,
`references/33_literature_intent_modes_and_state_loop.md`).

Run: multimodel-fullscan-benchmark-20260812 / arms/fable5-thinking-max
Task: map predecessor and adjacent-method landscape of "Stochastic Path
Sampler for Lattice Field Theory" (arXiv:2606.13790). Scan level: full.
graph_mode: OFF. Hard cap: 40 web calls.

Status values: planned → in_progress → on_disk → verified (+ needs_update).

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | manifest-first law | verified | this file; final batch update at stop |
| research_state.md | markdown | — | mode, scope, budget mirror | on_disk | final: stopped, mirror 28/40, funnel counts |
| candidate_pool.md | markdown | search rounds | C-level per candidate | on_disk | final: P0001–P0077, DEDUP0001–0004 |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk | final: E0001–E0017, ERQ0001–0002 resolved |
| round_log.md | markdown | — | call ledger rows for every web call, n/40 | on_disk | ledger rows 1–28 (incl. 1 failed call); rounds R0001–R0006 |
| search_budget_contract.md | markdown | — | actual column backfilled at stop | on_disk | actuals backfilled: 28/40 with ledger row refs |
| search_scope.md | markdown | — | eligibility, seeds, facets | on_disk |  |
| search_route_log.md | markdown | executed queries | one row per route/query | on_disk | RT01–RT06 executed + coverage notes |
| candidate_screening_table.md | markdown | candidate_pool.md | include/exclude/uncertain/monitor labels | on_disk | 77 pooled rows + monitor/exclude tiers |
| coverage_stopping_report.md | markdown | all state files | honest scope-limited stop rationale | on_disk | stop = stopped_with_known_risk; no completeness claim |
| keyword_ledger.csv | csv | seed paper + task statement | source anchors per seed term | on_disk | T001–T030 (6 search-derived) |
| query_matrix.csv | csv | keyword_ledger.csv | axis-crossed queries with TermIDs | on_disk | Q001–Q017, all executed |
| query_yield_log.csv | csv | executed queries | per-query yield | on_disk | all executed queries logged incl. failed call 13 |
| sources/pdfs/2606.13790_SPS.pdf | pdf | web call 2 | integrity E0002: 33 pp, 2,263,775 B | verified | seed, title checked |
| sources/pdfs/1904.12072_FlowMCMC_LFT.pdf | pdf | web call 20 | integrity E0009: 13 pp, 884,944 B | verified | title checked |
| sources/pdfs/2002.06707_SNF_WuKoehlerNoe.pdf | pdf | web call 21 | integrity E0010: 21 pp, 7,114,775 B | verified | title checked |
| sources/pdfs/2201.08862_SNF_noneq_Caselle.pdf | pdf | web call 22 | integrity E0011: 32 pp, 899,741 B | verified | title checked |
| sources/pdfs/2111.15141_PIS_ZhangChen.pdf | pdf | web call 23 | integrity E0012: 26 pp, 2,713,763 B | verified | title checked |
| sources/pdfs/2302.13834_DDS_Vargas.pdf | pdf | web call 24 | integrity E0013: 30 pp, 4,179,526 B | verified | title checked |
| sources/pdfs/2309.17082_DiffusionSQ_Wang.pdf | pdf | web call 25 | integrity E0014: 31 pp, 2,486,741 B | verified | title checked |
| sources/pdfs/2410.02711_NETS_Albergo.pdf | pdf | web call 26 | integrity E0015: 31 pp, 2,113,233 B | verified | title checked |
| seed_abs.html | html | web call 1 | raw fetched seed abs page | on_disk | audit trail |
| seed_fulltext.txt | txt | local extraction from seed PDF | full text for bib screening | on_disk | audit trail |
| r0002_arxiv_results.json | json | web calls 3–11 | raw lexical query results | on_disk | audit trail |
| r0003_s2_results.json | json | web calls 12–16 | raw citation-channel results | on_disk | audit trail |
| r0003_s2_batch.json | json | web call 17 | raw S2 batch cross-validation | on_disk | audit trail |
| r0004_inspire.json | json | web calls 18–19 | raw INSPIRE responses | on_disk | audit trail |
| r0006_gapfill.json | json | web calls 27–28 | raw gap-fill + adversarial results | on_disk | audit trail |
| scripts_run_arxiv_queries.py | py | — | reproducibility of R0002 queries | on_disk | audit trail |

graph_mode is OFF: no relation ledger / graph files are planned for this run.
