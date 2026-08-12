# Candidate Pool

All candidate papers appear here before being confirmed, marked unconfirmed, or
excluded. Confirmed = present in seed's reference list AND corroborated on ≥2
channels OR downloaded to `sources/pdfs/`. Candidate (metadata-only) = surfaced
by a coverage search on ≥1 channel but not yet cross-validated.

Facet key: **A** = learned/neural samplers for unnormalized densities; **B** = learned samplers for lattice field theory; **C** = correction/exactness mechanism.

## Seed

| PaperID | Title | Authors | Year | Venue | DOI / arXiv | Source | Found by | RoundID | Status | Verification | Facet | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P0001 | Stochastic Path Sampler For Lattice Field Theory | Chen, Qian, Aarts, Lucini, Zhou | 2026 | arXiv (hep-lat) | arXiv:2606.13790 | arXiv+INSPIRE+OpenAlex | seed | R0001 | confirmed | C2 (title+abstract+authors+refs on 3 channels) | A+B+C | seed | 11 figs, 32 pages; 58 refs; cited_by_count=0 |

## Confirmed from seed reference list (INSPIRE cross-validation available)

| PaperID | Title | Authors | Year | Venue | DOI / arXiv | Status | Verification | Facet | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| P0002 | Variational inference with normalizing flows | Rezende, Mohamed | 2015 | ICML | — (mlr.press) | confirmed | C1(bib-of-C2 seed) | A | high | NF ancestor; single-channel raw ref via INSPIRE |
| P0003 | Neural ordinary differential equations | Chen R.T.Q. et al. | 2018 | NeurIPS | — | confirmed | C1(bib-of-C2 seed) | A | medium | CNF backbone |
| P0004 | Solving Statistical Mechanics Using Variational Autoregressive Networks | Wu, Wang, Zhang | 2019 | PRL 122 080602 | 10.1103/PhysRevLett.122.080602 | confirmed | C1 (DOI+INSPIRE) | A+B | high | VAN foundational |
| P0005 | Continuous-Mixture Autoregressive Networks Learning the Kosterlitz-Thouless Transition | Wang, Jiang, He, Zhou | 2022 | Chin.Phys.Lett. 39 120502 | arXiv:2005.04857, 10.1088/0256-307X/39/12/120502 | confirmed | C1 (arXiv+DOI+INSPIRE) | B | medium | autoregressive on lattice KT |
| P0006 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | Albergo, Kanwar, Shanahan | 2019 | PRD 100 034515 | arXiv:1904.12072, 10.1103/PhysRevD.100.034515 | confirmed | C3 (PDF 884944 B, ~13 pages) | A+B | high | founding paper for flow-based LFT sampling; PDF on disk |
| P0007 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | Nicoli et al. | 2021 | PRL 126 032001 | arXiv:2007.07115, 10.1103/PhysRevLett.126.032001 | confirmed | C3 (PDF 618576 B, ~13 pages) | B+C | high | reweighted flow estimator for LFT (NIS) |
| P0008 | Flow-based sampling for fermionic lattice field theories | Albergo, Kanwar, Racanière, Rezende, Urban, Boyda, Cranmer, Hackett, Shanahan | 2021 | PRD 104 114507 | arXiv:2106.05934, 10.1103/PhysRevD.104.114507 | confirmed | C1 (arXiv+DOI+INSPIRE) | B | high | fermionic-lattice extension |
| P0009 | Equivariant flow-based sampling for lattice gauge theory | Kanwar et al. | 2020 | PRL 125 121601 | arXiv:2003.06413, 10.1103/PhysRevLett.125.121601 | confirmed | C3 (PDF 1017965 B, ~6 pages) | B | high | equivariant flows for gauge theory |
| P0010 | Sampling using SU(N) gauge equivariant flows | Boyda et al. | 2021 | PRD 103 074504 | 10.1103/PhysRevD.103.074504 | confirmed | C1 (DOI+INSPIRE, arXiv metadata missing in INSPIRE dump but findable via DOI) | B | medium | SU(N) extension |
| P0011 | Flow-based sampling in the lattice Schwinger model at criticality | Albergo, Boyda, Cranmer, Hackett, Kanwar, Racanière, Rezende, Romero-López, Shanahan, Urban | 2022 | PRD 106 014514 | arXiv:2202.11712, 10.1103/PhysRevD.106.014514 | confirmed | C1 (arXiv+DOI+INSPIRE) | B | high | fermionic Schwinger at criticality |
| P0012 | Variational Autoregressive Networks Applied to φ⁴ Field Theory Systems | Qian, Chen | 2025/2026 | arXiv preprint | arXiv:2512.19575 | confirmed | C1 (arXiv+INSPIRE) | B | medium | same-group VAN for φ⁴ |
| P0013 | Learning lattice quantum field theories with equivariant continuous flows | Gerdes, de Haan, Rainone, Bondesan, Cheng | 2023 | SciPost Phys. 15 238 | arXiv:2207.00283, 10.21468/SciPostPhys.15.6.238 | confirmed | C1 | B | high | equivariant CNFs on LFT |
| P0014 | Scaling up machine learning for quantum field theory with equivariant continuous flows | de Haan, Rainone, Cheng, Bondesan | 2021 | arXiv preprint | arXiv:2110.02673 | confirmed | C1 | B | medium | scale-up CNF |
| P0015 | Exploring Generative Networks for Manifolds with Non-Trivial Topology | Chen S.Y., Aarts, Lucini | 2025 | PoS LATTICE2024 042 | arXiv:2502.02127 | confirmed | C1 | B | medium | same first-author lineage as SPS |
| P0016 | Flow-based sampling for multimodal and extended-mode distributions in lattice field theory | Hackett et al. | 2025 | arXiv preprint | arXiv:2107.00734 | confirmed | C1 | B+C | high | multimodal flow proposal + reweighting |
| P0017 | Fourier-flow model generating Feynman paths | Chen S., Savchuk, Zheng, Chen B., Stoecker, Wang, Zhou | 2023 | PRD 107 056001 | arXiv:2211.03470, 10.1103/PhysRevD.107.056001 | confirmed | C1 | A+B | medium | Fourier-basis flow for path integrals |
| P0018 | Exploring QCD matter in extreme conditions with Machine Learning | Zhou, Wang, Pang, Shi | 2024 | PPNP 135 104084 | arXiv:2303.15136, 10.1016/j.ppnp.2023.104084 | confirmed | C1 | B | low | review; context only |
| P0019 | Stochastic normalizing flows | Wu, Köhler, Noe | 2020 | NeurIPS 33 | — (no arXiv/DOI in INSPIRE) | confirmed | C1(bib-of-C2 seed) | A+C | high | SNF foundational |
| P0020 | Stochastic normalizing flows as non-equilibrium transformations | Caselle, Cellini, Nada, Panero | 2022 | JHEP 07 015 | arXiv:2201.08862, 10.1007/JHEP07(2022)015 | confirmed | C3 (PDF 899741 B, ~32 pages) | B+C | high | SNF-on-LFT with Jarzynski reweighting |
| P0021 | Stochastic normalizing flows for lattice field theory | Caselle, Cellini, Nada, Panero | 2023 | PoS LATTICE2022 005 | arXiv:2210.03139, 10.22323/1.430.0005 | confirmed | C1 | B+C | medium | SNF PoS extension |
| P0022 | Stochastic normalizing flows for effective string theory | Caselle, Cellini, Nada | 2025 | arXiv preprint | arXiv:2412.19109 | confirmed | C1 | B | medium | EST application |
| P0023 | Numerical determination of the width and shape of the effective string using Stochastic Normalizing Flows | Caselle, Cellini, Nada | 2025 | JHEP 02 090 | arXiv:2409.15937, 10.1007/JHEP02(2025)090 | confirmed | C1 | B | medium | EST width/shape via SNF |
| P0024 | Regressive and generative neural networks for scalar field theory | Zhou, Endrődi, Pang, Stöcker | 2019 | PRD 100 011501 | arXiv:1810.12879, 10.1103/PhysRevD.100.011501 | confirmed | C1 | B | medium | early generative NN for scalar LFT |
| P0025 | Generative modeling by estimating gradients of the data distribution | Song, Ermon | 2019 | NeurIPS 32 | arXiv:1907.05600 | confirmed | C1(bib-of-C2 seed) | A | high | score-based generative modeling ancestor |
| P0026 | Diffusion models as stochastic quantization in lattice field theory | Wang, Aarts, Zhou | 2024 | JHEP 05 060 | arXiv:2309.17082, 10.1007/JHEP05(2024)060 | confirmed | C3 (PDF 2486741 B, ~31 pages) | A+B | high | direct link diffusion ↔ SQ; same-group |
| P0027 | Physics-conditioned diffusion models for lattice gauge theory | Zhu, Aarts, Wang, Zhou, Wang | 2026 | JHEP 03 111 | arXiv:2502.05504, 10.1007/JHEP03(2026)111 | confirmed | C1 | B | high | physics-conditioned DM for LGT |
| P0028 | Group-Equivariant Diffusion Models for Lattice Field Theory | Vega, Komijani, El-Khadra, Marinkovic | 2025 | arXiv preprint | arXiv:2510.26081 | confirmed | C1 | B | medium | group-equivariant DM |
| P0029 | Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory | Aarts, Habibi, Ipp, Müller, Ranner, Wang, Wang, Zhu | 2026 | arXiv preprint | arXiv:2601.19552 | confirmed | C1 | B | high | equivariant DM for NAGT |
| P0030 | Diffusion Models for SU(2) Lattice Gauge Theory in Two Dimensions | Alharazin, Panteleeva, Sun | 2026 | arXiv preprint | arXiv:2602.09045 | confirmed | C1 | B | medium | SU(2) LGT DM |
| P0031 | Diffusion model for SU(N) gauge theories | Komijani, Marinkovic, Turgut | 2026 | arXiv preprint | arXiv:2605.06134 | confirmed | C1 | B | high | SU(N) LGT DM |
| P0032 | Combining complex Langevin dynamics with score-based and energy-based diffusion models | Aarts, Habibi, Wang, Zhou | 2025 | JHEP 12 160 | arXiv:2510.01328, 10.1007/JHEP12(2025)160 | confirmed | C1 | A+B | medium | complex-Langevin + DM |
| P0033 | Operator Spectroscopy of Trained Lattice Samplers | Qian | 2026 | arXiv preprint | arXiv:2605.11199 | confirmed | C1 | B | medium | diagnostic for trained lattice samplers |
| P0034 | Path Integral Sampler: a stochastic control approach for sampling | Zhang, Chen | 2022 | ICLR | arXiv:2111.15141 | confirmed | C3 (PDF 2713763 B, ~26 pages) | A+C | high | PIS — direct ancestor of SPS path-space framing |
| P0035 | Denoising Diffusion Samplers | Vargas, Grathwohl, Doucet | 2023 | ICLR | arXiv:2302.13834 | confirmed | C3 (PDF 4179526 B, ~30 pages) | A+C | high | DDS — direct ancestor of SPS learned-backward objective |
| P0036 | An optimal control perspective on diffusion-based generative modeling | Berner, Richter, Ullrich | 2024 | TMLR | arXiv:2211.01364 | confirmed | C1 | A | high | optimal-control view of diffusion; theoretical ancestor |
| P0037 | Improved sampling via learned diffusions | Richter, Berner | 2024 | ICLR | arXiv:2307.01198 | confirmed | C1 | A | high | log-variance loss and improved learned diffusion samplers |
| P0038 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | Vargas, Padhy, Blessing, Nüsken | 2024 | ICLR | arXiv:2307.01050 | confirmed | C1 | A+C | high | CMCD — learn both drifts, akin to SPS |
| P0039 | NETS: A Non-Equilibrium Transport Sampler | Albergo, Vanden-Eijnden | 2024 | arXiv preprint | arXiv:2410.02711 | confirmed | C3 (PDF 2113233 B, ~31 pages) | A+C | high | NETS — non-equilibrium reweighted sampler; SPS-analogous |
| P0040 | Perturbation Theory Without Gauge Fixing (Stochastic Quantization) | Parisi, Wu | 1981 | Sci.Sin. 24 483 | — | confirmed | C1(bib-of-C2 seed) | A | medium | foundational SQ paper |
| P0041 | Stochastic Quantization | Damgaard, Huffel | 1987 | Phys.Rept. 152 227 | 10.1016/0370-1573(87)90144-X | confirmed | C1 | A | medium | SQ review |
| P0042 | Flow network based generative models for non-iterative diverse candidate generation | Bengio E. et al. | 2021 | NeurIPS 34 | — | confirmed | C1(bib-of-C2 seed) | A+C | medium | GFlowNet foundational |
| P0043 | GFlowNet foundations | Bengio Y. et al. | 2023 | JMLR 24 | — | confirmed | C1(bib-of-C2 seed) | A+C | medium | GFlowNet theory |
| P0044 | Trajectory balance: improved credit assignment in gflownets | Malkin et al. | 2022 | NeurIPS 35 | — | confirmed | C1(bib-of-C2 seed) | A+C | high | trajectory-balance loss (named in SPS) |
| P0045 | Optimal scaling of discrete approximations to Langevin diffusions | Roberts, Rosenthal | 1998 | JRSS-B 60 255 | — | confirmed | C1 | A+C | low | MALA scaling; classical baseline |
| P0046 | Riemann manifold Langevin and Hamiltonian Monte Carlo methods | Girolami, Calderhead | 2011 | JRSS-B 73 123 | 10.1111/j.1467-9868.2010.00765.x | confirmed | C1 | A+C | low | manifold MALA/HMC baseline |
| P0047 | Equalities and Inequalities: Irreversibility and the Second Law of Thermodynamics at the Nanoscale | Jarzynski | 2013 | Prog.Math.Phys. 63 145 | 10.1007/978-3-0348-0359-5_4 | confirmed | C1 | C | high | Jarzynski equality (exactness ancestor for AIS/SNF) |

