# Round Log

Run: `multimodel-fullscan-benchmark-20260812` / arm `opus-5-thinking-xhigh`.
Date: 2026-08-12. Scan level: full. `graph_mode`: off.

## Call Ledger

This table is the only authoritative budget counter; `research_state.md` mirrors
it. One search query = one call, one URL fetch = one call; retries, failed, and
blocked calls count too. Local file reads, PDF text extraction, and re-reads of
already-fetched responses are free and are not logged. Hard cap: 40.

| # | RoundID | type | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | HTTP 200, 42,328 B; seed identity: title, 5 authors, hep-lat, submitted 2026-06-11 | 1/40 |
| 2 | R0001 | fetch | https://arxiv.org/pdf/2606.13790v1 | HTTP 200, 2,263,775 B, 33 pages; full text + 58-entry bibliography | 2/40 |
| 3 | R0002 | fetch | http://export.arxiv.org/api/query?id_list=(32 ids) | **FAILED** HTTP 301, 0 B (plain-HTTP redirect not followed) | 3/40 |
| 4 | R0002 | fetch | https://export.arxiv.org/api/query?id_list=(32 ids) | HTTP 200, 68,733 B; 32/32 bibliography identifiers resolved with authoritative metadata | 4/40 |
| 5 | R0003 | search | arXiv API Q01: cat:hep-lat AND ("normalizing flow" OR "trivializing map" OR "neural sampler" OR "machine learning sampler") | HTTP 200; 84 total matches, 60 returned; seed 2606.13790 recovered by this independent route | 5/40 |
| 6 | R0003 | search | arXiv API Q02: (cs.LG OR stat.ML OR stat.CO) AND ("Boltzmann generator" OR "annealed flow transport" OR "unnormalized target" OR "neural sampler" OR "unnormalized densities") | HTTP 200; 184 total, 60 returned | 6/40 |
| 7 | R0003 | search | arXiv API Q03: ("Jarzynski equality" OR "independence Metropolis" OR "neural importance sampling" OR "annealed importance sampling" OR "asymptotically unbiased") AND ("lattice field theory" OR "normalizing flow" OR "neural sampler" OR "diffusion sampler") | HTTP 200; 32 total, 32 returned; seed recovered again | 7/40 |
| 8 | R0004 | fetch | POST api.semanticscholar.org/graph/v1/paper/batch (37 arXiv ids) | HTTP 200; 37/37 resolved with DOI, venue, citation counts — second-channel cross-validation | 8/40 |
| 9 | R0004 | fetch | api.semanticscholar.org/.../ARXIV:2606.13790/citations?fields=...,authors.name | **FAILED** HTTP 400 "Unrecognized or unsupported fields: [authors.name]" | 9/40 |
| 10 | R0004 | fetch | api.semanticscholar.org/.../ARXIV:2606.13790/citations (corrected fields) | HTTP 200; 3 citing papers (G1-forward on the seed) | 10/40 |
| 11 | R0005 | search | INSPIRE-HEP Q04: (t sampler/sampling) AND (t lattice/gauge/field theory) AND (t neural/ML/flow/diffusion/generative) | HTTP 200; 8 hits; 3 not seen on any arXiv route, incl. one grey-literature record with no eprint | 11/40 |
| 12 | R0005 | search | INSPIRE-HEP Q05: "stochastic quantization" AND (t diffusion/neural/ML/sampler/generative) | HTTP 200; 11 hits; seed cross-validated in a domain database (citation count 3, agrees with Semantic Scholar) | 12/40 |
| 13 | R0006 | search | Web search: "benchmark evaluation of neural samplers for unnormalized target distributions diffusion samplers survey arXiv" | 5 result pages + named methods (iDEM, Adjoint Sampling, SCLD, PDDS) surfaced as C0 text mentions | 13/40 |
| 14 | R0006 | fetch | https://export.arxiv.org/api/query?id_list=(31 ids) | HTTP 200; 31/31 newly surfaced identifiers resolved, incl. the 3 seed-citing papers | 14/40 |
| 15 | R0006 | search | arXiv API Q06 (title route): ti:"Iterated Denoising Energy Matching" OR ti:"Adjoint Sampling" OR ti:"Sequential Controlled Langevin Diffusions" OR ti:"Particle Denoising Diffusion Sampler" OR ti:"Liouville Flow Importance Sampler" OR ti:"Trajectory balance" OR ti:"GFlowNet Foundations" | HTTP 200; 15 returned; all 7 C0 method names promoted to verified identifiers | 15/40 |
| 16 | R0007 | fetch | https://arxiv.org/pdf/2111.15141 | HTTP 200, 2,713,763 B, 26 pages | 16/40 |
| 17 | R0007 | fetch | https://arxiv.org/pdf/2302.13834 | HTTP 200, 4,179,526 B, 30 pages | 17/40 |
| 18 | R0007 | fetch | https://arxiv.org/pdf/2307.01050 | HTTP 200, 3,598,216 B, 43 pages | 18/40 |
| 19 | R0007 | fetch | https://arxiv.org/pdf/2410.02711 | HTTP 200, 2,113,233 B, 31 pages | 19/40 |
| 20 | R0007 | fetch | https://arxiv.org/pdf/1904.12072 | HTTP 200, 884,944 B, 13 pages | 20/40 |
| 21 | R0007 | fetch | https://arxiv.org/pdf/2201.08862 | HTTP 200, 899,741 B, 32 pages | 21/40 |
| 22 | R0007 | fetch | https://arxiv.org/pdf/2309.17082 | HTTP 200, 2,486,741 B, 31 pages | 22/40 |
| 23 | R0007 | fetch | https://arxiv.org/pdf/2002.06707 | HTTP 200, 7,114,775 B, 21 pages | 23/40 |
| 24 | R0008 | fetch | api.crossref.org/works?filter=doi:(8 DOIs) | HTTP 200; 8/8 DOIs resolved to publisher, volume, year — identifier-resolver channel | 24/40 |
| 25 | R0008 | search | arXiv API Q07 (title route, adversarial/older): ti:"Aspects of scaling and scalability" OR ti:"A-NICE-MC" OR ti:"Sampling using SU(N) gauge equivariant flows" OR ti:"Nonequilibrium candidate Monte Carlo" OR ti:"Annealed Importance Sampling" OR ti:"Neural Network Renormalization Group" OR ti:"Flow-based sampling for lattice field theories" | HTTP 200; 31 returned; recovered the pre-2019 precursor layer and the scalability-critique paper | 25/40 |
| 26 | R0008 | fetch | https://scipost.org/SciPostPhys.15.6.238 | **BLOCKED** HTTP 200 but body is an anti-bot interstitial ("Making sure you're not a bot!"), 3,830 B, no record fields | 26/40 |
| 27 | R0008 | fetch | https://link.springer.com/article/10.1007/JHEP07(2022)015 | HTTP 200, 424,861 B; publisher page confirms title, Caselle, DOI and arXiv 2201.08862 — publisher channel substituted for the blocked one | 27/40 |
| 28 | R0009 | search | arXiv API Q08 (saturation probe): cat:hep-lat AND ("diffusion model" OR "score-based" OR "stochastic quantization" OR "generative model") | HTTP 200; 108 total, 50 returned; no new method family, high classical-physics noise | 28/40 |
| 29 | R0009 | fetch | api.semanticscholar.org/.../ARXIV:2410.02711/citations (limit 100) | HTTP 200; 68 citing papers, 19 from 2026 — frontier check on the closest ML ancestor | 29/40 |

