# Round Log

Quick-scan run: predecessor identification and identity verification for
arXiv:2606.13790. One round (R0001).

## Call Ledger

This table is the only authoritative budget counter; the budget line in
`research_state.md` mirrors it. One search query = one call, one URL fetch =
one call; retries, failed, and blocked calls count too. Local file reads
(the skill's SKILL.md, references, templates, and re-reads of already-fetched
response bodies) are free and not logged.

Budget granted: 10 calls. Used: 5. All five succeeded; none failed, timed out,
or was blocked.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | Full text of the focal paper plus its complete 58-entry bibliography. Yielded E0001-E0008 (C3/C4) and every candidate in the pool. Identified the two requested families and the specific refs [55], [48], [10], [43], [49], [6], [8], [9], [34], [3], [54], [12], [35], [51], [40], [18], [41]. | 1/10 |
| 2 | R0001 | fetch | https://export.arxiv.org/api/query?id_list=2111.15141,2302.13834,2211.01364,2307.01198,2307.01050,2410.02711,1904.12072,2309.17082,2201.08862,2007.07115&max_results=20 | 10 of 10 records returned (`totalResults` 10). Verified title, authors, versioned ID, categories, `journal_ref`, DOI for P0001-P0006, P0010-P0012, P0014. Yielded E0009-E0018. | 2/10 |
| 3 | R0001 | search | arXiv API, `ti:"stochastic normalizing flows" OR ti:"trajectory balance"`, 40 results, ascending by submission date | 20 records. Resolved the two predecessors whose arXiv IDs the focal bibliography omits: P0013 (2002.06707) and P0009 (2201.13259). Also exposed the same-title collision with 2002.09547 (Hodgkinson et al.), and returned identity fields for P0015, P0027, P0028. Yielded E0019-E0021. | 3/10 |
| 4 | R0001 | fetch | https://export.arxiv.org/api/query?id_list=2512.19575,2605.11199,2211.03470,2502.02127&max_results=10 | 4 of 4 records returned. Verified the same-collaboration lattice lineage P0016-P0019, and caught the Shile-vs-Shiyang Chen author-initial ambiguity. Yielded E0022-E0025. | 4/10 |
| 5 | R0001 | search | arXiv API, `ti:"GFlowNet Foundations" OR ti:"Flow Network based Generative Models for Non-Iterative Diverse Candidate Generation"` | 2 of 2 records returned. Verified P0007 (2106.04399) and P0008 (2111.09266), completing the trajectory-balance lineage cited as refs [8] and [9] with no arXiv IDs in the focal bibliography. Yielded E0026-E0027. | 5/10 |

Cost note: batching kept identity verification to 4 calls for 19 records.
One-fetch-per-paper would have exceeded the budget before the lattice branch was
reached.

## R0001

**Date:** 2026-08-12
**Intent mode:** locate (secondary: learn)
**Round goal:** Identify the prior methods arXiv:2606.13790 directly builds on
in two families — learned/neural samplers for unnormalized targets, and learned
samplers for lattice field theory — and verify each one's exact title, authors,
and arXiv ID from sources actually visited in this run.
**Current state summary:** New run directory; no prior state to reconcile.
`output_manifest.md` was created first with all four remaining run files at
`planned`, before any web call.

### Diagnosis

- Seed recall: one seed given by the user (the focal paper). Highest-value first
  action is fetching that seed's full text, because the question is about the
  paper's own declared lineage and the answer set is defined by its Section 1 and
  its bibliography rather than by keyword search.
- Topic coverage: two named families, plus a third group (trajectory balance)
  that the paper treats as the source of its central mechanism and that the task
  wording does not anticipate.
- Author coverage: several antecedents share authors with the focal paper
  (Aarts, Zhou, Qian, Chen), so a same-collaboration lineage pass was needed
  beyond the two named families.
- Citation closure: backward only. No forward-citation pass at quick level.
- Confirmed/unconfirmed ratio at start: 0 / 0.
- Biggest missing risk at start: asserting predecessor identities from model
  memory instead of a fetched record — for instance the two distinct 2020 arXiv
  papers titled "Stochastic Normalizing Flows", where memory alone would pick
  the wrong ID roughly half the time.

### Chosen Action

**Action:** `locate_source` — (1) fetch the focal paper's full text once to
harvest both the lineage statements and the bibliography; (2) verify identities
in batched arXiv API queries rather than one fetch per paper.
**Why this action was chosen:** the arXiv API accepts a comma-separated
`id_list` and boolean title queries, so one call can authoritatively verify many
records at once. This converts a ~20-call task into a 4-call task and leaves
budget headroom for surprises.
**Expected gain:** high — identity verification for the full in-scope set.
**Expected cost:** 4-6 calls of 10.

