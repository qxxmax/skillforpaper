# Search Route Log

## Route Plan

| route id | route family | source | query / action | expected strength | expected blind spot | status |
|---|---|---|---|---|---|---|
| RT1 | backward citation | arXiv API (`id_list`) | verify the seed's 58-entry bibliography | highest precision; the seed's own view of its ancestry | inherits every gap in the seed's reading | executed (Q00-bib, Q09-bib2) |
| RT2 | lexical, domain-locked | arXiv API | one query per facet with `cat:` or phrase lock | recall independent of the seed | phrasing drift; only the first 50–60 of each result set retrieved | executed (Q01, Q02, Q03, Q12) |
| RT3 | lexical, exact title | arXiv API | resolve method names seen as text mentions | turns C0 names into identifiers | only finds what was already named somewhere | executed (Q10, Q11) |
| RT4 | identifier cross-validation | Semantic Scholar batch | 37 core identifiers in one call | second channel for the whole core set at once | S2 metadata can lag or vary in title form | executed (Q04) |
| RT5 | forward citation | Semantic Scholar citations | descendants of the seed and of NETS | finds 2026 frontier work no keyword list anticipates | S2-scoped; citation graphs are incomplete for very recent preprints | executed (Q05, Q13) |
| RT6 | domain database | INSPIRE-HEP | two topic queries | hep-lat precision; catches grey literature | title-field search is narrow; weak outside hep | executed (Q06, Q07) |
| RT7 | identifier resolver | Crossref | 8 core DOIs | authoritative publisher metadata | verifies existence, not relevance | executed (Q14) |
| RT8 | publisher / venue page | Springer, SciPost | landing pages for core records | strongest identity evidence | anti-bot walls | partly blocked (Q15 ok, Q16 blocked) |
| RT9 | general web | web search | benchmark/survey framing | catches survey framing the APIs bury | secondary sources; no identifiers | executed (Q08) |
| RT10 | Google Scholar / OpenAlex / WoS | — | index-overlap estimate | independent index for recall estimation | — | **not executed** (budget and access); recorded as a residual risk |

## Query / Retrieval Log

| date | route id | source | query / action | filters | hits | unique new | included after screen |
|---|---|---|---|---|---:|---:|---:|
| 2026-08-12 | RT1 | arXiv API | Q00-bib: 32 seed-bibliography identifiers | id_list | 32 | 32 | 32 |
| 2026-08-12 | RT2 | arXiv API | Q01: normalizing flow / trivializing map / neural sampler / ML sampler | cat:hep-lat | 84 matched, 60 retrieved | 54 | 33 (27 new) |
| 2026-08-12 | RT2 | arXiv API | Q02: Boltzmann generator / annealed flow transport / unnormalized target / neural sampler / unnormalized densities | cat:cs.LG, stat.ML, stat.CO | 184 matched, 60 retrieved | 57 | 17 (15 new) |
| 2026-08-12 | RT2 | arXiv API | Q03: Jarzynski / independence Metropolis / neural importance sampling / AIS / asymptotically unbiased | AND domain phrases | 32 matched, 32 retrieved | 21 | 19 (8 new) |
| 2026-08-12 | RT4 | Semantic Scholar | Q04: batch of 37 identifiers | — | 37 | 1 | 36 (1 new) |
| 2026-08-12 | RT5 | Semantic Scholar | Q05: citations of 2606.13790 | — | 3 | 3 | 3 (3 new) |
| 2026-08-12 | RT6 | INSPIRE-HEP | Q06: sampler × lattice/gauge × neural/ML/flow/diffusion/generative | title fields | 8 | 2 | 7 (2 new) |
| 2026-08-12 | RT6 | INSPIRE-HEP | Q07: "stochastic quantization" × diffusion/neural/ML/sampler/generative | — | 11 | 7 | 7 (3 new) |
| 2026-08-12 | RT9 | web search | Q08: neural-sampler benchmark/survey framing | — | 5 pages | — | 0 direct; 4 method names to resolve |
| 2026-08-12 | RT1 | arXiv API | Q09-bib2: 31 newly surfaced identifiers | id_list | 31 | 3 | 31 (3 new) |
| 2026-08-12 | RT3 | arXiv API | Q10: 7 exact method titles | ti: | 15 | 15 | 7 (7 new) |
| 2026-08-12 | RT3 | arXiv API | Q11: 7 exact precursor/critique titles | ti: | 31 | 26 | 9 (7 new) |
| 2026-08-12 | RT7 | Crossref | Q14: 8 core DOIs | filter=doi | 8 | 0 | 8 (0 new; cross-validation only) |
| 2026-08-12 | RT8 | SciPost | Q16: SciPostPhys.15.6.238 | — | **blocked** | 0 | 0 |
| 2026-08-12 | RT8 | Springer | Q15: 10.1007/JHEP07(2022)015 | — | 1 | 0 | 1 (cross-validation only) |
| 2026-08-12 | RT2 | arXiv API | Q12: hep-lat × diffusion/score-based/stochastic quantization/generative | cat:hep-lat | 108 matched, 50 retrieved | 34 | 19 (4 new) |
| 2026-08-12 | RT5 | Semantic Scholar | Q13: citations of 2410.02711 | limit 100 | 68 | 43 | 15 (**0 new**) |

Totals: 452 raw records returned, 298 distinct after deduplication by arXiv
identifier, 112 labeled include.

## Route Coverage Notes

| route id | seed items recovered | new facets found | duplicate with other routes | residual blind spot |
|---|---|---|---|---|
| RT1 backward | all six families the seed names | none by construction | 32 of 32 later re-confirmed by RT4 | cannot find anything the seed did not read |
| RT2 lexical | **the seed itself** (Q01 and Q03), plus flows, SNF, diffusion-for-LFT | trivializing maps; annealed flow transport; Boltzmann generators | 54/60, 57/60, 21/32 first-seen — i.e. RT2 is the main discovery engine | truncated at 50–60 of up to 184 matches per query |
| RT3 title | — | precursor layer 1998–2018; scalability critique | 26 of 31 first-seen in Q11 | only resolves names already encountered |
| RT4 cross-validation | — | none (by design) | 36 of 37 already seen | S2-only records stay at C1 |
| RT5 forward | — | 2026 frontier; one bridge node (2607.15682) | Q13: 43 of 67 first-seen but **0 new includes** | forward expansion done on 2 nodes only |
| RT6 INSPIRE | seed re-confirmed | one grey-literature record | 2 of 7 and 7 of 11 first-seen | title-only matching; 8 and 11 hits are small |
| RT7 Crossref | — | none | all 8 known | metadata only |
| RT8 publisher | — | none | 1 known | one of two publishers blocked |
| RT9 web | — | 4 method names (later resolved by RT3) | — | no identifiers of its own |

Route overlap: 83 of 298 distinct records (28%) were returned by two or more
independent routes; the seed itself was returned by three (RT1 identifier, RT2
lexical ×2, RT6 domain database).
