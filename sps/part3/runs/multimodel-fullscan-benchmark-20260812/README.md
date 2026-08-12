# E2: Multi-Model Bounded Full-Scan Benchmark (2026-08-12)

Second Part 3 experiment on the skill itself, same day as E1
(`../multimodel-quickscan-benchmark-20260812/`). Eight models each ran the
skill's **full-scan contract** — budget contract, multi-channel routes,
keyword/query ledgers, screening funnel, C3 source gate (≥6 PDFs), coverage
stopping report — capped at 40 web calls per arm, against a ground truth of
20 verified core papers frozen in `experiment_contract.md` before launch.

Result: 8/8 arms completed the file contract with validator CONSISTENT
(H1 PASS); mean recall 14.0/20 = 70% vs the pre-registered 60% bar (H2
PASS); one core paper was found by no arm, quantifying the discovery tail
that only the unbounded original run reached. Details: `scoring_report.md`.

Read in this order: `experiment_contract.md` → `run_ledger.csv` →
`scoring_report.md` → `claim_promotion_ledger.md`. Per-arm workspaces
(including downloaded PDFs) live under `arms/`.