### Execution Result

- New candidates: 40 (P0000 focal, P0001-P0019 in-scope predecessors,
  P0020-P0039 cited-but-unreached, plus 4 excluded groups X0001-X0004).
- New confirmed papers: 19 (P0001-P0019). Eighteen at C2, P0015 at C1.
- New unconfirmed papers: 20 (P0020-P0039), all `C1(bib-of-C4)`.
- New excluded papers: 4 exclusion groups, with reasons, not deleted.
- New EvidenceIDs: E0001-E0027. E0001-E0008 are focal-paper full-text/quote
  evidence at C3/C4; E0009-E0027 are independent arXiv identity records at
  C1/C2.
- New graph edges: none recorded — `graph_mode` is off and no relation ledger
  was requested. Lineage relations live in the candidate-pool family sections.
- New risks found:
  - Title collision: two 2020 arXiv papers named "Stochastic Normalizing Flows"
    (2002.06707 Wu/Köhler/Noé versus 2002.09547 Hodgkinson et al.). Resolved by
    matching the focal paper's cited author list.
  - Author-initial ambiguity: the focal bibliography's "S. Chen" for the
    Fourier-flow paper is Shile Chen, not focal-paper author Shiyang Chen.
  - Venue disagreement for P0005: the focal paper cites ICLR 2024, the arXiv
    comment field names an ICML 2023 workshop. Both recorded; neither
    overwritten.
  - Single-channel verification: arXiv only, so reference 34's cross-validation
    rule is unmet. Logged as ERQ0001 rather than glossed.

### Answer Produced This Round

Family A, data-free learned samplers for unnormalized targets (the family the
paper says it adapts): Path Integral Sampler 2111.15141; Denoising Diffusion
Samplers 2302.13834; the optimal-control/DIS formulation 2211.01364; improved
sampling via learned diffusions 2307.01198; Controlled Monte Carlo Diffusions
2307.01050; NETS 2410.02711.

Family B, the trajectory-balance mechanism: GFlowNets 2106.04399; GFlowNet
Foundations 2111.09266; Trajectory Balance 2201.13259.

Family C, learned samplers for lattice field theory: flow-based MCMC 1904.12072;
diffusion models as stochastic quantization 2309.17082; stochastic normalizing
flows 2002.06707 and their lattice non-equilibrium form 2201.08862 (with
2210.03139); thermodynamic-observable estimation 2007.07115; and the
same-collaboration antecedents 2211.03470, 2502.02127, 2512.19575, 2605.11199.

### File Patches

Files updated this round:

- output_manifest.md: created first, before any web call, with all four
  remaining run files at `planned`; rows moved to `on_disk` after each file
  landed, then to `verified` after the validator run.
- research_state.md: created — mode schema, scope, budget mirror (Used: 5 of
  10), root config, findings summary, stop status, validator result.
- candidate_pool.md: created — focal paper, three confirmed family tables,
  unconfirmed `C1(bib-of-C4)` table, exclusions with reasons, two
  deduplication decisions.
- evidence_registry.md: created — E0001-E0027 plus four unverified-evidence
  requests (ERQ0001-ERQ0004).
- round_log.md: created — this call ledger and round entry.
- search_route_log.md / relation_ledger.csv / missing_risk_report.md: not
  applicable at quick scan level; not created, and not claimed anywhere.

### Validator

Closing action of the round:
`python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py <this run directory>`
-> profile `literature`, status **CONSISTENT**, 4 manifest rows, 0 errors,
0 warnings, exit code 0. Result mirrored in `research_state.md`.

### Next Best Action

**Recommended next action:** if this arm is promoted beyond a quick scan, spend
2-3 batched `id_list` calls to clear P0020-P0039 from `C1(bib-of-C4)` to C2, then
add a second verification channel (publisher DOI pages) for the confirmed set to
satisfy reference 34's cross-validation rule.
**Reason:** those are the two known evidence-strength gaps; neither changes the
answer to the question as asked.
**User input needed:** scope choice — quick scan is complete as specified.

### Stop Decision

**Stop status:** saturated_under_budget
**Reason:** every predecessor the focal paper names in the two requested
families has both an author statement (C4 quote) and an independently fetched
arXiv record (C2), with 5 of 10 calls unspent. Remaining risks are recorded in
`research_state.md` and as ERQ rows rather than resolved by guessing.
