# Candidate Pool

All candidates appear here before being confirmed, marked unconfirmed, or
excluded. Nothing is deleted silently. Every candidate was found by reading the
focal paper's full text and bibliography (call 1); every `confirmed` row was
then checked against an independently fetched arXiv record (calls 2-5).

Verification levels: C0 candidate only, C1 metadata verified, C2 abstract or
source summary checked, C3 full text checked, C4 specific claim verified.
`C1(bib-of-C4)` means the entry was read inside the C4-verified full text of the
focal paper but has no independent source of its own.

## Focal Paper

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---:|---|---|
| P0000 | Stochastic Path Sampler For Lattice Field Theory | S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou | 2026 | arXiv preprint, dated 11 Aug 2026 | https://arxiv.org/abs/2606.13790 | arXiv | user | R0001 | confirmed | C4 | 1.00 | high | Root node. Full text fetched, incl. Sec. 1 lineage statements and complete bibliography. |

## Family A: Data-Free Learned Samplers For Unnormalized Targets

The focal paper names this family in Sec. 1 as the one it adapts to lattice
field theory ("The present work can be viewed as a stochastic-quantization-
inspired adaptation of this family of path-space variational samplers").

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---:|---|---|
| P0001 | Path Integral Sampler: a stochastic control approach for sampling | Qinsheng Zhang, Yongxin Chen | 2021 (v2 2022) | ICLR 2022 | arXiv:2111.15141 / https://arxiv.org/abs/2111.15141 | arXiv API | backward citation, ref [55] | R0001 | confirmed | C2 | 0.95 | high | Closest ML ancestor: Schrödinger-bridge / stochastic-control sampler for unnormalized densities with importance weights correcting sub-optimality and time discretization — the structural analogue of SPS's IMH correction. |
| P0002 | Denoising Diffusion Samplers | Francisco Vargas, Will Grathwohl, Arnaud Doucet | 2023 | ICLR 2023 | arXiv:2302.13834 / https://arxiv.org/abs/2302.13834 | arXiv API | backward citation, ref [48] | R0001 | confirmed | C2 | 0.90 | high | Data-free diffusion sampler for unnormalized densities plus normalizing-constant estimation; SPS's free-energy estimator plays the same role. |
| P0003 | An optimal control perspective on diffusion-based generative modeling | Julius Berner, Lorenz Richter, Karen Ullrich | 2022 (v3 2024) | TMLR 2024 | arXiv:2211.01364 / https://arxiv.org/abs/2211.01364 | arXiv API | backward citation, ref [10] | R0001 | confirmed | C2 | 0.88 | high | Formulates diffusion generative modeling as path-space KL minimization and introduces the time-reversed diffusion sampler (DIS) for unnormalized densities — the objective family SPS minimizes. |
| P0004 | Improved sampling via learned diffusions | Lorenz Richter, Julius Berner | 2023 (v2 2024) | ICLR 2024 | arXiv:2307.01198 / https://arxiv.org/abs/2307.01198 | arXiv API | backward citation, ref [43] | R0001 | confirmed | C2 | 0.86 | high | Unifies these samplers as a generalized Schrödinger bridge with divergences between time-reversed path measures; flags reverse-KL mode collapse, which is the boundary SPS hits in the broken phase. |
| P0005 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken | 2023 (v12 2025) | ICLR 2024 (arXiv lists ICML 2023 workshop) | arXiv:2307.01050 / https://arxiv.org/abs/2307.01050 | arXiv API | backward citation, ref [49] | R0001 | confirmed | C2 | 0.92 | high | Singled out by the focal paper as the predecessor that, like SPS, learns both forward and backward drifts; also grounded in Jarzynski/Crooks identities, as SPS is. |
| P0006 | NETS: A Non-Equilibrium Transport Sampler | Michael S. Albergo, Eric Vanden-Eijnden | 2024 (v3 2025) | arXiv preprint | arXiv:2410.02711 / https://arxiv.org/abs/2410.02711 | arXiv API | backward citation, ref [6] | R0001 | confirmed | C2 | 0.90 | high | Jarzynski-based learned-drift sampler with tunable diffusion coefficient, already demonstrated on a statistical lattice field theory model; nearest competitor on both axes of SPS's claim. |

## Family B: Trajectory-Balance Lineage

Source of the "Trajectory Level Balance" condition the focal paper enforces
(Sec. 2, refs [8; 9; 34]).

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---:|---|---|
| P0007 | Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation | Emmanuel Bengio, Moksh Jain, Maksym Korablyov, Doina Precup, Yoshua Bengio | 2021 | NeurIPS 2021 | arXiv:2106.04399 / https://arxiv.org/abs/2106.04399 | arXiv API | backward citation, ref [8] | R0001 | confirmed | C2 | 0.70 | medium | Original GFlowNet: converts an energy function into a generative distribution via flow-consistency, the amortized-sampling idea SPS reuses on path space. |
| P0008 | GFlowNet Foundations | Yoshua Bengio, Salem Lahlou, Tristan Deleu, Edward J. Hu, Mo Tiwari, Emmanuel Bengio | 2021 (v5 2026) | JMLR 24(210) | arXiv:2111.09266 / https://arxiv.org/abs/2111.09266 | arXiv API | backward citation, ref [9] | R0001 | confirmed | C2 | 0.70 | medium | Theory layer, incl. partition-function and free-energy estimation from a trained sampler. |
| P0009 | Trajectory balance: Improved credit assignment in GFlowNets | Nikolay Malkin, Moksh Jain, Emmanuel Bengio, Chen Sun, Yoshua Bengio | 2022 | NeurIPS 2022 | arXiv:2201.13259 / https://arxiv.org/abs/2201.13259 | arXiv API | backward citation, ref [34] | R0001 | confirmed | C2 | 0.82 | high | Names and formalizes trajectory balance — the whole-trajectory forward/backward ratio condition SPS transplants to a discretized Langevin path measure. |

## Family C: Learned Samplers For Lattice Field Theory

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---:|---|---|
| P0010 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | M. S. Albergo, G. Kanwar, P. E. Shanahan | 2019 | Phys. Rev. D 100, 034515 / DOI 10.1103/PhysRevD.100.034515 | arXiv:1904.12072 / https://arxiv.org/abs/1904.12072 | arXiv API | backward citation, ref [3] | R0001 | confirmed | C2 | 0.94 | high | Founding data-free learned sampler for 2D phi^4 with an MCMC-exactness step; SPS's problem statement (autocorrelation near criticality, no training data) is inherited directly from it. |
| P0011 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | Lingxiao Wang, Gert Aarts, Kai Zhou | 2023 (v2 2024) | JHEP 05 (2024) 060 / DOI 10.1007/JHEP05(2024)060 | arXiv:2309.17082 / https://arxiv.org/abs/2309.17082 | arXiv API | backward citation, ref [51] | R0001 | confirmed | C2 | 0.96 | high | Direct antecedent and named contrast: shares two SPS authors, establishes the diffusion/stochastic-quantization link for 2D phi^4, and is the "Langevin-based sampler" whose manually chosen diffusion coefficient SPS replaces with a learned sigma_theta(t) (Sec. 2.2). |
| P0012 | Stochastic normalizing flows as non-equilibrium transformations | Michele Caselle, Elia Cellini, Alessandro Nada, Marco Panero | 2022 | JHEP 07 (2022) 015 / DOI 10.1007/JHEP07(2022)015 | arXiv:2201.08862 / https://arxiv.org/abs/2201.08862 | arXiv API | backward citation, ref [12] | R0001 | confirmed | C2 | 0.90 | high | Lattice non-equilibrium/Jarzynski reading of learned samplers — the same thermodynamic framing SPS builds its entropy-production objective on. |
| P0013 | Stochastic Normalizing Flows | Hao Wu, Jonas Köhler, Frank Noé | 2020 | NeurIPS 2020, vol. 33, 5933-5944 | arXiv:2002.06707 / https://arxiv.org/abs/2002.06707 | arXiv API | backward citation, ref [54] | R0001 | confirmed | C2 | 0.85 | high | ML origin of interleaving Langevin/stochastic steps with learned deterministic maps. Disambiguation: a different 2020 paper with the identical title exists (arXiv:2002.09547, Hodgkinson, van der Heide, Roosta, Mahoney); the focal paper's author list and NeurIPS page range match 2002.06707. |
| P0014 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | Kim A. Nicoli, Christopher J. Anders, Lena Funcke, Tobias Hartung, Karl Jansen, Pan Kessel, Shinichi Nakajima, Paolo Stornati | 2020 (v2 2021) | Phys. Rev. Lett. 126, 032001 / DOI 10.1103/PhysRevLett.126.032001 | arXiv:2007.07115 / https://arxiv.org/abs/2007.07115 | arXiv API | backward citation, ref [35] | R0001 | confirmed | C2 | 0.88 | high | Absolute free energy from a learned sampler — the estimator SPS reproduces via its path-dependent reweighting factor; SPS also adopts this paper's L x 8 finite-temperature geometry (Sec. 3). |
| P0015 | Stochastic normalizing flows for lattice field theory | Michele Caselle, Elia Cellini, Alessandro Nada, Marco Panero | 2022 | PoS LATTICE2022, 005 | arXiv:2210.03139 / https://arxiv.org/abs/2210.03139 | arXiv API | backward citation, ref [13] | R0001 | confirmed | C1 | 0.72 | medium | Identity confirmed inside the same logged API response as P0013 (title/authors/ID); abstract not separately inspected, so held at C1. |
| P0016 | Fourier-Flow model generating Feynman paths | Shile Chen, Oleh Savchuk, Shiqi Zheng, Baoyi Chen, Horst Stoecker, Lingxiao Wang, Kai Zhou | 2022 | Phys. Rev. D 107, 056001 / DOI 10.1103/PhysRevD.107.056001 | arXiv:2211.03470 / https://arxiv.org/abs/2211.03470 | arXiv API | backward citation, ref [18] | R0001 | confirmed | C2 | 0.75 | medium | Path-level learned sampler for Feynman paths with periodic structure, from the same group as SPS co-authors Wang/Zhou. Caution: first author is Shile Chen, not SPS co-author Shiyang Chen; the bibliography's "S. Chen" is ambiguous. |
| P0017 | Exploring Generative Networks for Manifolds with Non-Trivial Topology | Shiyang Chen, Gert Aarts, Biagio Lucini | 2025 | PoS LATTICE2024, 042 | arXiv:2502.02127 / https://arxiv.org/abs/2502.02127 | arXiv API | backward citation, ref [17] | R0001 | confirmed | C2 | 0.86 | high | Same three-author core as SPS; applies GFlowNet-derived generative sampling to non-trivial-topology manifolds and 2D scalar field theory — the immediate predecessor of SPS's trajectory-balance route. |
| P0018 | Variational Autoregressive Networks Applied to $\phi^4$ Field Theory Systems | Moxian Qian, Shiyang Chen | 2025 | arXiv preprint | arXiv:2512.19575 / https://arxiv.org/abs/2512.19575 | arXiv API | backward citation, ref [40] | R0001 | confirmed | C2 | 0.84 | high | Same two lead authors as SPS; data-free training for 2D phi^4 with Metropolis-Hastings corrections on learned proposals — the same "learned proposal + MH exactness" pattern SPS uses with IMH. |
| P0019 | Operator Spectroscopy of Trained Lattice Samplers | Moxian Qian | 2026 | arXiv preprint | arXiv:2605.11199 / https://arxiv.org/abs/2605.11199 | arXiv API | backward citation, ref [41] | R0001 | confirmed | C2 | 0.70 | medium | Same-author diagnostic layer for trained 2D phi^4 samplers (flow-matching velocity, diffusion score, flow action residual); cited by SPS as diagnostics for learned proposals rather than as a sampler. |

## Unconfirmed (Cited By The Focal Paper, Not Independently Verified)

Metadata below was read inside the C4-verified full text of P0000 and is
therefore `C1(bib-of-C4)`: the citation context is trusted, the entry's own
metadata is single-source. These are in-family works that the budget did not
reach. They are not asserted as verified predecessors.

| PaperID | Title (as cited by P0000) | Authors (as cited) | arXiv ID (as cited) | Status | Verification | Family | Next action |
|---|---|---|---|---|---|---|---|
| P0020 | Equivariant flow-based sampling for lattice gauge theory | Kanwar et al. | 2003.06413 | unconfirmed | C1(bib-of-C4) | C, gauge extension | fetch arXiv record |
| P0021 | Flow-based sampling for fermionic lattice field theories | Albergo et al. | 2106.05934 | unconfirmed | C1(bib-of-C4) | C | fetch arXiv record |
| P0022 | Flow-based sampling in the lattice Schwinger model at criticality | Albergo et al. | 2202.11712 | unconfirmed | C1(bib-of-C4) | C | fetch arXiv record |
| P0023 | Sampling using SU(N) gauge equivariant flows | Boyda et al. | (no arXiv ID in bib; PRD 103, 074504) | unconfirmed | C1(bib-of-C4) | C | resolve ID, then fetch |
| P0024 | Learning lattice quantum field theories with equivariant continuous flows | Gerdes et al. | 2207.00283 | unconfirmed | C1(bib-of-C4) | C, CNF branch | fetch arXiv record |
| P0025 | Scaling up machine learning for quantum field theory with equivariant continuous flows | de Haan et al. | 2110.02673 | unconfirmed | C1(bib-of-C4) | C, CNF branch | fetch arXiv record |
| P0026 | Flow-based sampling for multimodal and extended-mode distributions in lattice field theory | Hackett et al. | 2107.00734 | unconfirmed | C1(bib-of-C4) | C, mode-coverage | fetch arXiv record |
| P0027 | Numerical determination of the width and shape of the effective string using Stochastic Normalizing Flows | Caselle, Cellini, Nada | 2409.15937 | unconfirmed | C1(bib-of-C4) | C, SNF branch | title/authors/ID also appeared in the call-3 response; abstract unchecked |
| P0028 | Stochastic normalizing flows for effective string theory | Caselle, Cellini, Nada | 2412.19109 | unconfirmed | C1(bib-of-C4) | C, SNF branch | as above |
| P0029 | Solving Statistical Mechanics Using Variational Autoregressive Networks | Wu, Wang, Zhang | (no arXiv ID in bib; PRL 122, 080602) | unconfirmed | C1(bib-of-C4) | C, autoregressive | resolve ID, then fetch |
| P0030 | Continuous-Mixture Autoregressive Networks Learning the Kosterlitz-Thouless Transition | Wang, Jiang, He, Zhou | 2005.04857 | unconfirmed | C1(bib-of-C4) | C, autoregressive | fetch arXiv record |
| P0031 | Regressive and generative neural networks for scalar field theory | Zhou, Endrodi, Pang, Stoecker | 1810.12879 | unconfirmed | C1(bib-of-C4) | C, early data-driven | fetch arXiv record |
| P0032 | Physics-conditioned diffusion models for lattice gauge theory | Zhu, Aarts, Wang, Zhou, Wang | 2502.05504 | unconfirmed | C1(bib-of-C4) | C, diffusion branch | fetch arXiv record |
| P0033 | Combining complex Langevin dynamics with score-based and energy-based diffusion models | Aarts, Habibi, Wang, Zhou | 2510.01328 | unconfirmed | C1(bib-of-C4) | C, diffusion branch | fetch arXiv record |
| P0034 | Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory | Aarts et al. | 2601.19552 | unconfirmed | C1(bib-of-C4) | C, diffusion branch | fetch arXiv record |
| P0035 | Group-Equivariant Diffusion Models for Lattice Field Theory | Vega, Komijani, El-Khadra, Marinkovic | 2510.26081 | unconfirmed | C1(bib-of-C4) | C, diffusion branch | fetch arXiv record |
| P0036 | Diffusion model for SU(N) gauge theories | Komijani, Marinkovic, Turgut | 2605.06134 | unconfirmed | C1(bib-of-C4) | C, diffusion branch | fetch arXiv record |
| P0037 | Diffusion Models for SU(2) Lattice Gauge Theory in Two Dimensions | Alharazin, Panteleeva, Sun | 2602.09045 | unconfirmed | C1(bib-of-C4) | C, diffusion branch | fetch arXiv record |
| P0038 | Variational inference with normalizing flows | Rezende, Mohamed | (no arXiv ID in bib; ICML 2015) | unconfirmed | C1(bib-of-C4) | A/C, NF background | resolve ID, then fetch |
| P0039 | Generative modeling by estimating gradients of the data distribution | Song, Ermon | 1907.05600 (in bib note) | unconfirmed | C1(bib-of-C4) | score-based background | fetch arXiv record |

## Excluded

| PaperID | Title (as cited by P0000) | Reason for exclusion |
|---|---|---|
| X0001 | Parisi & Wu 1981, Perturbation Theory Without Gauge Fixing; Damgaard & Hüffel 1987, Stochastic Quantization | Genuine conceptual ancestors of SPS's stochastic-quantization framing, but not learned samplers and pre-arXiv, so outside the two requested families. Kept here rather than dropped. |
| X0002 | Neural ordinary differential equations (Chen et al. 2018) | Generic architecture background, not a sampler for unnormalized targets. |
| X0003 | Clausius/entropy-production application citations (Coleman & Noll; Kleidon; Dyke & Kleidon; Karbowski; Skinner & Dunkel; Jakimowicz; Purvis et al.; Landauer; Parrondo et al.; Sagawa & Ueda; Pachter et al.; Jarzynski; Kullback & Leibler) | Cited for the thermodynamic framing and for named identities, not as sampling methods. |
| X0004 | MALA / Riemann-manifold HMC (Roberts & Rosenthal 1998; Girolami & Calderhead 2011); GAN (Zhou et al. 2019); QCD-ML review (Zhou et al. 2024) | Classical or non-learned MCMC baselines, adversarial-model context, and a field review; not members of the two requested families. |

## Deduplication Notes

| Duplicate group | PaperIDs | Decision | Reason |
|---|---|---|---|
| DEDUP0001 | P0013 vs arXiv:2002.09547 | keep P0013 (2002.06707) | Two distinct 2020 arXiv papers share the title "Stochastic Normalizing Flows". The focal paper's cited authors (Wu, Köhler, Noé) and NeurIPS vol. 33 pp. 5933-5944 match 2002.06707; 2002.09547 is Hodgkinson et al. and is a different work, excluded as a title collision. |
| DEDUP0002 | P0012 vs P0015 | keep both | Same authors and topic but distinct records: JHEP 07 (2022) 015 journal article vs PoS LATTICE2022 proceedings; the focal paper cites them as refs [12] and [13] separately. |

## Promotion Rules Applied

- `confirmed` requires the focal paper naming the work as an antecedent (C4
  quote) **and** an independently fetched arXiv record matching title, authors,
  and ID. All 19 confirmed rows meet both conditions except P0015, held at C1
  because only its identity fields were read.
- Important but unreached works stay `unconfirmed` at `C1(bib-of-C4)` with a
  next action, per the budget rule.
- Out-of-family works are `excluded` with a reason, not deleted.