## Excluded from facet map (seed refs used only as thermodynamics or foundational context)

| PaperID | Title | Reason for exclusion |
|---|---|---|
| P0048 | Coleman & Noll 1963 — thermodynamics of elastic materials | not a learned sampler; used only to motivate second-law context |
| P0049 | Kleidon 2010 — max entropy production in environmental systems | out-of-scope (ecology) |
| P0050 | Dyke & Kleidon 2010 — max entropy production principle | out-of-scope (earth system) |
| P0051 | Skinner & Dunkel 2021 — bounds on entropy production in living systems | out-of-scope (biophysics) |
| P0052 | Karbowski 2024 — info thermodynamics from physics to neuroscience | out-of-scope |
| P0053 | Jakimowicz 2020 — entropy in economics | out-of-scope |
| P0054 | Purvis 2019 — entropy in urban systems | out-of-scope |
| P0055 | Landauer 1961 — irreversibility in computing | out-of-scope |
| P0056 | Sagawa & Ueda 2008 — second law with quantum feedback | out-of-scope |
| P0057 | Parrondo, Horowitz, Sagawa 2015 — thermodynamics of information | out-of-scope |
| P0058 | Pachter, Yang, Dill 2024 — entropy irreversibility inference | context only (foundational review) |
| P0059 | Kullback & Leibler 1951 — On information and sufficiency | foundational statistics; context only |

