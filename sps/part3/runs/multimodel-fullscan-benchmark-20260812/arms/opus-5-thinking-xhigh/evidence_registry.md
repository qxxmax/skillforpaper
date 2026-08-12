# Evidence Registry

Every identity, link, and claim used anywhere in this run is registered here.
Reports cite `EvidenceID`, not just `PaperID`.

Screenshot policy for this run: **none** (headless run). Provenance is carried by
saved raw API responses under `sources/raw/`, downloaded PDFs under
`sources/pdfs/`, and extracted text under `sources/text/` — all re-inspectable
without re-running a web call. Anchors of the form `text L<n>` refer to line `n`
of the corresponding `sources/text/<id>.txt`, produced by `pdftotext` from the
stored PDF.

## Identity And Channel Evidence

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Anchor | Verification level | RoundID |
|---|---|---|---|---|---|---|---|
| E0001 | 2606.13790 | E_LINK | Seed exists; title, 5 authors, hep-lat, submitted 2026-06-11 | https://arxiv.org/abs/2606.13790 | `sources/raw/seed_abs.html`, 42,328 B | C1 | R0001 |
| E0002 | 2606.13790 | E_ABSTRACT | Seed's own problem statement: target known up to normalization, critical slowing down, data-free | abstract on the arXiv record | abstract block of `seed_abs.html` | C2 | R0001 |
| E0003 | 2606.13790 | E_FULLTEXT | Full text available | https://arxiv.org/pdf/2606.13790v1 | `sources/pdfs/2606.13790_SPS_lattice.pdf`, 2,263,775 B, **33 pages** | C3 | R0001 |
| E0004 | 2606.13790 | E_QUOTE | Seed's own landscape map (5 physics families + 1 ML family) and its named correction step | seed full text | text L1–L60 (Introduction), 58-entry bibliography at text "References" | C4 | R0001 |
| E0005 | 32 seed references | E_DOI | 32/32 bibliography identifiers resolve to real arXiv records with matching titles | https://export.arxiv.org/api/query?id_list=… | `sources/raw/arxiv_idlist_batch1.xml`, 68,733 B | C1→C2 | R0002 |
| E0006 | route Q01 | E_LINK | hep-lat lexical route: 84 matches, 60 retrieved; **seed recovered independently** | arXiv API | `sources/raw/q_lattice_flow.xml` | C2 | R0003 |
| E0007 | route Q02 | E_LINK | ML-side lexical route: 184 matches, 60 retrieved | arXiv API | `sources/raw/q_ml_sampler.xml` | C2 | R0003 |
| E0008 | route Q03 | E_LINK | Correction/exactness route: 32 matches, 32 retrieved; seed recovered again | arXiv API | `sources/raw/q_exactness.xml` | C2 | R0003 |
| E0009 | 37 core records | E_DOI | Second-channel cross-validation: 37/37 resolved with DOI/venue/citation counts | https://api.semanticscholar.org/graph/v1/paper/batch | `sources/raw/s2_batch.json`, 22,131 B | C1 (2-channel) | R0004 |
| E0010 | 2007.07115 | E_METADATA_ONLY | Title variant across channels: Semantic Scholar "*On* Estimation of…" vs arXiv/Crossref "Estimation of…" | S2 batch response | `s2_batch.json` | C1, flagged | R0004 |
| E0011 | 2606.13790 | E_LINK | Forward citations = 3 (2607.21436, 2607.15682, 2607.08505), Semantic-Scholar-scoped as of 2026-08-12 | S2 citations endpoint | `sources/raw/s2_seed_citations.json` | C1 | R0004 |
| E0012 | INSPIRE route | E_LINK | Domain-database route returned 3 records unseen on arXiv routes, incl. one grey-literature record with no eprint | https://inspirehep.net/api/literature | `sources/raw/inspire_lattice.json` | C1 | R0005 |
| E0013 | 2606.13790 | E_LINK | Seed indexed in INSPIRE-HEP; citation count 3, agreeing with Semantic Scholar | INSPIRE-HEP | `sources/raw/inspire_sq.json` | C1 (2-channel) | R0005 |
| E0014 | web route | E_LINK | Benchmark/survey framing of the diffusion-sampler field; surfaced 4 method names as C0 mentions | web search | round_log row 13 | C0 for the names | R0006 |
| E0015 | 31 records | E_DOI | 31/31 newly surfaced identifiers resolved on arXiv | arXiv API | `sources/raw/arxiv_idlist_batch2.xml` | C2 | R0006 |
| E0016 | 7 named methods | E_DOI | iDEM 2402.06121, Adjoint Sampling 2504.11713, SCLD 2412.07081, PDDS 2402.06320, LFIS 2405.06672, Trajectory Balance 2201.13259, GFlowNet Foundations 2111.09266 — all promoted C0→C2 | arXiv API title route | `sources/raw/q_titles.xml` | C2 | R0006 |
| E0035 | 8 core DOIs | E_DOI | Crossref confirms publisher, volume, year for 8 core records | https://api.crossref.org/works | `sources/raw/crossref.json`, 10,370 B | C1 (3rd channel) | R0008 |
| E0036 | 2201.08862 | E_LINK | Publisher page confirms title, author, DOI and arXiv number | https://link.springer.com/article/10.1007/JHEP07(2022)015 | `sources/raw/springer_jhep07_2022_015.html`, 424,861 B | C1 (publisher channel) | R0008 |
| E0037 | SciPost | E_LINK | **Blocked channel**: anti-bot interstitial, no record fields returned | https://scipost.org/SciPostPhys.15.6.238 | `sources/raw/scipost_15_238.html`, 3,830 B | not evidence | R0008 |
| E0038 | 8 older records | E_DOI | Precursor layer verified: physics/9803008, 1105.2278, 1706.07561, 1802.02840, 2008.05456, 2211.07541, 2401.01297, 2208.07698 | arXiv API title route | `sources/raw/q_titles2.xml` | C2 | R0008 |
| E0039 | route Q08 | E_LINK | Saturation probe: 108 matches, 50 retrieved, no new method family | arXiv API | `sources/raw/q_lattice_diffusion.xml` | C2 | R0009 |
| E0040 | 2410.02711 | E_LINK | Frontier check: 68 citing papers, 19 from 2026, all inside mapped families | S2 citations endpoint | `sources/raw/s2_nets_citations.json` | C1 | R0009 |
| E0041 | 2607.15682 | E_LINK | Bridge node: cites both the seed and NETS; same first author as seed co-author M. Qian | S2 citations of seed and of NETS | both citation JSONs | C1 | R0009 |

