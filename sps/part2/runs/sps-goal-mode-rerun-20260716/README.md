# SPS Part 2 Goal-Mode Run

This run uses the verified SPS Part 1 source package to answer three questions:

1. Which SPS components already appear in PIS, DDS, CMCD, and SNF?
2. What is the narrowest difference supported by the checked equations?
3. Can the corrected SPS algorithm be reconstructed through level T3?

The checked difference is the use of the full trajectory ratio in an
extended-space independence-MH correction. This is a method comparison, not a
first-ever priority claim. T0-T3 pass; code mapping and numerical reproduction
were not requested.

## Start Here

| Artifact | Contents |
|---|---|
| [`part2_learning_report.pdf`](part2_learning_report.pdf) | five-page visual report |
| [`part2_learning_report.md`](part2_learning_report.md) | full source-anchored explanation |
| [`paper_reading_ledger.csv`](paper_reading_ledger.csv) | five-paper comparison table |
| [`innovation_delta.csv`](innovation_delta.csv) | inherited, changed, inferred, and unresolved components |
| [`lineage_learning_path.mmd`](lineage_learning_path.mmd) | checked predecessor and later-citation path |
| [`review_core.md`](review_core.md) | retained, rejected, and open claims |
| [`goal_usage_summary.md`](goal_usage_summary.md) | Goal-mode token and elapsed-time accounting |

The individual `paper_reading_record_P*.md` files retain equations, benchmark
anchors, limitations, and allowed or prohibited wording for each source.

## Validate

Run from the repository root:

```bash
python3 play-the-toy-with-children/scripts/validate_part2_learning_package.py \
  sps/part2/runs/sps-goal-mode-rerun-20260716

pdflatex -interaction=nonstopmode \
  -output-directory=sps/part2/runs/sps-goal-mode-rerun-20260716 \
  sps/part2/runs/sps-goal-mode-rerun-20260716/part2_learning_report.tex
```

Downloaded papers were temporary reading inputs and are not included in this
public package.
