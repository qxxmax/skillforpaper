# Evidence Registry

Every DOI/link/full-text confirmation gets an EvidenceID. Screenshot policy:
none (metadata + downloaded PDF only). PDF integrity note = byte size + valid
`%PDF-` header (page-count metadata unavailable in the temp download dir).

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | Integrity / Extract | Verification level | Checked by | RoundID |
|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0001 | E_FULLTEXT | seed identity + method + IMH correction | arxiv.org/abs/2606.13790, /html/2606.13790v1 | §1, §2.3, App. B.3 | "learned forward process provides independent proposals ... corrected by an extended-space Independence Metropolis–Hastings step" (Eq. 53) | C4 | manual full-text read | R0001 |
| E0002 | P0002-P0034 | E_LINK | seed reference list = backward-citation lineage | arxiv.org/html/2606.13790v1 §References | References | ~57 bib entries harvested (C1 bib-of-C4) | C1(bib-of-C4) | manual read | R0001 |
| E0003 | P0002,P0003,P0005,P0006,P0007,P0008,P0010,P0012,P0019,P0020,P0024,P0025 | E_METADATA_ONLY | year/venue/DOI cross-validation | api.semanticscholar.org/graph/v1/paper/batch | — | 12/12 records returned, venue+DOI consistent with seed bib | C2 | S2 Graph API | R0002 |
| E0004 | P0003 | E_DOI | independent physics-index confirmation | inspirehep.net/api/literature?q=arxiv:2003.06413 | — | PRL 125, 121601 (2020); DOI 10.1103/PhysRevLett.125.121601 | C2 | INSPIRE-HEP | R0002 |
| E0005 | P0002 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/1904.12072 | whole | 884,944 B, %PDF- header | C3 | curl download | R0003 |
| E0006 | P0019 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/2111.15141 | whole | 2,713,763 B, %PDF- header | C3 | curl download | R0003 |
| E0007 | P0020 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/2302.13834 | whole | 4,179,526 B, %PDF- header | C3 | curl download | R0003 |
| E0008 | P0010 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/2201.08862 | whole | 899,741 B, %PDF- header | C3 | curl download | R0003 |
| E0009 | P0012 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/2309.17082 | whole | 2,486,741 B, %PDF- header | C3 | curl download | R0003 |
| E0010 | P0007 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/2007.07115 | whole | 618,576 B, %PDF- header | C3 | curl download | R0003 |
| E0011 | P0024 | E_FULLTEXT | full-text PDF acquired | arxiv.org/pdf/2410.02711 | whole | 2,113,233 B, %PDF- header | C3 | curl download | R0003 |
| E0012 | P0031 | E_DOI | out-of-bib adjacent family confirmed | doi.org/10.1126/science.aaw1147 ; arxiv.org/abs/1812.01729 | abstract | Science 365(6457) 2019; reweighting to Boltzmann distribution | C2 | web search (arXiv+Science+Zenodo) | R0004 |
| E0013 | P0032,P0033 | E_ABSTRACT | out-of-bib adjacent family confirmed | arxiv.org/abs/2208.01893 ; 2111.11510 | §3.1 | "augment flows with annealed importance sampling ... minimize mass-covering α-divergence" | C2 | web search + S2 | R0004 |
| E0014 | P0034 | E_ABSTRACT | out-of-bib adjacent family (arXiv unverified) | proceedings.mlr.press/v139/arbel21a | abstract | AFT = AIS/SMC + normalizing flows; PMLR v139 (2021) | C2(metadata) | web search (PMLR) | R0004 |

## Evidence Rules

- `E_METADATA_ONLY` (E0003) supports identity/venue only, not full-text claims.
- C1(bib-of-C4) entries (E0002) are trusted as citation context but need an
  independent index to reach C2 (cross-validation rule, reference 34).
- Screenshots: none captured (policy = none).

## Verification Levels

| level | meaning |
|---|---|
| C0 | candidate only |
| C1 | metadata verified (single source; bib-of-C4 = read in seed full text) |
| C2 | abstract/metadata cross-validated by >=2 independent channels |
| C3 | full text checked (PDF on disk) |
| C4 | specific claim verified by page/quote in seed full text |

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | P0034 | arXiv id / DOI | AFT arXiv id not confirmed this run | resolve via arXiv/Crossref next round |
| ERQ0002 | P0004,P0009,P0011,P0013–P0018,P0026–P0028 | independent index | still C1 bib-of-C4 | S2/INSPIRE batch next round |
