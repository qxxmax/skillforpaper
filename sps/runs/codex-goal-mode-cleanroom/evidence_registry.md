# Evidence Registry

- Core records: 31
- Evidence entries: 155
- Rule: each synthesis claim cites an EvidenceID, not only a paper name.

## 2606.13790 — Stochastic Path Sampler For Lattice Field Theory

- `E-260613790-M`: Learn paired forward and auxiliary backward Langevin paths by minimizing a path-space variational free energy / entropy-production upper bound. (PDF pp.4-8 Sec. 2)
- `E-260613790-R`: Corrected SPS observables agree with HMC in the tested 2D phi4 systems and show shorter autocorrelation near the pseudocritical region. (PDF pp.12-18 Sec. 3, Tables 1-4)
- `E-260613790-L`: Uncorrected tails and multimodal regions deviate; finite network capacity, terminal diffusion and support coverage remain practical limits, and the reported timing is hardware/setup specific. (PDF pp.12-13 Secs. 3.1-3.2; pp.19-21 discussion)

## 2111.15141 — Path Integral Sampler: a stochastic control approach for sampling

- `E-211115141-M`: Formulate sampling as a Schrodinger-bridge / stochastic optimal-control problem and learn a neural control for a reference diffusion. (PDF pp.4-8 method)
- `E-211115141-R`: The learned path sampler is competitive with the reported MCMC, SMC and normalizing-flow baselines on its benchmark suite. (PDF pp.9-18 experiments)
- `E-211115141-L`: Training overhead, time discretization and a suboptimal learned control can produce weight variance and residual bias if correction is omitted. (PDF pp.19-20 discussion)

## 2302.13834 — Denoising Diffusion Samplers

- `E-230213834-M`: Train a denoising diffusion sampler through a path-space objective and construct tractable forward/reverse trajectory densities. (PDF pp.4-8 method)
- `E-230213834-R`: The method performs strongly on the paper's multimodal and Bayesian benchmarks relative to selected diffusion and SMC baselines. (PDF pp.10-18 experiments)
- `E-230213834-L`: Optimization and diffusion discretization are sensitive, and the paper identifies smoothing/objective design as open improvements. (PDF final discussion, around pp.18-20)

## 2307.01050 — Transport meets Variational Inference: Controlled Monte Carlo Diffusions

- `E-230701050-M`: Jointly adapt forward and backward controlled diffusions using path-space divergences linked to transport and nonequilibrium identities. (PDF pp.3-8 method)
- `E-230701050-R`: Controlled Monte Carlo Diffusions improve the reported sampling metrics across the benchmark suite. (PDF pp.9-15 results)
- `E-230701050-L`: Performance still depends on annealing schedule, divergence choice, numerical SDE solution and learned-control quality. (PDF final discussion)

## 2410.02711 — NETS: A Non-Equilibrium Transport Sampler

- `E-241002711-M`: NETS augments nonequilibrium Langevin transport with a learned drift chosen to reduce estimator variance while retaining the nonequilibrium identity. (PDF pp.3-7 method)
- `E-241002711-R`: The learned transport improves effective sample size on the reported molecular and lattice phi4 examples. (PDF results section)
- `E-241002711-L`: Drift capacity, protocol, diffusion strength, training cost and remaining weight variance determine practical gains. (PDF final discussion)

## 2409.15937 — Numerical determination of the width and shape of the effective string using Stochastic Normalizing Flows

- `E-240915937-M`: Use stochastic normalizing flows that interleave invertible layers with stochastic nonequilibrium updates. (PDF method sections)
- `E-240915937-R`: The method reproduces Nambu-Goto benchmarks and is used to study string width, flux-tube shape and beyond-leading behavior. (PDF results and conclusion, around pp.15-20)
- `E-240915937-L`: This is an effective-string application, not a general scaling demonstration for realistic gauge theories; more complex models remain future work. (PDF p.20 conclusion)

## 2412.19109 — Stochastic normalizing flows for Effective String Theory

- `E-241219109-M`: Combine normalizing-flow transformations with stochastic updates along an interpolating protocol. (PDF pp.2-5 method)
- `E-241219109-R`: The proceedings contribution reports Binder and flux-profile observables consistent with reference expectations. (PDF results section)
- `E-241219109-L`: Proceedings-scale evidence and one application domain limit conclusions about general scalability. (PDF final section)

## 2210.03139 — Stochastic normalizing flows for lattice field theory

- `E-221003139-M`: Interleave normalizing-flow layers and Monte Carlo updates to form a stochastic normalizing flow for 2D phi4 theory. (PDF pp.2-5 method)
- `E-221003139-R`: The short study reports improved sampling efficiency over its purely learned or stochastic components. (PDF results section)
- `E-221003139-L`: The paper is a compact proceedings report in a low-dimensional scalar benchmark, so broad scaling claims are unsupported. (PDF final section)

