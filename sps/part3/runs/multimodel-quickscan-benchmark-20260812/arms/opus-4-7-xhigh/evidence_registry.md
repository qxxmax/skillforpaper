# Evidence Registry

Every claim, screenshot, DOI, link, and full-text confirmation must be
registered here. Final report / summary must cite `EvidenceID`, not just
`PaperID`. Each row below is backed by a single web fetch logged in
`round_log.md` (call ledger).

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | ScreenshotRef | Quote / Extract | Verification level | Checked by | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0000 | E_FULLTEXT | title, authors, abstract, Introduction paragraphs identifying predecessor families, and full reference list of SPS | https://arxiv.org/abs/2606.13790 | abstract, §1 Introduction, References list | — | "data-free diffusion-based samplers that minimize a path-space Kullback-Leibler objective closely related to the one employed in this work have been developed, including the Path Integral Sampler [55], Denoising Diffusion Samplers [48], optimal-control formulations of diffusion-based generative modeling [10, 43], Controlled Monte Carlo Diffusions [49], which, like the present work, learn both the forward and the backward drifts, and non-equilibrium transport samplers [6]." | C3 | own fetch | R0001 (call 1) | source of the predecessor enumeration; SPS also links to lattice-sampler family in §1 paragraphs 2–3 |
| E0002 | P0001 | E_ABSTRACT | title "Path Integral Sampler: a stochastic control approach for sampling" + authors Qinsheng Zhang, Yongxin Chen + venue ICLR 2022 + arXiv ID 2111.15141 | https://arxiv.org/abs/2111.15141 | landing page (title, authors, abstract) | — | "Path Integral Sampler (PIS), a novel algorithm to draw samples from unnormalized probability density functions." | C2 | own fetch | R0001 (call 2) | matches SPS ref [55] |
| E0003 | P0002 | E_ABSTRACT | title "Denoising Diffusion Samplers" + authors Francisco Vargas, Will Grathwohl, Arnaud Doucet + arXiv ID 2302.13834 | https://arxiv.org/abs/2302.13834 | landing page (title, authors, abstract) | — | "Denoising Diffusion Samplers (DDS) are obtained by approximating the corresponding time-reversal." | C2 | own fetch | R0001 (call 3) | matches SPS ref [48] |
| E0004 | P0003 | E_ABSTRACT | title "An optimal control perspective on diffusion-based generative modeling" + authors Julius Berner, Lorenz Richter, Karen Ullrich + arXiv ID 2211.01364 | https://arxiv.org/abs/2211.01364 | landing page (title, authors, abstract) | — | "our time-reversed diffusion sampler (DIS) can outperform other diffusion-based sampling approaches." | C2 | own fetch | R0001 (call 4) | matches SPS ref [10] |
| E0005 | P0004 | E_ABSTRACT | title "Improved sampling via learned diffusions" + authors Lorenz Richter, Julius Berner + arXiv ID 2307.01198 | https://arxiv.org/abs/2307.01198 | landing page (title, authors, abstract) | — | "we identify these approaches as special cases of a generalized Schrödinger bridge problem ... we propose the so-called log-variance loss." | C2 | own fetch | R0001 (call 5) | matches SPS ref [43] |
| E0006 | P0005 | E_ABSTRACT | title "Transport meets Variational Inference: Controlled Monte Carlo Diffusions" + authors Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken + arXiv ID 2307.01050 | https://arxiv.org/abs/2307.01050 | landing page (title, authors, abstract) | — | "Controlled Monte Carlo Diffusions ... a score-based annealing technique that crucially adapts both forward and backward dynamics in a diffusion model." | C2 | own fetch | R0001 (call 6) | matches SPS ref [49] (CMCD); SPS explicitly notes CMCD, like SPS, learns both forward and backward drifts |
| E0007 | P0006 | E_ABSTRACT | title "NETS: A Non-Equilibrium Transport Sampler" + authors Michael S. Albergo, Eric Vanden-Eijnden + arXiv ID 2410.02711 | https://arxiv.org/abs/2410.02711 | landing page (title, authors, abstract) | — | "Non-Equilibrium Transport Sampler (NETS), to sample from unnormalized probability distributions. NETS can be viewed as a variant of annealed importance sampling (AIS) based on Jarzynski's equality." | C2 | own fetch | R0001 (call 7) | matches SPS ref [6]; abstract also notes application to a lattice-field-theory target |
| E0008 | P0007 | E_ABSTRACT | title "Flow-based generative models for Markov chain Monte Carlo in lattice field theory" + authors M. S. Albergo, G. Kanwar, P. E. Shanahan + PRD 100 (2019) 034515 + arXiv ID 1904.12072 | https://arxiv.org/abs/1904.12072 | landing page (title, authors, abstract) | — | "A Markov chain update scheme using a machine-learned flow-based generative model is proposed for Monte Carlo sampling in lattice field theories ... compared with HMC and local Metropolis sampling for phi^4 theory in two dimensions." | C2 | own fetch | R0001 (call 8) | matches SPS ref [3]; same 2D phi^4 target as SPS |
| E0009 | P0008 | E_ABSTRACT | title "Diffusion Models as Stochastic Quantization in Lattice Field Theory" + authors L. Wang, G. Aarts, K. Zhou + JHEP 2024 (05) 060 + arXiv ID 2309.17082 | https://arxiv.org/abs/2309.17082 | landing page (title, authors, abstract) | — | "In this work, we establish a direct connection between generative diffusion models (DMs) and stochastic quantization (SQ) ... we demonstrate that the DM can serve as a global sampler for generating quantum lattice field configurations in two-dimensional phi^4 theory." | C2 | own fetch | R0001 (call 9) | matches SPS ref [51]; shared authors Aarts and Zhou with SPS |
| E0010 | P0009 | E_ABSTRACT | title "Stochastic normalizing flows as non-equilibrium transformations" + authors M. Caselle, E. Cellini, A. Nada, M. Panero + JHEP 07 (2022) 015 + arXiv ID 2201.08862 | https://arxiv.org/abs/2201.08862 | landing page (title, authors, abstract) | — | "stochastic normalizing flows, in which neural-network layers are combined with Monte Carlo updates, is the same that underlies out-of-equilibrium simulations based on Jarzynski's equality." | C2 | own fetch | R0001 (call 10) | matches SPS ref [12]; direct lattice-side methodological neighbor of SPS |

