# Paper Reading Record

Record status: `VERIFIED`

## Identity Lock

| Field | Value | Evidence |
|---|---|---|
| Title | Stochastic Path Sampler For Lattice Field Theory | E-260613790-I |
| Authors | Shiyang Chen; Moxian Qian; Gert Aarts; Biagio Lucini; Kai Zhou | E-260613790-I |
| Version and date | v1; 2026-06-11 | E-260613790-I |
| arXiv / DOI | arXiv:2606.13790v1 | E-260613790-I |
| Canonical URL | https://arxiv.org/abs/2606.13790 | E-260613790-I |
| Local full text | sources/pdfs/2606.13790.pdf (local audit cache; not redistributed) | E-260613790-I |
| Pages | 33 | E-260613790-I |
| Reading level | C4 | E-260613790-I |

## Paper Map

| Region | Purpose in the argument | Anchor | EvidenceID |
|---|---|---|---|
| Abstract and introduction | Defines the unnormalized-target problem, critical slowing down, prior model families, and the paper's claimed gap | pp. 1-3, Sec. 1 | E-260613790-P |
| Path-space construction | Defines the forward and backward stochastic paths, entropy-production objective, and finite-training residual | pp. 3-7, Secs. 2.1-2.3 | E-260613790-M |
| Exact correction | Defines the trajectory-level independence Metropolis-Hastings correction and its support condition | pp. 7-9, Sec. 2.4, Eqs. (2.18)-(2.19) | E-260613790-M |
| Two-dimensional benchmark | Specifies the phi4 action, observables, lattice geometry, training regime, and HMC comparison | pp. 9-18, Sec. 3, Tables 1-4 | E-260613790-R |
| Autocorrelation analysis | Compares SPS+IMH and HMC for absolute magnetization near the finite-volume pseudocritical region | pp. 18-20, Sec. 3.5, Fig. 8 | E-260613790-R |
| Conclusions and appendices | States scaling limits, future directions, architecture details, and mode-coverage diagnostics | pp. 20-28, Sec. 4, Appendices B-C | E-260613790-L |

## Problem and Position

| Role | Paper-layer statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | Lattice targets are known only up to normalization, while conventional chains can develop long autocorrelation times near phase transitions or the continuum limit. | p. 1, abstract; pp. 1-2, Sec. 1 | E-260613790-P |
| Existing baseline | The paper positions HMC as the conventional benchmark and groups learned alternatives into variational models, supervised generative models, and data-free path-space samplers. | pp. 1-3, Sec. 1 | E-260613790-P |
| Gap | A useful proposal should require no target samples, handle stochastic paths rather than only a deterministic endpoint map, and still admit an exact correction. | pp. 2-3, Sec. 1 | E-260613790-P |
| Contribution | SPS learns paired forward and auxiliary backward Langevin dynamics by reducing path-space irreversibility, then corrects independent trajectory proposals with extended-space IMH. | p. 1, abstract; pp. 3-9, Sec. 2 | E-260613790-M |

## Mechanism

| Component or step | Definition / action | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| Forward path | Starts from a tractable prior and applies a learned drift plus Gaussian diffusion to reach a terminal proposal. | The prior is sampleable and the target action can be evaluated. | p. 5, Sec. 2.2, Eqs. (2.2), (2.5)-(2.6) | E-260613790-M |
| Auxiliary backward path | Uses a second learned drift on the same trajectory space to define a reverse path measure from target to prior. | Forward and backward kernels share the specified scalar time-dependent diffusion coefficient. | pp. 5-6, Sec. 2.2, Eqs. (2.3), (2.7)-(2.8) | E-260613790-M |
| Training objective | Minimizes the KL divergence between the forward path measure and an unnormalized backward path measure, equivalently the expected path log-ratio. | Finite capacity, finite training, and discretization can leave residual irreversibility. | pp. 6-7, Sec. 2.3, Eqs. (2.11)-(2.17) | E-260613790-M |
| Exactness gate | Applies an independence Metropolis-Hastings accept/reject step using full trajectory probabilities. | Exactness requires that the SPS proposal cover the support of the target. | pp. 7-9, Sec. 2.4, Eqs. (2.18)-(2.19) | E-260613790-M |

## Equations

