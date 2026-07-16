# Paper Reading Record

Record status: `VERIFIED`

## Identity Lock

| Field | Value | Evidence |
|---|---|---|
| Title | Path Integral Sampler: a stochastic control approach for sampling | E-211115141-I |
| Authors | Qinsheng Zhang; Yongxin Chen | E-211115141-I |
| Version and date | v2; 2022-03-10 | E-211115141-I |
| arXiv / DOI | arXiv:2111.15141v2 | E-211115141-I |
| Canonical URL | https://arxiv.org/abs/2111.15141 | E-211115141-I |
| Local full text | temporary exact PDF; SHA-256 recorded in source_identity_ledger.csv; not redistributed | E-211115141-I |
| Pages | 26 | E-211115141-I |
| Reading level | C4 | E-211115141-I |

## Paper Map

| Region | Purpose in the argument | Anchor | EvidenceID |
|---|---|---|---|
| Introduction | Positions finite-horizon controlled diffusion against MCMC, SMC, and explicit variational densities. | PDF pp. 1-2, Sec. 1 | E-211115141-P |
| Control formulation | Defines the controlled SDE, Schrodinger bridge, path KL, and trainable control objective. | PDF pp. 3-5, Secs. 2-3.3 | E-211115141-M |
| Calibration | Derives trajectory importance weights, ESS, and normalization estimators. | PDF p. 6, Sec. 3.4, Eqs. (17)-(19) | E-211115141-M |
| Experiments | Tests Bayesian inference, normalization, multimodal targets, molecules, and image posteriors. | PDF pp. 6-9, Sec. 4, Tables 1-3 | E-211115141-R |
| Conclusion | States training, policy-quality, and hyperparameter limits. | PDF p. 9, Sec. 5 | E-211115141-L |

## Problem and Position

| Role | Paper-layer statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | Draw from an unnormalized target in finite time without relying on a long-mixing Markov chain. | PDF pp. 1-3, Secs. 1-2.1 | E-211115141-P |
| Existing baseline | MCMC can mix slowly; SMC needs annealing and resampling choices; explicit variational densities constrain architecture. | PDF pp. 1-2, Sec. 1 | E-211115141-P |
| Gap | A learned stochastic path needs both a trainable quality objective and a correction when the learned control or time discretization is imperfect. | PDF pp. 2, 5-6, Secs. 1 and 3.3-3.4 | E-211115141-L |
| Contribution | PIS casts sampling as Schrodinger-bridge stochastic control, trains one forward control by a path cost, and calibrates outputs with trajectory importance weights. | PDF pp. 3-6, Sec. 3 | E-211115141-M |

## Mechanism

| Component or step | Definition / action | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| Controlled path | Evolves $dx_t=u_tdt+dw_t$ from an easy initial state. | The target log density is evaluable up to a constant. | PDF p. 3, Eq. (2) | E-211115141-M |
| Target-conditioned path | Chooses terminal cost $\Psi=\log(\mu^0/\mu)$, making the optimal path end in $\mu$. | The stated Schrodinger-bridge conditions hold. | PDF p. 4, Eqs. (9)-(13) | E-211115141-M |
| Training | Minimizes expected control energy plus terminal density ratio with a neural control. | Optimization and SDE differentiation are stable enough for the chosen discretization. | PDF pp. 4-5, Eq. (14), Algorithm 1 | E-211115141-M |
| Calibration | Reweights each full trajectory by $dQ^*/dQ^u$. | The proposal path measure covers the target path measure. | PDF p. 6, Eq. (17), Algorithm 2 | E-211115141-M |

## Equations

| Object | Exact formula or faithful notation | Symbol definitions | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Endpoint KL bound | $D_{KL}(\mu_Q\Vert\mu)\leq D_{KL}(Q\Vert P)$ | $Q,P$ are proposal and target path measures; $\mu_Q,\mu$ their terminal marginals. | Makes path KL a sampler-quality objective. | PDF p. 3, Eq. (1) | E-211115141-M |
| Path-control identity | $D_{KL}(Q^u\Vert Q^*)=E_{Q^u}[\int_0^T\frac12\|u_t\|^2dt+\log(\mu^0(x_T)/\mu(x_T))]$ | $Q^*$ is the optimal target-conditioned path. | Defines the training loss. | PDF p. 4, Eq. (13) | E-211115141-M |
| Importance weight | $w^u(\tau)=\exp[-\int_0^T\frac12\|u_t\|^2dt-u_t^\top dw_t-\Psi(x_T)]$ | $w^u=dQ^*/dQ^u$. | Corrects suboptimal control and time discretization in weighted estimates. | PDF p. 6, Eq. (17) | E-211115141-M |
| Normalizer identity | $Z=E_{Q^u}[\exp(-\hat S^u(\tau))]$ | $\hat S^u$ is the unnormalized path cost. | Gives an unbiased estimator of $Z$. | PDF p. 6, Eq. (19) | E-211115141-M |

## Experiments and Numbers

| Test | Setup / baseline / metric | Retained result | Uncertainty or cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Bayesian and normalization benchmarks | HMC, NUTS, SMC, annealed flow transport, variational normalizing flow, and PIS variants. | The reported PIS variants are competitive on the paper's benchmark suite. | Comparisons are task- and tuning-specific. | PDF pp. 6-9, Sec. 4, Tables 1-3 | E-211115141-R |
| MNIST posterior normalizers | One hundred image-conditioned posterior targets; long SMC runs supply the reference. | Table 3 reports lower combined bias/standard-deviation score for PISRW-Grad than the listed alternatives. | The reference itself is an empirical long-run SMC estimate. | PDF p. 9, Table 3 | E-211115141-R |
| Finite-step quality | Policy approximation error and time step enter the Wasserstein bound. | The paper gives $W_2=O(\sqrt{Td(\Delta t+\epsilon)})$ under its stated conditions. | This is a conditional bound, not a measured universal rate. | PDF pp. 5, 14, Eq. (16) and Theorem 5 | E-211115141-L |

## Boundaries

| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | Unweighted endpoint samples are not guaranteed unbiased when the learned control is suboptimal or the SDE is discretized. | PDF pp. 5-6, Secs. 3.3-3.4 | E-211115141-L |
| Author-stated | PIS requires target-specific network training; poor hyperparameters can cause numerical failure. | PDF p. 9, Sec. 5 | E-211115141-L |
| Reviewer inference | The paper's correction is importance weighting, not a trajectory-level Metropolis accept/reject chain. | PDF p. 6, Eq. (17), Algorithm 2 | inference |
| Unresolved | How weight variance scales for lattice field targets near criticality is not tested here. | PDF pp. 6-9, Sec. 4 | pending |

## Safe Output

| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | PIS already trains a data-free controlled stochastic path with a path-space objective and uses full-trajectory importance weights to correct finite-control and discretization error. | E-211115141-M; E-211115141-L |
| Prohibited sentence | SPS introduced data-free path-control sampling or trajectory correction. | PIS contains both ingredients, although its correction is weighting rather than SPS's IMH. |

## Search Leads

| Lead | Why it follows from this paper | Route | Status |
|---|---|---|---|
| Denoising Diffusion Samplers, arXiv:2302.13834 | Replaces pinned Brownian reference dynamics with OU dynamics and compares stability. | forward citation / method extension | verified in run |
| Controlled Monte Carlo Diffusions, arXiv:2307.01050 | Learns coupled forward and backward annealed dynamics and retains path weights. | forward / adjacent method | verified in run |
| Weight variance near criticality | Tests whether PIS-style calibration remains practical in the SPS regime. | gap closure | open |
