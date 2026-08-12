# Research State

## Project

**Research question:** Map the predecessor and adjacent-method landscape of
"Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790):
(a) learned/neural samplers for unnormalized target distributions, (b) learned
samplers for lattice field theory, and (c) the correction/exactness mechanisms
they use.
**Primary intent:** cover
**Secondary intent:** learn
**Risk level:** high (missed prior art / fabricated citation risk in a benchmark)
**Current round:** R0004
**Current status:** stopped

## Scope

### Inclusion Criteria

- Learned/neural samplers (normalizing flows, diffusion/stochastic-control
  samplers, Boltzmann generators, neural importance sampling) targeting an
  unnormalized density.
- Learned samplers specifically applied to lattice field / gauge theory.
- Methods whose core contribution is a correction/exactness mechanism
  (independence Metropolis, importance reweighting, Jarzynski/nonequilibrium,
  stochastic normalizing flows, flow-AIS).

### Exclusion Criteria

- Pure classical MCMC with no learned component (context only).
- Generative modelling with no unnormalized-target sampling claim.

### Time Range
2018–2026 (no hard lower bound for foundational NEIS/MCMC context).

### Language Range
English.

### Source / Database Range
arXiv (search + abs + pdf), Semantic Scholar Graph API, INSPIRE-HEP,
publisher/DOI pages (via web search).

### Human Budget
- Max rounds: 4 · Max papers to screen: ~34 · Max full texts: 8 (7 PDFs +
  seed) · Max screenshots: 0 (policy: none).

## Root Configuration For Graph

**Root type:** paper
**Root node(s):** arXiv:2606.13790 (SPS for LFT) — VERIFIED seed (C4).
**Reason for root choice:** the benchmark target whose lineage is mapped.
graph_mode is OFF, so no lineage graph files are produced.

## Current Optimization Target

- Cover: maximize `recall + coverage + verification - human_cost - missed_risk`.

## Budget

- **Used: 14** web calls (mirror of the round_log.md call ledger, which is
  authoritative). Cap: 40. Stopped under budget.

## Seed Verification

Seed CONFIRMED via arXiv abs + HTML + web search: "Stochastic Path Sampler For
Lattice Field Theory", Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini,
Kai Zhou; created 2026-06-11, updated 2026-06-15. Method: path-space
variational free energy with an extended-space Independence Metropolis–Hastings
correction. Full text read (E0001).

## Facet Status

- F1 learned samplers for unnormalized targets: MET (>=8 verified: PIS, DDS,
  CMCD, Improved-diffusions, optimal-control, NETS, SNF, Boltzmann Generators,
  FAB).
- F2 learned samplers for lattice field theory: MET (>=12 verified: Albergo-
  Kanwar-Shanahan, Kanwar, Albergo fermionic/Schwinger, Nicoli, Gerdes,
  Caselle SNF, Wang-Aarts-Zhou, ...).
- F3 correction/exactness mechanisms: MET (IMH, importance reweighting,
  SNF/Jarzynski nonequilibrium, NETS transport, FAB α-divergence AIS,
  trajectory balance).

## Current Next Best Action

**Action:** stop and report.
**Reason:** three facets covered and cross-validated; marginal yield now mostly
duplicates/foundational; well under the 40-call cap.
**Expected gain:** low. **Expected cost:** n/a. **Required user input:** none.

## Stop Status

**Current stop status:** saturated_under_budget (with recorded residual risk).
**Reason:** facet quotas met + cross-validated at 14/40 calls.
**Remaining risks:** forward-citation closure not done (graph_mode OFF); 9
lineage entries remain C1 bib-of-C4; AFT arXiv id unverified. See
coverage_stopping_report.md.

## Validator Result

`python3 scripts/validate_run_state.py <run-dir>` was run at stop. Exact output:

```
run:     .../arms/opus-4-8-high
profile: literature
status:  CONSISTENT
EXIT=0
```

Interpretation: all mandatory (literature profile) + full-set files are on
disk, every on-disk file has a manifest row, and the call-ledger total (14)
matches the `Used: 14` budget mirror. The initial run flagged one error
(`sources/pdfs/` directory row marked `on_disk`); this was corrected to
`not_applicable` because the validator reconciles only top-level files, after
which it passed. The 7 PDFs are individually integrity-logged (E0005–E0011).
