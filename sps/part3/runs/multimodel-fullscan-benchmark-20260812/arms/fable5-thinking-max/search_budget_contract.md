# Search Budget Contract

| field | value |
|---|---|
| token policy | balanced |
| max answer tokens | n/a (benchmark: one-paragraph final response) |
| max artifact tokens / file size | no explicit cap; keep files auditable |
| max search rounds | 6 |
| max sources/databases | 4 channel families (arXiv API, Semantic Scholar API, INSPIRE-HEP API, arXiv abs/publisher pages) |
| max screened candidates | ~60 |
| max full-text reads | 8 PDFs (≥6 core PDFs required by C3 gate) |
| max wall-clock time | single session |
| graph required | no (graph_mode OFF) |
| human labeling budget | none (autonomous benchmark arm) |
| stop criterion | budget ≤40 web calls reached OR (seed lineage recovered + 3 facets each ≥3 representatives + marginal yield low); never claim completeness |

## Call Allocation (unit = web calls; HARD CAP 40 total)

| stage | planned budget | actual budget | notes |
|---|---:|---:|---|
| scope and criteria | 0 | 0 | local only |
| seed verification (abs page + PDF of 2606.13790) | 3 | 2 | ledger rows 1–2 |
| route generation | 0 | 0 | local only |
| retrieval: lexical searches (arXiv API) | 10 | 10 | ledger rows 3–11 (9 planned) + 28 (adversarial) |
| retrieval: citation expansion (Semantic Scholar) | 8 | 5 | ledger rows 13–17 (incl. 1 failed 429 + retry) |
| cross-validation (INSPIRE-HEP / arXiv abs pages) | 8 | 4 | ledger rows 12, 18–19, 27 (arXiv id_list + INSPIRE) |
| full-text acquisition (core PDF downloads) | 9 | 7 | ledger rows 20–26; 8 PDFs on disk incl. seed |
| reserve (retries, failures, gap-fill) | 2 | 0 | failure/retry absorbed in S2 line |
| screening | 0 | 0 | local only |
| synthesis / report | 0 | 0 | local only |
| **total** | **40** | **28** | round_log.md call ledger is authoritative (rows 1–28) |
