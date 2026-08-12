# Retrieval Backends And Citation Expansion

Use this reference when the task needs broad paper discovery, multi-database
search, forward/backward citation expansion, author or recommendation routes,
or open-access full-text acquisition. Retrieval expands the candidate pool. It
does not replace source verification, native paper reading, or claim evidence.

## Backend Roles

| backend | preferred role | credential | main blind spot |
|---|---|---|---|
| `paper-search-mcp` | concurrent multi-source discovery, deduplication, OA-first PDF retrieval | optional source-specific keys | broad metadata does not prove a claim or citation relation |
| Semantic Scholar Graph API | paper search, forward/backward citations, author graph | key recommended; some endpoints require it | one index, throttling, incomplete or delayed metadata |
| Semantic Scholar Recommendations API | semantic neighbors from positive/negative seeds | API key | recommendations are candidates, not citation edges |
| OpenAlex API | broad graph search and citation expansion | `OPENALEX_API_KEY` under the current API contract | index lag and machine-assigned fields |
| Crossref REST API | DOI identity and publisher-deposited metadata | no key; `mailto` recommended | not a complete full-text or citation-context source |
| domain archive | arXiv, PubMed/PMC, INSPIRE, Europe PMC, ACL, IEEE, or field equivalent | varies | narrow disciplinary coverage |

Do not activate every backend by default. Choose independent routes that cover
the current scope and record inaccessible routes as blocked. Maintain
`retrieval_backend_manifest.csv` from the template in `templates/`.

## Standard Sequence

```text
query matrix
-> broad lightweight search
-> normalize and deduplicate
-> screen title/abstract candidates
-> hydrate selected records
-> backward/forward/author/recommendation expansion
-> OA-first full-text acquisition for selected papers
-> original-text reading and C0-C4 evidence promotion
```

The broad-first/detail-later split controls cost. Do not download or deeply
read every metadata hit before screening.

## Runner

Use the standard-library runner when the available environment permits it:

```bash
python scripts/run_retrieval_backends.py doctor

python scripts/run_retrieval_backends.py search \
  --query "topic or exact query" \
  --backend crossref \
  --backend semantic-scholar \
  --route-id CH001 \
  --query-id Q001 \
  --round-id R0001 \
  --output-dir outputs/retrieval/R0001

python scripts/run_retrieval_backends.py expand \
  --seed DOI:10.xxxx/example \
  --backend semantic-scholar \
  --direction both \
  --route-id CH002 \
  --round-id R0002 \
  --output-dir outputs/retrieval/R0002
```

For a locally installed `paper-search` command, add
`--backend paper-search --paper-search-sources arxiv,semantic,crossref`. For
OpenAlex, set `OPENALEX_API_KEY`; never place keys in commands, logs, URLs saved
to reports, or committed files.

The runner writes:

- `raw/`: backend responses, retained for reproducibility;
- `retrieval_events.jsonl`: query, route, timing, status, hit count, and error;
- `normalized_candidates.csv`: spreadsheet-ready metadata candidates;
- `normalized_candidates.jsonl`: the same records with full structured fields;
- `dedupe_groups.csv`: exact duplicates and possible preprint/journal manifestations;
- `citation_edge_candidates.csv`: metadata-level graph edges awaiting checking;
- `retrieval_summary.json`: counts, backend status, and failures.

All retrieved records start as `candidate`, `C0`, and `metadata_only`. A DOI,
citation count, abstract, recommendation score, or API citation edge cannot by
itself promote a record to C3/C4 or `green_check`.

## Search Diversity

For `cover` mode, use at least these independent route families when relevant:

1. exact/lexical query against a broad graph;
2. domain-specific archive or database;
3. backward references from verified seeds;
4. forward citations from verified seeds;
5. recent-paper route sorted by publication date;
6. author/lab/venue route;
7. semantic-neighbor route;
8. DOI/publisher verification for promoted records.

Do not use a minimum-citation threshold as the only snowballing gate. It hides
new papers and small fields. Run impact-ranked and recency-ranked routes
separately, then fuse and screen them.

## Deduplication And Manifestations

Deduplicate exact identities in this order:

1. DOI;
2. arXiv/PMID/PMCID or another stable domain identifier;
3. source-native graph identifier;
4. normalized title plus compatible first author and year.

Do not silently collapse a preprint and journal article. When titles match but
stable identifiers differ, place them in a possible-manifestation group for
manual resolution. Preserve every source family and raw provenance file on the
canonical record.

## Citation And Recommendation Boundaries

- Forward/backward API relations may enter `citation_edge_candidates.csv`.
- Public direct-citation edges require bibliography or citation-context checks.
- Semantic recommendations are `conceptual_neighbor` candidates, never direct
  citations unless separately verified.
- Citation counts describe index metadata, not quality, support, or correctness.
- API-provided citation contexts are leads. Check the original citing paper
  before using them as claim evidence.

## Full-Text Boundary

Use open-access, publisher-authorized, repository, or user-provided copies.
Record the landing page, PDF URL, license/access status, local path, hash when
needed, and extraction result. Never bypass access controls. A failed download
is an acquisition status, not an exclusion or relevance decision.

## External Design Sources

The adapter contract was informed by these independently maintained projects:

- `openags/paper-search-mcp`: multi-source discovery and OA fallback;
- `spideryzarc/smart-semantic-scholar-mcp`: cache-aware broad/detail split,
  citation snowballing, recommendations, and author graph;
- `Zsun79/LitReviewSkill`: iterative screening, saturation, workflow logs, and
  shallow output folders;
- `JosephElvisMaman1/ResearchPilot-Skills`: normalized schemas and explicit
  OpenAlex/Crossref fallbacks.

These are optional external backends or design references. No external result
is trusted merely because a tool returned it, and no external workflow controls
the claim/evidence gates in this skill.
