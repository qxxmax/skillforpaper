# Part 2 Technical Learning Report

Report status: VERIFIED

## Learning Question

Which components of SPS already appear in PIS, DDS, CMCD, and stochastic
normalizing flows; what does SPS change; and how does the corrected SPS
algorithm work through competence level T3?

## Lineage Learning Path

| Order | PaperID / concept | Role | Prerequisite supplied | Relation / anchor | EvidenceID | Status |
|---|---|---|---|---|---|---|
| 1 | P002 / PIS | predecessor | controlled path, path cost, and trajectory importance weight | R0171; PDF pp. 3-6, Sec. 3 | E-211115141-M | C4 read |
| 2 | P003 / DDS | predecessor | OU reference, reverse path KL, and reference-preserving discretization | R0177; PDF pp. 2-8, Secs. 2-3.4 | E-230213834-M | C4 read |
| 3 | P004 / CMCD | closest dynamics predecessor | simultaneous score-coupled forward/backward drift adaptation | R0178; PDF pp. 6-9, Eqs. (21)-(24) | E-230701050-M | C4 read |
| 4 | P007 / SNF | lattice predecessor branch | lattice path ratios, Jarzynski reweighting, and hybrid stochastic layers | R0172; PDF pp. 6-12, Eqs. (20)-(34) | E-220108862-M | C4 read |
| 5 | P001 / SPS | focal | independent drift networks, learned diffusion, path KL, and trajectory IMH | PDF pp. 5-9, Eqs. (2.2)-(2.19) | E-260613790-M | C4 read |
| 6 | P031 / later citing paper | successor check | confirms a later citation, not method reuse | R0199; method section and Sec. V | E-260708505-M | reuse not established |

Dijkstra supplied the initial reading order. P004 was added after P001
identified CMCD as a method that already learns both directions. Paper
equations, not the graph score, support the comparison.

## Core Technical Difference

| Candidate difference | Statement layer | Compared sources | Fast locator | Verification anchor | EvidenceID | Decision |
|---|---|---|---|---|---|---|
| Data-free path sampling | source_supported_synthesis | P002, P003, P001 | path objectives | P002 Eq. (13); P003 Eq. (10); P001 Eq. (2.13) | E-211115141-M; E-230213834-M; E-260613790-M | inherited |
| Forward/backward drift learning | source_supported_synthesis | P004, P001 | drift equations | P004 Eqs. (21)-(22); P001 Eqs. (2.2)-(2.8) | E-230701050-M; E-260613790-M | inherited family; parameterization changed |
| Independent drift networks and learned scalar diffusion | source_supported_synthesis | P004, P001 | operative kernels | P004 pp. 6-9; P001 pp. 5-7 | E-230701050-M; E-260613790-M | design difference; benefit unresolved |
| Lattice stochastic path ratios | source_supported_synthesis | P007, P001 | path-ratio sections | P007 Eqs. (23)-(27); P001 Eqs. (2.13)-(2.17) | E-220108862-M; E-260613790-M | inherited lattice branch |
| Extended-space trajectory IMH | source_supported_synthesis | P002, P003, P004, P007, P001 | correction equations | predecessor weight equations; P001 Eqs. (2.18)-(2.19) | E-211115141-M; E-230213834-M; E-230701050-M; E-220108862-M; E-260613790-M | narrowest checked difference |
| Universal efficiency gain | reviewer_inference | P007, P001 | cost boundaries | P007 pp. 16-24; P001 Table 4 and Sec. 3.5 | E-220108862-L; E-260613790-L | unsupported |

The defensible sentence is:

> SPS adapts the path-space sampler family to lattice field theory and uses
> the full trajectory ratio as an extended-space independence-MH correction.

This is a checked design difference, not a first-ever priority claim.

## Technical Mechanism

