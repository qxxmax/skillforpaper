# Deterministic algorithm benchmark

Command executed from the repository root on 2026-07-13:

```bash
/usr/bin/time -p python3 play-the-toy-with-children/scripts/run_literature_dijkstra.py \
  --nodes sps/runs/codex-goal-mode-full-dijkstra-20260713/dijkstra_candidate_graph_nodes.csv \
  --edges sps/runs/codex-goal-mode-full-dijkstra-20260713/dijkstra_candidate_graph_edges.csv \
  --root paper:arxiv:2606.13790 \
  --output-dir /private/tmp/sps-dijkstra-benchmark-20260713
```

Observed output:

```text
nodes=3300 edges=8187 reachable=3300
real 0.11
user 0.06
sys 0.02
```

This is one local observation, not a hardware-independent benchmark. It covers
CSV input, Dijkstra traversal, path reconstruction, validation of recomputed
costs, and CSV/report output. It excludes candidate discovery, network access,
paper download, reading, source verification, gap closure, and synthesis.
