# Review Response And Revision Loop

Use this reference when reviews arrive, when the user asks to write a
rebuttal or revision, or when preparing a resubmission (Part 5).

## Intake: Comment Decomposition

Decompose every review into atomic comments in
`review_response_matrix.csv` before writing any response prose. One row per
distinct point; a reviewer paragraph often contains 2-4 rows. Each row keeps
the reviewer's verbatim quote (truncated to the operative sentence),
so the response can never drift from what was actually asked.

Classify each row:

| class | meaning | default action |
|---|---|---|
| `factual_error_ours` | reviewer found a real defect | fix manuscript, thank, show the fix |
| `misread` | reviewer misunderstood existing text | clarify the text (the misread is evidence the text failed), point to revision |
| `scope_request` | asks for work beyond the paper's claim | add boundary statement or targeted experiment; may decline with reason |
| `new_experiment` | asks for a run | route to Part 3 with a compute estimate before promising anything |
| `citation_request` | asks to cite/discuss work | route to Part 1 for verification before citing |
| `subjective` | taste or framing disagreement | respond once, respectfully, with evidence; do not argue in circles |

## Response Discipline

- Respond to **every** row. Silence on a point reads as concession or evasion.
- Order responses by reviewer, in the reviewer's order; never merge two
  reviewers' points into one answer.
- Each response has three parts: (1) restate/quote the point, (2) the answer
  with evidence pointers (page/line/figure of the revision, or a ledger ID),
  (3) what changed in the manuscript, verbatim where short.
- Never claim a change that was not made; the revision diff ledger (below) is
  checked against the response before sending.
- Disagreement is allowed and sometimes required, but only with evidence and
  without heat. Write "we respectfully disagree because [evidence]", not
  concession to a point that is wrong.
- If reviewers contradict each other, say so explicitly and state which path
  the revision takes and why.
- Rebuttal windows with length limits: budget space by row class —
  `factual_error_ours` and `new_experiment` rows get space first;
  `subjective` rows get one sentence each.

## Revision Diff Ledger

Track every manuscript change in `revision_diff_ledger.md`: location
(section/paragraph), old text (short quote), new text (short quote), and the
matrix row(s) that motivated it. Changes with no motivating row are allowed
(self-caught defects) but must still be logged — reviewers notice unexplained
changes. Before sending, run `validate_review_response.py`: every matrix row
must have a response and a disposition; every `revised` disposition must
reference at least one diff ledger entry.

## New Experiments Under Deadline

A rebuttal-window experiment is a Part 3 run with a hard deadline: write the
experiment contract first, cap the compute, and decide in advance what result
is worth reporting. A rushed result that cannot be defended is worse than
"this experiment requires X and is out of scope for the rebuttal window; we
commit to including it in the revision."

## Outcome Handling

| outcome | action |
|---|---|
| accept | final-version gate: apply mandatory edits, re-run submission gate items (reference 44), update arXiv |
| minor/major revision | full loop above; the revision letter is the response matrix rendered as prose |
| reject | post-mortem row per reviewer point: valid (fix before resubmission) vs venue-specific (note and move on); update selection matrix; do not resubmit elsewhere unchanged if any `factual_error_ours` row is open |
| desk reject | record reason; back to reference 44 selection matrix |

All outcomes update `research_state.md` and the interaction log.
