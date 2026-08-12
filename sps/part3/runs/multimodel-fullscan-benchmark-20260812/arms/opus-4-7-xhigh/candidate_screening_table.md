# Candidate Screening Table

Labels:
- **include**: enters the landscape record for the three-facet map.
- **exclude**: outside scope; reason stated.
- **uncertain**: needs a follow-on cross-check or full text before a decision (kept at C0/C1).
- **monitor**: relevant but post-seed or context-only; watched, not asserted as predecessor.

Score column: 0-100, mixing relevance to the three facets and evidence quality.
Rank column: within-facet ordering by score.

| id | title / item | source | route(s) found | year | score | rank | label | facet | reason | URL / DOI |
|---|---|---|---|---|---:|---:|---|---|---|---|
| P0001 | Stochastic Path Sampler For Lattice Field Theory | arXiv | R-arx-abs, R-inspire-rec, R-openalex-rec | 2026 | 100 | seed | include | A+B+C | seed itself | arXiv:2606.13790 |
| P0034 | Path Integral Sampler | ICLR | R-arx-abs (seed ref), R-arx-pdf | 2022 | 96 | A-1 | include | A+C | direct method ancestor (path-space objective) | arXiv:2111.15141 |
| P0035 | Denoising Diffusion Samplers | ICLR | seed ref, R-arx-pdf | 2023 | 95 | A-2 | include | A+C | direct method ancestor (learned backward drift) | arXiv:2302.13834 |
| P0039 | NETS: Non-Equilibrium Transport Sampler | preprint | seed ref, R-arx-pdf | 2024 | 94 | A-3 | include | A+C | non-equilibrium annealed reweighted sampler; SPS-analogous | arXiv:2410.02711 |
| P0038 | Controlled Monte Carlo Diffusions | ICLR | seed ref | 2024 | 90 | A-4 | include | A+C | learn-both-drifts (explicitly named parallel in seed) | arXiv:2307.01050 |
| P0036 | Optimal-control view of diffusion generative modeling | TMLR | seed ref | 2024 | 82 | A-5 | include | A | theoretical umbrella for learned-diffusion samplers | arXiv:2211.01364 |
| P0037 | Improved sampling via learned diffusions | ICLR | seed ref | 2024 | 81 | A-6 | include | A | log-variance loss / better learned samplers | arXiv:2307.01198 |
| P0025 | Score-based generative modeling (Song–Ermon) | NeurIPS | seed ref | 2019 | 78 | A-7 | include | A | score-based ancestor | arXiv:1907.05600 |
| P0019 | Stochastic normalizing flows (Wu, Köhler, Noe) | NeurIPS | seed ref | 2020 | 76 | A-8 / C-3 | include | A+C | SNF foundational (arXiv ID needs cross-check) | NeurIPS 2020 |
| P0002 | Variational inference with normalizing flows | ICML | seed ref | 2015 | 70 | A-9 | include | A | NF ancestor | ICML 2015 |
| P0003 | Neural ODE | NeurIPS | seed ref | 2018 | 55 | A-10 | include | A | CNF backbone | NeurIPS 2018 |
| P0042 | GFlowNets (Bengio 2021) | NeurIPS | seed ref | 2021 | 58 | A-11 | include | A+C | trajectory-balance ancestor | NeurIPS 2021 |
| P0043 | GFlowNet foundations | JMLR | seed ref | 2023 | 55 | A-12 | include | A+C | GFlowNet theory | JMLR 2023 |
| P0044 | Trajectory balance (Malkin et al.) | NeurIPS | seed ref | 2022 | 70 | A-13 | include | A+C | trajectory-balance loss named in SPS Section 2 | NeurIPS 2022 |
| P0060 | Importance Weighted Score Matching | arXiv | R-arx-api | 2025 | 60 | A-14 | uncertain (potentially missed) | A+C | pre-seed; explicit IW correction; not in seed refs | arXiv:2505.19431 |
| P0064 | ScoreNF: Score-Based NF for Sampling Unnormalized Distributions | arXiv | R-inspire-flow | 2025 | 72 | A/B-15 | uncertain (potentially missed) | A+C | directly on-topic; not in seed refs | arXiv:2510.21330 |
| P0063 | Neural Triangular Transport Maps for Sampling in Lattice QCD | arXiv | R-inspire-flow | 2025 | 68 | A/B-16 | uncertain (potentially missed) | A+B | alternative transport-map sampler; not in seed refs | arXiv:2510.13112 |
| P0040 | Parisi & Wu — Stochastic Quantization | Sci.Sin. | seed ref | 1981 | 65 | A-17 | include | A | SQ foundational | Sci.Sin. 1981 |
| P0041 | Damgaard & Huffel — Stochastic Quantization review | Phys.Rept. | seed ref | 1987 | 55 | A-18 | include | A | SQ review | Phys.Rept. 1987 |
| P0006 | Albergo, Kanwar, Shanahan 2019 | PRD | seed ref, R-arx-pdf | 2019 | 96 | B-1 | include | B | founding LFT flow-sampler paper | arXiv:1904.12072 |
| P0009 | Kanwar et al. 2020 | PRL | seed ref, R-arx-pdf | 2020 | 92 | B-2 | include | B | equivariant flow for LGT | arXiv:2003.06413 |
| P0007 | Nicoli et al. 2021 | PRL | seed ref, R-arx-pdf | 2021 | 92 | B-3 / C-1 | include | B+C | thermodynamic observables + NIS reweighting | arXiv:2007.07115 |
| P0008 | Fermionic flow-based sampling (Albergo et al. 2021) | PRD | seed ref | 2021 | 82 | B-4 | include | B | fermionic-lattice extension | arXiv:2106.05934 |
| P0010 | SU(N) gauge equivariant flows (Boyda 2021) | PRD | seed ref | 2021 | 82 | B-5 | include | B | SU(N) extension | 10.1103/PhysRevD.103.074504 |
| P0011 | Schwinger model at criticality (Albergo 2022) | PRD | seed ref | 2022 | 84 | B-6 | include | B | fermionic critical benchmark | arXiv:2202.11712 |
| P0016 | Multimodal flow (Hackett 2025) | preprint | seed ref | 2025 | 84 | B-7 / C-4 | include | B+C | multimodal proposal + reweighting | arXiv:2107.00734 |
| P0013 | Equivariant CNFs (Gerdes 2023) | SciPost | seed ref | 2023 | 78 | B-8 | include | B | equivariant CNFs on LFT | arXiv:2207.00283 |
| P0014 | Scale-up equivariant CNFs (de Haan 2021) | preprint | seed ref | 2021 | 70 | B-9 | include | B | scale-up CNF | arXiv:2110.02673 |
| P0020 | Caselle SNF non-equilibrium 2022 | JHEP | seed ref, R-arx-pdf | 2022 | 92 | B-10 / C-2 | include | B+C | SNF on lattice with Jarzynski reweighting | arXiv:2201.08862 |
| P0021 | Caselle SNF PoS 2023 | PoS | seed ref | 2023 | 72 | B-11 | include | B+C | conf extension | arXiv:2210.03139 |
| P0023 | Caselle EST SNF (JHEP 2025) | JHEP | seed ref | 2025 | 78 | B-12 | include | B | EST application via SNF | arXiv:2409.15937 |
| P0022 | Caselle EST SNF (preprint 2025) | preprint | seed ref | 2025 | 72 | B-13 | include | B | EST via SNF | arXiv:2412.19109 |
| P0017 | Fourier-flow Feynman paths (Chen 2023) | PRD | seed ref | 2023 | 76 | B-14 | include | A+B | Fourier-basis flow for path integrals | arXiv:2211.03470 |
| P0024 | Zhou Endrődi Pang Stöcker 2019 | PRD | seed ref | 2019 | 60 | B-15 | include | B | early generative NN for scalar LFT | arXiv:1810.12879 |
| P0026 | Diffusion as stochastic quantization (Wang, Aarts, Zhou 2024) | JHEP | seed ref, R-arx-pdf | 2024 | 92 | B-16 / A-19 | include | A+B | direct link SPS ↔ diffusion ↔ SQ; same-group lineage | arXiv:2309.17082 |
| P0027 | Physics-conditioned DM for LGT (Zhu 2026) | JHEP | seed ref | 2026 | 82 | B-17 | include | B | conditioned DM | arXiv:2502.05504 |
| P0028 | Group-equivariant DM (Vega 2025) | preprint | seed ref | 2025 | 78 | B-18 | include | B | equivariant DM | arXiv:2510.26081 |
| P0029 | Equivariant DM for NAGT (Aarts 2026) | preprint | seed ref | 2026 | 84 | B-19 | include | B | NAGT diffusion | arXiv:2601.19552 |
| P0030 | SU(2) LGT DM (Alharazin 2026) | preprint | seed ref | 2026 | 76 | B-20 | include | B | SU(2) 2D DM | arXiv:2602.09045 |
| P0031 | SU(N) LGT DM (Komijani 2026) | preprint | seed ref | 2026 | 82 | B-21 | include | B | SU(N) DM | arXiv:2605.06134 |
| P0032 | Complex Langevin + DM (Aarts 2025) | JHEP | seed ref | 2025 | 76 | B-22 / A-20 | include | A+B | complex-Langevin + DM | arXiv:2510.01328 |
| P0033 | Operator spectroscopy of trained lattice samplers (Qian 2026) | preprint | seed ref | 2026 | 74 | B-23 | include | B | diagnostic for trained samplers | arXiv:2605.11199 |
| P0004 | VAN (Wu, Wang, Zhang 2019) | PRL | seed ref | 2019 | 74 | B-24 / A-21 | include | A+B | VAN for statistical mechanics | 10.1103/PhysRevLett.122.080602 |
| P0005 | Cont-mixture ARNs KT (Wang 2022) | Chin.Phys.Lett. | seed ref | 2022 | 62 | B-25 | include | B | AR net on lattice KT | arXiv:2005.04857 |
| P0012 | VANs for φ⁴ (Qian & Chen 2025) | preprint | seed ref | 2025 | 78 | B-26 | include | B | same-group VAN for φ⁴ | arXiv:2512.19575 |
| P0015 | Generative networks for non-trivial topology (Chen SY 2025) | PoS | seed ref | 2025 | 74 | B-27 | include | B | same first-author lineage | arXiv:2502.02127 |
| P0018 | QCD-ML review (Zhou 2024) | PPNP | seed ref | 2024 | 40 | B-28 | include | B (context) | review only | arXiv:2303.15136 |
| P0061 | SESaMo | arXiv | R-inspire-diff | 2025 | 55 | B-29 | uncertain (potentially missed) | B | symmetry-enforcing NF; not in seed refs | arXiv:2505.19619 |
| P0062 | Symmetry-preserving NN in LFT | arXiv | R-inspire-flow | 2025 | 55 | B-30 | uncertain (potentially missed) | B | not in seed refs | arXiv:2506.12493 |
| P0065 | Scaling flow topology sampling SU(3) | arXiv | R-inspire-flow | 2025 | 68 | B-31 | uncertain (potentially missed) | B | not in seed refs | arXiv:2510.25704 |
| P0066 | Spectral Diffusion SU(N) | arXiv | R-inspire-flow, R-inspire-diff | 2025 | 68 | B-32 | uncertain (potentially missed) | B | not in seed refs | arXiv:2512.19877 |
| P0067 | Analytic bijections for interpretable NFs | arXiv | R-inspire-flow | 2026 | 55 | B-33 | uncertain (potentially missed) | A+B | not in seed refs | arXiv:2601.10774 |
| P0068 | Flow-based topological-freezing mitigation | arXiv | R-inspire-flow | 2026 | 78 | B-34 / C-5 | uncertain (potentially missed) | B+C | HIGH-priority: direct competitor for seed's topological-freezing motivation | arXiv:2601.20708 |
| P0069 | NF-based density-of-states with θ-term | arXiv | R-inspire-flow | 2026 | 72 | B-35 / C-6 | uncertain (potentially missed) | B+C | NF density-of-states = reweighting; not in seed refs | arXiv:2603.12501 |
| P0070 | Enhanced sampling for LGT | arXiv | R-inspire-flow | 2026 | 55 | B-36 | uncertain (potentially missed) | B | not in seed refs | arXiv:2604.01287 |
| P0071 | Scalable generative sampling + multilevel estimation LFT near criticality | arXiv | R-inspire-flow | 2026 | 76 | B-37 / C-7 | uncertain (potentially missed) | B+C | near-criticality generative + multilevel; not in seed refs | arXiv:2604.10209 |
| P0072 | ML for 4D SU(3) LGT | arXiv | R-inspire-flow, R-inspire-diff | 2026 | 68 | B-38 | uncertain (potentially missed) | B | not in seed refs | arXiv:2604.12416 |
| P0073 | NF for all-orders QED corrections in LFT | arXiv | R-inspire-flow | 2026 | 55 | B-39 | uncertain (potentially missed) | B | not in seed refs | arXiv:2605.22444 |
| P0074 | Learning generating functional for variance reduction in lattice QCD | arXiv | R-inspire-flow | 2026 | 65 | B-40 / C-8 | uncertain (potentially missed) | B+C | same-month as seed; possibly concurrent, not in seed refs | arXiv:2606.15986 |
| P0047 | Jarzynski equality 2013 | Prog.Math.Phys. | seed ref | 2013 | 68 | C-9 | include | C | Jarzynski identity (exactness ancestor) | 10.1007/978-3-0348-0359-5_4 |
| P0045 | MALA optimal scaling (Roberts–Rosenthal 1998) | JRSS-B | seed ref | 1998 | 42 | C-10 | include | A+C | Langevin scaling baseline | JRSS-B |
| P0046 | Riemann-manifold Langevin/HMC (Girolami–Calderhead 2011) | JRSS-B | seed ref | 2011 | 42 | C-11 | include | A+C | manifold MALA/HMC baseline | 10.1111/j.1467-9868.2010.00765.x |
| P0075 | Sampling Schwinger with equivariant DM | arXiv | R-inspire-diff | 2026 | — | — | monitor | B | post-seed | arXiv:2606.27481 |
| P0076 | DM near criticality LFT | arXiv | R-inspire-diff, R-inspire-flow | 2026 | — | — | monitor | B | post-seed | arXiv:2607.08505 |
| P0077 | Self-learning DM LFT config generation | arXiv | R-inspire-flow, R-inspire-diff | 2026 | — | — | monitor | B | post-seed | arXiv:2607.12587 |
| P0078 | Stochastic Quantization as Optimal Control | arXiv | R-inspire-diff | 2026 | — | — | monitor | A+B | post-seed; extends SPS's SQ+control angle | arXiv:2607.21436 |
| P0079 | Weight-space physics for LQFT | arXiv | R-inspire-flow | 2026 | — | — | monitor | B | post-seed | arXiv:2607.07127 |
| P0080 | NFs for pseudo-PDFs | arXiv | R-inspire-flow | 2026 | — | — | monitor | B (adjacent) | post-seed; not a Gibbs-measure sampler | arXiv:2607.25282 |
| P0048–P0059 | Various thermodynamics/information-theory foundational refs | INSPIRE seed record | seed ref | 1951–2024 | — | — | exclude | none | out-of-scope for facet map | see candidate_pool.md |
| P0081 | LGT via LLVM autodiff | arXiv | R-inspire-flow | 2026 | — | — | exclude | none | toolchain, not a learned sampler | arXiv:2602.20516 |
| P0082 | Particle MC for LFT | arXiv | R-inspire-flow | 2025 | — | — | exclude | none | classical MC variant | arXiv:2511.15196 |

