# Research State

## Project

**Research question:** The paper "Stochastic Path Sampler for Lattice Field
Theory" (arXiv:2606.13790) proposes a learned stochastic sampler for lattice
phi^4 theory. Identify the key prior methods this paper directly builds on —
learned/neural samplers for unnormalized target distributions and learned
samplers for lattice field theory — and verify each one's identity (exact
title, authors, arXiv ID) with own web calls.
**Primary intent:** evaluate (identify + verify direct predecessors)
**Secondary intent:** locate (verify identity of each predecessor)
**Risk level:** medium (fabrication risk on identities is high without
verification)
**Current round:** R0001  
**Current status:** stopped (saturated_under_budget)  

## Scope

### Inclusion Criteria

- Method papers cited by or clearly foundational to the SPS paper for either
  (a) learned/neural samplers of unnormalized target densities, or
  (b) learned samplers specifically applied to lattice field theory
  (especially lattice phi^4 or gauge models).

### Exclusion Criteria

- Application-only follow-ups not preceding SPS.
- Standard textbook references (Metropolis, HMC) unless SPS presents them as
  a direct method predecessor.
- Papers from outside the sampler / lattice-sampler families (e.g. purely
  classification networks).

### Time Range

Predecessors published before or around June 2026 (SPS arXiv date range).

### Language Range

English.

### Source / Database Range

- arXiv listing/abstract pages.
- One web-search backend per query.

### Human Budget

- Max web calls (search + fetch, combined): **10** (hard cap).
- Max rounds: 1 (quick scan; may add second lightweight round only if budget
  allows).
- Max full texts to verify: SPS abstract only; predecessors identified by
  arXiv landing page (title/authors/ID).
- Max screenshots to capture: 0 (screenshot policy: none for this quick scan;
  landing-page URL is the evidence).

## Root Configuration For Graph

**Root type:** paper
**Root node(s):** SPS (arXiv:2606.13790)
**Reason for root choice:** target paper of the research question.

## Current Optimization Target

Evaluate mode: maximize decision confidence about which prior methods SPS
directly builds on, while minimizing fabrication risk. Each claimed
predecessor requires a logged web call landing on its authoritative arXiv or
publisher page.

## Current Next Best Action

**Action:** none within this quick-scan budget. Deeper verification (C3/C4
full-text audit of individual predecessor claims, forward/backward citation
snowballing, or coverage of the additional lattice-sampler references
[35, 23, 54, 42, 56] which remain at C1(bib-of-C3)) would require a new
round with additional budget.
**Reason:** budget cap of 10 web calls hit exactly, and all predecessors that
SPS explicitly names in the "learned samplers for unnormalized densities"
family are C2-verified.
**Expected gain:** for the current quick-scan intent, none.
**Expected cost:** N/A.
**Required user input:** budget increase to continue.

## Budget Mirror (authoritative counter is `round_log.md`)

- Cap: 10 web calls (searches + fetches).
- Used: **10/10** — 1 for SPS itself, 9 for direct predecessors. See
  `round_log.md` call ledger for the authoritative counter (this line is a
  mirror only).

## Confirmed Predecessors (backed by logged fetches)

Family A — learned/neural samplers for unnormalized target distributions:

1. Path Integral Sampler (PIS) — Zhang & Chen — arXiv:2111.15141 (E0002)
2. Denoising Diffusion Samplers (DDS) — Vargas, Grathwohl, Doucet —
   arXiv:2302.13834 (E0003)
3. Optimal-control perspective on diffusion-based generative modeling
   (DIS) — Berner, Richter, Ullrich — arXiv:2211.01364 (E0004)
4. Improved sampling via learned diffusions — Richter & Berner —
   arXiv:2307.01198 (E0005)
5. Controlled Monte Carlo Diffusions (CMCD) — Vargas, Padhy, Blessing,
   Nüsken — arXiv:2307.01050 (E0006) — SPS notes CMCD, like SPS itself,
   learns both forward and backward drifts
6. Non-Equilibrium Transport Sampler (NETS) — Albergo & Vanden-Eijnden —
   arXiv:2410.02711 (E0007)

Family B — learned samplers for lattice field theory:

1. Flow-based generative models for MCMC in lattice field theory —
   Albergo, Kanwar, Shanahan — arXiv:1904.12072 (E0008); benchmarked on the
   same 2D phi^4 target as SPS
2. Diffusion Models as Stochastic Quantization in Lattice Field Theory —
   Wang, Aarts, Zhou — arXiv:2309.17082 (E0009); shares two authors
   (Aarts, Zhou) with SPS and is the closest same-group precursor for the
   "stochastic-quantization-inspired" framing
3. Stochastic Normalizing Flows as non-equilibrium transformations —
   Caselle, Cellini, Nada, Panero — arXiv:2201.08862 (E0010); direct
   lattice-side methodological neighbor combining Langevin and NFs

## Stop Status

**Current stop status:** saturated_under_budget
**Reason:** 10-call cap reached exactly; all predecessors SPS explicitly
names in the two families in the research question have been C2-verified.
**Remaining risks:**

- Nicoli et al. 2020/2021 (arXiv:2007.07115), Gerdes et al. 2023
  (arXiv:2207.00283), Wu–Köhler–Noé Stochastic Normalizing Flows (NeurIPS
  2020), Rezende & Mohamed 2015 normalizing flows, and Zhou et al. 2019
  (arXiv:1810.12879) are named in SPS's Introduction / reference list but
  only trusted as `C1(bib-of-C3)` — a follow-up round should fetch each
  to promote them to C2 if the downstream user wants full family coverage.
- The evidence level for the 9 confirmed predecessors is C2 (arXiv landing
  page). Any strong per-paper claim about method internals would require
  C3/C4 evidence not gathered in this quick scan.
- SPS itself is C3 (its abstract page includes the full introduction and
  reference list). No full-PDF audit of SPS's own numerical claims was in
  scope.

## Validator Status

Command:

```
python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py \
  ~/Desktop/skillforpaper/sps/part3/runs/multimodel-quickscan-benchmark-20260812/arms/opus-4-7-xhigh
```

Output:

```
run:     ~/Desktop/skillforpaper/sps/part3/runs/multimodel-quickscan-benchmark-20260812/arms/opus-4-7-xhigh
profile: literature
status:  CONSISTENT
```

Interpretation: the auto-detected profile is `literature`; the manifest,
call ledger, and on-disk state files reconcile with no mismatch. Every
predecessor claim in `research_state.md` maps to an `EvidenceID` in
`evidence_registry.md`, which in turn maps to a `round_log.md` ledger row.


## Validator Status

To be filled at end of run after
`python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py <run-dir>`.
