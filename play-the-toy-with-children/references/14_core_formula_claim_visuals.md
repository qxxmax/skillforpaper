# Core Formula And Claim Visuals

Use this reference when the project has formulas, mechanisms, estimators,
models, or a central conceptual contribution that should become a figure,
poster panel, or slide.

## Formula Triage

Classify each formula:

- Core formula: needed to understand the contribution.
- Diagnostic formula: needed to know when to trust the result.
- Boundary formula: explains why the claim is limited.
- Intermediate derivation: useful in appendix or backup slides, not the hero.

For each formula, record:

- what object it defines
- what claim it supports
- what evidence checks it needs
- whether it belongs in paper body, backup, poster, or appendix

## Visual Forms

Use these patterns:

- Core formula card: one formula, one sentence, one claim.
- Process strip: `input -> method -> formula -> diagnostic -> output`.
- Claim-evidence panel: claim, figure/table/formula, scope boundary.
- Diagnostic gate: metric, threshold or qualitative rule, pass/borderline/fail.
- Boundary card: what the current evidence does not support.

## Learned Sampler Pattern

For learned sampler, path, transport, flow, diffusion, or importance-sampling
work, the default visual contract is:

```text
target density -> learned path/protocol -> exact weight -> diagnostic gates -> bounded claim
```

Common formula cards:

- Jarzynski or free-energy equality.
- Path/AIS log weight.
- Effective sample size.
- Jensen gap or work variance.
- Domain-specific observable gate.

For learned nonequilibrium samplers, do not reduce the poster formula center to
only target density, final weight, and ESS.  Show the three formula layers:

1. Path law / transition kernels:
   `Q_theta(Gamma)=pi_0(x_0) prod_t K_{theta,t}(x_{t+1}|x_t)`.
2. Local increment to cumulative work/log weight:
   `log w(Gamma)=sum_t[log gamma_{t+1}(x_t)-log gamma_t(x_t)]=-W(Gamma)`.
3. Estimator and trust gate:
   `Delta F_hat=-log mean_i exp[-W(Gamma_i)]` and
   `ESS=(sum_i w_i)^2/sum_i w_i^2`.

If the learned kernel is stochastic and not a standard AIS-invariant update,
include a compact forward/backward-ratio note in the figure or backup:
`log w = target/action terms + sum_t log K^-_t / K^+_t`.

## Poster-Safe Math

Use compact formulas that render reliably.  If a formula contains fragile LaTeX
macros or uncommon symbols, use poster-safe notation first and render
camera-ready formula images in a later polish pass.

Do not let exact typography block diagnosis.
