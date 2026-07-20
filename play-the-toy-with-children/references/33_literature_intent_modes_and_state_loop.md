# Literature Intent Modes And State Loop

Use this reference before literature research, source verification, graph
navigation, or report export.  The workflow is not a one-shot search assistant;
it is an iterative, evidence-aware, graph-based literature recall optimizer.

## Contents

1. Intent modes
2. Mode schema
3. Required state files
4. State write order
5. Call ledger
6. Interrupted-run recovery
7. Evidence registry
8. Mode-specific scoring
9. Multi-round loop
10. User commands
11. Required round response

## Intent Modes

Classify the user's request into one primary intent mode before searching.

| mode | Chinese shorthand | English shorthand | objective |
|---|---|---|---|
| `locate` | find the source | known-item search | find and verify a specific paper, quote, DOI, dataset, tool, or original source |
| `learn` | build understanding | map-building search | build a topic map and reading path with low learning cost |
| `evaluate` | judge a claim | claim-evaluation search | decide whether a claim is supported, refuted, mixed, or uncertain |
| `cover` | minimize missed literature | high-recall search | reduce the risk of missing relevant literature under stated budgets |

Do not use `argue` as a primary mode.  It can invite confirmation bias.  Use
`evaluate` and actively look for supporting, opposing, mixed, null, and boundary
evidence.

Do not promise absolute `exhaustive` or `full` coverage.  Use `cover` or
`high-recall` and report the remaining missed-literature risk.

If multiple modes apply and the user does not choose, select the highest-risk
mode as primary:

```text
cover > evaluate > learn > locate
```

`locate` is often a sub-action inside the other modes.

## Mode Schema

Record mode decisions in `research_state.md`:

```yaml
intent_mode:
  primary: locate | learn | evaluate | cover
  secondary: locate | learn | evaluate | cover | none

risk_level: low | medium | high

current_action:
  locate_source
  build_topic_map
  collect_supporting_evidence
  collect_opposing_evidence
  expand_query
  chase_citations
  expand_author_network
  verify_full_text
  generate_lineage_graph
  audit_exclusions

output_mode:
  answer
  citation
  reading_path
  evidence_table
  citation_list
  lineage_graph
  audit_package
```

Examples:

```yaml
intent_mode:
  primary: cover
  secondary: learn
current_action: build_topic_map
output_mode: audit_package
```

```yaml
intent_mode:
  primary: evaluate
  secondary: locate
current_action: locate_source
output_mode: evidence_table
```

## Mode Details

### `locate`: Find The Source

Use when the user wants a known paper, quote, dataset, benchmark, tool, DOI,
arXiv record, PMID, official citation, or original source.

Objective:

- Minimize time to verified source.

Stop rule:

- Stop once a credible source and consistent metadata are verified.

Outputs:

- Canonical citation, DOI/arXiv/PMID/URL, and metadata verification notes.

### `learn`: Build Understanding

Use when the user wants to understand a field, learn concepts, identify major
branches, or create a reading path.

Objective:

- Maximize knowledge gain, topic coverage, and readability under limited
  reading time.

Stop rule:

- Stop when major concepts, schools, methods, datasets, and debates are covered
  well enough that more search only adds detail.

Outputs:

- `reading_path.md`, `topic_map.md`, key concepts, representative papers, and
  genealogy graph.

### `evaluate`: Judge A Claim

Use when the user wants evidence to support, refute, compare, or decide a
claim.

Objective:

- Maximize decision confidence and minimize confirmation bias.

Search must include:

- supporting evidence;
- opposing evidence;
- mixed or null results;
- limitations;
- replications;
- benchmark comparisons;
- boundary conditions.

Stop rule:

- Stop when the conclusion is stable and major counter-evidence has been
  checked.

Outputs:

- Claim-by-claim evidence table, support/opposition summary, evidence quality
  notes, and uncertainty report.

### `cover`: Minimize Missed Literature

Use when the user needs high recall, systematic/scoping-review quality,
complete citation coverage, prior-art search, related-work coverage, or
auditable completeness.

Objective:

- Maximize recall and minimize missed relevant literature under budget
  constraints.

Required loop:

1. query expansion;
2. multi-source search;
3. seed recall validation;
4. forward and backward citation chasing;
5. author/topic/venue expansion;
6. deduplication;
7. exclusion audit;
8. missing-risk reporting.

Stop rule:

- Stop only when seed recall, marginal yield, topic coverage, citation closure,
  and residual risk are acceptable.

Outputs:

