# Graph View Manifest

- `landscape_map`: source `source_matrix.csv`; cluster counts; arXiv ID deduplication.
- `citation_lineage_graph`: source `relation_ledger.csv` and `source_matrix.csv`; only reviewed direct/precedent/comparison edges.
- `audit_funnel`: source `audit_funnel_counts.csv`; counts generated from deduplicated tables.
- Rendering command: `MPLCONFIGDIR=/tmp/mplconfig python3 scripts/render_views.py`.
- Direct citation means the target occurs in the root live bibliography/context. External additions use dashed conceptual/comparison relations.
