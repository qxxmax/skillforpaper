# Iterative Literature Loop

Use this reference when the user asks for literature review, market research,
related work, novelty positioning, proposal background, citation grounding, or
source verification.

## Gate

At the start of a play-the-toy-with-children task, ask or infer the scan level:

- None: stay within provided/local material.
- Quick: 5-15 high-signal sources, enough to identify likely neighbors and
  novelty risks.
- Full: broad same-field comparison with seed search, backward/forward
  snowballing, source verification, and a gap ledger.
- Monitor: repeat the loop when the thesis, method, proposal aims, slide story,
  or reviewer objections change.
- High-recall overlay: when missed sources carry high risk, read
  `references/28_high_recall_search_optimization.md` and define a search
  objective, route plan, screening log, coverage estimate, and stopping rule
  before claiming the scan is complete enough.

Do not force the gate if the user explicitly says to skip literature work.  If
the task involves current literature, funding calls, policies, venues, prices,
or other unstable facts, verify with current sources before using them.

## Hard Rules

- Never produce a literature comparison without a literature matrix.
- Never stop a full scan without a reviewer-comparison matrix.
- Never stop a full scan without an author/lab/method-lineage snowballing pass.
- Never stop a full or high-recall scan without a route log, seed/facet map,
  candidate screening table, and coverage/stopping report.
- Never feed literature into proposal, slides, or paper revision without
  updating the claim/evidence ledger or explicitly marking that no claim changed.
- Never treat a source as verified unless it has a primary source, DOI/arXiv
  page, official repository, publisher page, venue page, or equivalent
  authoritative source.

## Loop

Run the literature loop as rounds, not a one-shot search:

0. User checkpoint: confirm no/quick/full/monitor scan and whether the target is
   proposal, paper introduction, slides, rebuttal, or skill design.  Also ask
   for the screenshot policy when provenance matters.
1. Optimization contract for full/high-recall scans: define relevance,
   exclusions, objective mode, budget, route families, and stopping standard.
2. Seed map: extract field clusters, known baselines, likely reviewer
   comparisons, and user-provided must-cite or must-avoid sources.
3. Broad search: find review papers, representative works, official repos, and
   benchmark or dataset sources for each cluster.
4. Lineage snowballing: for each seed, must-cite paper, direct baseline, and
   reviewer-critical source, search the author network, lab/group trail,
   project lineage, citing works, prior works by the same group, follow-up
   works by the same group, and method-family neighbors.  Record this in
   `lineage_snowball_map.md`.  This is mandatory for full scans because it
   catches continuous work from the same authors, the same research circle, and
   the same method spectrum that keyword-only searches often miss.
5. Focused search: select the most relevant 3-7 works per cluster and fill the
   literature matrix.
6. Citation snowballing: inspect references and citing works for seed papers, direct
   baselines, and reviewer-critical sources when novelty or baseline coverage
   remains uncertain.
7. Coverage check for full/high-recall scans: record seed recall, independent
   route overlap, facet saturation, estimated missing items when possible, and
   whether another search round is expected to change the argument.
8. Gap synthesis: write what others solved, what they did not solve, what this
   project solves, and what this project still does not solve.
9. Argument update: revise proposal intro, related work, slide motivation,
   paper positioning, or skill rules; update the claim/evidence ledger.
10. Stop/continue decision: if a new conceptual cluster appears, run another
   focused round; if no new cluster changes the argument, freeze a literature
   snapshot and switch to monitor mode.

## Comparison Matrix

Maintain a table with these columns:

- Work/source
- arXiv ID
- DOI
- Publisher/journal/official page URL
- Source-page screenshot path
- Metadata verified date
- Year/venue/status
- Problem or task
- Method/mechanism
- Correctness, validation, or trust mechanism
- Data/evidence
- Main result
- Limitation or open gap
- Relation to our claim
- Baseline/comparison role
- Citation status and BibTeX key

For non-paper market research, replace venue with organization/product and add
"adoption signal" and "what users buy or use it for."

Use `templates/literature_matrix_template.md` when creating a file artifact.

## Provenance Evidence

For each must-cite paper, direct baseline, or reviewer-critical comparison,
record a provenance bundle:

- arXiv ID, when available.
- DOI, when available.
- Publisher, journal, conference, dataset, or official repository URL.
- Source-page screenshot path, stored under the task artifact directory.
- Local PDF or downloaded metadata path, if available.
- Metadata verified date.
- BibTeX key or citation key.

Let the user choose the screenshot policy:

- none: record links and metadata only.
- key-only: capture screenshots only for must-cite papers, direct baselines,
  reviewer-critical comparisons, disputed sources, and numerical-claim sources.
- all: capture screenshots for every matrix row.
- on-demand: leave screenshot cells blank until the user asks for specific
  provenance captures.

