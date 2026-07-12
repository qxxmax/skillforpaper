# Play the Toy with Children

## 终于完成 Part 1 了

An auditable Codex research skill and one complete worked case: the Stochastic
Path Sampler (SPS) literature audit.

Public repository: <https://github.com/qxxmax/skillforpaper>

## What this repository contains

- `play-the-toy-with-children/`: the installable Codex skill.
- `sps/`: the worked SPS case, including source tables, claim ledgers,
  lineage views, validation reports, screenshots, and an audit workbook.
- `install.py`: safe cross-platform installation and update helper.
- `requirements-optional.txt`: packages needed only for graph rendering and
  API-observable token/cost runs.

Downloaded third-party papers and full-text caches are not distributed.

## Quick start: install through Codex

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

### Prepare a proposal or slides

```text
Use $play-the-toy-with-children.
First audit the literature and claims. Then turn only the verified material
into a proposal outline and a slide storyboard. Keep derivations, detailed
tables, and reviewer questions in backup.
```

## Expected outputs

The exact files depend on the intent and budget. A full `cover` run normally
produces:

| Output | Purpose |
|---|---|
| `research_state.md` | Current objective, risk, next action, and stopping state |
| `candidate_pool.md` | Discovered records before evidence promotion |
| `source_matrix.csv` | Identity, URLs, reading status, and source anchors |
| `keyword_ledger.csv` / `query_matrix.csv` | Source-derived search vocabulary and routes |
| `claim_source_ledger.md` | What can be written and which source supports it |
| `numerical_ledger.csv` | Every retained number with an original anchor |
| `relation_ledger.csv` | Checked citation, method, author, and comparison relations |
| lineage and landscape figures | Public graph views generated from reviewed relations |
| `gap_ledger.csv` | Unresolved questions and prohibited overclaims |
| `literature_research_report.md` | Bounded synthesis for writing or presentation |

The complete example and concrete file previews are under
[`sps/`](sps/README.md).

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

## License status

This repository is public, but no software license has been selected yet.
Public visibility permits reading and cloning; permission to modify,
redistribute, or create derivative works is not granted until the repository
owner adds a license. Choose a license before presenting the project as open
source.
