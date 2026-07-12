# Observable API Runner

Use `scripts/observable_research_runner.py` when exact token accounting is a
required experiment output. The ordinary Codex skill path cannot manufacture
usage counters that its runtime does not expose.

## Invocation

```bash
export OPENAI_API_KEY="..."
python3 scripts/observable_research_runner.py \
  --topic "Find the SPS family tree" \
  --output outputs/sps_observable_run \
  --model gpt-5.6-sol \
  --reasoning-effort xhigh
```

The output directory must not already exist. Each research stage is preserved
as Markdown and raw response JSON. Exact values from `response.usage` are
written to:

- `token_usage_by_round.csv`
- `token_usage.json`
- `run_usage_report.md`

The runner also writes `final_report.md` and a `rounds/` directory. API cost is
left uncalculated unless the caller supplies `--pricing pricing.json`; this
avoids silently using stale prices.

## Boundary

This is an API-observable companion to the Codex-native skill, not a claim that
the API can report usage for an earlier Codex task. Compare runs only when the
model, reasoning effort, stage protocol, search policy, and stopping conditions
match.