| Step | Object / state | Operation | Assumption | Output | Anchor | EvidenceID |
|---|---|---|---|---|---|---|
| 1 | prior state $s_0$ | draw from the tractable Gaussian prior | prior is sampleable | path start | PDF p. 5, Eq. (2.6) | E-260613790-M |
| 2 | forward path | apply learned $K_{\theta,F}$ and $\sigma_\theta$ for $T$ steps | Gaussian kernels are evaluable | endpoint proposal and forward factors | PDF p. 5, Eqs. (2.2), (2.5)-(2.6) | E-260613790-M |
| 3 | same path in reverse order | evaluate learned $K_{\theta,B}$ and reverse Gaussian factors | both directions share the stated scalar diffusion | backward factors | PDF pp. 5-6, Eqs. (2.7)-(2.8) | E-260613790-M |
| 4 | forward and unnormalized backward path measures | minimize their sampled log ratio | target action is evaluable without $Z$ | trained path proposal | PDF pp. 6-7, Eqs. (2.13)-(2.17) | E-260613790-M |
| 5 | current and proposed extended paths | accept or reject with the full trajectory ratio | proposal covers target support | target-invariant corrected chain | PDF pp. 7-9, Eqs. (2.18)-(2.19) | E-260613790-M |
| 6 | corrected chain | compute observables and autocorrelation | burn-in and error analysis follow the stated setup | benchmark estimates | PDF pp. 10-20, Sec. 3 | E-260613790-R |

## Formula and Assumptions

