# Paper Reading Record

Record status: VERIFIED

## Identity Lock

| Field | Value | Evidence |
|---|---|---|
| Title | Denoising Diffusion Samplers | E-230213834-I |
| Authors | Francisco Vargas; Will Grathwohl; Arnaud Doucet | E-230213834-I |
| Version and date | v2; 2023-08-16 | E-230213834-I |
| arXiv / DOI | arXiv:2302.13834v2 | E-230213834-I |
| Canonical URL | https://arxiv.org/abs/2302.13834 | E-230213834-I |
| Local full text | temporary exact PDF; SHA-256 recorded in source_identity_ledger.csv; not redistributed | E-230213834-I |
| Pages | 30 | E-230213834-I |
| Reading level | C4 | E-230213834-I |

## Paper Map

| Region | Purpose in the argument | Anchor | EvidenceID |
|---|---|---|---|
| Introduction | Defines data-free diffusion sampling and its relation to AIS, SMC, and diffusion models. | PDF p. 1, Sec. 1 | E-230213834-P |
| Continuous formulation | Defines target noising, stationary OU reference, learned reverse process, path KL, and normalizer identity. | PDF pp. 2-4, Sec. 2 | E-230213834-M |
| Discretization | Constructs a reference-preserving integrator so the objective remains an ELBO. | PDF pp. 5-6, Sec. 3 | E-230213834-M |
| Method relations | Compares DDS with PIS, Schrodinger bridges, and path-integral control. | PDF pp. 6-8, Sec. 3.4 | E-230213834-M |
| Experiments | Compares DDS with PIS, SMC, and variational inference on multimodal and Bayesian targets. | PDF pp. 8-12, Sec. 4 | E-230213834-R |

## Problem and Position

| Role | Paper-layer statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | Learn a diffusion sampler for an unnormalized target without target-distributed training samples. | PDF p. 1, abstract and Sec. 1 | E-230213834-P |
| Existing baseline | PIS uses a pinned Brownian reference; SMC/AIS use manually chosen intermediate targets; DDPM score matching needs target data. | PDF pp. 1, 6-8, Secs. 1 and 3.4 | E-230213834-P |
| Gap | The PIS reference drift becomes steep near its pinned endpoint and can be numerically unstable. | PDF p. 7, Sec. 3.4; PDF pp. 13-14, Appendix A.2 | E-230213834-L |
| Contribution | DDS uses a stationary OU reference and learns its target-dependent time reversal by reverse path KL, with a discretization that preserves the reference marginal and ELBO. | PDF pp. 2-6, Secs. 2-3 | E-230213834-M |

## Mechanism

| Component or step | Definition / action | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| Conceptual noising process | OU dynamics carries the target toward an approximately Gaussian terminal marginal. | The integrated noise schedule is large enough for the Gaussian approximation. | PDF p. 2, Eq. (2) | E-230213834-M |
| Stationary reference | Starts the same OU process from its Gaussian invariant law. | The Gaussian reference is tractable. | PDF p. 3, Sec. 2.2, Eq. (4) | E-230213834-M |
| Learned reverse path | Simulates from the Gaussian reference with a neural correction $f_\theta$. | Target density is evaluable; the reverse process is differentiable through simulation. | PDF pp. 3-4, Eqs. (8)-(10) | E-230213834-M |
| Discrete sampler | Uses exact OU transitions plus a controlled shift and trains Algorithm 1. | The chosen discretization preserves the reference invariant marginal. | PDF pp. 5-6, Eqs. (17)-(20), Algorithm 1 | E-230213834-M |

## Equations

