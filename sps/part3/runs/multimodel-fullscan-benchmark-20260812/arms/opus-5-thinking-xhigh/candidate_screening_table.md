# Candidate Screening Table

Every distinct record returned by a logged call appears here exactly once. Nothing is dropped silently: the tail is screened at title/abstract level and kept with its route and reason (reference 30 monitor tier).

- distinct records screened: **298** (arXiv-identified) + 1 INSPIRE record with no arXiv eprint (see notes)

- include: **112**  |  monitor: **30**  |  exclude: **156**

- facet tallies among includes: {'F2': 67, 'F3': 30, 'F1': 39, 'SEED': 1}


Facets: `F1` learned sampler for unnormalized targets; `F2` learned sampler for lattice field theory; `F3` correction / exactness mechanism; `SEED` the target paper.


Route codes: `bib`/`bib2` = seed-bibliography verification batches, `lex_lat` / `lex_ml` / `lex_exact` / `lex_diff` = arXiv lexical queries, `title1` / `title2` = arXiv title routes, `s2_batch` = Semantic Scholar cross-validation, `fwd_seed` / `fwd_nets` = forward-citation routes, `inspire1` / `inspire2` = INSPIRE-HEP.


## Include

| arXiv | title | route(s) found | #routes | facet / reason |
|---|---|---|---:|---|
| 0907.5491 | Trivializing maps, the Wilson flow and the HMC algorithm | bib2 + lex_lat + s2_batch | 3 | F2,F3 |
| 1102.1852 | Testing trivializing maps in the Hybrid Monte Carlo algorithm | lex_lat | 1 | F2 |
| 1105.2278 | Nonequilibrium candidate Monte Carlo: A new tool for efficient equilibrium simulation | title2 | 1 | F3 |
| 1610.09017 | Applications of Jarzynski's relation in lattice gauge theories | lex_exact | 1 | F3 |
| 1706.07561 | A-NICE-MC: Adversarial Training for MCMC | title2 | 1 | F1,F3 |
| 1810.12879 | Regressive and generative neural networks for scalar field theory | bib | 1 | F2 |
| 1811.03533 | Reducing Autocorrelation Times in Lattice Simulations with Generative Adversarial Networks | lex_lat | 1 | F2 |
| 1812.01729 | Boltzmann Generators -- Sampling Equilibrium States of Many-Body Systems with Deep Learning | bib2 + lex_ml + s2_batch | 3 | F1 |
| 1904.12072 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | bib + lex_diff + s2_batch | 3 | F2,F3 |
| 1910.13496 | Asymptotically unbiased estimation of physical observables with neural samplers | bib2 + lex_exact + lex_ml + s2_batch | 4 | F2,F3 |
| 2002.06707 | Stochastic Normalizing Flows | bib2 + s2_batch | 2 | F1,F3 |
| 2003.06413 | Equivariant flow-based sampling for lattice gauge theory | bib + inspire1 + s2_batch | 3 | F2 |
| 2005.04857 | Continuous-mixture Autoregressive Networks for efficient variational calculation of many-body systems | bib | 1 | F2 |
| 2007.07115 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | bib + lex_diff + s2_batch | 3 | F2,F3 |
| 2008.05456 | Sampling using $SU(N)$ gauge equivariant flows | title2 | 1 | F2 |
| 2101.08176 | Introduction to Normalizing Flows for Lattice Field Theory | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2102.07501 | Annealed Flow Transport Monte Carlo | bib2 + lex_exact + lex_ml + s2_batch | 4 | F1,F3 |
| 2105.12481 | Efficient Modelling of Trivializing Maps for Lattice $φ^4$ Theory Using Normalizing Flows: A First Look at Scalability | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2106.05934 | Flow-based sampling for fermionic lattice field theories | bib + s2_batch | 2 | F2 |
| 2107.00734 | Flow-based sampling for multimodal and extended-mode distributions in lattice field theory | bib + inspire1 + s2_batch | 3 | F2 |
| 2108.13444 | Calculation of the running coupling in non-Abelian gauge theories from Jarzynski's equality | lex_exact | 1 | F3 |
| 2110.02673 | Scaling Up Machine Learning For Quantum Field Theory with Equivariant Continuous Flows | bib + lex_lat | 2 | F2 |
| 2110.13216 | Adaptation of the Independent Metropolis-Hastings Sampler with Normalizing Flow Proposals | bib2 + lex_exact + s2_batch | 3 | F1,F3 |
| 2111.09266 | GFlowNet Foundations | title1 | 1 | F1 |
| 2111.15141 | Path Integral Sampler: a stochastic control approach for sampling | bib + s2_batch | 2 | F1 |
| 2112.15532 | Machine Learning Trivializing Maps: A First Step Towards Understanding How Flow-Based Samplers Scale Up | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2201.08862 | Stochastic normalizing flows as non-equilibrium transformations | bib + lex_exact + lex_lat + s2_batch | 4 | F2,F3 |
| 2201.13117 | Continual Repeated Annealed Flow Transport Monte Carlo | bib2 + lex_exact + lex_lat + lex_ml + s2_batch | 5 | F1,F3 |
| 2201.13259 | Trajectory balance: Improved credit assignment in GFlowNets | title1 | 1 | F1 |
| 2202.11712 | Flow-based sampling in the lattice Schwinger model at criticality | bib + s2_batch | 2 | F2 |
| 2207.00283 | Learning Lattice Quantum Field Theories with Equivariant Continuous Flows | bib | 1 | F2 |
| 2207.00980 | Conditional Normalizing flow for Monte Carlo sampling in lattice scalar field theory | inspire1 + lex_lat | 2 | F2 |
| 2208.01893 | Flow Annealed Importance Sampling Bootstrap | bib2 + lex_exact + s2_batch + title2 | 4 | F1,F3 |
| 2208.07698 | Score-Based Diffusion meets Annealed Importance Sampling | title2 | 1 | F1,F3 |
| 2208.08903 | GomalizingFlow.jl: A Julia package for Flow-based sampling algorithm for lattice field theory | bib2 + inspire1 | 2 | F2 |
| 2210.03139 | Stochastic normalizing flows for lattice field theory | bib + lex_exact + lex_lat + s2_batch | 4 | F2,F3 |
| 2211.01364 | An optimal control perspective on diffusion-based generative modeling | bib + lex_ml + s2_batch | 3 | F1 |
| 2211.03470 | Fourier-Flow model generating Feynman paths | bib | 1 | F2 |
| 2211.07541 | Aspects of scaling and scalability for flow-based sampling of lattice QCD | title2 | 1 | F2 |
| 2211.12806 | Learning trivializing flows | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2212.08469 | Learning Trivializing Gradient Flows for Lattice Gauge Theories | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2301.01504 | Generative models for scalar field theories: how to deal with poor scaling? | lex_diff | 1 | F2 |
| 2302.04763 | On Sampling with Approximate Transport Maps | lex_exact | 1 | F1,F3 |
| 2302.08408 | Learning Trivializing Flows | bib2 + lex_lat | 2 | F2 |
| 2302.13834 | Denoising Diffusion Samplers | bib + s2_batch | 2 | F1 |
| 2302.14082 | Detecting and Mitigating Mode-Collapse for Flow-based Sampling of Lattice Field Theories | bib2 + lex_lat + s2_batch + title2 | 4 | F2 |
| 2303.15136 | Exploring QCD matter in extreme conditions with Machine Learning | bib | 1 | F2 |
| 2305.02402 | Normalizing flows for lattice gauge theory in arbitrary space-time dimension | lex_lat | 1 | F2 |
| 2306.00581 | Sampling U(1) gauge theory using a re-trainable conditional flow-based model | inspire1 + lex_lat | 2 | F2 |
| 2307.01050 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | bib + s2_batch | 2 | F1,F3 |
| 2307.01198 | Improved sampling via learned diffusions | bib + s2_batch | 2 | F1 |
| 2309.15480 | Entanglement entropy from non-equilibrium lattice simulations | lex_exact | 1 | F3 |
| 2309.17082 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | bib + inspire2 + lex_diff + s2_batch | 4 | F2 |
| 2310.11979 | Out-of-equilibrium simulations to fight topological freezing | lex_exact | 1 | F3 |
| 2311.03578 | Generative Diffusion Models for Lattice Field Theory | bib2 + inspire2 + lex_diff | 3 | F2 |
| 2401.00828 | Multi-Lattice Sampling of Quantum Field Theories via Neural Operator-based Flows | lex_lat | 1 | F2 |
| 2401.01297 | Flow-based sampling for lattice field theories | title2 | 1 | F2 |
| 2402.05098 | Improved off-policy training of diffusion samplers | bib2 | 1 | F1 |
| 2402.06121 | Iterated Denoising Energy Matching for Sampling from Boltzmann Densities | title1 | 1 | F1 |
| 2402.06320 | Particle Denoising Diffusion Sampler | title1 | 1 | F1,F3 |
| 2402.06561 | Mitigating topological freezing using out-of-equilibrium simulations | lex_exact | 1 | F3 |
| 2404.10819 | Multiscale Normalizing Flows for Gauge Theories | lex_lat | 1 | F2 |
| 2405.06672 | Liouville Flow Importance Sampler | title1 | 1 | F1,F3 |
| 2408.16249 | Iterated Energy-based Flow Matching for Sampling from Boltzmann Densities | lex_ml | 1 | F1 |
| 2409.15937 | Numerical determination of the width and shape of the effective string using Stochastic Normalizing Flows | bib + lex_lat | 2 | F2 |
| 2409.18861 | Sampling SU(3) pure gauge theory with Stochastic Normalizing Flows | bib2 + lex_exact + lex_lat + s2_batch | 4 | F2,F3 |
| 2410.02711 | NETS: A Non-Equilibrium Transport Sampler | bib + lex_exact + s2_batch | 3 | F1,F3 |
| 2410.12456 | Training Neural Samplers with Reverse Diffusive KL Divergence | fwd_nets + lex_ml | 2 | F1 |
| 2410.13161 | Non-Perturbative Trivializing Flows for Lattice Gauge Theories | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2410.19602 | Diffusion models for lattice gauge field simulations | bib2 + inspire2 + lex_diff | 3 | F2 |
| 2411.11297 | Stochastic quantization and diffusion models | bib2 + inspire2 + lex_diff | 3 | F2 |
| 2412.00200 | Scaling of Stochastic Normalizing Flows in $\mathrm{SU}(3)$ lattice gauge theory | bib2 + fwd_nets + lex_exact + lex_lat + s2_batch | 5 | F2,F3 |
| 2412.01919 | Diffusion models learn distributions generated by complex Langevin dynamics | lex_diff | 1 | F2 |
| 2412.07081 | Sequential Controlled Langevin Diffusions | fwd_nets + title1 | 2 | F1,F3 |
| 2412.13704 | Diffusion models and stochastic quantisation in lattice field theory | lex_diff | 1 | F2 |
| 2412.19109 | Stochastic normalizing flows for Effective String Theory | bib + lex_lat | 2 | F2 |
| 2501.19077 | Temperature-Annealed Boltzmann Generators | lex_ml | 1 | F1 |
| 2502.00263 | Progress in Normalizing Flows for 4d Gauge Theories | lex_lat | 1 | F2 |
| 2502.02127 | Exploring Generative Networks for Manifolds with Non-Trivial Topology | bib | 1 | F2 |
| 2502.05504 | Physics-Conditioned Diffusion Models for Lattice Gauge Theory | bib + inspire2 + lex_diff + s2_batch | 4 | F2 |
| 2502.06685 | No Trick, No Treat: Pursuits and Challenges Towards Simulation-free Training of Neural Samplers | fwd_nets + lex_ml | 2 | F1 |
| 2502.10843 | LEAPS: A discrete neural sampler via locally equivariant networks | fwd_nets + lex_exact + lex_ml | 3 | F1 |
| 2502.18462 | Scalable Equilibrium Sampling with Sequential Boltzmann Generators | fwd_nets + lex_ml | 2 | F1 |
| 2503.01006 | Underdamped Diffusion Bridges with Applications to Sampling | lex_ml | 1 | F1 |
| 2503.11482 | NeuMC -- a package for neural sampling for lattice field theories | bib2 + lex_lat | 2 | F2 |
| 2504.11713 | Adjoint Sampling: Highly Scalable Diffusion Samplers via Adjoint Matching | fwd_nets + title1 | 2 | F1 |
| 2504.18126 | Lecture Notes on Normalizing Flows for Lattice Quantum Field Theories | bib2 + lex_lat + s2_batch | 3 | F2 |
| 2505.19552 | On scalable and efficient training of diffusion samplers | bib2 + fwd_nets | 2 | F1 |
| 2505.19646 | Energy-based generator matching: A neural sampler for general state space | fwd_nets + lex_ml | 2 | F1 |
| 2506.22565 | Adjoint Schrödinger Bridge Sampler | bib2 + fwd_nets | 2 | F1 |
| 2508.10684 | MDNS: Masked Diffusion Neural Sampler via Stochastic Optimal Control | fwd_nets + lex_ml | 2 | F1 |
| 2510.01328 | Combining complex Langevin dynamics with score-based and energy-based diffusion models | bib + lex_diff + s2_batch | 3 | F2 |
| 2510.21330 | SCORENF: Score-based Normalizing Flows for Sampling Unnormalized distributions | lex_diff + lex_exact + lex_lat | 3 | F2 |
| 2510.25704 | Scaling flow-based approaches for topology sampling in $\mathrm{SU}(3)$ gauge theory | fwd_nets + inspire1 + lex_lat | 3 | F2 |
| 2510.26081 | Group-Equivariant Diffusion Models for Lattice Field Theory | bib + lex_diff | 2 | F2 |
| 2512.19575 | Variational Autoregressive Networks Applied to $φ^4$ Field Theory Systems | bib | 1 | F2 |
| 2601.19552 | Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory | bib + inspire2 + lex_diff | 3 | F2 |
| 2601.20708 | A scalable flow-based approach to mitigate topological freezing | lex_lat | 1 | F2 |
| 2602.09045 | Diffusion Models for SU(2) Lattice Gauge Theory in Two Dimensions | bib + lex_diff | 2 | F2 |
| 2603.00530 | Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching | lex_ml | 1 | F1 |
| 2604.10209 | Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality | lex_lat | 1 | F2 |
| 2605.00229 | A unified perspective on fine-tuning and sampling with diffusion and flow models | fwd_nets + lex_ml | 2 | F1 |
| 2605.03984 | Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes | fwd_nets + lex_ml | 2 | F1 |
| 2605.06134 | Diffusion model for SU(N) gauge theories | bib + lex_diff | 2 | F2 |
| 2605.11199 | Operator Spectroscopy of Trained Lattice Samplers | bib + lex_lat | 2 | F2 |
| 2605.27064 | Flow-Based Global Proposals for Monte Carlo Sampling in SU(2) Lattice Gauge Theory | bib2 + inspire1 | 2 | F2,F3 |
| 2606.13790 | Stochastic Path Sampler For Lattice Field Theory | inspire2 + lex_exact + lex_lat + s2_batch | 4 | SEED |
| 2606.27481 | Sampling the Schwinger Model with Gauge-Equivariant Diffusion | lex_diff | 1 | F2 |
| 2607.08505 | Diffusion Models for Sampling Near Criticality in Lattice Field Theories | bib2 + fwd_seed + lex_diff | 3 | F2 |
| 2607.15682 | Neural Non-Equilibrium Hamiltonian Monte Carlo for Corrected Boltzmann Sampling | bib2 + fwd_nets + fwd_seed | 3 | F1,F2,F3 |
| 2607.21436 | Stochastic Quantization as Optimal Control | bib2 + fwd_seed + lex_diff | 3 | F2 |
| physics/9803008 | Annealed Importance Sampling | title2 | 1 | F1,F3 |