## 2201.08862 — Stochastic normalizing flows as non-equilibrium transformations

- `E-220108862-M`: Unify invertible flow layers and stochastic nonequilibrium transitions within a path-probability/Jarzynski framework. (PDF pp.2-8 method)
- `E-220108862-R`: Hybrid stochastic normalizing flows improve free-energy estimation and sampling efficiency in the reported lattice examples. (PDF results sections)
- `E-220108862-L`: Efficiency trades off network training, protocol length, stochastic steps and residual work variance. (PDF pp.20-22 conclusions)

## 2502.05504 — Physics-Conditioned Diffusion Models for Lattice Gauge Theory

- `E-250205504-M`: Train a physics-conditioned diffusion model and use annealed Langevin / Metropolis-adjusted Langevin updates in 2D U(1). (PDF pp.3-8 method)
- `E-250205504-R`: The conditioned model transfers across couplings/lattice settings and improves topological exploration in the reported tests. (PDF results sections)
- `E-250205504-L`: Training-data topology can bias the model; non-Abelian groups, fermion nonlocality and large-volume cost remain open. (PDF pp.15-16 conclusion)

## 2311.03578 — Generative Diffusion Models for Lattice Field Theory

- `E-231103578-M`: Learn the reverse diffusion / score process in a toy model and 2D phi4 theory. (PDF pp.2-4 method)
- `E-231103578-R`: The model reproduces tested observables and can reduce chain autocorrelation when used as a global sampler. (PDF pp.3-5 results)
- `E-231103578-L`: The demonstrations are toy/2D, require training configurations, and leave data-free training, gauge fields, fermions and sign problems open. (PDF pp.5-6 conclusion)

## 2605.06134 — Diffusion model for SU(N) gauge theories

- `E-260506134-M`: Use implicit score matching with a gauge-equivariant U-Net and a predictor-corrector/Hamiltonian refinement. (PDF method sections)
- `E-260506134-R`: The paper demonstrates 2D and 4D SU(3)-family gauge sampling with improved observables after correction. (PDF results sections)
- `E-260506134-L`: Correction raises computational cost; large-volume/continuum efficiency and richer gauge dynamics remain unresolved. (PDF conclusion)

## 2211.01364 — An optimal control perspective on diffusion-based generative modeling

- `E-221101364-M`: Derive time-reversed diffusion samplers from Hamilton-Jacobi-Bellman control and path-space KL objectives. (PDF pp.3-8 theory)
- `E-221101364-R`: The method outperforms selected diffusion-sampler baselines on the paper's general benchmark suite. (PDF pp.8-12 experiments)
- `E-221101364-L`: It is not lattice-specific and leaves high-dimensional physics scaling and numerical-control error to future applications. (PDF p.12 discussion)

## 2605.11199 — Operator Spectroscopy of Trained Lattice Samplers

- `E-260511199-M`: Project learned score/force errors onto operator sectors such as zero modes, finite momentum modes and gauge-loop structures. (PDF method and diagnostic sections)
- `E-260511199-R`: Operator-resolved tests localize sampler error that aggregate loss or ESS can miss. (PDF pp.4-21 results)
- `E-260511199-L`: The operator basis and interpretation are model- and symmetry-dependent, and a detected failure still needs an algorithmic remedy. (PDF pp.21-22 discussion)

## 2106.05934 — Flow-based sampling for fermionic lattice field theories

- `E-210605934-M`: Construct joint, marginal and pseudofermion-conditioned flow models and test them in a 2D Yukawa system. (PDF theory/method sections)
- `E-210605934-R`: The proof of principle reproduces observables in a dynamical-fermion lattice example. (PDF results, around pp.8-20)
- `E-210605934-L`: The study does not establish realistic 4D QCD scaling; pseudofermion variance and determinant/nonlocal costs remain central. (PDF conclusion)

## 2211.07541 — Aspects of scaling and scalability for flow-based sampling of lattice QCD

- `E-221107541-M`: Decompose training, proposal and correction costs and analyze how architecture, transfer learning, stopping rules and protocols change scaling. (PDF pp.3-8 analysis)
- `E-221107541-R`: The paper shows that no single flow scaling law is meaningful; scalability must be assessed experimentally for each full algorithm. (PDF pp.1-8)
- `E-221107541-L`: Training cost can vary by orders of magnitude with protocol, and state-of-the-art QCD viability remains unproven. (PDF pp.7-10 limitations/discussion)

## 2409.18861 — Sampling SU(3) pure gauge theory with Stochastic Normalizing Flows

