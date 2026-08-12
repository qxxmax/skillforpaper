# Compute Budget

- Budget policy: balanced
- Unit: web calls per arm; wall time and transcript volume observed

## Line Items

| ExperimentID | purpose | planned runs | planned compute | actual runs | actual compute | note |
|---|---|---|---|---|---|---|
| E2 arms | 8 models × bounded full scan | 8 | ≤40 web calls each | | | tokens: dashboard backfill or unavailable |
| E2 scoring | orchestrator scoring pass | 1 | 0 web calls (frozen local ground truth) | | | |
| exploration | — | 0 | 0 | | | none planned |

## Stop Accounting

- Backfilled on (date):
- Ledger rows counted:
- Over/under budget and why:
