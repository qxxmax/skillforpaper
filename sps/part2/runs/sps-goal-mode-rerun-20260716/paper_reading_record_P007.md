# Paper Reading Record

Record status: VERIFIED

## Identity Lock

| Field | Value | Evidence |
|---|---|---|
| Title | Stochastic normalizing flows as non-equilibrium transformations | E-220108862-I |
| Authors | Michele Caselle; Elia Cellini; Alessandro Nada; Marco Panero | E-220108862-I |
| Version and date | v3; 2022-07-06 | E-220108862-I |
| arXiv / DOI | arXiv:2201.08862v3 | E-220108862-I |
| Canonical URL | https://arxiv.org/abs/2201.08862 | E-220108862-I |
| Local full text | temporary exact PDF; SHA-256 recorded in source_identity_ledger.csv; not redistributed | E-220108862-I |
| Pages | 32 | E-220108862-I |
| Reading level | C4 | E-220108862-I |

## Paper Map

| Region | Purpose in the argument | Anchor | EvidenceID |
|---|---|---|---|
| Introduction | Connects lattice free-energy estimation, Jarzynski protocols, normalizing flows, and critical slowing down. | PDF pp. 2-3, Sec. 1 | E-220108862-P |
| Nonequilibrium identities | Defines work, forward paths, Jarzynski weights, and weighted observables. | PDF pp. 4-6, Sec. 2, Eqs. (1)-(10) | E-220108862-M |
| Unified path framework | Defines deterministic/stochastic path ratios and the path KL objective. | PDF pp. 6-10, Sec. 3, Eqs. (11)-(34) | E-220108862-M |
| Lattice tests | Compares stochastic evolutions, normalizing flows, and hybrid SNFs in two-dimensional phi4. | PDF pp. 10-22, Sec. 4, Figs. 1-9 | E-220108862-R |
| Discussion | Records cost, architecture, protocol, and near-criticality limits. | PDF pp. 22-24, Sec. 5 | E-220108862-L |

## Problem and Position

| Role | Paper-layer statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | Deterministic flows can be hard to train globally, while pure nonequilibrium protocols may need many stochastic updates. | PDF pp. 2-3, Sec. 1 | E-220108862-P |
| Existing baseline | Normalizing flows use invertible maps; Jarzynski/AIS-like methods use stochastic nonequilibrium paths and work weights. | PDF pp. 2-6, Secs. 1-2 | E-220108862-P |
| Gap | Place deterministic learned maps and stochastic Monte Carlo updates in one path-probability framework. | PDF pp. 3, 6-10, Secs. 1 and 3 | E-220108862-P |
| Contribution | The paper derives a common forward/reverse path ratio and builds SNFs by alternating affine flow blocks with stochastic detailed-balance updates. | PDF pp. 6-12, Secs. 3-4 | E-220108862-M |

## Mechanism

| Component or step | Definition / action | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| Forward stochastic path | Multiplies Markov transition probabilities along a prescribed protocol. | Each stochastic update is evaluable; the protocol connects base and target. | PDF pp. 7-9, Eqs. (20)-(22), (31)-(34) | E-220108862-M |
| Path weight | Uses the target/base boundary ratio times reverse/forward transition ratio. | Reverse transition probabilities are evaluable. | PDF pp. 8-9, Eqs. (23)-(27) | E-220108862-M |
| Deterministic block | Recovers normalizing-flow Jacobian factors as a special path transition. | Each map is invertible with tractable Jacobian. | PDF pp. 8-9, Eqs. (28)-(30) | E-220108862-M |
| Hybrid SNF | Alternates affine deterministic blocks and stochastic Monte Carlo blocks. | The selected stochastic kernels satisfy detailed balance at intermediate distributions. | PDF pp. 9-12, Secs. 3-4 | E-220108862-M |

## Equations

