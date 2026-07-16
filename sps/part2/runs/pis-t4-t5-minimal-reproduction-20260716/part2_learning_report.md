# Part 2 Technical Learning Report

Report status: `VERIFIED`

## Learning Question

Can the PIS path-control objective be followed from the checked paper, through
the official implementation, to a numerical result that can be calculated by
hand? This is the T4-T5 question. SPS is retained as the checked successor that
changes the path construction and correction mechanism, not as an executable
code target. The identities are locked by E-211115141-I and E-260613790-I.

## Lineage Learning Path

| Order | Object | What it supplies | Checked anchor |
|---|---|---|---|
| 1 | PIS, P002 | Controlled path, path KL objective, trajectory weight, and official code | PDF pp. 3-6, Eqs. (2), (13), (14), and (17); E-211115141-M |
| 2 | SPS, P001 | Paired forward/backward path measures and trajectory IMH correction | PDF pp. 5-9, Eqs. (2.2)-(2.19); E-260613790-M |
| 3 | Code branch | PIS can proceed to T4-T5; SPS v1 stops at an unavailable-code record | PIS PDF p. 9, Sec. 5; SPS PDF p. 21, Sec. 4; E-211115141-L; E-260613790-L |

The learning path is therefore paper-to-code for PIS and paper-to-boundary for
SPS. An unavailable branch is a checked result, not a cue to infer an
implementation.

## Core Technical Difference

PIS learns one controlled forward stochastic process and corrects imperfect
control or time discretization with trajectory importance weights. SPS retains
path-space learning but introduces learned forward and auxiliary backward
Langevin dynamics, then uses a trajectory-level independence
Metropolis-Hastings transition. The formulas supporting this comparison are
PIS Eq. (17), PDF p. 6, and SPS Eqs. (2.18)-(2.19), PDF pp. 7-9
(E-211115141-M; E-260613790-M). This is a mechanism comparison; it is not a
claim that the two papers used comparable benchmarks.

## Technical Mechanism

1. PIS starts from an easy initial distribution and evolves a controlled
   stochastic path, PDF p. 3, Eq. (2), E-211115141-M.
2. It trains the control by combining accumulated quadratic control energy
   with the terminal target-to-prior density term, PDF pp. 4-5, Eqs. (13)-(14),
   E-211115141-M.
3. The official code stores the running control energy as an extra state
   component; `loss_pis` adds its mean to target NLL minus prior NLL.
4. At generation time, the code also accumulates the stochastic-work term used
   by the trajectory importance correction, PDF p. 6, Eq. (17),
   E-211115141-M.

## Formula and Assumptions

| Formula | Role | Assumption or boundary | Source |
|---|---|---|---|
| $dx_t=u_tdt+dw_t$ | Controlled proposal path | Target energy is evaluable up to normalization | PIS PDF p. 3, Eq. (2), E-211115141-M |
| $D_{KL}(Q^u\Vert Q^*)=E[\int \frac12\lVert u_t\rVert^2dt+\log(\mu^0(x_T)/\mu(x_T))]$ | Training objective | The path-measure construction and terminal density ratio are well defined | PIS PDF p. 4, Eq. (13), E-211115141-M |
| $w^u=dQ^*/dQ^u$ | Weighted correction | The proposal path measure covers the target path measure | PIS PDF p. 6, Eq. (17), E-211115141-L |
| trajectory IMH ratio | SPS exactness gate | The proposal covers target support | SPS PDF pp. 7-9, Eqs. (2.18)-(2.19), E-260613790-L |

The PIS paper also states that policy quality, time discretization, training,
and hyperparameters remain practical limits, PDF pp. 5 and 9,
E-211115141-L.

One implementation detail is visible only after reading the code: `loss_pis`
divides both objective terms by `y1.shape[1]`, the width of the augmented state
including the regularizer channel. PIS Eq. (13) does not specify this
normalization. It rescales the fixed objective uniformly here; the present test
records it without treating it as a paper-level claim.

## Algorithm and Implementation

| Step | Paper object | Official code at locked commit |
|---|---|---|
| 1 | Controlled SDE, Eq. (2) | `src/models/pis_nn.py`: `PISNN.f`, `PISNN.g` |
| 2 | Quadratic control energy, Eq. (13) | `src/models/loss.py`: `quad_reg` |
| 3 | Terminal target/prior term, Eqs. (13)-(14) | `src/models/loss.py`: `loss_pis` |
| 4 | Training call | `src/models/base_model.py`: `BaseModel.training_step`; `configs/experiment/ou.yaml` |
| 5 | Weight terms, Eq. (17) | `PISNN.step_with_uw`; `src/utils/sampling.py`: `generate_samples_loss` |