| Formula ID | Formula | Symbols | Assumptions | Role | Source anchor | EvidenceID |
|---|---|---|---|---|---|---|
| F01 | $D_{KL}(Q^u\Vert Q^*)=E[\mathrm{control\ energy}+\mathrm{terminal\ cost}]$ | $Q^u$ is the PIS controlled path | target path is absolutely continuous with respect to proposal | inherited path-control objective | P002 PDF p. 4, Eq. (13) | E-211115141-M |
| F02 | $KL(Q_\theta\Vert P)=E[\mathrm{OU\ control\ energy}+\mathrm{endpoint\ ratio}]$ | $P$ is target noising; $Q_\theta$ learned reverse | OU terminal marginal is approximately Gaussian | inherited reverse path KL | P003 PDF p. 4, Eq. (10) | E-230213834-M |
| F03 | $L_D^{CMCD}=D(P_F\Vert P_B)$ | $P_F,P_B$ share a score-coupled learned control | intermediate scores are tractable | paired-drift predecessor | P004 PDF p. 7, Eq. (22) | E-230701050-M |
| F04 | $\tilde D_{KL}(q_0P_f\Vert pP_r)=-E_f\log\tilde w+\log(Z/Z_0)$ | $\tilde w$ is the SNF path weight | reverse transitions or Jacobians are evaluable | lattice path-ratio predecessor | P007 PDF p. 8, Eq. (26) | E-220108862-M |
| F05 | $D_{KL}=\int dq_F\log(dq_F/d\tilde q_B)$ | $dq_F$ uses the prior; $d\tilde q_B$ uses the unnormalized target | finite training may leave residual path dependence | SPS training | P001 PDF p. 6, Eq. (2.13) | E-260613790-M |
| F06 | $P_{acc}=\min[1,\tilde\pi(s_T')T(s_T'\!\to s_T)/(\tilde\pi(s_T)T(s_T\!\to s_T'))]$ | each $T$ contains complete path factors | proposal support covers target support | SPS exactness gate | P001 PDF pp. 7-9, Eqs. (2.18)-(2.19) | E-260613790-M |

## Algorithm and Implementation

T3 reconstruction:

    training
      draw s0 from the prior
      simulate a complete forward Langevin path
      evaluate forward and backward Gaussian factors on that path
      form log qF(path) - log qtildeB(path)
      update both drift networks and the diffusion network

    generation and correction
      independently draw a new complete path and endpoint
      retain its path-dependent proposal ratio
      compare proposed and current extended paths with Eq. (2.19)
      accept or retain the current path
      measure observables on the corrected endpoint chain

Inputs, state, updates, output, and correction are ordered and source-anchored,
which satisfies T3. T4 and T5 were not requested. Accordingly,
equation_code_map.csv traces formulas to algorithm steps but does not invent
code symbols or a reproduction result.

## Evidence and Benchmarks

| Test | Comparable setup | Metric / observable | Result | Uncertainty / cost | Anchor | EvidenceID |
|---|---|---|---|---|---|---|
| corrected observables | 2D $L\times8$ phi4, $L=16,32,48,64$; HMC, SPS, SPS+IMH | magnetization and susceptibility | corrected SPS follows the reported HMC values across the tested scan | row-level statistical errors are reported | PDF pp. 10-17, Figs. 3-5, Tables 1-3 | E-260613790-R |
| correction acceptance | 4096 proposals over the stated scan | IMH acceptance | text reports about 0.60-0.76 at $L=16$ and 0.45-0.62 at $L=64$ | acceptance is not total efficiency | PDF pp. 13-18, Fig. 6 | E-260613790-R |
| timing | $\kappa=0.27$ and stated hardware/schedules | training and proposal generation | about 1.1-1.2 h training and 1.1-2.1 min generation across $L=16$ to 64 | no matched HMC GPU-hour ratio | PDF p. 17, Table 4 | E-260613790-L |
| autocorrelation | $\kappa=0.27$, $L=64$ | absolute-magnetization $\tau_{int}$ | paper reports about 0.5 for SPS+IMH and about 160 for HMC | IMH steps and HMC trajectories are different units; cost is unmatched | PDF pp. 18-20, Fig. 8 | E-260613790-R; E-260613790-L |

## Technical Review

review_core.md rejects three broad claims: SPS did not introduce path-space
sampling, did not first learn both drift directions, and is not shown to be
universally faster than HMC. The retained claims are the lattice adaptation,
the corrected benchmark, and extended-space trajectory IMH, together with
their support and cost limits.

## Checked Difference

innovation_delta.csv contains six verified component comparisons, one
reviewer inference about unmatched efficiency, and one unresolved successor
claim. The narrowest checked difference is the use of the path-dependent
trajectory ratio in an independence-MH correction. A broader novelty or
priority claim would require another Part 1 search aimed specifically at
earlier auxiliary-variable and path-space MH constructions.

## Learning Status

| Level | Demonstration | Evidence | Status |
|---|---|---|---|
| T0 | five exact versions, page counts, URLs, and hashes | source_identity_ledger.csv | pass |
| T1 | problem, inherited mechanism, result, and limits are explained below | Teach Back and review_core.md | pass |
| T2 | six aligned formula roles and five C4 reading records | Formula table; paper_reading_record_P*.md | pass |
| T3 | ordered SPS training, proposal, extended-state correction, and output | Algorithm section; equation_code_map.csv | pass |
| T4 | official code-symbol mapping | outside the declared target | not_requested |
| T5 | numerical reproduction | outside the declared target | not_requested |

## Teach Back

PIS already showed that an unnormalized target can be reached by learning a
controlled stochastic path and correcting imperfect training with trajectory
weights. DDS changed the reference process to OU dynamics and trained its
reverse path. CMCD then learned coupled forward and backward annealed drifts.
SNF had already used path ratios and stochastic updates in lattice field
theory. SPS combines this lineage differently: it learns separate forward and
backward Langevin drift networks and a scalar diffusion, then uses the
path-dependent proposal ratio inside an extended-space independence-MH step.
That step turns approximate independent proposals into a corrected Markov
chain, provided the proposal covers the target support. The paper validates
this combination on a two-dimensional phi4 scan; it does not yet establish a
matched total-cost speedup or the isolated benefit of each learned component.

## Boundaries and Open Questions

| Layer | Statement | Source / reasoning | Next action |
|---|---|---|---|
| Author-stated | exact IMH sampling requires proposal support | P001 PDF pp. 7-8; E-260613790-L | Part 3 support and tail stress tests |
| Author-stated | autocorrelation units and total costs are not matched | P001 PDF p. 20; E-260613790-L | compare observable error per total GPU-hour |
| Reviewer inference | extended-space trajectory IMH is the narrowest difference among the five checked core papers | predecessor correction equations plus P001 Eqs. (2.18)-(2.19) | priority search before saying first |
| Unresolved | independent drifts or learned diffusion may help, but their effects are not isolated | P004/P001 equation comparison; no matched ablation | Part 3 controlled ablation |
| Unresolved | P031 cites SPS but does not establish method reuse | R0199 and P031 method record | monitor later citations and explicit reuse |
