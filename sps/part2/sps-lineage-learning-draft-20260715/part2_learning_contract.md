# Part 2 Learning Contract

Package status: `DRAFT`

| Field | Value |
|---|---|
| Topic or method | Stochastic Path Sampler (SPS) for lattice field theory |
| Target capability | Explain the SPS mechanism, compare it with checked predecessors, and reconstruct the algorithm through T3 |
| Source Part 1 run | `../../runs/codex-goal-mode-full-dijkstra-20260713` |
| Focal PaperIDs | `P001 / arXiv:2606.13790v1` |
| Mode | `understand` |
| Target competence | `T3` |
| Frontier cutoff | `2026-07-15` |
| Time budget | No new web search or full-text download in this draft |
| Token policy | `balanced`; no API usage object is available |
| Compute budget | No reproduction requested |
| Requested outputs | `md / csv / tex / pdf / lineage graph` |
| Stop condition | T0-T3 have supporting records; each innovation statement has anchors from every compared paper or stays pending |

## Core Questions

| Question ID | Question | Why it matters | Target level | Status |
|---|---|---|---|---|
| Q01 | What scientific object and stochastic path does SPS define? | Locks the mechanism before comparison | T2 | checked for P001 |
| Q02 | Which ingredients are already present in path-integral sampling, denoising diffusion sampling, and stochastic normalizing flows? | Prevents an inherited component from being called new | T2 | broad C4 anchors exist; equation-level alignment pending |
| Q03 | Which equation or algorithm step is the smallest supported SPS difference after predecessor comparison? | Locates the core innovation efficiently | T3 | pending predecessor R0-R6 upgrade |
| Q04 | Which correction, benchmark, and cost statements survive reviewer-style scrutiny? | Separates exactness from practical efficiency | T3 | checked for P001; cross-paper comparison pending |

## Part 1 Inputs

| Artifact | Path | Required content | Status |
|---|---|---|---|
| Evidence registry | `../../runs/codex-goal-mode-full-dijkstra-20260713/evidence_registry.csv` | EvidenceIDs and source anchors | checked and reused |
| Relation ledger | `../../runs/codex-goal-mode-full-dijkstra-20260713/relation_ledger.csv` | checked direct-citation edges | checked and reused |
| Reading records | `../../runs/codex-goal-mode-full-dijkstra-20260713/native_paper_reading_record_sps.md` | focal R0-R6 record | P001 verified; predecessor upgrades pending |
| Graph nodes/views | `../../runs/codex-goal-mode-full-dijkstra-20260713/dijkstra_shortest_paths.csv` | navigation paths and evidence refs | checked; navigation only |
| Existing review | `../../runs/codex-goal-mode-full-dijkstra-20260713/native_paper_review_gate_sps.md` | claim and validity audit | ready and reused |

## Learning Targets

| Level | Target | Evidence | Status |
|---|---|---|---|
| T0 | required | P001 identity row and source hash | pass |
| T1 | required | explanation with result and scope limits | pass |
| T2 | required | four source-anchored focal equations | pass for P001 |
| T3 | required | ordered algorithm plus predecessor-subtraction trace | pending |
| T4 | not_requested | `equation_code_map.csv` records public-code availability | not_requested |
| T5 | not_requested | minimal reproduction command and result | not_requested |

## Boundary

- Part 2 reconstructs the published method, compares checked sources, audits
  claims, and proposes the smallest test of understanding.
- Dijkstra sets reading order; it does not establish novelty. An incomplete
  predecessor read cannot establish absence.
- Missing evidence returns to Part 1 as: exact PaperID, missing section or
  equation, required relation type, and the claim it would support.
- New research ideas hand off to Part 3 as: hypothesis, baseline, observable,
  compute budget, acceptance test, and source-backed motivation.
