# High-Recall Search Optimization

Use this reference when a task is not just to answer from known sources, but to
find as many relevant sources/items as possible under time, API, access, or
screening constraints.  This includes full literature scans, systematic or
scoping reviews, prior-art searches, source triangulation, dataset/tool
discovery, legal/eDiscovery-style review, and internal workflow search.

In the intent-mode taxonomy from
`references/33_literature_intent_modes_and_state_loop.md`, this is the `cover`
mode: high-recall search that minimizes missed-literature risk.  It can contain
`locate`, `learn`, and `evaluate` actions, but its stop rule is coverage and
residual-risk based.

## Core Idea

Treat search as a sequential optimization problem:

```text
choose next action = argmax expected marginal utility / expected cost
```

The action may be a Boolean query, BM25/lexical search, dense/semantic search,
citation chasing, author/venue search, repository search, grey-literature
search, full-text acquisition, or another screening round.

The goal is not "the model searched once."  The goal is to justify why the
current source set is sufficient for the decision, claim, proposal, paper, or
review being written.

## Token And Cost Model

Every search action has a weighted cost:

```text
weighted_cost(a) =
  w_tok * Tok(a) +
  w_time * Time(a) +
  w_money * Money(a) +
  w_risk * Risk(a)

score(a) = E[DeltaUtility(a)] / weighted_cost(a)
```

Token policy must be recorded before deep search:

| policy | behavior |
|---|---|
| strict | keep only highest decision-value evidence in the main answer |
| balanced | default; use route logs, key papers, gaps, and next steps |
| generous | run more routes and include graph/evidence diagnostics |
| no_budget | externalize state into files and continue by batches until stopping rules pass |

`no_budget` means persistent files and multi-round audit, not one giant answer.
Use `templates/search_budget_contract_template.md`.

## Decision Contract

Before searching, define these in `search_scope.md`:

- Relevant item: what counts as in scope.
- Exclusion rule: what looks related but should be excluded.
- Objective mode:
  - High-recall: minimize missed relevant items subject to budget.
  - Scoping: maximize facet coverage, novelty, and representativeness.
  - Decision: continue only while more evidence could change the decision.
- Budget: time, searches, APIs, full-text access, and human screening.
- Stopping standard: target recall, saturation, residual-yield threshold,
  capture-recapture/Chao estimate, random safety sample, or decision
  sufficiency.
- Audit standard: source log, query log, deduplication log, screening reasons,
  and limitations.

Use `templates/search_scope_template.md` when creating the file.

Also create or update `research_state.md`, `candidate_pool.md`,
`evidence_registry.md`, `round_log.md`, and `output_manifest.md` when the
search will run across multiple rounds or feed a public report.  Use the
templates listed in `references/33_literature_intent_modes_and_state_loop.md`.

## Route Plan

Do not rely on one query or one source when completeness matters.  Build
independent search routes and record them in `search_route_log.md`.
For channel-family coverage, required source sets, cross-validation rules, and
N-generation citation expansion, also read
`references/34_channel_lineage_and_cross_validation_gate.md`.

Use route families such as:

- Lexical: Boolean strings, exact phrases, BM25, controlled vocabulary.
- Semantic: embedding or natural-language search against papers, abstracts, or
  full text.
- Citation graph: backward references, forward citations, co-citation, related
  papers.
- Author/venue/lab: known groups, instruments, datasets, grants, venues, and
  project names.
- Repository/source-specific: arXiv, PubMed, Semantic Scholar, Crossref,
  OpenAlex, GitHub, dataset registries, patent databases, standards bodies.
- Grey or negative evidence: theses, reports, clinical registries, issue
  trackers, benchmark failures, withdrawn or contradicted work.

For each route, write its expected strength and blind spot.  Overlap across
routes is evidence for coverage; non-overlap reveals missing facets.

Create `channel_coverage_plan.md` when route coverage itself is part of the
claim or when the user will present the workflow as an auditable method.

## Seventeen-Point Priority Ladder

Use this order when search, screening, graphing, and writing compete for token
or time budget:

1. Scope / research question.
2. Inclusion / exclusion rules.
3. User budget policy.
4. Seed / sentinel set.
5. Source selection.
6. Exact terms / controlled vocabulary.
7. Semantic expansion.
8. Independent search routes.
9. Deduplication / provenance.
10. Relevance probability.
11. Evidence hierarchy / study design.
12. Quality / bias / retraction risk.
13. Citation graph position.
14. Citation intent / relationship.
15. Facet coverage.
16. Residual risk / stopping rule.
17. Output packaging / audit report.

## Retrieval And Fusion

When routes return ranked lists, fuse ranks rather than trusting one score:

```text
RRF(d) = sum over routes 1 / (k + rank_route(d))
```

Use rank fusion when scores are not calibrated.  Track route provenance for
each candidate because a paper found by lexical + citation routes carries a
different coverage signal than a paper found only by one semantic query.

## Screening Loop

Run search in rounds:

1. Deduplicate candidates.
2. Rank by expected value per cost: relevance probability, source value,
   missing facet value, and review/acquisition cost.