Repository: https://github.com/qsh-zh/pis. Locked commit:
`c1cbc1f3f28f69aa001df44762fb919de5804ebb`. The code map records file hashes,
symbols, configuration, tests, and boundaries row by row.

## Evidence and Benchmarks

The T5 run uses fixed tensors. For control increment $(3,4)$, the official
`quad_reg` function returns
$\frac12(3^2+4^2)=12.5$. For two synthetic terminal states, the official
`loss_pis` function returns:

| Quantity | Observed | Hand-checked value | Status |
|---|---:|---:|---|
| regularization term | 3.0 | 3.0 | pass |
| target NLL term | 5.0 | 5.0 | pass |
| prior NLL term | 0.0 | 0.0 | pass |
| total objective | 8.0 | 8.0 | pass |

The locked commit and `loss.py` SHA-256 also pass. These observations are
stored in `reproduction_output.json`. They test the formula-to-code mapping;
they do not reproduce the experiments reported in PIS Sec. 4, PDF pp. 6-9,
E-211115141-R, or the SPS lattice results in Sec. 3, PDF pp. 9-20,
E-260613790-R.

## Technical Review

- **Validity checked:** the implemented objective has the same control-energy
  plus terminal-density decomposition as PIS Eq. (13).
- **Implementation detail:** `loss_pis` normalizes by the augmented state
  width. This code-level scaling is separate from the paper formula.
- **Correction boundary:** the objective calculation is not itself the
  trajectory importance estimator; that requires the additional stochastic
  work accumulated during generation, PIS PDF p. 6, Eq. (17).
- **Reproducibility checked:** repository, commit, source hash, command,
  environment, output, and output hash are recorded.
- **Not checked:** network training, paper benchmark values, seed sensitivity,
  throughput, and SPS implementation.
- **Environment note:** the official project declares an older dependency
  stack. The formula-level module imports with Python 3.9.6 and torch 2.7.0;
  that does not establish compatibility of the full training pipeline.

## Checked Difference

The comparison supports three precise statements:

1. Both methods train in path space, but their learned path constructions
   differ, PIS PDF pp. 3-5 and SPS PDF pp. 5-7.
2. PIS uses trajectory importance weighting whereas SPS uses trajectory IMH,
   PIS PDF p. 6, Eq. (17), and SPS PDF pp. 7-9, Eqs. (2.18)-(2.19).
3. PIS has an official code branch available for T4-T5 at this cutoff; SPS v1
   explicitly defers code and data release, PIS PDF p. 9 and SPS PDF p. 21.

`innovation_delta.csv` preserves the exact statement layer, evidence IDs, and
reasoning for each comparison.

## Learning Status

| Gate | Demonstrated ability | Supporting artifact | Status |
|---|---|---|---|
| T0 | Lock papers, official repository, commit, and source identity | contract; code_source_ledger.csv | pass |
| T1 | Explain the PIS objective, correction, and SPS successor difference | this report; reading records | pass |
| T2 | Align core formulas, assumptions, and boundaries | Formula and Assumptions; equation_code_map.csv | pass |
| T3 | Reconstruct training and weighted-generation steps | Algorithm and Implementation | pass |
| T4 | Trace equations to official files, symbols, and configuration | equation_code_map.csv | pass |
| T5 | Execute and verify one fixed objective calculation | reproduction_output.json; minimal_reproduction_report.md | pass |

## Teach Back

PIS turns sampling into learning a stochastic path. Its training loss pays for
the control used along the path and for disagreement between the terminal
sample and the target relative to the prior. In the official code, those are
the accumulated regularization state and `sample_nll - prior_nll`. The small
test proves that this decomposition is implemented as read. It does not prove
that training succeeds on a benchmark. SPS is learned next as a successor that
changes both the bidirectional path model and the final exactness mechanism.

## Boundaries and Open Questions

- No PIS network was trained and no table or figure from the paper was
  reproduced.
- No PIS-to-SPS performance ranking is made because their reported tasks and
  compute accounting differ, PIS PDF pp. 6-9 and SPS PDF pp. 9-20.
- SPS v1 cannot pass a public code mapping at the cutoff because the paper says
  code and data will be released later, SPS PDF p. 21, E-260613790-L.
- Weight variance, support coverage, scaling near criticality, and matched
  compute comparisons remain Part 3 experiment questions rather than Part 2
  learning claims.
