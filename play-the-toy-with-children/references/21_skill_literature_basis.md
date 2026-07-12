# Skill Literature Basis

Use this reference only when improving this play-the-toy-with-children skill from
literature, competing systems, or workflow papers.  Do not load it for ordinary
proposal, slides, or paper work unless the user asks how the skill itself should
evolve.

## Source Basis

Primary sources checked on 2026-06-16:

- SkillOpt: https://arxiv.org/abs/2605.23904
- SkillGen: https://arxiv.org/abs/2605.10999
- SkillOps: https://arxiv.org/abs/2605.13716
- SkillGenBench: https://arxiv.org/abs/2605.18693
- PaperOrchestra: https://arxiv.org/abs/2604.05018
- AutoResearchClaw: https://arxiv.org/abs/2605.20025
- The AI Scientist: https://arxiv.org/abs/2408.06292

Local synthesis source:

- `PROJECT_ROOT/.agents/skills/eft-paper-revision/references/source_synthesis.md`

## What To Borrow

| Work | What it contributes | Borrow for this skill | Boundary |
|---|---|---|---|
| SkillOpt | Treats a skill document as optimizable external state with bounded edits, rollout evidence, held-out gates, rejected-edit memory, and deployable best skill artifacts. | Make skill iteration bounded, evidence-based, and validation-gated. Keep rejected user feedback as design memory. | Do not claim this skill is optimized unless a held-out evaluation actually ran. |
| SkillGen | Synthesizes auditable skills from successful and failed trajectories and verifies with/without-skill intervention effects. | Use success/failure interaction logs to update rules and acceptance tests. | Do not summarize only successes; include regressions and failures. |
| SkillOps | Frames skill libraries as maintained ecosystems with contracts, compatibility, risk, and validation dimensions. | Add project manifest, claim ledger, artifact contracts, and maintenance checks. | Avoid turning every task into library maintenance. |
| SkillGenBench | Evaluates skill generation with fixed harnesses, pinned environments, and deterministic execution checks. | Add artifact acceptance tests and template validators where possible. | Our research-writing outputs often need human judgment beyond deterministic tests. |
| PaperOrchestra | Converts raw research materials into paper drafts with literature synthesis and visuals. | Keep a source map, literature matrix, figure plan, and artifact-specific rendering path. | Do not jump from raw material to polished prose without the claim/evidence ledger. |
| AutoResearchClaw | Uses iterative hypothesis, failure recovery, verifiable reporting, and human-in-the-loop intervention modes. | Make literature and proposal work looped, with checkpoint questions and risk-led continuation. | Human checkpoints are intentional, not a failure of automation. |
| The AI Scientist | Shows end-to-end idea-code-experiment-visual-paper-review loops. | Treat paper/proposal/slides as downstream artifacts of evidence and review loops. | Do not let fully autonomous writing overtake evidence boundaries. |

## Skill-Design Implications

The play-the-toy-with-children skill should not be a poster skill.  It should be a
research-to-argument system:

```text
input material
-> project manifest
-> claim/evidence ledger
-> literature loop
-> argument positioning
-> artifact-specific rendering
```

The stable core is the argument state, not the final surface.  Proposal, slides,
paper revision, cover letter, rebuttal, abstract, talk script, and poster should
all read from the same manifest, claim ledger, and literature snapshot.

## High-Priority Rules

1. Never generate polished prose before building or updating the claim/evidence
   ledger.
2. Never do literature comparison without producing a literature matrix and a
   reviewer-comparison matrix.
3. Never generate slides directly; always produce storyboard, source map, and
   speaker notes first.
4. Never accept a skill update because it sounds plausible; validate links,
   templates, and at least one realistic forward task when feasible.

## Next Skill Modules To Add

Prioritize these modules before adding more surface artifacts:

- `project_manifest_schema`: stable project identity, thesis, method family,
  correctness mechanism, limitations, target artifacts, and forbidden
  overclaims.
- `claim_evidence_ledger`: claim type, source, exact value/formula, allowed
  wording, forbidden wording, and artifact use.
- `artifact_acceptance_tests`: proposal, slides, literature, paper revision,
  cover letter, and rebuttal acceptance rules.
- `style_bank`: preferred phrases and forbidden overclaims for recurring
  technical language.

## Evaluation Questions

When updating the skill, ask:

- Does the change make future proposal/slides/paper work more evidence-bound?
- Does it reduce repeated user correction about focus, missing claims, or
  overclaiming?
- Does it preserve portability by avoiding machine-specific paths in generic
  instructions?
- Does it create a reusable artifact or only a one-off explanation?
- Can a future agent know when to stop searching, polishing, or drawing?
