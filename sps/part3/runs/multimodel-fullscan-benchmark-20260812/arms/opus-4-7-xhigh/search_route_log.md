# Search Route Log

## Route Plan

| route id | route family | source | query / action | expected strength | expected blind spot | status |
|---|---|---|---|---|---|---|
| R-arx-abs | identifier | arXiv | fetch abs for 2606.13790 | authoritative title/abstract/authors/refs | v2+ silently supersedes v1 metadata | executed |
| R-inspire-rec | identifier | INSPIRE-HEP | fetch literature record with references | canonical bibliography with 58 refs, DOI/arXiv per row | ML-only refs (Rezende, Bengio, etc.) sometimes missing DOI/arXiv | executed |
| R-s2-rec | identifier | Semantic Scholar API | fetch paper record via arXiv:2606.13790 | third channel + Corpus/Paper IDs | strict rate limits without API key | executed (429) |
| R-arx-pdf | identifier | arXiv PDF | fetch PDFs for the 8 core papers | full text for C3 | large payloads consume budget; no page-count metadata direct | executed 8/8 |
| R-openalex-rec | identifier | OpenAlex API | fetch works record for seed via DOI | third distinct channel + citation count | metadata for ML-only refs may lag | executed |
| R-inspire-fwd | forward citation | INSPIRE-HEP | refersto:arxiv:2606.13790 | forward citation graph | very-new-paper 0-hit false negative | executed |
| R-arx-listing | topic | arXiv listing | list/hep-lat/2606 | contemporaneous LFT papers | blocked with 403 | executed (403) |
| R-inspire-flow | topic | INSPIRE-HEP | fulltext "normalizing flow" AND hep-lat AND de>=2023 | recent LFT flow papers not in seed refs | fulltext coverage limited to indexed papers | executed |
| R-inspire-diff | topic | INSPIRE-HEP | fulltext "diffusion model" AND hep-lat AND de>=2024 | recent LFT diffusion papers | gamma-ray / neutrino false positives | executed |
| R-arx-api | keyword | arXiv API | (neural sampler OR learned sampler) AND (importance weight OR Metropolis-Hastings OR reweighting OR Jarzynski) | Facet A + C bridge, cs.LG side | narrow phrase matching may miss papers using synonyms | executed |

## Query / Retrieval Log

| date | route id | source | query / action | filters | hits | unique new hits | included after screen | notes |
|---|---|---|---|---|---:|---:|---:|---|
| 2026-08-12 | R-arx-abs | arXiv | fetch https://arxiv.org/abs/2606.13790 | — | 1 | 1 | 1 | seed abs + full references |
| 2026-08-12 | R-inspire-rec | INSPIRE-HEP | q=arxiv:2606.13790 fields=references | hep-lat | 1 | 1 | 1 | 58 references extracted |
| 2026-08-12 | R-s2-rec | Semantic Scholar | paper/arXiv:2606.13790 fields=... | — | 0 | 0 | 0 | HTTP 429 rate limit |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/1904.12072 | — | 1 | 1 | 1 | 884944 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2111.15141 | — | 1 | 1 | 1 | 2713763 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2302.13834 | — | 1 | 1 | 1 | 4179526 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2007.07115 | — | 1 | 1 | 1 | 618576 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2201.08862 | — | 1 | 1 | 1 | 899741 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2410.02711 | — | 1 | 1 | 1 | 2113233 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2309.17082 | — | 1 | 1 | 1 | 2486741 bytes |
| 2026-08-12 | R-arx-pdf | arXiv PDF | pdf/2003.06413 | — | 1 | 1 | 1 | 1017965 bytes |
| 2026-08-12 | R-openalex-rec | OpenAlex | works/doi:10.48550/arXiv.2606.13790 | — | 1 | 1 | 1 | cited_by_count=0, hep-lat topic |
| 2026-08-12 | R-inspire-fwd | INSPIRE-HEP | refersto arxiv:2606.13790 | — | 1 | 0 | 0 | only seed self-hit; no forward citations |
| 2026-08-12 | R-arx-listing | arXiv listing | list/hep-lat/2606 | — | 0 | 0 | 0 | HTTP 403 (blocked) |
| 2026-08-12 | R-inspire-flow | INSPIRE-HEP | fulltext:"normalizing flow" AND hep-lat AND de>=2023 | most recent | 69 | ≥15 | 12 | ~12 potentially missed adjacents |
| 2026-08-12 | R-inspire-diff | INSPIRE-HEP | fulltext:"diffusion model" AND hep-lat AND de>=2024 | most recent | 38 | ≥5 | 5 | ~5 new including 2607.21436 SQ-as-optimal-control |
| 2026-08-12 | R-arx-api | arXiv API | (neural sampler OR learned sampler) AND (importance weight OR MH OR reweighting OR Jarzynski) | sortByDate desc | 2 | 1 | 1 | Importance Weighted Score Matching 2505.19431 |

## Route Coverage Notes

| route id | seed items recovered | new facets found | duplicate with other routes | residual blind spot |
|---|---|---|---|---|
| R-arx-abs | seed itself + full ref list of 58 | all three (A/B/C via seed's own framing) | overlaps with R-inspire-rec on ref list | v2 revisions after 2026-08-11 not checked |
| R-inspire-rec | seed + 58 refs with DOI/arXiv metadata | Facet B DOI coverage | overlaps with R-arx-abs on reference set | ML-only refs (Chen NeurIPS 2018, Bengio) have no arXiv/DOI in raw record |
| R-s2-rec | none (blocked 429) | none | — | Semantic Scholar coverage unchecked |
| R-arx-pdf | 8 core papers to C3 | direct method verification | — | 50 other seed refs not downloaded (kept at C1) |
| R-openalex-rec | seed | third-channel identity | overlaps with R-arx-abs/INSPIRE on seed | citation count is real-time OpenAlex; may lag |
| R-inspire-fwd | seed only | forward citation gap (0 papers cite seed) | — | very recent citing preprints outside INSPIRE indexing |
| R-arx-listing | blocked | none | — | contemporaneous non-seed hep-lat submissions unchecked via arXiv listing |
| R-inspire-flow | ~12 potentially missed 2025-2026 LFT flow papers | Facet B expansion | duplicates seed refs when they appear in top 25 | pre-2023 flow papers already covered by seed refs; not reprobed |
| R-inspire-diff | ~5 potentially missed LFT diffusion papers, including SQ-as-Optimal-Control 2607.21436 | Facet A+B bridge (SQ variants) | some duplicate with R-inspire-flow (SU(N) diffusion in both) | fulltext:"diffusion model" misses papers using "score-based" language exclusively |
| R-arx-api | 1 new candidate (2505.19431 IWSM) | Facet A+C generic ML sampler with correction | — | narrow phrase; papers using "learned neural sampler" or "amortized sampler" language may not match |
