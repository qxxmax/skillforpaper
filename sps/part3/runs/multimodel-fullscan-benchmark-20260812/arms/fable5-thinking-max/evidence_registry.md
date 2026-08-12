# Evidence Registry

Every DOI, link, abstract check, full-text confirmation, and PDF integrity
note gets an `EvidenceID`. Final statements cite EvidenceID, not just PaperID.

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | Quote / Extract / Integrity note | Verification level | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0001 | E_LINK + E_ABSTRACT | seed identity: title "Stochastic Path Sampler For Lattice Field Theory"; authors Chen, Qian, Aarts, Lucini, Zhou; date 2026/06/11; hep-lat; abstract (SPS, path-space variational free energy, extended-space Independence MH, 2D phi^4 vs HMC) | https://arxiv.org/abs/2606.13790 | abs page | "we propose a novel sampler based on nonequilibrium thermodynamics, called Stochastic Path Sampler (SPS)" | C2 | R0001 | fetched call #1 |
| E0002 | P0001 | E_FULLTEXT | seed full text + reference list | https://arxiv.org/pdf/2606.13790 → sources/pdfs/2606.13790_SPS.pdf | whole PDF | integrity: 33 pages, 2,263,775 bytes; 58 references extracted | C3 | R0001 | fetched call #2 |

| E0003 | P0010, P0035, P0036, P0039, P0040 | E_METADATA_ONLY → E_LINK | hypothesized arXiv IDs confirmed against arXiv API id_list: titles+authors match seed-bib entries exactly (1809.10606, 2201.13259, 1505.05770, 1907.05600, 2106.04399) | http://export.arxiv.org/api/query?id_list=... | API response | e.g. "Solving Statistical Mechanics Using Variational Autoregressive Networks — Dian Wu, Lei Wang, Pan Zhang" | C1 (two-source) | R0003 | call 12 |
| E0004 | whole pool (63 arXiv IDs) | E_METADATA_ONLY | Semantic Scholar batch resolution: all 63 pooled arXiv IDs exist with matching titles; venues + citation counts recorded in r0003_s2_batch.json | https://api.semanticscholar.org/graph/v1/paper/batch | API response | 63/63 resolved; e.g. 1904.12072 = PRD, 282 cites | C1 cross-validated (arXiv + S2) | R0003 | call 17; note: 1812.01729 S2 record is arXiv preprint only (Science version is separate S2 record, 11 vs journal cites) |
| E0005 | P0001 → P0065, P0067, P0068 | E_METADATA_ONLY | seed has 3 citing papers in S2 as of 2026-08-12: 2607.21436, 2607.15682, 2607.08505 | S2 /paper/arXiv:2606.13790/citations | API response | 3 records | C1, single-channel (S2-scoped, dated) | R0003 | call 16 |
| E0006 | P0029 references (P0069–P0075 et al.) | E_METADATA_ONLY | PIS reference list (63 records) — mechanism-root recovery route | S2 /paper/arXiv:2111.15141/references | API response | Neal AIS, SMC samplers, A-NICE-MC, NeuTra, i-flow, Nicoli estimator present | C1 | R0003 | call 15 |
| E0007 | P0002 forward set | E_METADATA_ONLY | 100 citing records of 1904.12072 (S2-scoped, first page) — used for forward screening; long monitor tail | S2 /paper/arXiv:1904.12072/citations | API response | 100 records | C1 | R0003 | call 14 |