## Monitor

| arXiv | title | route(s) found | #routes | facet / reason |
|---|---|---|---:|---|
| 2012.10264 | Generative Neural Samplers for the Quantum Heisenberg Chain | lex_ml | 1 | generative neural samplers for the quantum Heisenberg chain |
| 2404.18323 | Flow-based Nonperturbative Simulation of First-order Phase Transitions | lex_lat | 1 | flow-based simulation of first-order phase transitions; physics application |
| 2406.14426 | Transferable Boltzmann Generators | lex_ml | 1 | transferable Boltzmann generators (molecular); adjacent application, not a predecessor |
| 2501.07371 | Simulating the Hubbard Model with Equivariant Normalizing Flows | lex_lat | 1 | equivariant flows for the Hubbard model; condensed-matter branch |
| 2502.04575 | Complexity Analysis of Normalizing Constant Estimation: from Jarzynski Equality to Annealed Importance Sampling and beyond | fwd_nets + lex_exact + title2 | 3 | complexity analysis Jarzynski to AIS; theory of the correction family |
| 2502.08696 | Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics | lex_exact | 1 | discrete diffusion samplers for combinatorial optimisation / stat-phys |
| 2505.19619 | SESaMo: Symmetry-Enforcing Stochastic Modulation for Normalizing Flows | lex_lat | 1 | SESaMo symmetry-enforcing stochastic modulation for flows |
| 2506.05231 | Progressive Tempering Sampler with Diffusion | fwd_nets + lex_ml | 2 | progressive tempering sampler; adjacent annealing family |
| 2506.17015 | Simulating Correlated Electrons with Symmetry-Enforced Normalizing Flows | lex_lat | 1 | symmetry-enforced flows for correlated electrons; condensed-matter branch |
| 2509.25486 | Scalable Boltzmann Generators for equilibrium sampling of large-scale materials | lex_ml | 1 | Boltzmann generators for materials; application branch |
| 2510.11711 | Reinforced sequential Monte Carlo for amortised sampling | fwd_nets + lex_exact | 2 | reinforced SMC for amortised sampling; adjacent correction family |
| 2510.18460 | Learning Boltzmann Generators via Constrained Mass Transport | fwd_nets + lex_ml | 2 | constrained mass transport for Boltzmann generators |
| 2511.15196 | Particle Monte Carlo methods for Lattice Field Theory | fwd_nets + lex_lat | 2 | particle Monte Carlo methods for LFT; adjacent MC family, unread |
| 2512.16607 | Boltzmann generators for amorphous particle systems | lex_ml | 1 | Boltzmann generators for amorphous systems; materials framing |
| 2601.10774 | Analytic Bijections for Smooth and Interpretable Normalizing Flows | lex_lat | 1 | analytic bijections for interpretable flows; architecture branch |
| 2601.18273 | Toward Scalable Normalizing Flows for the Hubbard Model | lex_lat | 1 | scalable flows for the Hubbard model; condensed-matter branch |
| 2601.21026 | Diffusion-based Annealed Boltzmann Generators : benefits, pitfalls and hopes | lex_ml | 1 | diffusion-based annealed Boltzmann generators; frontier, molecular framing |
| 2602.05961 | Discrete diffusion samplers and bridges: Off-policy algorithms and applications in latent spaces | fwd_nets | 1 | discrete diffusion samplers and bridges; 2026 frontier |
| 2602.08243 | Discrete Adjoint Schrödinger Bridge Sampler | fwd_nets | 1 | discrete adjoint Schrodinger bridge sampler; 2026 frontier |
| 2602.10637 | Coarse-Grained Boltzmann Generators | lex_ml | 1 | coarse-grained Boltzmann generators; molecular framing |
| 2602.12027 | General-purpose post-sampling reweighting method for multimodal target measures | fwd_nets | 1 | post-sampling reweighting for multimodal targets; correction-adjacent |
| 2602.21272 | Counterdiabatic Hamiltonian Monte Carlo | fwd_nets | 1 | counterdiabatic HMC; adjacent nonequilibrium MC |
| 2603.02984 | Variance reduction in lattice QCD observables via normalizing flows | lex_lat | 1 | variance reduction in lattice QCD via flows; observable-estimation branch |
| 2603.18205 | Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows | lex_lat | 1 | flows for the doped Hubbard sign problem; condensed-matter branch |
| 2604.20301 | Properties and limitations of geometric tempering for gradient flow dynamics | fwd_nets | 1 | limits of geometric tempering; negative-result candidate, unread |
| 2604.27738 | Sampling two-dimensional spin systems with transformers | lex_lat + lex_ml | 2 | transformer sampling of 2d spin systems; adjacent architecture |
| 2605.17808 | A Unified Framework for Data-Free One-Step Sampling via Wasserstein Gradient Flows | fwd_nets | 1 | data-free one-step sampling via Wasserstein gradient flows |
| 2605.31498 | Scalable Inference-Time Annealing with Surrogate Likelihood Estimators | fwd_nets | 1 | inference-time annealing with surrogate likelihoods; 2026 frontier |
| 2606.27361 | Autoregressive Boltzmann Generators | lex_ml | 1 | autoregressive Boltzmann generators; frontier, molecular framing |
| 2606.29110 | Few-Step Boltzmann Generators via Scalable Likelihood Flow Maps | lex_ml | 1 | few-step Boltzmann generators; 2026 frontier, application branch |

