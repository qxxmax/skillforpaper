# Funding Proposal From Literature And Experiment Ladder

Use this reference when a user wants a grant, fellowship, seed-funding,
internal-funding, or project proposal built from an existing literature scan,
slide deck, paper direction, or early experimental idea.

## Core Rule

Do not start with generic "AI for X" or "new method for Y" language. Start
with the controllable scientific object:

```text
measurement object -> bottleneck / perturbation -> inference/control object
-> staged validation -> deliverable
```

The proposal should make the experimental path visible before it makes broad
impact claims.

## Required Inputs Or Inferred Inputs

Collect or infer:

- target funder, call, page limit, deadline, and review criteria
- one-sentence ask
- field object: spectrum, dataset, instrument, model, sample, target density,
  patient cohort, corpus, or mechanism
- current literature ledgers: literature matrix, gap ledger, claim/evidence
  ledger, lineage map, and sentence/result bank
- candidate experimental ladder: simplest test, intermediate test, main
  benchmark, transfer/stress test
- baselines that a reviewer will expect
- what is preliminary evidence and what is only proposed
- what claim must remain conditional until simulation, extraction, or
  experiment is performed

If the literature ledgers are missing, run the full literature scan gate before
drafting polished proposal prose.

## Proposal Spine

Create this spine before writing full prose:

| Element | Required content |
|---|---|
| Title | narrow object + method + domain |
| Ask | what funding/support enables |
| Problem | concrete bottleneck before any method is introduced |
| Gap | what existing literature solves and what remains open |
| Hypothesis | testable claim, not a slogan |
| Aim 1 | model or measurement object |
| Aim 2 | method/controller/inference design |
| Aim 3 | staged validation and stress test |
| Baselines | direct comparator list |
| Metrics | acquisition cost, accuracy, fidelity, calibration, transfer, or field-specific equivalents |
| Risks | failure mode, detection signal, alternative path |
| Deliverables | data, code, spectra, protocol, benchmark, software, paper, or deck |

## Experiment Ladder Pattern

For experimental proposals, define a ladder:

1. **Console / instrument-only / simulation-only check**: calibrate control
   variables, latency, drift, or target conventions.
2. **Minimal observable**: one-line, two-line, toy dataset, tiny molecule,
   single benchmark, or low-dimensional target.
3. **Intermediate complexity**: enough structure to test identifiability,
   multi-feature behavior, or baseline separation.
4. **Main benchmark**: the proposed publishable or fundable target.
5. **Transfer / stress test**: changed sample, geometry, split, molecule,
   perturbation, instrument, distribution, or user condition.

Do not hard-code a named main benchmark until literature evidence, simulation,
or local data supports it. Phrase it as a target complexity class when needed.

## Bayesian / Data-Driven Controller Pattern

When the proposal uses Bayesian, ML, ensemble, active-learning, or data-driven
control:

- Define the hidden state or parameter vector.
- Define the observation features.
- Define the prior, likelihood, surrogate, or posterior update.
- Define the next-action rule.
- Define uncertainty calibration as a measured deliverable.
- Include a fallback or diagnostic action when uncertainty is high.
- Compare against direct baselines, not only against manual tuning.

Allowed wording:

> The controller estimates the perturbation direction and proposes the next
> compensation action with uncertainty.

Avoid wording:

> The model solves the instrument-control problem.

## AI / Empty-Prose Cleanup Gate

Before converting to TeX or PDF, run a Markdown-only cleanup pass:

- remove self-referential workflow narration
- replace "generic AI" framing with object-specific scientific language
- remove repeated "will" constructions where present-tense method statements
  are clearer
- replace defensive "this is not..." language with affirmative scope
- delete filler such as "important to note", "pivotal", "groundbreaking",
  "delve", "holistic", and "cutting-edge"
- check that every broad sentence points to an aim, method, metric, source, or
  deliverable
- keep unsupported claims in the risk or future-work section

Generate a `proposal_ai_quality_audit.md` recording what was changed and what
still needs evidence.

## TeX / PDF Gate

Only move to TeX/PDF after the Markdown passes:

- proposal spine is stable
- aims are not changing
- claim/evidence ledger is current
- references have DOI or primary-source URLs where possible
- placeholders are in private notes, not audience-facing text

For TeX, use UTF-8 and a Unicode-capable engine when the proposal contains
Chinese or mixed-language titles.

