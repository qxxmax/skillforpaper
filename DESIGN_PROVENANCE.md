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

## Licenses

Each external project remains governed by its own license and attribution
requirements. No external source file should be copied into this repository
without a separate license review and preserved notices.

This repository has not yet selected a software license. Public visibility
alone does not grant reuse rights; the owner should choose a license before
describing the project as open source.
