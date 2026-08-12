# Evidence Registry

| EvidenceID | PaperID | Type | Verification | What it verifies | Location / note |
|---|---|---|---|---|---|
| E001 | P0001 | E_LINK | C2 | arXiv landing page exists | https://arxiv.org/abs/2606.13790 call 1 |
| E002 | P0001 | E_DOI | C2 | DOI resolves via arXiv | 10.48550/arxiv.2606.13790 call 2 |
| E003 | P0001 | E_FULLTEXT | C3 | Full PDF integrity | sources/pdfs/arxiv-2606.13790.pdf — 2263775 B, 33 pages |
| E004 | P0001 | E_QUOTE | C3 | IMH correction claim | §2.4 Independence Metropolis–Hastings; Eq. 18–19 |
| E005 | P0001 | E_QUOTE | C3 | Data-free + path KL objective | Intro §1; §2.3 Eq. 12–13 |
| E006 | P0001 | E_METADATA_ONLY | C1 | INSPIRE cross-val | inspirehep.net/literature/3168332 call 3 |
| E007 | P0002 | E_FULLTEXT | C3 | Flow+IMH baseline PDF | sources/pdfs/arxiv-1904.12072.pdf — 884944 B, 13 pages |
| E008 | P0003 | E_FULLTEXT | C3 | Equivariant flow LGT PDF | sources/pdfs/arxiv-2002.02428.pdf — 2889175 B, 16 pages |
| E009 | P0004 | E_FULLTEXT | C3 | PIS PDF | sources/pdfs/arxiv-2111.15141.pdf — 2713763 B, 26 pages |
| E010 | P0005 | E_FULLTEXT | C3 | CMCD PDF | sources/pdfs/arxiv-2307.01050.pdf — 3598216 B, 43 pages |
| E011 | P0006 | E_FULLTEXT | C3 | Diffusion LFT PDF | sources/pdfs/arxiv-2309.17082.pdf — 2486741 B, 31 pages |
| E012 | P0006 | E_DOI | C2 | Published JHEP cross-val | 10.1007/JHEP05(2024)060 via search call 8 |
| E013 | P0007 | E_ABSTRACT | C1 | DDS metadata | arXiv:2302.13834 call 25 — **no PDF downloaded** |
| E014 | P0008 | E_LINK | C1 | NeuMC package record | arXiv:2503.11482 call 22 |
| E015 | P0001 | E_METADATA_ONLY | C1 | Forward citations (titles) | Semantic Scholar API call 9 — 3 cites |
| E016 | — | E_METADATA_ONLY | C0 | arXiv search UI failure | call 23 HTTP 403 |

## Correction mechanism registry (C3-backed only)

| Mechanism | Papers (C3) | EvidenceID |
|---|---|---|
| Independence MH / extended trajectory MH | P0001, P0002 | E004, E007 |
| Importance weights (path sub-optimality) | P0004 | E009 |
| Jarzynski / Crooks / controlled path VI | P0005 | E010 |
| Optional MH after diffusion trajectory | P0006 | E011 (abstract mentions accept–reject) |
| Gauge-equivariant flow + MH | P0003 | E008 |
