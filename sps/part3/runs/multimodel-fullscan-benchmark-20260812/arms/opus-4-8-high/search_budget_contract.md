# Search Budget Contract

| field | value |
|---|---|
| token policy | balanced |
| max answer tokens | one-paragraph final report |
| max artifact tokens / file size | small markdown/csv files |
| max search rounds | 4 |
| max sources/databases | >=3 channels (arXiv, Semantic Scholar, INSPIRE, publisher/DOI, web search) |
| max screened candidates | ~30 |
| max full-text reads | 8 (>=6 downloaded PDFs) |
| max wall-clock time | single session |
| graph required | no (graph_mode OFF) |
| human labeling budget | manual screening of ~30 candidates |
| stop criterion | facet quotas met + saturation, or 40-web-call cap |

## Token / Call Allocation

`planned budget` and `actual budget` are in **web calls** (the scored budget).
Actuals backfilled from the round_log.md call ledger at stop.

| stage | planned budget | actual budget | notes |
|---|---:|---:|---|
| scope and criteria | 0 | 0 | local reasoning only |
| route generation | 0 | 0 | local reasoning only |
| retrieval (search) | 12 | 3 | ledger rows #2, #12, #13 (seed + 2 adversarial searches) |
| screening | 0 | 0 | local screening of returned metadata (free) |
| full-text / claim verification | 24 | 11 | rows #1 (seed abs/full text), #3 & #14 (S2 batches), #4 (INSPIRE), #5–#11 (7 PDF downloads) |
| graph construction | 0 | 0 | graph_mode OFF |
| synthesis / report | 4 | 0 | local synthesis only |
| **total** | **40** | **14** | 14/40 used; stopped under budget at facet saturation |
