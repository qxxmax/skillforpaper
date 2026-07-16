# SPS Part 2 Worked Draft

This example starts from the completed SPS Part 1 run and asks how the method
works, which earlier ideas it uses, and which claims survive technical review.

The SPS reading record is complete. Equation-level comparisons with P002,
P003, and P007 are not, so the innovation claim is not final.

## Read In This Order

1. `part2_learning_report.pdf`: two-page overview.
2. `part2_learning_report.md`: full technical reading.
3. `lineage_learning_path.mmd`: selected predecessor and later-work path.
4. `innovation_delta.csv`: inherited and changed components.
5. `equation_code_map.csv`: equations, algorithm steps, and code availability.
6. `review_core.md`: technical review, limits, and next reading steps.

The remaining files record the scope, tests, and validation result.

## Validate And Rebuild

From the repository root:

```bash
python3 play-the-toy-with-children/scripts/validate_part2_learning_package.py \
  sps/part2/sps-lineage-learning-draft-20260715

xelatex -interaction=nonstopmode \
  -output-directory=sps/part2/sps-lineage-learning-draft-20260715 \
  sps/part2/sps-lineage-learning-draft-20260715/part2_learning_report.tex
```

A PASS confirms that the files and source IDs agree. It does not change a draft
scientific conclusion into a verified one.
