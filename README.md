# Play the Toy with Children

An auditable research skill and one worked literature-review case: the
Stochastic Path Sampler (SPS) for lattice field theory.

This repository intentionally contains only:

1. the `play-the-toy-with-children` Codex skill;
2. public SPS research artifacts;
3. recorded runtime, validation, and cost/effect boundaries.

No unrelated project examples are included.

## Install and invoke the skill

Copy `play-the-toy-with-children/` into the Codex skills directory, start a new
Codex task, and use a prompt such as:

```text
Please use the play-the-toy-with-children skill.
Intent: cover. Budget: balanced. Screenshot policy: key-only.
Starting clue: SPS / Moxian Qian stochastic path sampler.

Confirm the target paper, expand through references, citations, authors,
collaborators, keywords, and adjacent methods, then return to the source text.
Produce a source matrix, claim-source ledger, lineage graph, gap ledger, and
report. Every number and identity needs a source. Mark unresolved points as
pending instead of completing the story.
```

The skill definition, workflow references, templates, validators, rendering
script, and observable API runner are under
[`play-the-toy-with-children/`](play-the-toy-with-children/).

## SPS worked case

The root object is:

> Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, and Kai Zhou,
> *Stochastic Path Sampler For Lattice Field Theory*, arXiv:2606.13790v1,
> submitted 2026-06-11.

Start with [`sps/README.md`](sps/README.md). The public case includes search
contracts, candidate and source tables, reading notes, evidence and numerical
ledgers, lineage views, reviewer questions, validation reports, and a workbook.
Downloaded paper PDFs and full-text caches are deliberately excluded.

## Recorded cost and effect

Two runs used the same SPS matched protocol:

| Runtime | Wall time | Candidates | Source PDFs read | Pages | Direct edges | Validation |
|---|---:|---:|---:|---:|---:|---|
| confirmed `gpt-5.6-sol`, `xhigh` | 1,345 s | 578 | 27 | 611 | 58/58 | PASS |
| Codex goal-mode runtime, exact deployment ID unavailable | 1,433 s | 578 | 27 | 611 | 58/58 | PASS |

The matched runs reproduce the same coverage result. They do **not** establish
a model speed ranking: exact token counters were unavailable, and the goal-mode
run retained an initial sandbox-blocked network attempt.

A separate clean-room goal-mode run recorded an observable active-goal snapshot
of 1,232,776 cumulative tokens and 3,360 seconds. It produced 594 deduplicated
candidates, 31 selected full texts, 731 verified pages, 155 evidence entries,
and a PASS validation result. This is a goal-level snapshot, not an API usage
object, final bill, or matched model comparison.

See [`sps/comparison/cost_effect_summary.md`](sps/comparison/cost_effect_summary.md)
for the source-linked table and measurement boundaries.

## Claim boundary

The repository demonstrates an auditable literature workflow and records its
observable outputs. It does not claim that the current data compare two fully
identified models, provide API pricing, or prove one runtime is intrinsically
faster. A controlled two-model protocol is included for the next experiment.