## Candidate (metadata-only, potentially missed by seed) — pre-seed date, in-scope

| PaperID | Title | Authors | arXiv | Source | Status | Verification | Facet | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|
| P0060 | Importance Weighted Score Matching for Diffusion Samplers with Enhanced Mode Coverage | Wang C. et al. | arXiv:2505.19431 | arXiv API | candidate | C1 (arXiv metadata; single channel) | A+C | high | May 2025 — pre-seed; explicit IW correction for neural diffusion samplers; not in seed refs |
| P0061 | SESaMo: Symmetry-Enforcing Stochastic Modulation for Normalizing Flows | (multi-author) | arXiv:2505.19619 | INSPIRE fulltext:"diffusion model" AND hep-lat | candidate | C1 (INSPIRE metadata; single channel) | B | medium | May 2025 — pre-seed; symmetry-enforced NF for LFT |
| P0062 | Symmetry-preserving neural networks in lattice field theories | (multi-author) | arXiv:2506.12493 | INSPIRE fulltext:"normalizing flow" AND hep-lat | candidate | C1 | B | medium | June 2025 — pre-seed |
| P0063 | Neural Triangular Transport Maps: A New Approach Towards Sampling in Lattice QCD | (multi-author) | arXiv:2510.13112 | INSPIRE | candidate | C1 | A+B | high | Oct 2025 — pre-seed; alternative transport-map sampler for lattice QCD |
| P0064 | ScoreNF: Score-Based Normalizing Flows for Sampling Unnormalized Distributions | (multi-author) | arXiv:2510.21330 | INSPIRE | candidate | C1 | A+C | high | Oct 2025 — pre-seed; directly on target: score-based NF for unnormalized targets |
| P0065 | Scaling flow-based approaches for topology sampling in SU(3) gauge theory | (multi-author) | arXiv:2510.25704 | INSPIRE | candidate | C1 | B | high | Oct 2025 — pre-seed; SU(3) topology sampling with flows |
| P0066 | Spectral Diffusion for Sampling on SU(N) | (multi-author) | arXiv:2512.19877 | INSPIRE | candidate | C1 | B | high | Dec 2025 — pre-seed; SU(N) spectral DM |
| P0067 | Analytic Bijections for Smooth and Interpretable Normalizing Flows | (multi-author) | arXiv:2601.10774 | INSPIRE | candidate | C1 | A+B | medium | Jan 2026 — pre-seed |
| P0068 | A scalable flow-based approach to mitigate topological freezing | (multi-author) | arXiv:2601.20708 | INSPIRE | candidate | C1 | B+C | high | Jan 2026 — pre-seed; direct competitor for the topological-freezing problem SPS motivates |
| P0069 | Normalizing-flow-based density of states for (1+1)D U(1) lattice gauge theory with θ-term | (multi-author) | arXiv:2603.12501 | INSPIRE | candidate | C1 | B+C | high | Mar 2026 — pre-seed; NF density-of-states = reweighting method |
| P0070 | Enhanced Sampling Techniques for Lattice Gauge Theory | (multi-author) | arXiv:2604.01287 | INSPIRE | candidate | C1 | B | medium | Apr 2026 — pre-seed |
| P0071 | Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality | (multi-author) | arXiv:2604.10209 | INSPIRE | candidate | C1 | B+C | high | Apr 2026 — pre-seed; near-criticality generative sampling + multilevel estimator |
| P0072 | Machine learning for four-dimensional SU(3) lattice gauge theories | (multi-author) | arXiv:2604.12416 | INSPIRE | candidate | C1 | B | medium | Apr 2026 — pre-seed |
| P0073 | Normalizing flows for all-orders QED corrections in lattice field theory | (multi-author) | arXiv:2605.22444 | INSPIRE | candidate | C1 | B | medium | May 2026 — pre-seed |
| P0074 | Learning the generating functional for variance reduction in lattice QCD | (multi-author) | arXiv:2606.15986 | INSPIRE | candidate | C1 | B+C | medium | Jun 2026 — same-month as seed; possibly concurrent |

