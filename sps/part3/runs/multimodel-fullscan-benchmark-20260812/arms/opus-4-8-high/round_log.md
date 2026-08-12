# Round Log

Full-scan benchmark arm `opus-4-8-high`. graph_mode OFF. Hard cap 40 web calls.

## Call Ledger

Authoritative budget counter. One search = one call; one URL fetch = one call;
one PDF download = one call. Local file reads (of already-fetched content) are
free. Backfilled into `search_budget_contract.md` actuals at stop.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed full text + complete reference list (backward lineage) | 1/40 |
| 2 | R0001 | search | "Stochastic Path Sampler" lattice field theory 2606.13790 | seed identity + authors + abstract confirmed (arXiv HTML) | 2/40 |
| 3 | R0002 | fetch | Semantic Scholar batch API (12 arXiv IDs) | year/venue/DOI cross-validation of 12 predecessors | 3/40 |
| 4 | R0002 | fetch | inspirehep.net literature q=arxiv:2003.06413 | INSPIRE record + DOI + PRL pub info (Kanwar 2020) | 4/40 |
| 5 | R0003 | fetch | https://arxiv.org/pdf/1904.12072 | PDF (Albergo-Kanwar-Shanahan), 884,944 B | 5/40 |
| 6 | R0003 | fetch | https://arxiv.org/pdf/2111.15141 | PDF (Path Integral Sampler), 2,713,763 B | 6/40 |
| 7 | R0003 | fetch | https://arxiv.org/pdf/2302.13834 | PDF (Denoising Diffusion Samplers), 4,179,526 B | 7/40 |
| 8 | R0003 | fetch | https://arxiv.org/pdf/2201.08862 | PDF (SNF as non-equilibrium transforms), 899,741 B | 8/40 |
| 9 | R0003 | fetch | https://arxiv.org/pdf/2309.17082 | PDF (Diffusion = stochastic quantization), 2,486,741 B | 9/40 |
| 10 | R0003 | fetch | https://arxiv.org/pdf/2007.07115 | PDF (Nicoli thermodynamic observables), 618,576 B | 10/40 |
| 11 | R0003 | fetch | https://arxiv.org/pdf/2410.02711 | PDF (NETS transport sampler), 2,113,233 B | 11/40 |
| 12 | R0004 | search | Boltzmann generators Noe 2019 deep learning arXiv | adjacent family (1812.01729 / Science) confirmed, not in seed bib | 12/40 |
| 13 | R0004 | search | annealed flow transport / FAB Midgley arXiv | adjacent families (2208.01893, 2111.11510, AFT/PMLR) confirmed | 13/40 |
| 14 | R0004 | fetch | Semantic Scholar batch API (7 arXiv IDs) | metadata cross-validation of adjacent F1 samplers | 14/40 |

**Total: 14/40. Stopped under budget at facet saturation.**

## R0001 — Seed lock + backward lineage

**Date:** 2026-08-12
**Intent mode:** cover (secondary: learn)
**Round goal:** verify seed arXiv:2606.13790 and harvest its reference list.

### Diagnosis
- Seed recall: seed unverified at round start.
- Biggest missing risk: fabricating a non-existent seed / mis-citing its lineage.

### Chosen Action
- Fetch arXiv abs+HTML and confirm via web search.

### Execution Result
- Seed CONFIRMED: "Stochastic Path Sampler For Lattice Field Theory",
  S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou; created 2026-06-11,
  updated 2026-06-15. Full text read (method: path-space variational free
  energy; extended-space Independence Metropolis–Hastings correction).
- Harvested full reference list (~57 entries) → backward-citation candidates
  (C1 bib-of-C4). New EvidenceIDs E0001–E0002.
- Stop decision: continue (cross-validate + acquire core PDFs).

## R0002 — Cross-validation (channels 2 & 3)

**Date:** 2026-08-12
**Intent mode:** cover
**Round goal:** raise bib-of-C4 candidates to C2 via independent channels.

### Diagnosis
- Confirmed/unconfirmed ratio low; bib entries single-source.

### Chosen Action
- Semantic Scholar batch (12 IDs) + INSPIRE-HEP record lookup.

### Execution Result
- 12 predecessors cross-validated (year/venue/DOI match seed bib) → C2.
- Kanwar 2020 independently confirmed on INSPIRE (PRL 125, 121601) → C2.
- New EvidenceIDs E0003–E0004. Stop decision: continue (acquire PDFs).

## R0003 — Core PDF acquisition (C3 gate)

**Date:** 2026-08-12
**Intent mode:** cover / learn
**Round goal:** download >=6 core PDFs, one+ per facet, record integrity.

### Execution Result
- 7 PDFs downloaded to sources/pdfs/, all valid `%PDF-` headers, sizes logged.
  → C3 for P0001-seed context, P0002, P0007, P0010, P0012, P0019, P0020, P0024.
- New EvidenceIDs E0005–E0011. Stop decision: continue (adversarial pass).

## R0004 — Adversarial / adjacent-family expansion + stop

**Date:** 2026-08-12
**Intent mode:** cover (adversarial: same-mechanism-older, out-of-bib families)
**Round goal:** catch adjacent learned-sampler families NOT in the seed bib.

### Diagnosis
- Seed bib is lattice-heavy; ML-sampler foundations (Boltzmann Generators) and
  flow+AIS correction families (FAB/AFT) risked being missed.

### Execution Result
- Found + cross-validated: Boltzmann Generators (1812.01729, Science 2019),
  FAB (2208.01893, ICLR 2023) + Bootstrap-Your-Flow (2111.11510),
  Annealed Flow Transport (Arbel et al., PMLR v139 2021).
- S2 batch confirmed 6 adjacent F1 samplers. New EvidenceIDs E0012–E0014.

### Next Best Action
- None. Facet quotas F1/F2/F3 each satisfied with >=3 verified representatives;
  marginal yield now mostly duplicates/foundational.

### Stop Decision
**Stop status:** saturated_under_budget (stopped_with_known_risk on graph closure)
**Reason:** 14/40 calls; three facets covered and cross-validated; graph_mode
OFF so no forward-citation closure was attempted (recorded as residual risk).