- `confirmed_literature.md`, `unconfirmed_literature.md`,
  `included_literature.md`, `excluded_literature.md`, `search_log.md`,
  citation/topic/author graph, `missing_risk_report.md`, and audit package.

## Required State Files

For multi-round, `cover`, `evaluate`, graph, source-verification, or final
report workflows, create or update these files:

| file | role |
|---|---|
| `research_state.md` | current mode, scope, budget, root nodes, next action, stop status |
| `candidate_pool.md` | all candidate papers before confirmation, exclusion, or unconfirmed status |
| `evidence_registry.md` | all DOI, URL, screenshot, quote, page, and claim evidence |
| `round_log.md` | each round's diagnosis, action, result, file patches, next step |
| `output_manifest.md` | final Markdown/TeX/PDF/graph/audit outputs and refresh status |

Do not delete candidate papers silently.  Move them to confirmed,
unconfirmed, or excluded with reasons.

At every scan level, including quick scans, create `output_manifest.md`
**first**, listing each planned run file with status `planned`. The manifest is
a live run ledger, not a final delivery checklist.

## State Write Order

State files must never claim a file that is not on disk. A run that dies
mid-write must leave the manifest behind the disk, never ahead of it.

For every produced or updated file, follow this order:

1. Write the artifact file to disk.
2. Update its `output_manifest.md` row (`planned` → `in_progress` →
   `on_disk` → `verified`).
3. Only then may `research_state.md`, `round_log.md`, or a report reference
   the file as existing.

Manifest status values:

| status | meaning |
|---|---|
| `planned` | listed but not yet written |
| `in_progress` | partially written this round |
| `on_disk` | complete file exists at the recorded path |
| `verified` | checked by a validator or by manifest reconciliation |
| `needs_update` | source evidence changed after the file was written |

At the end of every round, the five state files must be mutually consistent:
every action in `round_log.md` has a manifest row, and every `on_disk` /
`verified` row has a real file.

## Call Ledger

`round_log.md` is the only authoritative budget counter. The budget line in
`research_state.md` is a mirror; when they disagree, the call ledger wins.

Every web search and every URL fetch gets one row, including retries and
failed calls:

```text
| # | RoundID | type | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | arxiv.org/abs/XXXX.XXXXX | full text, C4 anchors | 1/8 |
| 2 | R0002 | search | "topic keywords" | 3 new candidates | 2/8 |
```

Counting rules:

- One search query = one call. One URL fetch = one call.
- Retrying the same URL counts again.
- Local file reads, template reads, and reads of already-fetched content are
  free and are not logged here.

A full or high-recall scan additionally uses `search_budget_contract.md`; the
call ledger is the lightweight budget record for quick scans.

## Interrupted-Run Recovery

