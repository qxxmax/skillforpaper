# Round Log

Each round records diagnosis, action, result, file updates, and next step.

## Call Ledger

Only authoritative budget counter. One search = one call, one fetch = one call;
retries, failed, and blocked calls count too. Local file reads are free.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | Full text + reference list of SPS; identifies Facet-A family [55,48,10,43,49,6] and Facet-B LFT samplers [3,51,28,12] | 1/10 |
| 2 | R0001 | fetch | http://export.arxiv.org/api/query?id_list=2111.15141,2302.13834,2307.01050,2410.02711,1904.12072,2309.17082,2003.06413,2201.08862,2211.01364,2307.01198 | 10/10 arXiv records returned; exact titles, authors, arXiv IDs verified for all predecessors | 2/10 |

**Calls used: 2/10.**

## R0001

**Date:** 2026-08-12
**Intent mode:** locate (secondary: learn)
**Round goal:** read arXiv:2606.13790 to identify the prior methods it directly
builds on (two facets), then independently verify each predecessor's identity.

### Diagnosis

- Seed recall: focal paper located and fully read (call 1).
- Topic coverage: both requested facets (ML samplers for unnormalized targets;
  learned LFT samplers) covered by the paper's own §1 lineage statements.
- Citation closure: predecessor arXiv IDs read from the SPS bibliography, then
  cross-validated on arXiv API (call 2), an independent source.
- Confirmed/unconfirmed ratio: 10/10 confirmed; 0 left unverified.
- Biggest missing risk: none blocking; predecessors verified within budget.

### Chosen Action

**Action:** (1) fetch SPS landing page; (2) batch-verify all named predecessor
IDs in a single arXiv API query.
**Why:** predecessors must come from the paper itself, not model memory; a single
id_list API call verifies many records at once, minimizing budget use.
**Expected gain:** authoritative identity for every key predecessor.
**Expected cost:** 2 web calls. **Actual:** 2 web calls.

### Execution Result

- New candidates: 10 (6 Facet A, 4 Facet B).
- New confirmed papers: 10 (all C2 via arXiv API).
- New unconfirmed papers: 0.
- New excluded papers: 0.
- New EvidenceIDs: E0001 (C4, focal paper full text) + E0002–E0011 (C2, arXiv API).
- New risks found: none.

Facet A (learned/neural samplers for unnormalized targets), the "path-space
variational sampler family" SPS adapts:
- Path Integral Sampler — 2111.15141 (Zhang, Chen) [SPS ref 55]
- Denoising Diffusion Samplers — 2302.13834 (Vargas, Grathwohl, Doucet) [ref 48]
- An optimal control perspective on diffusion-based generative modeling —
  2211.01364 (Berner, Richter, Ullrich) [ref 10]
- Improved sampling via learned diffusions — 2307.01198 (Richter, Berner) [ref 43]
- Controlled Monte Carlo Diffusions — 2307.01050 (Vargas, Padhy, Blessing,
  Nüsken) [ref 49] — closest analogue (learns both forward and backward drifts)
- NETS: A Non-Equilibrium Transport Sampler — 2410.02711 (Albergo,
  Vanden-Eijnden) [ref 6]

Facet B (learned samplers for lattice field theory):
- Flow-based generative models for MCMC in LFT — 1904.12072 (Albergo, Kanwar,
  Shanahan) [ref 3] — foundational flow-based 2D phi^4 sampler
- Diffusion Models as Stochastic Quantization in LFT — 2309.17082 (Wang, Aarts,
  Zhou) [ref 51] — direct parent of SPS's stochastic-quantization framing
- Equivariant flow-based sampling for lattice gauge theory — 2003.06413
  (Kanwar et al.) [ref 28]
- Stochastic normalizing flows as non-equilibrium transformations — 2201.08862
  (Caselle, Cellini, Nada, Panero) [ref 12]

### File Patches

- output_manifest.md: rows for all five run files → on_disk/verified.
- research_state.md: status → reporting; budget mirror 2/10; validator result.
- candidate_pool.md: 10 confirmed predecessors added (Facet A + Facet B).
- evidence_registry.md: E0001–E0011 added.
- round_log.md: call ledger (2 rows) + this round entry.

### Next Best Action

**Recommended next action:** none required for the quick scan; identity of all
key predecessors is confirmed within budget. Optional future rounds could deep-
read CMCD (2307.01050) and DM-as-SQ (2309.17082) as the two closest parents.
**User input needed:** none

### Stop Decision

**Stop status:** saturated_under_budget
**Reason:** both requested facets covered; all named key predecessors verified
at C2 against an independent source using 2 of 10 permitted web calls.
