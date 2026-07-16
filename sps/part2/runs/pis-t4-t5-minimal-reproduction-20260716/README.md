# PIS T4-T5 Minimal Reproduction

This package extends the completed SPS T0-T3 learning run with a code-available
case from the same checked lineage. It locks the official PIS repository,
maps paper formulas to code, and executes a small objective-level reproduction.

| Item | Recorded result |
|---|---|
| PIS paper | arXiv:2111.15141v2 |
| Official code | `https://github.com/qsh-zh/pis` |
| Locked commit | `c1cbc1f3f28f69aa001df44762fb919de5804ebb` |
| T4 | four formula roles mapped to files, symbols, and config |
| T5 | fixed-tensor PIS objective check passed |
| SPS code branch | unavailable in v1; the paper promises a future release |

## Actual T5 output

| Quantity | Hand calculation | Official code | Status |
|---|---:|---:|---|
| quadratic control cost | 12.5 | 12.5 | PASS |
| regularizer contribution | 3.0 | 3.0 | PASS |
| target NLL contribution | 5.0 | 5.0 | PASS |
| total objective | 8.0 | 8.0 | PASS |

The test is deliberately small. It checks the implementation of the objective
decomposition, not the numerical results or efficiency claims in the paper.

## Formula-to-code preview

| Paper object | Official implementation | Check status |
|---|---|---|
| Eq. (2), controlled path | `PISNN.f`; `PISNN.g` | source traced |
| Eq. (13), path objective | `quad_reg`; `loss_pis` | executed and hand checked |
| Eq. (14), training step | `BaseModel.training_step`; OU config | source traced |
| Eq. (17), trajectory weight | `step_with_uw`; `generate_samples_loss` | source traced |
| SPS Eqs. (2.18)-(2.19), trajectory IMH | no public SPS v1 code | unavailable at cutoff |

The complete row-level map is in
[`equation_code_map.csv`](equation_code_map.csv). It also records an
implementation-only normalization in `loss_pis` and keeps it separate from the
paper formula.

## Main files

| File | Purpose |
|---|---|
| [`equation_code_map.csv`](equation_code_map.csv) | paper equation to code/config chain |
| [`minimal_reproduction_report.md`](minimal_reproduction_report.md) | command, calculation, result, and boundary |
| [`reproduction_output.json`](reproduction_output.json) | machine-readable observed output |
| [`cross_case_validation.csv`](cross_case_validation.csv) | SPS unavailable-code branch versus PIS tested-code branch |
| [`part2_validation.json`](part2_validation.json) | package validator result |

Third-party source code is not copied into this repository. The script expects
a separately cloned official PIS repository at the locked commit.