When entering a run directory that already contains state files (resuming your
own interrupted run or taking over another agent's), reconcile before doing
any new work:

1. Diff `output_manifest.md` against the disk. Rows claiming `on_disk` or
   `verified` with no file are demoted to `planned` and redone. Files on disk
   with no row are registered before use.
2. Recount the call ledger in `round_log.md` and correct the mirror in
   `research_state.md`.
3. Treat claims in `research_state.md` about produced files as unverified
   until step 1 confirms them.
4. Record the reconciliation as a round in `round_log.md` (action:
   `resume_reconciliation`), then continue the normal loop.

`scripts/validate_run_state.py <run-directory>` automates steps 1–2 and
reports mismatches; run it first when resuming.

## Evidence Registry

Every claim, screenshot, DOI, link, and full-text confirmation must receive an
`EvidenceID`.

Evidence types:

- `E_LINK`: link existence or source page evidence.
- `E_DOI`: DOI or identifier metadata.
- `E_ABSTRACT`: abstract-only relevance evidence.
- `E_FULLTEXT`: full-text availability.
- `E_SCREENSHOT`: page, table, figure, method, result, or claim screenshot.
- `E_QUOTE`: short quote supporting a specific claim.
- `E_METADATA_ONLY`: metadata evidence that must not support strong claims.

Verification levels:

| level | meaning |
|---|---|
| C0 | candidate only |
| C1 | metadata verified |
| C2 | abstract or source summary checked |
| C3 | full text checked |
| C4 | specific claim verified by page, quote, note, or screenshot |

Final reports must cite `EvidenceID`, not just `PaperID`.

A `PaperID` tells which paper is being discussed.  An `EvidenceID` tells why a
specific claim, figure, link, or metadata field is trusted.

Screenshots must be registered in `evidence_registry.md` before entering TeX,
PDF, slides, or a public report.

## Mode-Specific Scoring

Use simple weighted scores first; only add heavier algorithms when the task
requires it.

Locate:

```text
score =
  0.45 * title_match +
  0.25 * author_match +
  0.15 * year_match +
  0.10 * identifier_match +
  0.05 * source_reliability
```

Learn:

```text
score =
  0.25 * review_or_survey_value +
  0.20 * hub_score +
  0.20 * topic_diversity_gain +
  0.15 * readability +
  0.10 * genealogy_value +
  0.10 * freshness
```

Evaluate:

```text
score =
  0.30 * claim_relevance +
  0.25 * evidence_quality +
  0.15 * opposing_evidence_value +
  0.10 * replication_or_benchmark_value +
  0.10 * verification_confidence +
  0.10 * uncertainty_reduction
```

Cover:

```text
score =
  0.20 * relevance_to_question +
  0.15 * expected_recall_gain +
  0.15 * topic_coverage_gain +
  0.10 * author_coverage_gain +
  0.10 * personalized_pagerank +
  0.08 * exp(-dijkstra_distance) +
  0.08 * authority_score +
  0.06 * bridge_score +
  0.05 * freshness +
  0.05 * verification_confidence -
  0.07 * redundancy_penalty -
  0.05 * access_cost
```

After scoring, apply diversity reranking so the top results do not all come
from the same author, topic, venue, database, or method family.

## Multi-Round Loop

When the user says "continue", "next round", or asks why the literature count
is not enough, run one loop:

1. Load `research_state.md`, `candidate_pool.md`, `evidence_registry.md`,
   `round_log.md`, and `missing_risk_report.md` when present.
2. Diagnose the biggest current risk: missing seed, missing topic, missing
   author cluster, citation gap, access gap, database gap, recency gap, or
   evidence-strength gap.
3. Choose one next best action by expected marginal utility per expected cost.
4. Add new candidates to `candidate_pool.md`.
5. Register DOI, URL, screenshot, quote, and page evidence in
   `evidence_registry.md`.
6. Promote only verified papers into confirmed lists; keep important but
   unverified papers in unconfirmed lists.
7. Update graph nodes/edges and Dijkstra/PPR/HITS notes when graph mode is on.
8. Update `missing_risk_report.md`.
9. Append the round to `round_log.md`.
10. Update `output_manifest.md` if any derived Markdown, TeX, PDF, slide,
    graph, dashboard, XLSX, or zip export is affected.

## User Commands

The user may control the loop with these commands or natural equivalents:

| command | action |
|---|---|
| `start project` | initialize `research_state.md` and choose intent mode |
| `continue next round` | diagnose coverage, run one more round, update files |
| `locate only` | switch current action to `locate_source` |
| `expand keywords` | run query expansion and update search log |
| `chase backward citations` | expand ancestors and method foundations |
| `chase forward citations` | expand descendants, applications, and frontiers |
| `expand author network` | expand authors, coauthors, labs, and grants |
| `expand topic network` | expand topic clusters and semantic neighbors |
| `verify links` | verify DOI, URL, arXiv, PMID, official page, or database record |
| `add screenshot evidence` | register screenshots in `evidence_registry.md` |
| `update graph` | update citation, author, topic, and evidence edges |
| `generate evidence table` | create or update claim/evidence tables |
| `generate md report` | create Markdown report from current state |
| `generate tex report` | create TeX report and bibliography from current state |
| `prepare pdf report` | compile or list missing assets for PDF export |
| `stop and report risks` | generate missing-risk report and output manifest |

## Required Round Response

At the end of every multi-round loop, respond with:

```text
# Round RXXXX Result

## 1. What changed

## 2. New papers

### Confirmed
### Unconfirmed but potentially important
### Excluded

## 3. New evidence

| EvidenceID | PaperID | Type | What it verifies | ScreenshotRef / URL |
|---|---|---|---|---|

## 4. Graph update

- New nodes:
- New edges:
- Important Dijkstra paths:
- PPR/HITS ranking changes:

## 5. File patches

- research_state.md:
- candidate_pool.md:
- search_log.md:
- confirmed_literature.md:
- unconfirmed_literature.md:
- evidence_registry.md:
- genealogy_graph.md:
- missing_risk_report.md:
- round_log.md:

## 6. Remaining risks

## 7. Next best action

## 8. Continue/stop decision
```

Do not only say what was found.  Say which state files changed, which evidence
IDs were created, what remains unverified, and whether the next loop should
expand search, verify sources, improve graph closure, or export a report.
