# Keyword Ontology And Query-Matrix Protocol

Use this protocol when a literature task must turn oral clues or papers into
repeatable search terms. It prevents title-only keyword extraction, acronym
noise, and unexplained query expansion.

## Required Pipeline

```text
scope contract
-> section-aware reading
-> six-axis term extraction
-> normalization and provenance
-> query matrix
-> route execution and yield log
-> term feedback
-> saturation audit
```

## Section-Aware Reading

Read terms from distinct paper regions because they serve different purposes:

| region | extract |
|---|---|
| title and abstract | object, problem, main method, headline result |
| introduction | motivation, domain, established families |
| related work | synonyms, competing schools, representative papers |
| method | learned object, dynamics, architecture, correction mechanism |
| experiments | benchmark, observable, baseline, metric, dataset |
| limitations and conclusion | failure mode, scaling issue, future direction |
| references | historical term, author cluster, backward-citation route |

Do not accept a keyword merely because it sounds plausible. Each seed term
must have a source anchor. Search-derived terms may instead cite the query round
and paper that introduced them.

## Six-Axis Ontology

Every term belongs to one or more axes:

1. `problem`: the difficulty or decision being addressed.
2. `method`: the named algorithm, model family, or experimental approach.
3. `learned_object`: what is optimized, inferred, transported, or measured.
4. `correction_validation`: exactness, correction, diagnostic, or trust gate.
5. `domain_benchmark`: system, population, dataset, observable, or baseline.
6. `limitation_direction`: failure mode, scale boundary, or future route.

Use `templates/keyword_ledger_template.csv`. Keep the original phrase and a
canonical term. Store synonyms, acronyms, broader terms, neighbor terms,
negative meanings, source section, source anchor, and confidence.

## Normalization Rules

- Never search an acronym alone.
- Preserve exact phrases before adding synonyms.
- Separate spelling variants from conceptual neighbors.
- Keep broader terms and neighboring methods in different fields.
- Record ambiguous meanings and known noise domains.
- Allow multi-axis and multi-label terms; do not force one exclusive family.
- Do not promote an LLM-suggested term without either a source anchor or an
  explicit `hypothesis_term` status.

## Query Matrix

Build queries by crossing axes, not by dumping all terms into one string:

```text
problem x method
method x correction_validation
method x domain_benchmark
limitation_direction x alternative method
benchmark x baseline
author x method
```

Use `templates/query_matrix_template.csv`. Each lexical or semantic query must
contain:

- one exact or canonical term;
- at least one domain-lock term;
- synonyms where recall matters;
- negative terms for known ambiguity;
- the `TermID` values that generated the query.

Identifier, author, venue, backward-citation, and forward-citation routes may
omit a domain lock because their object is already constrained.

## Feedback Loop

After each round:

1. screen results;
2. extract new phrases only from retained papers;
3. add provenance and normalize them;
4. measure query yield and unique-facet gain;
5. update negative meanings from false positives;
6. generate the next matrix from the largest uncovered facet.

Use `templates/query_yield_log_template.csv`. Do not silently discard a noisy
query; preserve its result and the learned negative terms.

## Stop Gate

Stop the keyword loop only when all are true under the declared scope:

- two consecutive rounds add no new method family or decision-changing term;
- the major ontology axes have nonzero coverage;
- seed-paper recall and citation closure pass;
- residual query yield is below the declared threshold;
- remaining ambiguity and missing channels are recorded.

## Required Audit

Before final prose or graphs, run
`scripts/validate_keyword_query_graph.py` against the keyword, query, and
relation ledgers. A passing schema check does not prove scientific correctness;
it proves that provenance and relation claims are inspectable.

