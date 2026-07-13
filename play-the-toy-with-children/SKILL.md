---
name: play-the-toy-with-children
description: >-
  Use when turning a research topic, dataset, codebase, draft, manuscript,
  book, or empty idea into source-grounded academic outputs including
  iterative literature or market landscape, high-recall source-discovery
  optimization with auditable stopping rules, literature graph navigation and
  controlled workflow evaluation, research proposal polish, grant or project
  proposal structure, paper outline or draft, revision plan, chapter map,
  argument tree, formula/concept inventory, evidence ledger, core
  formula/claim visuals, slide deck, PPT deck, poster, or refreshed
  TeX/PDF/PPTX/zip exports after a research update. Also use when the user wants to iterate a
  science-writing or research-to-poster skill and record how users should
  interact with it.
---

# Play The Toy With Children

Use this skill to move from research material to publishable communication
without losing evidence, claim boundaries, or the user's intended emphasis.

## Six-Part Roadmap And Current Scope

Organize the research lifecycle into six parts:

1. Understand the toy: identify the object, map the literature, read sources,
   trace lineages, and record evidence and gaps.
2. Learn how people use and make toys: deep-read methods, formulas,
   implementations, and current technical progress.
3. Build a toy rigorously: design, execute, diagnose, and validate the research.
4. Find support for the toy: prepare a complete research or funding proposal.
5. Finish the toy and choose its toy box: write the paper, choose a venue,
   submit, and revise.
6. Present the toy: prepare slides, posters, and talks for different audiences.

The current public release and SPS test package validate **Part 1**. Treat the
later output modes as provisional workflow routes; do not describe Parts 2-6
as complete or fully tested without corresponding public test artifacts.

## Start With Input Mode

Identify the user's starting state:

- Topic only: clarify the research question and offer a landscape-research gate.
- Data/code only: inspect what the evidence can support before drafting.
- Draft/manuscript/book/PDF: extract the current argument before rewriting.
- Nothing yet: create a topic-discovery and literature-scoping path.

Ask or infer whether to run a landscape/literature loop:

- No landscape scan: use only provided/local materials.
- Quick landscape scan: map adjacent work, likely gaps, and novelty risks.
- Full landscape scan: compare same-field work, what each did, open gaps, and how this project differs.
- Monitor loop: repeat literature search after the thesis, proposal aims,
  slide spine, or reviewer objections change.

## Diagnosis Before Writing

Before drafting a paper, PPT, or poster, produce four diagnostic artifacts:

1. Project or chapter map: unit title, core problem, core claim, evidence/formula, and relation to the main spine.
2. Argument tree: one-sentence thesis, chapter/section claims, supporting claims, and boundaries.
3. Formula/concept inventory: core formulas versus intermediate derivations, what each says, and how it can be visualized.
4. Display-figure candidates: hero figure, formula cards, logic flow, evidence panels, and claim-boundary panels.

Do not treat these as decoration.  They are the control surface for later paper,
PPT, and poster work.

## Focus And Completeness Rule

Separate the artifacts:

- Source map equals completeness.
- Poster/PPT equals selective argument.
- Paper draft equals ordered prose supported by the source map.
- Interaction log equals how the user corrected the agent's focus and scope.

When the user says the focus is unclear, make the thesis the largest object or
the first paragraph.  When the user says something is missing, expand the source
map or evidence ledger first, then choose what belongs in the public artifact.

## Core Visual Contract

For research involving formulas, models, samplers, estimators, or mechanisms,
try to express the contribution as:

```text
problem -> method -> core formula -> evidence -> boundary -> conclusion
```

For learned samplers and path methods, the default spine is:

```text
target density -> learned path/protocol -> exact weight -> diagnostic gates -> bounded claim
```

See `references/14_core_formula_claim_visuals.md` for formula and claim visual
patterns.  For poster composition, section grids, visual hierarchy, structured
drawing prompts, and concept-versus-camera-ready handoff, read
`references/16_poster_layout_prompt_protocol.md`.  When a rough poster,
AI-generated PNG, screenshot, or prototype must become editable and
camera-ready, read `references/17_camera_ready_poster_rebuild.md`.

## Output Modes

- Literature mode: build a source-discovery loop, high-recall search strategy
  when completeness matters, comparison matrix, gap ledger, novelty statement,
  citation shortlist, and open-question list.