| E0008 | seed + hep-lat core (13 records) | E_METADATA_ONLY | INSPIRE-HEP third-channel confirmation: seed record exists (3 citations, INSPIRE-scoped, 2026-08-12); 12/13 core records resolved with venues (PRL/PRD/JHEP/CMP); 2002.06707 NOT indexed (domain-database blind spot, expected for NeurIPS-only paper) | https://inspirehep.net/api/literature | API response (r0004_inspire.json) | e.g. 0907.5491 = Commun.Math.Phys., 441 cites | C1 three-channel for hep-lat core | R0004 | calls 18–19 |
| E0009 | P0002 | E_FULLTEXT | full text on disk; first-page title/authors match | https://arxiv.org/pdf/1904.12072 → sources/pdfs/1904.12072_FlowMCMC_LFT.pdf | whole PDF | integrity: 13 pages, 884,944 bytes | C3 | R0005 | call 20 |
| E0010 | P0014 | E_FULLTEXT | full text on disk; first-page title/authors match (Wu, Koehler, Noe) | https://arxiv.org/pdf/2002.06707 → sources/pdfs/2002.06707_SNF_WuKoehlerNoe.pdf | whole PDF | integrity: 21 pages, 7,114,775 bytes | C3 | R0005 | call 21 |
| E0011 | P0015 | E_FULLTEXT | full text on disk; first-page title/authors match (Caselle, Cellini, Nada, Panero) | https://arxiv.org/pdf/2201.08862 → sources/pdfs/2201.08862_SNF_noneq_Caselle.pdf | whole PDF | integrity: 32 pages, 899,741 bytes | C3 | R0005 | call 22 |
| E0012 | P0029 | E_FULLTEXT | full text on disk; ICLR 2022 header, title/authors match | https://arxiv.org/pdf/2111.15141 → sources/pdfs/2111.15141_PIS_ZhangChen.pdf | whole PDF | integrity: 26 pages, 2,713,763 bytes | C3 | R0005 | call 23 |
| E0013 | P0030 | E_FULLTEXT | full text on disk; ICLR 2023 header, title/authors match (Vargas, Grathwohl, Doucet) | https://arxiv.org/pdf/2302.13834 → sources/pdfs/2302.13834_DDS_Vargas.pdf | whole PDF | integrity: 30 pages, 4,179,526 bytes | C3 | R0005 | call 24 |
| E0014 | P0019 | E_FULLTEXT | full text on disk; "Accepted at JHEP", title/authors match (Wang, Aarts, Zhou) | https://arxiv.org/pdf/2309.17082 → sources/pdfs/2309.17082_DiffusionSQ_Wang.pdf | whole PDF | integrity: 31 pages, 2,486,741 bytes | C3 | R0005 | call 25 |
| E0015 | P0034 | E_FULLTEXT | full text on disk; title/authors match (Albergo, Vanden-Eijnden) | https://arxiv.org/pdf/2410.02711 → sources/pdfs/2410.02711_NETS_Albergo.pdf | whole PDF | integrity: 31 pages, 2,113,233 bytes | C3 | R0005 | call 26 |

| E0016 | P0075, P0076, P0069, P0070 | E_METADATA_ONLY → E_LINK | arXiv id_list confirmation: 1910.13496 = Nicoli et al. estimator; 1711.09268 = Levy/Hoffman/Sohl-Dickstein L2HMC; physics/9803008 = Neal AIS; cond-mat/0212648 = Del Moral/Doucet SMC samplers | arXiv API id_list | API response (r0006_gapfill.json) | titles+authors match | C1 (two-source for P0069/P0070/P0075) | R0006 | call 27 |
| E0017 | adversarial pass | E_METADATA_ONLY | adversarial query "neural network"+"critical slowing down": 16 hits, no new decision-changing method family; self-learning MC review pooled (P0077); GAN-based-sampler line NOT recovered — residual gap recorded in coverage report | arXiv API | API response (r0006_gapfill.json) | — | C1 | R0006 | call 28 |

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | P0010, P0014, P0035, P0036, P0039, P0040 | independent identifier (arXiv/DOI page) | bib entries lack printed arXiv IDs; identity single-source | RESOLVED R0003 (E0003, DEDUP0001) — all six IDs confirmed |
| ERQ0002 | P0075 | arXiv ID (hypothesis: 1910.13496) | key F3 mechanism paper; S2 record lacks ArXiv field | verify via arXiv id_list in gap-fill round |
