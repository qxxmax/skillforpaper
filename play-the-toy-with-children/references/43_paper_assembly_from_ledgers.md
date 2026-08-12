# Paper Assembly From Ledgers

Use this reference when the user asks to write, assemble, restructure, or
finalize a paper manuscript (Part 5). Part 5 turns verified ledgers into a
submission; it does not create new evidence. A missing source goes back to
Part 1, a missing technical understanding goes back to Part 2, and a missing
result goes back to Part 3.

Part 5 runs are runs: the Minimal Run Contract and the three run-state laws
apply (`output_manifest.md` first, per-call ledger in `round_log.md`, state
never leads the disk).

## Boundary Between Parts

| Part | Main question | Stop condition |
|---|---|---|
| Part 3 | What did we build and what do the results support? | validated claims with experiment evidence |
| Part 5 | Is the manuscript assembled, venue-fit, submitted, and revised? | accepted, withdrawn, or explicitly parked with recorded state |

## Sentence-To-Evidence Discipline

Every substantive sentence in the manuscript must trace to one of:

- a Part 1 `EvidenceID` (literature claims);
- a Part 3 `validated_claim` row (own results) or, before Part 3 exists, a
  local figure/table/log with a recorded path;
- an explicit boundary/limitation statement.

Maintain the trace in `claim_evidence_ledger.md`. A sentence that traces to
nothing is either deleted or rewritten as an explicitly marked open question.
Comparative and superlative sentences ("first", "state of the art",
"outperforms") additionally need the reviewer-comparison matrix row that
defends them.

## Assembly Order

Write in this order; do not start prose before step 3 is stable:

1. Claim skeleton: the main claim, 3-5 supporting claims, and each one's
   evidence pointer.
2. Figure/table plan: which figure carries which claim; every planned figure
   names its data source and generating script.
3. Outline against the venue profile (see reference 44): section budget in
   pages, appendix split.
4. Section drafts from the ledgers, least-certain sections first (results and
   limitations before introduction).
5. Introduction and abstract last, from the frozen claim skeleton.

Keep the complete source map separate from the selected argument (the
Focus And Completeness Rule of `SKILL.md`).

## Submission Package Manifest

Track every submission artifact in `submission_package_manifest.md`: main PDF,
appendices, code/data availability statement, checklist, cover letter, arXiv
version, and their mutual consistency (same title, same author list, same
numbers in abstract and results).

## Venue Checklists Are Rubrics

Machine-learning venues score the checklist; treat every item as a claim that
reviewers verify. Answer honestly: a justified "no" (for example, "error bars
omitted because the compute cost of repeated training is prohibitive") is
acceptable and safer than an unsupported "yes" — an unsupported "yes" is a
verifiable false statement in the permanent record. For every "yes", point to
the section that backs it. Physics journals (PRL/JHEP style) have no formal
checklist; apply the same discipline through the submission package manifest.

## Numbers Freeze

Before submission, freeze every number that appears in the abstract,
introduction, or conclusions and check it against its source figure/table/log.
Record the freeze in `claim_evidence_ledger.md` with the check date. A number
that appears in prose but not in any frozen source is a blocker.

## Stop Conditions

Stop the assembly phase only when:

- every substantive sentence has a ledger trace or an explicit boundary mark;
- the figure plan is fully realized or gaps are explicitly parked;
- the submission package manifest is complete and internally consistent;
- the venue gate (reference 44) passes;
- exports are refreshed per `references/31_artifact_refresh_and_export_gate.md`.
