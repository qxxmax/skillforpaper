# Play the Toy with Children

## 终于完成 Part 1 了

This project follows a six-part research roadmap. We are publishing and
validating it one part at a time. The current release is **Part 1: understand
the toy**, with one complete worked case: the Stochastic Path Sampler (SPS)
literature audit.

Public repository: <https://github.com/qxxmax/skillforpaper>

## The six-part roadmap

The toy metaphor describes a complete research lifecycle:

| Part | Toy language | Research meaning | Current status |
|---|---|---|---|
| **1** | **Understand the toy** | Turn a spoken clue into a checked literature landscape: identify the object, expand the search, read sources, trace lineages, and record evidence and gaps. | **Available and demonstrated here** |
| 2 | Learn how people use and make toys | Deep-read methods, formulas, implementations, and the latest technical progress. | Planned |
| 3 | Build a toy rigorously with the child | Design the method and experiments, run them, inspect failures, and validate the result. | Planned |
| 4 | Find support for the toy | Build and write a complete research or funding proposal. | Planned |
| 5 | Finish the toy and put it in the right toy box | Complete the paper, choose a venue, submit it, and respond to review. | Planned |
| 6 | Present the toy at different toy fairs | Produce slides, posters, and talks for different audiences and venues. | Planned |

**Scope of this release:** the installation instructions, prompts, SPS case,
output files, validation, and cost notes below all document **Part 1**. They
should not be read as evidence that Parts 2-6 are already complete or fully
tested.

## What this repository contains

- `play-the-toy-with-children/`: the installable Codex skill.
- `sps/`: the worked SPS case, including source tables, claim ledgers,
  lineage views, validation reports, screenshots, and an audit workbook.
- `install.py`: safe cross-platform installation and update helper.
- `requirements-optional.txt`: packages needed only for graph rendering and
  API-observable token/cost runs.
- [`DESIGN_PROVENANCE.md`](DESIGN_PROVENANCE.md): external systems evaluated,
  what was abstracted, and what is not included as a dependency.

Downloaded third-party papers and full-text caches are not distributed.

## Part 1 quick start: install through Codex

This is the recommended path. In Codex, send:

```text
Use the skill-installer skill to install:
https://github.com/qxxmax/skillforpaper/tree/main/play-the-toy-with-children
```

The installer places the skill under
`$CODEX_HOME/skills/play-the-toy-with-children` or, when `CODEX_HOME` is
unset, `~/.codex/skills/play-the-toy-with-children`.

After installation, send a new message or start a new Codex task:

```text
Use $play-the-toy-with-children.
Intent: cover. Budget: balanced. Screenshot policy: key-only.
Starting clue: SPS / Moxian Qian stochastic path sampler.

Confirm the target, search repeatedly through references, citations, authors,
collaborators, keywords, and adjacent methods, then return to the source text.
Produce a source matrix, claim-source ledger, lineage graph, gap ledger, and
report. Every number, date, identity, and performance claim needs a source.
Mark unresolved points as pending instead of completing the story.
```

To require an executable literature-graph pass and a controlled comparison,
add:

```text
graph_mode=on, optimizer=dijkstra.
Run the algorithm; do not only describe it. Preserve graph nodes, weighted
edges, reconstructed shortest paths, recomputed path costs, and an equal-budget
comparison against non-graph ranking. Keep source verification and gap closure.
```

## Manual installation

### macOS or Linux

```bash
git clone https://github.com/qxxmax/skillforpaper.git
cd skillforpaper
python3 install.py
python3 install.py --check
```

### Windows PowerShell

```powershell
git clone https://github.com/qxxmax/skillforpaper.git
cd skillforpaper
py install.py
py install.py --check
```

The installer refuses to overwrite an existing installation. To update an
installed copy after pulling a newer repository version:

```bash
git pull --ff-only
python3 install.py --update
python3 install.py --check
```

On Windows, replace `python3` with `py`. Updates keep the previous installed
copy under `$CODEX_HOME/skill-backups/`.

## Example requests

### Locate one paper

```text
Use $play-the-toy-with-children.
Intent: locate.
Clue: Moxian Qian's recent stochastic path sampler paper.
Confirm title, authors, version, date, arXiv/DOI, and the primary source.
```

### Build a literature family tree

```text
Use $play-the-toy-with-children.
Intent: cover. Budget: balanced.
Start from arXiv:2606.13790. Expand backward and forward, then through authors,
collaborators, source-derived keywords, adjacent methods, and negative results.
Return a checked citation lineage, method landscape, evidence ledger, and gaps.
```

### Audit what can and cannot be claimed

```text
Use $play-the-toy-with-children.
Intent: evaluate. Budget: balanced.
Check this claim against the original paper and its cited sources. Return the
supported sentence, source anchor, boundary, unresolved point, and the wording
that must not be used.
```

## Part 1 outputs

