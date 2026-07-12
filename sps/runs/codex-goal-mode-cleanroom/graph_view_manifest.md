# Graph View Manifest

| View | Question | Source tables | Encoding | Integrity check |
|---|---|---|---|---|
| `graphs/landscape_map.*` | Which method families and years are covered? | `literature_graph_nodes.csv` | x=year; y=method cluster; size=claim relevance | 31 deduplicated current-run nodes |
| `graphs/citation_lineage_graph.*` | Which checked direct citations define the public core genealogy? | `display_relation_ledger.csv` (subset of `relation_ledger.csv`) | arrows=cited -> citing; same cluster colors | 29 displayed edges; all 124 checked edges remain in the full ledger |
| `graphs/audit_funnel.*` | How did the search shrink to claim evidence? | `audit_funnel_counts.csv` | horizontal log-count bars | counts computed from current CSVs |

Shared authorship and conceptual similarity are intentionally excluded from the citation-lineage arrows. Author recurrence is reported separately in `author_lineage_table.csv`.
