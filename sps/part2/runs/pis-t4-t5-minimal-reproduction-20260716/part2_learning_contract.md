# Part 2 Learning Contract

Package status: `VERIFIED`

| Field | Value |
|---|---|
| Topic or method | PIS objective implementation inside the SPS method lineage |
| Target capability | Trace checked PIS formulas to official code and reproduce one objective calculation through T5 |
| Source Part 1 run | `../../../runs/codex-goal-mode-full-dijkstra-20260713` |
| Focal PaperIDs | `P002 / arXiv:2111.15141v2`; successor context `P001 / arXiv:2606.13790v1` |
| Mode | `reproduce` |
| Target competence | `T5` |
| Frontier cutoff | `2026-07-16` |
| Requested outputs | `md / csv / json / code` |
| Stop condition | T0-T5 pass for the declared formula-level reproduction; code and output identities are locked; broader benchmark reproduction remains outside scope |

## Declared Scope

- T0-T3 reuse the checked PIS and SPS reading records and lineage evidence.
- T4 maps PIS Eqs. (2), (13), (14), and (17) to the official repository at a locked commit.
- T5 executes the official `quad_reg` and `loss_pis` functions on fixed tensors and compares the result with a hand calculation.
- T5 does not claim to reproduce paper tables, train a network, or compare sampler performance.
- SPS v1 states that its code and data will be released in a future manuscript version; this run records that branch as unavailable rather than inventing a mapping. E-260613790-L, PDF p. 21.

## Completion Gates

| Level | Required demonstration | Status |
|---|---|---|
| T0 | lock PIS paper, SPS successor context, official repository, and commit | pass |
| T1 | explain the objective and correction boundary | pass |
| T2 | align PIS Eqs. (2), (13), (14), and (17) with assumptions | pass |
| T3 | reconstruct training and weighted-generation steps | pass |
| T4 | map formula roles to code files, symbols, and configuration | pass |
| T5 | execute a fixed formula-level check and retain machine output | pass |
