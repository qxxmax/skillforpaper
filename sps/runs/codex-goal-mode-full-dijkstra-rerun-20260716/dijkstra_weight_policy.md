# Dijkstra Weight Policy

- root-to-query: 0.05 for identity, then 0.20 to 0.80 as expansion rounds move farther from the root.
- query-to-paper: 0.25 + log(1 + arXiv rank) / 2.5.
- checked direct citation: 0.15.
- declared non-citation method neighbor: 0.80.
- paper-author and author-paper: 0.45 and 0.60.
- paper-method and method-paper: 0.65 and 0.85.

All weights are positive. Distances rank navigation cost only; neither a short
path nor a query hit is scientific evidence.
