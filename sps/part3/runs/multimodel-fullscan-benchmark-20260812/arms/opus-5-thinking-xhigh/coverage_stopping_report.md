# Coverage And Stopping Report

## Summary

- **Scan level:** full (`cover` mode), `graph_mode` off.
- **Objective mode:** high-recall under a hard 40-call cap.
- **Stop decision:** **stop** — `saturated_under_budget`, with 11 calls unspent.
- **Date:** 2026-08-12.

This report states what was traversed and what was not. It does **not** claim the
literature is complete, and the coverage numbers below are scoped to the six
channels listed in `channel_coverage_plan.md`.

## Funnel

| stage | count |
|---|---|
| raw records returned across 29 logged calls | 452 |
| distinct after deduplication by arXiv identifier | 298 (+1 INSPIRE record with no eprint) |
| screened `include` | 112 |
| — `confirmed` (≥2 independent channels) | 61 |
| — `candidate` (1 channel; labeled, not claim-usable) | 51 |
| `monitor` | 30 |
| `exclude` (reason recorded) | 156 |
| full texts downloaded (C3 gate) | 9 PDFs, 260 pages |
| mechanism sentences anchored at C4 | 18, across those 9 papers |

## Diagnostics

| diagnostic | result | interpretation | action taken |
|---|---|---|---|
| seed recall | The seed (2606.13790) was returned by Q01 (hep-lat lexical), Q03 (exactness lexical) and the INSPIRE route — three routes that do not use its identifier | The query vocabulary genuinely reaches the target region; this is the strongest single recall signal available without a labeled gold set | none needed |
| family recall | All six method families the seed names in its own introduction were recovered by non-bibliography routes, except autoregressive networks (2005.04857), which only the identifier route returned | One vocabulary gap: "autoregressive" was not in any lexical query | recorded in `search_scope.md`; would be a one-call fix |
| route overlap | 83 of 298 records (28%) returned by ≥2 independent routes | Substantial but not saturating overlap: routes are complementary rather than redundant, which argues against declaring high recall | kept as a limitation |
| marginal yield by round | New *include* records per query: 32, 27, 15, 8, 1, 3, 2, 3, 3, 7, 7, **4**, **0** | Monotone collapse. The last two rounds added 4 and 0 new includes | stop condition met |
| consecutive no-new-family rounds | 2 (Q12 saturation probe; Q13 NETS forward citations) | Q12 returned 108 matches and no new family; Q13 returned 68 citing papers, 19 from 2026, all inside families already mapped | stop condition met |
| facet coverage | F1 = 39, F2 = 67, F3 = 30 include records; every facet has ≫3 representatives and ≥3 read in full | All three facets of the question are populated with verified records | none needed |
| estimated missing items | **not estimated** | A capture–recapture estimate would need two genuinely independent indexes; every discovery route here is arXiv-centric, so any number computed from this run would be misleadingly small | explicitly declined; recorded as a risk instead |
| singleton / doubleton pattern | 215 of 298 records were returned by exactly one route | High singleton fraction is the classic signature of *incomplete* coverage. It is reported here rather than explained away | recorded as the primary residual risk |
| adversarial pass | Executed: older-method layer (physics/9803008, 1105.2278, 1706.07561, 1802.02840), scaling critiques (2211.07541, 2301.01504), failure-mode papers (2302.14082, 2502.06685, 2302.04763), and reviews framing the field differently (2101.08176, 2504.18126, 2401.01297, 2303.15136) | The landscape is not one-sidedly positive | complete |
| decision sufficiency | Sufficient to describe the predecessor landscape and the correction taxonomy; **not** sufficient to support a novelty claim against the trivializing-map or annealed-transport families | Those families are abstract-level only | recorded as reopening trigger #1 |

## What Was Traversed

- The seed's full text and its complete 58-entry bibliography, with 32 in-scope
  identifiers verified against arXiv.
- Four lexical facet queries (408 total matches reported, 202 records retrieved),
  two exact-title routes, two INSPIRE queries, one general web search.
- Two forward-citation expansions (seed, NETS), one Semantic Scholar batch
  cross-validation of 37 core records, one Crossref resolution of 8 DOIs, one
  successful publisher page.
- Nine full texts covering all three facets, with the correction mechanism located
  verbatim in each.

## What Was Not Traversed

- **No Google Scholar, OpenAlex, Web of Science, Scopus, or ADS.** Every discovery
  route was arXiv-centric.
- **No co-citation and no bibliographic-coupling pass** (G2), and no dedicated
  author-channel query — author lineage was reconstructed from names already
  present in retrieved records.
- **Forward citations expanded on 2 nodes only**; the four highest-citation hubs
  in the pool were not expanded.
- **About 208 matched arXiv records were never retrieved** because result sets
  were truncated at 50–60.
- **103 of 112 include records were never opened**; 51 rest on a single channel.
- **English-language records only.** No grey-literature channel, no non-arXiv
  proceedings search, one publisher blocked.

## Residual Risks

| risk | likely impact | mitigation / monitor trigger |
|---|---|---|
| arXiv-centric discovery | A journal-only or non-arXiv predecessor is invisible | run one OpenAlex query on the same facets and measure overlap |
| 215 singleton records | Suggests the route set has not saturated the space | more routes, not more results per route |
| shallow forward expansion | A 2025–26 method citing PIS or Albergo but not the seed or NETS is missed | expand 2111.15141 and 1904.12072 forward |
| abstract-level mechanism claims for 103 records | The F3 taxonomy could mis-assign a mechanism | download PDFs before any mechanism claim enters public prose (ERQ0003) |
| 51 single-channel identities | Identity error possible | one Semantic Scholar batch call (ERQ0002) |
| SciPost blocked | SciPost records lack venue-page confirmation | retry from a different client or accept Crossref |
| high 2026 publication rate | Snapshot decays in weeks | re-run the forward-citation check monthly |
| probable duplicate pair unresolved | Method count off by one | check the EPJC record (ERQ0004) |

## Stop Rationale

Another round is **not** expected to change the landscape's shape: the last two
rounds added four and then zero new include records, no new method family appeared
in either, and every family named by the seed plus two families the seed omits
(trivializing maps; annealed flow transport) are already mapped with verified
identifiers. The remaining budget (11 calls) would be better spent on *depth* —
clearing the 51 single-channel identities and opening PDFs for the trivializing-map
lineage — than on more breadth, and that work is queued as ERQ0002/ERQ0003 rather
than done here, because the task's deliverable is the landscape map.

Another round **is** required before any of the following: a novelty claim against
the trivializing-map or annealed-transport families, a systematic-review framing,
or any statement about a specific baseline's exactness proof.

**Coverage statement:** this search has auditable coverage of the three stated
facets under an arXiv-centric, English-language, six-channel scope as of
2026-08-12. It is not complete, and the singleton fraction above is direct evidence
that it is not.
