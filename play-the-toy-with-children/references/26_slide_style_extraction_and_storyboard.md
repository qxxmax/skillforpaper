# Slide Style Extraction And Storyboard Workflow

Use this reference when the user asks to build, polish, reorganize, or generate
slides from an existing deck style, a manuscript, a proposal, a literature
review, or a claim/evidence ledger.

## Purpose

This workflow turns a reference deck into reusable presentation grammar.  It is
not visual mimicry.  Extract the author's slide style, confirm the scientific
story with the author, ground every slide in evidence, audit formulas and
notation, and only then generate Beamer, PPTX, Quarto, or PDF artifacts.

## Intake Gate

Ask or infer:

- deck target: 5 min pitch, 20 min talk, 40 min seminar, 60 min tutorial,
  expert talk, proposal defense, group meeting, rebuttal/defense, or teaching
  deck;
- audience level: broad scientific, field-adjacent, same-field expert,
  committee/panel, students, or reviewers;
- source style: PDF, PPTX, Keynote, Beamer, image renders, institution
  template, or no reference style;
- source grounding: none, local-only, key citations, or full
  literature-backed deck;
- visual policy: author-owned figures, redrawn paper-figure schematics,
  direct paper figures with provenance, generated visuals, or official-source
  search when missing;
- formula depth: conceptual, moderate, expert, or backup-only;
- output target: storyboard only, Beamer/LaTeX, PPTX, Quarto/HTML, PDF, or
  multiple variants.

Do not generate a final deck before creating or updating:

- `slide_style_profile.md`;
- `author_slide_intake.md` or an explicit inferred-intake note;
- `slide_framework.md` and slide-by-slide storyboard;
- `visual_source_ledger.md`;
- `equation_notation_audit.md`;
- claim/evidence ledger update or explicit unchanged marker;
- `slide_quality_gate_checklist.md` before export.

## Hard Rules

1. Extract style tokens and layout grammar first; do not copy the reference
   deck's content blindly.
2. Every slide must have one main claim, one visual plan, and one
   source/evidence entry.
3. Every literature visual must be recorded in a visual source ledger with
   source, figure/table/equation number when available, verification status,
   citation text, and reuse/redraw policy.
4. Prefer redrawn schematic/vector versions of copyrighted paper figures unless
   the user owns the figure or explicitly chooses direct figure reuse.
5. Every displayed nontrivial formula must have a canonical LaTeX entry in the
   equation/notation audit.
6. If a figure, formula, result, or citation cannot be verified, mark it
   `unverified` and keep it out of final public slides.
7. Before export, audit typography, notation, subscripts/superscripts, Greek
   letters, units, signs, constants, punctuation, capitalization, hyphenation,
   citation formatting, and backup coverage.
8. Build from source.  Do not edit PDFs directly unless the user explicitly
   requests that path.

## Workflow

### Round 0 - Style Intake

Inspect the reference deck multimodally when possible.  Extract:

- aspect ratio and page size;
- title slide, outline, section divider, summary, and backup patterns;
- header, footer, citation, and page-number style;
- approximate typography and font hierarchy;
- color tokens and their semantic use;
- formula, table, plot, arrow, box, and diagram style;
- progressive reveal or overlay strategy;
- backup labels and backup roadmap conventions.

Output `slide_style_profile.md`.  For reusable implementation, also create
`style_tokens.yaml` when useful.

### Round 1 - Author Intake

Before writing slides, confirm or infer:

- talk goal and one-sentence thesis;
- audience, duration, language, and formula tolerance;
- must-include results, formulas, figures, and citations;
- must-avoid sources or overclaims;
- whether literature lineage/taxonomy belongs in the main line;
- desired number and depth of backup slides;
- figure policy: direct reuse, redraw, generated schematic, or official-source
  search.

Output `author_slide_intake.md`.

### Round 2 - Story Architecture

Build the framework before slide-by-slide details.

- Tutorial: motivation -> basics -> method -> evidence -> limitations ->
  outlook.
- Expert talk: thesis -> direct baselines -> method distinction ->
  diagnostics/ablations -> limitations -> future work.
- Proposal talk: bottleneck -> gap -> innovation -> evidence -> aims ->
  risks/mitigation.
- Paper talk: problem -> method identity -> main results -> diagnostics ->
  scope boundary -> take-home.

Output `slide_framework.md`.

### Round 3 - Slide Storyboard

For each slide record:

- slide ID and title;
- main claim;
- audience level;
- visual plan;
- exact source/evidence;
- formulas required;
- citations;
- speaker note;
- backup link;
- risk or likely audience question.

Do not generate Beamer/PPTX until the storyboard is approved or the user asks
to proceed despite open items.

### Round 4 - Source Visuals And Formulas

For visuals:

1. Check local author-owned figures first.
2. Check manuscript, supplement, claim/evidence ledger, and result folders.
3. Check must-cite papers for exact figure/table/equation numbers.
4. Record official page, DOI/arXiv/URL, screenshot or extraction path, caption
   summary, and permission/copyright status.
5. If direct reuse is unsuitable, redraw the concept as a schematic or recreate
   a simple plot from allowed data.
6. If no verified source exists, search official or authoritative sources and
   leave the visual out of final slides until verified.

Output `visual_source_ledger.md`.

For formulas:

1. Create canonical LaTeX.
2. Record meaning, units/domain, source, and first slide introduced.
3. Define notation once and reuse it consistently.
4. Move long derivations into backup unless the audience requires them.

Output `equation_notation_audit.md`.

### Round 5 - Build Deck Source

Use the output target:

- Beamer/LaTeX for formula-heavy decks.
- PPTX for broad talks or collaborative editing.
- Quarto/Reveal/HTML for web-first talks.

If the user wants the style of an existing PDF deck, recreate the visual
grammar in a source theme or PPT master rather than editing the PDF.

### Round 6 - Quality Gate

Before export, verify:

- every slide has one main claim and one evidence source;
- every claim maps to the claim/evidence ledger or explicit assumption;
- every formula compiles and uses consistent notation;
- all non-original visuals have provenance and reuse/redraw status;
- no screenshot includes excessive copyrighted article text;
- citations are real and not fabricated;
- text is readable, not overloaded, and not overlapping;
- backup slides answer likely expert questions;
- variants share the same claim/evidence ledger and notation audit.

Output `slide_quality_gate_checklist.md`.

## Multi-Version Deck Generation

When one topic needs multiple talks, create a shared slide bank and compile
variants:

- `20min`: minimal background, core method, 2-3 results, claim boundary.
- `40min`: balanced background, method, literature, evidence, outlook.
- `60min`: tutorial, method, full literature lineage, extended backup.
- `expert`: direct baselines, equations, diagnostics, limitations, reviewer
  risk, and Q&A backup.

All variants use the same claim/evidence ledger, visual ledger, and notation
audit.

## Deliverables

A complete style-to-slides run should produce:

- `slide_style_profile.md`;
- `author_slide_intake.md`;
- `slide_framework.md`;
- `slide_storyboard_[duration_or_audience].md`;
- `visual_source_ledger.md`;
- `equation_notation_audit.md`;
- `claim_evidence_ledger_update.md` or unchanged marker;
- `slide_quality_gate_checklist.md`;
- final source deck (`.tex`, `.pptx`, `.qmd`, etc.);
- exported deck and preview renders when requested.

