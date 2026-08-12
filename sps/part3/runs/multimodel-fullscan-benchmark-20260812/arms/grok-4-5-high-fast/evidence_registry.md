# Evidence Registry

| EvidenceID | PaperID | Type | Locator | Integrity / note | Verified | Call# |
|---|---|---|---|---|---|---|
| E001 | P000 | arXiv_api_atom | `sources/arxiv_seed_2606.13790.xml` | abs+authors+hep-lat | 2026-08-12 | 1 |
| E002 | P000 | pdf | `sources/pdfs/2606.13790.pdf` | **2263775 bytes; 33 pages** (pdfinfo); internal working data | 2026-08-12 | 2 |
| E003 | P000 | inspire_record | `sources/inspire_seed_record.json` | control 3168332; cites=3 | 2026-08-12 | 25 |
| E004 | — | inspire_search | `sources/inspire_q006_nf_lattice.json` | total=65 | 2026-08-12 | 5 |
| E005 | — | inspire_author | `sources/inspire_author_zhou.json` | total=24 | 2026-08-12 | 7 |
| E006 | P003 | arXiv_api | `sources/arxiv_q_pis.xml` | ti Path Integral Sampler → 2111.15141 | 2026-08-12 | 8 |
| E007 | P001 | openalex | `sources/openalex_albergo1904.json` | DOI PRD; cites=233 | 2026-08-12 | 9 |
| E008 | — | openalex_noisy | `sources/openalex_nf_lft.json` | high noise; not used for identity | 2026-08-12 | 10 |
| E009 | — | arXiv_search | `sources/arxiv_q002c_nf_lattice.xml` | total=73 | 2026-08-12 | 11 |
| E010 | P009 | arXiv_search | `sources/arxiv_q_neural_path_samplers.xml` | noisy; 2307.01198 present | 2026-08-12 | 12 |
| E011 | — | inspire_search | `sources/inspire_q_snf_pis.json` | total=6 | 2026-08-12 | 13 |
| E012 | P001 | pdf | `sources/pdfs/1904.12072.pdf` | **884944 bytes; 13 pages** | 2026-08-12 | 14 |
| E013 | P003 | pdf | `sources/pdfs/2111.15141.pdf` | **2713763 bytes; 26 pages** | 2026-08-12 | 15 |
| E014 | P004 | pdf | `sources/pdfs/2302.13834.pdf` | **4179526 bytes; 30 pages** | 2026-08-12 | 16 |
| E015 | P005 | pdf | `sources/pdfs/2210.03139.pdf` | **622586 bytes; 9 pages** | 2026-08-12 | 17 |
| E016 | P002 | pdf | `sources/pdfs/2101.08176.pdf` | **1193260 bytes; 39 pages** | 2026-08-12 | 18 |
| E017 | P006 | pdf | `sources/pdfs/2309.17082.pdf` | **2486741 bytes; 31 pages** | 2026-08-12 | 19 |
| E018 | P003–P010 | arXiv_id_list | `sources/arxiv_idlist_core_ml.xml` | 6 titles verified | 2026-08-12 | 20 |
| E019 | P001 | inspire_record | `sources/inspire_albergo_record.json` | control 1731778; cites=239 | 2026-08-12 | 22 |
| E020 | P001 | s2_graph | `sources/s2_albergo_1904.json` | ArXiv+DOI; cites=282 | 2026-08-12 | 23 |
| E021 | — | inspire_forward | `sources/inspire_forward_albergo.json` | 239 citers; 30 titles logged | 2026-08-12 | 24 |
| E022 | — | s2_citations | `sources/s2_albergo_citations.json` | 20 citing papers | 2026-08-12 | 26 |
| E023 | P001 | crossref | `sources/crossref_albergo.json` | DOI 10.1103/physrevd.100.034515 | 2026-08-12 | 27 |
| E024 | — | arXiv_SNF | `sources/arxiv_q_snf.xml` | total=18 | 2026-08-12 | 28 |
| E025 | — | inspire_forward_seed | `sources/inspire_forward_seed.json` | 3 citers of SPS | 2026-08-12 | 29 |
| E026 | — | openalex_title | `sources/openalex_title_nf_lft.json` | count=10 | 2026-08-12 | 30 |
| E027 | P011–P013 | arXiv_CRAFT_ECF | `sources/arxiv_q_craft_ecf.xml` | total=3 | 2026-08-12 | 31 |
| E028 | P000 | local_pdf_text | `sources/seed_pdf_text_extract.txt` | refs [1]–[58]; 33 arXiv-like ids extracted | local | — |
| E029 | — | failure | S2 seed 429 | `sources/s2_seed_2606.13790.json` / retry | 2026-08-12 | 4,32 |
| E030 | — | failure | OpenAlex invalid ids.arxiv | `sources/openalex_pis.json` | 2026-08-12 | 33 |

## PDF Integrity Notes (≥6 required)

| File | PaperID | Bytes | Pages | Call# |
|---|---|---:|---:|---:|
| sources/pdfs/2606.13790.pdf | P000 | 2263775 | 33 | 2 |
| sources/pdfs/1904.12072.pdf | P001 | 884944 | 13 | 14 |
| sources/pdfs/2111.15141.pdf | P003 | 2713763 | 26 | 15 |
| sources/pdfs/2302.13834.pdf | P004 | 4179526 | 30 | 16 |
| sources/pdfs/2210.03139.pdf | P005 | 622586 | 9 | 17 |
| sources/pdfs/2101.08176.pdf | P002 | 1193260 | 39 | 18 |
| sources/pdfs/2309.17082.pdf | P006 | 2486741 | 31 | 19 |

## Correction / exactness mechanisms (from verified sources only)

| PaperID | Mechanism (as stated in abs/seed text or title-level) | Evidence |
|---|---|---|
| P000 | Extended-space **Independence Metropolis–Hastings** on learned forward proposals | E001/E002 abstract |
| P001 | Flow proposals inside **MCMC** (exactness via accept/reject / standard flow-MCMC pattern per title+field) | E007/E012; deep claim needs page anchors (not C4 here) |
| P003–P004, P009–P010 | Path/diffusion samplers for unnormalized targets (seed positions as related); exact weight/control objectives per family | E006/E018; seed refs E028 |
| P005/P008 | Stochastic normalizing flows / non-equilibrium transformations | E015/E018 |
| P011 | Annealed flow transport / SMC-AIS family (CRAFT) | E027 |

Unverified identities remain C0/C1 with labels; **zero fabricated citations**.