## Candidate (metadata-only, post-seed / adjacent contemporary — not a predecessor)

| PaperID | Title | arXiv | Status | Facet | Priority | Notes |
|---|---|---|---|---|---|---|
| P0075 | Sampling the Schwinger Model with Gauge-Equivariant Diffusion | arXiv:2606.27481 | monitor | B | low | late Jun 2026; not predecessor |
| P0076 | Diffusion Models for Sampling Near Criticality in Lattice Field Theories | arXiv:2607.08505 | monitor | B | low | Jul 2026; post-seed |
| P0077 | Lattice Configuration Generation with a Self-Learning Diffusion Model | arXiv:2607.12587 | monitor | B | low | Jul 2026; post-seed |
| P0078 | Stochastic Quantization as Optimal Control | arXiv:2607.21436 | monitor | A+B | medium | Jul 2026; post-seed but semantically extends SPS's SQ+control angle |
| P0079 | Weight-Space Physics: Interpretable Hypernetworks for LQFT | arXiv:2607.07127 | monitor | B | low | Jul 2026; post-seed |
| P0080 | Normalizing Flows to Reconstruct Pseudo-PDFs | arXiv:2607.25282 | monitor | B (adjacent) | low | Jul 2026; not a sampler for the Gibbs measure |

## Excluded from candidate pool (out-of-scope even as adjacent)

