# Environment Snapshot: env-cursor-subagents-20260812

- Env tag (referenced by `run_ledger.csv`): env-cursor-subagents-20260812
- Snapshot date: 2026-08-12

## Code

- Skill under test: `play-the-toy-with-children` at repo commit `55386d2`
  (github.com/qxxmax/skillforpaper)
- Uncommitted changes at run time: this benchmark directory only

## Software

| component | version/slug | pin source |
|---|---|---|
| harness | Cursor Task subagents (local) | Cursor app, 2026-08-12 |
| arm 1 model | inherit (Fable 5) | Cursor slug |
| arm 2 model | claude-fable-5-thinking-max | Cursor slug |
| arm 3 model | claude-opus-4-7-xhigh | Cursor slug |
| arm 4 model | claude-opus-4-8-high | Cursor slug |
| arm 5 model | claude-opus-5-thinking-xhigh | Cursor slug |
| arm 6 model | composer-2.5-fast | Cursor slug |
| arm 7 model | cursor-grok-4.5-high-fast | Cursor slug |
| arm 8 model | gpt-5.6-sol-medium | Cursor slug |
| arm 9 model | inherit (Fable 5), no skill | Cursor slug |

## Hardware

- Machine: user's macOS host (darwin 24.3.0); model inference is remote and
  not further identifiable from this harness

## Observability Limits

- Per-arm token/cost counters are not exposed to the orchestrator; they can
  only be backfilled from the user's Cursor usage dashboard. Absent that,
  M6 stays `unavailable` per the no-estimation rule of reference 37.
- Model deployment identifiers beyond the Cursor slug are not observable.

## Rebuild

- Re-run: launch the 9 subagent prompts recorded in `README.md` against the
  same skill commit.
