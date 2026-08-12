# Round Log — opus-4-7-xhigh arm

Each row of the call ledger below is authoritative for the 40-call web budget.
`research_state.md` mirrors this counter; when the two disagree, this ledger
wins. Retries, failed calls, and blocked calls all count (see reference 33).

## Call Ledger

| # | RoundID | type | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed title + abstract + 58 refs | 1/40 |
| 2 | R0001 | search | https://inspirehep.net/api/literature?q=arxiv:2606.13790&fields=titles,authors,arxiv_eprints,references | INSPIRE record with 58 structured refs; cross-validates seed identity | 2/40 |
| 3 | R0002 | fetch | https://api.semanticscholar.org/graph/v1/paper/arXiv:2606.13790?fields=... | HTTP 429 rate limit; no yield; third channel blocked | 3/40 |
| 4 | R0003 | fetch | https://arxiv.org/pdf/1904.12072 | 884944 B PDF (Albergo-Kanwar-Shanahan 2019) | 4/40 |
| 5 | R0003 | fetch | https://arxiv.org/pdf/2111.15141 | 2713763 B PDF (Zhang-Chen PIS) | 5/40 |
| 6 | R0003 | fetch | https://arxiv.org/pdf/2302.13834 | 4179526 B PDF (Vargas et al. DDS) | 6/40 |
| 7 | R0003 | fetch | https://arxiv.org/pdf/2007.07115 | 618576 B PDF (Nicoli et al. 2021) | 7/40 |
| 8 | R0003 | fetch | https://arxiv.org/pdf/2201.08862 | 899741 B PDF (Caselle et al. SNF 2022) | 8/40 |
| 9 | R0003 | fetch | https://arxiv.org/pdf/2410.02711 | 2113233 B PDF (Albergo-Vanden-Eijnden NETS) | 9/40 |
| 10 | R0003 | fetch | https://arxiv.org/pdf/2309.17082 | 2486741 B PDF (Wang-Aarts-Zhou 2024) | 10/40 |
| 11 | R0003 | fetch | https://arxiv.org/pdf/2003.06413 | 1017965 B PDF (Kanwar et al. 2020) | 11/40 |
| 12 | R0004 | search | https://arxiv.org/list/hep-lat/2606 | HTTP 403; substituted with INSPIRE fulltext + arXiv API | 12/40 |
| 13 | R0004 | fetch | https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2606.13790 | third-channel seed identity; cited_by_count=0; hep-lat topic; CC-BY | 13/40 |
| 14 | R0004 | search | https://inspirehep.net/api/literature?q=refersto:arxiv:2606.13790 | 0 forward citations (only seed itself via OR clause) | 14/40 |
| 15 | R0005 | search | https://inspirehep.net/api/literature?q=fulltext:"normalizing flow" AND hep-lat AND de>=2023 | 69 hits; ~12 potentially-missed pre-seed candidates | 15/40 |
| 16 | R0005 | search | https://inspirehep.net/api/literature?q=fulltext:"diffusion model" AND hep-lat AND de>=2024 | 38 hits; ~5 potentially-missed candidates including 2607.21436 SQ-as-Optimal-Control | 16/40 |
| 17 | R0005 | search | http://export.arxiv.org/api/query?search_query=(abs:"neural sampler" OR abs:"learned sampler") AND (abs:"importance weight" OR abs:"Metropolis-Hastings" OR abs:"reweighting" OR abs:"Jarzynski") | 2 hits total (seed + Importance Weighted Score Matching 2505.19431) | 17/40 |

Calls used: **17 / 40**. Residual budget: **23 calls**. Stop chosen when marginal yield went decision-neutral, not by budget exhaustion.

## R0001 — Seed verification

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** verify seed identity, extract seed reference list.

### Diagnosis
Nothing loaded yet; seed identity is the only precondition for keyword provenance.

### Chosen Action
Fetch arXiv abs (call 1) and INSPIRE record (call 2).

### Execution Result
- Seed identity confirmed on 2 channels (arXiv + INSPIRE).
- 58 references extracted (INSPIRE structured); 34 seed terms (T001-T034) recorded in `keyword_ledger.csv` with source_anchor provenance.
- Seed abstract quote (E0013) explicitly names the PIS / DDS / CMCD / NETS ML lineage and the "trajectory-level Independence Metropolis–Hastings correction" — anchors all three facets in-scope.

