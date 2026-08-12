# Evidence Registry

Every predecessor claimed has a row here citing the URL actually visited.
Two web calls were made (see round_log.md call ledger):
- Call 1: fetch of the SPS paper landing page (https://arxiv.org/abs/2606.13790)
  — establishes which methods SPS names as its base (full text + bibliography).
- Call 2: arXiv API batch query verifying the identity of each predecessor
  independently (http://export.arxiv.org/api/query?id_list=...).

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Section / Anchor | Quote / Extract | Verification level | Checked by | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| E0001 | SPS (2606.13790) | E_FULLTEXT | Focal paper full text + reference list; which prior methods SPS names as base | https://arxiv.org/abs/2606.13790 | §1 Introduction; References | "The present work can be viewed as a stochastic-quantization-inspired adaptation of this family of path-space variational samplers to lattice field theory" | C4 | fetch (call 1) | R0001 | Names Facet-A family [55,48,10,43,49,6] and Facet-B LFT samplers [3,51,28,12] |
| E0002 | P-A1 | E_METADATA_ONLY | Title/authors/arXiv ID of Path Integral Sampler | http://export.arxiv.org/api/query?id_list=2111.15141 | arXiv:2111.15141v2 | "Path Integral Sampler: a stochastic control approach for sampling" — Q. Zhang, Y. Chen | C2 | arXiv API (call 2) | R0001 | "draw samples from unnormalized probability density functions"; Schrödinger bridge |
| E0003 | P-A2 | E_METADATA_ONLY | Title/authors/arXiv ID of Denoising Diffusion Samplers | http://export.arxiv.org/api/query?id_list=2302.13834 | arXiv:2302.13834v2 | "Denoising Diffusion Samplers" — F. Vargas, W. Grathwohl, A. Doucet | C2 | arXiv API (call 2) | R0001 | "sample approximately from unnormalized probability density functions"; ICLR 2023 |
| E0004 | P-A3 | E_METADATA_ONLY | Title/authors/arXiv ID of optimal-control diffusion sampler | http://export.arxiv.org/api/query?id_list=2211.01364 | arXiv:2211.01364v3 | "An optimal control perspective on diffusion-based generative modeling" — J. Berner, L. Richter, K. Ullrich | C2 | arXiv API (call 2) | R0001 | time-reversed diffusion sampler (DIS); path-space KL; TMLR 2024 |
| E0005 | P-A4 | E_METADATA_ONLY | Title/authors/arXiv ID of Improved sampling via learned diffusions | http://export.arxiv.org/api/query?id_list=2307.01198 | arXiv:2307.01198v2 | "Improved sampling via learned diffusions" — L. Richter, J. Berner | C2 | arXiv API (call 2) | R0001 | generalized Schrödinger bridge; log-variance loss; ICLR 2024 |
| E0006 | P-A5 | E_METADATA_ONLY | Title/authors/arXiv ID of Controlled Monte Carlo Diffusions | http://export.arxiv.org/api/query?id_list=2307.01050 | arXiv:2307.01050v12 | "Transport meets Variational Inference: Controlled Monte Carlo Diffusions" — F. Vargas, S. Padhy, D. Blessing, N. Nüsken | C2 | arXiv API (call 2) | R0001 | CMCD "adapts both forward and backward dynamics" — matches SPS learning both drifts |
| E0007 | P-A6 | E_METADATA_ONLY | Title/authors/arXiv ID of NETS | http://export.arxiv.org/api/query?id_list=2410.02711 | arXiv:2410.02711v3 | "NETS: A Non-Equilibrium Transport Sampler" — M. S. Albergo, E. Vanden-Eijnden | C2 | arXiv API (call 2) | R0001 | Jarzynski-based; learned drift + tunable diffusion; tested on lattice field theory model |
| E0008 | P-B1 | E_METADATA_ONLY | Title/authors/arXiv ID of flow-based MCMC for LFT | http://export.arxiv.org/api/query?id_list=1904.12072 | arXiv:1904.12072v3 | "Flow-based generative models for Markov chain Monte Carlo in lattice field theory" — M. S. Albergo, G. Kanwar, P. E. Shanahan | C2 | arXiv API (call 2) | R0001 | Foundational data-free flow sampler for 2D phi^4; PRD 100, 034515 |
| E0009 | P-B2 | E_METADATA_ONLY | Title/authors/arXiv ID of Diffusion Models as Stochastic Quantization | http://export.arxiv.org/api/query?id_list=2309.17082 | arXiv:2309.17082v2 | "Diffusion Models as Stochastic Quantization in Lattice Field Theory" — L. Wang, G. Aarts, K. Zhou | C2 | arXiv API (call 2) | R0001 | DM=SQ for 2D phi^4; conceptual parent of SPS's stochastic-quantization route; JHEP 05 (2024) 060 |
| E0010 | P-B3 | E_METADATA_ONLY | Title/authors/arXiv ID of equivariant flow-based gauge sampling | http://export.arxiv.org/api/query?id_list=2003.06413 | arXiv:2003.06413v1 | "Equivariant flow-based sampling for lattice gauge theory" — G. Kanwar et al. | C2 | arXiv API (call 2) | R0001 | Gauge-equivariant flows; PRL 125, 121601 |
| E0011 | P-B4 | E_METADATA_ONLY | Title/authors/arXiv ID of stochastic normalizing flows | http://export.arxiv.org/api/query?id_list=2201.08862 | arXiv:2201.08862v3 | "Stochastic normalizing flows as non-equilibrium transformations" — M. Caselle, E. Cellini, A. Nada, M. Panero | C2 | arXiv API (call 2) | R0001 | SNF for LFT; Jarzynski link; JHEP 07 (2022) 015 |

## Verification Levels

| level | meaning |
|---|---|
| C0 | candidate only |
| C1 | metadata verified |
| C2 | abstract or source summary checked |
| C3 | full text checked |
| C4 | specific claim verified by page, quote, note, or screenshot |

## Notes On Evidence Strength

- E0001 is C4 for the focal SPS paper (full text read), establishing the
  *claimed* lineage. The bibliography entries inside it are C1(bib-of-C4).
- E0002–E0011 raise each predecessor to C2 via an independent arXiv API record
  (title + authors + arXiv ID + abstract), satisfying cross-validation: the
  identity is confirmed by a source separate from the SPS paper itself.
