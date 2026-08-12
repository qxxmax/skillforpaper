# Round Log

Full-scan benchmark arm fable5-thinking-max. Each round: diagnosis, action,
result, file patches, next step.

## Call Ledger

Only authoritative budget counter (HARD CAP 40). One search query = one call;
one URL fetch = one call; one PDF download = one call; retries/failures count
and are noted.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed identity verified: title/authors/date/abstract/subjects (E0001) | 1/40 |
| 2 | R0001 | fetch (PDF) | https://arxiv.org/pdf/2606.13790 | seed PDF 33 pp, 2,263,775 B → sources/pdfs/2606.13790_SPS.pdf; full text + 58-item reference list extracted (E0002) | 2/40 |
| 3 | R0002 | search | arXiv API Q001 "normalizing flow"+"lattice field theory" | total 47, 30 returned, 3 new includes + monitor tail | 3/40 |
| 4 | R0002 | search | arXiv API Q002 "flow-based sampling"+"lattice" | total 17, 2 new includes (incl. bib[9] ID recovery), many dedups | 4/40 |
| 5 | R0002 | search | arXiv API Q003 "stochastic normalizing flows" | total 20, P0014 arXiv ID recovered, 3 new includes | 5/40 |
| 6 | R0002 | search | arXiv API Q004 "annealed importance sampling"+"normalizing flow" | total 6, 3 new includes (AFT, CRAFT, FAB) | 6/40 |
| 7 | R0002 | search | arXiv API Q005 "Boltzmann generator" | total 50, 1 core include (1812.01729), heavy molecular-conformer noise | 7/40 |
| 8 | R0002 | search | arXiv API Q006 "unnormalized"+"neural"+"sampler" | total 23, SEED RECALLED, 4 new includes incl. same-author 2607.15682 | 8/40 |
| 9 | R0002 | search | arXiv API Q007 "diffusion model"+"lattice gauge theory" | total 6, 1 new include, rest dedup | 9/40 |
| 10 | R0002 | search | arXiv API Q008 "trivializing"+"lattice" | total 3762 (noisy), 5 new includes incl. Luescher 0907.5491 | 10/40 |
| 11 | R0002 | search | arXiv API Q009 "Jarzynski"+"lattice" | total 32, 3 new includes (1604.05544 root), rest dedup/out-of-scope | 11/40 |
| 12 | R0003 | fetch | arXiv API id_list 1809.10606,2201.13259,1505.05770,1907.05600,2106.04399 | all 5 hypothesized identities CONFIRMED (titles+authors match bib) (E0003) | 12/40 |
| 13 | R0003 | fetch | S2 batch POST /paper/batch (56 IDs) | FAILED — HTTP 429 rate limit; retried as call 17 | 13/40 |
| 14 | R0003 | fetch | S2 citations of arXiv:1904.12072 (limit 100) | 100 citing records; ~9 new in-scope keepers, long monitor tail (E0007) | 14/40 |
| 15 | R0003 | fetch | S2 references of arXiv:2111.15141 (limit 100) | 63 refs; mechanism roots recovered: Neal AIS physics/9803008, SMC samplers cond-mat/0212648, A-NICE-MC, NeuTra, i-flow, Nicoli PRE estimator (E0006) | 15/40 |
| 16 | R0003 | fetch | S2 citations of arXiv:2606.13790 (seed) | 3 citing papers: 2607.21436, 2607.15682, 2607.08505 (E0005) | 16/40 |
| 17 | R0003 | fetch | S2 batch POST /paper/batch (63 IDs, retry of call 13) | 63/63 resolved; two-source metadata for whole pool + venues + citation counts (E0004) | 17/40 |
| 18 | R0004 | search | INSPIRE API q=arxiv:2606.13790 | seed record confirmed, 3 citations (INSPIRE-scoped) (E0008) | 18/40 |
| 19 | R0004 | search | INSPIRE API OR-query 13 core arXiv IDs | 12/13 resolved with venues; 2002.06707 not indexed (blind spot noted) (E0008) | 19/40 |
| 20 | R0005 | fetch (PDF) | arxiv.org/pdf/1904.12072 | 13 pp, 884,944 B, title verified (E0009) | 20/40 |
| 21 | R0005 | fetch (PDF) | arxiv.org/pdf/2002.06707 | 21 pp, 7,114,775 B, title verified (E0010) | 21/40 |
| 22 | R0005 | fetch (PDF) | arxiv.org/pdf/2201.08862 | 32 pp, 899,741 B, title verified (E0011) | 22/40 |
| 23 | R0005 | fetch (PDF) | arxiv.org/pdf/2111.15141 | 26 pp, 2,713,763 B, title verified (E0012) | 23/40 |
| 24 | R0005 | fetch (PDF) | arxiv.org/pdf/2302.13834 | 30 pp, 4,179,526 B, title verified (E0013) | 24/40 |
| 25 | R0005 | fetch (PDF) | arxiv.org/pdf/2309.17082 | 31 pp, 2,486,741 B, title verified (E0014) | 25/40 |
| 26 | R0005 | fetch (PDF) | arxiv.org/pdf/2410.02711 | 31 pp, 2,113,233 B, title verified (E0015) | 26/40 |
| 27 | R0006 | fetch | arXiv API id_list 1910.13496,1711.09268,physics/9803008,cond-mat/0212648 | all 4 confirmed: Nicoli estimator (ERQ0002 resolved), L2HMC new candidate, Neal AIS + SMC two-source (E0016) | 27/40 |
| 28 | R0006 | search | arXiv API Q_adv "neural network"+"critical slowing down" | total 16; 1 new low-priority include (self-learning MC review), no new decision-changing family — saturation signal (E0017) | 28/40 |

