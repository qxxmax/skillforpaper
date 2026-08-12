# Research State

## Budget Mirror

The call ledger in `round_log.md` is authoritative; this line mirrors it.

**Calls used: 29** of a hard cap of 40 (11 unspent). Failed or blocked calls: 3
(one HTTP 301, one HTTP 400, one anti-bot interstitial) — all logged and counted.

## Project

**Research question:** Map the predecessor and adjacent-method landscape of
*Stochastic Path Sampler for Lattice Field Theory* (arXiv:2606.13790) across three
facets: (F1) learned/neural samplers for unnormalized target distributions,
(F2) learned samplers for lattice field theory, and (F3) the correction and
exactness mechanisms those samplers rely on.

**Primary intent:** cover
**Secondary intent:** learn
**Risk level:** high (a missed predecessor family is the failure mode this run exists to prevent)
**Current round:** R0009
**Current status:** stopped
**Scan level:** full · **graph_mode:** off (by task instruction) · **token policy:** balanced ·
**screenshot policy:** none (headless; raw API responses and PDFs stored instead)

## Scope

### Inclusion Criteria

- Methods that learn a sampler, transport, flow, or control for a target known only
  up to normalization.
- Learned samplers applied to lattice field theory or lattice gauge theory.
- Mechanisms that restore or quantify exactness for such samplers
  (Metropolis–Hastings correction, importance weights, Jarzynski/annealing weights,
  resampling, unbiased estimators).

### Exclusion Criteria

- Classical stochastic quantization / complex Langevin with no learned component.
- Generative modelling whose target is a data distribution rather than `e^{-S}`.
- GFlowNet or trajectory-balance work whose application is language or vision.
- ML for collider event generation and phase-space integration.
- Molecular and materials Boltzmann-generator applications (kept at monitor tier,
  not excluded, since they share the F1 mechanism).

### Time Range

No lower bound (the oldest included record is Neal's Annealed Importance Sampling,
physics/9803008, 1998). Upper bound: the state of the indexes on 2026-08-12.

### Language Range

English-language records only; no translated or non-English channel was searched.

### Source / Database Range

arXiv API, Semantic Scholar Graph API, INSPIRE-HEP API, Crossref, one publisher
page (Springer), one general web search. Google Scholar, Web of Science, Scopus,
OpenAlex, and ADS were **not** searched — see `channel_coverage_plan.md`.

### Human Budget

- Max rounds: 9 (used 9)
- Max web calls: 40 (used 29)
- Max screened candidates: no cap; 298 distinct records were screened
- Max full texts to verify: 9 (used 9)
- Max screenshots: 0 (policy: none)

## Root Configuration

**Root type:** paper
**Root node:** arXiv:2606.13790 (verified at C4, E0001–E0004, E0017–E0018)
**Reason for root choice:** the task names one seed; its 58-entry bibliography is
the highest-yield backward route, and its own related-work section names the six
method families that the independent routes were then tested against.

## Current Optimization Target

Cover: maximize recall and channel-verified coverage under the 40-call cap, while
keeping every unverified record explicitly labeled.

## Funnel

| stage | count |
|---|---|
| raw records returned across all 29 logged calls | 452 |
| distinct after deduplication by arXiv identifier | 298 (+1 INSPIRE record with no eprint) |
| screened `include` | 112 |
| of which `confirmed` (≥2 independent channels) | 61 |
| of which `candidate` (single channel, labeled, not claim-usable) | 51 |
| `monitor` tier | 30 |
| `excluded` with recorded reason | 156 |
| C3/C4 full texts downloaded | 9 (260 pages) |

## Current Next Best Action

**Action:** none this run — stopped.
**If resumed, the highest-value next action:** one Semantic Scholar batch call over
the 51 single-channel include records (clears ERQ0002 at a cost of one call), then
PDF acquisition for the trivializing-map lineage (0907.5491, 2212.08469, 2410.13161)
whose exactness mechanism is currently asserted from abstracts only.
**Required user input:** none.

## Stop Status

**Current stop status:** saturated_under_budget
**Reason:** two consecutive rounds added no new method family; the seed was
recovered independently by two keyword routes; every required channel family was
searched or explicitly marked blocked. Coverage is auditable **under this scope**;
the literature is **not** claimed to be complete.
**Remaining risks:** see `missing_risk_report.md` — no Google Scholar / OpenAlex /
Web of Science channel, one blocked publisher, 103 of 112 includes read at
abstract level only, forward-citation expansion limited to two nodes, and
English-only coverage.

## Validator Result

### `scripts/validate_run_state.py` — PASS

Command:

```
python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py \
  ~/Desktop/skillforpaper/sps/part3/runs/multimodel-fullscan-benchmark-20260812/arms/opus-5-thinking-xhigh
```

Output:

```
run:     ~/Desktop/.../arms/opus-5-thinking-xhigh
profile: literature
status:  CONSISTENT
```

Exit code **0**. Zero errors, zero warnings. This confirms that the literature
profile's mandatory files exist, that every manifest row claiming `on_disk` or
`verified` has a real file, that every top-level file has a manifest row, and that
the call-ledger total (29) matches the budget mirror at the top of this file.

### `scripts/validate_keyword_query_graph.py` — ledgers clean

Run because the keyword and query ledgers are present (SKILL.md step 23). The
script requires a relation ledger argument even when `graph_mode` is off, so the
skill's own `templates/relation_ledger_template.csv` was passed as a placeholder.

```
"counts": {"keywords": 35, "queries": 19, "relations": 1},
"schemas": {"keyword_ledger": "canonical", "query_matrix": "canonical",
            "relation_ledger": "canonical"},
"errors": ["relation row 2: missing EvidenceID",
           "relation row 2: missing RelationBasis"]
```

Both remaining errors belong to the **placeholder template**, not to this run's
files. `keyword_ledger.csv` (35 terms) and `query_matrix.csv` (19 rows) validate
with zero errors against the canonical schema; an earlier run flagged one real
error in this run's own data — a `T001-T035` range shorthand in the SourceTermIDs
of the Semantic Scholar batch query — which was corrected to an explicit TermID
list before this pass. No relation ledger of this run's own exists, because
`graph_mode` is off.

Schema validation is a provenance check. It shows that term and query provenance
is inspectable; it does not certify that the scientific classification is right.
