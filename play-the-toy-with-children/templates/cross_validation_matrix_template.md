# Cross-Validation Matrix

Use this matrix for core records, green-check records, and any source that
supports a public claim.

| PaperID | Claim / metadata item | Source 1 | Source 2 | Source 3 | Agreement | Verification level | EvidenceIDs | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| P0001 | title/authors/year | DOI page | OpenAlex | publisher page | yes / no / partial | C1 | E0001, E0002 | verified / access_limited / recheck |  |
| P0001 | method claim | PDF p. X | screenshot | quote | yes / no / partial | C4 | E0003 | verified / recheck |  |

## Status Rules

- `verified`: independent sources agree or a primary source directly verifies.
- `access_limited`: source exists but page/PDF access is blocked; use metadata
  confirmation only.
- `recheck`: evidence is too weak or conflicting for public claims.
- `metadata_only`: record can remain in candidate pool but cannot support a
  substantive conclusion.

## Conflicts

| ConflictID | PaperID | Conflict | Sources involved | Resolution / next action |
|---|---|---|---|---|
| CV001 |  |  |  |  |
