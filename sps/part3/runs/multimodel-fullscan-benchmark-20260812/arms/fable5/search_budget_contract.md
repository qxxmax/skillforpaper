# Search Budget Contract

| field | value |
|---|---|
| token policy | balanced |
| max answer tokens | n/a (benchmark; one-paragraph final answer) |
| max artifact tokens / file size | no hard cap; keep files concise |
| max search rounds | 6 |
| max sources/databases | 4-5 channel families |
| max screened candidates | ~60 |
| max full-text reads | 8 (≥6 core PDFs mandatory) |
| max wall-clock time | single session |
| graph required | no (graph_mode OFF per task) |
| human labeling budget | none |
| stop criterion | 40-web-call hard cap OR facet saturation (no new method family for 2 consecutive rounds), whichever first; honest residual-risk report at stop |

## Web Call Allocation (HARD CAP: 40 calls total)

The call ledger in `round_log.md` is the only authoritative counter. Backfill
the `actual` column from it at stop.

| stage | planned budget | actual budget | notes |
|---|---:|---:|---|
| seed verification (arXiv abs + PDF of 2606.13790) | 3 | 2 | ledger rows 1-2 |
| lexical searches (arXiv API, web search) | 10 | 9 | ledger rows 3-9 (arXiv API), 23-24 (web search) |
| citation expansion (Semantic Scholar refs/citations) | 5 | 3 | ledger rows 10-12 (row 11 failed 429, counted) |
| channel cross-check (INSPIRE-HEP) | 3 | 2 | ledger rows 13-14 |
| identity verification fetches (abs/DOI pages) | 10 | 0 | folded into the single S2 batch call (row 10) — large saving vs plan |
| core PDF downloads (C3 gate, ≥6) | 7 | 8 | ledger rows 15-22 (9 PDFs total incl. seed) |
| reserve / retries | 2 | 0 | unused |
| **total** | **40** | **24** | stopped saturated_under_budget at 24/40; backfilled from round_log.md call ledger 2026-08-12 |
