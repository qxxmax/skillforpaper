# Part 2 Technical Review

Review status: `READY`

## Entry Check

- PIS is locked as P002, arXiv:2111.15141v2, with checked identity and full
  text: E-211115141-I.
- SPS is locked as P001, arXiv:2606.13790v1, as the checked successor context:
  E-260613790-I.
- The official PIS repository is `https://github.com/qsh-zh/pis` at commit
  `c1cbc1f3f28f69aa001df44762fb919de5804ebb`.
- SPS v1 states that code and data will be made public in a future version,
  PDF p. 21, Sec. 4, E-260613790-L.

## Method Comparison

| Question | Checked answer | Source |
|---|---|---|
| What is inherited? | Data-free stochastic path learning from an easy prior toward an unnormalized target | PIS PDF pp. 3-5, E-211115141-M; SPS PDF pp. 3-7, E-260613790-M |
| What changes? | One controlled forward path becomes paired learned forward/backward path measures | PIS PDF p. 3, Eq. (2); SPS PDF pp. 5-6, Eqs. (2.2)-(2.8) |
| How is residual error handled? | PIS uses trajectory weights; SPS uses trajectory IMH | PIS PDF p. 6, Eq. (17); SPS PDF pp. 7-9, Eqs. (2.18)-(2.19) |
| Are benchmark values directly comparable? | No; tasks, baselines, observables, and cost accounting differ | PIS PDF pp. 6-9, E-211115141-R; SPS PDF pp. 9-20, E-260613790-R |

## Validity And Reproducibility

The fixed-tensor check executes the official PIS functions rather than a
reimplementation. It locks the Git commit and source hash before evaluating
the expected values. All four machine checks pass. The test establishes that
the read objective decomposition maps to the current official source; it does
not establish optimizer convergence, benchmark reproduction, or general
sampler validity.

`loss_pis` divides both the accumulated regularizer and terminal density term
by the augmented state width. The paper's Eq. (13), PDF p. 4,
E-211115141-M, does not prescribe this implementation normalization. It is
recorded as a code-level scaling rather than silently folded into the paper
formula.

Full repository installation was not used as evidence. The public project
declares an older training stack, while the minimal objective module runs under
Python 3.9.6 and torch 2.7.0. Compatibility of the full pipeline therefore
remains untested.

## Core Claims

**Supported:**

- PIS Eq. (13) maps to `quad_reg` plus the terminal NLL difference in
  `loss_pis`, PDF p. 4, E-211115141-M.
- The official functions return the hand-calculated values for the fixed test.
- PIS and SPS use different trajectory-level correction mechanisms, PIS PDF
  p. 6 and SPS PDF pp. 7-9.

**Not supported:**

- The full PIS benchmark has been reproduced.
- PIS or SPS is faster under matched compute.
- The unpublished SPS implementation has a particular file or symbol layout.

## Reading Order

1. PIS PDF pp. 3-5, Eqs. (2), (13), and (14): controlled path and objective.
2. PIS PDF p. 6, Eq. (17): trajectory correction.
3. `equation_code_map.csv`: formula-to-code chain.
4. `reproduction_output.json`: machine result.
5. SPS PDF pp. 5-9, Eqs. (2.2)-(2.19): successor difference.
6. `innovation_delta.csv`: checked comparison and statement layers.

## Decision

The package passes its declared T5 formula-level target. It is suitable as the
Part 2 code-available branch test. Broader PIS training and all SPS code
reproduction remain outside the result and must not be inferred from this
pass.
