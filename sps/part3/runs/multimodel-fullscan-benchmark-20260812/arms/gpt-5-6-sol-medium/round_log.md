# Round Log

## Call Ledger
| # | RoundID | type | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed identity, abstract, full HTML text, references | 1/40 |
| 2 | R0001 | PDF download | https://arxiv.org/pdf/2606.13790 | success: local core PDF | 2/40 |
| 3 | R0002 | search | exact SPS title + citations/related work | arXiv, DOI, INSPIRE, JHEP; seed cross-check | 3/40 |
| 4 | R0002 | search | learned neural samplers + PIS/DDS/CMCD | PIS, improved learned diffusions, SCLD, PDNS candidates | 4/40 |
| 5 | R0002 | search | arXiv LFT flow sampling + MH exact correction | flow review, 1904.12072, fermionic/multimodal works | 5/40 |
| 6 | R0002 | search | INSPIRE learned LFT sampler query | SNF SU(3), LFT score model, gauge-flow candidates | 6/40 |
| 7 | R0002 | search | learned flow + AIS/FAB + unnormalized target | FAB/Bootstrap Your Flow and reweighting evidence | 7/40 |
| 8 | R0002 | search | LFT flow mode collapse/scaling limitation | scaling audit, mode-collapse papers, review | 8/40 |
| 9 | R0003 | fetch | Semantic Scholar Graph API: ARXIV:2606.13790 | seed metadata plus 3 forward citations | 9/40 |
| 10 | R0003 | fetch | INSPIRE API query arxiv:2606.13790 | curated seed metadata, 58 references, 33 pages | 10/40 |
| 11 | R0003 | fetch | arXiv API exact phrase “stochastic path sampler” | 1 exact seed; 32-page arXiv record | 11/40 |
| 12 | R0004 | PDF download | https://arxiv.org/pdf/2111.15141 | success: PIS core PDF | 12/40 |
| 13 | R0004 | PDF download | https://arxiv.org/pdf/2302.13834 | success: DDS core PDF | 13/40 |
| 14 | R0004 | PDF download | https://arxiv.org/pdf/2307.01198 | success: learned-diffusion synthesis PDF | 14/40 |
| 15 | R0004 | PDF download | https://arxiv.org/pdf/2307.01050 | success: CMCD core PDF | 15/40 |
| 16 | R0004 | PDF download | https://arxiv.org/pdf/1904.12072 | success: foundational LFT flow PDF | 16/40 |
| 17 | R0004 | PDF download | https://arxiv.org/pdf/2201.08862 | success: lattice SNF PDF | 17/40 |
| 18 | R0004 | PDF download | https://arxiv.org/pdf/2309.17082 | success: LFT diffusion/SQ PDF | 18/40 |
| 19 | R0005 | fetch | arXiv API: “unnormalized target distribution” AND sampling | 20 returned / 23 indexed; mixed precision | 19/40 |
| 20 | R0005 | fetch | arXiv API: “lattice field theory” AND “normalizing flow” AND sampling | 20 returned / 31 indexed; multiple new LFT-flow candidates | 20/40 |
| 21 | R0005 | fetch | arXiv API: “lattice field theory” AND “diffusion model” | 9 returned; data-driven diffusion cluster and SPS citer | 21/40 |
| 22 | R0005 | fetch | Semantic Scholar Graph API: ARXIV:2111.15141 | PIS metadata, 63 references, 197 citations; high-noise forward set | 22/40 |
| 23 | R0005 | fetch | Semantic Scholar Graph API: ARXIV:1904.12072 | failed: HTTP 429 rate limit; no yield | 23/40 |
| 24 | R0005 | fetch | INSPIRE API author query “Zhou, Kai” AND lattice | valid call but 0 results (query syntax/coverage miss) | 24/40 |
| 25 | R0005 | search | SPS author-lineage query | Shiyang Chen INSPIRE profile; VAN and diagnostics leads | 25/40 |
| 26 | R0006 | fetch | arXiv API id_list for 7 downloaded predecessors | all 7 identities/abstracts verified in one batch | 26/40 |
| 27 | R0007 | search | learned sampler + exact correction / weights / SMC | NETS, LEAPS, reverse-diffusion SMC; mechanism closure | 27/40 |
| 28 | R0007 | fetch | arXiv API exact AFT query | AFT and CRAFT; SMC weights/resampling/MCMC family | 28/40 |
| 29 | R0007 | fetch | arXiv API exact FAB query | FAB and application record; AIS/reweighting family | 29/40 |
| 30 | R0007 | search | older neural MCMC / A-NICE-MC / Boltzmann generators | A-NICE-MC and LFT application; MH-corrected predecessor | 30/40 |
| 31 | R0007 | fetch | https://arxiv.org/abs/2607.15682 | SPS/PIS forward adjacent: corrected neural non-equilibrium HMC | 31/40 |
| 32 | R0007 | fetch | https://arxiv.org/abs/2607.21436 | SPS forward citation: stochastic quantization as optimal control | 32/40 |

This table is the authoritative budget counter; failures count.

## R0000 — Initialization
- Date: 2026-08-12
- Intent: cover (secondary: learn), full scan, graph_mode off.
- Result: manifest created first; scope, budget, channel, keyword/query, screening, and evidence ledgers initialized.
- Stop: continue to seed verification.

## R0001 — Seed verification
- Verified SPS on arXiv and acquired its PDF; extracted the full reference list and mechanism anchors.
- Stop: continue; independent channels and predecessor facets missing.

## R0002 — Broad lexical/facet discovery
- Six searches covered path samplers, LFT flows, INSPIRE-oriented records, AIS/SNF, and scaling/mode-collapse challenges.
- Stop: continue; cross-validation and full texts missing.

## R0003 — Channel cross-validation
- Cross-checked SPS through arXiv, Semantic Scholar, and INSPIRE; obtained 58 backward and 3 forward records.
- Stop: continue; core evidence-strength gap.

## R0004 — C3 acquisition
- Downloaded seven additional core PDFs (8 total); `pdfinfo` and text extraction succeeded for all.
- Registered PDF integrity and section-anchored correction evidence.
- Stop: continue; citation/author and correction-family closure missing.

## R0005 — Citation, author, and archive expansion
- arXiv returned 20 unnormalized-target, 20 LFT-flow, and 9 LFT-diffusion records.
- PIS graph returned 63 references and 197 citations; one Albergo Semantic Scholar request failed with HTTP 429, and one INSPIRE author query returned zero.
- Stop: continue; hydrate core identities and run adversarial closure.

## R0006 — Batch identity hydration
- All seven non-SPS core arXiv identities/abstracts were verified in one batch.
- No new method or correction family appeared.
- Stop: continue for one adversarial focused round.

## R0007 — Adversarial and correction closure
- Recovered AFT/CRAFT, FAB, NETS, LEAPS, reverse-diffusion SMC, A-NICE-MC, and two post-SPS adjacencies.
- Older-method, negative/scaling, and exactness searches added instances but no correction family beyond MH, path/work weights, and SMC/resampling.
- Funnel frozen: 434 raw route records → 368 deduplicated/screened → 31 includes → 8 C3 PDFs.
- Stop: **stopped with known risk at 32/40 calls**; see `coverage_stopping_report.md`.
