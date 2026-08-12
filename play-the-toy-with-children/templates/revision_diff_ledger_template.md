# Revision Diff Ledger

One ledger per revision round. Every manuscript change gets a row, including
self-caught fixes with no reviewer row (`MatrixRows` = `self`). Before the
response letter is sent, `validate_review_response.py` checks this ledger
against `review_response_matrix.csv`.

- Manuscript version: [v1 → v2]
- Round: [rebuttal / revision 1 / ...]

## Changes

| DiffID | Location | Old (short quote) | New (short quote) | MatrixRows | Notes |
|---|---|---|---|---|---|
| D-01 | Sec 3.1, Eq. (3) | "minus sign example" | "plus sign example" | R1-01 |  |
| D-02 | Sec 2, para 2 | — (new paragraph) | "discussion of method X..." | R1-02 |  |

## Unchanged-On-Purpose

Points where the manuscript deliberately did not change; each needs a matrix
row with disposition `declined_with_reason` or `clarified_in_response`.

| MatrixRows | Reason |
|---|---|
| R2-01 | compute beyond rebuttal budget; committed to revision |
