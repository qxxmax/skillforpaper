# Native Paper Reading Protocol

Use this protocol when the user asks to read, explain, summarize, compare, or
critique a paper, or when a literature candidate is promoted from metadata to a
core source. This module is self-contained; no external paper-reading skill is
required.

## Core Rule

Reading is an evidence transformation, not a prose-generation step:

```text
identified paper -> mapped full text -> anchored mechanism and results
-> separated boundaries -> safe reusable statements
```

Do not mark a paper `read` because an abstract, external summary, or model
memory looks sufficient. If the full text is unavailable, stop at C2 and record
the access gap.

## Native Reading Passes

| Pass | Question | Required output |
|---|---|---|
| R0 identity lock | Which exact object is being read? | title, authors, version/date, DOI/arXiv, canonical URL, local file, page count |
| R1 paper map | Where does the argument live? | section map plus relevant equations, figures, tables, and appendices |
| R2 position | What problem, baseline, gap, and contribution does the paper state? | claim rows with page/section anchors |
| R3 mechanism | What objects, assumptions, equations, and steps make the method work? | symbol definitions, equation anchors, algorithm trace |
| R4 evidence | What experiments or derivations test the claims? | datasets/models, baselines, metrics, ablations, numbers, uncertainty, cost |
| R5 boundary | What is stated, inferred, missing, or unresolved? | author limitations separated from reviewer inference |
| R6 synthesis | What can be reused safely? | allowed sentence, prohibited sentence, open questions, next-search leads |

## Anchor Contract

Every retained technical claim needs both an `EvidenceID` and a source anchor.
Use the most specific available form, for example:

```text
p. 12, Sec. 4.2, Eq. (7)
p. 18, Fig. 5 caption
p. 21, Table 3, row "L=16"
Appendix B, Algorithm 1, steps 4-7
```

Identity fields may be supported by a canonical metadata page. Method,
equation, experiment, numerical, and limitation claims require the full text.
Do not convert a source URL or a shortest-path score into claim evidence.

## Extraction Before Evaluation

Keep two layers separate:

1. **Paper layer:** what the authors state, define, derive, measure, and admit.
2. **Review layer:** assumptions that may fail, missing controls, alternative
   explanations, reproducibility risk, and questions for the authors.

Complete the paper layer first. A strong critique cannot repair an incomplete
extraction, and a favorable summary cannot replace a missing source anchor.

## Required Artifacts

For one core paper, create:

- `paper_reading_record.md` from
  `templates/paper_reading_record_template.md`;
- one row in `paper_reading_ledger.csv` using
  `templates/paper_reading_ledger_template.csv`;
- `paper_review_gate.md` from `templates/paper_review_gate_template.md` when
  critique, evaluation, proposal positioning, or reviewer simulation is needed;
- corresponding entries in `evidence_registry` and the claim/gap ledgers.

For a multi-paper scan, keep one detailed record per core paper and aggregate
only the compact fields into the ledger. Do not flatten conflicting definitions
or metrics into one row.

## Promotion And Failure Rules

- `C0-C2`: identity or abstract-level material; not a completed reading.
- `C3`: full text checked and paper map completed.
- `C4`: each reused claim is tied to an anchored evidence entry.
- External summaries, reviews, or skills may suggest questions, but they remain
  candidate notes until checked against the paper.
- A failed download, parse, OCR, equation extraction, or page match is a failed
  stage. Do not emit a success-looking reading record.
- Record `pending` rather than filling missing equations, numbers, limitations,
  or costs from memory.

## Validation

Before delivery, run:

```bash
python3 scripts/validate_paper_reading_record.py paper_reading_record.md
```

The validator checks structure, identity, anchors, evidence IDs, boundary
separation, and unresolved placeholders. Passing validates the record contract,
not the scientific correctness of the interpretation.
