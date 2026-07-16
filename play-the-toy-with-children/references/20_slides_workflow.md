# Slides Workflow

Use this reference for proposal decks, conference talks, defense decks, lab
updates, teaching decks, paper walkthroughs, and PPT/PowerPoint slide planning.

## Intake

Identify:

- Audience: funders, reviewers, collaborators, students, committee, or general
  technical audience.
- Purpose: persuade, teach, report progress, defend, recruit, or decide.
- Duration, slide count, format, and delivery mode.
- Source materials: draft, paper, book, figures, code, data, literature,
  proposal, or notes.
- Required artifacts: outline only, editable PPTX, PDF, speaker notes, backup,
  or figure pack.

If the deck needs literature comparison or current context, run the iterative
literature loop first or in parallel with deck planning.

If the deck should follow the style of an existing PDF/PPTX/Beamer deck, or if
the user wants several versions of one talk, read
`26_slide_style_extraction_and_storyboard.md` before drafting.  Extract a style
profile, confirm or infer author-intake decisions, then produce the storyboard,
visual source ledger, and equation/notation audit before creating deck source.

## Deck Contract

Every main-line slide should have:

- One action title that states the claim.
- One visual anchor: figure, diagram, equation card, table, screenshot, or
  simple flow.
- One evidence source: local result, literature source, derivation, or explicit
  assumption.
- One takeaway or transition.

Do not use slides as manuscript paragraphs.  Move dense proof, derivation, and
parameter detail into backup.

## Modes

- Proposal pitch: problem, gap, thesis, aims, feasibility, risk plan, timeline,
  impact, ask.
- Conference talk: motivation, method, core formula/mechanism, evidence,
  comparison, limitation, takeaway.
- Defense deck: thesis, contribution map, methods, results, limitations,
  committee questions, backup derivations.
- Teaching deck: concept ladder, worked examples, literature figures, full
  backup calculations, symbol definitions.
- Paper walkthrough: section map, argument tree, figure-by-figure story,
  reviewer-facing boundary notes.

## Workflow

1. Build a source map of papers, local files, figures, formulas, datasets, and
   code paths.
2. Create the deck spine: 6-12 slide-level claims before writing slide text.
3. Create an internal evidence path before drafting slides: map each deck
   segment to a question, an evidence object, and a reason for the order.  Put
   this in `slide_framework.md`.
4. Add a visible table of contents / agenda near the start of the deck.  It
   should be short enough to read at a glance; do not put the full internal
   evidence-path table on the slide unless the audience needs that audit trail.
5. Choose visual anchors for each slide.  Prefer real plots, source-grounded
   diagrams, formula cards, and evidence tables over decorative imagery.
6. If a reference style is used, create `slide_style_profile.md` and apply its
   layout grammar without copying topic-specific content.
7. Create or update `visual_source_ledger.md` for every non-original figure,
   screenshot, redrawn schematic, generated visual, and local result figure.
8. Create or update `equation_notation_audit.md` for every displayed formula
   and notation convention.
9. Draft main-line slides with action titles and minimal body text.
10. Build backup: derivations, definitions, ablations, extra baselines,
   literature detail, implementation details, and risk answers.
11. Add speaker notes when the slide alone cannot carry the reasoning.
12. Render or compile the deck and inspect representative slides for layout,
   readability, equation overflow, figure resolution, citation labels, and
   accidental text overlap.
13. Run named polish rounds and record what each round changed.  Typical rounds
    are: figure/evidence grounding, audience-prose cleanup, visual
    emphasis, slide-by-slide logic audit, and readability / word economy.
14. When using red or other alert color, use it sparingly for core claims, key
    result numbers, comparison caveats, or terms the speaker must explicitly
    point to.  Do not use alert color as general decoration, and do not use it
    to mark missing PDFs, missing figures, or extraction failures on
    audience-facing slides.
15. In the readability / word-economy round, inspect every rendered page:
    figure-internal labels must be readable at presentation scale, dense paper
    figures should become focused crops or zoom slides, and every bottom-line or
    callout should lose words that do not change the talk.
16. In the keyword-question / audience-comprehension round, ask the deck's key
    terms as questions from a listener's perspective.  For each term, decide
    whether the answer belongs on a checkpoint slide, in an existing table, in
    speaker notes, or nowhere.  Add visible content only when missing the term
    would make later evidence, figures, or metrics hard to understand.
17. In the source-availability cleanup round, remove any visible placeholders
    such as "missing figure", "PDF not found", "extract later", or "insert
    original figure".  Record unavailable sources in `visual_source_ledger.md`,
    status files, speaker notes, backup, or the final progress report instead
    of making them slide content.
18. In the hard de-bloat round, remove self-referential process labels, workflow
    narration, repeated caveats, generic bottom-line boxes, and any sentence the
    speaker can say aloud.  Convert three-column explanation tables into
    two-column term/value tables when possible, and delete redundant checkpoint
    slides.

## Slide Inventory

Maintain a table:

- Slide number
- Action title
- Question answered
- Visual anchor
- Evidence/source
- Formula or concept
- Speaker note
- Backup link
- Status: draft / needs figure / needs citation / ready

## Literature And Figure Rules

- Literature figures require source captions and permission status when public
  release matters.
- If permission is uncertain, redraw the concept or use the figure only in
  internal drafts.
- Every axis, symbol, and color meaning must be explained.
- A comparison figure must say what is being compared and what conclusion the
  audience should draw.

## Quality Gates

Before finalizing:

- The deck has a visible spine, not a pile of facts.
- Every slide can be read from 1-2 meters or on a laptop screen.
- Main-line formulas are few and central; derivations live in backup.
- Figures are large enough to inspect.
- Slide titles form a coherent story if read alone.
- Claims have evidence and boundaries.
- Backup answers likely audience questions.
- Style-profile, visual-ledger, and equation-audit files exist or are explicitly
  marked unnecessary.
- `slide_framework.md` records the internal evidence path, and the visible deck
  contains a concise table of contents / agenda near the start.
- A named polish-round record exists when the deck has been revised more than
  once; it states the logic of every slide, what each page explains, what is
  emphasized visually, and whether the slide is clear.
- Any red/alert emphasis is limited to evidence-bearing claims, result numbers,
  comparison caveats, or terms the speaker must point to.
- Audience-facing slides contain no missing-PDF, missing-figure,
  extraction-failure, or "insert later" placeholders.
- Paper figures are readable at final render size.  If not, the deck uses
  source-grounded crops, zoom panels, or a separate figure-reading slide instead
  of shrinking the whole figure.
- Body text, bottom-line boxes, and boundary notes have passed a word-economy
  check: remove generic explanation, repeated caveats, and prose that a speaker
  can say aloud without putting it on the slide.
- No audience-facing slide contains internal process notes or material that
  belongs in the status record.
- Key terms have passed a keyword-question check.  If a term is required for
  following the next figure, method, or result table, the deck defines it before
  use through a compact checkpoint, table row, or figure-reading note.

## Output Contract

Return:

- Deck spine.
- Slide inventory.
- Figure/formula asset list.
- Style profile, visual source ledger, and equation/notation audit when used.
- Backup plan.
- Literature/citation status.
- Rendered or editable deck path when a file is produced.
