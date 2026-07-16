# Runtime Accounting

| Snapshot | Goal tokens used | Goal time | Scope |
|---|---:|---:|---|
| S00 | 358,798 | 211 s | Fresh run contract and output directory created. |
| S01 | 1,095,277 | 2,954 s | Pre-final-validation state after fresh retrieval, reading, lineage, and visual audit. |
| S02 | 1,165,477 | 3,168 s | Final validator passed all 21 checks after the raw-source path repair. |
| Delta S00 to S02 | 806,679 | 2,957 s (49 min 17 s) | This fresh rerun's observed Goal-counter increment. |

## Measurement boundary

These are desktop Goal-mode cumulative counters exposed to the task. They are
not OpenAI API `response.usage` data: input, output, cache, and reasoning-token
components are unavailable, and no monetary price is inferred. They are useful
only for a same-surface workflow comparison when the start/stop snapshots and
the fixed output contract are recorded together.

The exact underlying deployment identifier and reasoning setting were not
exposed by the Goal-mode runtime, so this record must not be used as a strict
per-model benchmark.
