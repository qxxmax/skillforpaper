# Research State

## Project

**Research question:** For 'Stochastic Path Sampler for Lattice Field Theory'
(arXiv:2606.13790), identify the key prior methods it directly builds on —
(a) learned/neural samplers for unnormalized target distributions and
(b) learned samplers for lattice field theory — and verify each predecessor's
identity (exact title, authors, arXiv ID) with own web calls.
**Primary intent:** locate
**Secondary intent:** learn
**Risk level:** medium
**Current round:** R0001
**Current status:** reporting

## Scope

### Inclusion Criteria

- Methods the SPS paper directly builds on / cites as its immediate predecessors.
- Facet A: learned/neural samplers for unnormalized target densities
  (e.g. Path Integral Sampler, diffusion/annealed samplers, Boltzmann generators).
- Facet B: learned samplers for lattice field theory (e.g. flow-based sampling
  for phi^4 / lattice gauge theory).

### Exclusion Criteria

- Generic MCMC / HMC background not specific to learned samplers.
- Works only tangentially related (unless SPS names them as a base method).

### Time Range

Through 2026.

### Source / Database Range

arXiv (primary), web search. CONTAMINATION GUARD: only the skill folder and
this run directory are read locally; all facts come from logged web calls.

### Human Budget

- Max rounds: 1-2 (quick scan)
- Max papers to screen: 20-40
- Max web calls: 10 (hard cap)

## Root Configuration For Graph

**Root type:** paper
**Root node(s):** arXiv:2606.13790 (Stochastic Path Sampler for Lattice Field Theory)
**Reason for root choice:** it is the focal paper whose predecessors we locate.

## Current Optimization Target

- Locate: minimize time_to_verified_source for each named predecessor.

## Findings — Confirmed Predecessors (all C2 via arXiv API, independent source)

Facet A — learned/neural samplers for unnormalized target distributions
(the "path-space variational sampler family" SPS §1 says it adapts):
- Path Integral Sampler — arXiv:2111.15141 (Zhang, Chen)
- Denoising Diffusion Samplers — arXiv:2302.13834 (Vargas, Grathwohl, Doucet)
- An optimal control perspective on diffusion-based generative modeling —
  arXiv:2211.01364 (Berner, Richter, Ullrich)
- Improved sampling via learned diffusions — arXiv:2307.01198 (Richter, Berner)
- Controlled Monte Carlo Diffusions — arXiv:2307.01050 (Vargas, Padhy, Blessing,
  Nüsken) — closest analogue: learns both forward and backward drifts
- NETS: A Non-Equilibrium Transport Sampler — arXiv:2410.02711 (Albergo,
  Vanden-Eijnden)

Facet B — learned samplers for lattice field theory:
- Flow-based generative models for MCMC in LFT — arXiv:1904.12072 (Albergo,
  Kanwar, Shanahan) — foundational 2D phi^4 flow sampler
- Diffusion Models as Stochastic Quantization in LFT — arXiv:2309.17082 (Wang,
  Aarts, Zhou) — direct parent of SPS's stochastic-quantization route
- Equivariant flow-based sampling for lattice gauge theory — arXiv:2003.06413
  (Kanwar et al.)
- Stochastic normalizing flows as non-equilibrium transformations —
  arXiv:2201.08862 (Caselle, Cellini, Nada, Panero)

## Stop Status

**Current stop status:** saturated_under_budget
**Reason:** both facets covered; all key named predecessors verified within budget.
**Remaining risks:** verification is C2 (metadata+abstract), not full-text deep
reading of each predecessor; that is appropriate for a quick locate scan.

## Budget Mirror (authoritative counter is round_log.md)

- Calls used: 2/10

## Validator Result

- Command: python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py ~/Desktop/skillforpaper/sps/part3/runs/multimodel-quickscan-benchmark-20260812/arms/opus-4-8-high
- Result: profile=literature, status=CONSISTENT, exit code 0 (run 2026-08-12).
