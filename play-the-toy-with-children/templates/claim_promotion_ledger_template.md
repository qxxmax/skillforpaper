# Claim Promotion Ledger

One row per result-backed statement. Levels: `observation` →
`candidate_claim` → `validated_claim`, plus `retracted`. Only
`validated_claim` rows may back substantive manuscript sentences. Promotion
requires the gate in
`references/42_diagnosis_and_claim_promotion_gate.md`; record which gate
items passed and which carry caveats.

## Claims

| ClaimID | Statement (with scope and caveats in the wording) | Level | RunRefs | ExperimentID | GateNotes |
|---|---|---|---|---|---|
| C-01 | "example: lr 0.003 improves acc from 0.91 to 0.93 on setup X, single seed" | candidate_claim | E1-R001, E1-R003 | E1 | repetition pending (seed policy: 3 seeds) |
| C-02 | "example: training diverges for lr >= 0.01 in setup X" | observation | E1-R002 | E1 | failure kept as evidence |

## Retractions

| ClaimID | Former level | Retracted because | Killing rows | Manuscript sentences re-checked? |
|---|---|---|---|---|
|  |  |  |  |  |
