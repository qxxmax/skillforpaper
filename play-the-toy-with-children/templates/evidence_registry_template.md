# Evidence Registry

Every claim, screenshot, DOI, link, and full-text confirmation must be
registered here.  Final reports cite `EvidenceID`, not just `PaperID`.

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | ScreenshotRef | Quote / Extract | Verification level | Checked by | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0001 | E_DOI | metadata |  |  |  |  | C1 | automated metadata check | R0001 |  |
| E0002 | P0001 | E_SCREENSHOT | claim / table / figure / method |  | p. 5 / Figure 2 | screenshots/E0002_p5_fig2.png |  | C4 | manual source check | R0002 |  |

## Evidence Rules

- `E_LINK` confirms existence or metadata.
- `E_DOI` confirms metadata.
- `E_ABSTRACT` supports relevance only.
- `E_FULLTEXT` supports full-text availability.
- `E_SCREENSHOT` supports a specific page, table, figure, method, result, or claim.
- `E_QUOTE` supports a specific claim; keep quotes short.
- `E_METADATA_ONLY` must not be used as strong claim evidence.

## Verification Levels

| level | meaning |
|---|---|
| C0 | candidate only |
| C1 | metadata verified |
| C2 | abstract or source summary checked |
| C3 | full text checked |
| C4 | specific claim verified by page, quote, note, or screenshot |

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | P0007 | screenshot of method section | central claim not verified | user upload PDF / library access |

## Report Rule

A `PaperID` tells us which paper.  An `EvidenceID` tells us why we trust a
specific claim, figure, result, link, or metadata field.