- `E-240918861-M`: Insert gauge-equivariant coupling layers into a non-equilibrium Monte Carlo protocol and train by dissipated-work/KL reduction. (PDF pp.2-6 method)
- `E-240918861-R`: SNF reaches similar KL/ESS with about half the protocol steps of NE-MCMC and inherits the tested volume scaling. (PDF pp.6-7, Figs. 2-3)
- `E-240918861-L`: Changing all links still implies n_step proportional to volume and becomes very expensive on fine lattices; protocol and architecture optimization remain open. (PDF pp.7-8 conclusion)

## 2510.21330 — SCORENF: Score-based Normalizing Flows for Sampling Unnormalized distributions

- `E-251021330-M`: Train an invertible normalizing flow with score-based and reverse-KL terms, then use it as an IMH proposal. (PDF pp.1-4 method)
- `E-251021330-R`: ScoreNF improves the reported NLL/RNLL balance, ESS and acceptance on Gaussian mixtures and a 64-dimensional phi4 example. (PDF pp.3-5 tables/results)
- `E-251021330-L`: It still relies on target samples for score estimation and is only tested on modest systems; larger symmetric systems are future work. (PDF p.5 conclusion)

## 2607.08505 — Diffusion Models for Sampling Near Criticality in Lattice Field Theories

- `E-260708505-M`: Use a fully convolutional reverse-SDE score model trained across volumes, plus score, MALA-acceptance and HMC-referenced ESS diagnostics. (PDF methods and Sec. V)
- `E-260708505-R`: Cross-volume models reproduce most 2D/3D phi4 observables and the propagator at unseen sizes, including L=64, with strongest residuals in infrared/zero-mode quantities. (PDF pp.20-21 summary)
- `E-260708505-L`: Results use scalar theories, support filters and 2000 score evaluations; zero-mode/action-density bias, transfer range, gauge equivariance and fermions remain open. (PDF pp.20-21 summary/outlook)

## 2604.10209 — Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality

- `E-260410209-M`: Factor the target coarse-to-fine; use conditional Gaussian mixtures and masked continuous normalizing flows while preserving coarse sites exactly. (PDF pp.4-7 method)
- `E-260410209-R`: On critical 2D phi4, the method reports much lower autocorrelation than HMC, high IS efficiency, consistent observables and MLMC variance reduction. (PDF pp.7-9 results/conclusion)
- `E-260410209-L`: ESS still falls at the largest volumes, fine-level quality limits MLMC gains, and extension to group-valued gauge theories is open. (PDF p.9 conclusion)

## 2512.19575 — Variational Autoregressive Networks Applied to phi4 Field Theory Systems

- `E-251219575-M`: Train variational autoregressive networks, add single-site/block MH corrections, and use transfer learning across coupling and size. (PDF pp.2-8 method)
- `E-251219575-R`: VAN+MH agrees with HMC on the tested Ising/phi4 systems and transfer learning reduces training epochs in the reported ranges. (PDF pp.16-17 conclusion)
- `E-251219575-L`: Only small lattices/parameter ranges are tested; gauge theories, larger finite-size scaling and other correction mechanisms remain open. (PDF p.17 conclusion)

## 2309.17082 — Diffusion models as stochastic quantization in lattice field theory

- `E-230917082-M`: Learn a reverse Langevin/score process from HMC data and deploy it as a global proposal in 2D phi4. (PDF pp.3-13 theory/method)
- `E-230917082-R`: The trained model reproduces tested configurations and reduces autocorrelation in symmetric and broken phases. (PDF pp.14-19 results)
- `E-230917082-L`: The study is a simple 2D demonstration and leaves data-free training, non-Abelian fields, fermions and complex actions unresolved. (PDF pp.19-20 conclusion)

## 1904.12072 — Flow-based generative models for Markov chain Monte Carlo in lattice field theory

- `E-190412072-M`: Train a normalizing flow without target samples and use independent flow proposals in a Metropolis-Hastings chain. (PDF pp.2-6 method)
- `E-190412072-R`: In 2D phi4, trained flow proposals reproduce observables and can eliminate sampling-stage critical slowing at fixed acceptance. (PDF results and pp.9-10 summary)
- `E-190412072-L`: Training took substantial GPU time in this proof of principle; architecture scaling, memory and extension to QCD were not established. (PDF pp.9-10 summary)

## 2003.06413 — Equivariant flow-based sampling for lattice gauge theory

- `E-200306413-M`: Construct gauge-equivariant normalizing-flow coupling layers and use them as independence-Metropolis proposals in 2D U(1). (PDF pp.2-4 method)
- `E-200306413-R`: For the tested beta=7, 16x16 setup, topological autocorrelation is far smaller than HMC/heat bath and the paper reports large efficiency gains for topological observables. (PDF pp.4-5 results)
- `E-200306413-L`: This is an Abelian 2D proof of principle; expressive invertible kernels for non-Abelian theories and full scaling remained future work. (PDF p.5 summary)

