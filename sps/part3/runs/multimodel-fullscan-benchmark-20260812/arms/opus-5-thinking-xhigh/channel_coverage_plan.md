# Channel Coverage Plan

Reference 34 gate. The goal is a defined channel lineage with an honest status per
family — not a completeness claim.

## Channel Families

| channel family | required? | instance used | status | calls | what it contributed |
|---|---|---|---|---|---|
| broad bibliographic graph | required | Semantic Scholar Graph API | **searched** | 3 (rows 8, 10, 29) | second-channel identity for 37 core records; forward citations for 2 nodes |
| domain-specific database / archive | required | arXiv API; INSPIRE-HEP API | **searched** | 11 arXiv + 2 INSPIRE | primary discovery engine; INSPIRE added 3 records and 1 grey-literature item |
| identifier resolver | required | Crossref | **searched** | 1 (row 24) | publisher, volume, year for 8 core DOIs |
| publisher / venue pages | required for core papers | Springer (JHEP); SciPost | **partly blocked** | 2 (rows 26, 27) | Springer confirmed 2201.08862 at publisher level; SciPost returned an anti-bot interstitial |
| backward references from seed | required | seed PDF bibliography → arXiv `id_list` | **searched** | 2 (rows 3–4) | 32/32 in-scope references verified |
| forward citations | required | Semantic Scholar citations | **searched, shallow** | 2 (rows 10, 29) | seed (3 citing) and NETS (68 citing) only |
| author / lab / grant channels | required for recurring groups | none directly | **not searched as a channel** | 0 | author lineage was reconstructed from names inside retrieved records (see `lineage_snowball_map.md`), which is weaker |
| topic / keyword expansion | required | arXiv lexical + title routes | **searched** | 6 | 4 facet queries + 2 title routes |
| grey / boundary sources | optional here | INSPIRE surfaced one thesis-type record | **incidental only** | 0 dedicated | no dedicated thesis/report/patent/repository search |
| general web | optional | web search | **searched** | 1 (row 13) | surfaced 4 method names for resolution |
| local / user sources | n/a | none provided | not applicable | 0 | — |

**Six distinct channels used** (arXiv API, Semantic Scholar, INSPIRE-HEP, Crossref,
Springer publisher page, general web search) against a requirement of three.

## Blocked Channel And Substitution

- **SciPost** (row 26): HTTP 200 with an anti-bot interstitial body
  ("Making sure you're not a bot!"), 3,830 B, no record fields.
- Per the blocked-channel rule the attempt was logged and **not** retried three
  times. Nearest-equivalent substitution: Crossref metadata (row 24, which does
  cover `10.21468/SciPostPhys.15.6.238`) plus a Springer publisher page (row 27)
  to demonstrate that the publisher channel itself is functional.
- **Resulting blind spot:** SciPost-published records have publisher-level
  confirmation only through Crossref, not through a rendered venue page. This is
  recorded in `missing_risk_report.md`.

## N-Generation Traversal Actually Performed

| generation | performed? | detail |
|---|---|---|
| G0 seeds | yes | 2606.13790 verified at C4; recovered independently by Q01, Q03 and INSPIRE |
| G1 backward | yes | 32 of the seed's 58 references verified; the 26 not pursued are the thermodynamics/information-theory context refs (39–48, 54, 57–58), the non-arXiv classics (Parisi–Wu, Damgaard–Hüffel, Roberts–Rosenthal, Girolami–Calderhead, Kullback–Leibler), and the NeurIPS/PMLR-only entries (1, 2, 3, 18, 51, 52, 53) — a deliberate, recorded scope choice, not an omission |
| G1 forward | yes, shallow | 2 nodes only (seed, NETS) |
| G2 co-citation | **no** | not attempted |
| G2 bibliographic coupling | **no** | not attempted |
| G2 author | partial | reconstructed from retrieved records, not from an author-channel query |
| G2 topic | yes | 4 lexical facet queries + 2 title routes |
| G3 bridge | partial | one bridge node identified (2607.15682, cites both the seed and NETS) |
| G4 audit | yes | all 298 records retained with status and reason; 3 failed/blocked calls logged |

Effective depth: **N = 1 with partial N = 2**, appropriate for a landscape map
under a 40-call cap, below the N = 3 that a prior-art or systematic review needs.

## Cross-Validation Status

| item | rule | status |
|---|---|---|
| paper identity | 2 independent sources | 61 of 112 includes have ≥2 channels; 51 have 1 (arXiv API only) and are labeled `candidate` |
| title / authors / year | identifier page + database or publisher | satisfied for the 37 records in the S2 batch and the 8 in Crossref |
| full-text claim | PDF page/section evidence with an EvidenceID | satisfied for 9 records (18 anchored sentences) |
| citation relation | citing/cited metadata + context | seed→3 citers and NETS→68 citers are S2-scoped counts, dated 2026-08-12; INSPIRE independently agrees on the seed's count of 3 |
| screenshot evidence | not applicable | screenshot policy `none`; raw responses stored instead |
| access-limited source | resolver + secondary metadata, marked | SciPost marked blocked, not counted as evidence |

## Public Statement This Supports

The search has **auditable coverage under the stated scope and channel set**. It
is not, and is not claimed to be, a complete map of the literature.
