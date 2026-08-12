# Coverage Stopping Report

**Date:** 2026-08-12  
**Arm:** composer-2-5-fast  
**Scan level:** full (graph_mode OFF)

## What was traversed

- **Seed recall:** arXiv:2606.13790 verified via arXiv abs, INSPIRE 3168332, Semantic Scholar API; C3 PDF read.
- **Channels:** arXiv (abs/PDF), INSPIRE, Semantic Scholar, general web search, partial Springer JHEP DOI metadata.
- **Query families:** identifier lock, lexical (method×domain, method×correction, ML path-space), one forward-citation API pull.
- **Core PDFs (C3):** 6 — seed, Albergo flow MCMC, equivariant flow, PIS, CMCD, diffusion LFT.
- **Facets with ≥1 verified representative:** F1 path-space data-free samplers; F2 flows+IMH; F3 diffusion LFT; F4 SNF (metadata); F5 correction taxonomy from C3 reads.

## What was not traversed (residual risk)

- Full **G1 backward** verification of all 58 INSPIRE references on the seed page.
- **Forward citations** of SPS beyond Semantic Scholar titles (3 papers at C0/C1).
- **Author/lab snowball** for Albergo–Rezende–Kanwar and Aarts–Zhou clusters beyond papers already hit by keywords.
- **Google Scholar** dedicated UI (only web search aggregation).
- **DDS** (2302.13834) and **Trajectory Balance** NeurIPS paper — metadata only, no C3 PDF.
- **4D QCD-scale** flow/SNF at production volumes — only 2412.00200 metadata.
- arXiv **search HTML UI** blocked (403) — possible missed recent preprints not indexed by other queries.

## Marginal yield assessment

Last queries (Q009 NeuMC, Q010 DDS) added ≤2 unique method families combined. Overlap with earlier flow/diffusion hits high. **Marginal yield below expansion threshold** under remaining 15-call budget vs cost of deep citation chase.

## Stopping decision

**STOP** — auditable partial coverage under stated scope and 40-call cap; **do not claim completeness**.

## What would reopen the search

1. User requires **verified forward-cite line** for SPS (lock P0012–P0014 IDs + PDFs).
2. **Systematic backward pass** through seed bibliography with per-ref DOI/arXiv verification.
3. **Author-network expansion** on Gert Aarts / Kai Zhou / Michael Albergo coauthor graphs.
4. Unblock arXiv search or add OpenAlex/Crossref channel for 2025–2026 preprints.
5. Target facet **F4 SNF** to C3 with dedicated PDF + JHEP/LATTICE proceedings verification.

## Honest scope statement

This arm delivers a **landscape sketch** of predecessor/adjacent learned samplers and correction mechanisms sufficient for positioning SPS, not an exhaustive systematic review.