**Budget used: 29 of 40. Unused: 11.** Failed/blocked calls: 3 (rows 3, 9, 26).

## R0001 — Seed identity and full text

**Date:** 2026-08-12
**Intent mode:** cover (secondary: learn)
**Round goal:** Lock the seed's identity and extract its own account of the landscape.

### Diagnosis

- Seed recall: not yet tested. Topic/author/citation coverage: zero.
- Biggest missing risk: building a landscape from model memory instead of the paper.

### Chosen Action

`locate_source` then `verify_full_text`: fetch the abstract page, then the PDF.

### Execution Result

- Identity: arXiv:2606.13790v1, *Stochastic Path Sampler For Lattice Field Theory*,
  Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou; hep-lat;
  submitted 2026-06-11; 33 pages.
- The paper positions itself explicitly against five families (normalizing flows,
  continuous flows, autoregressive networks, stochastic normalizing flows,
  data-driven GAN/diffusion models) and one ML family (path-space variational
  samplers), and names its own correction mechanism as an extended-space
  Independence Metropolis–Hastings step.
- 58-entry bibliography extracted — this became the backward-citation route.
- New EvidenceIDs: E0001–E0004.

### Next Best Action

Verify the bibliography identifiers rather than trusting the reference strings.

### Stop Decision

**Stop status:** continue.

## R0002 — Backward citation verification (G1 backward)

### Diagnosis

Bibliography entries read inside a C3 full text are `C1(bib-of-C3)`; they are
single-source and cannot be cited at that level.

### Chosen Action

`chase_backward_citations` by batching 32 physics/ML identifiers into one arXiv
API `id_list` call (the thermodynamics-philosophy references 39–48 and the
non-arXiv classics were deliberately not pursued — recorded as a scope choice).

### Execution Result

- First attempt failed on plain HTTP (301); retried on HTTPS.
- 32/32 identifiers resolved. Every seed reference in scope now has authoritative
  title/author/date, and 12 of them also carry a journal reference and DOI.
- New EvidenceIDs: E0005.

### Stop Decision

**Stop status:** continue — backward closure is good, but a bibliography-only
landscape would inherit the seed's blind spots.

## R0003 — Independent lexical routes (three facets)

### Diagnosis

Everything so far descends from the seed's own reference list. If the seed missed
a family, this run would miss it too.

### Chosen Action

`expand_query`: three arXiv lexical queries built from the query matrix, one per
facet, each with a domain lock (`cat:hep-lat`, `cat:cs.LG/stat.ML`, or an explicit
domain phrase).

### Execution Result