## Rounds

## R0001

**Date:** 2026-08-12
**Intent mode:** cover (secondary: learn)
**Round goal:** verify seed identity, acquire full text, extract backward-citation candidates and anchored keywords.

### Diagnosis

- Seed recall: seed itself now verified at C3.
- Topic coverage: 0 before this round.
- Biggest missing risk: everything downstream depends on seed reference list.

### Chosen Action

Fetch arXiv abs page + PDF of 2606.13790 (2 calls).

### Execution Result

- Seed confirmed: "Stochastic Path Sampler For Lattice Field Theory", S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou, arXiv 2026/06/11, hep-lat, 32 pp + refs (PDF has 33 pages). Mechanism per abstract: learnable forward/backward stochastic dynamics, path-space variational free energy (entropy-production upper bound), extended-space Independence Metropolis–Hastings correction; 2D φ⁴; compared to HMC.
- 58-item reference list extracted locally (free). ~40 in-scope backward candidates pooled at C1(bib-of-C3); bib entries without printed arXiv IDs kept at C1 with `arXiv ID unverified` notes.
- Bib items screened out at bib level (not pooled, reason logged here, no silent deletion from the pool since they never entered it): refs [39–48], [54] (general entropy-production/information-thermodynamics background, not samplers), [55–57] (classical MCMC scaling / KL divergence background), [2] (Neural ODE — architecture background; monitor note in screening table), [46–48] (information thermodynamics).
- New EvidenceIDs: E0001 (seed abs page, C2), E0002 (seed PDF integrity + full text, C3).

### File Patches

- candidate_pool.md: +40 rows (P0001–P0040).
- evidence_registry.md: E0001–E0002.
- keyword_ledger.csv: T001–T024 with seed-abstract/bib anchors; hypothesis terms flagged.
- query_matrix.csv: Q001–Q015 planned.
- search_route_log.md: RT01 executed rows.
- output_manifest.md: batch status update.

### Next Best Action

Run lexical arXiv API queries (RT02) across the three facets, then citation expansion.

### Stop Decision

continue — budget 2/40 used.

## R0002

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** lexical recall across all three facets via 9 arXiv API queries (Q001–Q009).

### Diagnosis

- Seed recall: PASSED — Q006 returned the seed 2606.13790 itself.
- Biggest pre-round risk: families absent from seed bib (Boltzmann generators, AIS/AFT line, trivializing maps, non-learned Jarzynski-for-lattice line).

### Chosen Action

Run Q001–Q009 (9 calls, raw results saved to r0002_arxiv_results.json).

### Execution Result

- Raw hits (totalResults): 47+17+20+6+50+23+6+3762+32 = 3963 (Q008 dominated by generic lattice noise; only first 30 per query retrieved = 196 records screened).
- New candidates: P0041–P0066 (26 rows). Key recoveries: Luescher trivializing maps (0907.5491), Jarzynski-for-LGT (1604.05544), Boltzmann generators (1812.01729), AFT/CRAFT/FAB, same-author follow-up 2607.15682 (Qian).
- Identity recoveries: P0014 = arXiv:2002.06707; seed bib [9] = arXiv:2008.05456 (P0054).
- Noise patterns learned: "Boltzmann generator" → molecular conformer/protein noise; "trivializing"+"lattice" → generic lattice QCD noise; recorded in query_yield_log.csv.
- New keyword terms T025–T030 (search-derived, anchored to retaining query+paper).

### File Patches

- candidate_pool.md: +26 rows, P0014/P0054 updates, DEDUP0001–0004.
- query_yield_log.csv: Q001–Q009 rows.
- search_route_log.md: RT02 executed rows.
- keyword_ledger.csv: T025–T030; T023 status updated.
- round_log.md: ledger rows 3–11.
- research_state.md: budget mirror 11/40.

### Next Best Action

R0003 citation channel (Semantic Scholar): batch-verify pooled IDs + unresolved bib identities (VAN, trajectory balance, GFlowNet, Rezende, Song&Ermon), forward citations of P0002, backward references of P0029.

### Stop Decision

continue — 11/40 used; facets F1/F2/F3 all have candidates but cross-validation channel still single (arXiv only).

## R0003

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** citation-channel expansion (Semantic Scholar) + resolution of six unverified bib identities.

### Diagnosis

- Pre-round risk: pool single-channel (arXiv); six bib identities unresolved; mechanism roots (AIS, SMC) and forward lineage of seed missing.