The exact files depend on the intent and budget. A full `cover` run normally
produces:

| Format | Output | Purpose |
|---|---|---|
| Markdown | `research_state.md` | Current objective, risk, next action, and stopping state |
| Markdown | `candidate_pool.md` | Discovered records before evidence promotion |
| Markdown | `round_log.md` | Search routes, decisions, and stop/continue records |
| Markdown | `claim_source_ledger.md` | What can be written and which source supports it |
| Markdown | `literature_research_report.md` | Bounded synthesis for writing or presentation |
| Markdown | `output_manifest.md` / `final_validation_report.md` | File inventory and validation state |
| CSV | `source_matrix.csv` | Identity, URLs, reading status, and source anchors |
| CSV | `manual_reading_notes.csv` | Per-paper problem, method, result, limitation, and page anchors |
| CSV | `keyword_ledger.csv` / `query_matrix.csv` | Source-derived search vocabulary and routes |
| CSV | `evidence_registry.csv` | Evidence IDs, source anchors, supported content, and status |
| CSV | `numerical_ledger.csv` | Every retained number with an original anchor |
| CSV | `relation_ledger.csv` | Checked citation, method, author, and comparison relations |
| CSV | `gap_ledger.csv` | Unresolved questions and prohibited overclaims |
| Excel | `<topic>_literature_audit.xlsx` | A reader-friendly workbook collecting the principal audit tables |
| PNG/SVG/Mermaid | lineage and landscape figures | Public graph views generated from reviewed relations |

The complete example and concrete file previews are under
[`sps/`](sps/README.md).

## Native paper reading

The skill does not require a separate third-party paper-reader. A promoted core
paper follows the repository's own protocol:

```text
identity lock -> paper map -> position -> mechanism and equations
-> experiments and numbers -> boundaries -> safe synthesis
```

The run produces a detailed `paper_reading_record.md`, a compact
`paper_reading_ledger.csv`, and, when critique is needed, a separate
`paper_review_gate.md`. The record validator rejects a `VERIFIED` file with
missing identity, source anchors, evidence IDs, or unresolved placeholders.

See
[`references/38_native_paper_reading_protocol.md`](play-the-toy-with-children/references/38_native_paper_reading_protocol.md).

## What works without an API key

| Capability | API key required? | Extra Python packages? |
|---|---|---|
| Core Codex skill workflow | No | No |
| Markdown/CSV evidence artifacts | No | No |
| Keyword/query/relation validation | No | No |
| Literature graph rendering | No | `matplotlib`, `networkx` |
| Exact Responses API token accounting | Yes | `openai` |
| Dollar-cost calculation | Yes, plus an explicit price file | `openai` |

The core workflow uses the tools and network access available to the user's
Codex environment. Database access limits and browser approvals still apply.

Install every optional package with:

```bash
python3 -m pip install -r requirements-optional.txt
```

The exact-cost runner never invents missing counters or hardcodes prices:

```bash
export OPENAI_API_KEY="..."
python3 play-the-toy-with-children/scripts/observable_research_runner.py \
  --topic "SPS / Moxian Qian stochastic path sampler" \
  --output ./runs/sps-api-observable \
  --model gpt-5.6-sol \
  --reasoning-effort xhigh
```

See
[`references/37_observable_api_runner.md`](play-the-toy-with-children/references/37_observable_api_runner.md)
before using monetary-cost results.

## Check the installation

From a cloned repository:

```bash
python3 install.py --check
python3 sps/scripts/validate_public_export.py
```

The check reports three separate states:

- **CORE**: skill structure and deterministic self-tests;
- **VISUALS**: whether `matplotlib` and `networkx` are installed;
- **API USAGE**: whether the `openai` package and `OPENAI_API_KEY` are present.

Missing optional packages do not make the core skill fail.

## SPS worked result

The root object is:

> Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, and Kai Zhou,
> *Stochastic Path Sampler For Lattice Field Theory*, arXiv:2606.13790v1,
> submitted 2026-06-11.

The recorded comparison is available at
[`sps/comparison/cost_effect_summary.md`](sps/comparison/cost_effect_summary.md).
It shows one confirmed `gpt-5.6-sol/xhigh` assignment and one Codex goal-mode
runtime. The goal-mode deployment identifier was not exposed, so this is a
workflow reproducibility comparison, not yet a strict two-model benchmark.

The executable with/without-Dijkstra comparison is available at
[`sps/comparison/dijkstra_effect_and_cost.md`](sps/comparison/dijkstra_effect_and_cost.md).
It reports the equal-budget selection effect, the complete task cost, the
deterministic graph runtime, and the costs that were not independently
measured.

## License status

This repository is public, but no software license has been selected yet.
Public visibility permits reading and cloning; permission to modify,
redistribute, or create derivative works is not granted until the repository
owner adds a license. Choose a license before presenting the project as open
source.
