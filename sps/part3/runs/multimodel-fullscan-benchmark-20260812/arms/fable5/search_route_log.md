# Search Route Log

## Route Plan

| route id | route family | source | query / action | expected strength | expected blind spot | status |
|---|---|---|---|---|---|---|
| RT1 | identifier | arXiv abs + PDF | verify seed 2606.13790, extract references | authoritative seed identity + G1-backward for free | none for seed | done (calls 1-2) |
| RT2 | lexical | arXiv API | axis-crossed keyword queries Q003-Q009 | precise arXiv-native recall for non-cited families | non-arXiv venues, synonym drift | done (calls 3-9) |
| RT3 | citation | Semantic Scholar API | batch identity verify + forward citations (Q010-Q012) | lineage recall independent of keywords; 2nd channel | S2 indexing lag; rate limits (hit once, 429) | done (calls 10-12) |
| RT4 | domain database | INSPIRE-HEP API | seed check + hep-lat topical search (Q013-Q014) | HEP-native coverage, venue metadata; 3rd channel | weak outside HEP | done (calls 13-14) |
| RT5 | web search | general web search | adversarial limitation + benchmark queries (Q015-Q016) | catches publisher pages, reviews, negative results | noisy; some hits lack arXiv IDs | done (calls 23-24) |
| RT6 | PDF acquisition | arXiv | 8 core PDF downloads | C3 gate | — | done (calls 15-22) |

## Query / Retrieval Log

| date | route id | source | query / action | filters | hits | unique new hits | included after screen | notes |
|---|---|---|---|---|---:|---:|---:|---|
| 2026-08-12 | RT1 | arXiv | Q001 abs page fetch | — | 1 | 1 | 1 | full HTML text + 38 in-scope bib refs harvested |
| 2026-08-12 | RT1 | arXiv | Q002 PDF download | — | 1 | 0 | 1 | 33 pp |
| 2026-08-12 | RT2 | arXiv API | Q003 NF x LFT | max 25, relevance | 25 | 21 | 8 | 4 dups with bib |
| 2026-08-12 | RT2 | arXiv API | Q004 Boltzmann generator / neural sampler | max 25 | 25 | 25 | 1 | 22 monitor overflow |
| 2026-08-12 | RT2 | arXiv API | Q005 AFT / FAB / AIS+neural | max 25 | 11 | 11 | 4 |  |
| 2026-08-12 | RT2 | arXiv API | Q006 trivializing map | max 25 | 25 | 25 | 4 | heavy math noise |
| 2026-08-12 | RT2 | arXiv API | Q007 neural IS unbiased lattice | max 25 | 0 | 0 | 0 | over-restrictive |
| 2026-08-12 | RT2 | arXiv API | Q008 L2HMC family | max 25 | 13 | 13 | 4 |  |
| 2026-08-12 | RT2 | arXiv API | Q009 self-learning MC | max 25 | 15 | 15 | 2 |  |
| 2026-08-12 | RT3 | S2 API | Q010 batch verify 46 IDs | — | 46 | 0 | 0 | verification, not discovery |
| 2026-08-12 | RT3 | S2 API | Q011 seed record | — | 0 | 0 | 0 | HTTP 429 logged |
| 2026-08-12 | RT3 | S2 API | Q012 seed citations | — | 3 | 3 | 0 | descendants → monitor |
| 2026-08-12 | RT4 | INSPIRE | Q013 seed record | — | 1 | 0 | 0 | 3rd-channel seed confirmation |
| 2026-08-12 | RT4 | INSPIRE | Q014 LFT sampler search | size 40, mostcited | 8 | 2 | 2 | seed self-recovered |
| 2026-08-12 | RT6 | arXiv | 8 PDF downloads | — | 8 | 0 | 0 | C3 gate |
| 2026-08-12 | RT5 | web search | Q015 adversarial limitations | — | 5 | 2 | 2 | E0017 |
| 2026-08-12 | RT5 | web search | Q016 sampler benchmarks | — | 5 | 1 | 1 | E0018 |

## Route Coverage Notes

| route id | seed items recovered | new facets found | duplicate with other routes | residual blind spot |
|---|---|---|---|---|
| RT1 | seed | F1/F2/F3 skeleton via bib | — | bib reflects authors' framing; non-cited families invisible |
| RT2 | 4 bib papers re-found | trivializing maps, Boltzmann generators, AFT/FAB, L2HMC, SLMC | overlaps RT1 on SNF/fermionic/etc. | non-arXiv venues; phrase-dependent recall |
| RT3 | 46/46 batch IDs confirmed | descendants (3) | high overlap by design | S2 rate limits; very recent items may lag |
| RT4 | seed self-recovered in topical search | scaling-critique cluster (P0069) | 2 hits overlapped RT2 | INSPIRE topical search returned only 8 items — narrow title-based query |
| RT5 | — | limitation + benchmark clusters | 1 hit overlapped RT2 (2302.14082) | publisher-page hits without arXiv IDs kept at C1/C2 |
