# Candidate Pool

All candidates appear here before confirmation/exclusion. No silent deletion.
Verification: C0 candidate only / C1 metadata verified / C2 abstract checked /
C3 full text checked / C4 claim-level. `C1(bib-of-C3)` = bibliography entry
read inside the C3-verified seed full text; identity still needs an
independent source to reach C2 (reference 34 cross-validation rule).

Facets: F1 = learned/neural samplers for unnormalized targets (general);
F2 = learned samplers for lattice field theory; F3 = correction/exactness
mechanisms.

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Facet | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|
| P0001 | Stochastic Path Sampler for Lattice Field Theory | S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou | 2026 | arXiv hep-lat | arXiv:2606.13790 | arXiv | seed | R0001 | confirmed | C3 | seed | high | seed paper; PDF on disk (E0002) |
| P0002 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | Albergo, Kanwar, Shanahan | 2019 | Phys. Rev. D 100 034515 | arXiv:1904.12072 | seed bib [5] | backward | R0001 | confirmed | C3 | F2 | high | founding flow+MH paper for LFT |
| P0003 | Equivariant flow-based sampling for lattice gauge theory | Kanwar et al. | 2020 | Phys. Rev. Lett. 125 121601 | arXiv:2003.06413 | seed bib [8] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | high |  |
| P0004 | Estimation of thermodynamic observables in lattice field theories with deep generative models | Nicoli et al. | 2021 | Phys. Rev. Lett. 126 032001 | arXiv:2007.07115 | seed bib [6] | backward | R0001 | candidate | C1(bib-of-C3) | F2+F3 | high | reweighting/estimator mechanism |
| P0005 | Flow-based sampling for fermionic lattice field theories | Albergo et al. | 2021 | Phys. Rev. D 104 114507 | arXiv:2106.05934 | seed bib [7] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium |  |
| P0006 | Flow-based sampling in the lattice Schwinger model at criticality | Albergo et al. | 2022 | Phys. Rev. D 106 014514 | arXiv:2202.11712 | seed bib [10] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium |  |
| P0007 | Flow-based sampling for multimodal and extended-mode distributions in lattice field theory | Hackett et al. | 2021 | arXiv | arXiv:2107.00734 | seed bib [15] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium |  |
| P0008 | Scaling up machine learning for quantum field theory with equivariant continuous flows | de Haan, Rainone, Cheng, Bondesan | 2021 | arXiv | arXiv:2110.02673 | seed bib [13] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium |  |
| P0009 | Learning lattice quantum field theories with equivariant continuous flows | Gerdes et al. | 2023 | SciPost Phys. 15 238 | arXiv:2207.00283 | seed bib [12] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium |  |
| P0010 | Solving statistical mechanics using variational autoregressive networks | Wu, Wang, Zhang | 2019 | Phys. Rev. Lett. 122 080602 | arXiv:1809.10606 + DOI 10.1103/PhysRevLett.122.080602 | seed bib [3] | backward | R0001 | candidate | C1 | F1 | high | ID confirmed R0003 call 12 (E0003), two-source |
| P0011 | Continuous-mixture autoregressive networks learning the Kosterlitz-Thouless transition | Wang, Jiang, He, Zhou | 2022 | Chin. Phys. Lett. 39 120502 | arXiv:2005.04857 | seed bib [4] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low |  |
| P0012 | Fourier-flow model generating Feynman paths | S. Chen et al. | 2023 | Phys. Rev. D 107 056001 | arXiv:2211.03470 | seed bib [16] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium | same-author lineage (Chen/Zhou) |
| P0013 | Regressive and generative neural networks for scalar field theory | Zhou, Endrodi, Pang, Stoecker | 2019 | Phys. Rev. D 100 011501 | arXiv:1810.12879 | seed bib [23] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium | same-author lineage (Zhou) |
| P0014 | Stochastic normalizing flows | Wu, Koehler, Noe | 2020 | NeurIPS 33 | arXiv:2002.06707 (recovered R0002, DEDUP0001) | seed bib [18] + arXiv API Q003 | backward+query | R0001 | confirmed | C3 | F1+F3 | high | arXiv ID recovered via Q003; metadata now two-source |
| P0015 | Stochastic normalizing flows as non-equilibrium transformations | Caselle, Cellini, Nada, Panero | 2022 | JHEP 07 015 | arXiv:2201.08862 | seed bib [19] | backward | R0001 | confirmed | C3 | F2+F3 | high | closest mechanism family |
| P0016 | Stochastic normalizing flows for lattice field theory | Caselle, Cellini, Nada, Panero | 2023 | PoS LATTICE2022 005 | arXiv:2210.03139 | seed bib [20] | backward | R0001 | candidate | C1(bib-of-C3) | F2+F3 | low | proceedings of P0015 line |
| P0017 | Numerical determination of the width and shape of the effective string using stochastic normalizing flows | Caselle, Cellini, Nada | 2025 | JHEP 02 090 | arXiv:2409.15937 | seed bib [22] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low |  |
| P0018 | Stochastic normalizing flows for effective string theory | Caselle, Cellini, Nada | 2024 | arXiv | arXiv:2412.19109 | seed bib [21] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low |  |
| P0019 | Diffusion models as stochastic quantization in lattice field theory | L. Wang, Aarts, Zhou | 2024 | JHEP 2024 60 | arXiv:2309.17082 | seed bib [25] | backward | R0001 | confirmed | C3 | F2 | high | same-author lineage (Aarts/Zhou); stochastic-quantization link |
| P0020 | Physics-conditioned diffusion models for lattice gauge theory | Zhu, Aarts, Wang, Zhou, Wang | 2026 | JHEP 03 111 | arXiv:2502.05504 | seed bib [26] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium | same-author lineage |
| P0021 | Group-equivariant diffusion models for lattice field theory | Vega, Komijani, El-Khadra, Marinkovic | 2025 | arXiv | arXiv:2510.26081 | seed bib [27] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low |  |
| P0022 | Generalizable equivariant diffusion models for non-Abelian lattice gauge theory | Aarts et al. | 2026 | arXiv | arXiv:2601.19552 | seed bib [28] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low | same-author lineage |
| P0023 | Diffusion models for SU(2) lattice gauge theory in two dimensions | Alharazin, Panteleeva, Sun | 2026 | arXiv | arXiv:2602.09045 | seed bib [29] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low |  |
| P0024 | Diffusion model for SU(N) gauge theories | Komijani, Marinkovic, Turgut | 2026 | arXiv | arXiv:2605.06134 | seed bib [30] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low |  |
| P0025 | Combining complex Langevin dynamics with score-based and energy-based diffusion models | Aarts, Habibi, Wang, Zhou | 2025 | JHEP 12 160 | arXiv:2510.01328 | seed bib [31] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | low | same-author lineage |
| P0026 | Operator spectroscopy of trained lattice samplers | M. Qian | 2026 | arXiv | arXiv:2605.11199 | seed bib [32] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium | same-author lineage (Qian) |
| P0027 | Variational autoregressive networks applied to phi^4 field theory systems | Qian, Chen | 2025 | arXiv | arXiv:2512.19575 | seed bib [11] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium | same-author lineage (Qian/Chen) |
| P0028 | Exploring generative networks for manifolds with non-trivial topology | S.-Y. Chen, Aarts, Lucini | 2025 | PoS LATTICE2024 042 | arXiv:2502.02127 | seed bib [14] | backward | R0001 | candidate | C1(bib-of-C3) | F2 | medium | same-author lineage (Chen/Aarts/Lucini) |
| P0029 | Path Integral Sampler: a stochastic control approach for sampling | Q. Zhang, Y. Chen | 2022 | ICLR 2022 | arXiv:2111.15141 | seed bib [33] | backward | R0001 | confirmed | C3 | F1 | high | closest general-sampler predecessor family |
| P0030 | Denoising Diffusion Samplers | Vargas, Grathwohl, Doucet | 2023 | ICLR 2023 | arXiv:2302.13834 | seed bib [34] | backward | R0001 | confirmed | C3 | F1 | high |  |
| P0031 | An optimal control perspective on diffusion-based generative modeling | Berner, Richter, Ullrich | 2024 | TMLR | arXiv:2211.01364 | seed bib [35] | backward | R0001 | candidate | C1(bib-of-C3) | F1 | medium |  |
| P0032 | Improved sampling via learned diffusions | Richter, Berner | 2024 | ICLR 2024 | arXiv:2307.01198 | seed bib [36] | backward | R0001 | candidate | C1(bib-of-C3) | F1 | medium |  |
| P0033 | Transport meets variational inference: controlled Monte Carlo diffusions | Vargas, Padhy, Blessing, Nuesken | 2024 | ICLR 2024 | arXiv:2307.01050 | seed bib [37] | backward | R0001 | candidate | C1(bib-of-C3) | F1 | medium |  |
| P0034 | NETS: a Non-Equilibrium Transport Sampler | Albergo, Vanden-Eijnden | 2024 | arXiv | arXiv:2410.02711 | seed bib [38] | backward | R0001 | confirmed | C3 | F1+F3 | high | Jarzynski-weighted transport |
| P0035 | Trajectory balance: improved credit assignment in GFlowNets | Malkin, Jain, Bengio, Sun, Bengio | 2022 | NeurIPS 35 | arXiv:2201.13259 | seed bib [53] | backward | R0001 | candidate | C1 | F1 | medium | ID confirmed R0003 call 12 (E0003); trajectory-balance loss namesake |
| P0036 | Flow network based generative models for non-iterative diverse candidate generation (GFlowNet) | E. Bengio et al. | 2021 | NeurIPS 34 | arXiv:2106.04399 | seed bib [51] | backward | R0001 | candidate | C1 | F1 | low | ID confirmed R0003 call 12 (E0003) |
| P0037 | Perturbation theory without gauge fixing (stochastic quantization) | Parisi, Wu | 1981 | Sci. Sin. 24 483 | none (pre-arXiv) | seed bib [49] | backward | R0001 | candidate | C1(bib-of-C3) | F3 | medium | mechanism root; no arXiv record expected |
| P0038 | Equalities and inequalities: irreversibility and the second law at the nanoscale | Jarzynski | 2013 | Prog. Math. Phys. 63 145 | none printed | seed bib [58] | backward | R0001 | candidate | C1(bib-of-C3) | F3 | medium | nonequilibrium-equality mechanism root |
| P0039 | Variational inference with normalizing flows | Rezende, Mohamed | 2015 | ICML 37 (PMLR) | arXiv:1505.05770 | seed bib [1] | backward | R0001 | candidate | C1 | F1 | medium | ID confirmed R0003 call 12 (E0003) |
| P0040 | Generative modeling by estimating gradients of the data distribution | Song, Ermon | 2019 | NeurIPS 32 | arXiv:1907.05600 | seed bib [24] | backward | R0001 | candidate | C1 | F1 | low | score-based root (data-space); ID confirmed R0003 call 12 (E0003) |

