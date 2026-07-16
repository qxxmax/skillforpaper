# Part 2 Technical Review

Review status: `BLOCKED`

## Entry Check

- [x] Focal paper and compared predecessors are identity-locked.
- [ ] All technical-core predecessors have detailed native R0-R6 records.
- [ ] Every cross-paper delta has equation- or algorithm-level anchors from
  both sides.
- [x] Relation-ledger edges used for the lineage are checked.
- [x] Author claims, source-supported synthesis, reviewer inference, and
  unresolved statements are separated.

## Method Comparison

| Dimension | Inherited component | Claimed change | Evidence that isolates it | Statement layer | Decision |
|---|---|---|---|---|---|
| objective | path-space learning for unnormalized targets in P002/P003 | SPS forward/backward path KL for a lattice target | P001 p. 6, Eq. (2.13); predecessor method anchors remain broad | source_supported_synthesis | pending exact subtraction |
| dynamics | learned stochastic path | paired forward and auxiliary backward Langevin drifts | P001 pp. 5-6, Eqs. (2.2)-(2.8) | author_claim | keep as mechanism; novelty pending |
| correction | path probabilities and nonequilibrium weighting in P007 | full-trajectory independence-MH correction | P001 pp. 7-9, Eqs. (2.18)-(2.19) | author_claim | exactness role supported; priority pending |
| benchmark | learned lattice samplers already tested on scalar systems | corrected SPS observables plus acceptance, timing, and autocorrelation | P001 Sec. 3, Tables 1-4, Fig. 8 | author_claim | benchmark-specific only |
| successor | later direct citation by P031 | possible continuation of lattice diffusion diagnostics | R0199 plus P031 method record | unresolved | do not infer adoption |

## Validity And Reproducibility

| Check | Finding | Source anchor / reasoning | Severity | Status |
|---|---|---|---|---|
| Assumptions | exact IMH correction requires proposal support | P001 pp. 7-8, Sec. 2.4; E-260613790-L | high | concern |
| Correctness / exactness | exactness belongs to the corrected SPS+IMH chain, not the uncorrected proposal | P001 pp. 7-15, Secs. 2.4 and 3 | high | pass with boundary |
| Baseline fairness | HMC validates observables, but autocorrelation update units differ | P001 pp. 18-20, Sec. 3.5 | high | concern |
| Metrics / observables | magnetization, susceptibility, free energy, acceptance, timing, and autocorrelation are reported | P001 pp. 10-20, Sec. 3 | low | pass |
| Ablations / controls | uncorrected SPS versus SPS+IMH tests the practical effect of correction | P001 pp. 10-15, Tables 1-2 | medium | pass |
| Uncertainty / sensitivity | observable tables include errors; matched total-cost uncertainty is absent | P001 Tables 1-3 and p. 20 | medium | concern |
| Code / data / version | the audit locks arXiv v1; public implementation is not established | E-260613790-I; gap G08 | medium | pending |
| Cost | SPS timings are reported without a matched HMC GPU-hour ratio | P001 p. 17, Table 4; p. 20 | high | concern |
| Successor evidence | P031 directly cites P001 but uses a different reverse-SDE setup | R0199; E-260708505-M | medium | unresolved |

## Core Claims

| Claim | Supporting evidence | Counterevidence / gap | Allowed wording | Decision |
|---|---|---|---|---|
| SPS defines paired stochastic paths and a trajectory-level IMH correction | E-260613790-M | support coverage remains a condition | state the correction and condition together | keep |
| SPS+IMH reproduces the tested HMC observables | E-260613790-R | reported 2D phi4 scope only | retain lattice, scan, and corrected method | keep |
| SPS mitigates critical slowing down | E-260613790-R; E-260613790-L | update units and total cost are unmatched | report shorter autocorrelation in the tested units | weaken |
| SPS is universally faster than HMC | none | no matched wall-time or GPU-hour comparison | do not write | reject |
| the path-space objective is uniquely new to SPS | none | P002 and P003 already supply related path-space mechanisms | leave innovation attribution pending | reject for now |

## Reading Order

| Priority | Read / derive / run | Purpose | Target | Evidence risk |
|---|---|---|---|---|
| P0 | P001 Secs. 2.2-2.4, Eqs. (2.2)-(2.19) | contains the entire operative proposal, objective, and correction | T2-T3 | low |
| P0 | align the corresponding path objectives in P002 and P003 | determines what SPS inherits and changes | T3 | medium until exact anchors are recorded |
| P1 | compare P007 path weighting/correction with P001 IMH | tests whether correction is the central delta | T3 | medium |
| P1 | P001 Sec. 3.5 plus Table 4 | separates autocorrelation from compute cost | review | low |
| P2 | inspect P031 after the focal comparison | adds later-work context | frontier context | high if overinterpreted |

## Decision

- Established: SPS uses the paired-path mechanism and trajectory-level
  correction described in P001.
- Still open: novelty rank, adoption in later work, and practical speedup.
- Read next: complete R0-R6 records for P002, P003, and P007, align their core
  equations with P001, and rerun this review.