### File Patches
- output_manifest.md, research_state.md, round_log.md — created (this round).
- keyword_ledger.csv — created with 34 seed terms.

### Next Best Action
Cross-validate seed on a third distinct channel; download 6+ core PDFs.

### Stop Decision
continue.

## R0002 — Third-channel identity check

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** Semantic Scholar cross-validation of seed identity.

### Diagnosis
Seed identity verified on 2 channels; per reference 34 cross-validation rule, prefer ≥2 independent confirmations; 3 preferred for robustness.

### Chosen Action
Semantic Scholar API for arXiv:2606.13790 (call 3).

### Execution Result
- HTTP 429 (rate-limited without API key).
- Per blocked-channel substitution rule (reference 34), will substitute with OpenAlex in R0004.

### File Patches
- round_log.md updated with call 3 (failed).

### Stop Decision
continue with substitution.

## R0003 — Core-PDF batch

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** download ≥6 core PDFs spanning Facets A, B, and C.

### Diagnosis
Landscape task requires C3 evidence for representative works.

### Chosen Action
Download 8 arXiv PDFs (calls 4-11) selected to span all three facets:
- Facet B foundational: 1904.12072, 2003.06413, 2007.07115.
- Facet B + Facet C bridge (LFT + reweighting): 2201.08862, 2309.17082.
- Facet A ancestors: 2111.15141 (PIS), 2302.13834 (DDS).
- Facet A + Facet C explicit: 2410.02711 (NETS).

### Execution Result
- All 8 PDFs land on disk (integrity: %PDF-1.5 header, sizes 618 KB – 4.18 MB, page-object counts 6–32).
- 8 new C3 evidence rows (E0005–E0012).
- Facets A, B, C each have ≥3 C1+ include papers already.

### File Patches
- sources/pdfs/ populated.
- evidence_registry.md — created with 12 rows.
- candidate_pool.md — created with 47 include + 12 exclude + candidate/monitor tail placeholders.

### Stop Decision
continue.

## R0004 — Third channel + forward citation

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** substitute for Semantic Scholar, close forward-citation gap.

### Diagnosis
Semantic Scholar remains blocked; OpenAlex is a good third bibliographic-graph channel. Forward citations must be checked before stopping.

### Chosen Action
- Attempt arXiv listing (call 12) as a topic-listing route.
- OpenAlex works record (call 13) for third-channel seed identity.
- INSPIRE refersto (call 14) for forward citations.

### Execution Result
- arXiv listing blocked (HTTP 403); substituted with INSPIRE fulltext and arXiv API in R0005.
- OpenAlex confirms seed (W7164828431, hep-lat topic, CC-BY, cited_by_count=0) — third channel achieved.
- INSPIRE refersto returned 0 forward citations (only seed via OR clause). Consistent with OpenAlex.

### File Patches
- evidence_registry.md — E0003 and E0004 added.
- search_route_log.md — created.

### Stop Decision
continue for one coverage round.

## R0005 — Coverage search + adversarial pass

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** probe for pre-seed adjacent literature NOT in the seed's reference list.

### Diagnosis
Seed's own reference list already covers the ML + LFT lineage well; still need to check for potentially-missed same-topic papers.

### Chosen Action
- INSPIRE fulltext "normalizing flow" AND hep-lat AND de>=2023 (call 15).
- INSPIRE fulltext "diffusion model" AND hep-lat AND de>=2024 (call 16).
- arXiv API narrow adversarial phrase for Facet A + Facet C (call 17).

### Execution Result
- 69 flow + 38 diffusion hits; overlap with seed refs high; residual pre-seed candidates recorded as P0060–P0074 at C1 metadata-only.
- Adversarial arXiv API pass returned 2 total (seed + IWSM 2505.19431); IWSM added as P0060.
- Marginal yield: decision-neutral for the "predecessor set shape" claim; new candidates are density additions, not clustering additions.

### File Patches
- candidate_pool.md — P0060–P0080 added.
- candidate_screening_table.md — full 90-entry table created.
- coverage_stopping_report.md — created.
- search_budget_contract.md — created with actuals backfilled.
- search_scope.md — created.
- query_matrix.csv, query_yield_log.csv — created.

### Stop Decision
**stopped_with_known_risk** — 17/40 web calls used; further queries expected to be decision-neutral for the landscape claim; 23 calls held in reserve for a follow-on promotion pass.

## Resume Reconciliation

None required; single-session run. `scripts/validate_run_state.py` invocation appended in `research_state.md`.
