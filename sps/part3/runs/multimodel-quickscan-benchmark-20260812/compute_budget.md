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

## Observed Volume Proxy (not tokens)

Exact token counters are not exposed to the orchestrator (see
`env_snapshot.md`). The table below records the only locally measurable
volume: each arm's message-transcript size (user-visible messages only;
reasoning tokens and tool payloads are NOT included, so thinking-model arms
are underrepresented). This is a labeled proxy, not an estimate of tokens.

| RunID | arm | transcript bytes | message events |
|---|---|---:|---:|
| E1-R001 | fable5 | 41,681 | 31 |
| E1-R002 | fable5-thinking-max | 43,078 | 36 |
| E1-R003 | opus-4-7-xhigh | 60,871 | 54 |
| E1-R004 | opus-4-8-high | 42,979 | 20 |
| E1-R005 | opus-5-thinking-xhigh | 80,593 | 29 |
| E1-R006 | composer-2-5-fast | 32,380 | 21 |
| E1-R007 | grok-4-5-high-fast | 52,507 | 25 |
| E1-R008 | gpt-5-6-sol-medium | 38,764 | 32 |
| E1-R009 | control-noskill | 15,541 | 9 |

Authoritative token/cost numbers live in the Cursor usage dashboard
(per-request rows for 2026-08-12, ~14:16-14:27 UTC+2); paste them here to
replace `unavailable` when read.

## Stop Accounting

- Backfilled on (date): 2026-08-12
- Ledger rows counted: 9 (all completed)
- Over/under budget and why: under; 62/90 arm calls used, orchestrator 0/0
