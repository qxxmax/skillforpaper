# Dijkstra Navigation Evaluation

The two rankings use the same screened candidate pool. Dijkstra uses only declared
search-route, citation, author, and method edges. The screen-only comparator uses
the C0-C2 screen order. The target set is the current run's predeclared 21-PDF reading
plan, so this is a workflow replay diagnostic rather than a general performance claim.

| budget | Dijkstra C4 | screen C4 | Dijkstra C3 | screen C3 | Dijkstra cited | screen cited |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5 | 3 | 5 | 4 | 4 | 0 |
| 10 | 9 | 7 | 10 | 8 | 9 | 3 |
| 20 | 14 | 8 | 16 | 13 | 10 | 4 |
| 40 | 14 | 9 | 19 | 15 | 10 | 5 |
| 60 | 14 | 11 | 19 | 17 | 10 | 6 |

## Interpretation boundary

A shorter Dijkstra path shows that the declared graph reaches a record cheaply. It does
not verify a method claim, establish causal influence, or measure scientific quality.
