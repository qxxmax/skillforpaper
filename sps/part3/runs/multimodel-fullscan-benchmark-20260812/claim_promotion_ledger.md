# Claim Promotion Ledger

Scored against the pre-registered contract; levels follow the promotion gate
of `references/42_diagnosis_and_claim_promotion_gate.md`. Single shot per
model, so nothing here exceeds candidate_claim.

## Claims

| ClaimID | Statement (with scope and caveats in the wording) | Level | RunRefs | ExperimentID | GateNotes |
|---|---|---|---|---|---|
| C-E2-1 | On this one task and one shot per model, the full-scan contract (13 mandatory files, call ledger, C3 source gate, honest stopping report) executed end-to-end on all 8 tested models within a 40-call cap, with validator CONSISTENT everywhere | candidate_claim | E2-R001; E2-R002; E2-R003; E2-R004; E2-R005; E2-R006; E2-R007; E2-R008 | E2 | 8/8 vs pre-registered 6/8; single shot blocks validated level |
| C-E2-2 | Under a 40-call cap, mean recall of the frozen 20-paper verified core set was 14.0/20 (70%), range 8-19; the two extended-thinking arms led (19, 18) | candidate_claim | E2-R001; E2-R002; E2-R003; E2-R004; E2-R005; E2-R006; E2-R007; E2-R008 | E2 | pre-registered bar 12/20 met; single task, single shot |
| C-E2-3 | One core paper (2404.09723) was recalled by zero arms and three more by ≤2 arms, indicating a discovery tail below the 40-call budget that the original ~36-route unbounded run did reach | candidate_claim | E2-R001; E2-R002; E2-R003; E2-R004; E2-R005; E2-R006; E2-R007; E2-R008 | E2 | negative-space finding; motivates budget-tiering guidance in the skill |
| C-E2-4 | No fabricated citations were detected within the locally adjudicable scope (321-ID verified corpus, 0-call scoring); unadjudicated IDs rely on arms' recorded dual-source verification | candidate_claim | E2-R001; E2-R002; E2-R003; E2-R004; E2-R005; E2-R006; E2-R007; E2-R008 | E2 | scope-limited by design; method in scoring_report.md M2 note |
| C-E2-5 | Transcript volume and wall time scale with invested search effort, not model tier alone (46 KB/5 min Composer to 220 KB/30 min Opus 5 Thinking); token counts unobservable at harness level | observation | E2-R001; E2-R002; E2-R003; E2-R004; E2-R005; E2-R006; E2-R007; E2-R008 | E2 | proxy metric only (scoring_report.md); dashboard tokens pending |

## Retractions

| ClaimID | Former level | Retracted because | Killing rows | Manuscript sentences re-checked? |
|---|---|---|---|---|
