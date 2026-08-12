# Search Budget Contract

| field | value |
|---|---|
| token policy | balanced |
| max answer tokens | n/a (file artifacts only) |
| max artifact tokens / file size | keep run files inspectable |
| max search rounds | 4 (R0–R3) |
| max sources/databases | ≥3 distinct (arXiv, INSPIRE, S2/OpenAlex); Crossref used |
| max screened candidates | 40 |
| max full-text reads | ≥6 C3 PDFs |
| max wall-clock time | single session |
| max web calls | **40** (hard) |
| graph required | no (graph_mode OFF) |
| human labeling budget | screen include/exclude/monitor only |
| stop criterion | channels searched/substituted; ≥6 C3; marginal yield low OR budget near exhaust; residual risk recorded |

## Token / Call Allocation

| stage | planned budget (calls) | actual | notes |
|---|---:|---:|---|
| scope and criteria | 0 | **0** | local files |
| route generation / keyword ontology | 1–2 | **2** | seed API+PDF (also retrieval) |
| retrieval (multi-channel) | 12–18 | **18** | arXiv/INSPIRE/OA/S2 attempts |
| screening | 0 | **0** | local |
| full-text / claim verification (PDF) | 6–10 | **7** | seed+6 neighbors |
| citation / author snowball | 4–8 | **6** | INSPIRE/S2/Crossref |
| failed / retries | — | **5** | http empty×2; S2 429×2; OA invalid×1 (counted in stages above; total still 33) |
| synthesis / report | 0 | **0** | local |
| **TOTAL** | **≤40** | **33** | stop with 7 unused |

## Actual column (at stop)

- **actual web calls:** 33/40  
- **actual C3 PDFs:** 7  
- **actual distinct channels with ≥1 successful informative response:** arXiv, INSPIRE, Semantic Scholar, OpenAlex, Crossref  
- **actual stop:** saturated_under_budget with known risk (see coverage_stopping_report.md)
