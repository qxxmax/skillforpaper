# Venue Selection And Submission Gate

Use this reference when the user asks where to submit, how to prepare a
submission, or whether a manuscript is ready to submit (Part 5).

## Venue Profile

Before formatting anything, create `venue_profile.md` for each candidate venue
from its **current official author guidelines** (fetch and date them — venue
rules change yearly; a stale profile is a defect). Record:

- page/word limits (main text, references, appendices) and template;
- review model (double-blind, single-blind, open) and anonymization rules;
- checklist or reproducibility requirements and whether they are scored;
- code/data submission policy;
- preprint policy (arXiv allowed before/while in review);
- deadline, decision timeline, and revision model (rebuttal window vs
  major/minor revision rounds);
- scope-fit statement: one sentence on why this paper belongs at this venue,
  with the venue's own scope text quoted.

## Selection Matrix

Compare 2-4 candidate venues in one table: scope fit, audience, timeline
pressure, prestige/risk, revision model, and code policy. Record the decision
and its reason in the interaction log. Do not restart this debate after
submission unless a desk reject or scope complaint forces it.

## Submission Gate

Run this gate before every submission and record it in
`submission_package_manifest.md`. All items must pass or carry an explicit
waiver with a reason:

| gate item | check |
|---|---|
| identity | title, author list, order, affiliations, ORCIDs identical across PDF, metadata form, and arXiv version |
| anonymity | double-blind venues: no author names, acknowledgments, repo links, or self-citation phrasing ("our previous work") that deanonymizes |
| length | main text within limit after final figure placement |
| checklist | every item answered; every "yes" points to a section; every "no" justified |
| numbers | abstract/conclusion numbers match frozen sources (reference 43) |
| figures | every figure legible at print size; fonts embedded; sources recorded in the visual ledger |
| code/data | availability statement matches reality (a promised repo exists and is public or clearly marked "on acceptance") |
| references | every citation verified at C1 or better in the Part 1 ledgers; no placeholder or fabricated entries |
| cover letter | venue-specific, names the main claim, suggests/excludes reviewers only per venue policy |
| exports | PDF built from current sources per reference 31 |

## ArXiv Coordination

If posting to arXiv: post only after the numbers freeze; keep the arXiv
version in the submission package manifest; record the arXiv ID in
`research_state.md`. Version updates (v2, v3) follow the same gate — a v2
that silently changes a number the journal version states is a defect.

## After Submission

Switch the run to monitor state: record venue, submission ID, date, and
expected timeline in `research_state.md`. Reviews arriving moves the run to
reference 45 (review response loop). A desk reject moves it back to the
selection matrix with the reject reason recorded.
