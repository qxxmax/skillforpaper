# Multi-View Literature Graph Contract

Use this protocol whenever papers are organized into a family tree, genealogy,
landscape, citation graph, author graph, or search-process figure.

## Do Not Use One Graph For Three Questions

Create separate views:

1. `landscape_map`: topic and method coverage across the full curated set.
2. `citation_lineage_graph`: checked citation and method-relation edges.
3. `audit_funnel`: candidate, screened, verified, full-text, and claim-core
   counts.

An optional `author_collaboration_graph` may be added, but it must not be
presented as method ancestry.

## Canonical Edge Types

Only use these relation labels unless the ledger declares and defines a new
project-specific type:

```text
direct_citation
forward_citation
method_precedent
method_extension
baseline_comparison
same_author_context
shared_benchmark
conceptual_neighbor
external_historical_relation
```

Use `templates/relation_ledger_template.csv`. Every edge needs an `EvidenceID`,
relation basis, confidence, and human-review status.

## Direct-Citation Gate

`direct_citation` is allowed only when the cited work appears in the source
paper bibliography or citation context. Similar formulas, shared authors, or a
plausible history do not establish a direct citation.

If an external paper helps explain history but is absent from the bibliography,
use `external_historical_relation` or `conceptual_neighbor`.

## Multi-Label Node Contract

Keep scientific membership separate from display placement:

- `PrimaryDisplayCluster`: one cluster used only for layout.
- `AllTopicLabels`: every applicable topic or method label.
- `EvidenceLevel`: metadata, abstract, full text, or claim anchored.
- `SourceRelation`: root, direct bibliography, external addition, or candidate.
- `ReadingPriority`: P0-P3 or the declared local scale.

This prevents interdisciplinary papers from being forced into one scientific
category merely because the drawing needs a single position.

## Visual Encoding

Recommended defaults:

| property | encoding |
|---|---|
| method/topic family | fill color |
| direct vs external source relation | border style |
| evidence level | node shape or badge |
| relevance/centrality | node size |
| year | horizontal position or label |
| direct citation | solid arrow |
| conceptual/external relation | dashed arrow |
| uncertain/unreviewed relation | dotted arrow or omit from public view |

Do not encode more than four simultaneous visual channels in a public slide.
The complete ledger remains the authoritative representation.

## Count Integrity

All displayed counts must be computed from deduplicated records, not typed into
the figure manually. Record the source table, deduplication key, filters, and
generation command in `templates/graph_view_manifest_template.md`.

## Output Set

For graph requests, create or update:

- `relation_ledger.csv`;
- `literature_graph_nodes.csv`;
- `landscape_map.*`;
- `citation_lineage_graph.*`;
- `audit_funnel.*` when search completeness is discussed;
- `graph_view_manifest.md`;
- source code used to render the views.

Start from `templates/literature_graph_nodes_template.csv` and, when search
completeness is discussed, `templates/audit_funnel_counts_template.csv`.
`scripts/render_literature_views.py` provides a deterministic default renderer;
projects may replace its styling, but must preserve the relation and count gates.

## Public-Graph Gate

Before a graph enters slides, paper, or report:

- every edge exists in the relation ledger;
- every direct-citation edge passes bibliography/context verification;
- author edges are not described as method ancestry;
- metadata-only nodes are visually distinct;
- counts reproduce from source tables;
- the graph caption states which relation types are shown;
- the visual has been rendered and inspected for clipping and overlap.
