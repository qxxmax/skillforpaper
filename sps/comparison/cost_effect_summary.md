# SPS cost and effect summary

## Matched output contract

| Metric | `gpt-5.6-sol` / xhigh | Codex goal mode |
|---|---:|---:|
| elapsed wall time | 1,345 s | 1,433 s |
| root references screened | 58 | 58 |
| fresh + fixed legacy routes | 30 + 6 | 30 + 6 |
| deduplicated candidates | 578 | 578 |
| source PDFs read locally | 27 | 27 |
| verified PDF pages | 611 | 611 |
| four-dimension reading records | 27 | 27 |
| evidence records | 108 | 108 |
| direct citation edges checked | 58/58 | 58/58 |
| final validation | PASS | PASS |
| exact token/cache counters | unavailable | unavailable |

Sources:

- [`gpt-5.6-sol` run metrics](../runs/gpt-5.6-sol-xhigh-matched/run_metrics.json)
- [goal-mode run metrics](../runs/codex-goal-mode-matched/run_metrics.json)
- [`gpt-5.6-sol` invocation identity](../runs/gpt-5.6-sol-xhigh-matched/invocation_manifest.json)
- [goal-mode invocation identity](../runs/codex-goal-mode-matched/invocation_manifest.json)

## What the matched result supports

The fixed contract reached the same recorded coverage and validation outputs in
both settings. This is a reproducibility observation about the workflow.

## What it does not support

It is not yet a strict two-model benchmark. The first model identity is
confirmed as `gpt-5.6-sol` with `xhigh` reasoning. The goal-mode task did not
expose its exact deployment identifier or reasoning effort. It also retained an
initial sandbox-blocked 36-route attempt, so the wall-time difference cannot be
attributed to the model alone.

## Goal-mode token snapshot

The independent clean-room run exposed one goal-level counter snapshot:

| Observable | Value |
|---|---:|
| cumulative goal tokens | 1,232,776 |
| cumulative elapsed time | 3,360 s |
| deduplicated candidates | 594 |
| selected full texts | 31 |
| verified pages | 731 |
| evidence entries | 155 |
| checked direct-citation edges | 124 |
| validation | PASS |

Sources:

- [goal-mode usage snapshot](../runs/codex-goal-mode-cleanroom/goal_mode_usage.md)
- [clean-room run report](../runs/codex-goal-mode-cleanroom/run_report.md)
- [clean-room validation](../runs/codex-goal-mode-cleanroom/final_validation_report.md)

This counter is not an OpenAI API `response.usage` object. It has no input,
output, cached, or reasoning-token split and cannot be converted into a reliable
monetary price. The snapshot was taken while the goal was active, so it is a
lower bound on the eventual complete-goal total.

## Executable graph-gate comparison

The later SPS run isolates relevance-only ranking versus an executable
Dijkstra gate inside one shared candidate pool and records a final goal count
of 1,012,083 tokens. That comparison is intentionally separate from the
two-runtime table above: see
[`dijkstra_effect_and_cost.md`](dijkstra_effect_and_cost.md).
