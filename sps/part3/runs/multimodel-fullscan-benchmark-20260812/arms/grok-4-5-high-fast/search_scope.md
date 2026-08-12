# Search Scope

## Question

Predecessor and adjacent-method landscape of **Stochastic Path Sampler for Lattice Field Theory** (arXiv:2606.13790), focusing on:

1. Learned/neural samplers for unnormalized target distributions  
2. Learned samplers for lattice field theory  
3. Correction / exactness mechanisms those methods use  

## Inclusion

- Methods that learn a proposal, path, flow, diffusion, or transport toward an unnormalized target / Boltzmann / lattice action.
- Lattice QFT / scalar field / gauge theory sampling with ML components.
- Exactness via MH accept/reject, importance weights, AIS/SMC, continuous-time reweighting, or similar.

## Exclusion

- Generative modeling without unnormalized-target sampling framing (monitor tier only).
- Pure classical MCMC surveys without learned component (unless seed-cited foundation).

## Facets To Cover

| FacetID | Facet | Notes |
|---|---|---|
| F1 | Neural/flow MCMC / normalizing-flow samplers | unnormalized targets |
| F2 | Continuous-time / diffusion / stochastic-path samplers | path/protocol learning |
| F3 | Lattice field theory ML samplers | φ⁴, gauge, QCD toys |
| F4 | Correction/exactness | MH, AIS, SMC, ESS, reweighting |
| F5 | Direct SPS neighbors / same authors / same problem | seed lineage |

## Channels Required

| Channel | Role | Status |
|---|---|---|
| arXiv API / abs / pdf | domain archive + OA PDF | planned |
| Semantic Scholar | bibliographic graph + citations | planned |
| INSPIRE-HEP | HEP/LFT domain DB | planned |

## Out Of Scope / Blocked

- Web of Science / Scopus (no institutional access assumed) — blocked, blind spot: citation completeness outside OA graphs.
- graph_mode files (explicitly OFF).