- 300 total matches reported across the three queries; 152 records retrieved.
- Seed recall: 2606.13790 was returned independently by Q01 and Q03 — the seed is
  reachable from the keyword routes, not only from its own identifier.
- New families found that are **not** in the seed bibliography: the Lüscher
  trivializing-map lineage (0907.5491 and descendants), Annealed Flow Transport /
  CRAFT, Flow Annealed Importance Sampling Bootstrap, mode-collapse diagnostics,
  and the flow-scalability critique literature.
- New EvidenceIDs: E0006–E0008.

### Stop Decision

**Stop status:** continue.

## R0004 — Second channel and forward citations

### Chosen Action

`verify_links` via the Semantic Scholar batch endpoint (37 core identifiers in one
call) and `chase_forward_citations` on the seed.

### Execution Result

- 37/37 resolved: every core record now has two independent channels.
- One title variant found: 2007.07115 is indexed by Semantic Scholar as
  "*On* Estimation of Thermodynamic Observables…" versus arXiv/Crossref
  "Estimation of Thermodynamic Observables…". Recorded, not silently normalized.
- Seed forward citations = 3 (2607.21436, 2607.15682, 2607.08505).
- First attempt failed (HTTP 400, invalid field name); retried successfully.
- New EvidenceIDs: E0009–E0011.

### Stop Decision

**Stop status:** continue.

## R0005 — Domain database channel (INSPIRE-HEP)

### Execution Result

- 19 hits over two queries; 3 records had not appeared on any arXiv route,
  including a grey-literature record with no eprint field (kept at C1, single
  channel, explicitly not used as evidence).
- INSPIRE independently reports the seed's citation count as 3, agreeing with
  Semantic Scholar.
- New EvidenceIDs: E0012–E0013.

### Stop Decision

**Stop status:** continue.

## R0006 — Web channel and name resolution

### Diagnosis

Method names were accumulating as bare strings inside other papers' related-work
sections (iDEM, Adjoint Sampling, SCLD, PDDS). Those are C0 mentions and must not
be asserted.

### Chosen Action

One general web search for benchmark/survey framing, then one arXiv title route
to convert every named method into a verified identifier.

### Execution Result

- All 7 named methods resolved to arXiv records; none had to be dropped as
  unverifiable, and none was asserted before resolution.
- New EvidenceIDs: E0014–E0016.

### Stop Decision

**Stop status:** continue to the source gate.

## R0007 — C3 source gate

### Chosen Action

`verify_full_text`: download 8 further core PDFs spanning all three facets.

### Execution Result

- 9 PDFs on disk (including the seed), 260 pages total, every one with a byte
  size and a page count recorded in `evidence_registry.md`.
- A specific correction/exactness sentence was located in each of the 9 texts,
  which is what promotes these records to C4.
- New EvidenceIDs: E0017–E0034.

### Stop Decision

**Stop status:** continue — one route family (publisher pages) still untouched.

## R0008 — Identifier resolver, publisher page, adversarial pass

### Execution Result

- Crossref resolved 8/8 core DOIs (publisher, volume, year).
- The adversarial title route recovered the older/negative layer the earlier
  queries had missed: Neal's Annealed Importance Sampling (physics/9803008),
  Nonequilibrium Candidate Monte Carlo (1105.2278), A-NICE-MC (1706.07561),
  Neural Network Renormalization Group (1802.02840), the SU(N) equivariant-flow
  paper that the seed cites without an eprint number (2008.05456), and the
  scalability critique (2211.07541).
- SciPost was blocked by an anti-bot interstitial. Per the blocked-channel rule
  the attempt was logged once, not retried three times, and the nearest
  equivalent (Crossref metadata + a Springer publisher page) was substituted.
- New EvidenceIDs: E0035–E0038.

### Stop Decision

**Stop status:** continue for one saturation round.

## R0009 — Saturation probe and frontier check

### Execution Result

- The hep-lat × diffusion/generative probe returned 108 matches, 50 retrieved:
  no new method family, and a high proportion of classical stochastic-quantization
  and complex-Langevin physics with no learned sampler. This is the second
  consecutive round adding no new family.
- The forward-citation check on NETS returned 68 citing papers, 19 from 2026. The
  2026 frontier is dense but stays inside families already mapped (diffusion
  samplers, Schrödinger-bridge samplers, discrete samplers, annealing/tempering).
  One record, 2607.15682, cites both NETS and the seed — a same-author bridge.
- New EvidenceIDs: E0039–E0041.

### File Patches (this round batch)

- output_manifest.md: all 16 rows moved `planned` → `on_disk`.
- candidate_pool.md, candidate_screening_table.md: generated from saved API
  responses (298 distinct records).
- evidence_registry.md: E0001–E0041.
- research_state.md, search_*.md, keyword/query CSVs, channel_coverage_plan.md,
  missing_risk_report.md, literature_matrix.md, lineage_snowball_map.md,
  coverage_stopping_report.md: written.

### Stop Decision

**Stop status:** `saturated_under_budget` — stopping at 29/40 calls with the
residual risks named in `missing_risk_report.md`. Reasons are in
`coverage_stopping_report.md`; the run is **not** claimed to be complete.