If the user does not specify a policy, default to key-only for full scans and
on-demand for quick scans.

Screenshots are audit evidence, not default public content.  For public
proposal/slides/paper artifacts, cite the source and use the screenshot only
when permission and context make it appropriate.  Avoid screenshots of full
copyrighted article text; prefer the official landing page showing title,
authors, venue, DOI/arXiv ID, abstract snippet, and date captured.

## Reviewer-Comparison Matrix

For proposal, slides, rebuttal, or paper-introduction work, maintain a second
matrix:

- Reviewer may ask
- Relevant literature
- Our answer
- Evidence
- Risk
- Artifact location

This matrix answers questions such as: why not this baseline, why now, what is
new beyond the adjacent method family, which limitation remains, and which
claim should be softened.

Use `templates/reviewer_comparison_matrix_template.md` when creating a file
artifact.

## Lineage Snowball Map

For full scans, maintain a third map that prevents two common blind spots:

- Missing the same author, same lab, same research circle, or project sequence.
- Treating each paper as isolated instead of seeing the method-family lineage.

Track:

- Seed work.
- Shared authors, labs, grants, datasets, codebases, instruments, or platforms.
- Earlier work by the same authors or group.
- Later work by the same authors or group.
- Adjacent method-family work by other groups.
- Citing works that directly change novelty, baseline coverage, or reviewer risk.
- What the lineage adds to the argument.
- Whether the paper becomes must-cite, context-only, monitor-only, or excluded.

Use `templates/lineage_snowball_map_template.md` when creating this artifact.

## Gap Ledger

Separate:

- Established fact: directly supported by verified sources.
- Neighboring claim: supported by related work but not exactly our result.
- Our evidence: supported by local data/code/experiments.
- Open risk: plausible but unverified.
- Forbidden claim: not supported and should not appear in the paper, proposal,
  or slides.

## Iteration Triggers

Repeat the loop when:

- The user changes the topic, thesis, target audience, venue, or funding call.
- A proposal aim needs "why now" or "why us" evidence.
- A slide needs a literature figure, baseline, or comparison.
- A reviewer objection introduces a missing baseline or citation.
- A result fails, a new experiment changes the supported claim, or a figure
  exposes a hidden boundary.
- Sources may be stale or the user asks for latest work.

## Stop Conditions

For a full scan, stop only when:

- `search_scope.md`, `search_route_log.md`, `candidate_screening_table.md`, and
  `coverage_stopping_report.md` exist or are explicitly marked not applicable.
- The seed set is recovered, or misses are explained with a concrete source or
  access limitation.
- At least two independent route families were used, such as lexical, semantic,
  citation, author/venue, database-specific, grey-literature, or repository
  search.
- Each major cluster has at least three representative works or an explicit
  reason why fewer exist.
- Each direct baseline has a one-sentence contrast.
- Each seed or reviewer-critical source has an author/lab/method-lineage pass,
  or an explicit reason why lineage search was impossible.
- Each main claim has a source, local figure/table, formula, or explicit
  unsupported marker.
- No new conceptual cluster appears for two consecutive focused rounds.
- The proposal/slides/paper motivation no longer changes its main line.

Before stopping, run an adversarial search pass for:

- same method but older
- negative result
- scaling limitation
- benchmark or dataset that contradicts the claim
- review paper that frames the field differently

Then freeze a literature snapshot with date, sources searched, query families,
included/excluded clusters, unresolved risks, and monitor triggers.  Use
`templates/literature_snapshot_template.md` when writing this file.

## Output Contract

Return these artifacts when the loop is active:

- Landscape summary: what the field has already done.
- Search optimization package: scope, route log, screening table, and
  coverage/stopping report when full/high-recall mode is active.
- Comparison matrix: who did what, with verified source links.
- Reviewer-comparison matrix: likely objections and evidence-backed answers.
- Lineage snowball map: same-author, same-lab, same-method-family, citing, and
  follow-up work that changes novelty or reviewer risk.
- Gap ledger: what remains unsolved and what our work can responsibly claim.
- Novelty statement: one paragraph and one sentence.
- Citation shortlist: must-cite, useful context, and optional background.
- Visual candidates: literature timeline, method taxonomy, baseline map,
  problem-method-evidence funnel, or claim-boundary panel.
- Literature snapshot: frozen state, monitor triggers, and remaining risks.
- Provenance bundle: arXiv/DOI/official page/screenshot paths for key works.
- Sentence/result bank: reusable supported sentences for proposal, slides,
  paper introduction, rebuttal, captions, and limitations.
- Quality gate checklist: pass/fail status before literature-derived prose is
  promoted into an artifact.

Never fabricate references.  Mark unverified citations and claims explicitly.
