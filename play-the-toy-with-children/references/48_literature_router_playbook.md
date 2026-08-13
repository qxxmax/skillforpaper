# Literature Router Playbook

The full step list for the Literature / Related Work / Novelty Router in
`SKILL.md`. Follow the steps in order; each step names the reference that
carries its detailed rules and the state files it creates or updates.

For broad discovery or graph expansion, route retrieval through
`references/40_retrieval_backend_and_citation_expansion.md` before screening.
Use its backend manifest and event log; do not let a retrieval backend assign
claim evidence or public graph edges.

1. Read `references/18_iterative_literature_loop.md`.
2. Read `references/33_literature_intent_modes_and_state_loop.md`.
3. Classify the request into:
   - `intent_mode.primary`: `locate`, `learn`, `evaluate`, or `cover`
   - `intent_mode.secondary`: another mode or `none`
   - `risk_level`: `low`, `medium`, or `high`
   - `current_action`: the next concrete action
   - `output_mode`: answer, citation, reading path, evidence table, citation
     list, lineage graph, or audit package.
   If multiple modes apply and the user gives no preference, choose the
   highest-risk primary mode: `cover > evaluate > learn > locate`.  Use
   `locate` freely as a sub-action inside the other modes.
4. For multi-round, `cover`, `evaluate`, graph, source-verification, or final
   report workflows, create or update:
   - `research_state.md` from `templates/research_state_template.md`
   - `candidate_pool.md` from `templates/candidate_pool_template.md`
   - `evidence_registry.md` from `templates/evidence_registry_template.md`
   - `round_log.md` from `templates/round_log_template.md`
   - `output_manifest.md` from `templates/output_manifest_template.md`
   Register DOI, URL, screenshot, quote, page, full-text, and claim evidence
   with `EvidenceID`; final reports cite `EvidenceID`, not just `PaperID`.
5. For full scans, systematic/scoping reviews, prior-art searches, source
   triangulation, or any task where missed sources carry high risk, read
   `references/28_high_recall_search_optimization.md`.
6. For channel coverage, required databases/sources, N-generation citation
   expansion, cross-validation, or coverage proof questions, read
   `references/34_channel_lineage_and_cross_validation_gate.md` and create or
   update:
   - `channel_coverage_plan.md` from
     `templates/channel_coverage_plan_template.md`
   - `citation_generation_log.md` from
     `templates/citation_generation_log_template.md`
   - `cross_validation_matrix.md` from
     `templates/cross_validation_matrix_template.md`
   State what was checked under the current scope; do not call the literature
   absolutely complete.
7. If the source count, screened count, green-check count, or facet coverage is
   below the user's purpose, or the user says the literature is not enough, read
   `references/30_candidate_pool_expansion_gate.md` and create
   `high_recall_expansion_plan.md` from
   `templates/high_recall_expansion_plan_template.md`.
8. For keyword extraction, controlled vocabulary, query expansion, or any full
   `cover` scan, read `references/35_keyword_ontology_and_query_matrix.md` and
   create or update:
   - `keyword_ledger.csv` from `templates/keyword_ledger_template.csv`
   - `query_matrix.csv` from `templates/query_matrix_template.csv`
   - `query_yield_log.csv` from `templates/query_yield_log_template.csv`
   Seed terms require section/page anchors. Acronyms may not be searched alone.
9. For strategy comparisons, graph navigation, genealogy maps, green-check
   evidence marking, or workflow demonstrations, read
   `references/29_literature_graph_navigation_and_evaluation.md`.
10. For family trees, landscapes, citation graphs, author graphs, or audit-flow
   figures, read `references/36_multiview_literature_graph_contract.md` and
   create or update:
   - `relation_ledger.csv` from `templates/relation_ledger_template.csv`
   - `literature_graph_nodes.csv` from
     `templates/literature_graph_nodes_template.csv`
   - `graph_view_manifest.md` from `templates/graph_view_manifest_template.md`
   - separate landscape, citation-lineage, and audit-funnel views as applicable.
   A direct-citation edge must be checked against bibliography or citation
   context; shared authorship or conceptual similarity is insufficient.
   Use `scripts/render_literature_views.py` as the reproducible default when a
   project does not already have a checked graph pipeline.
