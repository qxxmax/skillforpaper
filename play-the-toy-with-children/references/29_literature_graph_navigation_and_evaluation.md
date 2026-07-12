# Literature Graph Navigation And Evaluation

Use this reference when the user wants the search workflow to become a
literature-space navigation system, not just a list of papers.  Use it for
strategy comparisons, controlled experiments, token/time/cost logging,
literature genealogy graphs, confirmed/unconfirmed paper classification, and
claims that one workflow is more optimized than another.

First load `references/33_literature_intent_modes_and_state_loop.md` and record
the current mode in `research_state.md`.  Graph navigation can serve different
primary modes:

- `locate`: shortest trusted path to a source or identifier.
- `learn`: readable path through reviews, hubs, landmarks, and topic clusters.
- `evaluate`: paths to supporting, opposing, replication, benchmark, and
  boundary evidence.
- `cover`: high-recall exploration of citation, author, topic, venue, and
  bridge neighborhoods.

When the graph is used to justify search coverage, also load
`references/34_channel_lineage_and_cross_validation_gate.md`.  That gate defines
required source-channel families, cross-validation rules, N-generation
citation/author/topic traversal, and stop judgment.

## Navigation Model

Represent the literature space as a heterogeneous graph:

```text
nodes = papers + authors + topics + venues + databases + queries
edges = citation + authorship + coauthor + topic membership + query hit
      + semantic similarity + bibliographic coupling + co-citation
```

Separate two layers:

- Fact layer: paper identity, author, venue, year, identifier, access,
  verification status, citation/context evidence, and graph edges.
- Strategy layer: which node to read, which query/source to expand, which
  citation path to chase, which candidate to downgrade, and when to stop.

## Verification Levels

Use these statuses in `paper_verification_ledger.md`:

| level | meaning |
|---|---|
| C0 candidate | proposed by search or model, not verified |
| C1 metadata | title/authors/year/source/identifier verified |
| C2 abstract | abstract accessible and relevance can be judged |
| C3 full_text | method/result/limitation can be checked |
| C4 claim | a specific claim is verified by source location, note, or screenshot |

Paywalled or inaccessible but likely important items should remain in an
unconfirmed queue instead of disappearing from the review.

## Graph Algorithms

- Dijkstra: use for knowledge paths from a root author, paper, or topic to a
  target node.  Convert relationship strength to distance with
  `cost(edge) = -log(strength + epsilon) + edge_type_penalty`.
- Personalized PageRank: use for root-conditioned ranking of papers/authors
  across many paths, not one shortest path.
- HITS: use to distinguish authority papers from hub/review papers.
- Community detection: use Louvain, Leiden, or a simpler clustering method to
  form topic/facet communities.
- MMR or submodular reranking: use after scoring so the top list is not all
  from the same author, source, or topic.
- Active learning: use user labels to update relevance, key-paper, and
  verification-priority scores.

Final ranking should combine relevance, graph position, coverage gain,
verification confidence, freshness, access cost, and redundancy:

```text
FinalScore =
  w_rel * relevance +
  w_ppr * personalized_pagerank +
  w_path * exp(-dijkstra_distance) +
  w_auth * authority +
  w_hub * hub +
  w_bridge * bridge_score +
  w_cov * delta_coverage +
  w_ver * verification_confidence +
  w_fresh * freshness -
  w_access * access_cost -
  w_redun * redundancy
```

When a mode-specific score is needed, use the formulas in
`references/33_literature_intent_modes_and_state_loop.md`, then apply
diversity reranking so top candidates are not all from one author, topic,
venue, database, or method family.

## Required Graph Artifacts

When graph mode is active, create:

- `research_state.md`
- `candidate_pool.md`
- `evidence_registry.md`
- `round_log.md`
- `paper_verification_ledger.md`
- `literature_graph_nodes.md`
- `literature_graph_edges.md`
- `ranked_reading_list.md`
- `literature_lineage_graph.mmd` or `graph.json` when visualization matters.
- `graph_optimizer_evaluation.md` when comparing strategies.

Use the matching templates in `templates/`.

## Full Lineage Scan Gate

Do not call a result a full lineage scan after a single seed search. A full
lineage scan must show at least five auditable loops:

| loop | required evidence |
|---|---|
| L0 seed | seed/sentinel papers recovered and scope fixed |
| L1 backward | reference/ancestor/method-foundation branch expanded |
| L2 forward | citing/descendant/application/frontier branch expanded |
| L3 cluster | author, method, topic, venue, tool, and boundary clusters checked |
| L4 gate | green/secondary/uncertain/caution/excluded labels and stopping reason recorded |

For high-recall or public-audit workflows, record these loops as generation
expansion in `citation_generation_log.md`:

- `G0` seeds and sentinels;
- `G1` backward and forward citation expansion;
- `G2` co-citation, bibliographic coupling, author, and topic expansion;
- `G3` bridge and cluster-gap expansion when needed;
- `G4` audit of unconfirmed, blocked, excluded, and access-limited records.

For teaching or public demonstration, also render the lineage graph to a
portable visual format such as PDF/JPG/PNG in addition to source tables. The
graph does not need to be beautiful in early loops, but it must make the
missing branches and non-green nodes visible.

Minimum checkpoint outputs:

- `channel_coverage_plan.md`
- `citation_generation_log.md`
- `cross_validation_matrix.md`
- `literature_records.csv` or equivalent candidate table with loop labels.
- `graph_nodes.csv` and `graph_edges.csv` with status, verification level, and
  relation semantics.
- `loop_expansion.md` recording what each loop added.
- link-existence audit for every non-empty source URL, including screenshot or
  metadata evidence paths.
- source-link completion ledger for every core record, including
  `MISSING_SOURCE_URL` and `NO_LINK_REQUIRED` rows.
