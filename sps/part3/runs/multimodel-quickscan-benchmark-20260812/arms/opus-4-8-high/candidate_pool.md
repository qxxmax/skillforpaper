# Candidate Pool

Predecessor methods that arXiv:2606.13790 (Stochastic Path Sampler, SPS)
directly builds on. Grouped by the two facets requested. Each row's identity
(title, authors, arXiv ID) was verified via a logged web call (arXiv API,
independent of the SPS paper). Do not delete candidates silently.

Legend: SPS cite tag = the reference number as it appears in arXiv:2606.13790.
Verification C2 = title+authors+abstract confirmed on arXiv API landing metadata.

## Facet A — learned/neural samplers for unnormalized target distributions

Per SPS §1: "data-free diffusion-based samplers that minimize a path-space
Kullback-Leibler objective closely related to the one employed in this work...
The present work can be viewed as a stochastic-quantization-inspired adaptation
of this family of path-space variational samplers to lattice field theory."

| PaperID | Title | Authors | Year | arXiv ID | SPS cite | Source | Found by | RoundID | Status | Verification | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|
| P-A1 | Path Integral Sampler: a stochastic control approach for sampling | Q. Zhang, Y. Chen | 2021 | 2111.15141 | [55] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | high | PIS; Schrödinger-bridge/stochastic-control sampler for unnormalized densities |
| P-A2 | Denoising Diffusion Samplers | F. Vargas, W. Grathwohl, A. Doucet | 2023 | 2302.13834 | [48] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | high | DDS; ICLR 2023 |
| P-A3 | An optimal control perspective on diffusion-based generative modeling | J. Berner, L. Richter, K. Ullrich | 2022 | 2211.01364 | [10] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | medium | time-reversed diffusion sampler (DIS); path-space KL |
| P-A4 | Improved sampling via learned diffusions | L. Richter, J. Berner | 2023 | 2307.01198 | [43] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | medium | generalized Schrödinger bridge; log-variance loss; ICLR 2024 |
| P-A5 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | F. Vargas, S. Padhy, D. Blessing, N. Nüsken | 2023 | 2307.01050 | [49] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | high | CMCD; "adapts both forward and backward dynamics" — closest analogue (SPS learns both drifts) |
| P-A6 | NETS: A Non-Equilibrium Transport Sampler | M. S. Albergo, E. Vanden-Eijnden | 2024 | 2410.02711 | [6] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | high | non-equilibrium transport sampler; Jarzynski-based; learned drift + tunable diffusion |

## Facet B — learned samplers for lattice field theory

| PaperID | Title | Authors | Year | arXiv ID | SPS cite | Source | Found by | RoundID | Status | Verification | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|
| P-B1 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | M. S. Albergo, G. Kanwar, P. E. Shanahan | 2019 | 1904.12072 | [3] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | high | Foundational flow-based sampling for 2D phi^4; data-free training; PRD 100, 034515 |
| P-B2 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | L. Wang, G. Aarts, K. Zhou | 2023 | 2309.17082 | [51] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | high | Langevin/DM-as-SQ for 2D phi^4; direct conceptual parent of SPS's stochastic-quantization framing; JHEP 05 (2024) 060 |
| P-B3 | Equivariant flow-based sampling for lattice gauge theory | G. Kanwar, M. S. Albergo, D. Boyda, K. Cranmer, D. C. Hackett, S. Racanière, D. J. Rezende, P. E. Shanahan | 2020 | 2003.06413 | [28] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | medium | Gauge-equivariant flows; PRL 125, 121601 |
| P-B4 | Stochastic normalizing flows as non-equilibrium transformations | M. Caselle, E. Cellini, A. Nada, M. Panero | 2022 | 2201.08862 | [12] | arXiv API | fetch SPS + verify | R0001 | confirmed | C2 | medium | SNF for LFT; Jarzynski/non-equilibrium link; JHEP 07 (2022) 015 |

## Promotion Rules

- All rows above are `confirmed` at C2: identity verified against the arXiv API,
  an independent source separate from the SPS paper's own bibliography.
- No predecessor is asserted without a logged web call (see evidence_registry.md).
- Budget was sufficient; no candidate left as unverified C0/C1.
