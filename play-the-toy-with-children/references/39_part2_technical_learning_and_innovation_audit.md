# Part 2 Technical Learning And Innovation Audit

Use this protocol after Part 1 has locked the target, sources, and literature
lineage. Part 2 turns that source set into a technical learning path.

## Boundary Between Parts

| Part | Main question | Stop condition |
|---|---|---|
| Part 1 | What exists, who did it, and what can be cited? | sources and claim limits are recorded |
| Part 2 | How does it work, what changed, and can we explain or minimally reproduce it? | the requested T0-T5 checks have supporting evidence |
| Part 3 | What new research should we design and execute? | project-specific validation is complete |

Part 2 may run a small reproduction to test understanding. Treat it as a
learning check, not a new research result.

## Entry Contract

Create `part2_learning_contract.md` before deep reading. Declare:

- target topic, method, or capability;
- source Part 1 run and graph/ledger paths;
- focal paper or method family;
- mode: `understand`, `reproduce`, `track`, or `transfer`;
- target competence level T0-T5;
- time, token, compute, and access limits;
- requested outputs: Markdown, TeX, PDF, graph, or code map;
- stop condition and unresolved-question policy.

If the target identity, full text, or relevant lineage is missing, send the
specific missing item back to Part 1.

## Lineage-First Learning Path

Reuse the checked `relation_ledger.csv`, graph nodes, and native reading
records. Build a learning path around three roles:

1. **Predecessor:** the source of an inherited object, objective, estimator,
   dynamics, architecture, or benchmark.
2. **Focal work:** the paper or method being learned.
3. **Successor:** a later work that retains, changes, tests, or rejects the
   focal contribution.

Prioritize checked `direct_citation`, `method_precedent`, `method_extension`,
and `baseline_comparison` edges. Graph scores may set the reading order; they
do not establish ancestry or novelty.

The learning order should respect prerequisites rather than publication date
alone. Record each selected node, the prerequisite it supplies, the competence
level it supports, and its relation-ledger edge or source anchor.

## Finding The Core Technical Difference

Use the following passes to identify and check the technical difference:

| Pass | Read first | Output | Evidence status |
|---|---|---|---|
| I0 identity | exact version, abstract, metadata | locked object | source confirmed |
| I1 claimed contribution | introduction contribution paragraph and overview figure | author-claimed contribution | candidate claim |
| I2 predecessor subtraction | cited predecessor method/equations and focal related work | inherited versus changed components | source-supported comparison when both sides are anchored |
| I3 mechanism comparison | focal key equations, algorithm, and implementation section | operative technical change | claim anchored |
| I4 evidence isolation | ablation, controlled baseline, diagnostic, or derivation | what evidence isolates the change | scope recorded |
| I5 successor persistence | checked later use, extension, or failure analysis | what survived or was replaced | lineage synthesis |

Compare at least these dimensions when applicable:

```text
scientific object -> objective -> state/dynamics -> estimator/correction
-> architecture -> training -> data -> benchmark -> cost -> scope
```

Write one row per dimension in `innovation_delta.csv`. Use four statement
layers:

- `author_claim`: explicitly stated by a paper;
- `source_supported_synthesis`: comparison supported by anchors from all
  compared papers;
- `reviewer_inference`: a reasoned interpretation that remains separate;
- `unresolved`: a plausible difference that lacks enough evidence.

Start with the first equation or experiment that differs from the predecessor.
Check its assumptions and limits before calling it central.

## Native Reading Integration

Every paper selected for technical comparison must pass the R0-R6 native paper
reading protocol in `38_native_paper_reading_protocol.md`.

Part 1 reading extracts reusable evidence. Part 2 adds cross-paper competence:

- align notation across papers;
- reconstruct prerequisite formulas;
- identify inherited and changed algorithm steps;
- map equations to code, configuration, and data;
- compare benchmarks under compatible setups;
- explain why a result supports or fails to support the claimed difference.

