# Goal-Mode Usage Snapshot

- Objective: `不能这样 必须完整的从头的开始`
- Status at snapshot: `active`
- Snapshot date: 2026-07-12
- Cumulative goal tokens: **1,232,776**
- Cumulative goal elapsed time: **3,360 seconds** (56 minutes 00 seconds)
- Runtime source: Codex goal-mode counter returned by `get_goal`.

## What this records

This is an observable total for the active clean-room goal. It is sufficient for
reporting the overall interaction budget of this run.

## What this does not record

- It is not an OpenAI API `response.usage` object.
- It does not split input, output, cached or reasoning tokens.
- It does not provide tokens per search/read/write stage.
- It does not imply an API price or monetary cost.

For controlled comparisons, model, reasoning effort, stage contract, search
policy and stopping condition must be held fixed. Exact per-stage token/cost
experiments require the API-observable runner and an API key.
