# Evidence Registry

Every claim, DOI, link, full-text confirmation, and PDF integrity note is
registered here. Final outputs cite `EvidenceID`, not just `PaperID`.

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | Quote / Extract / Integrity note | Verification level | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0001 | E_LINK + E_FULLTEXT | seed identity: title, authors (S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou), date 2026-08-11, abstract; full HTML text served | https://arxiv.org/abs/2606.13790 | whole page | "we propose a novel sampler based on nonequilibrium thermodynamics, called Stochastic Path Sampler (SPS)" | C3 | R0001 | call 1 |
| E0002 | P0001 | E_FULLTEXT | seed PDF integrity | sources/pdfs/2606.13790_sps.pdf | — | 2,263,775 bytes, 33 pages (pypdf) | C3 | R0001 | call 2; C3 gate PDF 1/6 |
| E0003 | P0001 | E_QUOTE | seed's correction mechanism | https://arxiv.org/abs/2606.13790 | abstract | "The learned forward process provides independent proposals, which are subsequently corrected by an extended-space Independence Metropolis–Hastings step." | C4 | R0001 |  |
| E0004 | P0001 | E_QUOTE | seed's self-declared ML method family (PIS, DDS, OC, CMCD, NETS) | https://arxiv.org/abs/2606.13790 | §1 | "data-free diffusion-based samplers that minimize a path-space Kullback-Leibler objective ... including the Path Integral Sampler 55, Denoising Diffusion Samplers 48, optimal-control formulations 10; 43, Controlled Monte Carlo Diffusions 49 ... and non-equilibrium transport samplers 6" | C4 | R0001 |  |
| E0005 | P0002–P0039 | E_QUOTE (bibliography) | existence + metadata of 38 in-scope references as cited by seed | https://arxiv.org/abs/2606.13790 | References section | full reference list with arXiv IDs where the seed provides them | C1(bib-of-C3) | R0001 | each entry needs independent confirmation to reach C2 |

| E0006 | P0002 | E_FULLTEXT | PDF integrity | sources/pdfs/1904.12072_flowmcmc_lft.pdf | — | 884,944 bytes, 13 pages (pypdf) | C3 | R0004 | call 15; C3 gate PDF 2 |
| E0007 | P0030 | E_FULLTEXT | PDF integrity | sources/pdfs/2111.15141_path_integral_sampler.pdf | — | 2,713,763 bytes, 26 pages | C3 | R0004 | call 16; C3 gate PDF 3 |
| E0008 | P0011 | E_FULLTEXT | PDF integrity | sources/pdfs/2002.06707_stochastic_normalizing_flows.pdf | — | 7,114,775 bytes, 21 pages | C3 | R0004 | call 17; C3 gate PDF 4 |
| E0009 | P0012 | E_FULLTEXT | PDF integrity | sources/pdfs/2201.08862_snf_noneq_lattice.pdf | — | 899,741 bytes, 32 pages | C3 | R0004 | call 18; C3 gate PDF 5 |
| E0010 | P0023 | E_FULLTEXT | PDF integrity | sources/pdfs/2309.17082_diffusion_stochastic_quantization.pdf | — | 2,486,741 bytes, 31 pages | C3 | R0004 | call 19; C3 gate PDF 6 |
| E0011 | P0031 | E_FULLTEXT | PDF integrity | sources/pdfs/2302.13834_denoising_diffusion_samplers.pdf | — | 4,179,526 bytes, 30 pages | C3 | R0004 | call 20; C3 gate PDF 7 |
| E0012 | P0048 | E_FULLTEXT | PDF integrity | sources/pdfs/1812.01729_boltzmann_generators.pdf | — | 10,488,625 bytes, 46 pages | C3 | R0004 | call 21; C3 gate PDF 8 |
| E0013 | P0065 | E_FULLTEXT | PDF integrity | sources/pdfs/2309.01156_ml_sampling_latticeqcd_review.pdf | — | 1,632,799 bytes, 11 pages | C3 | R0004 | call 22; C3 gate PDF 9 |
| E0014 | 46 pool papers (see sources/queries/s2_batch.json) | E_METADATA (cross-validation) | title/year/venue for 46 arXiv IDs on second channel (Semantic Scholar); resolves hypothesis IDs 1809.10606, 2002.06707, 2008.05456, 2106.04399, 2201.13259, 2111.09266, 1505.05770, 1910.13496, 2105.12603, 2309.01156 | api.semanticscholar.org/graph/v1/paper/batch | — | saved JSON: sources/queries/s2_batch.json | C1 (two-channel identity) | R0003 | call 10 |
| E0015 | P0001 | E_METADATA (cross-validation) | seed identity on third channel (INSPIRE): title, authors, earliest date 2026-06-11, 3 citations | inspirehep.net/api/literature?q=arxiv:2606.13790 | — | saved JSON: sources/queries/inspire_seed.json | C1 (three-channel identity for seed) | R0003 | call 13 |
| E0016 | P0066, P0067, P0068 | E_METADATA_ONLY | forward citations of seed as of 2026-08-12, Semantic-Scholar-scoped | api.semanticscholar.org .../citations | — | saved JSON: sources/queries/s2_seed_citations.json | C1 (single channel for P0066/P0067; P0068 also INSPIRE) | R0003 | call 12 |
| E0017 | P0042 | E_QUOTE | limitation claims: poor volume scaling, long-range-correlation failure, self-training mode collapse | https://doi.org/10.1103/physrevd.108.114501 (page text saved by search tool) | intro | "the training process becomes increasingly challenging as the dimensionality of the lattice increases, resulting in poor volume scaling ... risk that the training will assign vanishing low probability mass to some of the modes" | C4 | R0005 | call 23 |
| E0018 | P0073 | E_QUOTE | taxonomy of F1 family: annealed-Langevin line (ULA, MCD, CMCD, UHA, LDVI) vs stochastic-optimal-control line (PIS, DDS, DIS, GFN) | https://arxiv.org/html/2406.07423 | related work | "A second line of work describes diffusion-based sampling from a stochastic optimal control perspective ... Path Integral Sampler (PIS) ... Denoising Diffusion Sampler (DDS) ... Time-Reversed Diffusion Sampler (DIS) ... Generative Flow Networks (GFN)" | C4 | R0005 | call 24 |

## Evidence Rules

- `E_LINK` existence/metadata; `E_DOI` metadata; `E_ABSTRACT` relevance only;
  `E_FULLTEXT` full-text availability (PDF downloads get integrity note:
  file size and page count); `E_QUOTE` specific short-quote claims;
  `E_METADATA_ONLY` never supports strong claims.
- Bibliography entries read inside a C3/C4-verified full text are annotated
  `C1(bib-of-C3)` until independently confirmed.
