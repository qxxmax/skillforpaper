# Research State

## Project

**Research question:** Map the predecessor and adjacent-method landscape of the "Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790), across three facets: (a) learned/neural samplers for unnormalized target distributions, (b) learned samplers for lattice field theory, (c) the correction / exactness mechanisms these samplers use.
**Primary intent:** cover
**Secondary intent:** learn
**Risk level:** medium
**Current round:** R0005
**Current status:** stopped_with_known_risk

## Scope

### Inclusion Criteria

- Learned or neural samplers whose target is an unnormalized density p(x) ∝ exp(−S(x)) (or Boltzmann/Gibbs), including normalizing-flow, diffusion, path-integral, Schrödinger-bridge, and stochastic-normalizing-flow variants.
- Learned samplers applied to lattice field theory / lattice gauge theory / lattice QCD scalar or fermionic sectors.
- Papers whose core contribution includes an exactness / correction mechanism: importance reweighting, Independent Metropolis–Hastings, Jarzynski / annealed importance sampling, non-equilibrium reweighting, exact-flow reweighting, extended-space MH.

### Exclusion Criteria

- Pure MCMC methods without a learned proposal (unless referenced as baseline).
- Learned samplers for image / text / generic generative modeling with no exactness/reweighting mechanism AND no lattice / physics application.
- Application-only lattice papers with no learned sampler component.

### Time Range

- 2017 to present; older foundational refs (Parisi-Wu 1981, Jarzynski 2013) admitted when cited as ancestral by the seed neighborhood.

### Language Range

- English.

### Source / Database Range

- arXiv (abs + PDFs), INSPIRE-HEP (record + fulltext search), OpenAlex (works record), Semantic Scholar (attempted, blocked), arXiv API (search).

### Human Budget

- Max rounds: 5 planned; 5 executed (R0001–R0005).
- Max web calls: 40 (hard cap); **17 used**, 23 in reserve.
- Max papers to screen: ~90 (58 seed refs + 30+ coverage-search entries).
- Max full texts to verify: ≥ 6 PDFs downloaded → **8 downloaded**.
- Max screenshots to capture: 0 (screenshot policy: none).

## Root Configuration For Graph

**Root type:** paper
**Root node(s):** arXiv:2606.13790
**Reason for root choice:** seed for this benchmark task. graph_mode OFF.

## Current Optimization Target

- Cover: `recall + coverage + verification − human_cost − missed_risk`, under the 40-call cap.

## Current Next Best Action

**Action:** (post-stop) hand off to benchmark harness.
**Reason:** stop criteria met (see coverage_stopping_report.md); further web calls decision-neutral for the landscape claim.
**Expected gain:** none (this run); a follow-on run could promote the 15 P0060–P0074 candidates to C2 at cost ~15 calls if the downstream benchmark requests it.
**Expected cost:** 0 (this run).
**Required user input:** none.

## Budget Mirror (authoritative counter lives in `round_log.md`)

- Calls used: **17 / 40**
- Channels executed: arXiv (abs + PDFs), INSPIRE-HEP (record + fulltext + refersto), OpenAlex (works record), arXiv API (search), Semantic Scholar attempted (blocked, substituted with OpenAlex).
- Distinct successful channels: **4** (arXiv, INSPIRE-HEP, OpenAlex, arXiv API) — meets the ≥3 requirement.
- Failed / blocked calls: 2 (Semantic Scholar 429; arXiv listing 403). Both substituted per reference 34's blocked-channel substitution rule.

## Stop Status

**Current stop status:** stopped_with_known_risk
**Reason:** Seed identity verified on 3 channels; ≥6 core PDFs on disk with integrity notes (actual: 8); each of 3 facets has ≥3 include papers at C1+ (many at C3); forward-citation channel returned 0 papers (recorded as scope limitation); marginal yield from the last coverage search went decision-neutral. Residual 23-call budget preserved for a targeted second-round promotion pass if the benchmark harness requests it.
**Remaining risks:** see `coverage_stopping_report.md` §Residual Risks — most important are (i) P0060–P0074 candidates remain single-channel C1 (potentially-missed pre-seed predecessors), and (ii) Semantic Scholar co-citation graph was not gathered.

## Validator Result

Command: `python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py ~/Desktop/skillforpaper/sps/part3/runs/multimodel-fullscan-benchmark-20260812/arms/opus-4-7-xhigh`

Result: **CONSISTENT** (2026-08-12).

```
run:     ~/Desktop/skillforpaper/sps/part3/runs/multimodel-fullscan-benchmark-20260812/arms/opus-4-7-xhigh
profile: literature
status:  CONSISTENT
```

Interpretation: `output_manifest.md` matches the disk; `round_log.md` call ledger and `research_state.md` budget mirror are consistent (17/40); mandatory literature-profile file set is present (output_manifest, research_state, candidate_pool, evidence_registry, round_log, plus full-set additions search_budget_contract, search_scope, search_route_log, candidate_screening_table, coverage_stopping_report, keyword_ledger.csv, query_matrix.csv, query_yield_log.csv).
