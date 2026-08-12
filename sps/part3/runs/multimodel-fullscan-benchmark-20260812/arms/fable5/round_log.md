# Round Log

## Call Ledger

Only authoritative budget counter (HARD CAP 40). One search query = one call,
one URL fetch = one call, one PDF download = one call; retries, failed, and
blocked calls count too. Local file reads are free.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed identity verified; arXiv served full HTML text incl. complete reference list with arXiv IDs (dated 2026-08-11) | 1/40 |
| 2 | R0001 | fetch (PDF) | https://arxiv.org/pdf/2606.13790 → sources/pdfs/2606.13790_sps.pdf | seed PDF, 2,263,775 bytes, 33 pages (C3 PDF 1/6) | 2/40 |
| 3 | R0002 | search | arXiv API Q003 "normalizing flow" AND "lattice field theory" | 25 hits; 8 pooled (P0040-P0047), 13 monitor overflow, 4 dups with bib | 3/40 |
| 4 | R0002 | search | arXiv API Q004 "Boltzmann generator" OR "neural sampler" | 25 hits; 1 pooled (P0048 Boltzmann Generators), 22 monitor overflow, 2 excluded | 4/40 |
| 5 | R0002 | search | arXiv API Q005 annealed flow transport / FAB / AIS+neural | 11 hits; 4 pooled (P0049-P0052), 3 monitor, 4 excluded | 5/40 |
| 6 | R0002 | search | arXiv API Q006 "trivializing map" | 25 hits; 4 pooled (P0053-P0056), 2 monitor, heavy pure-math noise → negative terms logged | 6/40 |
| 7 | R0002 | search | arXiv API Q007 neural+importance sampling+unbiased+lattice | 0 hits (query too restrictive; target paper later resolved as 1910.13496 via S2) | 7/40 |
| 8 | R0002 | search | arXiv API Q008 "generalizing Hamiltonian Monte Carlo" OR L2HMC | 13 hits; 4 pooled (P0057-P0060), rest excluded (classical HMC theory/off-topic) | 8/40 |
| 9 | R0002 | search | arXiv API Q009 "self-learning Monte Carlo" | 15 hits; 2 pooled (P0061-P0062), 13 monitor (condensed-matter variants) | 9/40 |
| 10 | R0003 | fetch (API POST) | Semantic Scholar /paper/batch, 46 arXiv IDs | all 46 records returned; second-channel identity for pool; 10 hypothesis IDs resolved | 10/40 |
| 11 | R0003 | fetch (API) | Semantic Scholar /paper/arXiv:2606.13790 | FAILED HTTP 429 (rate limit) — counts per contract | 11/40 |
| 12 | R0003 | fetch (API) | Semantic Scholar /paper/arXiv:2606.13790/citations | 3 forward citations (2607.21436, 2607.15682, 2607.08505) | 12/40 |
| 13 | R0003 | fetch (API) | INSPIRE-HEP q=arxiv:2606.13790 | 1 record; seed third-channel confirmation; earliest date 2026-06-11; 3 citations | 13/40 |
| 14 | R0003 | search | INSPIRE-HEP t:(generative/flow/diffusion/ML)+(sampling)+lattice | 8 hits; 2 new pooled (P0069, P0070); seed self-recovered (seed recall pass) | 14/40 |
| 15 | R0004 | fetch (PDF) | arxiv.org/pdf/1904.12072 | 884,944 B, 13 pp (C3 PDF 2) | 15/40 |
| 16 | R0004 | fetch (PDF) | arxiv.org/pdf/2111.15141 | 2,713,763 B, 26 pp (C3 PDF 3) | 16/40 |
| 17 | R0004 | fetch (PDF) | arxiv.org/pdf/2002.06707 | 7,114,775 B, 21 pp (C3 PDF 4) | 17/40 |
| 18 | R0004 | fetch (PDF) | arxiv.org/pdf/2201.08862 | 899,741 B, 32 pp (C3 PDF 5) | 18/40 |
| 19 | R0004 | fetch (PDF) | arxiv.org/pdf/2309.17082 | 2,486,741 B, 31 pp (C3 PDF 6) | 19/40 |
| 20 | R0004 | fetch (PDF) | arxiv.org/pdf/2302.13834 | 4,179,526 B, 30 pp (C3 PDF 7) | 20/40 |
| 21 | R0004 | fetch (PDF) | arxiv.org/pdf/1812.01729 | 10,488,625 B, 46 pp (C3 PDF 8) | 21/40 |
| 22 | R0004 | fetch (PDF) | arxiv.org/pdf/2309.01156 | 1,632,799 B, 11 pp (C3 PDF 9) | 22/40 |
| 23 | R0005 | search | web search: NF LFT critical slowing down / scaling limitations / mode collapse negative results | 5 results; limitation cluster confirmed; P0071, P0072 pooled; E0017 | 23/40 |
| 24 | R0005 | search | web search: benchmark evaluation neural samplers unnormalized densities 2024-2026 | 5 results; benchmark cluster (P0073); DIS/MCD/UHA/LDVI named as sub-branches; E0018 | 24/40 |

