# Part 2: Technical Learning

| Package | Status | Purpose |
|---|---|---|
| [`runs/sps-goal-mode-rerun-20260716`](runs/sps-goal-mode-rerun-20260716/README.md) | one complete end-to-end run, verified through T3 | full SPS rerun with equation-level reading, lineage comparison, PDF, and Goal usage |
| [`runs/pis-t4-t5-minimal-reproduction-20260716`](runs/pis-t4-t5-minimal-reproduction-20260716/README.md) | verified through T5 for its declared formula-level target | official PIS code mapping, fixed objective check, and SPS unavailable-code branch |
| [`sps-lineage-learning-draft-20260715`](sps-lineage-learning-draft-20260715/README.md) | historical draft | earlier package retained for comparison |

Part 2 starts from a completed Part 1 source package, reads the focal paper and
its closest predecessors, compares equations and assumptions, reconstructs the
algorithm, and records what can and cannot be claimed.

## Public completion contract

| Level | Public demonstration | Result |
|---|---|---|
| T0 object | exact paper, version, source, and repository identity | pass |
| T1 concept | anchored method and boundary explanation | pass |
| T2 formula | symbols, assumptions, and equation roles | pass |
| T3 algorithm | ordered training and correction steps | pass on SPS lineage run |
| T4 implementation | formula-to-file/function/config map | pass on official PIS code |
| T5 reproduction | command, environment, locked output, and interpretation | pass for one PIS objective calculation |

SPS v1 explicitly defers its code and data release. The SPS code branch is
therefore recorded as unavailable at the cutoff; it is not silently replaced
with guessed code. The T5 pass is deliberately narrower than a paper benchmark
reproduction.

## Invoke Part 2

```text
Use $play-the-toy-with-children for Part 2 technical learning.
Method or paper: [exact paper or verbal clue]
Mode: understand or reproduce.
Target competence: T3, T4, or T5.

Reuse the checked Part 1 sources and lineage. Read the necessary papers,
identify the inherited and changed mechanism, map formulas to algorithms and
official code, and run only the requested minimal reproduction. Return the
learning report, innovation delta, equation/code map, technical review, and
all reproduction records. Keep source statements, reviewer inference, and
unresolved questions separate.
```
