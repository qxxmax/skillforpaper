# Search Budget Contract

Agreed before searching; `actual` values backfilled at stop from the call ledger
in `round_log.md` (the authoritative counter).

| field | value |
|---|---|
| token policy | balanced |
| max answer tokens | one paragraph final response (task-specified) |
| max artifact tokens / file size | no hard cap; files sized to be auditable |
| max search rounds | 10 planned / 9 used |
| max web calls (hard cap) | **40** |
| max sources/databases | ≥3 distinct channels required; 6 used |
| max screened candidates | no cap; 298 distinct screened |
| max full-text reads | ≥6 required by the C3 gate; 9 downloaded |
| max wall-clock time | single session |
| graph required | no (`graph_mode` off by instruction) |
| human labeling budget | 0 (autonomous run) |
| stop criterion | two consecutive rounds with no new method family, seed recall demonstrated on an independent route, all required channel families searched or marked blocked, residual risk recorded |

## Call Allocation

`planned` was set before round R0003; `actual` is backfilled from the call ledger
with row references.

| stage | planned calls | actual calls | ledger rows | notes |
|---|---:|---:|---|---|
| seed identity and full text | 2 | 2 | 1–2 | no overrun |
| backward-citation verification | 2 | 2 | 3–4 | one HTTP 301 failure consumed a call; the retry succeeded |
| lexical / facet retrieval | 6 | 6 | 5–7, 25, 28, and web row 13 | under budget: batching 3 facets into 3 queries with 50–60 results each replaced ~12 narrow queries |
| cross-validation (second channel) | 3 | 3 | 8, 24, 27 | Semantic Scholar batch + Crossref + Springer |
| forward-citation expansion | 3 | 3 | 9, 10, 29 | one HTTP 400 failure consumed a call |
| domain-database (INSPIRE) | 2 | 2 | 11–12 | as planned |
| identifier resolution of named methods | 2 | 2 | 14–15 | promoted 7 C0 names to verified identifiers |
| full-text acquisition (C3 gate) | 8 | 8 | 16–23 | 8 downloads + the seed PDF already counted in the seed stage = 9 PDFs |
| publisher-page verification | 2 | 2 | 26–27 | one blocked (SciPost), one successful (Springer) |
| reserve / contingency | 10 | 0 | — | **11 calls left unspent** (see stop rationale) |
| **total** | **40** | **29** | rows 1–29 | 3 of the 29 were failed or blocked calls |

## Token / Effort Allocation

| stage | planned share | actual notes |
|---|---|---|
| scope and criteria | small | written once, before searching |
| route generation | small | 13 executed queries recorded in `query_matrix.csv` |
| retrieval | medium | 452 raw records pulled in 29 calls (~15.6 records per call) |
| screening | large | all 298 distinct records labeled; none dropped silently |
| full-text / claim verification | large | 9 PDFs, 260 pages, 18 anchored mechanism sentences |
| graph construction | none | `graph_mode` off |
| synthesis / report | medium | literature matrix, lineage map, coverage report |

## Contract Compliance

- Hard cap respected: 29 of 40, no unlogged calls.
- C3 gate exceeded: 9 PDFs against a required 6, each with a byte/page integrity note.
- Channel minimum exceeded: 6 channels against a required 3.
- Every failed and blocked call is in the ledger (rows 3, 9, 26).
