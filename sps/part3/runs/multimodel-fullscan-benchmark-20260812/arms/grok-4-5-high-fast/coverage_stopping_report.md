# Coverage Stopping Report

**Status:** stopped under budget with known residual risk — **do not claim completeness**.

## Traversed

- **Seed locate:** arXiv API + PDF + INSPIRE record for arXiv:2606.13790 (Chen–Qian–Aarts–Lucini–Zhou).
- **Channels (≥3):** arXiv, INSPIRE-HEP, Semantic Scholar (partial), OpenAlex, Crossref.
- **Lexical facets:** normalizing-flow LFT; stochastic normalizing flows; path/diffusion samplers (PIS/DDS/NETS); CRAFT/ECF; author Zhou lineage.
- **Citation expansion:** INSPIRE forward from Albergo 1904.12072 (239); S2 citation sample (20); INSPIRE forward from seed (3).
- **Backward (seed refs):** local PDF reference extract (not a web call) → arXiv ids used to prioritize PDFs/id_list verification.
- **C3 PDFs:** 7 OA arXiv PDFs with byte + page integrity notes.

## Not Traversed

- Google Scholar UI / SerpAPI.
- Web of Science / Scopus (blocked).
- Full publisher HTML landing pages (PRD/JHEP) beyond Crossref DOI for Albergo.
- Complete S2 graph for the **seed** (persistent 429).
- Exhaustive reading of all 239 Albergo citers (only top/sampled screened).
- G2 co-citation / bibliographic coupling automation.
- Grey literature (theses, unpublished notes) beyond INSPIRE/arXiv.
- graph_mode lineage graph files (explicitly OFF).
- Deep claim anchoring (C4 page/figure quotes) for non-seed PDFs.

## Facet Saturation (honest)

| Facet | Coverage judgment |
|---|---|
| F1 NF / neural MCMC unnormalized | Good for LFT; weaker for general Boltzmann ML outside HEP indexes |
| F2 path/diffusion/SNF | Core seed-cited ML + LFT SNF covered; broader ML venue depth limited |
| F3 LFT learned samplers | Strong via INSPIRE+arXiv |
| F4 correction/exactness | Mechanisms noted at abs/title level; not fully page-audited for every include |
| F5 SPS neighbors/authors | Author + forward seed cites covered under budget |

## Would Reopen Search If

1. Seed appears on S2 without 429 and shows unseen highly cited neighbors.
2. A new method family (not NF/SNF/diffusion/path/IMH/AIS) is claimed as SPS baseline in reviews.
3. User requires systematic-review-level recall across non-HEP ML venues (NeurIPS/ICLR full graph).
4. Ambiguous SNF 2020 arXiv pair (2002.06707 vs 2002.09547) must be canonically resolved for BibTeX.
5. Remaining call budget used for publisher pages + additional C3 PDFs (2003.06413, 2410.02711, 2201.13117).

## Stop Decision

**Decision:** `saturated_under_budget` (scoped landscape) / **stopped_with_known_risk**  
**Calls at stop:** **33/40**  
**Reason:** Required channel families searched or substituted; ≥6 C3 PDFs; marginal lexical routes adding mostly duplicates/noise; residual risks explicitly listed — **not** absolute completeness.
