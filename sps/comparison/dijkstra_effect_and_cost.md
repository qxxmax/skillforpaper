# Dijkstra ranking: effect and cost

This comparison asks a narrow question: **what changed when the same SPS
candidate pool was ranked with executable literature-graph Dijkstra?**

| Metric | Without Dijkstra | With Dijkstra | Result |
|---|---:|---:|---|
| candidate pool | 593 | 593 | controlled input |
| first reading budget | 30 | 30 | controlled budget |
| selected-set overlap | 30 | 20 | 10 papers entered and 10 left |
| exact SPS bibliography papers retained | 19 | 21 | +2 with Dijkstra |
| coarse facets | 7 | 7 | no gain |
| method groups | 8 | 8 | no gain |
| mean heuristic screen score | 16.700 | 16.067 | -0.633 with Dijkstra |

After source verification and gap closure, the final package contains 37 read
papers, 10 declared facets, 185 evidence entries, and 199 checked direct
citation relations. The complete run passed 19/19 validation checks.

## Cost

- Complete goal-mode task: **1,012,083 tokens** and **4,039 s**.
- Snapshot through final validation: **3,656 s**.
- Deterministic 3,300-node / 8,187-edge Dijkstra pass: **0.11 s** in one local
  run, including CSV input and output.
- API dollar cost: unavailable because this task exposed no billable API usage
  object.

Both ranking arms share discovery, screening, and downstream processing, so
per-arm token and wall-time costs are unavailable. This experiment measures
the change in paper selection, not a full no-skill versus skill benchmark.

Full packet: [`codex-goal-mode-full-dijkstra-20260713`](../runs/codex-goal-mode-full-dijkstra-20260713/README.md).
