# Coverage And Stopping Report

## Summary

- Scan level: full (graph_mode OFF)
- Objective mode: high-recall within hard 40-call budget (scoping quality, NOT systematic-review completeness)
- Stop decision: stop (stopped_with_known_risk / saturated_under_budget)
- Date: 2026-08-12
- Calls used: 28/40 (27 successful, 1 failed-and-retried; round_log.md ledger is authoritative)

## What Was Traversed

- Seed verified to C3 (arXiv abs + PDF, 33 pp); all 58 seed references screened; ~40 in-scope backward candidates pooled.
- 10 lexical arXiv API queries (9 planned + 1 adversarial) across problem/method/correction/domain axis crossings from the anchored keyword ledger.
- Citation channel (Semantic Scholar): forward citations of the seed (3 records) and of the founding LFT-flow paper 1904.12072 (first 100), backward references of PIS 2111.15141 (63); batch identity resolution of all 63 pooled arXiv IDs.
- Domain database (INSPIRE-HEP): seed + 13 core hep-lat records cross-validated (12 resolved; NeurIPS-only 2002.06707 not indexed — expected blind spot).
- 8 core PDFs on disk with integrity notes (C3 gate ≥6 PASSED): seed, 1904.12072, 2002.06707, 2201.08862, 2111.15141, 2302.13834, 2309.17082, 2410.02711.
- Final pool: 77 candidates (P0001–P0077); 75 with verified arXiv IDs; 2 pre-arXiv mechanism roots (Parisi–Wu 1981, Jarzynski 2013 review) remain C1(bib-of-C3), explicitly labeled.

## Diagnostics

| diagnostic | result | interpretation | action |
|---|---|---|---|
| seed recall | PASS — Q006 lexical query independently returned the seed | query matrix reaches the seed's own niche | none |
| route overlap | high on F2 core (bib ∩ lexical ∩ citation ∩ INSPIRE all recover Albergo/Kanwar/Caselle clusters) | core F2 landscape is closed under current scope | none |
| facet coverage | F1: ≥10 candidates, 4 at C3; F2: ≥30 candidates, 4 at C3 (incl. seed); F3: ≥8 candidates, 3 at C3 | all three facets exceed the ≥3 representatives / ≥2 C3 quota | none |
| consecutive no-new-include rounds | R0006 adversarial round added only 1 low-priority include, 0 new method families | marginal yield low; saturation signal (single round only — see risks) | acceptable under budget |
| estimated missing items | unquantified; known named gap: GAN-based LFT samplers (Pawlowski–Urban-type line) not recovered by executed queries | one recognized family absent from pool | recorded below; would reopen search |
| singleton pattern | monitor tail dominated by singletons from single routes | typical long tail; low decision risk for landscape purpose | monitor tier |
| decision sufficiency | predecessor + adjacent-method landscape and exactness-mechanism taxonomy (reweighting / MH accept-reject / AIS-Jarzynski / SNF path-weights / control-based trajectory weights) are stable across last two rounds | sufficient for the mapping task | stop |

## What Was NOT Traversed (honest scope limits)

1. GAN-based samplers for LFT: a known family (e.g. GAN reduction of autocorrelations) was NOT recovered by the executed queries; no identity was verified, so nothing is asserted about it. Highest-priority reopen target.
2. Forward citations beyond the first 100 (S2 page 1) of 1904.12072; forward citations of other core papers (2002.06707: 225 citing, 2111.15141: 197 citing) were not enumerated.
3. Non-arXiv venues and grey literature: OpenReview-only workshop papers, theses, blog/code-first work; Google Scholar was not used as a channel.
4. G2 expansions (co-citation, bibliographic coupling, systematic author-network crawl) — only implicit same-author lineage screening was done (Chen/Qian/Aarts/Lucini/Zhou; Caselle/Cellini/Nada; MIT/DeepMind flow cluster).
5. Abstract-level (C2) checks for most non-core pool members — they remain C1 (two-source metadata), explicitly labeled; claims about their content must not be made from this run.
6. Indexing lag risk for mid-2026 records (seed's citation count will move).
7. Downstream synthesis artifacts (literature matrix, reviewer-comparison matrix, lineage snowball map, gap ledger) were not requested in this benchmark arm's mandatory file set and were not produced; producing them would require C2+ checks on more of the pool.

## Residual Risks

| risk | likely impact | mitigation / monitor trigger |
|---|---|---|
| missed GAN-for-LFT and other pre-2019 learned-proposal work | incomplete predecessor story for F2 | reopen with targeted queries ("adversarial network" + lattice/autocorrelation) and backward refs of P0002 |
| single-pass saturation evidence (only one adversarial round) | stop may be premature by the two-consecutive-rounds standard | one more focused round on F1 (e.g. "sequential Monte Carlo" + "normalizing flow", "Schroedinger bridge" + sampler) |
| C1-only tail (~65 papers without abstract checks) | mislabelled facet assignments possible | C2 pass before any public artifact cites them |
| S2/INSPIRE citation counts are channel-scoped and dated | numbers not comparable across channels | always quote with channel + date |
| non-arXiv/grey literature unsearched | applied or negative results missed | add Google Scholar / OpenReview channel on reopen |

## What Would Reopen The Search

- Any downstream artifact (report, related-work section, slides) that must cite the F2 predecessor story in detail → close gap 1 and run C2 checks.
- The seed paper being revised/published, or its citation count moving materially (monitor trigger).
- A reviewer or user naming any family not in the pool.

## Stop Rationale

Under the declared scope and the 40-call cap, another lexical or citation round is not expected to change the three-facet landscape: the last round added no new method family, all facet quotas are exceeded, the seed and its whole verified pool are cross-validated in at least two independent channels, and the C3 core covers every major mechanism family (flow+MH, SNF/nonequilibrium, AIS/Jarzynski weights, diffusion/control-based trajectory weights, stochastic quantization). The search has auditable coverage under this scope; it is NOT claimed to be complete.
