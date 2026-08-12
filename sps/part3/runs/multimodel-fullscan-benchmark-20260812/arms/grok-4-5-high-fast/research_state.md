# Research State

## Project

**Research question:** Map the predecessor and adjacent-method landscape of "Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790): learned/neural samplers for unnormalized target distributions, learned samplers for lattice field theory, and the correction/exactness mechanisms they use.

**Primary intent:** cover  
**Secondary intent:** learn  
**Risk level:** high  
**Current round:** R0003  
**Current status:** stopped  
**Scan level:** full  
**graph_mode:** OFF  

## Scope

### Inclusion Criteria

- Learned / neural / flow / diffusion / path samplers targeting unnormalized densities or Boltzmann / lattice actions.
- Learned samplers for lattice field theory.
- Explicit correction / exactness mechanisms (MH, AIS/SMC, reweighting, path-measure objectives).

### Exclusion Criteria

- Pure generative ML without unnormalized-target sampling framing (monitor/exclude).
- Classical MCMC without learned component (background only).

### Time Range

~2015–2026 (plus foundations if seed-linked).

### Language Range

English.

### Source / Database Range

arXiv, INSPIRE-HEP, Semantic Scholar (partial), OpenAlex, Crossref.

### Human Budget

- Max web calls: 40 → **used 33**
- C3 PDFs: ≥6 → **7**

## Budget Mirror (non-authoritative; see round_log.md)

**Calls used:** 33/40  
**Channels covered:** arXiv, INSPIRE, Semantic Scholar (Albergo OK; seed 429), OpenAlex, Crossref  

## Funnel Mirror

- Raw hits (cumulative logged): ~510  
- Deduplicated pool rows: 36  
- Screened include: ~28  
- C3 PDFs: 7  
- Distinct verified papers with arXiv IDs: 34  

## Landscape Snapshot (scope-limited)

- **Seed (P000):** SPS learns forward/backward stochastic dynamics via path-space variational free energy; proposals corrected by extended-space Independence MH; demonstrated on 2D φ⁴ vs HMC.
- **LFT flow predecessors:** Albergo–Kanwar–Shanahan flow MCMC (1904.12072) and tutorial (2101.08176); gauge equivariant flows; trivializing/conditional/multiscale NFs.
- **Non-equilibrium / SNF:** Caselle et al. SNF for LFT (2210.03139) and non-eq SNF (2201.08862).
- **Path/diffusion ML samplers:** PIS (2111.15141), DDS (2302.13834), learned diffusions (2307.01198), NETS (2410.02711).
- **SQ/diffusion LFT (overlapping authors):** 2309.17082 and later gauge diffusion works.
- **Correction families observed:** Independence MH (seed); flow-MCMC accept/reject; SNF non-eq weights; AIS/AFT (CRAFT); diffusion path-measure / importance-style corrections (family-level; not all C4-anchored).

## Stop Status

**Current stop status:** saturated_under_budget / stopped_with_known_risk  
**Reason:** Multi-channel cover of requested facets under 40-call hard cap; ≥6 C3 PDFs; residual risks in coverage_stopping_report.md.  
**Remaining risks:** S2 seed blind; non-HEP ML venue depth; incomplete citer screening; no C4 deep reads for most PDFs.

## Validator

```
command: python3 .../scripts/validate_run_state.py <this-run-dir>
profile: literature
status: CONSISTENT
exit_code: 0
recorded: 2026-08-12
```

Manifest directory-row issue fixed before pass (PDF artifacts remain under `sources/pdfs/` as internal working data; integrity recorded in `evidence_registry.md`).
