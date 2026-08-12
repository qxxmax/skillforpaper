# Search Scope

## Research question

Map the predecessor and adjacent-method landscape of **Stochastic Path Sampler for Lattice Field Theory** (arXiv:2606.13790): learned/neural samplers for unnormalized targets, learned samplers for lattice field theory, and correction/exactness mechanisms.

## Inclusion

- Peer-reviewed or arXiv preprints on neural/generative samplers applied to Boltzmann/lattice actions.
- ML path-space / Schrödinger-bridge / optimal-control samplers for **unnormalized** densities (PIS, CMCD, DDS, etc.).
- Explicit correction: independence Metropolis–Hastings, standard MH, importance reweighting, Jarzynski/Crooks weighting, accept–reject after diffusion trajectories.
- Reviews/proceedings that taxonomy the LFT neural-sampler field (e.g. flow-based sampling review).

## Exclusion

- Pure HMC/MALA algorithm papers without learned proposals.
- Unrelated "path sampler" strings (instrumentation, QKD, etc.) — excluded after title screen.
- Claims not backed by logged fetch/search metadata.

## Facets (must cover under full scan)

| facet | representative verified works |
|---|---|
| F1 Data-free path-space variational | P0001 SPS, P0004 PIS, P0005 CMCD, P0007 DDS |
| F2 Normalizing flows + IMH in LFT | P0002, P0003, P0008 NeuMC |
| F3 Diffusion/score LFT (often data-driven) | P0006 Wang–Aarts–Zhou JHEP |
| F4 Stochastic normalizing flows / NE-MCMC | P0010 SNF SU(3) (metadata C1) |
| F5 Correction taxonomy | IMH, IS weights, trajectory-extended MH |

## Seed recall

- arXiv:2606.13790 — **recovered** (C3 PDF).
- Cross-validated: arXiv abs + INSPIRE 3168332 + Semantic Scholar paperId.

## Date

2026-08-12 (benchmark arm composer-2-5-fast)
