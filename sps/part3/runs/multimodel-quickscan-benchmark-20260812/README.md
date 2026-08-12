# E1: Multi-Model Quick-Scan Benchmark (first real Part 3 run)

First worked exercise of the Part 3 contracts
(`references/41_experiment_design_and_run_ledger.md`,
`references/42_diagnosis_and_claim_promotion_gate.md`), and simultaneously
the skill's first controlled multi-model benchmark.

## Design In One Paragraph

Nine subagent arms run the same bounded task — identify the direct
predecessor methods of the SPS paper (arXiv:2606.13790) with at most 10
logged web calls. Eight arms follow the skill's quick-scan contract on
different models; one control arm gets the same question and budget but no
contract. Ground truth is the four checked predecessors from the verified
Part 2 review (PIS, DDS, CMCD, SNF). Success criteria were pre-registered in
`experiment_contract.md` **before** any arm launched. Arms are barred from
reading this repository's prior SPS runs (contamination guard); pretraining
priors cannot be excluded, so the fabrication metric checks resolvability of
citations, not novelty of discovery.

## Arms

| RunID | arm directory | model slug | skill |
|---|---|---|---|
| E1-R001 | arms/fable5/ | inherit (Fable 5) | on |
| E1-R002 | arms/fable5-thinking-max/ | claude-fable-5-thinking-max | on |
| E1-R003 | arms/opus-4-7-xhigh/ | claude-opus-4-7-xhigh | on |
| E1-R004 | arms/opus-4-8-high/ | claude-opus-4-8-high | on |
| E1-R005 | arms/opus-5-thinking-xhigh/ | claude-opus-5-thinking-xhigh | on |
| E1-R006 | arms/composer-2-5-fast/ | composer-2.5-fast | on |
| E1-R007 | arms/grok-4-5-high-fast/ | cursor-grok-4.5-high-fast | on |
| E1-R008 | arms/gpt-5-6-sol-medium/ | gpt-5.6-sol-medium | on |
| E1-R009 | arms/control-noskill/ | inherit (Fable 5) | off |

## Observability Note

Per-arm token/cost counters are not exposed to the orchestrator (see
`env_snapshot.md`); the compute budget's token column is backfilled from the
user's Cursor usage dashboard or recorded `unavailable`. Wall time, file
outputs, call ledgers, and validator results are recorded directly.

## Status

Launched 2026-08-12 ~14:20 UTC+2. Scoring report follows arm completion.
