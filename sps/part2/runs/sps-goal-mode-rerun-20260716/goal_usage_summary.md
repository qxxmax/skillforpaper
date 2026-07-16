# Goal-Mode Usage Summary

The counters below are cumulative observations from Codex Goal mode. They are
not API `response.usage`, a model-specific tokenizer bill, or monetary cost.

| Stage | Work completed | Added tokens | Added time | Cumulative tokens | Cumulative time |
|---|---|---:|---:|---:|---:|
| S00 | goal start | 0 | 0:00 | 0 | 0:00 |
| S01 | contract and Part 1 lock | 14,413 | 0:39 | 14,413 | 0:39 |
| S02 | exact source lock | 381,019 | 65:06 | 395,432 | 65:45 |
| S03 | five equation-level readings | 315,759 | 19:45 | 711,191 | 85:30 |
| S04 | predecessor comparison and review | 51,847 | 4:26 | 763,038 | 89:56 |
| S05 | output generation and visual layout check | 152,801 | 7:01 | 915,839 | 96:57 |
| S06 | final pre-completion audit | 167,400 | 6:43 | 1,083,239 | 103:40 |
| S07 | Goal completion | 78,423 | 2:27 | 1,161,662 | 106:07 |

`goal_usage_snapshots.csv` retains timestamps and raw counters. S06 was taken
after source resolution, public-boundary validation, wording checks, and the
five-page visual inspection. S07 is the authoritative counter returned when
Goal mode marked the run complete.
