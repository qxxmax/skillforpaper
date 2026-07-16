# Literature To Artifact Compiler

Use this reference after the literature matrix, reviewer-comparison matrix, gap
ledger, claim/evidence ledger, and sentence/result bank exist or are explicitly
marked unchanged.

## General Rule

Do not rewrite polished prose first.  Compile the literature loop into the
target artifact's argument structure, then polish language.

## Proposal Compiler

Convert literature outputs into:

- Field problem paragraph.
- Existing approaches paragraph.
- Gap paragraph.
- Innovation paragraph.
- Feasibility/evidence paragraph.
- Risk and mitigation paragraph.
- Reviewer-objection answers.

The proposal version must separate correctness mechanism, efficiency mechanism,
proposal geometry, diagnostics/failure mode, and scope limitation when those
roles exist in the project.

## Slides Compiler

Create a storyboard before generating PPTX/Beamer/PDF.  If an existing deck
style is provided or requested, first read
`26_slide_style_extraction_and_storyboard.md` and produce a style profile,
author intake, visual source ledger, and equation/notation audit.

Before slide drafting, create an internal evidence path in `slide_framework.md`.
For each route segment, record:

- Question or decision the segment answers.
- Evidence object: paper figure, local result, formula, table, protocol detail,
  or source slot tracked outside the audience-facing slide.
- Why this segment comes before the next one.
- Which later claim depends on it.

The first main-line deck section should give the audience a concise table of
contents / agenda immediately after the title.  Do not place the full internal
question-evidence-order table on screen by default; it belongs in
`slide_framework.md`, speaker notes, or backup unless the talk is explicitly
about the evidence-audit workflow.

For each slide, record:

- Main claim.
- Literature hook.
- Our contrast.
- Visual.
- Source/evidence.
- Formula(s), if any.
- Citation(s).
- Speaker note.
- Likely audience question.
- Backup slide needed.

After a draft exists, do not treat polish as a single pass.  Run and record
named polish rounds.  A mature research deck usually needs at least:

- Evidence round: confirm every technical page is grounded by a paper figure,
  result number, protocol detail, or formula.  If a source is unavailable,
  record it in the ledger/status file rather than presenting a missing-source
  placeholder as slide content.
- Prose round: remove generic, repetitive, or workflow-meta language
  from the audience-facing slides.
- Visual emphasis round: use red or other alert color only for core claims,
  key numbers, comparison caveats, and terms the speaker must point to.
- Logic audit round: make a slide-by-slide record of what each page explains,
  why it is in that position, and whether the page is clear.
- Readability / word-economy round: check final rendered pages for paper-figure
  label size, image legibility, and redundant prose.  Replace unreadable whole
  figures with source-grounded crops or zoom panels, and shorten bottom-line
  boxes, risk notes, and table text until only slide-essential words remain.
- Keyword-question / audience-comprehension round: ask what a listener needs to
  understand for each important keyword before the next slide can be read.  Add
  compact checkpoint slides or table rows only for terms whose absence would
  break the logic; leave minor details for speaker notes or backup.
- Hard de-bloat round: when the deck still reads wordy, remove process
  language, repeated caveats, generic bottom lines, and redundant checkpoints.
  Preserve scientific evidence and key definitions, not the scaffolding used to
  create them.

Use one claim per slide.  If a literature figure or local result is too dense,
split it into multiple slides rather than shrinking it into unreadable form.

Acceptance tests:

- One main claim per slide.
- Every literature slide has citation anchors.
- Every result slide has a source figure, table, or value; unavailable metrics
  are tracked outside the audience-facing slide.
- No audience-facing slide contains internal process notes.
- Every limitation or failure-mode slide has a diagnostic or boundary
  statement.
- Every non-original visual appears in `visual_source_ledger.md`.
- Every displayed formula appears in `equation_notation_audit.md`.

## Paper Introduction Compiler

Compile into:

- Field context.
- Pain point.
- Prior approach clusters.
- Missing mechanism or evidence gap.
- This paper's contribution.
- Evidence preview.
- Scope boundary.

Avoid writing related work as a bibliography dump.  Each paragraph should
answer why the current project exists.

## Rebuttal Compiler

Compile into:

- Reviewer concern.
- Relevant literature or baseline.
- Our evidence.
- Proposed paper change.
- Boundary or concession.

Never promise new experiments, proofs, or claims unless the user has approved
and the evidence exists.

## Cover Letter / Editor Pitch Compiler

Compile into:

- One-sentence contribution.
- Field fit.
- Why this venue or audience.
- Main evidence.
- Claim boundary.
- Conflict with possible prior work and why it is resolved.

## Output Contract

For any artifact compiler, return:

- Artifact spine.
- Source rows used.
- Sentence/result bank entries used.
- Claim/evidence ledger changes.
- Risks and unresolved citations.

When the artifact becomes proposal text, slides, paper prose, rebuttal, or a
cover letter, also maintain a trace table:

| Artifact claim | Literature source | Local evidence | Risk | Final location |
|---|---|---|---|---|
