# Clean-Room Research Contract

## Permitted inputs

- Oral clue: `SPS / Moxian Qian stochastic path sampler`.
- Installed `play-the-toy-with-children` skill, its general references, templates,
  and generic validators.
- Public sources retrieved during this run.

## Forbidden inputs

- Any query matrix, keyword ledger, candidate table, PDF list, reading note,
  relation ledger, report, or conclusion from runs 1-5.
- The previous fixed `build_research_artifacts.py` and fixed PDF download lists.
- Copying or importing previous scientific result files before or after freeze.

## Required derivation chain

1. Resolve the root identity from the oral clue.
2. Download and read the root source and PDF.
3. Extract root-grounded terms and bibliography dynamically.
4. Generate query routes from those extracted terms and author metadata.
5. Execute the generated routes and screen current results.
6. Select full texts by recorded score and facet quota, not by a fixed ID list.
7. Read selected PDFs and record problem, method/correction, result, limitation,
   and original-text anchors.
8. Generate claims, gaps, lineage, and the report from the new ledgers.
9. Validate schemas, source links, citation semantics, PDF integrity, and graphs.

## Completion rule

The run is complete only if provenance files demonstrate every major artifact's
current-run parent files and a dependency scan finds no previous-run path or
fixed-result generator reference.
