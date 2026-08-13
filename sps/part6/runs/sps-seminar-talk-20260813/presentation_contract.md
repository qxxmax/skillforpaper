# Presentation Contract: SPS in the learned-sampler lineage

Written before the first slide. Amendments are logged at the bottom, never
silently edited.

## Setting

- Format: seminar
- Venue and date: group seminar (rehearsal package), 2026-08-13
- Duration: 20 + 5 questions
- Audience tier: specialist (lattice field theory + ML-for-sampling)
- Audience assumed to know: MCMC for lattice actions, critical slowing down,
  normalizing-flow samplers at the level of Albergo et al. 1904.12072

## Core Message

SPS's contribution is a specific recombination — PIS-style path-control
sampling brought to lattice field theory with an extended-space
Metropolis-Hastings correction — whose components are all inherited and
whose isolated benefits are not yet measured.

## Claim Level Cap

- Highest level this talk may assert: validated_claim
- Why: lineage claims D001-D004 are `verified` in
  `innovation_delta.csv`; effect-size claims stay at their recorded levels
  (several are explicitly unmeasured and are presented as boundaries)

## Sources Consumed

| ledger / run | path | what it provides |
|---|---|---|
| innovation delta ledger | `sps/part2/runs/sps-goal-mode-rerun-20260716/innovation_delta.csv` | verified lineage deltas D001-D004 |
| Part 1 full rerun | `sps/runs/codex-goal-mode-full-dijkstra-rerun-20260716/` | landscape graph exports, coverage stopping report |
| Part 2 learning report | `sps/part2/runs/sps-goal-mode-rerun-20260716/part2_learning_report.md` | method reconstruction, equation anchors |

## Intended Effect

After this talk the audience should be able to: place SPS relative to PIS,
DDS, and CMCD, name its correction mechanism, and state which of its claimed
advantages are measured versus asserted.

## Amendment Log

| date | what changed | why |
|---|---|---|
