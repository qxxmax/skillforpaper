# Environment Snapshot: env-cursor-subagents-20260812-e2

- Env tag (referenced by `run_ledger.csv`): env-cursor-subagents-20260812-e2
- Snapshot date: 2026-08-12 (evening)

Same harness and model slugs as E1
(`../multimodel-quickscan-benchmark-20260812/env_snapshot.md`): Cursor Task
subagents, 8 arms — inherit (Fable 5), claude-fable-5-thinking-max,
claude-opus-4-7-xhigh, claude-opus-4-8-high, claude-opus-5-thinking-xhigh,
composer-2.5-fast, cursor-grok-4.5-high-fast, gpt-5.6-sol-medium.
Skill under test at repo commit `9474754`.

Observability limits unchanged: per-arm token counters not exposed;
transcript-volume proxy and wall time recorded; dashboard numbers backfill
on request.
