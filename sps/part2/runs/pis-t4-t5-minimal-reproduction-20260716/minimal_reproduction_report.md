# Minimal Reproduction Report

Status: `PASS`

## Question

Does the official PIS implementation compute the control-energy and terminal
density terms in the decomposition read from PIS Eq. (13), PDF p. 4,
E-211115141-M?

## Locked Inputs

| Item | Value |
|---|---|
| Repository | https://github.com/qsh-zh/pis |
| Commit | `c1cbc1f3f28f69aa001df44762fb919de5804ebb` |
| Source | `src/models/loss.py` |
| Source SHA-256 | `28fa5ab4ec8a00d9897ead9c55f66bbe0877f00d202b859181b136c05817af0e` |
| Runtime | Python 3.9.6; torch 2.7.0 |

## Public Reproduction Command

```bash
git clone https://github.com/qsh-zh/pis.git
git -C pis checkout c1cbc1f3f28f69aa001df44762fb919de5804ebb
python3 scripts/verify_pis_loss_formula.py --repo pis --output reproduction_output.json
```

The third command is run from this package directory.

## Fixed Calculation

For `dx = (3, 4)`, the expected quadratic term is
$\frac12(3^2+4^2)=12.5$. For the synthetic terminal states, the expected
decomposition is regularization 3.0 plus target NLL 5.0 minus prior NLL 0.0,
giving total loss 8.0.

| Check | Observed | Expected | Status |
|---|---|---|---|
| locked commit | exact match | exact match | pass |
| source SHA-256 | exact match | exact match | pass |
| quadratic control cost | 12.5 | 12.5 | pass |
| objective decomposition | 8.0 | 8.0 | pass |

Machine output: `reproduction_output.json`.

## Interpretation

The result closes the chain from paper formula to official function to a
hand-checkable number. It does not train the model, integrate a learned path,
compute ESS, or reproduce a paper benchmark. Those stronger statements are
outside this T5 test.