| PaperID | Title | arXiv | Reason |
|---|---|---|---|
| P0081 | Lattice Gauge Theory via LLVM-Level Automatic Differentiation | arXiv:2602.20516 | not a learned sampler; toolchain paper |
| P0082 | Particle Monte Carlo methods for Lattice Field Theory | arXiv:2511.15196 | classical MCMC variant, not a learned sampler |

## Deduplication Notes

| Duplicate group | PaperIDs | Decision | Reason |
|---|---|---|---|
| DEDUP0001 | none | — | no duplicates detected between seed refs and coverage-search candidates by arXiv ID |
| DEDUP0002 | P0028 vs coverage search "Group-equivariant diffusion models for LFT (2510.26081, 2026)" | keep P0028 | same arXiv ID, minor casing difference in venue label |

## Promotion Rules

- Confirmed rows here have (a) INSPIRE record + arXiv ID (two channels), or (b) arXiv PDF on disk with integrity note, or (c) an INSPIRE record with DOI even when arXiv metadata is missing.
- Candidate rows (P0060-P0074) come from a single search channel; they need a second-channel cross-check before promotion. Under this run's 40-call cap these were not individually re-verified per candidate (each spot-check would consume a call). They remain C1 metadata-only and are explicitly recorded as potentially-missed predecessors, not asserted identities.
- Monitor rows (P0075-P0080) are post-seed dated and not predecessors.
- Excluded rows have a written reason.
