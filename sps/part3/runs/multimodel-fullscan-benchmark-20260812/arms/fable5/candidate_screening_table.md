# Candidate Screening Table

Labels: include (enters landscape), exclude (outside scope, reason recorded),
uncertain (needs verification), monitor (not central now). Non-pool overflow
hits are kept in the monitor/excluded overflow section of `candidate_pool.md`
(reference 30 — never silently dropped).

## Pool entries

| id | title / item (short) | route(s) found | year | label | facet | reason | URL / DOI |
|---|---|---|---|---:|---|---|---|
| P0001 | Stochastic Path Sampler for LFT (seed) | seed | 2026 | include | seed | focal paper; C3 | arXiv:2606.13790 |
| P0002 | Flow-based generative models for MCMC in LFT | bib+S2 | 2019 | include | F2 | founding flow-for-LFT; MH correction; C3 | arXiv:1904.12072 |
| P0003 | Equivariant flow-based sampling for lattice gauge theory | bib+S2 | 2020 | include | F2 | gauge-equivariant flows | arXiv:2003.06413 |
| P0004 | Sampling using SU(N) gauge equivariant flows | bib+S2 | 2020 | include | F2 | SU(N) flows; ID resolved via S2 | arXiv:2008.05456 |
| P0005 | Flow-based sampling for fermionic LFT | bib+S2+Q003 | 2021 | include | F2 | fermionic extension | arXiv:2106.05934 |
| P0006 | Flow-based sampling in lattice Schwinger model at criticality | bib+S2 | 2022 | include | F2 | criticality benchmark | arXiv:2202.11712 |
| P0007 | Flow-based sampling for multimodal/extended-mode distributions | bib+S2 | 2021 | include | F2 | multimodality failure mode | arXiv:2107.00734 |
| P0008 | Estimation of thermodynamic observables in LFT with DGMs | bib+S2 | 2020 | include | F2/F3 | IS-reweighting correction on lattice | arXiv:2007.07115 |
| P0009 | Scaling up ML for QFT with equivariant continuous flows | bib+S2 | 2021 | include | F2 | CNF for LFT | arXiv:2110.02673 |
| P0010 | Learning lattice QFTs with equivariant continuous flows | bib+S2 | 2022 | include | F2 | CNF for LFT | arXiv:2207.00283 |
| P0011 | Stochastic normalizing flows (ML) | bib+S2 | 2020 | include | F1/F3 | flows+stochastic layers, NEQ path weights; C3 | arXiv:2002.06707 |
| P0012 | SNFs as non-equilibrium transformations | bib+S2+Q003 | 2022 | include | F2/F3 | Jarzynski/Crooks correction on lattice; C3 | arXiv:2201.08862 |
| P0013 | SNFs for lattice field theory (PoS) | bib+S2+Q003 | 2022 | monitor | F2 | proceedings version of P0012 | arXiv:2210.03139 |
| P0014 | Effective string width/shape via SNF | bib | 2024 | monitor | F2 | application; C1(bib-of-C3) only, unverified | arXiv:2409.15937 |
| P0015 | SNFs for effective string theory | bib+Q003 | 2024 | monitor | F2 | application | arXiv:2412.19109 |
| P0016 | Solving statistical mechanics using VANs | bib+S2 | 2018 | include | F1 | variational free-energy training, exact AR likelihood | arXiv:1809.10606 |
| P0017 | Continuous-mixture AR networks (KT transition) | bib+S2 | 2020 | monitor | F2 | peripheral application | arXiv:2005.04857 |
| P0018 | VANs applied to phi4 | bib | 2025 | include | F2 | seed-author lineage; C1(bib-of-C3) UNVERIFIED label | arXiv:2512.19575 |
| P0019 | Fourier-flow model generating Feynman paths | bib+S2 | 2022 | monitor | F2 | peripheral (paths, not lattice fields) | arXiv:2211.03470 |
| P0020 | Generative networks for manifolds with non-trivial topology | bib | 2025 | include | F2 | seed-author lineage; C1(bib-of-C3) UNVERIFIED label | arXiv:2502.02127 |
| P0021 | Regressive and generative NNs for scalar field theory | bib+S2 | 2018 | monitor | F2 | early GAN-family, data-driven side | arXiv:1810.12879 |
| P0022 | Operator spectroscopy of trained lattice samplers | bib | 2026 | include | F2 | diagnostics of learned proposals; C1(bib-of-C3) UNVERIFIED label | arXiv:2605.11199 |
| P0023 | Diffusion models as stochastic quantization in LFT | bib+S2 | 2023 | include | F2 | diffusion↔SQ bridge; C3 | arXiv:2309.17082 |
| P0024 | Physics-conditioned diffusion models for lattice gauge theory | bib+S2 | 2025 | include | F2 | diffusion-for-LFT representative | arXiv:2502.05504 |
| P0025 | Generalizable equivariant diffusion models (non-abelian) | bib | 2026 | monitor | F2 | diffusion cluster member; C1(bib-of-C3) | arXiv:2601.19552 |
| P0026 | Diffusion models for SU(2) LGT in 2D | bib | 2026 | monitor | F2 | diffusion cluster member; C1(bib-of-C3) | arXiv:2602.09045 |
| P0027 | Diffusion model for SU(N) gauge theories | bib | 2026 | monitor | F2 | diffusion cluster member; C1(bib-of-C3) | arXiv:2605.06134 |
| P0028 | Group-equivariant diffusion models for LFT | bib | 2025 | monitor | F2 | diffusion cluster member; C1(bib-of-C3) | arXiv:2510.26081 |
| P0029 | Complex Langevin + score/energy-based diffusion | bib | 2025 | monitor | F2 | sign-problem niche; C1(bib-of-C3) | arXiv:2510.01328 |
| P0030 | Path Integral Sampler | bib+S2 | 2021 | include | F1/F3 | closest ML family per seed; path-space KL; C3 | arXiv:2111.15141 |
| P0031 | Denoising Diffusion Samplers | bib+S2 | 2023 | include | F1/F3 | data-free diffusion sampler; C3 | arXiv:2302.13834 |
| P0032 | Optimal control perspective on diffusion generative modeling | bib+S2 | 2022 | include | F1 | OC/DIS lineage | arXiv:2211.01364 |
| P0033 | Improved sampling via learned diffusions | bib+S2 | 2023 | include | F1 | unifies PIS/DIS (general bridge) | arXiv:2307.01198 |
| P0034 | Controlled Monte Carlo Diffusions | bib+S2 | 2023 | include | F1/F3 | learns forward+backward drifts like seed | arXiv:2307.01050 |
| P0035 | NETS: non-equilibrium transport sampler | bib+S2 | 2024 | include | F1/F3 | NEQ transport + Jarzynski weights | arXiv:2410.02711 |
| P0036 | GFlowNet (flow network generative models) | bib+S2 | 2021 | include | F1/F3 | trajectory-balance ancestry of seed objective | arXiv:2106.04399 |
| P0037 | Trajectory balance: improved credit assignment in GFlowNets | bib+S2 | 2022 | include | F1/F3 | trajectory-level balance named in seed §2 | arXiv:2201.13259 |
| P0038 | Variational inference with normalizing flows | bib+S2 | 2015 | include | F1 | NF foundation | arXiv:1505.05770 |
| P0039 | Generative modeling by estimating gradients (score) | bib+S2 | 2019 | monitor | F1 | data-driven foundation, not unnormalized-target | arXiv:1907.05600 |
| P0040 | Introduction to NF for LFT (notes) | Q003+S2 | 2021 | include | F2 | pedagogical reference of founding group | arXiv:2101.08176 |
| P0041 | HMC with normalizing flows | Q003 | 2021 | include | F2 | flow-augmented HMC (field-transformation HMC) | arXiv:2112.01586 |
| P0042 | Detecting/mitigating mode-collapse for flow-based sampling | Q003+S2+web23 | 2023 | include | F2/F3 | limitation cluster: mode collapse biases estimators | arXiv:2302.14082 |
| P0043 | SCORENF: score-based NF for unnormalized distributions | Q003+S2 | 2025 | include | F1/F2 | score↔NF bridge for unnormalized targets | arXiv:2510.21330 |
| P0044 | Sampling QCD configs with gauge-equivariant flow models | Q003 | 2022 | monitor | F2 | cluster member | arXiv:2208.03832 |
| P0045 | NeuMC package | Q003 | 2025 | monitor | F2 | software | arXiv:2503.11482 |
| P0046 | Conditional NF for MCMC in critical region | Q003+INSPIRE | 2022 | include | F2 | criticality focus, same problem as seed | arXiv:2207.00980 |
| P0047 | Scalable generative sampling near criticality | Q003+INSPIRE | 2026 | monitor | F2 | parallel 2026 work | arXiv:2604.10209 |
| P0048 | Boltzmann Generators | Q004+S2 | 2018 | include | F1/F3 | major predecessor family (not cited by seed); reweighting; C3 | arXiv:1812.01729 |
| P0049 | Annealed Flow Transport Monte Carlo | Q005+S2 | 2021 | include | F1/F3 | flows in SMC; SMC-weight correction | arXiv:2102.07501 |
| P0050 | CRAFT | Q005+S2 | 2022 | include | F1/F3 | AFT continual variant | arXiv:2201.13117 |
| P0051 | Flow Annealed Importance Sampling Bootstrap | Q005+S2 | 2022 | include | F1/F3 | AIS-driven flow training | arXiv:2208.01893 |
| P0052 | Learning optimal flows for NEQ importance sampling | Q005+S2 | 2022 | include | F1/F3 | NEQ-IS lineage (pre-NETS) | arXiv:2206.09908 |
| P0053 | Trivializing maps, Wilson flow and HMC (Lüscher) | Q006+S2 | 2009 | include | F2 | conceptual ancestor of learned maps for LFT | arXiv:0907.5491 |
| P0054 | Testing trivializing maps in HMC | Q006 | 2011 | include | F2 | early limitation result | arXiv:1102.1852 |
| P0055 | Efficient modeling of trivializing maps for phi4 (scalability) | Q006+S2 | 2021 | include | F2 | scalability critique | arXiv:2105.12481 |
| P0056 | ML trivializing maps: how flow-based samplers scale up | Q006+S2 | 2021 | include | F2 | scaling study | arXiv:2112.15532 |
| P0057 | L2HMC: generalizing HMC with neural networks | Q008+S2 | 2017 | include | F1 | learned-MCMC-kernel family; exact MH retained | arXiv:1711.09268 |
| P0058 | Deep learning HMC | Q008+S2 | 2021 | include | F2 | L2HMC on lattice | arXiv:2105.03418 |
| P0059 | LeapfrogLayers: trainable topological sampling | Q008 | 2021 | include | F2 | learned-HMC lattice line | arXiv:2112.01582 |
| P0060 | MLMC: machine learning Monte Carlo for LGT | Q008 | 2023 | include | F2 | learned-MC lattice line | arXiv:2312.08936 |
| P0061 | Self-learning Monte Carlo method | Q009+S2 | 2016 | include | F1 | learned effective-action proposals + exact MH | arXiv:1610.03137 |
| P0062 | SLMC for non-abelian gauge theory with dynamical fermions | Q009 | 2020 | include | F2 | SLMC on lattice gauge | arXiv:2010.11900 |
| P0063 | Asymptotically unbiased generative neural sampling | S2 | 2019 | include | F1/F3 | founding neural-IS reweighting (predecessor of P0008) | arXiv:1910.13496 |
| P0064 | Adaptive Monte Carlo augmented with normalizing flows | S2 | 2021 | include | F1 | adaptive flow+MCMC family | arXiv:2105.12603 |
| P0065 | Advances in ML-based sampling motivated by lattice QCD (review) | S2 | 2023 | include | F2 | field review; C3 | arXiv:2309.01156 |
| P0066 | Stochastic quantization as optimal control | S2 fwd | 2026 | monitor | descendant | cites seed; not predecessor; single-channel C1 | arXiv:2607.21436 |
| P0067 | Neural NEQ HMC for corrected Boltzmann sampling | S2 fwd | 2026 | monitor | descendant | cites seed; single-channel C1 | arXiv:2607.15682 |
| P0068 | Diffusion models for sampling near criticality in LFT | S2 fwd+INSPIRE | 2026 | monitor | descendant | cites seed | arXiv:2607.08505 |
| P0069 | Aspects of scaling/scalability for flow-based sampling of lattice QCD | INSPIRE | 2022 | include | F2 | central scaling-limitation study | arXiv:2211.07541 |
| P0070 | Generative models for sampling of LFT | INSPIRE | 2020 | monitor | F2 | early overview | arXiv:2012.01442 |
| P0071 | Learning trivializing gradient flows for LGT | web23 | 2023 | include | F2 | Lüscher+CNF unification; arXiv ID not verified this run | doi:10.1103/PhysRevD.107.L051504 |
| P0072 | Super-resolving normalising flows for LFT | web23 | 2024 | monitor | F2 | variant | arXiv:2412.12842 |
| P0073 | Beyond ELBOs: large-scale evaluation of variational sampling | web24 | 2024 | include | F1/F3 | benchmark; names DIS/MCD/UHA/LDVI sub-branches | arXiv:2406.07423 |

## Counts

- Pool entries screened: 73
- include: 53, monitor: 20, exclude (pool): 0
- Non-pool overflow (monitor/excluded, in candidate_pool.md overflow section): ~75 raw hits (≈50 monitor-tier, ≈25 excluded with reasons)
- Seed-bibliography context refs excluded at harvest (thermodynamics/entropy/ML foundations not in sampler scope: Coleman-Noll, Jarzynski 2013, Parisi-Wu 1981, Damgaard-Huffel 1987, Kullback-Leibler 1951, Landauer, Sagawa-Ueda, Parrondo, MALA/Roberts-Rosenthal, Girolami-Calderhead, Neural ODE, Kleidon, Dyke, Jakimowicz, Karbowski, Purvis, Skinner-Dunkel, Pachter, Zhou 2024 QCD-ML review, Wu 2019 GAN ref 56 unresolved): recorded here, not silently dropped. Parisi-Wu/Damgaard-Huffel remain visible via keyword T011 (stochastic quantization ancestry).