| P0041 | Boltzmann generators — sampling equilibrium states of many-body systems with deep learning | Noe, Olsson et al. | 2019 | Science 365 eaaw1147 | arXiv:1812.01729 | arXiv API Q005 | query | R0002 | candidate | C1 | F1 | high | canonical flow+reweighting predecessor, not in seed bib |
| P0042 | Annealed Flow Transport Monte Carlo | Arbel, Matthews, Doucet | 2021 | ICML/NeurIPS-era (venue TBC) | arXiv:2102.07501 | arXiv API Q004 | query | R0002 | candidate | C1 | F1+F3 | high | SMC+flows with AIS weights |
| P0043 | Continual Repeated Annealed Flow Transport Monte Carlo (CRAFT) | Matthews, Arbel, Rezende (et al. TBC) | 2022 | ICML (TBC) | arXiv:2201.13117 | arXiv API Q003/Q004 | query | R0002 | candidate | C1 | F1+F3 | high |  |
| P0044 | Flow Annealed Importance Sampling Bootstrap (FAB) | Midgley, Stimper et al. | 2022 | ICLR 2023 (TBC) | arXiv:2208.01893 | arXiv API Q004 | query | R0002 | candidate | C1 | F1+F3 | high | AIS-driven flow training |
| P0045 | Trivializing maps, the Wilson flow and the HMC algorithm | Luescher | 2009 | Commun. Math. Phys. (TBC) | arXiv:0907.5491 | arXiv API Q008 | query | R0002 | candidate | C1 | F2+F3 | high | non-learned conceptual root of flow-based LFT sampling |
| P0046 | Efficient modelling of trivializing maps for lattice phi^4 theory using normalizing flows | Del Debbio, Marsh Rossney, Wilson | 2021 | Phys. Rev. D (TBC) | arXiv:2105.12481 | arXiv API Q008 | query | R0002 | candidate | C1 | F2 | high | scaling critique of flow-based sampling |
| P0047 | Machine learning trivializing maps: a first step towards understanding how flow-based samplers scale | Del Debbio, Marsh Rossney, Wilson | 2021 | PoS (TBC) | arXiv:2112.15532 | arXiv API Q008 | query | R0002 | candidate | C1 | F2 | medium |  |
| P0048 | Learning trivializing flows | Albandea, Del Debbio, Hernandez et al. | 2023 | arXiv/EPJC (TBC) | arXiv:2302.08408 | arXiv API Q008 | query | R0002 | candidate | C1 | F2 | medium |  |
| P0049 | Learning trivializing gradient flows for lattice gauge theories | Bacchio, Kessel, Schaefer | 2022 | Phys. Rev. D (TBC) | arXiv:2212.08469 | arXiv API Q008 | query | R0002 | candidate | C1 | F2 | medium |  |
| P0050 | Jarzynski's theorem for lattice gauge theory | Caselle, Costagliola, Nada et al. | 2016 | Phys. Rev. D (TBC) | arXiv:1604.05544 | arXiv API Q009 | query | R0002 | candidate | C1 | F3 | high | non-learned nonequilibrium predecessor of SNF-for-LFT line |
| P0051 | Applications of Jarzynski's relation in lattice gauge theories | Nada, Caselle, Costagliola et al. | 2016 | PoS (TBC) | arXiv:1610.09017 | arXiv API Q009 | query | R0002 | candidate | C1 | F3 | medium |  |
| P0052 | Introduction to normalizing flows for lattice field theory | Albergo, Boyda, Hackett et al. | 2021 | arXiv (lecture notes) | arXiv:2101.08176 | arXiv API Q001 | query | R0002 | candidate | C1 | F2 | high | field review/intro |
| P0053 | Flow-based sampling for lattice field theories (review) | Kanwar | 2024 | proceedings/review (TBC) | arXiv:2401.01297 | arXiv API Q002 | query | R0002 | candidate | C1 | F2 | medium |  |
| P0054 | Sampling using SU(N) gauge equivariant flows | Boyda, Kanwar, Racaniere et al. | 2020 | Phys. Rev. D 103 074504 | arXiv:2008.05456 | arXiv API Q002 + seed bib [9] | query+backward | R0002 | candidate | C1 | F2 | high | bib [9] had no printed arXiv ID; ID recovered by search (two-source metadata) |
| P0055 | Detecting and mitigating mode-collapse for flow-based sampling of lattice field theories | Nicoli, Anders, Hartung et al. | 2023 | Phys. Rev. D (TBC) | arXiv:2302.14082 | arXiv API Q001 | query | R0002 | candidate | C1 | F2+F3 | medium | failure-mode/diagnostics |
| P0056 | Mitigating topological freezing using out-of-equilibrium simulations | Bonanno, Nada, Vadacchino | 2024 | JHEP (TBC) | arXiv:2402.06561 | arXiv API Q009 | query | R0002 | candidate | C1 | F3 | medium | non-learned Jarzynski-based sampling |
| P0057 | Sampling SU(3) pure gauge theory with stochastic normalizing flows | Bulgarelli, Cellini, Nada | 2024 | arXiv (TBC) | arXiv:2409.18861 | arXiv API Q003/Q009 | query | R0002 | candidate | C1 | F2 | medium |  |
| P0058 | Scaling of stochastic normalizing flows in SU(3) lattice gauge theory | Bulgarelli, Cellini, Nada | 2024 | arXiv (TBC) | arXiv:2412.00200 | arXiv API Q003/Q009 | query | R0002 | candidate | C1 | F2 | low |  |
| P0059 | Diffusion models for lattice gauge field simulations | Zhu, Aarts, Wang et al. | 2024 | arXiv (TBC) | arXiv:2410.19602 | arXiv API Q007 | query | R0002 | candidate | C1 | F2 | medium | predecessor of P0020, same-author lineage |
| P0060 | Stochastic Normalizing Flows (Hodgkinson et al. — different paper from P0014) | Hodgkinson, van der Heide, Roosta | 2020 | arXiv (TBC) | arXiv:2002.09547 | arXiv API Q003 | query | R0002 | candidate | C1 | F1 | low | title collision with P0014 — identity note |
| P0061 | A neural network MCMC sampler that maximizes proposal entropy | Z. Li, Y. Chen et al. | 2020 | Entropy (TBC) | arXiv:2010.03587 | arXiv API Q006 | query | R0002 | candidate | C1 | F1 | low | learned-MCMC family |
| P0062 | Liouville Flow Importance Sampler | Tian, Panda et al. | 2024 | ICML (TBC) | arXiv:2405.06672 | arXiv API Q006 | query | R0002 | candidate | C1 | F1 | medium |  |
| P0063 | Adjoint Sampling: highly scalable diffusion samplers via adjoint matching | Havens, Miller et al. | 2025 | arXiv (TBC) | arXiv:2504.11713 | arXiv API Q006 | query | R0002 | candidate | C1 | F1 | medium | recent scalable diffusion-sampler line |
| P0064 | SCORENF: score-based normalizing flows for sampling unnormalized distributions | Kanaujia, Arora | 2025 | arXiv (TBC) | arXiv:2510.21330 | arXiv API Q001 | query | R0002 | candidate | C1 | F1+F2 | low |  |
| P0065 | Neural Non-Equilibrium Hamiltonian Monte Carlo for Corrected Boltzmann Sampling | M. Qian | 2026 | arXiv | arXiv:2607.15682 | arXiv API Q006 | query | R0002 | candidate | C1 | F1+F3 | high | same-author (Qian) follow-up to SPS; forward lineage |
| P0066 | NeuMC — a package for neural sampling for lattice field theories | Bialas, Korcyl, Stebel | 2025 | arXiv (TBC) | arXiv:2503.11482 | arXiv API Q001 | query | R0002 | candidate | C1 | F2 | low | tooling |

