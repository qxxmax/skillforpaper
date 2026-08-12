# Research State

## Project

**Research question:** Which prior methods does "Stochastic Path Sampler for
Lattice Field Theory" (arXiv:2606.13790) directly build on, in the two families
(a) learned/neural samplers for unnormalized target distributions and
(b) learned samplers for lattice field theory — and what is each one's verified
identity (exact title, authors, arXiv ID)?
**Primary intent:** locate
**Secondary intent:** learn
**Risk level:** medium
**Current round:** R0001
**Current status:** stopped

**Budget mirror (authoritative counter is the round_log.md call ledger):**
Used: 5 of 10 web calls. 5 remaining, deliberately unspent.

## Mode Decision

```yaml
intent_mode:
  primary: locate
  secondary: learn
risk_level: medium
current_action: locate_source
output_mode: evidence_table
```

Reason for `locate` as primary rather than `cover`: the task fixes a bounded
predecessor set defined by the focal paper's own text and asks for identity
verification (exact title, authors, arXiv ID) of each member. No high-recall or
completeness claim is requested or made, and the scan level is quick, so the
`cover` loop (query expansion, forward/backward snowballing, exclusion audit,
missing-risk estimation) is out of scope. `learn` is secondary because the
predecessors have to be grouped into the two named method families.

## Scope

### Inclusion Criteria

- Works the focal paper itself names as the family it adapts or contrasts
  against, in the two requested families:
  - data-free/learned samplers for unnormalized targets (path-space KL,
    stochastic-control, and trajectory-balance formulations);
  - learned (flow, diffusion, autoregressive, stochastic-flow) samplers for
    lattice field theory.
- Works whose identity could be verified by an authoritative arXiv record
  fetched inside this run's call budget.

### Exclusion Criteria

- Thermodynamics/entropy-production application citations outside sampling
  (materials, ecology, neuroscience, economics, information theory): cited by
  the focal paper for context, not sampler predecessors.
- Generic ML background not specific to sampling unnormalized targets
  (e.g. neural ODEs, score matching as a generative technique).
- Pre-arXiv foundations (stochastic quantization: Parisi & Wu 1981; Damgaard &
  Hüffel 1987) — real intellectual ancestors, but not learned samplers and not
  arXiv-identifiable; recorded as context in the candidate pool only.

### Time Range

1981 (context only) to 2026; verified predecessors span 2019-2026.

### Language Range

English.

### Source / Database Range

arXiv abstract page for the focal paper (full text, HTML v1 rendering) and the
arXiv API (`export.arxiv.org/api/query`) for authoritative metadata. No other
database was queried at this scan level.

### Human Budget

- Max rounds: 1
- Max papers to screen: ~40 bibliography entries of the focal paper
- Max full texts to verify: 1 (the focal paper)
- Max screenshots to capture: 0 (screenshot policy: on-demand, the quick-scan
  default; no screenshots requested, none captured)

## Root Configuration For Graph

**Root type:** paper
**Root node(s):** P0000 = arXiv:2606.13790, Stochastic Path Sampler for Lattice
Field Theory.
**Reason for root choice:** the question is defined entirely by this paper's own
lineage claims, so backward citation from this single root is the only route
that can answer it.
**graph_mode:** off (no lineage graph requested; no relation ledger produced).

## Current Optimization Target

Locate: minimize `time_to_verified_source` — reach an authoritative arXiv record
for every claimed predecessor at the lowest call cost. Achieved by (i) taking
the focal paper's full text in one fetch, which yields both the lineage
statements and the bibliography, and (ii) batching identity verification into
arXiv API `id_list` / boolean-title queries instead of one fetch per paper.

## Findings Summary

The focal paper states its own lineage explicitly in Section 1, so the
predecessor set is author-asserted (C4 quote evidence) and each member's
identity is independently confirmed against arXiv metadata (C2). Three groups:

1. **Data-free learned samplers for unnormalized targets** — the family the
   paper says it adapts: Path Integral Sampler (2111.15141), Denoising
   Diffusion Samplers (2302.13834), the optimal-control / time-reversed
   diffusion sampler (2211.01364), improved sampling via learned diffusions
   (2307.01198), Controlled Monte Carlo Diffusions (2307.01050), and NETS
   (2410.02711). CMCD is singled out by the focal paper as the one that, like
   SPS, learns both forward and backward drifts.
2. **Trajectory-balance lineage** — the source of the "Trajectory Level
   Balance" objective SPS enforces on path space: GFlowNets (2106.04399),
   GFlowNet Foundations (2111.09266), and Trajectory Balance (2201.13259).
3. **Learned samplers for lattice field theory** — flow-based MCMC
   (1904.12072), diffusion models as stochastic quantization (2309.17082,
   which SPS also contrasts against on the learned-versus-manual diffusion
   coefficient), stochastic normalizing flows in ML (2002.06707) and their
   lattice non-equilibrium formulation (2201.08862, 2210.03139), deep
   generative estimation of thermodynamic observables (2007.07115, whose
   L x 8 finite-temperature geometry SPS reuses), plus the same-collaboration
   antecedents 2211.03470, 2502.02127, 2512.19575 and 2605.11199.

## Current Next Best Action

**Action:** stop; hand the evidence table back to the requester.
**Reason:** every predecessor in the two requested families that the focal paper
names as a direct antecedent now has an independently fetched arXiv record. The
next marginal action (forward-citation expansion, or independent cross-validation
of the ~15 bibliography-only lattice/diffusion entries) belongs to a full scan,
not a quick one.
**Expected gain:** low at this scan level.
**Expected cost:** 1-6 further calls.
**Required user input:** scope decision — whether to promote this to a full scan
with citation snowballing and a cross-validation matrix.

## Stop Status

**Current stop status:** saturated_under_budget
**Reason:** the question is bounded by one root paper's own lineage statements;
all in-scope members are verified at C2 or better with 5 of 10 calls unspent.
**Remaining risks:**

- Identity verification rests on a single authoritative channel (arXiv). Journal
  or publisher records were not independently checked, so reference 34's
  two-channel cross-validation rule is not satisfied; journal references quoted
  here come from the arXiv `journal_ref` field, not from the publisher page.
- Roughly fifteen further lattice flow/diffusion works are cited by the focal
  paper but stay at `C1(bib-of-C4)`: their metadata was read inside a
  C4-verified full text and is not independently sourced. They are listed as
  unconfirmed in `candidate_pool.md` and are not asserted as verified.
- The focal paper's bibliography renders the Fourier-flow first author as
  "S. Chen"; the arXiv record says "Shile Chen", who is a different person from
  SPS co-author Shiyang Chen. Recorded so the initial is not misread as
  same-author lineage.
- No forward-citation pass, so a more recent method that supersedes this lineage
  would not have been seen.

## Validator

`python3 scripts/validate_run_state.py <this directory>` (run at stop):
status **CONSISTENT**, profile `literature`, 4 manifest rows (the manifest itself
needs no row), 0 errors, 0 warnings, exit code 0. Recorded in `round_log.md`
R0001 as the closing action.