## Facet Coverage Summary

- Facet A (learned samplers for unnormalized densities): 14 include (PIS, DDS, NETS, CMCD, Berner, Richter-Berner, Song-Ermon, SNF, Rezende, Neural ODE, GFlowNets ×3, Trajectory balance) + 2 uncertain potentially-missed (IWSM, ScoreNF).
- Facet B (learned samplers for LFT): 25 include (Albergo/Kanwar/Nicoli/Hackett/Caselle/Wang/Zhou/Boyda/Qian/Gerdes/de Haan/Chen SY/Chen S 2023/Aarts/Alharazin/Komijani/Vega/Zhu/Aarts 2025 lines) + 12 uncertain potentially-missed.
- Facet C (correction/exactness mechanisms): 11 include (IMH via seed; Nicoli reweighting; Caselle SNF Jarzynski; Hackett reweighting; NETS non-equilibrium; DDS; PIS; CMCD; Jarzynski 2013; GFlowNet trajectory balance; MALA/Roberts-Rosenthal) + 8 uncertain potentially-missed (IWSM, ScoreNF, topological-freezing flow, NF density-of-states, near-criticality multilevel, learning generating functional variance reduction, plus overlaps).

Each facet has ≥3 representative confirmed works with C1+ evidence; several with C3 evidence. Coverage floor met per search_scope.md.
