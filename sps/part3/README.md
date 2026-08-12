# SPS Part 3 runs

Worked examples for **Part 3: build a toy rigorously** on the SPS case. Each
run follows the Part 3 Minimal Run Contract in
`play-the-toy-with-children/SKILL.md`: experiment contract with
pre-registered criteria before execution, a run ledger where failures are
evidence, and a claim promotion gate between "a run printed a number" and "a
conclusion".

| Run | Date | What it exercises |
|---|---|---|
| [multimodel-quickscan-benchmark-20260812](runs/multimodel-quickscan-benchmark-20260812/README.md) | 2026-08-12 | 8 models + 1 no-skill control on a matched quick-scan contract; pre-registered H1/H2; honest partial-support outcome (H2 held on auditability only, not recall) |
| [multimodel-fullscan-benchmark-20260812](runs/multimodel-fullscan-benchmark-20260812/README.md) | 2026-08-12 | E2: the same 8 models each run the **full-scan contract** (13 mandatory files, C3 gate, 40-call cap) against a frozen 20-paper ground truth; H1 PASS 8/8, H2 PASS mean recall 70%; quantifies the discovery tail below the cap |
