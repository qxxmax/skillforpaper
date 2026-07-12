# Poster Layout And Prompt Protocol

Use this reference after the source map, argument tree, formula inventory, and
display candidates exist.  Its job is to turn the scientific story into a
layout specification and, when useful, a structured prompt for a visual draft.

## Two Separate Tasks

Do not collapse layout design and rendering/tool invocation.

1. Composition: page ratio, grid, modules, visual path, figure/formula/table
   placement, and information density.
2. Rendering specification: exact text, equations, figures, data values,
   colors, constraints, and quality checks passed to a drawing tool or
   implemented in PPT/LaTeX/Matplotlib.

## Story-To-Layout Skeleton

For a one-page academic poster, prefer this reading order unless the project
needs a different spine:

```text
title / one-sentence thesis
problem
core mechanism figure
formal objects / formulas
workflow or method strip
theory or claim cards
evidence / result panels
scope boundary
bottom takeaway
```

For portrait posters, use a top-down story.  For landscape posters, use a
left-to-right comparison or a central mechanism with evidence panels around it.

## Grid And Area Budget

Use a grid before writing detailed text:

- Portrait: think in a 12-column grid and vertical bands.
- Landscape: think in 2-3 horizontal bands and 2-4 evidence columns.
- Keep outer margins stable.  Do not add floating cards inside cards.
- Let the largest visual object be the method's core mechanism, not a generic
  decoration.

Typical portrait area budget:

```text
header / thesis: 8-12%
problem + mechanism: 20-28%
formal objects + workflow: 18-24%
theory / claim cards: 12-18%
evidence panels: 28-36%
scope / takeaway: 6-10%
```

Adjust the budget to the paper.  If evidence is the contribution, evidence can
be the largest block.  If mechanism is the contribution, the mechanism figure
must dominate the first scan.

## Core Mechanism Figure

Every poster should have one visual core.  It should answer the three-second
question: "What changed?"

Examples:

- strict gate vs branch-preserving controller
- generator-only path vs corrected/audited estimator
- endpoint-only metric vs endpoint/path diagnostic split

Use paired panels when the contribution is a contrast.  Use a process strip
when the contribution is a contract or pipeline.

## Formula Selection Rule

Select formula layers, not isolated formulas.  A formula-heavy poster usually
needs at most three layers:

1. Object/law: what mathematical object is being generated or optimized.
2. Accumulation/update: what local increments or decisions produce the
   central quantity.
3. Estimator/diagnostic: how the final claim is estimated and trusted.

For learned nonequilibrium samplers, do not show only target, final weight, and
ESS.  Show the path law and work accumulation:

```text
Q_theta(Gamma) = pi_0(x_0) prod_t K_{theta,t}(x_{t+1}|x_t)
log w(Gamma) = sum_t [log gamma_{t+1}(x_t)-log gamma_t(x_t)] = -W(Gamma)
Delta F_hat = -log mean_i exp[-W(Gamma_i)],   ESS = (sum_i w_i)^2 / sum_i w_i^2
```

For general stochastic learned kernels, add a small forward/backward-ratio note
or backup card:

```text
log w = target/action terms + sum_t log K^-_t(x_t|x_{t+1}) / K^+_t(x_{t+1}|x_t)
```

This keeps the transition kernels and cumulative work visible.

## Structured Rendering Prompt

When using an image-generation tool for a concept draft, write a structured
prompt rather than asking it to "make a poster."  Include:

1. Overall style: language, orientation, background, palette, academic poster
   tone, and vector/infographic preference.
2. Exact title, subtitle, authors, and section names.
3. Section-by-section text, preferably concise bullets.
4. The exact visual core: what appears on the left/right or in each stage,
   which arrows, nodes, colors, symbols, and warnings mean what.
5. Exact equations.  State that equations must be rendered cleanly, but expect
   to replace them with LaTeX/PowerPoint equations for camera-ready output.
6. Exact numerical values and table rows.  Use "include exactly these values"
   for concept prompts, then verify manually.
7. Design constraints: legible typography, no invented claims, no copyrighted
   logos, balanced density, and visible boundary language.
8. Output intent: concept draft versus camera-ready/editable poster.

## Concept Draft Versus Camera-Ready

Image generation is useful for quick concept posters because it can align
icons, workflow diagrams, tables, and visual style quickly.  Treat it as a
blueprint, not final evidence.

For camera-ready posters:

- rebuild the layout in PPT/Keynote/Google Slides/Illustrator/Inkscape/LaTeX
  or a deterministic plotting script
- render formulas with LaTeX or an equation editor
- redraw charts from the real data
- use source figures or source PDFs, not hallucinated plots
- export PDF plus high-DPI PNG
- inspect the rendered output for text overlap, distorted images, wrong
  numbers, and formula errors

For a full editable rebuild procedure, including source-file triage,
page-to-poster maps, section scripts, vector plot redraws, deletion ledgers,
and numerical/formula audit checklists, read
`references/17_camera_ready_poster_rebuild.md`.

## QA Checklist

Before handoff, check:

- The one-sentence thesis is visible in the first scan.
- The visual core explains the mechanism without reading all text.
- The formula layers include object/law, accumulation/update, and
  estimator/diagnostic.
- Every evidence panel has one claim, one source anchor, and one boundary.
- Boundary language prevents obvious overclaims.
- Text is not clipped or overlapping.
- Images are not stretched unless deliberately schematic.
- Source figure resolution is sufficient for the rendered size.
