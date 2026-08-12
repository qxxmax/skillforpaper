# Search Route Log

## Route Plan

| route id | route family | source | query / action | expected strength | expected blind spot | status |
|---|---|---|---|---|---|---|
| RT01 | identifier | arxiv.org abs + PDF | verify seed 2606.13790, download PDF | seed identity + reference list | none | executed |
| RT02 | lexical | arXiv API (export.arxiv.org) | axis-crossed queries from query_matrix.csv | recall across all 3 facets | non-arXiv venues, indexing lag | executed (calls 3-11, 28) |
| RT03 | citation | Semantic Scholar API | backward refs + forward citations of seed and core papers | lineage recovery | S2 coverage gaps, rate limits | executed (calls 13-17; one 429) |
| RT04 | domain-database cross-validation | INSPIRE-HEP API | verify hep-lat core records via second channel | independent confirmation for F2 | weak outside HEP | executed (calls 18-19) |
| RT05 | identifier | arxiv.org abs pages | C2 abstract checks for screened-in candidates | promotion evidence | counts against budget per page | merged into RT01/RT06 (no separate abs-page calls needed) |
| RT06 | full-text | arxiv.org PDF | download ≥6 core PDFs | C3 gate | large files; budget | executed (calls 20-26) |

## Query / Retrieval Log

| date | route id | source | query / action | filters | hits | unique new hits | included after screen | notes |
|---|---|---|---|---|---:|---:|---:|---|
| 2026-08-12 | RT01 | arxiv.org | fetch abs + PDF of 2606.13790 | — | 1 | 1 | 1 | seed verified C3; 58 bib refs extracted (calls 1–2) |
| 2026-08-12 | RT02 | arXiv API | Q001 | max 30, relevance | 47 | 4 | 3 | call 3 |
| 2026-08-12 | RT02 | arXiv API | Q002 | max 30, relevance | 17 | 3 | 2 | call 4 |
| 2026-08-12 | RT02 | arXiv API | Q003 | max 30, relevance | 20 | 5 | 4 | call 5; P0014 ID recovered |
| 2026-08-12 | RT02 | arXiv API | Q004 | max 30, relevance | 6 | 3 | 3 | call 6 |
| 2026-08-12 | RT02 | arXiv API | Q005 | max 30, relevance | 50 | 2 | 1 | call 7; heavy MD noise |
| 2026-08-12 | RT02 | arXiv API | Q006 | max 30, relevance | 23 | 5 | 4 | call 8; seed recalled |
| 2026-08-12 | RT02 | arXiv API | Q007 | max 30, relevance | 6 | 2 | 1 | call 9 |
| 2026-08-12 | RT02 | arXiv API | Q008 | max 30, relevance | 3762 | 6 | 5 | call 10; noisy query |
| 2026-08-12 | RT02 | arXiv API | Q009 | max 30, relevance | 32 | 4 | 3 | call 11 |

## Route Coverage Notes

| route id | seed items recovered | new facets found | duplicate with other routes | residual blind spot |
|---|---|---|---|---|
| RT01 | seed itself + 40 backward candidates | all 3 facets seeded | — | none for seed |
| RT02 | seed re-found by Q006 (recall PASS) | trivializing maps, Jarzynski-for-LGT, AFT/CRAFT/FAB, Boltzmann generators | heavy overlap with RT01 on F2 core (good) | non-arXiv venues; GAN-for-LFT line missed |
| RT03 | all 63 pooled IDs resolved; 3 seed citations | mechanism roots (AIS, SMC), learned-MCMC family | overlaps RT01/RT02 on core | only first 100 fwd citations of P0002; other cores not expanded |
| RT04 | 12/13 core hep-lat records | none (validation route) | by design | 2002.06707 not indexed; weak outside HEP |
| RT06 | 8 PDFs incl. seed | C3 evidence | — | paywalled/published versions not fetched |

Also logged: RT02 adversarial query (call 28) and RT03/RT04 identifier gap-fill (call 27).
