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

## Interpretation

The fixed contract reached the same recorded coverage and validation outputs in
both settings. This shows that the recorded contract was reproducible, but it
is not a strict two-model benchmark: Goal mode did not expose its deployment
identifier or reasoning effort, and its timing includes an initial
sandbox-blocked 36-route attempt.

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

## Executable Dijkstra comparison

The later SPS run isolates relevance-only ranking versus an executable
Dijkstra ranking inside one shared candidate pool and records a final goal count
of 1,012,083 tokens. That is a different experiment from the two-runtime table;
see
[`dijkstra_effect_and_cost.md`](dijkstra_effect_and_cost.md).

## Fresh 2026-07-16 rerun

The later fresh Goal-mode rerun rebuilt the L0-L10 search and C0-C4 package
under a new contract. Its case summary and historical comparison with the
identified `gpt-5.6-sol/xhigh` run are reported separately in
[`sol_xhigh_vs_goal_full_rerun_20260716.md`](sol_xhigh_vs_goal_full_rerun_20260716.md).
It is not appended to the matched table above because the route definitions,
reading depth, citation target, and runtime observability differ.