| P0067 | Diffusion models for sampling near criticality in lattice field theories | (authors TBC) | 2026 | arXiv | arXiv:2607.08505 | S2 citations of seed | forward | R0003 | candidate | C1 | F2 | high | cites seed; direct adjacent competitor |
| P0068 | Stochastic quantization as optimal control | (authors TBC) | 2026 | arXiv | arXiv:2607.21436 | S2 citations of seed | forward | R0003 | candidate | C1 | F1+F3 | high | cites seed; bridges SQ and control-based samplers |
| P0069 | Annealed importance sampling | R. Neal | 1998 | Statistics and Computing 11 (2001) | arXiv:physics/9803008 | S2 references of P0029 | backward | R0003 | candidate | C1 | F3 | high | canonical exactness-mechanism root |
| P0070 | Sequential Monte Carlo samplers | Del Moral, Doucet, Jasra | 2002/2006 | JRSS-B (TBC) | arXiv:cond-mat/0212648 | S2 references of P0029 | backward | R0003 | candidate | C1 | F3 | medium | SMC mechanism root |
| P0071 | A-NICE-MC: adversarial training for MCMC | Song, Zhao, Ermon (TBC) | 2017 | NeurIPS 2017 | arXiv:1706.07561 | S2 references of P0029 | backward | R0003 | candidate | C1 | F1 | medium | early learned-MCMC family |
| P0072 | NeuTra-lizing bad geometry in Hamiltonian Monte Carlo using neural transport | Hoffman et al. (TBC) | 2019 | arXiv | arXiv:1903.03704 | S2 references of P0029 | backward | R0003 | candidate | C1 | F1 | medium | flow-preconditioned HMC |
| P0073 | i-flow: high-dimensional integration and sampling with normalizing flows | Gao, Isaacson, Krause (TBC) | 2020 | Mach. Learn. Sci. Tech. | arXiv:2001.05486 | S2 references of P0029 | backward | R0003 | candidate | C1 | F1 | medium | NF importance sampling for HEP integrals |
| P0074 | Deep involutive generative models for neural MCMC | Spanbauer, Freer et al. (TBC) | 2020 | arXiv | arXiv:2006.15167 | S2 references of P0029 | backward | R0003 | candidate | C1 | F1 | low | learned-MCMC family |
| P0075 | Asymptotically unbiased estimation of physical observables with neural samplers | Nicoli, Nakajima, Strodthoff et al. | 2020 | Phys. Rev. E 101 023304 (per arXiv record) | arXiv:1910.13496 (confirmed R0006, E0016) | S2 references of P0029 + arXiv id_list | backward | R0003 | candidate | C1 (two-source) | F3 | high | key neural-importance-sampling mechanism paper; ERQ0002 resolved |
| P0076 | Generalizing Hamiltonian Monte Carlo with neural networks (L2HMC) | Levy, Hoffman, Sohl-Dickstein | 2017 | ICLR 2018 (TBC) | arXiv:1711.09268 | arXiv id_list gap-fill | manual hypothesis, verified | R0006 | candidate | C1 | F1 | high | founding learned-MCMC predecessor; hypothesis ID confirmed by title/author match |
| P0077 | Self-learning Monte Carlo method: a review | Pan, Chen et al. | 2025 | arXiv review | arXiv:2507.12554 | arXiv API Q_adv | query | R0006 | candidate | C1 | F1 | low | adjacent learned-update MCMC family (cond-mat lineage), review |