### Chosen Action

Calls 12–17: arXiv id_list identity check; S2 batch (failed once, 429, retried per ≤3-failure rule); forward citations of P0002; references of P0029; forward citations of seed.

### Execution Result

- ERQ0001 resolved: all six missing identities confirmed (E0003, DEDUP0001).
- Whole pool (63 IDs) cross-validated in S2 (E0004) — two independent metadata sources for every pooled arXiv ID.
- Seed forward lineage found: 3 citing papers (E0005), incl. same-author 2607.15682 and two new candidates P0067–P0068.
- Mechanism roots recovered from PIS references (E0006): Neal AIS physics/9803008 (P0069), SMC samplers cond-mat/0212648 (P0070), plus learned-MCMC family P0071–P0074 and P0075 (Nicoli estimator, ID unverified → ERQ0002).
- P0002 forward set (E0007): 100 records screened, mostly monitor tail; confirms F2 saturation (nearly all high-relevance citing works already pooled).
- New candidates: P0067–P0075.

### File Patches

- candidate_pool.md: +9 rows; identity fixes P0010/P0035/P0036/P0039/P0040.
- evidence_registry.md: E0003–E0007; ERQ0001 resolved; ERQ0002 opened.
- round_log.md: ledger rows 12–17 (incl. failed call 13).
- research_state.md: budget mirror 17/40.

### Next Best Action

R0004: INSPIRE-HEP cross-validation (channel family #3, domain database) for seed + hep-lat core; then R0005 core PDF acquisition (C3 gate).

### Stop Decision

continue — 17/40 used.

## R0004

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** third-channel (INSPIRE-HEP domain database) cross-validation of seed + hep-lat core.

### Execution Result

- Seed record exists in INSPIRE with 3 citations (consistent with S2) — E0008.
- 12/13 core records resolved with journal venues (PRL, PRD, JHEP, Commun.Math.Phys.). Blind spot: 2002.06707 (NeurIPS-only, P0014) not indexed in INSPIRE — its identity remains two-source (seed bib + arXiv + S2), which is sufficient.
- Channel families used so far: arXiv identifier pages (RT01), arXiv API lexical (RT02), Semantic Scholar citation graph (RT03), INSPIRE-HEP domain DB (RT04) = 4 distinct channels.

### File Patches

- evidence_registry.md: E0008; round_log ledger rows 18–19; research_state mirror.

### Stop Decision

continue — 19/40; C3 gate still open.

## R0005

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** C3 source gate — acquire core full texts.

### Execution Result

- 7 core PDFs downloaded (calls 20–26), all valid, first-page titles/authors verified locally: P0002, P0014, P0015, P0029, P0030, P0019, P0034. With the seed (E0002), 8 PDFs on disk in sources/pdfs/ — C3 gate (≥6) PASSED.
- Core-set rationale: P0002 founding flow+MH for LFT (F2); P0014 SNF (F1/F3 mechanism bridge); P0015 SNF-as-nonequilibrium for LFT (closest predecessor family); P0029 PIS (closest general-sampler family, F1); P0030 DDS (F1); P0019 diffusion-as-stochastic-quantization for LFT (F2, same-author lineage); P0034 NETS (F1+F3 Jarzynski-weighted transport).
- Pool statuses updated: these 7 → confirmed C3.

### File Patches

- evidence_registry.md: E0009–E0015; candidate_pool.md: 7 status promotions; ledger rows 20–26.

### Stop Decision

continue — 26/40; one gap-fill + adversarial round (R0006) remains within budget.

## R0006 (final)

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** gap-fill unresolved identities + adversarial pass (same-method-but-older / negative / limitation work).

### Execution Result

- Call 27: 1910.13496 (Nicoli estimator — ERQ0002 resolved), 1711.09268 (L2HMC, new P0076), physics/9803008 (Neal AIS) and cond-mat/0212648 (SMC samplers) all confirmed by title/author match (E0016).
- Call 28 adversarial: 16 hits, 1 low-priority include (P0077 self-learning MC review), no new decision-changing family (E0017). Negative meaning of "critical slowing down" (control theory, neuroscience, climate) recorded.
- Saturation signal + all facet quotas met → STOP at 28/40.

### File Patches

- candidate_pool.md: P0075 update, +P0076, +P0077 (final pool: 77).
- candidate_screening_table.md: generated (77 pooled rows + monitor/exclude tiers).
- coverage_stopping_report.md: written.
- evidence_registry.md: E0016–E0017.
- query_matrix.csv / query_yield_log.csv / search_route_log.md: final statuses.
- search_budget_contract.md: actuals backfilled from this ledger.
- research_state.md: final state, mirror 28/40.
- output_manifest.md: final batch statuses.

### Stop Decision

**Stop status:** stopped_with_known_risk (saturated under budget)
**Reason:** see coverage_stopping_report.md — facet quotas exceeded, marginal yield low, budget 28/40; known gaps recorded (GAN-for-LFT line, grey literature, C1 tail).
