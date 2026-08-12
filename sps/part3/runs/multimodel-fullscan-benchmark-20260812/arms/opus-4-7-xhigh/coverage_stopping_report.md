# Coverage And Stopping Report

## Summary

- Scan level: full
- Objective mode: high-recall under a hard 40-call cap
- Stop decision: **stop** (with monitor triggers recorded)
- Date: 2026-08-12

## Diagnostics

| diagnostic | result | interpretation | action |
|---|---|---|---|
| seed recall | 1/1 seed items verified across 3 channels (arXiv, INSPIRE-HEP, OpenAlex) | seed identity is not a source of residual risk | none |
| route overlap | INSPIRE ↔ arXiv seed reference list ~100% overlap by arXiv/DOI; INSPIRE fulltext ↔ arXiv API on Facet A/C query overlap only on the seed and IWSM candidate | independent routes give consistent picture for confirmed set; coverage searches surface a small pre-seed candidate tail | record tail as potentially-missed |
| estimated missing items | unknown; bounded above by "papers in hep-lat between 2025-01 and 2026-06 whose fulltext contains 'normalizing flow' or 'diffusion model' and are not in the seed's 58 refs" — roughly 12–15 items surfaced this run | non-trivial residual risk on Facet B potentially-missed predecessors | monitor via a second-round targeted spot-check per candidate |
| singleton / doubleton pattern | 15 candidates in P0060–P0074 are single-channel finds (INSPIRE fulltext or arXiv API only) | each needs a second-channel confirmation before promotion beyond C1 | out of budget this run |
| consecutive no-new-include rounds | R0005 (arXiv API adversarial) returned 1 new include (IWSM); the two INSPIRE fulltext queries each returned tails but overlapped substantially with seed refs; marginal yield now decision-neutral for the predecessor claim | stop criterion 6 met | stop |
| facet coverage | Facet A: 14 include + 2 potentially-missed. Facet B: 25 include + 12 potentially-missed. Facet C: 11 include + 8 potentially-missed. All facets ≥3 include with C1+; Facets A, B, C each have ≥3 C3 evidence rows | coverage floor for the landscape task is met | none |
| random / uncertainty safety sample | not run (would consume 2–3 additional calls); replaced by the adversarial phrase search on Facet A + Facet C | acceptable given the seed's own reference list already covers the ML lineage exhaustively | record limitation |
| decision sufficiency | for the "map the predecessor and adjacent-method landscape" task, the confirmed 47 in-scope seed references + 14 potentially-missed pre-seed candidates provide a sufficient landscape record with explicit gaps | yes | stop |

## Residual Risks

| risk | likely impact | mitigation / monitor trigger |
|---|---|---|
| Semantic Scholar channel blocked (429) | third-channel identity check used OpenAlex instead; no S2 CorpusID / co-citation graph gathered | if a follow-on run requires S2-specific citation-influence signals, retry with an API key |
| forward-citation channel empty | 0 papers cite the seed; if this reflects lag rather than actual absence, a real follow-up will emerge in ~4-8 weeks | re-run refersto:arxiv:2606.13790 monthly |
| single-channel P0060–P0074 candidates | 15 potentially-missed predecessors at C1; misclassifying any as "not in landscape" is a false-negative risk | each candidate needs 1 arXiv abs fetch (~15 calls total) to reach C2 |
| Wu-Köhler-Noe SNF (P0019) arXiv ID unrecovered | reference is asserted at C1(bib-of-C2 seed) via NeurIPS-only URL; not a scientific gap because the paper is well-known, but a provenance gap | 1 arXiv search would recover the ID (arXiv:2002.06707, unconfirmed here) |
| non-arXiv adjacent literature (stochastic-control theory outside cs.LG/hep-lat, e.g. applied probability) | possible missing predecessors from Schrödinger-bridge / stochastic-optimal-control literature outside my three channels | if the follow-on task is "learned samplers for unnormalized densities" narrowly, add ACM DL or arXiv math.PR searches |
| coverage tail beyond 2 pages of INSPIRE results | R-inspire-flow returned 69 hits; only top 25 inspected | request more pages (25 more hits) at cost 1 call each |
| non-English literature | none checked | monitor only |
| conference/PoS-only papers not in INSPIRE fulltext | possible under-coverage on LATTICE conference records | INSPIRE tag filter run at cost 1 call |

## Stop Rationale

Another search or screening round is **not expected to change the main line** of the predecessor / adjacent-method landscape claim, because:

1. The seed's own 58-reference bibliography, cross-verified in INSPIRE, is by construction a curated adjacent-method map produced by domain experts (Aarts, Lucini, Zhou groups). This gives high confidence on the confirmed portion of the landscape.
2. The three coverage searches produced ≥90% overlap with the seed's ref list on the top-25 slice; the fresh candidates (P0060–P0074) are recorded as potentially-missed at C1 metadata-only and openly flagged as such — they do not change the *shape* of the landscape (still three facets, same clusters), only its *density*.
3. Forward-citation traversal is empty by construction (seed is too recent), so no G1-forward round is possible.
4. Budget-aware stopping preserves 23 unused calls for a second-round promotion pass (each P0060–P0074 candidate can be verified with a single arXiv abs fetch) if the benchmark's downstream stage requests it.

Another round WOULD be triggered by any of the following:

- The benchmark scoring or downstream user asks for C2 promotion of the P0060–P0074 candidates.
- Any P0060–P0074 candidate is renamed as a must-cite predecessor by a reviewer.
- A monthly re-run of INSPIRE refersto:arxiv:2606.13790 returns citing papers (would open forward-citation snowballing).
- The claim scope shifts from "predecessor + adjacent" to "systematic review with completeness guarantee", which would require doubling the query matrix and adding grey-literature / thesis / patent channels.

## Coverage Statement (scope-limited)

This scan achieves **auditable coverage of the seed's cited predecessor set** on three channels, with 8 core PDFs on disk providing C3 evidence for representative papers spanning all three facets, and with 15 additional potentially-missed pre-seed candidates recorded at C1 metadata-only. The scan **does not** claim absolute completeness of the "learned samplers for unnormalized densities + lattice field theory + correction mechanisms" literature; a monitor loop trigger and a second-round promotion pass are recommended before promoting the potentially-missed candidates into a public artifact.