| Object | Exact formula or faithful notation | Symbol definitions | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Weighted observable | $\langle O\rangle_{\eta_{fin}}=\langle O(\phi_N)e^{-w}\rangle_f/\langle e^{-w}\rangle_f$ | $w$ is protocol work; $f$ denotes forward trajectories. | Produces target observables from nonequilibrium paths. | PDF p. 6, Eq. (10) | E-220108862-M |
| General path weight | $\tilde w(y_{0:N})=Zp(y_N)P_r(y_{N:0})/[Z_0q_0(y_0)P_f(y_{0:N})]$ | $P_f,P_r$ are forward/reverse path probabilities. | Unifies stochastic and deterministic transformations. | PDF p. 8, Eq. (23) | E-220108862-M |
| Path KL | $\tilde D_{KL}(q_0P_f\Vert pP_r)=-\langle\log\tilde w\rangle_f+\log(Z/Z_0)$ | The expectation is over base-initialized forward paths. | Training loss and irreversibility measure. | PDF p. 8, Eq. (26) | E-220108862-M |
| Jarzynski identity | $Z/Z_0=\langle\tilde w(y_{0:N})\rangle_f$ | The protocol and kernels satisfy the stated construction. | Normalizer estimate. | PDF p. 8, Eq. (27) | E-220108862-M |

## Experiments and Numbers

| Test | Setup / baseline / metric | Retained result | Uncertainty or cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| Two-dimensional phi4 | $16\times8$ through $64\times8$ lattices; pure stochastic paths, deterministic flows, and SNFs; $2\times10^5$ independent measurements. | Alternating stochastic and convolutional affine blocks improves the reported ESS and free-energy error in the tested setups. | The cost proxy in Fig. 3 omits training and deterministic-layer measurement cost. | PDF pp. 12-18, Secs. 4.1-4.3, Figs. 1-6 | E-220108862-R; E-220108862-L |
| Volume behavior | Fixed temporal extent and increasing spatial size. | At the tested settings, balanced numbers of stochastic and affine blocks maintain better effectiveness than pure stochastic protocols. | Architecture, protocol, and hardware dependence prevent a full quantitative comparison. | PDF pp. 18-22, Figs. 6-9 | E-220108862-R; E-220108862-L |

## Boundaries

| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | The efficiency comparison omits some deterministic and training costs, and a full quantitative comparison is beyond scope. | PDF pp. 16-18, Sec. 4.2 | E-220108862-L |
| Author-stated | Results are specific to affine CNN blocks, alternating placement, and the tested protocol; behavior near the transition may require other architectures. | PDF pp. 21-24, Secs. 4.4-5 | E-220108862-L |
| Reviewer inference | The main SNF estimator uses trajectory reweighting; the paper mentions ordinary independent MH as an alternative for deterministic flows but does not make extended-space trajectory IMH its SNF correction. | PDF pp. 7-9, Eqs. (16), (23)-(27) | inference |
| Unresolved | A matched comparison between SNF path weights and SPS extended-space IMH on the same target is absent. | P007 PDF pp. 12-24; P001 PDF pp. 7-20 | pending |

## Safe Output

| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | SNF already combines learned deterministic maps, stochastic path transitions, forward/reverse trajectory ratios, and Jarzynski reweighting in lattice field theory. | E-220108862-M; E-220108862-R |
| Prohibited sentence | SPS introduced stochastic lattice paths, path probability ratios, or exact weighted observables. | P007 contains all three, although it does not use SPS's extended-space trajectory IMH. |

## Search Leads

| Lead | Why it follows from this paper | Route | Status |
|---|---|---|---|
| CMCD, arXiv:2307.01050 | Learns annealed forward/backward dynamics rather than inserting fixed detailed-balance stochastic blocks. | forward / adjacent method | verified in run |
| SPS, arXiv:2606.13790 | Replaces weighted output by a corrected chain using a trajectory-dependent proposal ratio. | forward / focal comparison | verified in run |
| Matched SNF versus SPS correction study | Separates weight degeneracy from rejection/autocorrelation. | gap closure | open |