- Proposal mode: polish or draft a grant, fellowship, project, or research proposal around the ask, significance, gap, hypothesis, staged validation, aims, approach, feasibility, risks, and reviewer-facing objections.
- Paper mode: build literature position, thesis, outline, claim ledger, figures/tables, then draft.
- Slides mode: build a talk or deck spine with one claim per slide, action-title headings, proof objects, backup derivations, literature/local figures, and visual continuity.
- Poster mode: one dominant thesis, one mechanism, three to five proof objects, and a bottom takeaway.
- Book mode: make a full chapter map before selecting a public-facing poster/deck spine.

For iterative literature/market research, read
`references/18_iterative_literature_loop.md`.  When the user is improving this
skill itself from papers or competing systems, also read
`references/21_skill_literature_basis.md`.
Before literature search, source verification, graph navigation, or report
export, read `references/33_literature_intent_modes_and_state_loop.md` to
classify the task as `locate`, `learn`, `evaluate`, or `cover`, and to decide
which state files must be maintained.
When the user asks whether the literature/source search is complete, asks for a
full scan, systematic/scoping review, prior-art search, source triangulation,
or any "find as much as possible" task, also read
`references/28_high_recall_search_optimization.md`.
When the user asks which databases/channels must be searched, how many citation
generations to expand, how to cross-verify source existence, or how to justify
coverage without claiming absolute completeness, also read
`references/34_channel_lineage_and_cross_validation_gate.md`.
When the user asks whether source links, screenshots, DOI/arXiv/publisher
pages, or screenshot evidence are complete or reliable, also read
`references/32_source_link_completion_and_verification_gate.md`.
When the user says the literature count is not enough, asks to expand the
candidate pool, or the current source set is below the target count/facet
coverage for its purpose, also read
`references/30_candidate_pool_expansion_gate.md`.
When the user asks to compare search strategies, track token/time/cost
parameters, build a literature lineage graph, classify confirmed versus
unconfirmed papers, or demonstrate that one workflow is more optimized than
another, also read
`references/29_literature_graph_navigation_and_evaluation.md`.
When the user asks how keywords were extracted, wants repeatable query
expansion, or needs search terms to grow from papers rather than model memory,
also read `references/35_keyword_ontology_and_query_matrix.md`.
When exact API token, cache, reasoning-token, time, or cost accounting is a
required experiment output, read `references/37_observable_api_runner.md` and
use `scripts/observable_research_runner.py`. Do not estimate counters missing
from the runtime, and do not compare runs with different stage contracts.
When the user requests a family tree, genealogy, landscape, citation graph,
author graph, or search-process figure, also read
`references/36_multiview_literature_graph_contract.md`.
For literature display formats, sentence/result banks, and artifact handoff,
read `references/25_literature_display_formats.md`,
`references/22_sentence_and_result_bank.md`,
`references/23_literature_to_artifact_compiler.md`, and
`references/24_literature_quality_gate_checklist.md`.
When a research, source-audit, proposal, slide, paper, poster, or workflow
evaluation pass changes source artifacts that have public exports, also read
`references/31_artifact_refresh_and_export_gate.md`.
For proposal polish, read `references/19_proposal_polish_workflow.md`.  When
building a funding proposal from a literature scan, slide deck, or staged
experiment idea, also read
`references/27_funding_proposal_from_literature_and_experiment_ladder.md`.
For slide decks, proposal decks, conference talks, defense decks, and teaching
slides, read `references/20_slides_workflow.md`.
When the user provides or references an existing deck style, or asks for
multiple slide versions from the same topic, read
`references/26_slide_style_extraction_and_storyboard.md` before generating
Beamer/PPTX/PDF.
For poster work, read `references/11_poster_workflow.md`.
For poster layout or image-generation prompt design, read
`references/16_poster_layout_prompt_protocol.md`.
For camera-ready poster reconstruction, editable PPT/Illustrator/Inkscape
builds, page-to-poster maps, vector plot redraws, and numerical/formula audit
checklists, read `references/17_camera_ready_poster_rebuild.md`.
For iteration and user-feedback capture, read `references/15_interaction_protocol.md`.

## Literature / Related Work / Novelty Router

If the user asks for literature review, market research, related work, novelty
positioning, proposal background, citation grounding, source verification,
reviewer-risk analysis, or current-source validation:

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
   The conclusion must say what is auditable under the current scope, not that
   the literature is absolutely complete.
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
18. Before assigning or preserving `green_check` for bibliographic records,
   create or update `source_link_verification_loop.md` from
   `templates/source_link_verification_loop_template.md` and verify that:
   - every core record appears in the source-link ledger;
   - every green-check and secondary bibliographic record has an authoritative
     URL;
   - access-control screenshots are marked as weak evidence rather than
     verified source pages;
   - expanded candidate pools are labeled metadata-only until candidates are
     promoted into core records.
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

