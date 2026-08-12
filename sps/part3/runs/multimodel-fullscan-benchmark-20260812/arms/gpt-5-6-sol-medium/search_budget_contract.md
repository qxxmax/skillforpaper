# Search Budget Contract

| field | value |
|---|---|
| token policy | balanced |
| max search rounds | 7 substantive rounds |
| max sources/databases | at least 3 distinct channels |
| max screened candidates | 368 deduplicated groups |
| max full-text reads | 8 core PDFs |
| graph required | no (graph_mode OFF) |
| stop criterion | facet/channel/seed closure or named-risk stop before 40 calls |

| stage | planned calls | actual calls | ledger rows |
|---|---:|---:|---|
| seed page | 2 | 1 | 1 |
| lexical/domain searches | 9 | 10 | 3–8, 11, 19–21 |
| bibliographic/citation/author/metadata | 8 | 7 | 9–10, 22–26 |
| forward official pages | 9 | 2 | 31–32 |
| core PDF downloads | 8 | 8 | 2, 12–18 |
| adversarial/closure | 4 | 4 | 27–30 |
| **Total** | **40** | **32** | **1–32** |

Actuals were backfilled from `round_log.md`. Eight calls remained unused after scoped decision sufficiency.
