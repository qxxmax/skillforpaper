# Output Manifest

Run: `multimodel-fullscan-benchmark-20260812` / arm `opus-5-thinking-xhigh`.
Scan level: **full** (`cover` mode). `graph_mode`: **OFF** (no relation ledger,
no lineage graph files this run).

This file is the live run ledger and was created **first**, before any other
run file. Status values: `planned` → `in_progress` → `on_disk` → `verified`,
plus `needs_update` when source evidence changes after the file was written.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| research_state.md | markdown | — | mode, scope, budget mirror of round_log.md | verified | budget mirror = 29, matches the call ledger |
| candidate_pool.md | markdown | search rounds | C-level per candidate | verified | 298 rows, generated from saved API responses |
| evidence_registry.md | markdown | fetched sources, downloaded PDFs | EvidenceID + anchors + integrity note per PDF | verified | E0001–E0041; 9 PDFs with byte/page notes |
| round_log.md | markdown | — | call-ledger row for every web call, running total n/40 | verified | 29 ledger rows incl. 3 failed/blocked |
| search_budget_contract.md | markdown | round_log.md | `actual` column backfilled at stop | verified | actuals backfilled with ledger row references |
| search_scope.md | markdown | seed paper | eligibility + seed set + facet map | on_disk | seed recall recorded per family |
| search_route_log.md | markdown | round_log.md | route plan + per-query hits | on_disk | 10 route families, 16 logged retrievals |
| candidate_screening_table.md | markdown | candidate_pool.md | label + reason per screened item | verified | 112 include / 30 monitor / 156 exclude |
| coverage_stopping_report.md | markdown | all of the above | scope-limited, no completeness claim | on_disk | explicit non-completeness statement |
| keyword_ledger.csv | csv | seed paper sections, retained papers | source anchor per seed term | on_disk | 35 terms, every seed term with a section anchor |
| query_matrix.csv | csv | keyword_ledger.csv | TermIDs + domain lock per query | on_disk | 16 executed + 1 blocked + 2 planned-not-run |
| query_yield_log.csv | csv | search_route_log.md | raw/dedup/screened/included per query | on_disk | marginal-yield collapse to 0 new includes |
| channel_coverage_plan.md | markdown | round_log.md | channel families required/searched/blocked | on_disk | 6 channels used; SciPost blocked + substituted |
| missing_risk_report.md | markdown | all of the above | named residual gaps | on_disk | index, citation-graph, depth, language gaps |
| literature_matrix.md | markdown | evidence_registry.md, sources/pdfs/ | verified identifiers per row | on_disk | C4 vs C2-abstract labeled per row |
| lineage_snowball_map.md | markdown | evidence_registry.md | author/lab/method-family pass | on_disk | same-author, same-lab, method-family, citing |

## Sub-Directory Artifacts

Not top-level manifest rows (the run-state validator reconciles top-level files
only); covered by the `evidence_registry.md` row above, which carries one
integrity note per downloaded file.

- `sources/pdfs/` — core PDFs downloaded under the C3 source gate, one
  `E_FULLTEXT` evidence row each with a byte-size and page-count integrity note.

## Not Applicable This Run

| Output | Reason |
|---|---|
| relation_ledger.csv, literature_graph_nodes.csv, literature_lineage_graph.mmd, graph_view_manifest.md | `graph_mode` is OFF by task instruction |
| screenshots/ | screenshot policy = `none` (headless run; PDFs and API records used instead) |
| final_report.md / .tex / .pdf | not requested; the landscape synthesis lives in literature_matrix.md and coverage_stopping_report.md |
| artifact_refresh_manifest.md | no pre-existing public export depends on this run |

## Export Rules

- Claims without an `EvidenceID` go to notes, not main conclusions.
- C0/C1 papers may be listed but never used as strong claim evidence, and are
  labeled as unverified-identity or metadata-only in every file that shows them.
- C3/C4 papers may support substantive claims.
- Paywalled or unreachable but central papers must appear in
  `missing_risk_report.md` and in the coverage report's residual risks.
