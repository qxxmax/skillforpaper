# Paper Reading Record

Record status: VERIFIED

## Identity Lock

| Field | Value | Evidence |
|---|---|---|
| Title | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | E-230701050-I |
| Authors | Francisco Vargas; Shreyas Padhy; Denis Blessing; Nikolas Nuesken | E-230701050-I |
| Version and date | v12; 2025-05-07 | E-230701050-I |
| arXiv / DOI | arXiv:2307.01050v12 | E-230701050-I |
| Canonical URL | https://arxiv.org/abs/2307.01050 | E-230701050-I |
| Local full text | temporary exact PDF; SHA-256 recorded in source_identity_ledger.csv; not redistributed | E-230701050-I |
| Pages | 43 | E-230701050-I |
| Reading level | C4 | E-230701050-I |

## Paper Map

| Region | Purpose in the argument | Anchor | EvidenceID |
|---|---|---|---|
| Framework | Connects variational inference and forward/reverse path divergences. | PDF pp. 1-5, Secs. 1-2 | E-230701050-P |
| Simultaneous learning | Explains why CMCD learns the forward and backward process together instead of alternating IPF updates. | PDF pp. 5-6, Sec. 3.1 | E-230701050-M |
| CMCD mechanism | Defines the annealed forward/backward drifts, path divergence, weight, and discrete algorithm. | PDF pp. 6-9, Sec. 3.2, Eqs. (21)-(24) | E-230701050-M |
| Experiments | Compares CMCD with annealed diffusion, PIS, DDS, and SMC baselines. | PDF pp. 9-10, Sec. 4, Fig. 1 | E-230701050-R |
| Discussion | States the tested scope and future work on annealing paths and divergences. | PDF p. 10, Sec. 5 | E-230701050-L |

## Problem and Position

| Role | Paper-layer statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | Fixed annealing diffusions can give unstable or high-variance path weights, while alternating forward/backward fitting is slow and accumulates error. | PDF pp. 5-7, Secs. 3.1-3.2 | E-230701050-P |
| Existing baseline | PIS and DDS learn a path in one principal direction; AIS-like methods use prescribed annealing; IPF alternates path projections. | PDF pp. 1-7, Secs. 1-3 | E-230701050-P |
| Gap | Learn an annealed diffusion end to end while adapting its coupled forward and backward dynamics and retaining a tractable trajectory ratio. | PDF pp. 5-7, Secs. 3.1-3.2 | E-230701050-P |
| Contribution | CMCD learns a control field along a prescribed density path, which modifies both forward and backward drifts under a score constraint, and trains it by path-space divergence. | PDF pp. 6-9, Eqs. (21)-(24) | E-230701050-M |

## Mechanism

| Component or step | Definition / action | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| Annealing path | Fixes tractable intermediate densities $\pi_t$ and their scores. | $\nabla\log\pi_t$ and unnormalized $\hat\pi_t$ can be evaluated. | PDF p. 6, Sec. 3.2 | E-230701050-M |
| Forward drift | Adds one learned control $\nabla\phi_t$ to $\sigma^2\nabla\log\pi_t$. | The controlled SDE is well posed. | PDF p. 6, Eq. (21) | E-230701050-M |
| Coupled backward drift | Uses $-\sigma^2\nabla\log\pi_t+\nabla\phi_t$, linked to the forward drift by the score. | The score constraint supplies the uniqueness result. | PDF p. 7, Eq. (22), Proposition 3.2 | E-230701050-M |
| Weight and training | Evaluates a forward/backward path ratio and minimizes its negative log estimate. | The discretized Gaussian transition densities are evaluable. | PDF pp. 7-9, Eqs. (23)-(24), Algorithms 1-2 | E-230701050-M |

## Equations

