# Part 2 Technical Review

Review status: `BLOCKED` (`BLOCKED` / `READY`)

## Entry Check

- [ ] Focal paper and compared predecessors are identity-locked.
- [ ] Required full texts pass the native R0-R6 reading protocol.
- [ ] Compared claims have anchors from every relevant paper.
- [ ] Relation-ledger edges used for lineage are checked.
- [ ] Author claims and reviewer inferences are separated.

## Method Comparison

| Dimension | Inherited component | Claimed change | Evidence that isolates it | Statement layer | Decision |
|---|---|---|---|---|---|
| `<objective / dynamics / estimator / architecture / training / data / benchmark / cost / scope>` | `<predecessor>` | `<focal difference>` | `<anchors / EvidenceIDs>` | `<layer>` | `<keep / weaken / reject / pending>` |

## Validity And Reproducibility

| Check | Finding | Source anchor / reasoning | Severity | Status |
|---|---|---|---|---|
| Assumptions | `<validity conditions>` | `<anchor>` | `<low / medium / high>` | `<pass / concern / pending>` |
| Correctness / exactness | `<what is proved or corrected>` | `<anchor>` | `<...>` | `<...>` |
| Baseline fairness | `<same task, schedule, budget, and estimator?>` | `<anchor>` | `<...>` | `<...>` |
| Metrics / observables | `<what the evidence measures>` | `<anchor>` | `<...>` | `<...>` |
| Ablations / controls | `<whether the difference is isolated>` | `<anchor>` | `<...>` | `<...>` |
| Uncertainty / sensitivity | `<reported or missing>` | `<anchor>` | `<...>` | `<...>` |
| Code / data / version | `<availability and match>` | `<URL / file / commit>` | `<...>` | `<...>` |
| Cost | `<training, sampling, memory, data, human cost>` | `<anchor>` | `<...>` | `<...>` |
| Successor evidence | `<retained, changed, failed, or superseded>` | `<checked relation and anchor>` | `<...>` | `<...>` |

## Core Claims

| Claim | Supporting evidence | Counterevidence / gap | Allowed wording | Decision |
|---|---|---|---|---|
| `<claim>` | `<EvidenceIDs>` | `<gap>` | `<source-supported wording>` | `<keep / weaken / reject / pending>` |

## Reading Order

| Priority | Read / derive / run | Purpose | Target | Evidence risk |
|---|---|---|---|---|
| P0 | `<exact section, equation, code, or test>` | `<reason>` | `<T0-T5>` | `<low / medium / high>` |

## Decision

- Established: `<source-supported statement>`
- Still open: `<separate inference or missing comparison>`
- Read next: `<ordered source sections or targeted Part 1 request>`
