# Search Budget Contract

| field | value |
|---|---|
| token policy | strict |
| max answer tokens | n/a (benchmark arm) |
| max artifact tokens / file size | minimal sufficient |
| max search rounds | 1 (+ resume optional) |
| max sources/databases | 5 channel families |
| max screened candidates | 40 |
| max full-text reads | 6 PDFs (C3 gate) |
| max wall-clock time | single session |
| graph required | no |
| human labeling budget | 0 |
| stop criterion | facet saturation partial OR call cap; honest coverage report |

## Token Allocation

| stage | planned budget | actual budget | notes |
|---|---:|---:|---|
| scope and criteria | 2 calls | 2 | calls 1–2 |
| route generation | 3 calls | 0 | folded into keyword/matrix setup (local) |
| retrieval | 28 calls | 23 | searches + fetches + 1 failed |
| screening | 0 calls | 0 | local from logged hits |
| full-text / claim verification | 6 calls | 6 | PDF downloads calls 15–20 |
| graph construction | 0 | 0 | graph_mode OFF |
| synthesis / report | 3 calls | 4 | calls 21–25 (includes failed arXiv search) |

**Total web calls:** 25/40 (ledger authoritative)
