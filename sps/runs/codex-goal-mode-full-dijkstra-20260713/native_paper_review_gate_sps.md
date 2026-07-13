# Paper Review Gate

Paper ID: `P001 / arXiv:2606.13790v1`

Reading record: `native_paper_reading_record_sps.md`

Review status: `READY`

## Entry Gate

- [x] Identity is locked to an exact version.
- [x] Full text was read and mapped.
- [x] Method, equations, experiments, numbers, and limitations have anchors.
- [x] Paper-layer statements are separated from reviewer inference.
- [x] Missing evidence remains pending.

## Validity Checks

| Check | Finding | Source anchor / reasoning | Severity | Status |
|---|---|---|---|---|
| Assumptions | Exact IMH correction requires the SPS proposal to cover the target support. | pp. 7-8, Sec. 2.4; Appendix C | high | concern |
| Baseline fairness | HMC validates observables, but autocorrelation is reported in HMC trajectories versus IMH steps. | pp. 18-20, Sec. 3.5 | high | concern |
| Metrics | Magnetization, susceptibility, free energy, acceptance, training history, and autocorrelation are reported. | pp. 10-20, Sec. 3 | low | pass |
| Ablations / controls | Uncorrected SPS versus SPS+IMH isolates the practical effect of exact correction on tested observables. | pp. 10-15, Tables 1-2 | medium | pass |
| Uncertainty | Observable tables report statistical errors; the headline autocorrelation comparison has no matched total-cost uncertainty. | Tables 1-3; p. 20, Sec. 3.5 | medium | concern |
| Reproducibility | Architecture and training details are supplied, but this audit does not establish an independently reproducible public code release. | Appendices B-C | medium | pending |
| Cost | Training and generation times are reported for SPS, but no matched HMC GPU-hour efficiency ratio is given. | p. 17, Table 4; p. 20, Sec. 3.5 | high | concern |

## Claim Audit

| Claim | Supporting evidence | Counterevidence / gap | Allowed wording | Decision |
|---|---|---|---|---|
| SPS+IMH reproduces HMC observables in the tested scan. | E-260613790-R | Limited to the reported 2D phi4 setup. | Keep the lattice, coupling range, and corrected method explicit. | keep |
| SPS mitigates critical slowing down near the tested pseudocritical point. | E-260613790-R | Update units differ and cost is not matched. | Say the reported autocorrelation decays faster; do not state a wall-time speedup. | weaken |
| SPS is exact. | E-260613790-M; E-260613790-L | Exactness belongs to SPS+IMH under support coverage, not to the uncorrected proposal. | Attribute exactness to the correction and state the support condition. | weaken |
| SPS scales efficiently to larger or higher-dimensional systems. | E-260613790-L | Demonstrated only through $L=64$ in the stated 2D geometry; architecture size grows with volume. | Present as an open direction. | reject |

## Reviewer Questions

| Priority | Question | Why it matters | Evidence needed to close it |
|---|---|---|---|
| P0 | Does the SPS autocorrelation gain survive matched total GPU-hours including training and correction? | This controls the practical efficiency claim. | Paired HMC/SPS timing, block errors, and cost-normalized observable variance. |
| P0 | How robust is the correction when rare target regions have weak proposal support? | IMH exactness assumes support coverage and finite runs may not expose missed tails. | Tail diagnostics, sector occupancy, repeated seeds, and stress tests. |
| P1 | How do acceptance, parameter count, and total cost scale with volume and diffusion step count? | The current architecture grows with lattice extent. | Controlled scaling sweep with uncertainty and hardware metadata. |
| P1 | What changes for gauge-valued fields and topological freezing? | This is a stated scientific extension, not a demonstrated result. | Gauge-equivariant implementation and a topology-sensitive benchmark. |

## Decision

- What the paper establishes: SPS defines a data-free path-space proposal with an exact trajectory-level IMH correction and validates it on the reported two-dimensional phi4 benchmarks.
- What remains unestablished: matched end-to-end efficiency, rare-support robustness beyond the shown diagnostics, and scaling to gauge fields or higher dimensions.
- Next action: accept the paper as a core method source, retain the cost and support gaps, and request matched efficiency experiments before making a speed claim.
