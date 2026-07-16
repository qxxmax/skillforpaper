# Artifact Refresh Manifest

| Changed input | Refresh | Check |
|---|---|---|
| paper identity or anchor | reading record, source ledger, report | reading-record validator |
| predecessor equation or decision | innovation table, review, lineage, report | Part 2 package validator |
| report text or usage row | TeX and PDF | two PDFLaTeX passes and page render |
| required file or public path | validation JSON | public-export validator |

Commands are run from the repository root:

```bash
python3 play-the-toy-with-children/scripts/validate_part2_learning_package.py \
  sps/part2/runs/sps-goal-mode-rerun-20260716 \
  --json-output sps/part2/runs/sps-goal-mode-rerun-20260716/part2_validation.json

pdflatex -interaction=nonstopmode \
  -output-directory=sps/part2/runs/sps-goal-mode-rerun-20260716 \
  sps/part2/runs/sps-goal-mode-rerun-20260716/part2_learning_report.tex
```

The final PDF is rendered to images and checked for clipping, overlap, and
unreadable tables or graph labels.
