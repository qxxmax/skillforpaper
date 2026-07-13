# Dijkstra gate: effect and cost

This comparison asks a narrow question: **what changed when the same SPS
candidate pool was ranked with an executable literature-graph Dijkstra gate?**

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
citation relations. The complete run passed 19/19 validation gates.

## Cost

- Complete goal-mode task: **1,012,083 tokens** and **4,039 s**.
- Snapshot through final validation: **3,656 s**.
- Deterministic 3,300-node / 8,187-edge Dijkstra pass: **0.11 s** in one local
  run, including CSV input and output.
- API dollar cost: unavailable because this task exposed no billable API usage
  object.

The two ranking arms share discovery, candidate screening, and the downstream
run. Therefore the task does **not** provide independent token or wall-time
costs for relevance-only versus Dijkstra. It measures a controlled selection
effect inside one run. A strict no-skill versus skill benchmark would require
two separately executed, matched tasks and is not claimed here.

Full packet: [`codex-goal-mode-full-dijkstra-20260713`](../runs/codex-goal-mode-full-dijkstra-20260713/README.md).