| Object | Exact formula or faithful notation | Symbol definitions | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Controlled forward SDE | $dY_t=[\sigma^2\nabla\log\pi_t(Y_t)+\nabla\phi_t(Y_t)]dt+\sigma\sqrt{2}\,dW_t$ | $\pi_t$ is the prescribed path; $\phi_t$ is learned. | Moves the prior along the annealing path. | PDF p. 6, Eq. (21) | E-230701050-M |
| Coupled path objective | $L_D^{CMCD}(\phi)=D(P_{\pi_0,\sigma^2\nabla\log\pi+\nabla\phi}^{\rightarrow}\Vert P_{\pi_T,-\sigma^2\nabla\log\pi+\nabla\phi}^{\leftarrow})$ | The two path measures share the learned control and differ by the score term. | Learns both directions simultaneously. | PDF p. 7, Eq. (22) | E-230701050-M |
| Normalizer identity | $Z=E[dP_{\hat\pi_T,-\sigma^2\nabla\log\pi+\nabla\phi}^{\leftarrow}/dP_{\pi_0,\sigma^2\nabla\log\pi+\nabla\phi}^{\rightarrow}]$ | The ratio is evaluated on controlled paths. | Unbiased importance estimate of $Z$ for any control; zero variance at the optimum. | PDF p. 7, Eq. (23) | E-230701050-M |
| Discrete KL loss | $L_{KL}^{CMCD}\approx E\log[\pi_0(Y_0)\prod_k q_F(Y_{k+1}|Y_k)/(\hat\pi_T(Y_T)\prod_k q_B(Y_k|Y_{k+1}))]$ | $q_F,q_B$ are the stated Gaussian kernels. | Practical trajectory-ratio training loss. | PDF pp. 8-9, Eq. (24) | E-230701050-M |

## Experiments and Numbers

| Test | Setup / baseline / metric | Retained result | Uncertainty or cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Annealed inference suite | Overdamped and underdamped CMCD against ULA, MCD, UHA, and LDVI. | The paper reports higher ELBOs for CMCD across its tested targets, especially at low step counts. | Results depend on target, annealing path, divergence, and tuning. | PDF pp. 9-10, Sec. 4, Fig. 1 | E-230701050-R |
| Normalizer and sample tests | Funnel and Gaussian-mixture targets; compare PIS, DDS, SMC, and CMCD. | CMCD is reported to recover log normalizers more consistently in the shown tests. | The figure uses thirty sampling seeds and $K\in\{8,16,32,64,128,256\}$. | PDF pp. 9-10, Sec. 4, Fig. 1 | E-230701050-R |

## Boundaries

| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | CMCD assumes a prescribed path with tractable intermediate scores and leaves optimal annealing paths and alternate divergences to future work. | PDF pp. 6, 10, Secs. 3.2 and 5 | E-230701050-L |
| Author-stated | Optimal control yields the desired path and zero-variance weight; the algorithm labels finite-trained terminal draws approximate. | PDF pp. 7-9, Eq. (23), Algorithm 1 | E-230701050-L |
| Reviewer inference | CMCD already learns both forward and backward dynamics, but they are coupled by the score relation and its correction is a path weight rather than an IMH accept/reject step. | PDF pp. 6-9, Eqs. (21)-(24) | inference |
| Unresolved | Whether independently parameterized drifts improve lattice-field coverage over the CMCD score-coupled form is not tested by these papers. | P004 PDF pp. 6-10; P001 PDF pp. 5-9 | pending |

## Safe Output

| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | CMCD predates SPS in jointly adapting forward and backward diffusion dynamics through a forward/reverse path objective, so paired drifts alone are not a defensible SPS novelty. | E-230701050-M; E-260613790-M |
| Prohibited sentence | SPS was the first method to learn both directions of a stochastic path. | P001 itself cites CMCD for this property, and P004 Eq. (22) defines the coupled pair. |

## Search Leads

| Lead | Why it follows from this paper | Route | Status |
|---|---|---|---|
| SPS trajectory IMH | Tests what changes when path weights become an extended-space accept/reject correction. | forward / focal comparison | verified in run |
| NETS, arXiv:2410.02711 | Adjacent nonequilibrium transport method cited by SPS. | forward / adjacent method | Part 1 verified; not promoted for T3 |
| Independent versus score-coupled drifts | Isolates one possible SPS design difference. | controlled ablation | open |
