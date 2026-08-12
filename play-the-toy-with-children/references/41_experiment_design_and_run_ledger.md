# Experiment Design And Run Ledger

Use this reference when the user asks to design, run, extend, or audit
experiments (Part 3): new numerical studies, ablations, baselines,
reproduction beyond Part 2's bounded scope, or reviewer-requested runs.

Part 3 runs are runs: the Minimal Run Contract and the three run-state laws
apply. The compute analog of the call ledger is the run ledger — every
executed run gets a row, and the ledger is the only authoritative record of
what was run.

## Experiment Contract Before Execution

Write `experiment_contract.md` before the first run of an experiment, from
`templates/experiment_contract_template.md`. The contract pre-registers:

- the question and the hypothesis, phrased so a result can fail it;
- independent variables (what is swept), controlled variables (what is
  fixed, including seeds policy), and measured metrics;
- the success criterion, decided **before** results exist (a number, an
  interval, or an explicit "exploratory: no criterion");
- baselines: what the result is compared against and where the baseline
  numbers come from (own run at C-level evidence, or literature number with
  `EvidenceID`);
- the compute budget (see below) and the stop condition;
- what each possible outcome would mean — including the negative one.

Changing the contract after results exist is allowed but must be logged as
an amendment with a reason, never silently edited. A criterion moved to match
an observed result is the failure mode this contract exists to prevent.

## Compute Budget

`compute_budget.md` is the Part 3 counterpart of
`search_budget_contract.md`: planned runs, planned wall-clock/GPU-hours per
experiment, and an `actual` column backfilled from the run ledger at stop.
Exploratory tinkering is legal but budgeted: give it a named line item
("exploration") rather than leaving it off the books.

## Run Ledger

Every executed run — including failed, crashed, and discarded runs — gets one
row in `run_ledger.csv` (from `templates/run_ledger_template.csv`) with:

| column | content |
|---|---|
| RunID | stable ID, e.g. `E1-R003` (experiment 1, run 3) |
| ExperimentID | contract this run belongs to |
| Command | exact command line or script path |
| ConfigRef | config file path or inline key params; enough to re-run |
| Seed | random seed(s), or `none` |
| Env | environment tag (commit hash, container, or `env_snapshot.md` ref) |
| Status | `completed` / `failed` / `crashed` / `killed` / `discarded` |
| KeyMetric | headline number(s), or `—` for failures |
| ArtifactPath | where logs/outputs live |
| Note | one line: why run, what happened |

Ledger laws:

1. The row is written when the run **starts** (status `running` is permitted
   as a transient), and finalized when it ends. A run with no row did not
   happen; a result with no row cannot be used.
2. Failures are evidence, not embarrassment. A `failed` row keeps its
   ArtifactPath (the traceback or diverging loss curve is the artifact) and
   gets a one-line diagnosis in the Note. Deleting failed rows is a defect:
   the failure pattern is what the diagnosis phase (reference 42) reads.
3. Re-runs after a fix get a new RunID; never overwrite a row.
4. `discarded` requires a reason (wrong config, bug found later) — this is
   how a result is retracted without deleting history.

## Environment Snapshot

Before the first real run of an experiment, record `env_snapshot.md` (from
`templates/env_snapshot_template.md`): code
commit hash, key package versions, hardware, and how to rebuild. One snapshot
per environment, referenced by ledger rows; a new snapshot when the
environment changes. Results from unsnapshotted environments are capped at
"preliminary" in any downstream claim.

## Numbers Flow One Way

A number travels: run artifact → run ledger row → claim promotion ledger
(reference 42) → manuscript. Skipping a stage (quoting a number from memory
of a terminal, or putting an un-promoted number in prose) is the Part 3
equivalent of citing an unverified paper.
