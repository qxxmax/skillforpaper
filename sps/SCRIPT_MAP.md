# Python script map

The repository's Python files do not form one large application. They belong
to four different layers:

| Layer | Scope | Who uses it? | Installed with the skill? |
|---|---|---|---|
| Installer | One entry point | Someone installing or updating the skill manually | No |
| General skill tools | Shared validators, graphing, Dijkstra, and optional API accounting | Codex | Yes |
| Public SPS maintenance | Export checks and generated comparison tables | Maintainers | No |
| Frozen SPS run scripts | Per-run reproducibility snapshots | Maintainers | No |

For ordinary use, send the skill prompt in Codex. You do not need to choose or
run a Python file yourself.

## Installer

| Script | Purpose |
|---|---|
| `install.py` | Installs or updates only `play-the-toy-with-children/`, keeps a backup during updates, and checks the installed copy. |

The installer does **not** copy `sps/` or its experimental scripts into the
Codex skill directory.

## General skill tools

These seven scripts live under `play-the-toy-with-children/scripts/`:

| Script | Purpose | When it is needed |
|---|---|---|
| `smoke_test.py` | Checks required skill files and reports optional capability readiness. | Installation check |
| `validate_paper_reading_record.py` | Rejects a paper-reading record that lacks identity, anchors, evidence IDs, or resolved placeholders. | Before using reading notes as claim support |
| `validate_keyword_query_graph.py` | Checks keyword provenance, query routes, and graph-relation contracts. | Multi-round or graph-based searches |
| `validate_part2_learning_package.py` | Checks the Part 2 contract, innovation and formula ledgers, competence levels, and requested exports. | Before using a technical-learning package |
| `run_literature_dijkstra.py` | Runs shortest-path navigation with recorded node, edge, and cost tables. | Only when Dijkstra graph mode is requested |
| `render_literature_views.py` | Produces separate landscape, lineage, and audit-funnel figures. | Only when public graph images are requested |
| `observable_research_runner.py` | Calls the Responses API while recording the usage counters exposed by the API. | Only for an API-observable token/cost experiment |

The first five use the Python standard library. Graph rendering additionally
uses `matplotlib` and `networkx`. Exact API accounting additionally uses the
`openai` package and an API key.

## Public SPS maintenance

| Script | Purpose |
|---|---|
| `sps/scripts/validate_public_export.py` | Checks the public repository boundary, required files, workbook, JSON files, and links without distributing downloaded papers. |
| `sps/scripts/validate_dijkstra_public_run.py` | Recomputes the public Dijkstra paths and checks the recorded graph invariants. |
| `sps/scripts/build_sol_goal_rerun_comparison.py` | Rebuilds the 2026-07-16 SPS case summary and the protocol-aware comparison with the earlier SOL run from recorded JSON/CSV artifacts. |

These scripts test the published example; they are not needed to conduct a new
literature review.

## Frozen SPS run scripts

The 34 scripts under `sps/runs/*/scripts/` preserve how particular SPS results
were produced. Together they record this pipeline:

```text
lock the root paper
-> derive references, keywords, and query routes
-> execute searches and retain raw provenance
-> deduplicate and screen candidates
-> download and verify selected full texts
-> build page-anchored reading packets
-> compile source, evidence, number, relation, and gap tables
-> run and render literature graphs
-> freeze hashes, metrics, and manifests
-> validate the final package
```

### What each group does

| Stage | Representative scripts | Output |
|---|---|---|
| Root and query construction | `parse_root.py`, `derive_root_artifacts.py`, `run_query_routes.py`, `execute_queries.py` | Root bibliography, grounded keywords, query matrix, and raw search provenance |
| Candidate recovery and screening | `rebuild_results_from_raw.py`, `screen_and_select.py`, `integrate_round2.py` | Deduplicated candidate pool, scores, selected papers, and gap-closure additions |
| Full-text acquisition | `download_selected.py`, `finalize_recovered_pdfs.py` | Verified local PDFs and download status |
| Paper reading | `build_reading_packets.py`, `extract_sections.py` | Page-aware text packets and method/result/conclusion excerpts |
| Evidence package | `build_current_evidence_package.py`, `build_research_artifacts.py`, `prepare_workbook_data.py` | Source matrix, reading notes, claim/source ledger, gaps, workbook data, and report |
| Graph navigation | `run_candidate_dijkstra.py`, `run_verified_dijkstra.py`, `render_views.py` | Candidate paths, verified paths, lineage, landscape, and audit figures |
| Provenance freeze | `build_artifact_milestones.py`, `freeze_current_run.py`, `freeze_fresh_run.py`, `cleanroom_dependency_scan.py` | Creation timeline, hashes, package boundary, and independence checks |
| Final validation | `validate_cleanroom_package.py`, `validate_direct_edges.py`, `validate_full_run.py`, `finalize_and_validate.py` | Counts, citation checks, graph invariants, manifests, and PASS/FAIL reports |

## Why some files are duplicated

The matched `gpt-5.6-sol/xhigh` and Goal-mode runs intentionally froze their
own copies of the execution scripts. Six script pairs are byte-for-byte
identical. Keeping them inside each run makes the historical package
self-contained, but it also makes the repository look more complicated.

The frozen copies remain because the run manifests reference them. Moving them
requires a versioned migration of those manifests and validators.
