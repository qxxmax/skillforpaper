# Part 2 Learning Contract

Package status: `VERIFIED`

| Field | Value |
|---|---|
| Topic or method | Stochastic Path Sampler (SPS) for lattice field theory |
| Target capability | Explain the SPS mechanism, compare its core equations with checked predecessors, and reconstruct the algorithm through T3 |
| Source Part 1 run | `../../../runs/codex-goal-mode-full-dijkstra-20260713` |
| Focal PaperIDs | `P001 / arXiv:2606.13790v1` |
| Comparison PaperIDs | `P002, P003, P004, P007` |
| Mode | `understand` |
| Target competence | `T3` |
| Frontier cutoff | `2026-07-16` |
| Time budget | Continue until T0-T3 pass or a source-specific blocker is recorded |
| Token policy | Goal-mode usage snapshots; no preset cap |
| Compute budget | No numerical reproduction requested |
| Requested outputs | `md / csv / tex / pdf / lineage graph / usage log` |
| Stop condition | T0-T3 have supporting records; every comparison has anchors from each paper or stays pending |

## Core Questions

| Question ID | Question | Why it matters | Target level | Status |
|---|---|---|---|---|
| Q01 | What stochastic object and path does SPS define? | Fixes the mechanism before comparison | T2 | answered; P001 reading record and algorithm trace |
| Q02 | Which ingredients already appear in PIS, DDS, CMCD, and stochastic normalizing flows? | Separates inherited structure from the SPS combination | T2 | answered; five reading records and comparison ledger |
| Q03 | What is the smallest source-supported SPS difference after equation-level predecessor comparison? | Identifies the technical contribution without relying on titles or abstracts | T3 | answered; `innovation_delta.csv` |
| Q04 | Which exactness, benchmark, autocorrelation, and cost statements survive technical review? | Separates correctness from efficiency | T3 | answered; `review_core.md` |

## Part 1 Inputs

| Input | Path | Use |
|---|---|---|
| Evidence registry | `../../../runs/codex-goal-mode-full-dijkstra-20260713/evidence_registry.csv` | EvidenceIDs and source anchors |
| Relation ledger | `../../../runs/codex-goal-mode-full-dijkstra-20260713/relation_ledger.csv` | checked citation relations |
| Paper verification | `../../../runs/codex-goal-mode-full-dijkstra-20260713/paper_verification_ledger.csv` | exact paper identities and source hashes |
| Focal reading | `../../../runs/codex-goal-mode-full-dijkstra-20260713/native_paper_reading_record_sps.md` | P001 R0-R6 record |
| Graph paths | `../../../runs/codex-goal-mode-full-dijkstra-20260713/dijkstra_shortest_paths.csv` | reading order only |

## Learning Targets

| Level | Target | Evidence | Status |
|---|---|---|---|
| T0 | exact identities and versions | verification-ledger rows and source pages | `pass` |
| T1 | explain the problem, mechanism, result, and limits | teach-back section | `pass` |
| T2 | align core formulas and assumptions | equation comparison and formula table | `pass` |
| T3 | reconstruct the algorithm and predecessor difference | ordered algorithm and innovation table | `pass` |
| T4 | map equations to official code | not requested | `not_requested` |
| T5 | reproduce a result | not requested | `not_requested` |

## Scope

- Dijkstra selects the reading order; source sections support technical claims.
- P004/CMCD was added during reading because P001 states that it already
  learns forward and backward drifts. It is required for the novelty check.
- This run may use official paper pages and local full-text copies for reading.
- Downloaded papers are temporary inputs and are not placed in the public run folder.
- New SPS experiments belong to Part 3.
