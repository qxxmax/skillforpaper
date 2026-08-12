# Search Route Log

| RouteID | Round | Family | Channel | Query / object | Calls used | Hits (raw) | Unique retained | Notes |
|---|---|---|---|---|---:|---:|---:|---|
| R0-ID | R1 | identifier | arXiv API | id_list=2606.13790 | 1 | 1 | 1 | seed |
| R0-PDF | R1 | fulltext | arXiv PDF | 2606.13790.pdf | 1 | 1 | 1 | C3 |
| R1-ARXIV-A | R1 | lexical | arXiv http | NF+lattice | 2 | 0 | 0 | FAIL empty body ×2 |
| R1-S2-SEED | R1 | bibliographic | Semantic Scholar | ARXIV:2606.13790 | 2 | 0 | 0 | 429 ×2 (calls 4,32) |
| R1-INSPIRE-NF | R1 | lexical | INSPIRE | NF ∧ lattice ∧ sampler/MCMC/FT | 1 | 65 | ~20 | strong LFT yield |
| R1-INSPIRE-ZHOU | R2 | author | INSPIRE | a Zhou,Kai ∧ (NF\|neural\|sampler) ∧ lattice | 1 | 24 | ~10 | lineage |
| R1-ARXIV-PIS | R1 | lexical | arXiv https | ti Path Integral Sampler | 1 | 1 | 1 | |
| R1-OA-DOI | R1 | identifier | OpenAlex | DOI Albergo | 1 | 1 | 1 | |
| R1-OA-FT | R1 | lexical | OpenAlex | fulltext NF LFT sampling | 1 | 20 (meta 53k) | 2–3 | noisy; substituted later |
| R1-ARXIV-NF | R1 | lexical | arXiv https | all NF ∧ lattice | 1 | 73 | ~25 | core LFT NF list |
| R1-ARXIV-DIFF | R1 | lexical | arXiv https | learned diffusion sampling OR | 1 | 52 | 1–2 | high noise |
| R1-INSPIRE-SNF | R1 | lexical | INSPIRE | SNF\|PIS\|DDS\|neural sampler | 1 | 6 | 5 | tight |
| R1-PDFS | R1 | fulltext | arXiv PDF | 6 neighbor PDFs | 6 | 6 | 6 | C3 |
| R2-IDLIST | R2 | identifier | arXiv | 6 ML/LFT ids | 1 | 6 | 6 | |
| R2-INSPIRE-ALB | R2 | citation_forward | INSPIRE | refersto:1731778 | 1+2 probe/record | 239 | ~25 screened | |
| R2-S2-ALB | R2 | bibliographic+forward | Semantic Scholar | Albergo paper+citations | 2 | 1+20 | ~15 | |
| R2-XREF | R2 | identifier | Crossref | DOI Albergo | 1 | 1 | 1 | |
| R2-ARXIV-SNF | R2 | lexical | arXiv | stochastic normalizing flows | 1 | 18 | ~10 | |
| R2-INSPIRE-SEED-FWD | R2 | citation_forward | INSPIRE | refersto:3168332 | 1 | 3 | 3 | |
| R2-OA-TITLE | R2 | lexical | OpenAlex | title.search NF lattice field | 1 | 10 | ~8 | cleaner |
| R2-ARXIV-CRAFT | R2 | lexical | arXiv | CRAFT / ECF | 1 | 3 | 3 | |
| R2-OA-PIS | R2 | identifier | OpenAlex | invalid ids.arxiv | 1 | 0 | 0 | FAIL |

## Channel Coverage Summary

| Channel | Searched? | Substitution? | Blind spot |
|---|---|---|---|
| arXiv (API/PDF) | **yes** | http→https after empty bodies | some http failures |
| Semantic Scholar | **partial** | OpenAlex+INSPIRE for seed | seed 429; Albergo OK |
| INSPIRE-HEP | **yes** | — | non-HEP ML sampler undercoverage |
| OpenAlex | **yes** | used as S2 substitute | fulltext search noisy |
| Crossref/DOI | **yes** | Albergo only | limited DOI pass |
| Google Scholar | **no** | budget | grey/citation UI gaps |
| WoS/Scopus | **blocked** | — | commercial indexing |
| Publisher pages | **no** (OA arXiv PDFs used) | — | journal HTML metadata |
