# Missing Risk Report

What this run could have missed, stated concretely enough to be acted on.

## Database And Index Gaps

| gap | why it matters | likely size of the blind spot | how to close |
|---|---|---|---|
| No Google Scholar, OpenAlex, Web of Science, Scopus, or NASA ADS | Every discovery route here is arXiv-centric. A record with no arXiv eprint is almost invisible to this run — the one such record found (a thesis-type INSPIRE entry) appeared only because INSPIRE was queried | Unknown, and *not* estimable from this run's data. Journal-only publications, book chapters, and non-arXiv proceedings are systematically under-represented | 1–2 calls on OpenAlex with the same three facets; measure index overlap against the 298 records |
| INSPIRE queries used title-field matching | Returned only 8 and 11 hits. A full-text or abstract INSPIRE search would return far more | Moderate for hep-lat records whose titles avoid the query words | one INSPIRE abstract-scoped query |
| arXiv result sets truncated | Q02 matched 184 records but 60 were retrieved; Q12 matched 108, retrieved 50; Q01 matched 84, retrieved 60. About 208 matched records were never seen | Bounded and known: ≤208 records, all within already-mapped facets | paginate Q02 and Q12 with `start=60` |
| No dedicated grey-literature channel | Theses, technical reports, and code repositories can carry negative results and implementation detail | Moderate | targeted repository/thesis search |

## Citation-Graph Gaps

- Forward expansion covered **2 nodes** (the seed and NETS). The high-citation
  hubs 2111.15141 (197 citations), 1904.12072 (282), 2003.06413 (219) and
  2002.06707 (225) were **not** expanded forward. A 2025–26 method that cites PIS
  or the Albergo line but neither the seed nor NETS would be missed.
- No co-citation or bibliographic-coupling pass (G2) was run at all. These are the
  routes that typically surface neighbouring methods with disjoint vocabulary.
- 26 of the seed's 58 references were deliberately not verified (context
  references and non-arXiv classics; itemized in `channel_coverage_plan.md`). Two
  of them are method-relevant NeurIPS/PMLR entries — Rezende & Mohamed (2015),
  Chen et al. neural ODEs (2018) — which therefore appear in this run **only** as
  `C1(bib-of-C4)` bibliography strings and are correspondingly absent from the
  candidate pool.

## Evidence-Depth Gaps

- **103 of 112 include records were never opened.** Their method family is verified
  from the arXiv abstract, but the correction-mechanism description in
  `literature_matrix.md` is abstract-level for all of them and is labeled as such.
  The taxonomy in F3 is therefore anchored at full-text level on 9 papers.
- **51 of 112 include records rest on a single channel** (the arXiv API). They are
  status `candidate`, not `confirmed`, and are excluded from claim use. One
  Semantic Scholar batch call would clear most of them (ERQ0002).
- The probable duplicate pair 2211.12806 / 2302.08408 was not resolved against a
  publisher record (ERQ0004), so the count of distinct "learning trivializing
  flows" contributions may be off by one.

## Access Gaps

- SciPost blocked by an anti-bot interstitial (ledger row 26). Substituted with
  Crossref + a Springer page; SciPost-published records therefore lack a rendered
  venue-page confirmation.
- No paywalled-publisher access was attempted beyond these two; APS, Elsevier and
  IOP pages were never fetched.

## Language, Geography, Recency

- **English only.** No non-English channel was searched. Relevant work published
  only in Chinese, Japanese, or Russian venues would be missed entirely.
- Recency: indexes were read on 2026-08-12. The seed is 2 months old; the 2026
  frontier found via NETS citations was dense (19 papers), which suggests the
  monthly rate of new adjacent work is high enough that this snapshot will decay
  within weeks.
- Citation counts quoted anywhere in this run (seed = 3, NETS = 68) are
  channel-scoped and dated; they are not absolute.

## Topic Gaps Deliberately Accepted

- Molecular and materials Boltzmann-generator work was sent to the monitor tier
  (30 records) rather than mapped. If the question shifts from "predecessors of
  SPS" to "state of neural samplers overall", that tier must be promoted.
- Discrete-state samplers (LEAPS, MDNS) are included but not read.
- The classical stochastic-thermodynamics literature that the seed cites for the
  Clausius inequality (refs 39–48) was not pursued; the seed uses it as framing,
  not as method.

## What Would Reopen This Search

1. Any claim in a downstream artifact that SPS is novel **relative to the
   trivializing-map or annealed-transport families** — those are currently
   abstract-level only.
2. A reviewer asking for the exactness proof of a specific baseline — only 9
   mechanisms are full-text verified.
3. Publication of a new same-circle follow-up; 2607.15682 already exists and was
   found at the very edge of this run.
4. Any use of these records in a systematic-review context, which would require
   the OpenAlex/Scholar channel and a G2 co-citation pass.