11. For source-link, screenshot, title-match, or evidence-proof questions, read
   `references/32_source_link_completion_and_verification_gate.md`.
12. Choose scan level: none / quick / full / monitor.
13. Record token policy: strict / balanced / generous / no_budget.
14. Record screenshot policy: none / key-only / all / on-demand.
15. For full or high-recall scans, create or update:
   - `search_budget_contract.md`
   - `search_scope.md`
   - `search_route_log.md`
   - `candidate_screening_table.md`
   - `coverage_stopping_report.md`
16. If the scan is below the target candidate/relevant/green-check count, create
   or update:
   - `high_recall_expansion_plan.md`
   - expanded candidate pool table or candidate-screening table
   - facet quota status
   - next-loop route list
17. For graph-navigation or evaluation tasks, create or update:
   - `paper_verification_ledger.md`
   - `literature_graph_nodes.md`
   - `literature_graph_edges.md`
   - `ranked_reading_list.md`
   - `graph_optimizer_evaluation.md`
   - `literature_lineage_graph.mmd` when a visual graph is requested.
   Generate public graphs from the relation ledger, not from prose memory.
   Turn `graph_mode` on when any of the following is true:
   - the user explicitly names Dijkstra, shortest paths, a graph optimizer, or
     literature-space navigation;
   - the user requests a complete/full `cover` workflow together with a family
     tree, lineage, genealogy, citation graph, or multi-round expansion;
   - the user asks to demonstrate, compare, audit, or ablate the search
     algorithm rather than only receive a reading list.
   When `graph_mode` is on and Dijkstra is named or selected, an actual
   executable run is mandatory. Notes, formulas, copied CSVs, or prose saying
   "Dijkstra-style" do not count. Preserve graph nodes, weighted edges, root,
   reconstructed shortest paths, recomputed path costs, and the command/script
   provenance. Use `scripts/run_literature_dijkstra.py` when its generic CSV
   contract fits; otherwise keep the project-specific runner in the output
   package. Compare against a non-graph ranking under the same reading budget
   when claiming an effect. Keep source verification and gap closure active: a
   shortest path is navigation metadata, not scientific evidence.
18. Before assigning or preserving `green_check` for bibliographic records,
   create or update `source_link_verification_loop.md` from
   `templates/source_link_verification_loop_template.md` and verify that:
   - every core record appears in the source-link ledger;
   - every green-check and secondary bibliographic record has an authoritative
     URL;
   - access-control screenshots are marked as weak evidence rather than
     verified source pages;
   - expanded candidate pools are labeled metadata-only until candidates are
     added to core records.
19. For full scans, create or update:
   - `literature_matrix.md`
   - `reviewer_comparison_matrix.md`
   - `gap_ledger.md`
   - `claim_evidence_ledger.md`
   - `literature_snapshot.md`
   - `sentence_result_bank.md`
   - `lineage_snowball_map.md`
20. Before proposal/slides/paper/rebuttal prose, read:
   - `references/25_literature_display_formats.md`
   - `references/22_sentence_and_result_bank.md`
   - `references/23_literature_to_artifact_compiler.md`
   - `references/24_literature_quality_gate_checklist.md`
21. Do not generate polished artifact prose until the claim/evidence ledger is
   updated or explicitly marked unchanged and the expansion plan says the
   candidate-pool count and facet quotas are sufficient, or explicitly records
   the remaining count gap as a limitation.
22. When producing a final literature report, use
   `templates/literature_research_report_template.md` or
   `templates/literature_research_report_template.tex`.  Substantive claims
   require `EvidenceID`; unverified but important sources belong in
   unconfirmed or limitations sections, not in main conclusions.
23. Before final delivery, if keyword, query, or graph ledgers are present, run
   `scripts/validate_keyword_query_graph.py`. Treat schema validation as a
   provenance check, not proof that the scientific classification is correct.
24. Before final delivery, if any PDF, TeX, slide deck, rendered graph,
   dashboard, spreadsheet, source-link report, zip, or public-facing export
   already exists or is requested, read
   `references/31_artifact_refresh_and_export_gate.md` and create or update
   `artifact_refresh_manifest.md` from
   `templates/artifact_refresh_manifest_template.md`. Refresh derived artifacts
   from their source files or explicitly mark them unchanged, stale, blocked, or
   not applicable.