## Deduplication Notes

| Duplicate group | PaperIDs | Decision | Reason |
|---|---|---|---|
| DEDUP0001 | P0014 (seed bib [18], no printed ID) = arXiv 2002.06707 (Q003 hit, Wu/Koehler/Noe) | keep P0014, attach arXiv:2002.06707 | title+authors+year match across bib and arXiv search (two independent sources) |
| DEDUP0002 | P0054 (Q002 hit 2008.05456) = seed bib [9] Boyda et al. PRD 103 074504 | keep P0054 | title+authors+venue match; bib entry had no printed arXiv ID |
| DEDUP0003 | Q001/Q002/Q003/Q009 re-hits of P0003, P0005, P0006, P0007, P0015, P0016, P0017, P0018, P0020, P0022, P0023, P0024, P0034 | keep existing PaperIDs | same arXiv IDs as seed-bib candidates; search re-hit = independent second metadata source |
| DEDUP0004 | P0014 vs P0060 | separate papers | same title "Stochastic Normalizing Flows", different author teams (Wu/Koehler/Noe vs Hodgkinson et al.) and arXiv IDs |

## Promotion Rules

- Confirmed only after identifier + abstract/full-text evidence pass.
- Important-but-unverified stays unconfirmed (C0/C1) with explicit label.
- Out-of-scope/duplicate → excluded with reason.
