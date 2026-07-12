# Channel Lineage And Cross-Validation Gate

Use this gate for `cover` mode and any literature workflow where the user asks
whether the search is broad enough, whether links exist, whether citation
expansion has gone far enough, or whether the evidence is auditable.

The goal is not to prove absolute completeness.  The goal is to define a
channel lineage, search required channels, cross-validate records, run
N-generation graph expansion, deduplicate, and report residual missing risk.

## Contents

1. Channel lineage
2. Required channel families
3. Cross-validation rules
4. N-generation graph traversal
5. Deduplication and identity rules
6. Stop judgment
7. Required artifacts

## Channel Lineage

Before expansion, define the source-channel hierarchy:

| channel family | examples | role | common blind spot |
|---|---|---|---|
| bibliographic databases | Web of Science, Scopus, Dimensions, OpenAlex, Semantic Scholar | broad publication graph | metadata gaps, indexing lag, paywalled context |
| domain databases | PubMed, arXiv, INSPIRE, ACM DL, IEEE Xplore, ACL Anthology, ChemRxiv | field-specific precision | uneven coverage outside domain |
| publisher / venue pages | journal pages, conference proceedings, society pages | authoritative metadata and PDF links | access control, missing citation graph |
| identifier resolvers | DOI, Crossref, DataCite, PubMed, arXiv | identity confirmation | may verify existence but not relevance |
| citation tools | Google Scholar, Semantic Scholar, OpenAlex, Crossref cited-by | forward/backward expansion | noisy or incomplete citation counts |
| author / lab / grant channels | author homepages, ORCID, institution pages, grants | lineage and small-circle detection | stale personal pages |
| grey or boundary sources | theses, reports, standards, patents, registries, repositories | prior art, negative or applied evidence | harder quality assessment |
| local/user sources | uploaded PDFs, notes, slides, code, datasets | project-specific evidence | provenance must be logged |

Record which channel families are required, optional, unavailable, or out of
scope in `channel_coverage_plan.md`.

## Required Channel Families

For high-recall `cover` mode, define a must-search set before searching.  A
default scientific literature set is:

- at least one broad bibliographic graph;
- at least one domain-specific database or archive;
- DOI/Crossref or equivalent identifier verification;
- publisher/venue pages for core papers;
- backward references from seed papers;
- forward citations for seed and core papers;
- author/lab expansion for recurring groups;
- topic/keyword expansion for synonym drift;
- grey/boundary channels when novelty, prior art, or negative evidence matters.

If a required channel is inaccessible, record it as `blocked` and explain the
likely blind spot in `missing_risk_report.md`.

## Cross-Validation Rules

Do not rely on a single source for core bibliographic claims.  For confirmed
or green-check literature, prefer at least two independent confirmations:

| item to verify | minimum confirmation |
|---|---|
| paper identity | DOI/arXiv/PMID/publisher page or two metadata sources |
| title/authors/year | identifier page plus bibliographic database or publisher page |
| full-text claim | PDF/page/section/figure/table evidence, registered with `EvidenceID` |
| citation relation | citing/cited metadata plus source context when relation semantics matter |
| figure/screenshot evidence | screenshot path plus source URL/page and `EvidenceID` |
| access-limited source | resolver metadata plus secondary metadata; mark as access-limited |

A record can stay in the candidate pool with one source, but it should not be
used as strong claim evidence until the required confirmations pass.

## N-Generation Graph Traversal

For full lineage or high-recall coverage, do not stop after one query.  Traverse
the graph by generations:

| generation | expansion target | output |
|---|---|---|
| G0 | user seeds, sentinel papers, known authors, known terms | seed recall table |
| G1 backward | references of seeds and core papers | ancestor/method-foundation candidates |
| G1 forward | citing papers of seeds and core papers | descendant/application candidates |
| G2 co-citation | papers often co-cited with core records | shared knowledge-base candidates |
| G2 bibliographic coupling | papers sharing references with core records | neighboring-method candidates |
| G2 author | authors, coauthors, labs, grants, recurring venues | small-circle and lineage candidates |
| G2 topic | synonyms, topic neighbors, datasets, instruments, methods | facet-gap candidates |
| G3 bridge | papers connecting separate clusters | bridge and missing-subfield candidates |
| G4 audit | excluded, unconfirmed, blocked, and access-limited records | residual-risk evidence |

The maximum generation `N` is a budget and risk decision, not a fixed constant.
Use `N=1` for quick orientation, `N=2` for proposal/slide grounding, and `N=3`
or higher for high-recall, prior-art, systematic-review, or public audit work.

## Deduplication And Identity Rules

Deduplicate by stable identifiers first, then by normalized title/author/year:

1. DOI, PMID, arXiv, ISBN, patent number, dataset DOI, or repository release.
2. Normalized title plus first author plus year.
3. Venue, volume, pages, preprint-to-publication relationship.
4. Manual review when translated titles, conference/journal versions, or
   preprint/revision chains are ambiguous.

Do not delete duplicates silently.  Keep a duplicate group row with the kept
PaperID and reason.

## Stop Judgment

Do not stop because the model feels done.  Stop only when the selected standard
is satisfied or the remaining risk is explicitly recorded:

- Required channel families searched or marked blocked.
- Seed/sentinel recall is acceptable.
- New-generation marginal yield is low by facet, not only globally.
- Major author, topic, venue, and method clusters have been checked.
- Citation closure is adequate: backward/forward expansion returns mostly
  duplicates, out-of-scope items, or low-priority records.
- Green-check/core records have source-link and evidence registry coverage.
- Unconfirmed but important records have next actions and omission risk.
- Missing-risk report names database, access, language, recency, grey-literature,
  topic, author, and citation gaps.

The public conclusion should say the search has auditable coverage under the
current scope, not that the literature is absolutely complete.

## Required Artifacts

When this gate is active, create or update:

- `channel_coverage_plan.md` from
  `templates/channel_coverage_plan_template.md`;
- `citation_generation_log.md` from
  `templates/citation_generation_log_template.md`;
- `cross_validation_matrix.md` from
  `templates/cross_validation_matrix_template.md`;
- `candidate_pool.md`;
- `evidence_registry.md`;
- `missing_risk_report.md`;
- `source_link_verification_loop.md` when source links or screenshots matter.

For TeX/PDF/slide outputs, propagate the gate result into the report: list
searched channels, blocked channels, generation depth, cross-validation status,
and residual risks.