## R0001 — Seed verification and bibliography harvest

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** verify seed identity, obtain full text, extract G1-backward candidates and anchored keywords.

### Diagnosis
- Seed recall: seed verified (call 1); full text obtained (calls 1-2).
- Biggest missing risk before round: everything unverified.

### Chosen Action
Fetch arXiv abs page + PDF of 2606.13790.

### Execution Result
- Seed confirmed: "Stochastic Path Sampler For Lattice Field Theory", S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou; HTML page dated 2026-08-11.
- Complete reference list extracted → 38 in-scope candidates added to pool at C1(bib-of-C3) (P0002–P0039); out-of-scope thermodynamics/context refs recorded as excluded in screening table.
- Anchored keywords extracted (T011–T026 in keyword_ledger.csv): stochastic quantization, trajectory-level balance (GFlowNet lineage), Independence Metropolis-Hastings, path-space variational free energy, critical slowing down, topological freezing, etc.
- New EvidenceIDs: E0001–E0005.

### File Patches
- candidate_pool.md: +39 rows; evidence_registry.md: +5 rows; keyword_ledger.csv: +16 anchored terms; query_matrix.csv: Q001-Q002 executed; query_yield_log.csv: 2 rows; search_route_log.md: RT1 done; output_manifest.md: sources/pdfs row in_progress.

### Next Best Action
Run lexical arXiv API queries (RT2) to find families NOT cited by the seed (Boltzmann generators, neural importance sampling, learned-MCMC, trivializing maps, annealed flow transport lineage).

### Stop Decision
continue (2/40 used)

## R0002 — Lexical expansion (arXiv API), calls 3–9

**Date:** 2026-08-12. **Intent mode:** cover. **Goal:** find method families NOT cited by the seed.

### Diagnosis
Seed bib covers flow-for-LFT, SNF, diffusion-LFT, and the PIS/DDS/OC/CMCD/NETS ML family; suspected blind spots: Boltzmann generators, trivializing maps (pre-ML ancestry), AFT/CRAFT/FAB (SMC corrections), learned-MCMC kernels (L2HMC), self-learning MC.

### Result
All five suspected blind-spot families confirmed to exist and pooled: P0040–P0062. New facet-3 correction mechanisms mapped: SMC weights/resampling (AFT/CRAFT), AIS-driven training (FAB), exact-MH-inside-learned-kernel (L2HMC/SLMC). Q007 returned 0 hits (over-restrictive); noise patterns from Q006 recorded as negative terms.

### Stop decision: continue (9/40).

## R0003 — Citation + channel cross-validation (S2, INSPIRE), calls 10–14

**Goal:** second/third-channel identity verification; forward citations; domain-database recall check.

### Result
S2 batch verified 46 IDs in one call (E0014); 10 hypothesis IDs resolved (incl. VAN 1809.10606, SNF 2002.06707, Nicoli 1910.13496, adaptive-MCMC 2105.12603, review 2309.01156). Call 11 rate-limited (429, logged). Seed has 3 forward citations (E0016). INSPIRE confirmed seed (E0015) and added P0069 (scaling critique) + P0070; seed self-recovered in the INSPIRE topical search (seed-recall check passed).

### Stop decision: continue (14/40).

## R0004 — C3 source gate (PDF downloads), calls 15–22

8/8 PDFs downloaded, integrity notes E0006–E0013. C3 gate satisfied: 9 PDFs ≥ 6, covering seed, F2 founding paper, F2 SNF-lattice, F2 diffusion-SQ bridge, F2 review, F1 PIS/DDS/SNF/Boltzmann-generators.

### Stop decision: continue (22/40).

## R0005 — Adversarial pass (web search), calls 23–24

**Goal:** stop-gate adversarial search: negative results, limitation framing, competing surveys/benchmarks.

### Result
Call 23: limitation cluster confirmed (volume scaling, long-range correlations, mode collapse, "criticality transferred into training"); P0071 (learned trivializing gradient flows), P0072 pooled; E0017 registered. Call 24: F1 benchmark cluster (P0073 Beyond ELBOs) + named sub-branches DIS/MCD/UHA/LDVI (monitor tier); E0018. Neither round produced a NEW method family — two consecutive rounds without a new family ⇒ keyword/facet stop gate satisfied.

### Stop decision: stop — saturated_under_budget at 24/40 calls; residual risks recorded in coverage_stopping_report.md.
