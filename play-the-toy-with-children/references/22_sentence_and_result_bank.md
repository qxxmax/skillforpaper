# Sentence And Result Bank

Use this reference after a literature loop when the next task is proposal
background, related work, slides, rebuttal, abstract, cover letter, or figure
caption writing.

## Purpose

The literature matrix is not enough.  Convert verified sources and local
evidence into reusable, claim-safe sentences that can be reused across
artifacts without changing the meaning.

## Bank Entries

Each sentence/result entry should record:

- Sentence type: background, related work, gap, method distinction,
  correctness/trust, result, limitation, future work, reviewer response, slide
  one-liner, or figure caption.
- Sentence.
- Support: source row, local figure/table, formula, or explicit assumption.
- Claim strength: established / supported-local / plausible / speculative.
- Risk: overclaim, stale source, missing baseline, weak evidence, or audience
  confusion.
- Forbidden expansions.
- Artifact location: proposal, slides, paper intro, rebuttal, cover letter,
  abstract, caption, or backup.

Use `templates/sentence_result_bank_template.md` when creating a file artifact.

## Claim-Safe Examples

For Jarzynski-corrected learned-transport/free-energy work:

- Prefer: "Path-space reweighting supplies the normalization correction, while
  nESS and maximum-weight diagnostics monitor finite-sample overlap."
- Avoid: "unbiased free-energy estimator" unless the sentence explicitly
  distinguishes an unbiased partition-function-ratio estimator before the log
  from a consistent but finite-sample-biased log free-energy estimate.
- Prefer: "direct free-energy estimates in the resolved-overlap regime."
- Avoid: "solves large-volume overlap" or "replaces HMC generally."

For fixed-target VMC / endpoint-SNIS work:

- Prefer: "The method is a fixed-target independent endpoint sampler for
  real-space VMC."
- Prefer: "Correctness is supplied by endpoint SNIS under the stated support
  and integrability conditions."
- Prefer: "Training improves efficiency by reducing work or weight
  fluctuations."
- Avoid: "optimizes the wavefunction", "produces exact samples", "solves
  nodal sampling", or "chemical-accuracy benchmark" unless the source evidence
  explicitly supports that narrower claim.

## Promotion Rule

Do not promote a sentence into polished artifact prose unless its support row,
claim strength, and forbidden expansions are recorded.  If a useful sentence is
not yet supported, keep it in the bank as "draft unsupported" rather than
placing it into proposal/slides/paper text.
