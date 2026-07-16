# Part 2 Technical Learning Report

Report status: `DRAFT`

## Learning Question

Which earlier methods are needed to understand SPS, how does SPS work, and
which technical differences are supported by the current sources?

## Lineage Learning Path

| Order | PaperID / concept | Role | Prerequisite supplied | Relation / anchor | EvidenceID | Status |
|---|---|---|---|---|---|---|
| 1 | P002 / Path Integral Sampler | predecessor | stochastic-control view of sampling an unnormalized target by a path | R0171; P002 PDF pp. 4-8 method | E-211115141-M | C4 source checked; detailed R0-R6 upgrade pending |
| 2 | P007 / stochastic normalizing flows | predecessor branch | nonequilibrium path probabilities and weighting in lattice examples | R0172; P007 PDF pp. 2-8 method | E-220108862-M | C4 source checked; detailed R0-R6 upgrade pending |
| 3 | P003 / denoising diffusion samplers | closest objective prerequisite | tractable forward/reverse path densities and a path-space objective | R0177; P003 PDF pp. 4-8 method | E-230213834-M | C4 source checked; detailed R0-R6 upgrade pending |
| 4 | P001 / SPS | focal | paired Langevin paths, path KL, trajectory IMH, and lattice benchmark | P001 pp. 3-20, Secs. 2-3 | E-260613790-M; E-260613790-R | native R0-R6 verified |
| 5 | P031 / diffusion near criticality | later comparison node | cross-volume and infrared diagnostics in a related lattice diffusion study | R0199; P031 methods and Sec. V | E-260708505-M; E-260708505-R | checked citation; persistence claim unresolved |

In the Part 1 graph, the three predecessor paths cost 0.2 and the later-citation
path costs 0.3. These values set the reading order. The claims use the relation
IDs, full-text anchors, and EvidenceIDs shown above.

## Core Technical Difference

| Candidate delta | Statement layer | Compared sources | Fast locator | Verification anchor | EvidenceID | Decision |
|---|---|---|---|---|---|---|
| Data-free stochastic path sampling | source_supported_synthesis | P002, P003, P001 | abstracts plus method overview | P002/P003 PDF pp. 4-8; P001 pp. 3-7 | E-211115141-M; E-230213834-M; E-260613790-M | inherited family property; do not call it SPS novelty alone |
| Paired forward and auxiliary backward Langevin paths trained by a path log-ratio | author_claim | P001 | first operative equations | P001 pp. 5-7, Eqs. (2.2)-(2.17) | E-260613790-M | focal mechanism confirmed; predecessor subtraction pending |
| Full-trajectory independence-MH correction | author_claim | P001, with P007 as comparison branch | correction section | P001 pp. 7-9, Eqs. (2.18)-(2.19); P007 PDF pp. 2-8 | E-260613790-M; E-220108862-M | exactness role confirmed; novelty rank pending |
| Shorter reported autocorrelation near the tested pseudocritical point | author_claim | P001 | result plus limitation | P001 pp. 18-20, Fig. 8 | E-260613790-R; E-260613790-L | keep only with unmatched-update and cost boundary |
| Adoption by later lattice diffusion work | unresolved | P031 citing P001 | checked forward edge then method section | R0199; P031 methods and Sec. V | CIT-260708505-260613790; E-260708505-M | citation is confirmed; adoption is not |

The reading order is: P001 contribution paragraph, P001 operative equations,
the matching equations in P002/P003/P007, and then the experiment that tests
the difference.

## Technical Mechanism

| Step | Object / state | Operation | Assumption | Output | Anchor | EvidenceID |
|---|---|---|---|---|---|---|
| 1 | tractable prior state | sample the initial state and start a forward Langevin path | prior is sampleable and target action is evaluable | stochastic trajectory proposal | p. 5, Sec. 2.2, Eqs. (2.2), (2.5)-(2.6) | E-260613790-M |
| 2 | same trajectory space | define an auxiliary backward path with a second learned drift | forward and backward kernels use the stated scalar diffusion | reverse trajectory density | pp. 5-6, Sec. 2.2, Eqs. (2.3), (2.7)-(2.8) | E-260613790-M |
| 3 | forward and unnormalized backward path measures | minimize their expected log-ratio | finite training may leave residual irreversibility | learned path proposal | pp. 6-7, Sec. 2.3, Eqs. (2.11)-(2.17) | E-260613790-M |
| 4 | old and proposed terminal trajectories | apply trajectory-level independence MH | proposal covers target support | target-invariant corrected chain | pp. 7-9, Sec. 2.4, Eqs. (2.18)-(2.19) | E-260613790-M |

## Formula and Assumptions

| Formula ID | Formula | Symbols | Assumptions | Role | Source anchor | EvidenceID |
|---|---|---|---|---|---|---|
| F01 | $s_{i+1}=s_i+\sigma_\theta^2 K_{\theta,F}\Delta t+\sigma_\theta\xi_i\sqrt{\Delta t}$ | $K_{\theta,F}$ forward drift; $\sigma_\theta$ scalar diffusion; $\xi_i$ Gaussian noise | evaluable target action and chosen time discretization | generate the forward path | p. 5, Eq. (2.2) | E-260613790-M |
| F02 | $D_{\mathrm{KL}}=\int dq_F(\tau)\log[dq_F(\tau)/d\widetilde q_B(\tau)]$ | $q_F$ forward path measure; $\widetilde q_B$ unnormalized backward measure | target normalization need not be known | train by path irreversibility | p. 6, Eq. (2.13) | E-260613790-M |
| F03 | $P_{\mathrm{acc}}=\min(1,\widetilde\pi^*T_{\mathrm{reverse}}/(\widetilde\pi^*T_{\mathrm{forward}}))$ | $T$ contains full path factors | proposal support covers target support | exact correction | pp. 7-9, Eqs. (2.18)-(2.19) | E-260613790-M |
| F04 | $\tau_{\mathrm{int}}=1/2+\sum_{t=1}^{t_{\max}}\rho(t)$ | $\rho$ normalized autocorrelation | the paper's automatic window choice | diagnose chain correlation | pp. 18-19, Eqs. (3.8)-(3.11) | E-260613790-R |

