# Round Log

**Run directory:** grok-4-5-high-fast  
**Hard cap:** 40 web calls (search + fetch + PDF download)  
**Authoritative budget counter:** this call ledger only.

## Call Ledger

| Call# | Time (local) | Channel | Action | URL / Query | Result | Running total |
|---:|---|---|---|---|---|---|
| 1 | 2026-08-12 | arXiv API | seed id_list | `id_list=2606.13790` | OK: title/authors/abs hep-lat | **1/40** |
| 2 | 2026-08-12 | arXiv PDF | download seed | `https://arxiv.org/pdf/2606.13790` | OK: 2263775 B, 33 pages | **2/40** |
| 3 | 2026-08-12 | arXiv API | lexical NF+lattice (http) | `all:"normalizing flow" AND (lattice…)` | FAIL: empty 0-byte body | **3/40** |
| 4 | 2026-08-12 | Semantic Scholar | seed paper | `ARXIV:2606.13790` | FAIL: HTTP 429 rate limit | **4/40** |
| 5 | 2026-08-12 | INSPIRE-HEP | lexical NF+lattice | `normalizing flow AND lattice AND (sampler OR MCMC OR "field theory")` | OK: total=65, returned 25 | **5/40** |
| 6 | 2026-08-12 | arXiv API | retry NF+lattice (http) | `all:"normalizing flow" AND all:lattice` | FAIL: empty 0-byte body | **6/40** |
| 7 | 2026-08-12 | INSPIRE-HEP | author lineage | `a Zhou, Kai and (normalizing flow or neural or sampler) and lattice` | OK: total=24 (incl. seed) | **7/40** |
| 8 | 2026-08-12 | arXiv API | title PIS | `ti:"Path Integral Sampler"` | OK: total=1 → 2111.15141 | **8/40** |
| 9 | 2026-08-12 | OpenAlex | DOI identity | `doi:10.1103/PhysRevD.100.034515` | OK: Albergo 2019, cites=233 | **9/40** |
| 10 | 2026-08-12 | OpenAlex | fulltext search | `normalizing flow lattice field theory sampling` | OK but noisy (meta count 53791); title-filter later | **10/40** |
| 11 | 2026-08-12 | arXiv API | lexical NF+lattice (https) | `all:"normalizing flow" AND all:lattice` | OK: total=73, top 30 saved | **11/40** |
| 12 | 2026-08-12 | arXiv API | learned diffusion sampling | broad OR query | OK: total=52; high noise; kept 2307.01198 | **12/40** |
| 13 | 2026-08-12 | INSPIRE-HEP | SNF/PIS/DDS/neural sampler | phrase OR query | OK: total=6 (tight) | **13/40** |
| 14 | 2026-08-12 | arXiv PDF | download | `1904.12072` | OK: 884944 B, 13 pages | **14/40** |
| 15 | 2026-08-12 | arXiv PDF | download | `2111.15141` | OK: 2713763 B, 26 pages | **15/40** |
| 16 | 2026-08-12 | arXiv PDF | download | `2302.13834` | OK: 4179526 B, 30 pages | **16/40** |
| 17 | 2026-08-12 | arXiv PDF | download | `2210.03139` | OK: 622586 B, 9 pages | **17/40** |
| 18 | 2026-08-12 | arXiv PDF | download | `2101.08176` | OK: 1193260 B, 39 pages | **18/40** |
| 19 | 2026-08-12 | arXiv PDF | download | `2309.17082` | OK: 2486741 B, 31 pages | **19/40** |
| 20 | 2026-08-12 | arXiv API | id_list core ML | `2111.15141,2302.13834,2410.02711,2307.01198,2201.08862,2003.06413` | OK: 6/6 titles verified | **20/40** |
| 21 | 2026-08-12 | INSPIRE-HEP | probe cites Albergo | `refersto:recid:1740645 OR eprint:1904.12072` | partial/wrong recid mix; total=12 | **21/40** |
| 22 | 2026-08-12 | INSPIRE-HEP | Albergo record | `eprint:1904.12072` | OK: control 1731778, cites=239 | **22/40** |
| 23 | 2026-08-12 | Semantic Scholar | Albergo paper | `ARXIV:1904.12072` | OK: DOI+arXiv, cites=282 | **23/40** |
| 24 | 2026-08-12 | INSPIRE-HEP | forward cites Albergo | `refersto:recid:1731778` | OK: total=239; top 30 retained | **24/40** |
| 25 | 2026-08-12 | INSPIRE-HEP | seed record | `eprint:2606.13790` | OK: control 3168332, cites=3 | **25/40** |
| 26 | 2026-08-12 | Semantic Scholar | Albergo citations | `/citations?limit=20` | OK: 20 citing papers | **26/40** |
| 27 | 2026-08-12 | Crossref | DOI verify Albergo | `10.1103/PhysRevD.100.034515` | OK: PRD 2019-08-23 | **27/40** |
| 28 | 2026-08-12 | arXiv API | SNF lexical | `all:"stochastic normalizing flows" AND (lattice OR sampling)` | OK: total=18 | **28/40** |
| 29 | 2026-08-12 | INSPIRE-HEP | forward cites seed | `refersto:recid:3168332` | OK: total=3 citers | **29/40** |
| 30 | 2026-08-12 | OpenAlex | title.search NF lattice | `title.search:normalizing flow lattice field` | OK: count=10 | **30/40** |
| 31 | 2026-08-12 | arXiv API | CRAFT/ECF | CRAFT title OR equivariant continuous flows+lattice | OK: total=3 (2201.13117, 2207.00283, 2110.02673) | **31/40** |
| 32 | 2026-08-12 | Semantic Scholar | seed retry | `ARXIV:2606.13790` | FAIL: 429 again | **32/40** |
| 33 | 2026-08-12 | OpenAlex | PIS ids.arxiv filter | invalid field attempt | FAIL: invalid query parameter | **33/40** |

**Calls used at stop: 33/40**

## Rounds

### R0000 — Initialize
- Manifest + mandatory empty ledgers created; intent `cover`/`learn`; graph_mode OFF.

### R0001 — Seed locate + multi-channel retrieval
- Seed verified (arXiv+PDF+INSPIRE). S2 blocked on seed (429); OpenAlex+INSPIRE+arXiv used. C3 PDFs: 7.

### R0002 — Citation/author snowball
- Albergo forward (INSPIRE 239 + S2 sample 20); Zhou author lineage; seed forward 3; SNF/CRAFT/ECF routes.

### R0003 — Stop under budget
- Facet coverage acceptable for scoped landscape; residual risk recorded; validator pending.
