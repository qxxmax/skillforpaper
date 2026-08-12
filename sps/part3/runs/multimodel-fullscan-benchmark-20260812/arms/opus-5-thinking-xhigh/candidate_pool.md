# Candidate Pool

All candidates from every logged call. Nothing is deleted; records move between
`confirmed`, `unconfirmed`, `candidate`, and `excluded` with a reason.

`PaperID` here is the arXiv identifier, which is also the deduplication key.

- distinct arXiv-identified candidates: **298**
- status: candidate 51, confirmed 61, excluded 156, unconfirmed 30
- verification: C1 47, C2 242, C4 9

Verification levels are *derived from logged calls*, not asserted: `C2` means the
arXiv API returned title/authors/date/abstract for that identifier in a saved response;
`C1` means only Semantic Scholar or INSPIRE returned it (metadata only, abstract not
fetched); `C4` means the PDF is in `sources/pdfs/` and a specific mechanism sentence was
located in its extracted text. No record was promoted on the strength of model memory.

| PaperID (arXiv) | Title | Verification | Status | Channels confirming identity | Facet | Notes |
|---|---|---|---|---|---|---|
| 0704.0464 | Annealed importance sampling of dileucine peptide | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0704.0722 | Two- and three-point Green's functions in two-dimensional Landau-gauge Yang-Mills theory | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0704.3877 | Relativistic diffusion equation from stochastic quantization | C1 | excluded | INSPIRE-HEP | - | screened out at title level; see candidate_screening_table.md |
| 0708.0779 | Real-time gauge theory simulations from stochastic quantization with optimized updating | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0807.1597 | Stochastic quantization at finite chemical potential | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0809.5227 | Stochastic quantization at nonzero chemical potential | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0810.2089 | Can stochastic quantization evade the sign problem? -- the relativistic Bose gas at finite chemical potential | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0810.2649 | Real-time gauge theory simulations from stochastic quantization using optimized updating | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0811.1850 | Two complex problems on the lattice: transport coefficients and finite chemical potential | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0902.4686 | Complex Langevin dynamics at finite chemical potential: mean field analysis in the relativistic Bose gas | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 0907.5491 | Trivializing maps, the Wilson flow and the HMC algorithm | C2 | confirmed | Crossref, Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 0912.0617 | Adaptive stepsize and instabilities in complex Langevin dynamics | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1102.1852 | Testing trivializing maps in the Hybrid Monte Carlo algorithm | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 1105.2278 | Nonequilibrium candidate Monte Carlo: A new tool for efficient equilibrium simulation | C2 | candidate | arXiv API | F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 1205.1925 | Hamiltonian Annealed Importance Sampling for partition function estimation | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1207.5950 | Two infrared Yang-Mills solutions in stochastic quantization and in an effective action formalism | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1302.1622 | Thirring model at finite density in 0+1 dimensions with stochastic quantization: Crosscheck with an exact solution | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1302.2249 | Thirring model at finite density in 2+1 dimensions with stochastic quantization | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1402.6035 | Annealed Important Sampling for Models with Latent Variables | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1606.00709 | f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1610.09017 | Applications of Jarzynski's relation in lattice gauge theories | C2 | candidate | arXiv API | F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 1611.01722 | Learning to Draw Samples: With Application to Amortized MLE for Generative Adversarial Learning | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1705.06231 | Cooling Stochastic Quantization with colored noise | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1706.07561 | A-NICE-MC: Adversarial Training for MCMC | C2 | candidate | arXiv API | F1,F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 1710.03247 | Particle Projection Using a Complex Langevin Method | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1710.04435 | The equation of state with non-equilibrium methods | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1710.10176 | Advances in non-relativistic matter via complex Langevin approaches | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1802.02840 | Neural Network Renormalization Group | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1804.04569 | Stochastic quantization of a self-interacting nonminimal scalar field in semiclassical gravity | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1810.03545 | Stein Neural Sampler | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1810.12879 | Regressive and generative neural networks for scalar field theory | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 1811.03533 | Reducing Autocorrelation Times in Lattice Simulations with Generative Adversarial Networks | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 1812.01729 | Boltzmann Generators -- Sampling Equilibrium States of Many-Body Systems with Deep Learning | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 1903.00804 | Machine Learning Holographic Mapping by Neural Network Renormalization Group | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1903.03630 | Imputation estimators for unnormalized models with missing data | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1904.12072 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | C4 | confirmed | Crossref, Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 1906.04904 | Learning Deep Generative Models with Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1906.09471 | Universal Renormalons in Principal Chiral Models | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1907.10183 | Complex Langevin and other approaches to the sign problem in quantum many-body physics | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1908.04153 | Complex Langevin Simulations of Zero-dimensional Supersymmetric Quantum Field Theories | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1910.06862 | Approximate Inference in Discrete Distributions with Monte Carlo Tree Search and Value Functions | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1910.13496 | Asymptotically unbiased estimation of physical observables with neural samplers | C2 | confirmed | Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 1911.07337 | Stochastic Gradient Annealed Importance Sampling for Efficient Online Marginal Likelihood Estimation | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 1912.06073 | Normalizing Constant Estimation with Gaussianized Bridge Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2002.06707 | Stochastic Normalizing Flows | C4 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2003.06413 | Equivariant flow-based sampling for lattice gauge theory | C2 | confirmed | Crossref, INSPIRE-HEP, Semantic Scholar, arXiv API | F2 | core landscape record |
| 2005.04857 | Continuous-mixture Autoregressive Networks for efficient variational calculation of many-body systems | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2005.12719 | Exhaustive Neural Importance Sampling applied to Monte Carlo event generation | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2007.07115 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | C2 | confirmed | Crossref, Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 2007.11926 | Efficient Evaluation of the Partition Function of RBMs with Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2008.05456 | Sampling using $SU(N)$ gauge equivariant flows | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2012.07823 | Annealed Importance Sampling with q-Paths | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2012.10264 | Generative Neural Samplers for the Quantum Heisenberg Chain | C2 | unconfirmed | arXiv API | monitor | generative neural samplers for the quantum Heisenberg chain |
| 2012.11198 | Spatial Monte Carlo Integration with Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2101.05755 | Normalizing Flows and the Real-Time Sign Problem | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2101.08176 | Introduction to Normalizing Flows for Lattice Field Theory | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2102.07501 | Annealed Flow Transport Monte Carlo | C2 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2105.12481 | Efficient Modelling of Trivializing Maps for Lattice $φ^4$ Theory Using Normalizing Flows: A First Look at Scalability | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2106.05934 | Flow-based sampling for fermionic lattice field theories | C2 | confirmed | Crossref, Semantic Scholar, arXiv API | F2 | core landscape record |
| 2107.00734 | Flow-based sampling for multimodal and extended-mode distributions in lattice field theory | C2 | confirmed | INSPIRE-HEP, Semantic Scholar, arXiv API | F2 | core landscape record |
| 2107.04150 | MCMC Variational Inference via Uncorrected Hamiltonian Annealing | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2107.10211 | Differentiable Annealed Importance Sampling and the Perils of Gradient Noise | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2108.13444 | Calculation of the running coupling in non-Abelian gauge theories from Jarzynski's equality | C2 | candidate | arXiv API | F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2110.02673 | Scaling Up Machine Learning For Quantum Field Theory with Equivariant Continuous Flows | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2110.02787 | Relative Entropy Gradient Sampler for Unnormalized Distributions | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2110.13216 | Adaptation of the Independent Metropolis-Hastings Sampler with Normalizing Flow Proposals | C2 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2111.09266 | GFlowNet Foundations | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2111.11510 | Bootstrap Your Flow | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2111.15141 | Path Integral Sampler: a stochastic control approach for sampling | C4 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2112.01586 | HMC with Normalizing Flows | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2112.12194 | Surrogate Likelihoods for Variational Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2112.15035 | Normalizing flows for the real-time sign problem | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2112.15532 | Machine Learning Trivializing Maps: A First Step Towards Understanding How Flow-Based Samplers Scale Up | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2201.08862 | Stochastic normalizing flows as non-equilibrium transformations | C4 | confirmed | Crossref, Semantic Scholar, Springer publisher page, arXiv API | F2,F3 | core landscape record |
| 2201.12001 | Complex Langevin simulations for $PT$-symmetric models | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2201.13117 | Continual Repeated Annealed Flow Transport Monte Carlo | C2 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2201.13259 | Trajectory balance: Improved credit assignment in GFlowNets | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2202.11712 | Flow-based sampling in the lattice Schwinger model at criticality | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2204.03784 | Free Energy Evaluation Using Marginalized Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2205.08665 | Annealed importance sampling for Ising models with mixed boundary conditions | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2206.01934 | Stochastic Multiple Target Sampling Gradient Descent | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2207.00283 | Learning Lattice Quantum Field Theories with Equivariant Continuous Flows | C2 | confirmed | Crossref, arXiv API | F2 | core landscape record |
| 2207.00980 | Conditional Normalizing flow for Monte Carlo sampling in lattice scalar field theory | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2208.01893 | Flow Annealed Importance Sampling Bootstrap | C2 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2208.07698 | Score-Based Diffusion meets Annealed Importance Sampling | C2 | candidate | arXiv API | F1,F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2208.08903 | GomalizingFlow.jl: A Julia package for Flow-based sampling algorithm for lattice field theory | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2209.13226 | Optimization of Annealed Importance Sampling Hyperparameters | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2210.03139 | Stochastic normalizing flows for lattice field theory | C2 | confirmed | Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 2210.10741 | A kernel Stein test of goodness of fit for sequential models | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2211.01364 | An optimal control perspective on diffusion-based generative modeling | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2211.03470 | Fourier-Flow model generating Feynman paths | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2211.07541 | Aspects of scaling and scalability for flow-based sampling of lattice QCD | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2211.12806 | Learning trivializing flows | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2212.00832 | Applications of Lattice Gauge Equivariant Neural Networks | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2212.08469 | Learning Trivializing Gradient Flows for Lattice Gauge Theories | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2212.11387 | Use of Schwinger-Dyson equation in constructing an approximate trivializing map | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2301.01504 | Generative models for scalar field theories: how to deal with poor scaling? | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2302.04763 | On Sampling with Approximate Transport Maps | C2 | candidate | arXiv API | F1,F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2302.08408 | Learning Trivializing Flows | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2302.13834 | Denoising Diffusion Samplers | C4 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2302.14082 | Detecting and Mitigating Mode-Collapse for Flow-based Sampling of Lattice Field Theories | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2303.15136 | Exploring QCD matter in extreme conditions with Machine Learning | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2304.01798 | Locality-constrained autoregressive cum conditional normalizing flow for lattice field theory simulations | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2305.02402 | Normalizing flows for lattice gauge theory in arbitrary space-time dimension | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2305.19473 | Chain of Log-Concave Markov Chains | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2306.00581 | Sampling U(1) gauge theory using a re-trainable conditional flow-based model | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2306.15283 | Adaptive Annealed Importance Sampling with Constant Rate Progress | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2307.01050 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | C4 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2307.01107 | Sampling the lattice Nambu-Goto string using Continuous Normalizing Flows | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2307.01198 | Improved sampling via learned diffusions | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2308.12355 | Renormalizing Diffusion Models | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2308.13294 | Training normalizing flows with computationally intensive target probability distributions | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2309.14983 | Sampling Nambu-Goto theory using Normalizing Flows | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2309.15480 | Entanglement entropy from non-equilibrium lattice simulations | C2 | candidate | arXiv API | F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2309.17082 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | C4 | confirmed | Crossref, INSPIRE-HEP, Semantic Scholar, arXiv API | F2 | core landscape record |
| 2310.03381 | Learning Trivializing Flows in a $φ^4$ theory from coarser lattices | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2310.11979 | Out-of-equilibrium simulations to fight topological freezing | C2 | candidate | arXiv API | F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2311.03578 | Generative Diffusion Models for Lattice Field Theory | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2312.04800 | Decimation map in 2D for accelerating HMC | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2312.13110 | Pre-training of Molecular GNNs via Conditional Boltzmann Generator | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2401.00828 | Multi-Lattice Sampling of Quantum Field Theories via Neural Operator-based Flows | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2401.01297 | Flow-based sampling for lattice field theories | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2401.03892 | Sampling in Unit Time with Kernel Fisher-Rao Flow | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2401.04246 | Scalable Normalizing Flows Enable Boltzmann Generators for Macromolecules | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2401.06860 | Trivializing Flow in 2D O(3) sigma model | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2401.09069 | Accelerating HEP simulations with Neural Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2401.15645 | Ensemble-Based Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2402.05098 | Improved off-policy training of diffusion samplers | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2402.06121 | Iterated Denoising Energy Matching for Sampling from Boltzmann Densities | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2402.06320 | Particle Denoising Diffusion Sampler | C2 | candidate | arXiv API | F1,F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2402.06561 | Mitigating topological freezing using out-of-equilibrium simulations | C2 | candidate | arXiv API | F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2403.01666 | Improving Adversarial Energy-Based Model via Diffusion Process | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2403.17149 | Symplectic Quantization: numerical results for the Feynman propagator on a 1+1 lattice and the theoretical relation with Quantum Field Theory | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2404.10819 | Multiscale Normalizing Flows for Gauge Theories | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2404.11229 | Mean field initialization of the Annealed Importance Sampling algorithm for an efficient evaluation of the Partition Function of Restricted Boltzmann Machines | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2404.18323 | Flow-based Nonperturbative Simulation of First-order Phase Transitions | C2 | unconfirmed | arXiv API | monitor | flow-based simulation of first-order phase transitions; physics applic |
| 2405.06672 | Liouville Flow Importance Sampler | C2 | candidate | arXiv API | F1,F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2405.14840 | Differentiable Annealed Importance Sampling Minimizes The Symmetrized Kullback-Leibler Divergence Between Initial and Target Distribution | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2406.12378 | Efficient mapping of phase diagrams with conditional Boltzmann Generators | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2406.13661 | Hitchhiker's guide on the relation of Energy-Based Models with other generative models, sampling and statistical physics: a comprehensive review | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2406.14426 | Transferable Boltzmann Generators | C2 | unconfirmed | arXiv API | monitor | transferable Boltzmann generators (molecular); adjacent application, n |
| 2407.20444 | Importance Corrected Neural JKO Sampling | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2408.06710 | Variational Learning of Gaussian Process Latent Variable Models through Stochastic Gradient Annealed Importance Sampling | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2408.16249 | Iterated Energy-based Flow Matching for Sampling from Boltzmann Densities | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2409.09787 | BNEM: A Boltzmann Sampler Based on Bootstrapped Noised Energy Matching | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2409.15937 | Numerical determination of the width and shape of the effective string using Stochastic Normalizing Flows | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2409.17505 | Sequential Kernelized Stein Discrepancy | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2409.18861 | Sampling SU(3) pure gauge theory with Stochastic Normalizing Flows | C2 | confirmed | Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 2410.02711 | NETS: A Non-Equilibrium Transport Sampler | C4 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2410.05163 | An Efficient On-Policy Deep Learning Framework for Stochastic Optimal Control | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2410.10390 | Stein Variational Evolution Strategies | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2410.12456 | Training Neural Samplers with Reverse Diffusive KL Divergence | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2410.13161 | Non-Perturbative Trivializing Flows for Lattice Gauge Theories | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2410.19602 | Diffusion models for lattice gauge field simulations | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2410.21212 | On learning higher-order cumulants in diffusion models | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2411.11297 | Stochastic quantization and diffusion models | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2411.16234 | Flow Annealed Importance Sampling Bootstrap meets Differentiable Particle Physics | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2412.00200 | Scaling of Stochastic Normalizing Flows in $\mathrm{SU}(3)$ lattice gauge theory | C2 | confirmed | Semantic Scholar, arXiv API | F2,F3 | core landscape record |
| 2412.01919 | Diffusion models learn distributions generated by complex Langevin dynamics | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2412.07081 | Sequential Controlled Langevin Diffusions | C2 | confirmed | Semantic Scholar, arXiv API | F1,F3 | core landscape record |
| 2412.13704 | Diffusion models and stochastic quantisation in lattice field theory | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2412.19109 | Stochastic normalizing flows for Effective String Theory | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2501.07371 | Simulating the Hubbard Model with Equivariant Normalizing Flows | C2 | unconfirmed | arXiv API | monitor | equivariant flows for the Hubbard model; condensed-matter branch |
| 2501.14260 | Stochastic quantization with discrete fictitious time | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2501.18288 | Normalizing flows for SU($N$) gauge theories employing singular value decomposition | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2501.19077 | Temperature-Annealed Boltzmann Generators | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2502.00263 | Progress in Normalizing Flows for 4d Gauge Theories | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2502.00355 | Sampling in High-Dimensions using Stochastic Interpolants and Forward-Backward Stochastic Differential Equations | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2502.02127 | Exploring Generative Networks for Manifolds with Non-Trivial Topology | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2502.04468 | Iterative Importance Fine-tuning of Diffusion Models | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2502.04575 | Complexity Analysis of Normalizing Constant Estimation: from Jarzynski Equality to Annealed Importance Sampling and beyond | C2 | unconfirmed | Semantic Scholar, arXiv API | monitor | complexity analysis Jarzynski to AIS; theory of the correction family |
| 2502.05504 | Physics-Conditioned Diffusion Models for Lattice Gauge Theory | C2 | confirmed | INSPIRE-HEP, Semantic Scholar, arXiv API | F2 | core landscape record |
| 2502.06079 | Debiasing Guidance for Discrete Diffusion with Sequential Monte Carlo | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2502.06685 | No Trick, No Treat: Pursuits and Challenges Towards Simulation-free Training of Neural Samplers | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2502.07337 | Neural Flow Samplers with Shortcut Models | C2 | excluded | Semantic Scholar, arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2502.08696 | Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics | C2 | unconfirmed | arXiv API | monitor | discrete diffusion samplers for combinatorial optimisation / stat-phys |
| 2502.10328 | Accelerated Parallel Tempering via Neural Transports | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2502.10843 | LEAPS: A discrete neural sampler via locally equivariant networks | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2502.18462 | Scalable Equilibrium Sampling with Sequential Boltzmann Generators | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2503.01006 | Underdamped Diffusion Bridges with Applications to Sampling | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2503.02819 | Feynman-Kac Correctors in Diffusion: Annealing, Guidance, and Product of Experts | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2503.11482 | NeuMC -- a package for neural sampling for lattice field theories | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2503.18929 | Trajectory Balance with Asynchrony: Decoupling Exploration and Learning for Fast, Scalable LLM Post-Training | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2504.08506 | Controlled stochastic processes for simulated annealing | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2504.11516 | FEAT: Free energy Estimators with Adaptive Transport | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2504.11713 | Adjoint Sampling: Highly Scalable Diffusion Samplers via Adjoint Matching | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2504.18126 | Lecture Notes on Normalizing Flows for Lattice Quantum Field Theories | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2505.10553 | Flowing Through Hilbert Space: Quantum-Enhanced Generative Models for Lattice Field Theory | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2505.13608 | Sampling NNLO QCD phase space with normalizing flows | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2505.19431 | Importance Weighted Score Matching for Diffusion Samplers with Enhanced Mode Coverage | C2 | excluded | Semantic Scholar, arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2505.19552 | On scalable and efficient training of diffusion samplers | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2505.19619 | SESaMo: Symmetry-Enforcing Stochastic Modulation for Normalizing Flows | C2 | unconfirmed | arXiv API | monitor | SESaMo symmetry-enforcing stochastic modulation for flows |
| 2505.19646 | Energy-based generator matching: A neural sampler for general state space | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2506.01158 | Efficient Regression-Based Training of Normalizing Flows for Boltzmann Generators | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2506.01904 | Machine-Learned Sampling of Conditioned Path Measures | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.03979 | Solving Inverse Problems via Diffusion-Based Priors: An Approximation-Free Ensemble Sampling Approach | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.05231 | Progressive Tempering Sampler with Diffusion | C2 | unconfirmed | Semantic Scholar, arXiv API | monitor | progressive tempering sampler; adjacent annealing family |
| 2506.05668 | RNE: plug-and-play diffusion inference-time control and energy-based training | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.05905 | Sequential Monte Carlo approximations of Wasserstein-Fisher-Rao gradient flows | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.16471 | Progressive Inference-Time Annealing of Diffusion Models for Sampling from Boltzmann Densities | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.17015 | Simulating Correlated Electrons with Symmetry-Enforced Normalizing Flows | C2 | unconfirmed | arXiv API | monitor | symmetry-enforced flows for correlated electrons; condensed-matter bra |
| 2506.17139 | Consistent Sampling and Simulation: Molecular Dynamics with Energy-Based Diffusion Models | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.18165 | Non-equilibrium Annealed Adjoint Sampler | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2506.22565 | Adjoint Schrödinger Bridge Sampler | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2507.00846 | BoltzNCE: Learning Likelihoods for Boltzmann Generation with Stochastic Interpolants and Noise Contrastive Estimation | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2508.10684 | MDNS: Masked Diffusion Neural Sampler via Stochastic Optimal Control | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2508.12511 | Trust Region Constrained Measure Transport in Path Space for Stochastic Optimal Control and Inference | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2508.18175 | Amortized Sampling with Transferable Normalizing Flows | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2509.00316 | Continuously Tempered Diffusion Samplers | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2509.01632 | Relative Trajectory Balance is equivalent to Trust-PCL | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2509.03726 | Energy-Weighted Flow Matching: Unlocking Continuous Normalizing Flows for Efficient and Scalable Boltzmann Sampling | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2509.21655 | DriftLite: Lightweight Drift Control for Inference-Time Scaling of Diffusion Models | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2509.25486 | Scalable Boltzmann Generators for equilibrium sampling of large-scale materials | C2 | unconfirmed | arXiv API | monitor | Boltzmann generators for materials; application branch |
| 2509.26364 | Data-to-Energy Stochastic Dynamics | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2510.01328 | Combining complex Langevin dynamics with score-based and energy-based diffusion models | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2510.03824 | Proximal Diffusion Neural Sampler | C2 | excluded | Semantic Scholar, arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2510.07732 | Rotated Mean-Field Variational Inference and Iterative Gaussianization | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2510.07965 | Stick-Breaking Mixture Normalizing Flows with Component-Wise Tail Adaptation for Variational Inference | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2510.11711 | Reinforced sequential Monte Carlo for amortised sampling | C2 | unconfirmed | Semantic Scholar, arXiv API | monitor | reinforced SMC for amortised sampling; adjacent correction family |
| 2510.18460 | Learning Boltzmann Generators via Constrained Mass Transport | C2 | unconfirmed | Semantic Scholar, arXiv API | monitor | constrained mass transport for Boltzmann generators |
| 2510.21330 | SCORENF: Score-based Normalizing Flows for Sampling Unnormalized distributions | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2510.21542 | HollowFlow: Efficient Sample Likelihood Evaluation using Hollow Message Passing | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2510.23106 | Sampling from Energy distributions with Target Concrete Score Identity | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2510.25704 | Scaling flow-based approaches for topology sampling in $\mathrm{SU}(3)$ gauge theory | C2 | confirmed | INSPIRE-HEP, Semantic Scholar, arXiv API | F2 | core landscape record |
| 2510.26081 | Group-Equivariant Diffusion Models for Lattice Field Theory | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2510.26678 | Generative sampling with physics-informed kernels | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2511.00543 | Learning an Efficient Optimizer via Hybrid-Policy Sub-Trajectory Balance | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2511.15196 | Particle Monte Carlo methods for Lattice Field Theory | C2 | unconfirmed | Semantic Scholar, arXiv API | monitor | particle Monte Carlo methods for LFT; adjacent MC family, unread |
| 2512.05116 | Value Gradient Guidance for Flow Matching Alignment | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2512.16607 | Boltzmann generators for amorphous particle systems | C2 | unconfirmed | arXiv API | monitor | Boltzmann generators for amorphous systems; materials framing |
| 2512.19575 | Variational Autoregressive Networks Applied to $φ^4$ Field Theory Systems | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2512.21829 | Tilt Matching for Scalable Sampling and Fine-Tuning | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2512.22153 | Sampling with Shielded Langevin Monte Carlo Using Navigation Potentials | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2512.23930 | Assessing generative modeling approaches for free energy estimates in condensed matter | C2 | excluded | Semantic Scholar, arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2601.04983 | Assessing the Impact of Low Resolution Control Electronics on Quantum Neural Network Performance | C1 | excluded | INSPIRE-HEP | - | screened out at title level; see candidate_screening_table.md |
| 2601.10774 | Analytic Bijections for Smooth and Interpretable Normalizing Flows | C2 | unconfirmed | arXiv API | monitor | analytic bijections for interpretable flows; architecture branch |
| 2601.18273 | Toward Scalable Normalizing Flows for the Hubbard Model | C2 | unconfirmed | arXiv API | monitor | scalable flows for the Hubbard model; condensed-matter branch |
| 2601.19552 | Generalizable Equivariant Diffusion Models for Non-Abelian Lattice Gauge Theory | C2 | confirmed | INSPIRE-HEP, arXiv API | F2 | core landscape record |
| 2601.20708 | A scalable flow-based approach to mitigate topological freezing | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2601.21026 | Diffusion-based Annealed Boltzmann Generators : benefits, pitfalls and hopes | C2 | unconfirmed | arXiv API | monitor | diffusion-based annealed Boltzmann generators; frontier, molecular fra |
| 2602.03729 | Efficient Training of Boltzmann Generators Using Off-Policy Log-Dispersion Regularization | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2602.04928 | Euphonium: Steering Video Flow Matching via Process Reward Gradient Guided Stochastic Dynamics | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2602.05961 | Discrete diffusion samplers and bridges: Off-policy algorithms and applications in latent spaces | C1 | unconfirmed | Semantic Scholar | monitor | discrete diffusion samplers and bridges; 2026 frontier |
| 2602.06895 | MadSpace -- Event Generation for the Era of GPUs and ML | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2602.08243 | Discrete Adjoint Schrödinger Bridge Sampler | C1 | unconfirmed | Semantic Scholar | monitor | discrete adjoint Schrodinger bridge sampler; 2026 frontier |
| 2602.09045 | Diffusion Models for SU(2) Lattice Gauge Theory in Two Dimensions | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2602.10637 | Coarse-Grained Boltzmann Generators | C2 | unconfirmed | arXiv API | monitor | coarse-grained Boltzmann generators; molecular framing |
| 2602.12027 | General-purpose post-sampling reweighting method for multimodal target measures | C1 | unconfirmed | Semantic Scholar | monitor | post-sampling reweighting for multimodal targets; correction-adjacent |
| 2602.17827 | Avoid What You Know: Divergent Trajectory Balance for GFlowNets | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2602.21272 | Counterdiabatic Hamiltonian Monte Carlo | C1 | unconfirmed | Semantic Scholar | monitor | counterdiabatic HMC; adjacent nonequilibrium MC |
| 2603.00252 | A Monte Carlo estimator of flow fields for sampling and noise problems | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2603.00454 | Rooted Absorbed Prefix Trajectory Balance with Submodular Replay for GFlowNet Training | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2603.00530 | Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching | C2 | candidate | arXiv API | F1 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2603.02984 | Variance reduction in lattice QCD observables via normalizing flows | C2 | unconfirmed | arXiv API | monitor | variance reduction in lattice QCD via flows; observable-estimation bra |
| 2603.12501 | Normalizing-flow-based density of states for (1+1)D U(1) lattice gauge theory with a $θ$-term | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2603.18205 | Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows | C2 | unconfirmed | arXiv API | monitor | flows for the doped Hubbard sign problem; condensed-matter branch |
| 2604.05303 | Jeffreys Flow: Robust Boltzmann Generators for Rare Event Sampling via Parallel Tempering Distillation | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2604.10209 | Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2604.20301 | Properties and limitations of geometric tempering for gradient flow dynamics | C1 | unconfirmed | Semantic Scholar | monitor | limits of geometric tempering; negative-result candidate, unread |
| 2604.27738 | Sampling two-dimensional spin systems with transformers | C2 | unconfirmed | arXiv API | monitor | transformer sampling of 2d spin systems; adjacent architecture |
| 2605.00229 | A unified perspective on fine-tuning and sampling with diffusion and flow models | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2605.00337 | Free Energy Surface Sampling via Reduced Flow Matching | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2605.00553 | Stable-GFlowNet: Toward Diverse and Robust LLM Red-Teaming via Contrastive Trajectory Balance | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2605.03984 | Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes | C2 | confirmed | Semantic Scholar, arXiv API | F1 | core landscape record |
| 2605.04013 | Conditional Diffusion Sampling | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2605.06134 | Diffusion model for SU(N) gauge theories | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2605.11199 | Operator Spectroscopy of Trained Lattice Samplers | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2605.13935 | Beyond Mode-Seeking RL: Trajectory-Balance Post-Training for Diffusion Language Models | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2605.15417 | $f$-Trajectory Balance: A Loss Family for Tuning GFlowNets, Generative Models, and LLMs with Off- and On-Policy Data | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2605.17326 | Noise scheduling and linear dynamics in diffusion models on Lie groups | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2605.17808 | A Unified Framework for Data-Free One-Step Sampling via Wasserstein Gradient Flows | C1 | unconfirmed | Semantic Scholar | monitor | data-free one-step sampling via Wasserstein gradient flows |
| 2605.17850 | Simple Approximation and Derivative Free Inference-Time Scaling for Diffusion Models via Sequential Monte Carlo on Path Measures | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2605.18745 | SURGE: Approximation and Training Free Particle Filter for Diffusion Surrogate | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2605.21722 | MetaDNS: Enhancing Exploration in Discrete Neural Samplers via Well-Tempered Metadynamics | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2605.22444 | Normalizing flows for all-orders QED corrections in lattice field theory | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2605.23346 | Contrastive Distribution Matching for Amortized Sequential Monte Carlo in Discrete Diffusion | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2605.27064 | Flow-Based Global Proposals for Monte Carlo Sampling in SU(2) Lattice Gauge Theory | C2 | confirmed | INSPIRE-HEP, arXiv API | F2,F3 | core landscape record |
| 2605.31498 | Scalable Inference-Time Annealing with Surrogate Likelihood Estimators | C1 | unconfirmed | Semantic Scholar | monitor | inference-time annealing with surrogate likelihoods; 2026 frontier |
| 2606.13790 | Stochastic Path Sampler For Lattice Field Theory | C4 | confirmed | INSPIRE-HEP, Semantic Scholar, arXiv API | SEED | core landscape record |
| 2606.27361 | Autoregressive Boltzmann Generators | C2 | unconfirmed | arXiv API | monitor | autoregressive Boltzmann generators; frontier, molecular framing |
| 2606.27481 | Sampling the Schwinger Model with Gauge-Equivariant Diffusion | C2 | candidate | arXiv API | F2 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |
| 2606.29110 | Few-Step Boltzmann Generators via Scalable Likelihood Flow Maps | C2 | unconfirmed | arXiv API | monitor | few-step Boltzmann generators; 2026 frontier, application branch |
| 2607.06841 | Tensor Train Diffusion: Leveraging Low-Rank Structures for High-Dimensional Score-Based Sampling | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2607.08505 | Diffusion Models for Sampling Near Criticality in Lattice Field Theories | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2607.15682 | Neural Non-Equilibrium Hamiltonian Monte Carlo for Corrected Boltzmann Sampling | C2 | confirmed | Semantic Scholar, arXiv API | F1,F2,F3 | core landscape record |
| 2607.19198 | ATLAS: A Foundation Neural Sampler for Amorphous Materials | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2607.21436 | Stochastic Quantization as Optimal Control | C2 | confirmed | Semantic Scholar, arXiv API | F2 | core landscape record |
| 2607.23591 | Neural Control Variates at LO and NLO | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| 2607.24393 | Stochastic Counterdiabatic Driving via Biorthogonal Liouvillian Eigenmodes | C1 | excluded | Semantic Scholar | - | screened out at title level; see candidate_screening_table.md |
| 2607.25282 | Normalizing Flows to Reconstruct Pseudo-PDFs | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| cond-mat/9407100 | Diffusion processes and coherent states | C1 | excluded | INSPIRE-HEP | - | screened out at title level; see candidate_screening_table.md |
| hep-lat/0508030 | Simulating nonequilibrium quantum fields with stochastic quantization techniques | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| hep-lat/0509134 | The Gluon Propagator in Lattice Landau Gauge with twisted boundary conditions | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| hep-lat/9205008 | Dynamics of Langevin Simulation | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| hep-lat/9310012 | Momentum Lattice Simulation on a Small Lattice Using Stochastic Quantization | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| hep-th/0512010 | Nonequilibrium quantum fields from first principles | C2 | excluded | arXiv API | - | screened out at title level; see candidate_screening_table.md |
| hep-th/9310109 | Minimum uncertainty and squeezing in diffusion processes and stochastic quantization | C1 | excluded | INSPIRE-HEP | - | screened out at title level; see candidate_screening_table.md |
| physics/9803008 | Annealed Importance Sampling | C2 | candidate | arXiv API | F1,F3 | single-channel identity; NOT usable as strong claim evidence until a second channel confirms |