## 2107.00734 — Flow-based sampling for multimodal and extended-mode distributions in lattice field theory

- `E-210700734-M`: Develop topology matching, equivariant/mixture architectures, forward-KL/adaptive retraining and composite HMC+flow sampling. (PDF method sections)
- `E-210700734-R`: The tested methods alleviate mode collapse in real and complex scalar theories, while hybrid chains escape high-weight tails more reliably. (PDF pp.36-38 conclusion)
- `E-210700734-L`: Inner-tail mismodeling persists, metrics can be deceptive, and architecture/training must be specialized; comparative cost is application dependent. (PDF pp.37-38 conclusion)

## 2604.12416 — Machine learning for four-dimensional SU(3) lattice gauge theories

- `E-260412416-M`: Review normalizing/stochastic flows, diffusion processes and learned renormalization-group/fixed-point actions with physics constraints. (PDF pp.3-12 review)
- `E-260412416-R`: The review identifies physics-conditioned diffusion, stochastic nonequilibrium flows and learned fixed-point actions as promising directions with some 4D evidence. (PDF pp.12-14 summary)
- `E-260412416-L`: Most approaches remain exploratory; plain normalizing flows have not scaled simultaneously to 4D, large volume and fine spacing, and physics input appears essential. (PDF pp.13-14 conclusion)

## 2208.03832 — Sampling QCD field configurations with gauge-equivariant flow models

- `E-220803832-M`: Combine marginal gauge and conditional pseudofermion flow models for a 4D two-flavor QCD demonstration. (PDF pp.2-5 method)
- `E-220803832-R`: On a 4^4 lattice the reweighted flow ensemble is statistically consistent with HMC for plaquette, Polyakov loop, pion correlator and topology. (PDF pp.5-7 results)
- `E-220803832-L`: The lattice is tiny; model/training choices and scaling tradeoffs are largely unexplored, and at-scale use requires major engineering/HPC integration. (PDF pp.6-8 outlook)

## 2601.20708 — A scalable flow-based approach to mitigate topological freezing

- `E-260120708-M`: Train localized gauge-equivariant defect SNFs that interpolate OBC to PBC through nonequilibrium updates. (PDF pp.2-5 method)
- `E-260120708-R`: In tested 4D SU(3), defect SNF improves over NE-MCMC by about a factor of three at fixed estimator quality and reproduces topological susceptibility references. (PDF pp.4-6 results/conclusion)
- `E-260120708-L`: Richer layers, optimized schedules and dynamical fermions remain open; the factor is setup specific. (PDF p.6 outlook)

## 2510.26081 — Group-Equivariant Diffusion Models for Lattice Field Theory

- `E-251026081-M`: Use group-equivariant score networks with force-regularized score matching for 2D phi4 and U(1). (PDF pp.9-18 method)
- `E-251026081-R`: Symmetry-aware models outperform generic scores and reproduce tested observables with ESS reported between 15% and 65% in U(1) examples. (PDF pp.26-28 results/conclusion)
- `E-251026081-L`: ESS decreases with volume, sampling is computationally expensive, and higher dimensions, SU(3), fermions and integrator choices remain untested. (PDF pp.27-29 conclusion)

## 2306.00581 — Sampling U(1) gauge theory using a re-trainable conditional flow-based model

- `E-230600581-M`: Train a beta-conditioned normalizing flow on HMC ensembles, use MH, and retrain with intermediate model samples for farther extrapolation. (PDF pp.2-6 method)
- `E-230600581-R`: In 2D U(1), extrapolated proposals retain roughly 50-60% acceptance over the reported range and reduce topological freezing. (PDF pp.6-7 results)
- `E-230600581-L`: Acceptance falls with extrapolation distance and the authors state the conditional flow is generally not scalable to high-dimensional targets. (PDF p.7 conclusion)

## 2605.12597 — The critical slowing down in diffusion models

- `E-260512597-M`: Analyze score training and reverse generation exactly in the Gaussian O(n to infinity) model; compare one-layer, two-layer and local score architectures. (PDF pp.7-15 theory/results)
- `E-260512597-R`: A one-layer exact-form score learns with critical slowing and transmits it to generation; a two-layer/local architecture changes training scaling from quadratic to logarithmic in system size in the analyzed setting. (PDF pp.12-15, Secs. IV-VI)
- `E-260512597-L`: The result is controlled only in the Gaussian O(n to infinity) limit; deeper architectures add overhead and finite-n/non-equilibrium systems remain open. (PDF pp.15-16 conclusion)
