# Claim Promotion Ledger

Levels per `references/42_diagnosis_and_claim_promotion_gate.md`. All rows
are single-shot (no repetition budget), so nothing here can pass the
repetition gate item: the ceiling for this experiment is `candidate_claim`
with a single-run caveat in the wording.

## Claims

| ClaimID | Statement (with scope and caveats in the wording) | Level | RunRefs | ExperimentID | GateNotes |
|---|---|---|---|---|---|
| C-01 | "On this task, single-shot, the quick-scan contract was model-portable: 8/8 model arms produced validator-CONSISTENT run states, complete call ledgers, and zero unresolvable citations" | candidate_claim | E1-R001,E1-R002,E1-R003,E1-R004,E1-R005,E1-R006,E1-R007,E1-R008 | E1 | pre-registration pass; repetition NOT met (single shot); baseline present; failure audit clean; boundary: one task with a bibliography shortcut |
| C-02 | "The no-skill control matched best-arm recall (4/4) at lowest cost (3 calls) but produced no reconstructable verification trail; on this task the skill's measured value was auditability, not recall" | candidate_claim | E1-R009,E1-R004,E1-R002 | E1 | reported prominently per outcome map; single control run; task under-tests discipline (see scoring finding 2) |
| C-03 | "All ground-truth misses concentrated on the same least-prominent paper (SNF lattice, 2201.08862), and all occurred in arms that searched laterally instead of reading the root bibliography first" | observation | E1-R006,E1-R007,E1-R008 | E1 | pattern over 3 arms, one task; motivates the root-bibliography-first default |
| C-04 | "Budget exhaustion produced honest degradation (C1 labels, next-round queries) rather than unverified assertions in all three arms that hit 10/10" | observation | E1-R001,E1-R006,E1-R007 | E1 | direct artifact evidence; single task |

## Retractions

| ClaimID | Former level | Retracted because | Killing rows | Manuscript sentences re-checked? |
|---|---|---|---|---|