## Records Without An arXiv Identifier

| record | source channel | status | verification | note |
|---|---|---|---|---|
| "Sampling in lattice field theory with flow-based generative models" (Marsh Rossney, 2025-07-17) | INSPIRE-HEP | unconfirmed | C1 (metadata only, single channel) | grey-literature/thesis-type record surfaced by the INSPIRE route; no arXiv eprint in the record, identity not cross-validated, not used as claim evidence |

## Deduplication Notes

| Duplicate group | PaperIDs | Decision | Reason |
|---|---|---|---|
| DEDUP0001 | 2211.12806, 2302.08408 | keep both, flagged as a probable version pair | Both are titled "Learning trivializing flows" by Albandea et al. with overlapping author lists; arXiv returns them as two distinct eprints (2022-11 and 2023-02) and Semantic Scholar resolved 2211.12806 twice in the batch response. Treated as one method contribution in the literature matrix, two records in the pool. Not merged, because the version relationship was not verified against a publisher record. |
| DEDUP0002 | 452 raw records -> 298 distinct | dedup by arXiv identifier (version suffix stripped) | 83 records were returned by two or more independent routes; that overlap is the route-redundancy evidence used in the coverage report. |

## Promotion Rules Applied

- `confirmed` requires the identity to appear in at least two independent channels
  (arXiv API, Semantic Scholar, INSPIRE-HEP, Crossref, publisher page).
- `candidate` = relevant but single-channel; explicitly not usable as strong claim evidence.
- `unconfirmed` = monitor tier: real record, outside the current three facets, retained
  because a change of thesis could pull it in.
- `excluded` = screened out at title level with a recorded reason.
