# Search Route Log

## Route Plan

| route id | route family | source | query / action | expected strength | expected blind spot | status |
|---|---|---|---|---|---|---|
| RT1 | domain database + identifier | arXiv abs/HTML | fetch seed 2606.13790 | authoritative seed text + full bib | forward citations absent | done |
| RT2 | lexical / web | web search | seed title | confirm identity, find mirrors | ranking noise | done |
| RT3 | bibliographic graph | Semantic Scholar API | batch metadata for bib arXiv IDs | cross-validate venue/DOI at scale | S2 indexing lag | done |
| RT4 | domain database | INSPIRE-HEP API | record lookup (physics) | independent HEP confirmation | ML-venue papers weakly indexed | done |
| RT5 | full-text acquisition | arXiv PDF | download 7 core PDFs | C3 evidence | download-only, no OCR anchors | done |
| RT6 | adversarial / topic expansion | web search | out-of-bib families (Boltzmann Gen, FAB, AFT) | catch missed adjacent families | recall depends on query terms | done |

## Query / Retrieval Log

| date | route id | source | query / action | filters | hits | unique new | included after screen | notes |
|---|---|---|---|---|---:|---:|---:|---|
| 2026-08-12 | RT1 | arXiv | fetch abs/html 2606.13790 | — | 1 | 1 | 1 | + ~57 bib entries |
| 2026-08-12 | RT2 | web | "Stochastic Path Sampler" LFT | — | 5 | 0 | 0 | seed mirrors only |
| 2026-08-12 | RT3 | S2 API | batch 12 arXiv IDs | fields=title,year,venue,externalIds | 12 | 0 | 12 | all cross-validated |
| 2026-08-12 | RT4 | INSPIRE | arxiv:2003.06413 | — | 1 | 0 | 1 | PRL confirmed |
| 2026-08-12 | RT5 | arXiv | 7 PDF downloads | — | 7 | 0 | 7 | C3 evidence |
| 2026-08-12 | RT6 | web | Boltzmann generators Noe | — | 5 | 1 | 1 | 1812.01729 (out-of-bib) |
| 2026-08-12 | RT6 | web | annealed flow transport / FAB | — | 5 | 3 | 3 | 2208.01893, 2111.11510, AFT |
| 2026-08-12 | RT3 | S2 API | batch 7 adjacent arXiv IDs | — | 7 | 0 | 6 | cross-validated adjacent F1 |

## Route Coverage Notes

| route id | seed items recovered | new facets found | duplicate with other routes | residual blind spot |
|---|---|---|---|---|
| RT1 | seed + full lineage | F1/F2/F3 seeds | — | forward citations not covered |
| RT3 | 18 records | none new (validation) | high with RT1 bib | S2 lag for 2026 preprints |
| RT4 | 1 | none new | with RT1/RT3 | HEP-only scope |
| RT5 | 7 | full-text depth | with RT1/RT3 | only 7 of ~26 in-scope |
| RT6 | — | Boltzmann Gen, FAB, AFT | low (out-of-bib) | molecular/SMC subfields partial |
