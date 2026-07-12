# Source Link Completion And Verification Gate

Use this reference when a literature scan, lineage graph, proposal, slide deck,
or public workflow demonstration needs auditable source links, screenshots, or
metadata proof.

This gate prevents two common mistakes:

- a core evidence table contains papers without authoritative URLs;
- a large expanded candidate pool is confused with verified green-check
  evidence.

## Position In The Workflow

Run this gate after screening and before green-check promotion:

```text
candidate pool expansion
-> relevance screening
-> link completion
-> multi-pass source verification
-> green-check / secondary / uncertain assignment
-> graph update
-> artifact refresh
```

Do not wait until the final PDF export to discover missing links. The PDF is a
derived artifact; source-link verification is part of the evidence gate.

## Record Layers

Keep these layers separate:

| layer | example | meaning | screenshot rule |
|---|---|---|---|
| core records | `literature_records.csv` | curated lineage/evidence nodes | every row appears in the link ledger; every bibliographic green/secondary/caution row has a URL or explicit failure |
| expanded candidates | `expanded_candidate_pool.csv` | high-recall metadata pool | no screenshot required until selected for promotion |
| promoted candidates | rows copied from candidate pool into core records | evidence candidates ready for claims | URL plus verification required before green-check |
| non-bibliographic nodes | author cluster, topic boundary, search noise | graph or workflow context, not a citable paper | mark `NO_LINK_REQUIRED` with reason |

This distinction explains why a project can have 60+ core records while the
high-recall search has several hundred candidates. The hundreds are search
space, not yet verified evidence.

## Link Completion Rules

For every core record, write one of:

- authoritative `source_url`;
- `MISSING_SOURCE_URL` with `next_link_action`;
- `NO_LINK_REQUIRED` with a reason such as author cluster, topic boundary,
  search noise, or excluded non-source object.

Mandatory URL before green-check promotion:

- all `green_check` bibliographic records;
- all `secondary` bibliographic records;
- any `caution` record used as a comparison object;
- any `uncertain` publication that may be promoted.

Do not assign `green_check` to a bibliographic record whose URL is missing,
unverifiable, title-mismatched, or only an access-control page.

## Multi-Pass Verification

Use at least two independent passes for records that support public claims:

| pass | evidence | acceptable result |
|---|---|---|
| P1 direct source | publisher, arXiv, ACL Anthology, PubMed, W3C, official project page | page resolves and title/source match |
| P2 metadata | DOI/Crossref, OpenAlex, Semantic Scholar, arXiv API, ACL metadata | title, year, and identifier match |
| P3 visual evidence | screenshot or rendered metadata card | human can see what was verified |
| P4 title/facet audit | compare source title to record title and claimed facet | no title drift or scope drift |

If a site blocks headless browsing, do not call the screenshot verified. Mark it
as `ACCESS_LIMITED`, `ACCESS_CONTROL_SCREENSHOT`, or
`ACCESS_LIMITED_METADATA_VERIFIED`.

For channel-level cross-validation, also update
`cross_validation_matrix.md` from
`templates/cross_validation_matrix_template.md`.  DOI, publisher, arXiv/PMID,
OpenAlex/Semantic Scholar/Crossref, and screenshot evidence should agree before
a record supports a public claim.

## Status Labels

Use these labels in `source_link_verification.csv`:

| status | meaning |
|---|---|
| `VERIFIED` | direct URL resolved and no access-control signal was detected |
| `ACCESS_LIMITED_METADATA_VERIFIED` | primary page was blocked or gated, but authoritative metadata confirms the source |
| `ACCESS_LIMITED` | primary page appears access-limited and no secondary proof is present |
| `ACCESS_CONTROL_SCREENSHOT` | screenshot shows a blocker such as "Just a moment", Cloudflare, access denied, or human verification |
| `RECHECK_REQUIRED` | source may exist, but current evidence is too weak for public proof |
| `MISSING_SOURCE_URL` | core record has no URL and needs link completion |
| `NO_LINK_REQUIRED` | record is a topic, cluster, boundary, excluded noise, or other non-citable node |
| `UNVERIFIABLE` | attempted source could not be verified |

## Promotion Rule

A candidate may move from expanded pool to core evidence only when:

```text
title match
AND authoritative URL present
AND source-link status in {VERIFIED, ACCESS_LIMITED_METADATA_VERIFIED}
AND relevance/facet label confirmed
AND duplicate/provenance checked
```

For `green_check`, also require that the record supports a specific claim in
the claim-evidence ledger.

## Reporting Rule

The source-link report must state:

- total core records;
- core records with source URLs;
- core records missing source URLs;
- records that do not require links and why;
- screenshot count and screenshot kind;
- records needing recheck;
- expanded candidate counts by case, with a note that those rows are
  metadata-only until promoted.

When this gate changes source-link status or evidence promotion, refresh any
derived Markdown, TeX, PDF, slide, graph, dashboard, and zip artifacts through
`31_artifact_refresh_and_export_gate.md`.