| Object | Exact formula or faithful notation | Symbol definitions | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Forward Langevin update | $s_{i+1}=s_i+\sigma_\theta^2(t_i)K_{\theta,F}(s_i,t_i)\Delta t+\sigma_\theta(t_i)\xi_i\sqrt{\Delta t}$ | $K_{\theta,F}$ is the learned forward drift; $\sigma_\theta$ is the learned scalar diffusion; $\xi_i$ is standard Gaussian noise. | Generates the stochastic proposal path from the prior. | p. 5, Eq. (2.2) | E-260613790-M |
| Path-space objective | $D_{\mathrm{KL}}=\int dq_F(\tau)\log[dq_F(\tau)/d\tilde q_B(\tau)]$ | $dq_F$ is the forward path measure and $d\tilde q_B$ uses the unnormalized target at the terminal state. | Measures path irreversibility without requiring the partition function. | p. 6, Eq. (2.13) | E-260613790-M |
| Trajectory IMH correction | $P_{\mathrm{accept}}=\min\{1,\tilde\pi^*(s_T')T(s_T'\!\to s_T)/[\tilde\pi^*(s_T)T(s_T\!\to s_T')]\}$ | $T$ contains the full forward and backward trajectory factors. | Restores target invariance for a support-covering proposal. | pp. 7-9, Eqs. (2.18)-(2.19) | E-260613790-M |
| Integrated autocorrelation | $\tau_{|M|,\mathrm{int}}=\frac{1}{2}+\sum_{t=1}^{t_{\max}}\bar C_{|M|}(t)$ | $\bar C$ is the normalized autocorrelation; $t_{\max}$ is chosen by the stated automatic window. | Quantifies correlation in the generated Markov chain. | pp. 18-19, Eqs. (3.8)-(3.11) | E-260613790-R |

## Experiments and Numbers

| Test | Setup / baseline / metric | Retained result | Uncertainty or cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Physical observables | Two-dimensional $L\times8$ phi4 lattices with $L=16,32,48,64$, $\lambda=0.022$, and $\kappa=0.20$ to $0.30$; compare HMC, uncorrected SPS, and SPS+IMH. | Corrected magnetization and susceptibility follow the HMC benchmark across the tested scan; uncorrected SPS shows larger deviations in difficult tail and multimodal regions. | Values and statistical errors are reported row by row. | pp. 10-17, Figs. 3-5, Tables 1-3 | E-260613790-R |
| Acceptance | IMH chains use 4096 SPS proposals over the same lattice sizes and coupling scan. | The text reports about 0.60-0.76 for $L=16$ and 0.45-0.62 for $L=64$, with a volume-dependent decrease. | These are acceptance ranges, not end-to-end efficiency. | pp. 13-18, Sec. 3.4, Fig. 6 | E-260613790-R |
| Training and generation | At $\kappa=0.27$, generation uses 2500 diffusion steps for 4096 samples; training uses 250 diffusion steps, 15000 optimization steps, and batch size 12. | Generation rises from about 1.1 to 2.1 minutes from $L=16$ to 64; training is about 1.1-1.2 hours. | Hardware and setup are specified separately; no matched HMC GPU-hour ratio is reported. | p. 17, Table 4; Appendix B.2 | E-260613790-L |
| Autocorrelation | At $\kappa=0.27$ and $L=64$, compare absolute-magnetization autocorrelation for SPS+IMH and HMC. | The paper reports $\tau_{|M|,\mathrm{int}}\simeq0.5$ for SPS+IMH and about 160 for HMC. | The paper explicitly notes that these use IMH steps versus HMC trajectories and are not a cost-matched speed ratio. | pp. 18-20, Sec. 3.5, Fig. 8 | E-260613790-R |

## Boundaries

| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | Finite model capacity, finite training, and discretization prevent exact trajectory balance before correction; proposal support is required for exact IMH sampling. | pp. 7-8, Secs. 2.3-2.4 | E-260613790-L |
| Author-stated | The reported autocorrelation times use different update units and do not provide a cost-matched comparison including training and generation. | p. 20, Sec. 3.5 | E-260613790-L |
| Author-stated | The current global convolutional architecture grows with lattice extent; larger and higher-dimensional systems need a scaling study and more local architectures. | p. 21, Sec. 4 | E-260613790-L |
| Reviewer inference | The evidence supports the tested two-dimensional benchmark, but not a universal claim that SPS is faster than HMC in wall time or GPU-hours. | p. 17, Table 4; p. 20, Sec. 3.5 | inference |
| Unresolved | Whether the autocorrelation advantage survives a matched total-cost comparison including training, proposal generation, and correction remains open. | p. 17, Table 4; pp. 19-20, Fig. 8 | pending |
| Unresolved | Scaling to gauge fields, larger volumes, and higher dimensions is proposed rather than demonstrated. | pp. 20-21, Sec. 4 | pending |

## Safe Output

| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | In the tested two-dimensional $L\times8$ phi4 benchmark, SPS+IMH reproduces the reported HMC observables and has a much shorter absolute-magnetization autocorrelation at $\kappa=0.27$, while the paper leaves a matched total-cost comparison open. | E-260613790-R; E-260613790-L |
| Prohibited sentence | SPS is universally 320 times faster than HMC. | The ratio divides autocorrelation times measured in different update units and omits matched training and generation cost; E-260613790-L. |

## Search Leads

| Lead | Why it follows from this paper | Route | Status |
|---|---|---|---|
| Path Integral Sampler, arXiv:2111.15141 | Earlier data-free stochastic-control path sampler named in the SPS positioning. | backward citation | verified in run |
| Denoising Diffusion Samplers, arXiv:2302.13834 | Closely related path-space KL construction and data-free diffusion sampling. | backward citation | verified in run |
| Controlled Monte Carlo Diffusions, arXiv:2307.01050 | P001 explicitly notes that this predecessor learns both forward and backward drifts, so it is required before making a novelty claim. | backward citation | verified and promoted in this run |
| Stochastic normalizing flows, arXiv:2201.08862 and 2210.03139 | Lattice lineage combining deterministic maps and stochastic updates. | backward citation | verified in run |
| Diffusion Models for Sampling Near Criticality in Lattice Field Theories, arXiv:2607.08505 | Later adjacent work useful for a forward comparison of criticality claims. | forward / adjacent | verified in run |
| Cost-normalized SPS versus HMC | Directly closes the boundary exposed by Sec. 3.5 and Table 4. | gap closure | open |