## Bibliographic-Only Context Evidence (no independent fetch)

The following SPS references are named in Introduction paragraphs 2–3 as
part of the lattice-sampler landscape but were **not independently fetched
within the 10-call quick-scan budget**. They are trusted as bibliographic
entries of an already-C3-verified full text (SPS itself), i.e.
`C1(bib-of-C3)`, but a strong claim about their contents would require a
separate independent fetch in a future round.

| EvidenceID | Cited-as | Title (per SPS bibliography) | arXiv ID | Verification |
|---|---|---|---|---|
| E_CTX01 | SPS ref [35] | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models (Nicoli et al., PRL 126 032001) | 2007.07115 | C1(bib-of-C3) |
| E_CTX02 | SPS ref [23] | Learning lattice quantum field theories with equivariant continuous flows (Gerdes et al., SciPost Phys 15) | 2207.00283 | C1(bib-of-C3) |
| E_CTX03 | SPS ref [54] | Stochastic normalizing flows (Wu, Köhler, Noé, NeurIPS 2020) | — (NeurIPS proceedings; SPS lists no arXiv ID) | C1(bib-of-C3) |
| E_CTX04 | SPS ref [42] | Variational inference with normalizing flows (Rezende & Mohamed, ICML 2015) | — (SPS lists no arXiv ID; historical ID 1505.05770 not verified this round) | C1(bib-of-C3) |
| E_CTX05 | SPS ref [56] | Regressive and generative neural networks for scalar field theory (Zhou et al., PRD 100 011501) | 1810.12879 | C1(bib-of-C3) |

## Evidence Rules

- `E_LINK` confirms existence or metadata.
- `E_DOI` confirms metadata.
- `E_ABSTRACT` supports relevance only.
- `E_FULLTEXT` supports full-text availability.
- `E_SCREENSHOT` supports a specific page/table/figure/method/result/claim.
- `E_QUOTE` supports a specific claim; keep quotes short.
- `E_METADATA_ONLY` must not be used as strong claim evidence.

## Verification Levels

| level | meaning |
|---|---|
| C0 | candidate only |
| C1 | metadata verified |
| C2 | abstract or source summary checked |
| C3 | full text checked |
| C4 | specific claim verified by page, quote, note, or screenshot |
| C1(bib-of-C3) | bibliographic entry read inside an already-C3-verified full text; single-source, awaiting independent cross-check |

## Report Rule

A `PaperID` tells us which paper. An `EvidenceID` tells us why we trust a
specific claim, figure, result, link, or metadata field.