## Exclude (screened out)

| arXiv | title | route(s) found | #routes | facet / reason |
|---|---|---|---:|---|
| 0704.0464 | Annealed importance sampling of dileucine peptide | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 0704.0722 | Two- and three-point Green's functions in two-dimensional Landau-gauge Yang-Mills theory | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 0704.3877 | Relativistic diffusion equation from stochastic quantization | inspire2 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 0708.0779 | Real-time gauge theory simulations from stochastic quantization with optimized updating | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 0807.1597 | Stochastic quantization at finite chemical potential | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 0809.5227 | Stochastic quantization at nonzero chemical potential | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 0810.2089 | Can stochastic quantization evade the sign problem? -- the relativistic Bose gas at finite chemical potential | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 0810.2649 | Real-time gauge theory simulations from stochastic quantization using optimized updating | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 0811.1850 | Two complex problems on the lattice: transport coefficients and finite chemical potential | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 0902.4686 | Complex Langevin dynamics at finite chemical potential: mean field analysis in the relativistic Bose gas | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 0912.0617 | Adaptive stepsize and instabilities in complex Langevin dynamics | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1205.1925 | Hamiltonian Annealed Importance Sampling for partition function estimation | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 1207.5950 | Two infrared Yang-Mills solutions in stochastic quantization and in an effective action formalism | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1302.1622 | Thirring model at finite density in 0+1 dimensions with stochastic quantization: Crosscheck with an exact solution | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1302.2249 | Thirring model at finite density in 2+1 dimensions with stochastic quantization | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1402.6035 | Annealed Important Sampling for Models with Latent Variables | title2 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1606.00709 | f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1611.01722 | Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1705.06231 | Cooling Stochastic Quantization with colored noise | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1710.03247 | Particle Projection Using a Complex Langevin Method | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1710.04435 | The equation of state with non-equilibrium methods | lex_exact | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1710.10176 | Advances in non-relativistic matter via complex Langevin approaches | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1802.02840 | Neural Network Renormalization Group | title2 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1804.04569 | Stochastic quantization of a self-interacting nonminimal scalar field in semiclassical gravity | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1810.03545 | Stein Neural Sampler | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 1903.00804 | Machine Learning Holographic Mapping by Neural Network Renormalization Group | title2 | 1 | different computational paradigm; not a learned sampler for e^{-S} |
| 1903.03630 | Imputation estimators for unnormalized models with missing data | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1906.04904 | Learning Deep Generative Models with Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 1906.09471 | Universal Renormalons in Principal Chiral Models | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1907.10183 | Complex Langevin and other approaches to the sign problem in quantum many-body physics | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1908.04153 | Complex Langevin Simulations of Zero-dimensional Supersymmetric Quantum Field Theories | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 1910.06862 | Approximate Inference in Discrete Distributions with Monte Carlo Tree Search and Value Functions | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 1911.07337 | Stochastic Gradient Annealed Importance Sampling for Efficient Online Marginal Likelihood Estimation | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 1912.06073 | Normalizing Constant Estimation with Gaussianized Bridge Sampling | lex_exact | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2005.12719 | Exhaustive Neural Importance Sampling applied to Monte Carlo event generation | lex_exact | 1 | ML for collider/event-generation integrals, not configuration sampling of a lattice action |
| 2007.11926 | Efficient Evaluation of the Partition Function of RBMs with Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2012.07823 | Annealed Importance Sampling with q-Paths | lex_ml + title2 | 2 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2012.11198 | Spatial Monte Carlo Integration with Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2101.05755 | Normalizing Flows and the Real-Time Sign Problem | lex_lat | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 2107.04150 | MCMC Variational Inference via Uncorrected Hamiltonian Annealing | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2107.10211 | Differentiable Annealed Importance Sampling and the Perils of Gradient Noise | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2110.02787 | Relative Entropy Gradient Sampler for Unnormalized Distributions | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2111.11510 | Bootstrap Your Flow | lex_exact | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2112.01586 | HMC with Normalizing Flows | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2112.12194 | Surrogate Likelihoods for Variational Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2112.15035 | Normalizing flows for the real-time sign problem | lex_lat | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 2201.12001 | Complex Langevin simulations for $PT$-symmetric models | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 2204.03784 | Free Energy Evaluation Using Marginalized Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2205.08665 | Annealed importance sampling for Ising models with mixed boundary conditions | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2206.01934 | Stochastic Multiple Target Sampling Gradient Descent | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2209.13226 | Optimization of Annealed Importance Sampling Hyperparameters | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2210.10741 | A kernel Stein test of goodness of fit for sequential models | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2212.00832 | Applications of Lattice Gauge Equivariant Neural Networks | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2212.11387 | Use of Schwinger-Dyson equation in constructing an approximate trivializing map | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2304.01798 | Locality-constrained autoregressive cum conditional normalizing flow for lattice field theory simulations | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2305.19473 | Chain of Log-Concave Markov Chains | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2306.15283 | Adaptive Annealed Importance Sampling with Constant Rate Progress | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2307.01107 | Sampling the lattice Nambu-Goto string using Continuous Normalizing Flows | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2308.12355 | Renormalizing Diffusion Models | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2308.13294 | Training normalizing flows with computationally intensive target probability distributions | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2309.14983 | Sampling Nambu-Goto theory using Normalizing Flows | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2310.03381 | Learning Trivializing Flows in a $φ^4$ theory from coarser lattices | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2312.04800 | Decimation map in 2D for accelerating HMC | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2312.13110 | Pre-training of Molecular GNNs via Conditional Boltzmann Generator | lex_ml | 1 | molecular/materials generative modelling; outside the lattice-field-theory and generic-target scope |
| 2401.03892 | Sampling in Unit Time with Kernel Fisher-Rao Flow | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2401.04246 | Scalable Normalizing Flows Enable Boltzmann Generators for Macromolecules | lex_ml | 1 | molecular/materials generative modelling; outside the lattice-field-theory and generic-target scope |
| 2401.06860 | Trivializing Flow in 2D O(3) sigma model | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2401.09069 | Accelerating HEP simulations with Neural Importance Sampling | lex_exact | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2401.15645 | Ensemble-Based Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2403.01666 | Improving Adversarial Energy-Based Model via Diffusion Process | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2403.17149 | Symplectic Quantization: numerical results for the Feynman propagator on a 1+1 lattice and the theoretical relation with Quantum Field Theory | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| 2404.11229 | Mean field initialization of the Annealed Importance Sampling algorithm for an efficient evaluation of the Partition Function of Restricted Boltzmann Machines | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2405.14840 | Differentiable Annealed Importance Sampling Minimizes The Symmetrized Kullback-Leibler Divergence Between Initial and Target Distribution | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2406.12378 | Efficient mapping of phase diagrams with conditional Boltzmann Generators | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2406.13661 | Hitchhiker's guide on the relation of Energy-Based Models with other generative models, sampling and statistical physics: a comprehensive review | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2407.20444 | Importance Corrected Neural JKO Sampling | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2408.06710 | Variational Learning of Gaussian Process Latent Variable Models through Stochastic Gradient Annealed Importance Sampling | title2 | 1 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2409.09787 | BNEM: A Boltzmann Sampler Based on Bootstrapped Noised Energy Matching | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2409.17505 | Sequential Kernelized Stein Discrepancy | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2410.05163 | An Efficient On-Policy Deep Learning Framework for Stochastic Optimal Control | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2410.10390 | Stein Variational Evolution Strategies | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2410.21212 | On learning higher-order cumulants in diffusion models | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2411.16234 | Flow Annealed Importance Sampling Bootstrap meets Differentiable Particle Physics | lex_exact + title2 | 2 | AIS / partition-function-estimation variant without a learned path-space proposal |
| 2501.14260 | Stochastic quantization with discrete fictitious time | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2501.18288 | Normalizing flows for SU($N$) gauge theories employing singular value decomposition | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2502.00355 | Sampling in High-Dimensions using Stochastic Interpolants and Forward-Backward Stochastic Differential Equations | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2502.04468 | Iterative Importance Fine-tuning of Diffusion Models | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2502.06079 | Debiasing Guidance for Discrete Diffusion with Sequential Monte Carlo | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2502.07337 | Neural Flow Samplers with Shortcut Models | fwd_nets + lex_ml | 2 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2502.10328 | Accelerated Parallel Tempering via Neural Transports | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2503.02819 | Feynman-Kac Correctors in Diffusion: Annealing, Guidance, and Product of Experts | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2503.18929 | Trajectory Balance with Asynchrony: Decoupling Exploration and Learning for Fast, Scalable LLM Post-Training | title1 | 1 | GFlowNet/trajectory-balance applied to LLM or vision training, not sampling of an unnormalized physical target |
| 2504.08506 | Controlled stochastic processes for simulated annealing | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2504.11516 | FEAT: Free energy Estimators with Adaptive Transport | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2505.10553 | Flowing Through Hilbert Space: Quantum-Enhanced Generative Models for Lattice Field Theory | lex_diff + lex_lat | 2 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2505.13608 | Sampling NNLO QCD phase space with normalizing flows | lex_exact | 1 | ML for collider/event-generation integrals, not configuration sampling of a lattice action |
| 2505.19431 | Importance Weighted Score Matching for Diffusion Samplers with Enhanced Mode Coverage | fwd_nets + lex_ml | 2 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2506.01158 | Efficient Regression-Based Training of Normalizing Flows for Boltzmann Generators | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2506.01904 | Machine-Learned Sampling of Conditioned Path Measures | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2506.03979 | Solving Inverse Problems via Diffusion-Based Priors: An Approximation-Free Ensemble Sampling Approach | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2506.05668 | RNE: plug-and-play diffusion inference-time control and energy-based training | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2506.05905 | Sequential Monte Carlo approximations of Wasserstein-Fisher-Rao gradient flows | fwd_nets | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2506.16471 | Progressive Inference-Time Annealing of Diffusion Models for Sampling from Boltzmann Densities | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2506.17139 | Consistent Sampling and Simulation: Molecular Dynamics with Energy-Based Diffusion Models | fwd_nets | 1 | molecular/materials generative modelling; outside the lattice-field-theory and generic-target scope |
| 2506.18165 | Non-equilibrium Annealed Adjoint Sampler | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2507.00846 | BoltzNCE: Learning Likelihoods for Boltzmann Generation with Stochastic Interpolants and Noise Contrastive Estimation | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2508.12511 | Trust Region Constrained Measure Transport in Path Space for Stochastic Optimal Control and Inference | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2508.18175 | Amortized Sampling with Transferable Normalizing Flows | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2509.00316 | Continuously Tempered Diffusion Samplers | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2509.01632 | Relative Trajectory Balance is equivalent to Trust-PCL | title1 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2509.03726 | Energy-Weighted Flow Matching: Unlocking Continuous Normalizing Flows for Efficient and Scalable Boltzmann Sampling | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2509.21655 | DriftLite: Lightweight Drift Control for Inference-Time Scaling of Diffusion Models | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2509.26364 | Data-to-Energy Stochastic Dynamics | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2510.03824 | Proximal Diffusion Neural Sampler | fwd_nets + lex_ml | 2 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2510.07732 | Rotated Mean-Field Variational Inference and Iterative Gaussianization | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2510.07965 | Stick-Breaking Mixture Normalizing Flows with Component-Wise Tail Adaptation for Variational Inference | lex_ml | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2510.21542 | HollowFlow: Efficient Sample Likelihood Evaluation using Hollow Message Passing | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2510.23106 | Sampling from Energy distributions with Target Concrete Score Identity | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2510.26678 | Generative sampling with physics-informed kernels | fwd_nets | 1 | variational-inference or goodness-of-fit method, not a sampler with an exactness mechanism |
| 2511.00543 | Learning an Efficient Optimizer via Hybrid-Policy Sub-Trajectory Balance | title1 | 1 | GFlowNet/trajectory-balance applied to LLM or vision training, not sampling of an unnormalized physical target |
| 2512.05116 | Value Gradient Guidance for Flow Matching Alignment | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2512.21829 | Tilt Matching for Scalable Sampling and Fine-Tuning | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2512.22153 | Sampling with Shielded Langevin Monte Carlo Using Navigation Potentials | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2512.23930 | Assessing generative modeling approaches for free energy estimates in condensed matter | fwd_nets + lex_exact | 2 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2601.04983 | Assessing the Impact of Low Resolution Control Electronics on Quantum Neural Network Performance | inspire2 | 1 | different computational paradigm; not a learned sampler for e^{-S} |
| 2602.03729 | Efficient Training of Boltzmann Generators Using Off-Policy Log-Dispersion Regularization | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2602.04928 | Euphonium: Steering Video Flow Matching via Process Reward Gradient Guided Stochastic Dynamics | fwd_nets | 1 | GFlowNet/trajectory-balance applied to LLM or vision training, not sampling of an unnormalized physical target |
| 2602.06895 | MadSpace -- Event Generation for the Era of GPUs and ML | lex_exact | 1 | ML for collider/event-generation integrals, not configuration sampling of a lattice action |
| 2602.17827 | Avoid What You Know: Divergent Trajectory Balance for GFlowNets | title1 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2603.00252 | A Monte Carlo estimator of flow fields for sampling and noise problems | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2603.00454 | Rooted Absorbed Prefix Trajectory Balance with Submodular Replay for GFlowNet Training | title1 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2603.12501 | Normalizing-flow-based density of states for (1+1)D U(1) lattice gauge theory with a $θ$-term | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2604.05303 | Jeffreys Flow: Robust Boltzmann Generators for Rare Event Sampling via Parallel Tempering Distillation | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.00337 | Free Energy Surface Sampling via Reduced Flow Matching | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.00553 | Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance | title1 | 1 | GFlowNet/trajectory-balance applied to LLM or vision training, not sampling of an unnormalized physical target |
| 2605.04013 | Conditional Diffusion Sampling | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.13935 | Beyond Mode-Seeking RL: Trajectory-Balance Post-Training for Diffusion Language Models | title1 | 1 | GFlowNet/trajectory-balance applied to LLM or vision training, not sampling of an unnormalized physical target |
| 2605.15417 | $f$-Trajectory Balance: A Loss Family for Tuning GFlowNets, Generative Models, and LLMs with Off- and On-Policy Data | title1 | 1 | GFlowNet/trajectory-balance applied to LLM or vision training, not sampling of an unnormalized physical target |
| 2605.17326 | Noise scheduling and linear dynamics in diffusion models on Lie groups | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.17850 | Simple Approximation and Derivative Free Inference-Time Scaling for Diffusion Models via Sequential Monte Carlo on Path Measures | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.18745 | SURGE: Approximation and Training Free Particle Filter for Diffusion Surrogate | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.21722 | MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Well-Tempered Metadynamics | lex_ml | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.22444 | Normalizing flows for all-orders QED corrections in lattice field theory | lex_lat | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2605.23346 | Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2607.06841 | Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional Score-Based Sampling | fwd_nets | 1 | different computational paradigm; not a learned sampler for e^{-S} |
| 2607.19198 | ATLAS: A Foundation Neural Sampler for Amorphous Materials | lex_ml | 1 | molecular/materials generative modelling; outside the lattice-field-theory and generic-target scope |
| 2607.23591 | Neural Control Variates at LO and NLO | lex_exact | 1 | ML for collider/event-generation integrals, not configuration sampling of a lattice action |
| 2607.24393 | Stochastic Counterdiabatic Driving via Biorthogonal Liouvillian Eigenmodes | fwd_nets | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| 2607.25282 | Normalizing Flows to Reconstruct Pseudo-PDFs | lex_lat | 1 | ML for collider/event-generation integrals, not configuration sampling of a lattice action |
| cond-mat/9407100 | Diffusion processes and coherent states | inspire2 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| hep-lat/0508030 | Simulating nonequilibrium quantum fields with stochastic quantization techniques | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| hep-lat/0509134 | The Gluon Propagator in Lattice Landau Gauge with twisted boundary conditions | lex_diff | 1 | classical stochastic-quantization / complex-Langevin lattice physics; no learned sampler |
| hep-lat/9205008 | Dynamics of Langevin Simulation | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| hep-lat/9310012 | Momentum Lattice Simulation on a Small Lattice Using Stochastic Quantization | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| hep-th/0512010 | Nonequilibrium quantum fields from first principles | lex_diff | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |
| hep-th/9310109 | Minimum uncertainty and squeezing in diffusion processes and stochastic quantization | inspire2 | 1 | title-level screen: outside the three facets (learned sampler for unnormalized targets / for LFT / correction mechanism) |

## Records Without An arXiv Identifier

| record | source | label | reason |
|---|---|---|---|
| "Sampling in lattice field theory with flow-based generative models" (Marsh Rossney, 2025-07-17) | INSPIRE-HEP literature record, no arXiv eprint field | monitor (C1, single-channel) | grey literature (thesis-type record); identity not cross-validated in a second channel, so it is not used as claim evidence |
