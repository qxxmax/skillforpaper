# Camera-Ready Poster Rebuild Protocol

Use this reference when a poster concept, AI-generated draft, screenshot,
Matplotlib prototype, PDF poster, or rough slide must become an editable,
source-grounded, camera-ready academic poster.

## Core Principle

Treat generated poster images as blueprints, not final evidence artifacts.
Rebuild all text, equations, plots, tables, and captions as editable or
deterministic elements before conference, arXiv, journal, or public use.

## Reconstruction Inputs

First classify source files by role:

- Main manuscript: title, abstract, method formulas, algorithm, headline
  figures, tables, and central claims.
- Supplement: exact numerical checks, diagnostic tables, ablations, stress
  cases, and uncertainty or boundary details.
- Cover letter, response, notes, or README: intended narrative, scope, and what
  the work is not claiming.
- Existing poster or AI draft: composition reference only; never trust rendered
  formulas, values, superscripts, or plot labels without source verification.

Build a page-to-poster map before editing:

```text
source page / table / figure -> poster section -> claim -> numbers/formulas used
```

This map prevents attractive but untraceable panels.

## Poster Narrative Compression

Compress the paper into five lines before drawing:

```text
Problem: what repeated or hard scientific task motivates the method?
Method: what pipeline or mechanism changes the task?
Correctness: what estimator, theorem, correction, or diagnostic makes it valid?
Results: which 3-5 results answer "does it work?"
Take-home: what should the reader remember and where does the claim stop?
```

For methods papers, separate "training improves efficiency" from "correction
sets the target."  Do not let learned-model performance replace the estimator
or diagnostic argument.

## Layout Ledger

Before detailed text, record the physical and visual constraints:

- poster size and aspect ratio, such as A0 portrait or 16:9 slide
- orientation and grid, such as three columns plus header/footer
- approximate area budget for title, main panels, take-home, and footer
- column widths and gutters
- palette, section-header colors, line weights, and fill colors
- target typography scale for title, subtitles, section headers, body text,
  captions, equations, and plot labels

For portrait method posters, a robust default is:

```text
top title/overview: 0-14% height
main content: 14-88% height
take-home band: 88-97% height
footer/provenance: 97-100% height
left column: problem + math
center column: method pipeline + why it matters
right column: key results
```

## Section Script

Write the complete poster text before final drawing.  For each section, record:

- exact section title
- exact bullets or captions
- exact equations in LaTeX or equation-editor-ready form
- source anchor for every formula, number, and plot
- edit rationale: what was compressed, merged, or omitted

For a method poster, a common section order is:

```text
title / subtitle / author / affiliation
overview box
1. Motivation
2. Target and estimator
3. Training objective
4. Method overview
pseudo-algorithm
5. Why it matters
6. Key results
7. Take-home messages
footer provenance
```

Use this order only when it matches the paper.  Evidence-heavy posters may put
results earlier; theory-heavy posters may give the theorem or mechanism more
space.

## Evidence Panel Specification

For every result panel, specify:

- panel title and one-sentence claim
- source figure/table/page
- exact plotted values or table rows
- which subplots to redraw and which to omit
- caption stating the evidence role, not a generic description
- boundary note when the result is a stress case, diagnostic, or limited claim

Prefer redrawing plots as vector charts from source data or verified values.
Screenshots and AI-rendered plots are acceptable only as temporary layout
placeholders.

## Deletion Ledger

Record what was intentionally removed from the full paper and why.  Common
poster deletions include:

- full introduction and related work
- theorem proofs or long assumptions
- secondary figures that duplicate a result
- cost or implementation details better suited for a talk
- supplement-wide surveys that distract from the headline story

This prevents omissions from becoming accidental overclaims.

## Numerical And Formula Audit

Make a formal checklist before handoff:

- title exactly matches the chosen manuscript or approved poster title
- superscripts, subscripts, Greek letters, hats, primes, and minus signs render
  correctly
- all reported numbers match the manuscript, supplement, or regenerated data
- stress-case values are labeled as stress or boundary cases
- no result panel claims more than its source table or figure supports
- formulas are editable LaTeX/equation objects or rendered from a deterministic
  equation source
- plots are redrawn or linked to verified source images/data

When an AI concept draft contains numbers, assume at least one number is wrong
until checked.

## Editable Rebuild Order

When rebuilding in PowerPoint, Illustrator, Inkscape, Keynote, Google Slides, or
a deterministic script:

1. Create the poster canvas with final size and guides.
2. Add title, subtitle, authors, affiliation, and overview box.
3. Build the column guides and section boxes.
4. Re-enter text manually from the section script.
5. Rebuild equations with the equation tool or deterministic LaTeX render.
6. Redraw the method flowchart with editable shapes and arrows.
7. Redraw or place verified result charts.
8. Add take-home messages and footer provenance.
9. Normalize typography, spacing, colors, borders, and line weights.
10. Export PDF and high-DPI PNG.
11. Inspect the export visually and run the numerical/formula audit checklist.

## Handoff Standard

A camera-ready poster handoff should include:

- editable source file or deterministic script
- PDF export
- high-DPI PNG preview
- source map or page-to-poster map
- numerical/formula audit checklist status
- remaining risks, such as plots that still need vector redraws
