# Design Provenance And External Boundaries

## Public Implementation

`play-the-toy-with-children` is a self-contained skill maintained in this
repository. It does not vendor or execute the external paper-reading projects
listed below. Its public scripts, templates, evidence contracts, graph runner,
and SPS test packet live under this repository's history.

The native single-paper module uses this repository's own sequence:

```text
identity lock -> paper map -> position -> mechanism -> evidence
-> boundary separation -> safe synthesis
```

## External Systems Evaluated Locally

The following projects were downloaded into a separate local test directory and
evaluated on the SPS paper. They are benchmarks and design inputs, not runtime
dependencies or redistributed components.

| Project | Tested commit | What was evaluated |
|---|---|---|
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | `c8b6421` | discovery, download, and text-read behavior |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | `be63716` | review and systematic-search prompts |
| [RealZYZhang/paper-reader-heilmeier](https://github.com/RealZYZhang/paper-reader-heilmeier) | `9856847` | concise paper explanation and critique structure |
| [KaguraTart/paper-to-course](https://github.com/KaguraTart/paper-to-course) | `b739c6a` | HTML, Markdown, and slide generation |
| [wentorai/research-plugins](https://github.com/wentorai/research-plugins) | `bf44b3c` | structured paper-summary prompts |
| [agentscope-ai/OpenJudge](https://github.com/agentscope-ai/OpenJudge) | `2151def` | review and bibliography verification failure behavior |
| [huggingface/skills](https://github.com/huggingface/skills) | `7039bdc` | paper retrieval from the Hugging Face surface |

`academic-research-suite` is also installed separately in the local Codex
environment. It is not included in this repository and is not required by this
skill.

## What Was Abstracted

The external trials reinforced four general workflow requirements:

- confirm and acquire the exact paper before interpretation;
- store structured, source-anchored reading records;
- separate extraction from critique;
- treat a partially failed pipeline as failed rather than emitting a
  success-looking report.

These requirements are implemented here with independent wording, schemas, and
validators integrated into the C0-C4 evidence model. External outputs may be
used as candidate notes only; they must return to the original paper before
promotion.

## Text And Code Screen

On 2026-07-13, the public skill tree was compared locally against the evaluated
external corpus and the installed academic-research suite. After case and
punctuation normalization, no exact substantive line of at least 60 characters
matched. This is a limited exact-match screen, not a legal opinion or a proof
that broad workflow ideas are unique.

## License Boundary

Each external project remains governed by its own license and attribution
requirements. No external source file should be copied into this repository
without a separate license review and preserved notices.

This repository has not yet selected a software license. Public visibility
alone does not grant reuse rights; the owner should choose a license before
describing the project as open source.