External summaries may suggest where to look. Check them against the exact
source before using them.

## T0-T5 Learning Levels

| Level | Demonstrated ability | Required evidence |
|---|---|---|
| T0 object | identify exact paper, code, version, data, and task | identity and source rows |
| T1 concept | explain problem, baseline, method, result, and boundary | anchored teach-back paragraph |
| T2 formula | define symbols, assumptions, derivation links, and estimator role | formula ledger with equation anchors |
| T3 algorithm | convert the method into ordered inputs, state, updates, outputs, and complexity | pseudocode or algorithm trace |
| T4 implementation | locate formula/algorithm counterparts in code, config, and data | `equation_code_map.csv` |
| T5 reproduction | run a minimal check and explain agreement, discrepancy, or blockage | reproduction command, environment, output, and report |

Mark levels above the requested target as `not_requested`. A summary does not
pass T4, and an unverified script run does not pass T5.

## Formula-To-Code Chain

For every core formula, retain this chain:

```text
source equation -> symbols and assumptions -> algorithm step
-> code symbol/file -> config/data -> test -> observed result -> boundary
```

Use `equation_code_map.csv`. Record unavailable official code as `unavailable`.
If code implements a different version, record both versions.

## Technical Review

After paper-layer extraction, audit the technical core across the lineage:

- novelty after predecessor comparison;
- validity of assumptions and correction/exactness claims;
- baseline and schedule fairness;
- whether metrics and observables answer the stated question;
- ablations or controls that isolate the claimed change;
- uncertainty, sensitivity, and failure modes;
- reproducibility: code, data, versions, seeds, and environment;
- training, sampling, memory, data, and human cost;
- successor evidence that confirms, narrows, or supersedes the method.

Use `review_core.md`. Reviewer inferences need linked anchors and a stated
reasoning chain. Keep them separate from author claims.

## End-To-End Loop

```text
Part 1 evidence and lineage
-> learning contract
-> prerequisite-aware lineage path
-> native R0-R6 reading
-> checked difference
-> formula-algorithm-code map
-> technical review
-> T0-T5 checks
-> teach-back and export
```

Loop rules:

- missing paper, edge, or source anchor -> targeted Part 1 search;
- missing conceptual prerequisite -> add the smallest prerequisite node;
- ambiguous technical difference -> compare predecessor and focal source again;
- failed reproduction -> record the failure and inspect version/config/data;
- new research hypothesis -> hand off to Part 3 rather than extending Part 2.

## Output Contract

Required files:

- `part2_learning_contract.md`;
- `part2_learning_report.md`;
- `innovation_delta.csv`;
- `equation_code_map.csv`;
- `review_core.md`;
- reused Part 1 evidence and relation ledgers;
- `output_manifest.md` and `artifact_refresh_manifest.md` when exports exist.

Before export, resolve every referenced `PaperID`, relation ID, `EvidenceID`,
and citation EvidenceID against the declared Part 1 ledgers. A well-formed ID
that has no source-ledger row is an error, including in a draft package.

Optional outputs:

- `lineage_learning_path.mmd`, `.png`, or `.pdf`;
- `minimal_reproduction_report.md` and code/logs;
- `part2_learning_report.tex`;
- `part2_learning_report.pdf`.

Generate Markdown and TeX from the same evidence rows. Preserve `EvidenceID`,
source anchors, statement layers, and open questions in every format. Compile
and inspect the PDF before delivery.

## Stop Conditions

Stop Part 2 when:

- every requested competence level has supporting evidence;
- every retained comparison row has source anchors or is explicitly
  marked inference/unresolved;
- formula-to-code rows are traced, unavailable, or blocked without invented
  mappings;
- reviewer-core questions are answered or carried forward explicitly;
- requested exports are current and recorded in the refresh manifest.

Passing the validator confirms package consistency, not scientific correctness.
