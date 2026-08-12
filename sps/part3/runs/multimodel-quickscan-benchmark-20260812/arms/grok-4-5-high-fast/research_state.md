# Research State

## Project

**Research question:** The paper 'Stochastic Path Sampler for Lattice Field Theory' (arXiv:2606.13790) proposes a learned stochastic sampler for lattice phi^4 theory. Identify the key prior methods this paper directly builds on — learned/neural samplers for unnormalized target distributions and learned samplers for lattice field theory — and verify each one's identity (exact title, authors, arXiv ID) with own web calls.

**Primary intent:** locate  
**Secondary intent:** evaluate  
**Risk level:** medium  
**Current round:** R0003  
**Current status:** stopped  
**Scan level:** quick  
**Call budget:** 10 web calls  
Used: 10  
**Calls used (mirror of round_log ledger):** 10/10  

## Scope

### Inclusion Criteria

- Papers that arXiv:2606.13790 explicitly cites as learned/neural samplers for unnormalized targets (esp. path-space VFE family named in §1).
- Papers that arXiv:2606.13790 explicitly cites as learned samplers for lattice field theory.
- Identity verified via own logged fetch of arXiv abs pages.

### Exclusion Criteria

- Unverified memory citations.
- Other benchmark arms/epochs (contamination guard).
- Generic non-learned MCMC unless treated as direct methodological parent (HMC used as baseline, not predecessor method).

### Time Range

Open; seeded by P0000 bibliography.

### Language Range

English.

### Source / Database Range

arXiv abs/html only in this run (10 fetches).

### Human Budget

- Max rounds: 3
- Max papers to screen: ~15
- Max full texts to verify: seed + up to 9 parents (done)
- Max screenshots: 0

## Root Configuration For Graph

**Root type:** paper  
**Root node(s):** P0000 arXiv:2606.13790  
**Reason for root choice:** user-specified seed.

## Current Optimization Target

- Locate: minimize time_to_verified_source for each claimed predecessor.

## Confirmed Predecessor Summary (identity-verified)

### Learned / neural samplers for unnormalized targets (path-space family P0000 §1 explicitly adapts)

| PaperID | arXiv | Title | Authors | Evidence |
|---|---|---|---|---|
| P0001 | 2111.15141 | Path Integral Sampler: a stochastic control approach for sampling | Qinsheng Zhang, Yongxin Chen | E0006–E0007 |
| P0002 | 2302.13834 | Denoising Diffusion Samplers | Francisco Vargas, Will Grathwohl, Arnaud Doucet | E0008–E0009 |
| P0003 | 2307.01050 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken | E0010–E0011 |
| P0004 | 2410.02711 | NETS: A Non-Equilibrium Transport Sampler | Michael S. Albergo, Eric Vanden-Eijnden | E0012–E0013 |
| P0005 | 2307.01198 | Improved sampling via learned diffusions | Lorenz Richter, Julius Berner | E0014–E0015 |
| P0006 | 2211.01364 | An optimal control perspective on diffusion-based generative modeling | Julius Berner, Lorenz Richter, Karen Ullrich | E0020–E0021 |

### Learned samplers for lattice field theory (verified)

| PaperID | arXiv | Title | Authors | Evidence |
|---|---|---|---|---|
| P0007 | 1904.12072 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | M. S. Albergo, G. Kanwar, P. E. Shanahan | E0016–E0017 |
| P0008 | 2309.17082 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | L. Wang, G. Aarts, K. Zhou | E0018–E0019 |
| P0009 | 2207.00283 | Learning Lattice Quantum Field Theories with Equivariant Continuous Flows | Mathis Gerdes, Pim de Haan, Corrado Rainone, Roberto Bondesan, Miranda C. N. Cheng | E0022 |

### Unverified (budget exhausted; C0/C1 only)

- P0010 Kanwar et al. equivariant gauge flows (bib 2003.06413)
- P0011 Caselle et al. stochastic normalizing flows (bib 2201.08862)
- P0012 Wu et al. Stochastic normalizing flows (NeurIPS 2020; Link-only in bib)

## Current Next Best Action

**Action:** none (budget saturated)  
**Reason:** 10/10 calls used; core named parents verified.  
**Expected gain:** N/A  
**Expected cost:** N/A  
**Required user input:** none  

## Stop Status

**Current stop status:** saturated_under_budget  
**Reason:** Call ledger at 10/10; key path-space and LFT predecessors identity-verified; residual bib leads left unconfirmed rather than asserted.  
**Remaining risks:** Kanwar / Caselle SNF / Wu SNF not independently fetched; no Semantic Scholar cross-check.

## Validator

**Command:** `python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py ~/Desktop/skillforpaper/sps/part3/runs/multimodel-quickscan-benchmark-20260812/arms/grok-4-5-high-fast`  
**Status:** CONSISTENT  
**Result:** profile=literature; errors=[]; warnings=[]; manifest_rows=4; call ledger 10 matches Used: 10  
