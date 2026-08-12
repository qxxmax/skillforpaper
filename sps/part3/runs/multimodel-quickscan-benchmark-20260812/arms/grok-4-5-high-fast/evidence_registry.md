# Evidence Registry

Every claim, screenshot, DOI, link, and full-text confirmation must be
registered here.  Final reports cite `EvidenceID`, not just `PaperID`.

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | ScreenshotRef | Quote / Extract | Verification level | Checked by | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0000 | E_LINK | seed abs landing exists; title/authors | https://arxiv.org/abs/2606.13790 | abs/html | — | Title: Stochastic Path Sampler For Lattice Field Theory; Authors: Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou | C2 | WebFetch | R0001 | call #1 |
| E0002 | P0000 | E_ABSTRACT | seed contribution + LFT/ML prior framing | https://arxiv.org/abs/2606.13790 | Abstract | — | SPS for unnormalized lattice target; path-space VFE; IMH correction; 2d φ⁴ | C2 | WebFetch | R0001 | call #1 |
| E0003 | P0000 | E_QUOTE | names key ML path-space predecessors | https://arxiv.org/abs/2606.13790 | §1 Introduction | — | "including the Path Integral Sampler 55, Denoising Diffusion Samplers 48, optimal-control formulations of diffusion-based generative modeling 10; 43, Controlled Monte Carlo Diffusions 49, ... and non-equilibrium transport samplers 6. The present work can be viewed as a stochastic-quantization-inspired adaptation of this family" | C4 | WebFetch | R0001 | call #1; key builds-on claim |
| E0004 | P0000 | E_QUOTE | names LFT learned-sampler families | https://arxiv.org/abs/2606.13790 | §1 Introduction | — | NF/CNF/autoregressive as variational free-energy models; GAN/DM as data-driven; cites Albergo flows, Gerdes CNF, Wang DM-as-SQ, etc. | C4 | WebFetch | R0001 | call #1 |
| E0005 | P0000 | E_FULLTEXT | bibliography identity leads for cited parents | https://arxiv.org/abs/2606.13790 | References | — | bib maps: [55]→2111.15141; [48]→2302.13834; [49]→2307.01050; [6]→2410.02711; [43]→2307.01198; [10]→2211.01364; [3]→1904.12072; [51]→2309.17082; [23]→2207.00283 | C3 | WebFetch | R0001 | bib-of-fulltext; parents need own fetches |
| E0006 | P0001 | E_LINK | PIS identity (title, authors, arXiv) | https://arxiv.org/abs/2111.15141 | abs | — | Path Integral Sampler: a stochastic control approach for sampling; Qinsheng Zhang, Yongxin Chen | C2 | WebFetch | R0002 | call #2 |
| E0007 | P0001 | E_ABSTRACT | PIS samples unnormalized targets via path integral / SOC | https://arxiv.org/abs/2111.15141 | Abstract | — | "draw samples from unnormalized probability density functions" via Schrödinger bridge / stochastic optimal control | C2 | WebFetch | R0002 | call #2 |
| E0008 | P0002 | E_LINK | DDS identity | https://arxiv.org/abs/2302.13834 | abs | — | Denoising Diffusion Samplers; Francisco Vargas, Will Grathwohl, Arnaud Doucet | C2 | WebFetch | R0002 | call #3 |
| E0009 | P0002 | E_ABSTRACT | DDS for unnormalized densities | https://arxiv.org/abs/2302.13834 | Abstract | — | "sample approximately from unnormalized probability density functions and estimate their normalizing constants" | C2 | WebFetch | R0002 | call #3 |
| E0010 | P0003 | E_LINK | CMCD identity | https://arxiv.org/abs/2307.01050 | abs | — | Transport meets Variational Inference: Controlled Monte Carlo Diffusions; Vargas, Padhy, Blessing, Nüsken | C2 | WebFetch | R0002 | call #4 |
| E0011 | P0003 | E_ABSTRACT | CMCD learns forward and backward drifts | https://arxiv.org/abs/2307.01050 | Abstract | — | "adapts both forward and backward dynamics in a diffusion model" for sampling/inference | C2 | WebFetch | R0002 | call #4 |
| E0012 | P0004 | E_LINK | NETS identity | https://arxiv.org/abs/2410.02711 | abs | — | NETS: A Non-Equilibrium Transport Sampler; Michael S. Albergo, Eric Vanden-Eijnden | C2 | WebFetch | R0002 | call #5 |
| E0013 | P0004 | E_ABSTRACT | NETS for unnormalized targets; LFT demo noted | https://arxiv.org/abs/2410.02711 | Abstract | — | "sample from unnormalized probability distributions"; demonstrates on "a model from statistical lattice field theory" | C2 | WebFetch | R0002 | call #5 |
| E0014 | P0005 | E_LINK | learned-diffusions identity | https://arxiv.org/abs/2307.01198 | abs | — | Improved sampling via learned diffusions; Lorenz Richter, Julius Berner | C2 | WebFetch | R0003 | call #6 |
| E0015 | P0005 | E_ABSTRACT | path-space variational sampling from unnormalized ρ | https://arxiv.org/abs/2307.01198 | Abstract | — | "sample from target distributions using controlled diffusion processes, being trained only on the unnormalized target densities" | C2 | WebFetch | R0003 | call #6 |
| E0016 | P0007 | E_LINK | Albergo LFT flow sampler identity | https://arxiv.org/abs/1904.12072 | abs | — | Flow-based generative models for Markov chain Monte Carlo in lattice field theory; M. S. Albergo, G. Kanwar, P. E. Shanahan | C2 | WebFetch | R0003 | call #7 |
| E0017 | P0007 | E_ABSTRACT | foundational learned NF sampler for LFT / φ⁴ | https://arxiv.org/abs/1904.12072 | Abstract | — | flow-based MCMC for lattice field theories; trained without existing samples; compared on 2d φ⁴ | C2 | WebFetch | R0003 | call #7 |
| E0018 | P0008 | E_LINK | Wang DM-as-SQ identity | https://arxiv.org/abs/2309.17082 | abs | — | Diffusion Models as Stochastic Quantization in Lattice Field Theory; L. Wang, G. Aarts, K. Zhou | C2 | WebFetch | R0003 | call #8 |
| E0019 | P0008 | E_ABSTRACT | LFT diffusion sampler linked to stochastic quantization / φ⁴ | https://arxiv.org/abs/2309.17082 | Abstract | — | connects DMs to SQ; global sampler for 2d φ⁴; reduces autocorrelation near criticality | C2 | WebFetch | R0003 | call #8 |
| E0020 | P0006 | E_LINK | optimal-control diffusion identity | https://arxiv.org/abs/2211.01364 | abs | — | An optimal control perspective on diffusion-based generative modeling; Julius Berner, Lorenz Richter, Karen Ullrich | C2 | WebFetch | R0003 | call #9 |
| E0021 | P0006 | E_ABSTRACT | DIS samples unnormalized densities; path-space KL | https://arxiv.org/abs/2211.01364 | Abstract | — | diffusion-based generative modeling as path-space KL; "novel diffusion-based method for sampling from unnormalized densities" (DIS) | C2 | WebFetch | R0003 | call #9 |
| E0022 | P0009 | E_LINK | Gerdes equivariant CNF LFT identity | https://arxiv.org/abs/2207.00283 | abs/html | — | Learning Lattice Quantum Field Theories with Equivariant Continuous Flows; Gerdes, de Haan, Rainone, Bondesan, Cheng | C2 | WebFetch | R0003 | call #10 |

## Evidence Rules

- `E_LINK` confirms existence or metadata.
- `E_DOI` confirms metadata.
- `E_ABSTRACT` supports relevance only.
- `E_FULLTEXT` supports full-text availability.
- `E_SCREENSHOT` supports a specific page, table, figure, method, result, or claim.
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

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | P0010 | independent abs fetch for Kanwar et al. Equivariant flow-based sampling (bib 2003.06413) | cited LFT parent; budget exhausted | next round fetch https://arxiv.org/abs/2003.06413 |
| ERQ0002 | P0011 | independent abs fetch for Caselle et al. Stochastic normalizing flows (bib 2201.08862) | cited SNF-in-LFT parent | next round fetch https://arxiv.org/abs/2201.08862 |
| ERQ0003 | P0012 | independent identity for Wu et al. Stochastic normalizing flows (NeurIPS 2020; bib Link-only) | cited SNF method parent | locate arXiv/venue page |

## Report Rule

A `PaperID` tells us which paper.  An `EvidenceID` tells us why we trust a
specific claim, figure, result, link, or metadata field.
