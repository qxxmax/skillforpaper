# Artifact Refresh And Export Gate

Use this reference when a literature scan, source audit, proposal pass, slide
workflow, or workflow-evaluation run changes any source material that has
derived presentation artifacts.

This gate prevents a common failure mode: Markdown, CSV, or graph tables are
updated, but the PDF, TeX, slides, dashboard, zip, or public-facing export still
shows an older state.

## Trigger

Enter this gate when any condition is true:

- a literature loop changes candidate counts, green-check status, source
  verification, graph nodes/edges, route logs, or stopping decisions;
- a proposal, slide deck, paper draft, poster, dashboard, or report has already
  been generated from those materials;
- the user asks whether the work is finished, ready to upload, ready to show,
  or ready to present;
- a package, zip, GitHub upload folder, PDF, PPTX, Beamer PDF, TeX report, JPG,
  PNG, or spreadsheet summary exists beside the updated source files.

## Source-Of-Truth Rule

Separate source artifacts from derived artifacts:

| layer | examples | rule |
|---|---|---|
| source | Markdown, CSV, JSON, BibTeX, graph nodes/edges, TeX source | edit here first |
| derived | PDF, PPTX, rendered PNG/JPG, XLSX, compiled dashboard, zip | rebuild from source |
| audit | logs, screenshots, manifests, validation reports | update after rebuild |

Do not hand-edit a PDF to patch stale content when a source file exists. Update
the source, rebuild, render or inspect the export, then record verification.

## Required Refresh Checklist

Before saying the research pass is complete, create or update
`artifact_refresh_manifest.md` from
`templates/artifact_refresh_manifest_template.md`.

For each derived artifact, record:

- artifact path;
- source files it depends on;
- whether it was refreshed, intentionally unchanged, blocked, or not applicable;
- command used to rebuild it;
- visual or compile verification performed;
- remaining risk.

## Literature-Research Completion Gate

After a high-recall or full literature scan, check these derived artifacts:

- summary Markdown and dashboard files;
- TeX/PDF reports;
- lineage graph PDF/JPG/PNG exports;
- source-link verification PDF or screenshot report;
- slide decks or proposal PDFs that cite the updated literature state;
- XLSX experiment matrices or CSV summaries;
- zip/package manifests when preparing upload.

If a public artifact exists and depends on updated evidence, refresh it or mark
why it is not refreshed. Do not leave a stale PDF silently beside updated
Markdown.

## Slides / Proposal / Paper Rule

For slides, proposals, papers, or posters:

1. Update evidence ledgers and visual-source ledgers first.
2. Rebuild the source artifact: Beamer, Quarto, PPTX, TeX, DOCX, or poster.
3. Export the final viewer artifact: PDF, PPTX, PNG, JPG, or zip as needed.
4. Render or visually inspect the export when layout matters.
5. Update `artifact_refresh_manifest.md`.

If the literature changed but the public deck or proposal is intentionally not
rebuilt yet, say that directly in the manifest and final reply.

## Stop / Continue Rule

The research loop may stop as a search process while the artifact refresh loop
continues. A final answer should distinguish:

- search status: stop / continue / monitor;
- evidence status: green-check / unconfirmed / excluded;
- export status: refreshed / unchanged / stale / blocked.

Only call the whole task done when the requested source artifacts and the
requested derived exports are both current or explicitly marked otherwise.

## Final Reply Requirement

When this gate is active, final replies should include:

- refreshed source artifacts;
- refreshed derived artifacts;
- validation commands and results;
- artifacts intentionally left unchanged;
- stale or blocked exports, if any.
