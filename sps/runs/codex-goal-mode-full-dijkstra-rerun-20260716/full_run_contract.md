# SPS Part 1 Fresh-Run Contract

## Objective

Run the complete `play-the-toy-with-children` Part 1 workflow from the verbal
clue **"SPS / stochastic path sampler"**. The objective is an auditable
literature map, not a prose-only summary.

## Fixed scope

- Root identity candidate: `arXiv:2606.13790`.
- Primary intent: `cover`; secondary intent: `evaluate`.
- Scan level: `full`.
- Search channels: root identity, root terminology, backward/reference cues,
  forward/current-neighbor cues, author and coauthor routes, method keywords,
  and failure/evaluation routes.
- Evidence ladder: C0 candidate, C1 bibliographic metadata, C2 abstract,
  C3 downloaded full text, C4 claim anchor.
- Optimizer: actual Dijkstra run over the current run's graph. Its distances
  rank inspection routes only; they do not prove citations or claims.

## Freshness rule

The 2026-07-13 SPS run may be consulted only for protocol comparison and for
candidate hypotheses. No metadata, source checksum, claim, citation relation,
or selection decision is copied into this run without a new source check.

## Completion gate

The run is complete only if all of the following exist and pass validation:

1. Raw route responses and a route-level retrieval log.
2. A deduplicated candidate pool with C0-C2 gates and recorded exclusions.
3. Selected current PDFs with checksums and C3/C4 status separated.
4. Claim-source, keyword/query, source-link, lineage, and gap ledgers.
5. A computed Dijkstra graph with reconstructable shortest paths and an
   equal-budget non-Dijkstra comparison.
6. Rendered landscape, lineage, and audit-funnel views that pass visual review.
7. Goal-mode time/token snapshots labelled as runtime accounting, not API cost.

## Boundaries

- arXiv and Crossref/OpenAlex metadata can establish bibliographic identity,
  not a method claim by themselves.
- A search hit remains a candidate until it passes the stated source gate.
- No universal compute-speed claim may be written from ESS or autocorrelation
  alone; cost-matched evidence is required.