## Full-Text Evidence (C3 Source Gate) With Integrity Notes

Nine PDFs, 260 pages total. Every row carries the byte size and page count read
from the stored file, plus the sentence that fixes the paper's correction or
exactness mechanism.

| EvidenceID | PaperID | Integrity note (bytes / pages) | Mechanism sentence located in the stored text | Anchor | Level |
|---|---|---|---|---|---|
| E0017 | 2606.13790 | 2,263,775 B / 33 p | "…are subsequently corrected by an extended-space Independence Metropolis–Hastings step." | text L35; §2.4 heading "Independence Metropolis–Hastings for SPS" at text L53 | C4 |
| E0018 | 2606.13790 | (same file) | "…with exactness restored by a trajectory-level Independence Metropolis–Hastings correction." | text L146 | C4 |
| E0019 | 1904.12072 | 884,944 B / 13 p | "To guarantee asymptotic exactness of sampling, a Markov chain is constructed using Metropolis-Hastings steps with p̃f taken as a proposal distribution." | text L54 | C4 |
| E0020 | 1904.12072 | (same file) | "…the known likelihood allows use of a Metropolis-Hastings acceptance step to ensure exactness." | text L89 | C4 |
| E0021 | 2002.06707 | 7,114,775 B / 21 p | "exact importance weights without having to marginalize out the randomness of the…" | text L35 | C4 |
| E0022 | 2002.06707 | (same file) | "generation of asymptotically unbiased samples from a target distribution defined up to a normalization" | text L45 | C4 |
| E0023 | 2111.15141 | 2,713,763 B / 26 p | "…is used to compute importance weights of the samples to compensate for…" | text L28 | C4 |
| E0024 | 2111.15141 | (same file) | "can generate unbiased samples over a finite time horizon." | text L73 | C4 |
| E0025 | 2302.13834 | 4,179,526 B / 30 p | "We can obtain an unbiased estimate of Z via the following importance sampling identity" | text L275 | C4 |
| E0026 | 2302.13834 | (same file) | "…can use this normalizing flow to obtain an unbiased estimate of Z using importance sampling" | text L300 | C4 |
| E0027 | 2307.01050 | 3,598,216 B / 43 p | "…we can estimate Z in π_T = π̂_T /Z_T unbiasedly via…" | text L706 | C4 |
| E0028 | 2307.01050 | (same file) | "this implies Jarzynski's equality" | text L750 | C4 |
| E0029 | 2410.02711 | 2,113,233 B / 31 p | "a variant of annealed importance sampling (AIS) based on Jarzynski's equality" | text L19 | C4 |
| E0030 | 2410.02711 | (same file) | "…is shown to be unbiased and, in addition, has a tunable diffusion coefficient…" | text L27 | C4 |
| E0031 | 2201.08862 | 899,741 B / 32 p | "…neural-network layers are combined with Monte Carlo updates, is the same that underlies out-of-equilibrium simulations based on Jarzynski's equality" | text L16 | C4 |
| E0032 | 2201.08862 | (same file) | "…based on an exact equality in nonequilibrium statistical mechanics discovered by C. Jarzynski more than 25 years ago" | text L62 | C4 |
| E0033 | 2309.17082 | 2,486,741 B / 31 p | "…which makes the algorithm not exact (as demonstrated by e.g., the finite-stepsize corrections). This can be remedied by introducing such an accept/reject step…" | text L377 | C4 |
| E0034 | 2309.17082 | (same file) | Classical Metropolis–Hastings discussed as the exactness route for the diffusion sampler | text L877 | C4 |

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | Marsh Rossney thesis (INSPIRE, no eprint) | a second channel with an identifier | grey-literature record is single-channel; cannot be cited | resolve via institutional repository or INSPIRE record page |
| ERQ0002 | 51 include-tier records at `candidate` status | second-channel confirmation | identity currently rests on the arXiv API alone | one Semantic Scholar batch call would clear most of them |
| ERQ0003 | 103 include-tier records without full text | PDF + mechanism anchor | their correction mechanism is asserted from title/abstract only, so it is stated as such | download PDFs in a follow-up round |
| ERQ0004 | 2211.12806 / 2302.08408 | version relationship | probable duplicate pair kept separate | check publisher record (EPJC) for which eprint is the published version |

## Evidence Rules Applied

- `E_METADATA_ONLY` and C0/C1 rows never support a substantive claim in this run.
- The blocked SciPost fetch (E0037) is recorded as a blocked attempt, **not** as
  access-control evidence for the record's existence.
- Claims about a paper's correction mechanism are made only for the nine C4 rows.
  For every other record the landscape files say what the title/abstract supports
  and label it as such.