3. Screen top candidates.
4. Label include / exclude / uncertain with a short reason.
5. Extract new terms, authors, venues, datasets, methods, and facets.
6. Update query routes and repeat.

Use `templates/candidate_screening_table_template.md` for reviewed candidates.

For high-recall workflows, prioritize likely relevant items first, but inject a
small uncertainty/random safety sample when stopping depends on residual-risk
estimation.

## Candidate Pool Adequacy Gate

Before synthesis or polished prose, check whether the candidate pool is large
enough for the user's purpose.  If not, read
`references/30_candidate_pool_expansion_gate.md` and create
`high_recall_expansion_plan.md` from
`templates/high_recall_expansion_plan_template.md`.

Suggested defaults:

| purpose | minimum candidate pool | minimum relevant records | minimum green-check records |
|---|---:|---:|---:|
| quick orientation | 20-40 | 8-15 | 3-8 |
| teaching/demo checkpoint | 60-100 | 25-50 | 10-20 |
| proposal/slides with novelty claims | 80-150 | 40-70 | 15-30 |
| paper related-work section | 120-250 | 60-120 | 20-50 |

Do not use global count alone.  Major facets should have their own quotas.  If
any required facet is thin, continue expansion even if the total count looks
large.

## Coverage And Stopping

Do not claim "complete"; report residual risk.  Use several diagnostics in
`coverage_stopping_report.md`:

- Seed recall: did the strategy recover known relevant seed items?
- Route overlap: how many included items are found by multiple independent
  routes?
- Capture-recapture: estimate unseen relevant items from route overlaps when
  assumptions are plausible.
- Chao-style estimate: use singleton/doubleton discoveries across routes or
  rounds to estimate residual unseen items.
- Saturation: consecutive reviewed items or rounds without a new include,
  tracked by facet rather than only globally.
- Facet coverage: each required method family, task, dataset, instrument,
  reviewer-risk cluster, or claim boundary has evidence or a documented gap.
- Decision sufficiency: further search is unlikely to change the proposal,
  slide spine, paper claim, or reviewer answer.
- Channel closure: required channel families have been searched or marked
  blocked with blind spots.
- Generation closure: N-generation citation/author/topic expansion has low
  marginal yield by facet and returns mostly duplicates, out-of-scope records,
  or low-priority candidates.

Stop only when the selected stopping standard is met, or when the remaining
gaps are explicitly named as limitations.

Use `templates/coverage_stopping_report_template.md` when creating the report.

## Green-Check Evidence Rule

A paper/item receives `green_check` only when all four gates pass:

```text
GREEN_CHECK = relevance_gate
           AND provenance_gate
           AND quality_gate
           AND contribution_gate
```

Do not promote a citation-count-only, abstract-only, or background-only item to
core evidence.  Use `secondary`, `uncertain`, `caution`, or `excluded` when one
gate is weak or failed.

## Research Basis To Remember

This workflow is aligned with known lines of work:

- Information foraging: maximize valuable information gained per unit effort.
- Probabilistic information retrieval, BM25, and relevance ranking.
- Relevance feedback and Rocchio-style query refinement.
- Rank fusion, including reciprocal rank fusion for combining retrieval routes.
- Systematic-review reporting and search design norms such as PRISMA-S, PRESS,
  and Cochrane-style search planning.
- Technology-assisted review, total-recall retrieval, active-learning screening,
  and conservative stopping rules.
- Capture-recapture, Chao-style residual estimates, and value-of-information
  stopping for deciding whether another search/screening round is worth the
  cost.

When writing a public method section or paper claim from this basis, verify the
specific citations with primary sources before citing them.

## Failure Modes

- One-shot LLM search presented as complete.
- One database only, with no route-diversity caveat.
- Pure semantic search that misses exact technical terms or identifiers.
- Pure keyword search that misses synonym drift or interdisciplinary terms.
- Global saturation that hides a missing subfield/facet.
- Query expansion that is not logged and cannot be reproduced.
- Stop decision based on fatigue rather than a stated standard.

## Integration With Literature Loop

For `play-the-toy-with-children`, this reference is a front-end optimization layer:

1. It starts from the intent-mode and state loop in
   `references/33_literature_intent_modes_and_state_loop.md`.
2. It uses `references/34_channel_lineage_and_cross_validation_gate.md` when
   channel coverage, cross-validation, or N-generation expansion must be
   auditable.
3. It creates `search_budget_contract.md`, `search_scope.md`,
   `search_route_log.md`, `candidate_screening_table.md`, and
   `coverage_stopping_report.md`.
4. Included and uncertain items feed the `literature_matrix.md`.
5. Route and coverage gaps feed `gap_ledger.md` and
   `reviewer_comparison_matrix.md`.
6. DOI, URL, screenshot, quote, and page evidence move into
   `evidence_registry.md` with `EvidenceID`.
7. Supported claims move into `claim_evidence_ledger.md` and
   `sentence_result_bank.md`.
8. Only after these files are stable should proposal, slides, paper prose, or
   rebuttal prose be polished.
