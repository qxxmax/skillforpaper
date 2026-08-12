# Coverage And Stopping Report

## Summary

- Scan level: full (graph_mode OFF)
- Objective mode: high-recall cover within a 40-web-call hard cap
- Stop decision: stop (saturated_under_budget)
- Date: 2026-08-12
- Calls used: 24/40 (authoritative ledger: round_log.md)

## Funnel

raw hits ~173 (38 in-scope seed-bib refs + 114 arXiv-API hits + 3 S2 forward
citations + 8 INSPIRE hits + 10 web-search results; excludes the 46-ID S2
verification batch, which was identity checking, not discovery)
→ deduplicated pool 73 (P0001–P0073; 8 dedup groups recorded; ~75 further
raw hits kept in the non-pool monitor/excluded overflow, not silently dropped)
→ screened include 53 (monitor 20)
→ C3 full-text PDFs 9 (seed + 8 core, integrity notes E0002, E0006–E0013).

## Diagnostics

| diagnostic | result | interpretation | action |
|---|---|---|---|
| seed recall | seed self-recovered by INSPIRE topical search (Q014); 4 bib papers re-found by independent arXiv queries | routes reach the seed's own neighborhood | none |
| route overlap | RT1∩RT2 = 4 papers, RT2∩RT4 = 2, RT2∩RT5 = 1 | independent routes converge on the same core | supports adequacy |
| estimated missing items | not formally estimated (no capture-recapture at this budget) | unknown residual, esp. non-arXiv venues | honest gap, listed below |
| singleton / doubleton pattern | new-family yield per round: R0001: 6 families; R0002: 5; R0003: 0; R0005: 0 | marginal family yield hit zero for two consecutive rounds | stop gate satisfied |
| consecutive no-new-family rounds | 2 (R0003/R0005; R0004 was PDF acquisition) | keyword stop gate (ref 35) satisfied | stop |
| facet coverage | F1: 21 includes / 4 C3; F2: 32 includes / 5 C3; F3: 8 distinct mechanisms each with ≥1 verified paper | all facets ≥3 representatives | stop |
| channel coverage | arXiv (page + API), Semantic Scholar API, INSPIRE-HEP API, general web search = 4 families | ≥3 required channels met | stop |
| decision sufficiency | landscape map supports the benchmark deliverable | — | stop |

## What was traversed

- Seed identity 3-channel verified (arXiv, INSPIRE; S2 attempt rate-limited and
  logged); full text on disk.
- G1-backward: complete seed bibliography harvested with source anchors.
- G1-forward: 3 citing papers (S2-scoped, as of 2026-08-12).
- Lexical expansion over 7 arXiv-API axis-crossed queries + 2 adversarial web
  searches; 5 method families found beyond the seed's own bibliography
  (trivializing maps, Boltzmann generators, AFT/CRAFT/FAB, L2HMC-family,
  self-learning MC).
- Cross-validation: 46 arXiv IDs confirmed on a second channel in one S2 batch.

## What was NOT traversed (honest limits)

- No G2 co-citation / bibliographic-coupling / author-network expansion rounds
  (budget choice; author lineage partially visible via seed-author bib entries).
- Forward citations only for the seed, not for core predecessors (e.g. citing
  works of 1904.12072 number in the hundreds and were not enumerated).
- Non-arXiv/paywalled venues (JMLR/NeurIPS-only items, e.g. GFlowNet NeurIPS
  versions verified only via S2+bib; Boyda et al. arXiv ID resolved via S2 only).
- 9 pool entries remain C1(bib-of-C3) single-source (P0014, P0018, P0020,
  P0022, P0025–P0029); P0066/P0067 are S2-single-channel; P0071 identity is
  publisher-page-based without a verified arXiv ID. None are asserted beyond
  their labels.
- Q007 returned zero hits; the intended target (1910.13496) was recovered via
  another route, but the neural-IS facet may have additional members not found
  by phrase search.
- No screenshots (policy: none; link+extract evidence only).

## Residual Risks

| risk | likely impact | mitigation / monitor trigger |
|---|---|---|
| missed non-arXiv ML-venue samplers (JMLR/PMLR-only) | moderate: F1 frontier under-counted | reopen with OpenAlex/PMLR channel |
| 2026 parallel work indexing lag (seed is 2 months old) | new descendants/competitors appear | re-run forward-citation query monthly |
| single-source C1 entries wrong metadata | low: labeled explicitly | verify the 9 bib-only IDs on next round |
| condensed-matter SLMC / molecular-BG overflow tiers unscreened in depth | low for this task's facets | screen overflow tier if scope widens beyond LFT |

## What would reopen the search

(1) A reviewer or user names a family absent from the pool (e.g. neural
quantile/transport samplers, Schrödinger-bridge samplers as a distinct line);
(2) the seed is revised with new references; (3) any C1-labeled identity fails
verification; (4) the task scope extends to G2 author/co-citation expansion or
to non-lattice application domains.

## Stop Rationale

Two consecutive discovery rounds added no new method family; every facet has
multiple verified representatives and at least one C3 anchor; all mandatory
channels were used; 16 calls remain unspent, but expected marginal yield per
call is now dominated by within-family duplicates. Coverage is auditable under
the stated scope; completeness is NOT claimed.
