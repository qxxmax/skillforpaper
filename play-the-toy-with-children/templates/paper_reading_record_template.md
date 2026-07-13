# Paper Reading Record

Record status: `DRAFT` (`DRAFT` / `VERIFIED` / `BLOCKED`)

## Identity Lock

| Field | Value | Evidence |
|---|---|---|
| Title | `<exact title>` | `E0001` |
| Authors | `<ordered author list>` | `E0001` |
| Version and date | `<version; YYYY-MM-DD>` | `E0001` |
| arXiv / DOI | `<identifier>` | `E0001` |
| Canonical URL | `<https://...>` | `E0001` |
| Local full text | `<relative path or unavailable>` | `E0002` |
| Pages | `<integer or pending>` | `E0002` |
| Reading level | `<C2 / C3 / C4>` | `E0002` |

## Paper Map

| Region | Purpose in the argument | Anchor | EvidenceID |
|---|---|---|---|
| `<section / appendix>` | `<what is established there>` | `<p. N, Sec. X>` | `E0003` |

## Problem and Position

| Role | Paper-layer statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | `<what problem is addressed>` | `<p. N, Sec. X>` | `E0004` |
| Existing baseline | `<what is done before this work>` | `<p. N, Sec. X>` | `E0005` |
| Gap | `<what remains insufficient>` | `<p. N, Sec. X>` | `E0006` |
| Contribution | `<what this paper adds>` | `<p. N, Sec. X>` | `E0007` |

## Mechanism

| Component or step | Definition / action | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| `<name>` | `<what it does>` | `<required condition>` | `<p. N, Sec. X>` | `E0008` |

## Equations

| Object | Exact formula or faithful notation | Symbol definitions | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| `<equation name>` | `<LaTeX>` | `<all symbols>` | `<why it matters>` | `<p. N, Eq. (X)>` | `E0009` |

## Experiments and Numbers

| Test | Setup / baseline / metric | Retained result | Uncertainty or cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| `<experiment>` | `<setup>` | `<number or qualitative result>` | `<reported value or pending>` | `<p. N, Fig./Table X>` | `E0010` |

## Boundaries

| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | `<limitation stated by the paper>` | `<p. N, Sec. X>` | `E0011` |
| Reviewer inference | `<our separate concern>` | `<linked source anchor or reasoning>` | `inference` |
| Unresolved | `<question not answered by the paper>` | `<where checked>` | `pending` |

## Safe Output

| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | `<bounded sentence that can be reused>` | `<EvidenceIDs>` |
| Prohibited sentence | `<overclaim that must not be used>` | `<missing evidence or violated boundary>` |

## Search Leads

| Lead | Why it follows from this paper | Route | Status |
|---|---|---|---|
| `<citation / author / keyword / adjacent method>` | `<reason>` | `<backward / forward / author / keyword>` | `pending` |
