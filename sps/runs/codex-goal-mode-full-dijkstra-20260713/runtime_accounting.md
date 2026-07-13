# Runtime and Token Accounting

- Run start: `2026-07-13T06:22:41+02:00`
- Validated snapshot: `2026-07-13T07:23:37+02:00`
- End-to-end wall clock through validation: `3,656 s` (`60 min 56 s`)
- Goal-mode token snapshot before finalization: `997,788`
- Goal-mode final elapsed time: `4,039 s` (`67 min 19 s`)
- Goal-mode final token count: `1,012,083`
- API token breakdown: unavailable; this run did not use an OpenAI API key or usage object.
- Monetary API cost: not computed because no billable API usage record exists.
- Per-stage timing: only stages explicitly instrumented in `logs/timing_log.csv` are reported; missing subdivisions are not estimated.

The final goal values include the post-validation packaging and completion work.
They describe the shared end-to-end run, not independent costs for each ranking
arm in the within-run comparison.
