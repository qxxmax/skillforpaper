# Paper Review Gate

Paper ID: `<PaperID>`

Reading record: `<relative path>`

Review status: `BLOCKED` (`BLOCKED` / `READY`)

## Entry Gate

- [ ] Identity is locked to an exact version.
- [ ] Full text was read and mapped.
- [ ] Method, equations, experiments, numbers, and limitations have anchors.
- [ ] Paper-layer statements are separated from reviewer inference.
- [ ] Missing evidence remains pending.

If any item fails, stop the review and return to the reading record.

## Validity Checks

| Check | Finding | Source anchor / reasoning | Severity | Status |
|---|---|---|---|---|
| Assumptions | `<which assumptions control validity>` | `<anchor>` | `<low / medium / high>` | `<pass / concern / pending>` |
| Baseline fairness | `<whether comparisons answer the same question>` | `<anchor>` | `<...>` | `<...>` |
| Metrics | `<whether metrics support the headline claim>` | `<anchor>` | `<...>` | `<...>` |
| Ablations / controls | `<what is isolated and what is not>` | `<anchor>` | `<...>` | `<...>` |
| Uncertainty | `<error, variance, sensitivity, or missing estimate>` | `<anchor>` | `<...>` | `<...>` |
| Reproducibility | `<data, code, parameters, seeds, environment>` | `<anchor>` | `<...>` | `<...>` |
| Cost | `<compute, data, human, or deployment cost>` | `<anchor>` | `<...>` | `<...>` |

## Claim Audit

| Claim | Supporting evidence | Counterevidence / gap | Allowed wording | Decision |
|---|---|---|---|---|
| `<claim>` | `<EvidenceIDs>` | `<gap or none>` | `<bounded wording>` | `<keep / weaken / reject / pending>` |

## Reviewer Questions

| Priority | Question | Why it matters | Evidence needed to close it |
|---|---|---|---|
| `<P0-P2>` | `<question>` | `<risk to claim>` | `<test / derivation / source>` |

## Decision

- What the paper establishes: `<bounded conclusion>`
- What remains unestablished: `<boundary>`
- Next action: `<accept as source / seek comparison / request experiment / pending>`
