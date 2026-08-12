# Compute Budget

- Budget policy: balanced
- Unit: web calls per arm (primary); wall-clock minutes and tokens (observed
  where available)

## Line Items

| ExperimentID | purpose | planned runs | planned compute | actual runs | actual compute | note |
|---|---|---|---|---|---|---|
| E1 skill arms | 8 models × quick scan | 8 | ≤10 web calls each | 8 | 59 calls (10,2,10,2,5,10,10,10) | tokens: unavailable pending dashboard |
| E1 control | no-skill baseline | 1 | ≤10 web calls | 1 | 3 calls | same question, no contract |
| E1 scoring | orchestrator scoring pass | 1 | 0 web calls (local ground truth) | 1 | 0 web calls; local bib check resolved one citation dispute | |
| exploration | — | 0 | 0 | | | none planned |

## Stop Accounting

- Backfilled on (date): 2026-08-12
- Ledger rows counted: 9 (all completed)
- Over/under budget and why: under; 62/90 arm calls used, orchestrator 0/0