| Object | Exact formula or faithful notation | Symbol definitions | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Forward noising | $dx_t=-\beta_t x_tdt+\sigma\sqrt{2\beta_t}\,dB_t,\;x_0\sim\pi$ | $\pi$ is the target; $\beta_t$ is the schedule. | Defines the unavailable target-initialized process whose reversal is sought. | PDF p. 2, Eq. (2) | E-230213834-M |
| Learned reverse | $dy_t=-\beta_{T-t}[y_t-2\sigma^2f_\theta(T-t,y_t)]dt+\sigma\sqrt{2\beta_{T-t}}\,dW_t$ | $f_\theta$ approximates the target/reference log-density-ratio score. | Generates approximate target samples from a Gaussian. | PDF p. 3, Eq. (8) | E-230213834-M |
| Reverse path KL | $KL(Q_\theta\Vert P)=E_{Q_\theta}[\int_0^T\sigma^2\beta_{T-t}\|f_\theta\|^2dt+\log(N(y_T;0,\sigma^2I)/\pi(y_T))]$ | $P$ is target noising; $Q_\theta$ is learned reverse. | Training objective. | PDF p. 4, Eq. (10) | E-230213834-M |
| Normalizer weight | $\hat Z=\gamma(y_T)N(y_T;0,\sigma^2I)^{-1}(dP^{ref}/dQ_\theta)(y_{0:T})$ | $\gamma=Z\pi$. | Gives an unbiased importance estimate of $Z$. | PDF p. 4, Eq. (11) | E-230213834-M |

## Experiments and Numbers

| Test | Setup / baseline / metric | Retained result | Uncertainty or cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Standard targets | Ten-dimensional funnel and a 1600-dimensional log-Gaussian Cox process; compare PIS, SMC, and mean-field VI. | DDS is reported as competitive and more numerically stable than PIS. | Training time is non-negligible; simple targets can favor SMC after training cost. | PDF pp. 8-10, Sec. 4 and Figs. 2-3 | E-230213834-R; E-230213834-L |
| Multimodal flow target | A pretrained NICE flow supplies a high-dimensional target with known sampling access for evaluation. | The paper reports less mode collapse for DDS than PIS and SMC in that test. | This is one constructed benchmark, not a lattice criticality result. | PDF pp. 10-12, Sec. 4; Appendix C | E-230213834-R |
| Reference-process ablation | Compares OU-based DDS and pinned-Brownian PIS training behavior. | The PIS drift grows near the pinned endpoint; DDS is reported more stable. | Depends on the schedules and tuning used. | PDF p. 7, Fig. 1; PDF pp. 13-14, Appendix A.2 | E-230213834-L |

## Boundaries

| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | The score-approximation assumption behind the theoretical bound is less realistic for DDS because target noising samples are unavailable. | PDF p. 6, Sec. 3.3 | E-230213834-L |
| Author-stated | DDS has non-negligible training cost and SMC can be preferable on simple targets when cost is included. | PDF pp. 8-10, Sec. 4 | E-230213834-L |
| Reviewer inference | DDS returns approximate unweighted terminal samples and an importance estimator for $Z$; it does not present a trajectory IMH correction. | PDF pp. 4-6, Eqs. (11), (17)-(20) | inference |
| Unresolved | Whether OU reference dynamics remain advantageous for lattice targets near a phase transition is not tested. | PDF pp. 8-12, Sec. 4 | pending |

## Safe Output

| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | DDS already uses a data-free reverse path KL with tractable forward/reverse trajectory densities; its main change from PIS is the OU reference process and ELBO-preserving discretization. | E-230213834-M; E-230213834-L |
| Prohibited sentence | SPS introduced reverse path-KL training or tractable trajectory ratios. | DDS and PIS already contain those ingredients. |

## Search Leads

| Lead | Why it follows from this paper | Route | Status |
|---|---|---|---|
| Controlled Monte Carlo Diffusions, arXiv:2307.01050 | Extends the path-space view to jointly adapted annealed forward/backward dynamics. | forward / method extension | verified in run |
| SPS, arXiv:2606.13790 | Adds a lattice application and trajectory-level IMH correction. | forward / focal | verified in run |
| OU versus learned-diffusion ablation on lattice targets | Separates reference-process choice from architecture and correction. | gap closure | open |
