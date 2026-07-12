# Run Parameter Log

| field | value |
|---|---|
| case | |
| arm | |
| loop id | L0 / L1 / L2 / L3 / L4 |
| start time | |
| end time | |
| wall minutes | |
| prompt tokens | |
| tool/output tokens | |
| synthesis tokens | |
| estimated total tokens | |
| tool calls | |
| searches | |
| sources queried | |
| raw hits | |
| unique candidates | |
| screened candidates | |
| included | |
| unconfirmed | |
| excluded | |
| full-text reads | |
| human labels | |
| graph nodes | |
| graph edges | |
| stop reason | coverage_stop / budget_stop / risk_stop / monitor |
| weighted compute/search cost | |

## Notes

Use exact token counts when available.  If exact token counts are not exposed,
record the estimator used and keep the estimate consistent across arms.