- `coverage_stopping_report.md` or equivalent stopping note.
- visual graph output when the user will present or teach the workflow.

For source-link audits, distinguish:

- `VERIFIED`: the recorded URL resolved directly with usable page evidence.
- `ACCESS_LIMITED_METADATA_VERIFIED`: the publisher page was blocked or gated,
  but DOI/Crossref/official metadata verified that the source exists.
- `UNVERIFIABLE`: no authoritative source or metadata confirmation was found.
- `ACCESS_CONTROL_SCREENSHOT`: browser evidence shows a blocker such as
  "Just a moment", Cloudflare, access denied, or human verification.
- `RECHECK_REQUIRED`: a URL exists but current evidence is too weak for public
  proof.
- `MISSING_SOURCE_URL`: a core record still needs link completion.
- `NO_LINK_REQUIRED`: the row is a non-bibliographic cluster, boundary, or
  excluded/noise node and must not be used as paper evidence.

Do not silently treat access-control pages as source verification.
For the full rule set, read
`references/32_source_link_completion_and_verification_gate.md`.

If the graph has fewer nodes than the user's purpose requires, treat it as a
checkpoint graph rather than a saturated lineage graph.  Return to
`references/30_candidate_pool_expansion_gate.md` and expand the candidate pool
before using the graph as evidence of literature completeness.

## Experiment Matrix

To claim that a strategy is more optimized, compare it against controls.

Recommended strategies:

| arm | strategy |
|---|---|
| A | one-shot LLM search |
| B | keyword/Boolean only |
| C | semantic search only |
| D | high-recall optimizer without graph navigation |
| E | graph optimizer with PPR/HITS/path/community/MMR/gates |

Control variables:

- Same research question and inclusion/exclusion rules.
- Same seed/sentinel set.
- Same token policy and token cap.
- Same time budget or search-round budget.
- Same accessible databases/tools.
- Same human labeling budget.
- Same output artifacts required.

Measure:

- wall-clock time, model/tool calls, estimated tokens, screened candidates.
- unique candidates, included papers, excluded papers, unconfirmed papers.
- seed recall at k, key-paper recall at budget, facet coverage, route overlap.
- C3/C4 verification yield and green-check count.
- lineage coverage: ancestors, descendants, author clusters, bridge papers.
- redundancy rate and residual-risk quality.
- artifact completeness: route log, node table, edge table, graph, stopping
  report, and audit report.

## Demonstration Cases

Use at least three cases for forward tests:

1. A recent, low-citation technical paper where author/method lineage matters.
   Example: Moxian Qian-related SPS/lattice-field-theory sampling.
2. A workflow-literature case where terminology is scattered across systematic
   review, agents, active learning, and research automation.
3. An LLM interpretability case where the field has fast-moving topics,
   reviews, circuits, sparse autoencoders, and method/tool communities.

For each case, run the same arms and record the same metrics.  Do not compare a
deep graph workflow against a shallow baseline unless the budget is matched or
the budget difference is itself reported.

## Loop Policy And Token-Energy Accounting

Use multiple loops when the task has any of these properties:

- seed/sentinel papers must be recovered;
- citation, author, or topic lineage matters;
- green-check evidence is required;
- the answer will be used in proposal, slides, paper, or public comparison;
- new labels from the user can change which route is best.

Use a single quick loop only for orientation tasks where the user explicitly
accepts weak coverage and no graph/evidence audit.

Recommended loop schedule:

| loop | purpose | stop / continue decision |
|---|---|---|
| L0 | define scope, seeds, token policy, controls | continue only if target and budget are clear |
| L1 | broad multi-route retrieval | continue if seeds or major facets are missing |
| L2 | screen, verify, and classify C0-C4 | continue if core claims lack C3/C4 evidence |
| L3 | graph navigation and lineage closure | continue if ancestor/descendant/bridge gaps remain |
| L4 | synthesis and stopping audit | stop, monitor, or run a targeted gap loop |

Token use should be recorded directly.  It can also be converted into an
`energy-like` normalized cost for optimization and teaching:

```text
compute_energy_units =
  w_tok * tokens +
  w_time * wall_minutes +
  w_tool * tool_calls +
  w_fulltext * full_text_reads +
  w_human * human_labels
```

This is useful as a budget accounting abstraction, not a physical claim.  In
public artifacts, call it "weighted compute/search cost" unless the audience is
explicitly discussing analogies with energy or thermodynamics.

## Green-Check Rule

Use these labels in node and evidence tables:

| status | meaning |
|---|---|
| green_check | relevant, verifiable, quality-passing, and contribution-bearing |
| secondary | relevant but redundant, narrow, or not central |
| uncertain | metadata/abstract only, missing full text, or unclear method |
| caution | usable only with bias, quality, conflict, or applicability caveat |
| excluded | out of scope, duplicate, retracted, unverifiable, or background-only |
| seed | user-supplied or sentinel item used to test recall |
| landmark | high-centrality or method-defining source |

Edges must say what the relation means: `uses_method`, `extends_result`,
`supports`, `contrasts`, `reviews`, `background_only`, `shares_references`, or
`same_dataset`.  Citation does not automatically mean support.

## Output Rule

The public answer should summarize the result.  The evidence that makes it
auditable should live in files: route logs, candidate tables, verification
ledgers, graph node/edge tables, experiment matrices, and stopping reports.
When the user will present, upload, or archive the work, also refresh the
derived artifacts that depend on those files: PDF/TeX reports, lineage graph
PDF/JPG/PNG exports, slide decks, dashboards, XLSX summaries, and zip/package
manifests.  Use `references/31_artifact_refresh_and_export_gate.md` and record
the refresh state in `artifact_refresh_manifest.md`.