## Slides From Existing Style Router

If the user asks to make, polish, reorganize, or generate slides using the
style of an existing deck:

1. Read `references/20_slides_workflow.md`.
2. Read `references/26_slide_style_extraction_and_storyboard.md`.
3. Extract or update `slide_style_profile.md` from the reference deck.
4. Ask or infer author-intake decisions: target audience, duration, central
   thesis, formula depth, visual policy, must-cite sources, and must-avoid
   claims.
5. Produce `slide_framework.md` with the evidence path before generating
   slides.  In the actual deck, show only a concise table of contents / agenda
   near the start; keep the detailed question-evidence-order rationale in
   `slide_framework.md` unless the audience genuinely needs it on screen.
6. Produce a slide-by-slide storyboard before
   generating Beamer/PPTX/PDF.
7. Build `visual_source_ledger.md` for literature figures, screenshots,
   redrawn schematics, generated visuals, and local result figures.
8. Build `equation_notation_audit.md` for every displayed formula and notation
   convention.
9. Polish slides in named rounds and record them.  At minimum distinguish:
   evidence/figure grounding, AI/meta-prose cleanup, and visual-emphasis plus
   slide-by-slide logic audit.  Add a readability / word-economy round when
   paper figures or dense text are present: check whether figure-internal labels
   are readable, crop or zoom dense panels, and delete redundant explanatory
   prose.  Add a keyword-question / audience-comprehension round when the deck
   uses domain terms: have the model ask what a non-specialist would need to
   know before the next slide makes sense, then add compact checkpoint content
   only for terms that would otherwise break the logic.  Use restrained red
   emphasis only for core claims, key result numbers, comparison caveats, and
   terms the speaker must point to.
10. If the user says the slides have too much filler, run a hard de-bloat pass:
   remove AI/self-referential labels, workflow narration, repeated caveats,
   generic bottom lines, and any sentence the speaker can say aloud.  Delete
   redundant checkpoint slides instead of preserving them for process
   completeness.
11. Run `slide_quality_gate_checklist.md` before export.
12. Prefer source-first Beamer/PPTX/Quarto generation; do not directly edit PDFs
   unless the user explicitly asks.

For multiple deck versions, create a shared slide bank and compile variants
such as `20min`, `40min`, `60min`, and `expert` from the same claim/evidence,
visual-source, and notation ledgers.

## Funding Proposal From Literature Router

If the user asks to turn a literature scan, slide deck, paper direction, or
experimental idea into a funding proposal:

1. Read `references/19_proposal_polish_workflow.md`.
2. Read `references/27_funding_proposal_from_literature_and_experiment_ladder.md`.
3. Create or update `funding_proposal_spine.md` from
   `templates/funding_proposal_spine_template.md`.
4. Check that the proposal has a concrete scientific object, direct baselines,
   staged validation, metrics, risks, alternatives, and deliverables.
5. Before TeX/PDF conversion, create `proposal_ai_quality_audit.md` from
   `templates/proposal_ai_quality_audit_template.md` and remove empty or
   defensive prose in Markdown.
6. Convert to TeX/PDF only after the Markdown proposal spine and aims are
   stable.  Use UTF-8 and a Unicode-capable TeX engine for multilingual text.
7. After conversion or any later evidence update, read
   `references/31_artifact_refresh_and_export_gate.md` and refresh the TeX/PDF
   export or mark it explicitly unchanged, stale, blocked, or not applicable.

## Evidence Guardrails

- Do not fabricate results, citations, formulas, or numerical claims.
- Mark unsupported material as boundary, open direction, or reserved slot.
- Keep claim wording tied to visible evidence.
- Distinguish local evidence, literature evidence, and speculation.
- Save source paths, verification steps, user feedback, and unresolved risks.
- Do not put missing-PDF, missing-figure, extraction failure, or "to be added"
  placeholders on audience-facing slides.  Put that status in the visual ledger,
  status file, speaker notes, backup, or user-facing progress report instead.

## Handoff

Final replies should state:

- what artifact changed
- which derived PDFs/TeX/slides/zip files were refreshed or intentionally left
  unchanged
- where the authoritative files are
- what sources were inspected
- what verification ran
- what user feedback was incorporated
- what remains unresolved
