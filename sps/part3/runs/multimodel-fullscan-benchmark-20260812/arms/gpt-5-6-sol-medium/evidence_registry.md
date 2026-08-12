# Evidence Registry

| EvidenceID | Paper / arXiv | Type | What it verifies | Source | Section | Integrity / extract | Level | Round |
|---|---|---|---|---|---|---|---|---|
| E0001 | SPS / 2606.13790 | E_FULLTEXT | identity/full text | sources/pdfs/2606.13790.pdf | whole PDF | 2263775 bytes; pdfinfo 33 pages; pdftotext succeeded | C3 | R0004 |
| E0002 | SPS / 2606.13790 | E_QUOTE | mechanism/correction boundary | sources/text/2606.13790.txt | §2.3–2.4/App. B.3 | paired forward/backward Langevin paths; path-space KL; extended-space trajectory IMH | C4 | R0004 |
| E0003 | Albergo LFT flow / 1904.12072 | E_FULLTEXT | identity/full text | sources/pdfs/1904.12072.pdf | whole PDF | 884944 bytes; pdfinfo 13 pages; pdftotext succeeded | C3 | R0004 |
| E0004 | Albergo LFT flow / 1904.12072 | E_QUOTE | mechanism/correction boundary | sources/text/1904.12072.txt | §II.A/conclusion | reverse-KL invertible flow proposal; independence MH | C4 | R0004 |
| E0005 | PIS / 2111.15141 | E_FULLTEXT | identity/full text | sources/pdfs/2111.15141.pdf | whole PDF | 2713763 bytes; pdfinfo 26 pages; pdftotext succeeded | C3 | R0004 |
| E0006 | PIS / 2111.15141 | E_QUOTE | mechanism/correction boundary | sources/text/2111.15141.txt | §3/App. B | Schrödinger-bridge stochastic control; path-integral importance weights | C4 | R0004 |
| E0007 | Lattice SNF / 2201.08862 | E_FULLTEXT | identity/full text | sources/pdfs/2201.08862.pdf | whole PDF | 899741 bytes; pdfinfo 32 pages; pdftotext succeeded | C3 | R0004 |
| E0008 | Lattice SNF / 2201.08862 | E_QUOTE | mechanism/correction boundary | sources/text/2201.08862.txt | nonequilibrium derivation/MH discussion | flow layers plus stochastic updates; Jarzynski work reweighting; optional MH | C4 | R0004 |
| E0009 | DDS / 2302.13834 | E_FULLTEXT | identity/full text | sources/pdfs/2302.13834.pdf | whole PDF | 4179526 bytes; pdfinfo 30 pages; pdftotext succeeded | C3 | R0004 |
| E0010 | DDS / 2302.13834 | E_QUOTE | mechanism/correction boundary | sources/text/2302.13834.txt | importance identity near Eq. 11 | learned time-reversed diffusion; path importance weights; unbiased Z, approximate endpoints | C4 | R0004 |
| E0011 | CMCD / 2307.01050 | E_FULLTEXT | identity/full text | sources/pdfs/2307.01050.pdf | whole PDF | 3598216 bytes; pdfinfo 43 pages; pdftotext succeeded | C3 | R0004 |
| E0012 | CMCD / 2307.01050 | E_QUOTE | mechanism/correction boundary | sources/text/2307.01050.txt | path-measure/normalizer sections | learned forward/backward annealed diffusions; Crooks/Jarzynski path weights | C4 | R0004 |
| E0013 | Improved learned diffusions / 2307.01198 | E_FULLTEXT | identity/full text | sources/pdfs/2307.01198.pdf | whole PDF | 4392424 bytes; pdfinfo 28 pages; pdftotext succeeded | C3 | R0004 |
| E0014 | Improved learned diffusions / 2307.01198 | E_QUOTE | mechanism/correction boundary | sources/text/2307.01198.txt | §2/Eq. 27 | time-reversed path-measure losses; log-variance loss; importance-weighted estimators, not automatic exact iid endpoints | C4 | R0004 |
| E0015 | LFT diffusion as SQ / 2309.17082 | E_FULLTEXT | identity/full text | sources/pdfs/2309.17082.pdf | whole PDF | 2486741 bytes; pdfinfo 31 pages; pdftotext succeeded | C3 | R0004 |
| E0016 | LFT diffusion as SQ / 2309.17082 | E_QUOTE | mechanism/correction boundary | sources/text/2309.17082.txt | §4/MH construction | data-trained reverse Langevin score model; estimated likelihood enables asymptotically exact MH chain | C4 | R0004 |
| E0017 | SPS | E_METADATA_ONLY | title/authors/year/ID | arXiv + Semantic Scholar + INSPIRE | metadata | three-channel identity agreement | C2 | R0003 |
| E0018 | SPS references | E_METADATA_ONLY | 58 backward candidates | INSPIRE 3168332 | bibliography | bibliography-level relations | C1(bib-of-C4) | R0003 |
| E0019 | SPS forward set | E_METADATA_ONLY | 3 citing candidates | Semantic Scholar | citations | index-scoped 2026-08-12 | C1 | R0003 |
| E0020 | PIS graph | E_METADATA_ONLY | 63 references + 197 citations | Semantic Scholar | graph metadata | candidates only | C1 | R0005 |
| E0021 | LFT flow/diffusion facets | E_ABSTRACT | relevance of C2 includes | arXiv query results | abstracts | 20 flow + 9 diffusion records returned | C2 | R0005 |
| E0022 | AFT/CRAFT | E_ABSTRACT | learned flows plus SMC | arXiv exact query | abstracts | weights/resampling/MCMC | C2 | R0007 |
| E0023 | FAB | E_ABSTRACT | AIS bootstrap/reweighting | arXiv exact query | abstract | mass-covering objective; reweighted observables | C2 | R0007 |
| E0024 | NETS/LEAPS/reverse-diffusion SMC | E_ABSTRACT | path-weight correction family | official arXiv/venue pages surfaced by search | abstracts | weights/resampling correction | C2 | R0007 |
| E0025 | A-NICE-MC | E_ABSTRACT | older neural proposal with MH | NeurIPS paper/project page | method | volume preservation + MH detailed balance | C2 | R0007 |
| E0026 | Post-SPS adjacent papers | E_ABSTRACT | forward chronology | arXiv 2607.15682/2607.21436 | abstracts/full HTML | forward adjacent, not predecessor | C2 | R0007 |

C3 PDF count: **8**. C0/C1 records are not used for strong mechanism claims.