## Algorithm and Implementation

The current T3 reconstruction is:

1. draw a state from the tractable prior;
2. generate a complete forward path with the learned forward drift;
3. evaluate the auxiliary backward path factors on that trajectory;
4. during training, minimize the sampled forward/backward path log-ratio;
5. after training, propose independent complete trajectories;
6. accept or reject the terminal proposal with the full trajectory ratio;
7. estimate observables and autocorrelation from the corrected chain.

`equation_code_map.csv` links each step to a source equation. Part 1 found no
public implementation to map, so the code fields remain `unavailable`.

## Evidence and Benchmarks

| Test | Comparable setup | Metric / observable | Result | Uncertainty / cost | Anchor | EvidenceID |
|---|---|---|---|---|---|---|
| corrected observables | 2D $L\times8$ phi4, $L=16,32,48,64$, stated coupling scan; HMC reference | magnetization and susceptibility | SPS+IMH follows the reported HMC values in the tested scan | row-level statistical errors reported | pp. 10-17, Figs. 3-5, Tables 1-3 | E-260613790-R |
| correction acceptance | 4096 SPS proposals over the stated scan | IMH acceptance | text reports roughly 0.60-0.76 at $L=16$ and 0.45-0.62 at $L=64$ | not an end-to-end efficiency measure | pp. 13-18, Sec. 3.4, Fig. 6 | E-260613790-R |
| timing | $\kappa=0.27$, reported hardware and schedule | training and generation wall time | about 1.1-1.2 h training; 1.1-2.1 min generation from $L=16$ to 64 | no matched HMC GPU-hour ratio | p. 17, Table 4 | E-260613790-L |
| autocorrelation | $\kappa=0.27$, $L=64$ | absolute-magnetization $\tau_{\mathrm{int}}$ | paper reports about 0.5 for SPS+IMH and about 160 for HMC | update units differ; total cost unmatched | pp. 18-20, Sec. 3.5, Fig. 8 | E-260613790-R; E-260613790-L |

## Technical Review

The sources support the SPS mechanism, its exact-correction condition, and the
reported 2D benchmark. They do not establish a universal speedup,
production-scale lattice-QCD readiness, or that every path-space component
originated in SPS. The detailed decisions are in `review_core.md`.

## Frontier Delta

`innovation_delta.csv` contains five comparisons. The unresolved question is
whether the central difference lies in the path-space objective, the paired
forward/backward parameterization, or the trajectory IMH correction. Answering
it requires equation-level R0-R6 reading of P002, P003, and P007.

## Learning Status

| Level | Demonstration | Evidence | Status |
|---|---|---|---|
| T0 | exact P001 version, authors, URL, source hash, and page count are locked | Part 1 identity and verification ledgers | pass |
| T1 | problem, mechanism, result, and scope can be explained without copying the abstract | Teach Back below | pass |
| T2 | four equations are defined by role, assumptions, and source anchor | Formula table and `equation_code_map.csv` | pass |
| T3 | focal algorithm is ordered, but predecessor equation subtraction is incomplete | algorithm trace plus pending delta rows | pending |
| T4 | official code mapping | `equation_code_map.csv` | not_requested |
| T5 | minimal reproduction | command, environment, output, and comparison | not_requested |

## Teach Back

SPS treats sampling as learning a stochastic route from an easy prior to an
unnormalized lattice target. A forward drift generates the proposal path and
an auxiliary backward drift makes a path-probability ratio available. Training
reduces that path mismatch. Because finite training does not make the proposal
exact, the method uses a full-trajectory independence-MH correction. In the
reported two-dimensional phi4 tests, the corrected observables agree with the
HMC reference and the autocorrelation in the paper's own update units is much
shorter near one tested pseudocritical setting. This does not yet establish a
matched GPU-hour speedup or broad scaling. Earlier path-control, diffusion, and
stochastic-flow papers already contain related ingredients, so the precise SPS
innovation must be stated only after their equations and correction mechanisms
are aligned.

## Boundaries and Open Questions

| Layer | Statement | Source / reasoning | Next action |
|---|---|---|---|
| Author-stated | exact correction requires proposal support over the target | P001 pp. 7-8, Sec. 2.4; E-260613790-L | add tail and support stress tests in Part 3 |
| Author-stated | autocorrelation units and total costs are not matched | P001 p. 20, Sec. 3.5; E-260613790-L | compare observable error per total GPU-hour |
| Reviewer inference | data-free path sampling alone is not an SPS-only contribution | P002/P003/P001 method evidence | finish predecessor equation subtraction |
| Unresolved | whether paired drifts plus trajectory IMH are the smallest supported central difference | broad predecessor method anchors only | create full R0-R6 records for P002, P003, P007 |
| Unresolved | whether later work retains or validates the SPS mechanism | R0199 proves citation, not method adoption | inspect later method comparisons and future citations |
