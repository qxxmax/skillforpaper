# Part 2 Technical Review

Review status: READY

## Entry Check

- [x] P001, P002, P003, P004, and P007 are identity- and version-locked.
- [x] All five full texts have validated R0-R6 reading records.
- [x] Every retained cross-paper delta has anchors from both sides.
- [x] R0171, R0172, R0177, and R0178 are checked direct-citation edges.
- [x] Source statements, synthesis, inference, and unresolved questions are separated.

## Method Comparison

| Dimension | Inherited component | Claimed change | Evidence that isolates it | Statement layer | Decision |
|---|---|---|---|---|---|
| scientific object | PIS and DDS already sample unnormalized targets by learned stochastic paths | SPS applies the family to lattice phi4 and produces a corrected chain | P002 PDF pp. 3-6; P003 PDF pp. 2-6; P001 PDF pp. 3-17 | source_supported_synthesis | keep as adaptation, not invention |
| objective | PIS, DDS, CMCD, and SNF all use path costs or forward/reverse path ratios | SPS uses a discrete forward-path KL against an unnormalized learned backward path | P001 p. 6, Eq. (2.13), compared with P002 Eq. (13), P003 Eq. (10), P004 Eq. (22), P007 Eq. (26) | source_supported_synthesis | keep as formulation difference |
| dynamics | CMCD already adapts forward and backward drifts simultaneously | SPS uses independent drift networks and a learned scalar diffusion rather than CMCD's score-coupled pair | P004 pp. 6-9, Eqs. (21)-(24); P001 pp. 5-7, Eqs. (2.2)-(2.17) | source_supported_synthesis | keep difference; benefit unresolved |
| correction | PIS, DDS, CMCD, and SNF use trajectory importance weights or reweighting | SPS uses the path-dependent ratio in extended-space independence MH | P002 p. 6, Eq. (17); P003 p. 4, Eq. (11); P004 pp. 7-9; P007 pp. 7-9; P001 pp. 7-9 | source_supported_synthesis | narrowest checked difference |
| lattice branch | SNF already combines stochastic paths and learned maps in lattice phi4 | SPS learns stochastic Langevin drifts and omits invertible affine blocks | P007 pp. 6-22; P001 pp. 5-20 | source_supported_synthesis | keep as architecture change |
| efficiency | each paper reports its own ESS, error, weight, or autocorrelation diagnostics | SPS reports corrected-chain autocorrelation and wall times | P007 pp. 16-24; P001 p. 17 and pp. 18-20 | reviewer_inference | no cross-paper speed ranking |

## Validity And Reproducibility

| Check | Finding | Source anchor / reasoning | Severity | Status |
|---|---|---|---|---|
| Assumptions | SPS exactness requires proposal support; path-training optimum is not assumed after IMH. | P001 pp. 7-9, Sec. 2.4; E-260613790-L | high | pass with condition |
| Correctness / exactness | Exactness belongs to SPS+IMH, not uncorrected SPS; predecessor weighted estimators are a different output object. | P001 pp. 7-15; P002 p. 6; P004 pp. 7-9 | high | pass with boundary |
| Baseline fairness | HMC validates observables, but SPS IMH steps and HMC trajectories are not matched compute units. | P001 pp. 18-20, Sec. 3.5 | high | concern |
| Metrics / observables | Magnetization, susceptibility, acceptance, timing, and autocorrelation are reported for the stated 2D scan. | P001 pp. 10-20, Sec. 3 | low | pass |
| Ablations / controls | Uncorrected SPS versus SPS+IMH isolates the need for correction, but independent drifts and learned diffusion are not separately ablated. | P001 pp. 10-15, Tables 1-2; Sec. 2 | medium | partial |
| Uncertainty / sensitivity | Observable tables report statistical errors; matched total-cost uncertainty and support stress tests are absent. | P001 Tables 1-4; Appendix C | medium | concern |
| Code / data / version | Exact paper versions and PDF hashes are locked; T4 code mapping was not requested. | source_identity_ledger.csv; equation_code_map.csv | low | pass for T3 |
| Cost | SPS gives training and generation times, not matched error per GPU-hour against HMC or SNF. | P001 p. 17, Table 4; p. 20 | high | concern |
| Successor evidence | P031 directly cites P001 but uses a different reverse-SDE construction. | R0199; E-260708505-M | medium | unresolved |

## Core Claims

| Claim | Supporting evidence | Counterevidence / gap | Allowed wording | Decision |
|---|---|---|---|---|
| SPS introduced path-space sampling | none | P002 and P003 predate it | do not write | reject |
| SPS was first to learn forward and backward drifts | none | P004 explicitly adapts both; P001 acknowledges this | do not write | reject |
| SPS differs from the checked predecessors by extended-space trajectory IMH | E-260613790-M; predecessor method records | no priority search over all literature | among the checked core comparators, this is the narrowest correction difference | keep |
| SPS+IMH reproduces the tested HMC observables | E-260613790-R | two-dimensional phi4 scope only | retain model, lattice scan, and corrected method | keep |
| SPS universally accelerates HMC | none | unmatched update units and GPU-hour cost | report only the paper's within-setup autocorrelation | reject |
| Independent drifts improve performance | none isolated | no controlled ablation against score-coupled drifts | design difference; performance effect open | unresolved |

## Reading Order

| Priority | Read / derive / run | Purpose | Target | Evidence risk |
|---|---|---|---|---|
| P0 | P002 Eqs. (13), (17)-(19) | lock inherited path control and weighting | T2 | low; complete |
| P0 | P003 Eqs. (8)-(11), (17)-(20) | lock OU reverse-KL branch | T2 | low; complete |
| P0 | P004 Eqs. (21)-(24) | test paired-drift novelty | T2-T3 | low; complete |
| P1 | P007 Eqs. (20)-(34) | align lattice path weighting and hybrid architecture | T2-T3 | low; complete |
| P1 | P001 Eqs. (2.2)-(2.19) | reconstruct focal training and correction | T3 | low; complete |
| P2 | matched correction and cost experiment | isolate practical benefit | Part 3 | open experiment |

## Decision

- Established: SPS combines independently parameterized Langevin path kernels,
  an unnormalized path KL, and extended-space trajectory IMH in a lattice-field
  sampler.
- Attribution boundary: path objectives, trajectory ratios, lattice stochastic
  paths, and paired drift adaptation all have checked predecessors.
- Strongest reusable delta: SPS adapts this family to lattice field theory and
  uses the full trajectory ratio as an IMH correction rather than only as an
  importance weight.
- Still open: first-ever priority, the isolated value of independent drifts or
  learned diffusion, support robustness, matched total-cost speed, and later
  adoption.
