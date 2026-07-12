# Literature Quality Gate Checklist

Use this checklist before promoting literature-derived content into proposal,
slides, paper introduction, rebuttal, cover letter, or abstract prose.

## Required For Any Literature Loop

- Literature matrix exists.
- Citation status is marked for every source.
- Unverified citations are marked, not hidden.
- No fabricated references, claims, venues, DOI values, or arXiv IDs.
- Screenshot policy is recorded.
- Sources used for claims have primary or authoritative pages.

## Required For Full Scan

- Token policy and search budget contract exist.
- Search scope exists, or the scan explicitly states why no high-recall
  optimization layer was needed.
- Search route log exists and includes at least two independent route families,
  or explains why only one route was possible.
- Candidate screening table exists for reviewed items, with include / exclude /
  uncertain labels and short reasons.
- Coverage/stopping report exists and records seed recall, route overlap,
  facet saturation, residual-risk estimate or reason unavailable, and the stop
  decision.
- Green-check evidence marks, if used, are backed by relevance, provenance,
  quality, and contribution gates.
- Reviewer-comparison matrix exists.
- Lineage snowball map exists.
- Gap ledger exists.
- Claim/evidence ledger is updated or explicitly marked unchanged.
- Literature snapshot is frozen.
- Author/lab/method-lineage pass was performed:
  - same author or same lab follow-up work
  - same research circle or shared platform/instrument work
  - same method-family work by other groups
  - citing works that change novelty or reviewer risk
  - older papers by the same group that explain motivation or infrastructure
- Adversarial search pass was performed:
  - same method but older
  - negative result
  - scaling limitation
  - contradictory benchmark/dataset
  - review paper with different framing
- Stop conditions are satisfied or remaining gaps are named.

## Artifact-Specific Checks

Proposal:

- Every main claim has source or local evidence.
- Novelty is expressible in one sentence.
- Explicit limitations are present.
- Milestones and deliverables are present.
- Comparison to prior work is present.
- Risks and mitigation are present.

Slides:

- Each slide has one claim.
- Each figure has a take-home caption.
- Formulas are central and not decorative.
- Speaker notes cover what the slide omits.
- Backup slides answer likely questions.

Paper introduction:

- Abstract/intro claims align with results.
- Related-work gap aligns with cited literature.
- Contribution wording does not overclaim beyond evidence.
- Discussion/conclusion boundaries match diagnostics and limitations.

Rebuttal:

- Every reviewer concern is mapped to evidence, source, or concession.
- No new experiment/proof is promised without approval.
- Changes promised in rebuttal are trackable.

## Quality Gate Output

Return a pass/fail table:

- Gate item
- Status: pass / fail / not applicable / deferred
- Evidence file or source row
- Action needed

Do not proceed to polished prose if a required gate fails unless the user
explicitly asks for a draft with visible placeholders and risk labels.
