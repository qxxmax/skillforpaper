# Artifact Refresh Manifest

| Artifact | Refresh trigger | Build or check | Current state |
|---|---|---|---|
| Markdown report | evidence, comparison, or status change | manual source-row refresh plus validator | current draft |
| TeX report | Markdown or CSV change | `xelatex -interaction=nonstopmode part2_learning_report.tex` | two clean passes on 2026-07-16 |
| PDF report | TeX change | two XeLaTeX passes, render pages, inspect visually | 2 pages; visual QA passed on 2026-07-16 |
| Validation JSON | any required source file change | `validate_part2_learning_package.py` | PASS for DRAFT; all referenced Part 1 IDs resolve; `ready_for_use=false` |
| Lineage view | relation-ledger or selected-node change | verify every edge ID against Part 1 | current |

Last design update: 2026-07-16.
