# Candidate Pool Expansion Gate

Use this reference when a literature scan, lineage graph, or source audit is
structurally correct but the number of retrieved or screened papers is still
too small for the user's purpose.

This gate prevents a common failure mode: a neat evidence graph with too few
nodes being treated as a high-recall literature review.

It also prevents the opposite failure mode: a large expanded candidate pool
being reported as if every row were verified evidence. Expanded candidates are
metadata-level until they pass link completion, source verification, relevance
screening, and graph/evidence promotion.

Before running large expansion, check
`references/34_channel_lineage_and_cross_validation_gate.md`.  A low count is
often caused by missing channel families, shallow citation generations, or
missing author/topic expansion rather than by a weak summary step.

## Trigger

Enter this gate when any condition is true:

- the user says the literature count is not enough;
- a full scan has fewer than the target candidate or relevant-record count;
- a facet has fewer than its minimum evidence quota;
- the graph has only seed/ancestor nodes and weak descendant or cluster
  expansion;
- the scan relies on one or two source families only;
- the stopping report says `continue`, `stop_budget`, or high residual risk.

## Count Targets

Set the target before expanding.  Suggested defaults:

| purpose | candidate pool before screening | relevant after screening | core green-check evidence |
|---|---:|---:|---:|
| quick orientation | 20-40 | 8-15 | 3-8 |
| teaching/demo checkpoint | 60-100 | 25-50 | 10-20 |
| proposal/slides with novelty claims | 80-150 | 40-70 | 15-30 |
| paper related-work section | 120-250 | 60-120 | 20-50 |
| systematic/scoping review | protocol-defined, often 300+ | protocol-defined | protocol-defined |

For narrow new topics, lower counts are acceptable only when the route log
shows multiple independent routes and the residual-risk report names the
remaining blind spots.

## Facet Quotas

Do not judge adequacy by global count alone.  Define required facets and set a
minimum quota for each, for example:

- method ancestors;
- direct baselines;
- same-author or same-lab lineage;
- forward applications or descendants;
- critique, negative, failure, or limitation evidence;
- review or survey hubs;
- instrumentation, dataset, benchmark, or domain-specific branch;
- adjacent terminology branch.

Default quota for proposal/slides: at least 5-10 candidate records per major
facet and at least 2-5 screened relevant records per major facet.

## Expansion Loops

After the L0-L4 lineage checkpoint, run L5-L10 until the count targets or
stopping rule are met:

| loop | purpose | output |
|---|---|---|
| L5 backward snowball | references of green-check and landmark papers | ancestor candidates |
| L6 forward snowball | citing papers, applications, replications, rebuttals | descendant candidates |
| L7 author/lab/venue | same author, group, venue, instrument, dataset, grant | lineage candidates |
| L8 facet query expansion | synonym, acronym, controlled vocabulary, cross-field terms | facet candidates |
| L9 route fusion and screening | deduplicate, rank-fuse, label include/exclude/uncertain | screened pool |
| L10 saturation audit | count yield, facet yield, singleton/doubleton pattern | continue/stop decision |

Record every loop in `high_recall_expansion_plan.md` or an equivalent status
file.  Do not hide low-yield or failed routes; they are evidence for coverage.

When reporting coverage, map these loops to generation expansion:

- L5 and L6 expand G1/G2 citation neighborhoods.
- L7 expands G2 author, lab, venue, instrument, dataset, and grant
  neighborhoods.
- L8 expands G2/G3 topic, synonym, and bridge neighborhoods.
- L9 fuses routes and screens the candidate pool.
- L10 is the G4 audit and stop judgment.

## Source Route Requirements

For a high-recall expansion, use at least three independent route families
unless the user explicitly sets a strict budget:

- bibliographic databases: OpenAlex, Semantic Scholar, Crossref, PubMed,
  arXiv, publisher pages, domain databases;
- citation routes: references, citing papers, co-citation, bibliographic
  coupling, related papers;
- author/lab/venue routes;
- lexical and controlled-vocabulary search;
- semantic or natural-language search;
- grey or negative evidence routes when relevant.

## Continue / Stop Rules

Continue expanding when:

- candidate count is below the target for the purpose;
- any required facet is below quota;
- seed recall is incomplete;
- new green-check yield remains high;
- many records are single-route discoveries, suggesting residual unseen items;
- the user will use the output for novelty, funding, paper, or public teaching.

Stop or defer only when:

- target counts and facet quotas are met; or
- two consecutive expansion loops add fewer than the configured threshold
  (`<5%` new relevant records or `<2` new green-check records by default); and
- unresolved gaps are recorded in `coverage_stopping_report.md`.

## Integration

This gate sits before polished prose:

```text
scope -> route log -> candidate pool expansion -> screening -> graph/source
verification -> coverage stopping -> sentence/result bank -> proposal/slides/paper
```

If the user asks for more literature after prose has started, pause prose and
return to this gate.  Update:

- `search_budget_contract.md`
- `search_route_log.md`
- `candidate_screening_table.md`
- `high_recall_expansion_plan.md`
- `coverage_stopping_report.md`
- graph nodes/edges and source-link audit when new records are promoted
- `artifact_refresh_manifest.md` and any derived PDF/TeX/slide/dashboard/zip
  exports when the updated scan will be presented, uploaded, or used as the
  current project record. Use
  `references/31_artifact_refresh_and_export_gate.md`.

For link completion and screenshot requirements before promotion, use
`references/32_source_link_completion_and_verification_gate.md`. Do not require
screenshots for every metadata-only candidate; require them for records that
enter or remain in the core evidence layer.
