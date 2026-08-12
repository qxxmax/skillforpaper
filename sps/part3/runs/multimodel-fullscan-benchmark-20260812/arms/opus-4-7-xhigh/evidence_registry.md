# Evidence Registry

Every claim, DOI, link, full-text confirmation, or cross-channel identity check
is registered here. Final claims cite `EvidenceID`, not just `PaperID`.

## Evidence Rows

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | ScreenshotRef | Quote / Extract | Verification level | Checked by | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0001 | E_ABSTRACT | seed title + authors + abstract + full 58-ref bibliography | https://arxiv.org/abs/2606.13790 | title, abstract, references | — | Title: "Stochastic Path Sampler For Lattice Field Theory". Abstract line: "corrected by an extended-space Independence Metropolis–Hastings step." | C2 | arXiv abs fetch | R0001 | 32-page paper, 11 figures per arXiv comment |
| E0002 | P0001 | E_DOI | seed indexed in INSPIRE-HEP with 58 refs and hep-lat category | https://inspirehep.net/api/literature?q=arxiv:2606.13790 | JSON /hits/hits[0]/metadata | — | metadata.arxiv_eprints=[{value:"2606.13790",categories:["hep-lat"]}]; 58 references | C2 (cross-channel) | INSPIRE API | R0001 | authoritative cross-validation of identity + refs |
| E0003 | P0001 | E_LINK | seed indexed in OpenAlex with cited_by_count=0 | https://api.openalex.org/works/https://doi.org/10.48550/arXiv.2606.13790 | JSON top level | — | id:W7164828431, publication_year:2026, cited_by_count:0 | C2 (cross-channel) | OpenAlex API | R0004 | third distinct channel confirming seed; zero forward citations |
| E0004 | P0001 | E_LINK | INSPIRE forward-citation query returns no citing papers | https://inspirehep.net/api/literature?q=refersto:arxiv:2606.13790 | hits.total | — | total.value=1 (only seed itself via OR clause) | C2 | INSPIRE API | R0004 | consistent with OpenAlex cited_by_count=0 |
| E0005 | P0006 | E_FULLTEXT | full text of Albergo, Kanwar, Shanahan 2019 downloaded | sources/pdfs/1904.12072.pdf | — | — | header %PDF-1.5, size 884944 bytes, ~13 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0006 | P0007 | E_FULLTEXT | full text of Nicoli et al. 2021 downloaded | sources/pdfs/2007.07115.pdf | — | — | header %PDF-1.5, size 618576 bytes, ~13 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0007 | P0009 | E_FULLTEXT | full text of Kanwar et al. 2020 downloaded | sources/pdfs/2003.06413.pdf | — | — | header %PDF-1.5, size 1017965 bytes, ~6 pages | C3 | arXiv PDF fetch | R0003 | PRL-length paper; integrity note = file bytes + page objects |
| E0008 | P0020 | E_FULLTEXT | full text of Caselle et al. 2022 (SNF non-eq) downloaded | sources/pdfs/2201.08862.pdf | — | — | header %PDF-1.5, size 899741 bytes, ~32 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0009 | P0026 | E_FULLTEXT | full text of Wang, Aarts, Zhou 2024 (diffusion=SQ) downloaded | sources/pdfs/2309.17082.pdf | — | — | header %PDF-1.5, size 2486741 bytes, ~31 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0010 | P0034 | E_FULLTEXT | full text of Zhang & Chen 2022 (PIS) downloaded | sources/pdfs/2111.15141.pdf | — | — | header %PDF-1.5, size 2713763 bytes, ~26 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0011 | P0035 | E_FULLTEXT | full text of Vargas, Grathwohl, Doucet 2023 (DDS) downloaded | sources/pdfs/2302.13834.pdf | — | — | header %PDF-1.5, size 4179526 bytes, ~30 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0012 | P0039 | E_FULLTEXT | full text of Albergo & Vanden-Eijnden 2024 (NETS) downloaded | sources/pdfs/2410.02711.pdf | — | — | header %PDF-1.5, size 2113233 bytes, ~31 pages | C3 | arXiv PDF fetch | R0003 | integrity note = file bytes + page objects |
| E0013 | P0001 | E_QUOTE | seed explicitly names the ML lineage it belongs to | https://arxiv.org/abs/2606.13790 | Section 1 paragraph 4 | — | "data-free diffusion-based samplers ... including the Path Integral Sampler, Denoising Diffusion Samplers, optimal-control formulations of diffusion-based generative modeling, Controlled Monte Carlo Diffusions, which, like the present work, learn both the forward and the backward drifts, and non-equilibrium transport samplers. The present work can be viewed as a stochastic-quantization-inspired adaptation of this family of path-space variational samplers to lattice field theory, with exactness restored by a trajectory-level Independence Metropolis–Hastings correction." | C4 (page/quote) | arXiv abs quote | R0001 | anchors Facet A + Facet C explicitly to PIS/DDS/CMCD/NETS + IMH correction |
| E0014 | P0001 | E_QUOTE | seed enumerates LFT generative-model taxonomy | https://arxiv.org/abs/2606.13790 | Section 1 paragraphs 2-3 | — | "generative models adopted in lattice field theory (LFT) can be divided into two categories based on their requirements for training reference data: variational free-energy based training models and data-driven training models." | C4 | arXiv abs quote | R0001 | anchors Facet B classification (NFs + CNFs + ARNs + GAN + DMs) |
| E0015 | P0004 | E_DOI | Wu Wang Zhang 2019 VAN paper DOI resolves in INSPIRE record | INSPIRE record | — | — | dois:["10.1103/PhysRevLett.122.080602"] | C1 | INSPIRE API | R0001 | metadata from seed reference list |
| E0016 | P0060 | E_METADATA_ONLY | Importance Weighted Score Matching for Diffusion Samplers metadata via arXiv API | http://export.arxiv.org/api/query?...neural+sampler...reweighting | — | — | id: 2505.19431; title "Importance Weighted Score Matching for Diffusion Samplers with Enhanced Mode Coverage"; primary_category cs.LG; 2025-05-26 | C1 | arXiv API | R0005 | single-channel; not in seed refs; predecessor-relevant for Facet A+C |
| E0017 | P0064 | E_METADATA_ONLY | ScoreNF metadata via INSPIRE fulltext search | INSPIRE fulltext:"normalizing flow" AND hep-lat AND de>=2023 | — | — | arxiv:2510.21330 "ScoreNF: Score-Based Normalizing Flows for Sampling Unnormalized Distributions" | C1 | INSPIRE API | R0005 | single-channel; not in seed refs; directly on-topic for Facet A+B+C |
| E0018 | P0068 | E_METADATA_ONLY | flow-based topological-freezing mitigation candidate via INSPIRE fulltext | INSPIRE fulltext:"normalizing flow" AND hep-lat | — | — | arxiv:2601.20708 "A scalable flow-based approach to mitigate topological freezing" | C1 | INSPIRE API | R0005 | single-channel; direct competitor for seed's topological-freezing motivation |
| E0019 | P0001 | E_QUOTE | seed reports SPS+IMH autocorrelation vs HMC | https://arxiv.org/abs/2606.13790 | Section 3.5 (end) + Section 4 | — | "τ_{|M|,int}^{SPS+IMH} ≈ 0.5 for SPS with IMH correction and τ_{|M|,int}^{HMC} ≈ 160 for HMC" | C4 | arXiv abs quote | R0001 | this is the seed's headline claim; recorded to anchor Facet B+C evidence |

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | P0019 (Wu Köhler Noe 2020 SNF) | arXiv ID + PDF | INSPIRE record did not carry arXiv ID; only NeurIPS proceedings URL | fetch NeurIPS proceedings URL or search arXiv for "Wu Köhler Noe stochastic normalizing flows"; deferred (single call not spent given budget cap) |
| ERQ0002 | P0060–P0074 | second-channel cross-validation (each) | promotion beyond C1 requires 2nd channel | budgeted for follow-on run; each candidate needs a single arXiv abs fetch to promote to C2 (12+ calls) |
| ERQ0003 | P0001 | v2+ arXiv metadata check | seed's arXiv record was checked on 2026-08-12 (v1 dated 2026-06-11); v2 (dated 2026-08-11) referenced by author affiliation string exists but was not re-fetched | one additional /abs/2606.13790v2 fetch if a later run needs revision-level tracking |
| ERQ0004 | P0010 (Boyda SU(N) 2021) | arXiv ID | INSPIRE record had DOI but no arXiv value; publicly known ID is arXiv:2008.05456 but not confirmed within this run | 1 INSPIRE record fetch by DOI would confirm |

## Report Rule

A `PaperID` tells us which paper. An `EvidenceID` tells us why we trust a
specific claim, figure, result, link, or metadata field. In this run:

- P0001 has both C2 (three-channel identity) and C4 (specific quotes on the ML lineage claim and the tau_int headline number).
- P0006, P0007, P0009, P0020, P0026, P0034, P0035, P0039 have C3 evidence (full text on disk).
- P0002-P0059 except the above have C1 metadata (seed reference cross-validated in INSPIRE; some ML-only refs remain C1(bib-of-C2 seed)).
- P0060-P0074 are C1 metadata-only via a single coverage-search channel; they are not asserted as verified.
