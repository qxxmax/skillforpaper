# Development Sources

## Scope

`play-the-toy-with-children` is implemented in this repository. The projects
below were reviewed during development, but they are not runtime dependencies
and their source files are not included here.

The paper-reading sequence used by this skill is:

```text
identity lock -> paper map -> position -> mechanism -> evidence
-> boundary separation -> safe synthesis
```

## Projects Reviewed

The tested commit is recorded so the comparison can be repeated against the
same version.

| Project | Tested commit | What was evaluated |
|---|---|---|
| [openags/paper-search-mcp](https://github.com/openags/paper-search-mcp) | `c8b6421` | discovery, download, and text-read behavior |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | `be63716` | review and systematic-search prompts |
| [RealZYZhang/paper-reader-heilmeier](https://github.com/RealZYZhang/paper-reader-heilmeier) | `9856847` | concise paper explanation and critique structure |
| [KaguraTart/paper-to-course](https://github.com/KaguraTart/paper-to-course) | `b739c6a` | HTML, Markdown, and slide generation |
| [wentorai/research-plugins](https://github.com/wentorai/research-plugins) | `bf44b3c` | structured paper-summary prompts |
| [agentscope-ai/OpenJudge](https://github.com/agentscope-ai/OpenJudge) | `2151def` | review and bibliography verification failure behavior |
| [huggingface/skills](https://github.com/huggingface/skills) | `7039bdc` | paper retrieval from the Hugging Face surface |

## Practices Retained

The comparison led to four requirements:

- confirm and acquire the exact paper before interpretation;
- store structured, source-anchored reading records;
- separate extraction from critique;
- report a failed stage as failed.

The schemas, validators, graph runner, and SPS example in this repository were
written for this project. External output can be used as a reading lead, but a
claim is retained only after checking the original source.

## Part 3 Sources (Experiment Execution)

References 41-42, the experiment/run/claim templates, and
`validate_part3_run_package.py` were designed against these systems, reviewed
in August 2026:

| Source | What was retained |
|---|---|
| [Xcientist research harness](https://arxiv.org/abs/2606.18874) | contract-governed experiment steps: declared inputs, deliverables, and acceptance criteria before execution |
| [XScientist](https://arxiv.org/abs/2607.12301) | failed branches are kept as evidence, not deleted; they explain later fixes and narrowed conclusions |
| [AiScientist file-as-bus](https://arxiv.org/abs/2604.13018) | persistent workspace state as the backbone of long-horizon work; matches this skill's manifest-first law |
| [RepoCheck](https://github.com/WtxwNs/RepoCheck) | reproducibility checks as numbered rules (`ENV001`, `SEED001`, ...) a validator can report per rule |

Deliberately out of scope: Part 3 does not schedule or execute experiments
(that is a tracking tool's job); it governs the evidence discipline around
them.

## Part 5 Sources (Submission And Review Response)

References 43-45, the venue/submission/review templates, and
`validate_review_response.py` were designed against these practices, reviewed
in August 2026:

| Source | What was retained |
|---|---|
| [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist) and the [Main Track Handbook](https://neurips.cc/Conferences/2026/MainTrackHandbook) | checklist items are scored claims; a justified "no" beats an unsupported "yes"; every "yes" points to a section |
| [Rebuttal letter benchmark study](https://manusights.com/blog/how-to-write-rebuttal-letter-to-journal-reviewers-benchmark) | point-by-point response with verbatim quotes; respond to every point; evidence-based disagreement without heat |
| [Revision response matrix template](https://manusights.com/blog/revision-response-matrix-template) | atomic comment decomposition into a matrix; change tracking linked to reviewer rows |

The comment-class taxonomy, the diff-ledger cross-check, and the validator
contract are original to this repository.

## Part 6 Sources (Talks, Posters, QA)

References 46-47, the presentation templates, and
`validate_part6_talk_package.py` were designed against these practices,
reviewed in August 2026:

| Source | What was retained |
|---|---|
| [Assertion-evidence approach](https://www.assertion-evidence.com/) (Michael Alley, *The Craft of Scientific Presentations*, Springer) | each slide headline is one complete assertion sentence; the body is visual evidence for that assertion, not a bulleted list |
| [Trees, Maps, and Theorems](https://principiae.be/X0100.php/pdfs/TM&Th-2.0-summary.pdf) (Jean-luc Doumont) | three laws — adapt to the audience, maximize signal-to-noise, use effective redundancy; one message per slide and one core message per talk |
| [Better Poster](https://www.cos.io/blog/researcher-qa-poster-project) (Mike Morrison, OSF templates) | main finding centered in plain language; silent-presenter strip readable without the author; detail kept to an evidence panel |

The claim-level cap on slides, the figure provenance gate, and the QA bank
contract are original to this repository.

## Licenses

Each external project remains governed by its own license and attribution
requirements. No external source file should be copied into this repository
without a separate license review and preserved notices.

This repository has not yet selected a software license. Public visibility
alone does not grant reuse rights; the owner should choose a license before
describing the project as open source.
