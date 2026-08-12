# Search Budget Contract

| field | value |
|---|---|
| token policy | balanced |
| max answer tokens | not enforced by the run harness |
| max artifact tokens / file size | ~40 KB per artifact typical; unbounded floor |
| max search rounds | 5 (R0001 through R0005) |
| max sources/databases | 4 distinct channels (arXiv, INSPIRE-HEP, OpenAlex, Semantic Scholar attempted) |
| max screened candidates | ~90 (58 seed refs + 30 coverage-search entries) |
| max full-text reads | ≥ 6 core PDFs downloaded to sources/pdfs/ |
| max wall-clock time | not tracked (single agent session) |
| graph required | no (graph_mode OFF per task instructions) |
| human labeling budget | 0 (autonomous run) |
| stop criterion | (i) 40-call cap reached, or (ii) ≥6 PDFs on disk + ≥3 channels executed + each of 3 facets ≥3 include papers + forward-citation channel checked + marginal yield decision-neutral |

## Token / Web-Call Allocation

`actual` column backfilled from the `round_log.md` call ledger at stop.

| stage | planned budget | actual budget | notes |
|---|---:|---:|---|
| scope and criteria | 0 | 0 | drafted from skill contract only |
| route generation | 0 | 0 | drafted from reference 34 channel families |
| retrieval (seed) | 3 | 3 | arXiv abs + INSPIRE record + OpenAlex |
| retrieval (PDF core set) | 8 | 8 | 8 arXiv PDFs downloaded to sources/pdfs/ |
| coverage search (Facet A/B/C) | 3 | 3 | INSPIRE flow + INSPIRE diffusion + arXiv API sampler-with-correction |
| forward-citation | 1 | 1 | INSPIRE refersto — returned 0 citing papers |
| Semantic Scholar third-channel (failed) | 1 | 1 | HTTP 429; substituted with OpenAlex |
| arXiv listing (failed) | 1 | 1 | HTTP 403; substituted with INSPIRE fulltext + arXiv API |
| screening / synthesis | 0 | 0 | local processing only |
| graph construction | 0 | 0 | graph_mode OFF |
| synthesis / report | 0 | 0 | local processing |
| **total** | **17** | **17** | 17 / 40; residual = 23 calls unused (stop chosen when marginal yield went decision-neutral, not because of budget exhaustion) |

## Stop Rationale (mirrors coverage_stopping_report.md)

Stopped at 17 / 40 web calls. Reasons:

1. Seed identity verified on three distinct channels (arXiv, INSPIRE-HEP, OpenAlex).
2. ≥6 core PDFs on disk (8 total, 618 KB – 4.18 MB each, all valid %PDF-1.5).
3. Each of the three facets has ≥3 include papers with C1+ evidence, with several C3.
4. Forward-citation channel returned 0 citing papers (seed is very new — recorded as scope limitation, not called "complete").
5. Two coverage searches (INSPIRE fulltext for flows + diffusion) both returned lists whose overlap with the seed's reference list was ≥50%, and the potentially-missed candidates that emerged (P0060–P0074) are recorded at C1 metadata-only. Additional queries at the same specificity are expected to return further overlapping content or off-topic gamma-ray / neutrino / autodiff false positives.
6. Adversarial arXiv API pass for "(neural sampler | learned sampler) AND (importance weight | MH | reweighting | Jarzynski)" returned only 2 items (seed itself + IWSM 2505.19431).

The unused 23 calls are held rather than spent on decision-neutral queries so that the honest scope-limited coverage report remains truthful and this run demonstrates budget-aware stopping rather than budget-maximizing exhaustion.
