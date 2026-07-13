# SPS Full Workflow With Dijkstra: Run Contract

## Objective

Starting from the oral clue `SPS / Moxian Qian stochastic path sampler`, rerun
the full literature-research workflow and include an actual Dijkstra
calculation over the current run's literature graph.

## Required stages

1. Resolve and verify the root paper identity from current public sources.
2. Download and read the root PDF and source package.
3. Extract root-grounded keywords and the live bibliography.
4. Generate and execute multi-channel search routes.
5. Deduplicate, screen, and select full texts under recorded facet quotas.
6. Download, validate, extract, and read the selected full texts.
7. Verify source links and direct-citation relations.
8. Build a heterogeneous graph from current-run papers, authors, methods,
   queries, and checked citation relations.
9. Execute Dijkstra from the SPS root and preserve graph inputs, edge weights,
   shortest distances, reconstructed paths, and ranked reading priorities.
10. Build evidence, claim, numerical, gap, lineage, report, graph, and workbook
    artifacts from this run.
11. Validate schemas, identifiers, URLs, citation semantics, Dijkstra
    invariants, provenance, and exported artifacts.

## Dijkstra completion gate

The run is not complete unless all of the following exist and pass validation:

- `dijkstra_graph_nodes.csv`
- `dijkstra_graph_edges.csv`
- `dijkstra_weight_policy.md`
- `dijkstra_shortest_paths.csv`
- `dijkstra_ranked_reading.csv`
- `dijkstra_run_report.md`
- a validator check that recomputes path costs and verifies root distance zero

Distances are navigation costs. They do not establish truth, scientific
similarity, direct citation, or C4 claim support.

## Reuse boundary

Previous runs may be consulted for script structure and regression comparison.
This run must obtain fresh root/source metadata and fresh route responses. Any
reused scientific judgment must be explicitly rechecked against the current
PDF text and marked as `rechecked`, not presented as newly discovered.

## Stop rule

Use a bounded stop only after required facets have selected full-text coverage,
source and citation audits pass, the Dijkstra graph has no unexplained
unreachable core nodes, and remaining gaps are recorded.
