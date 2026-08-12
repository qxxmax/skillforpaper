# Round Log

Each round records diagnosis, action, result, file updates, and next step.

## Call Ledger

This table is the only authoritative budget counter; the budget line in
`research_state.md` mirrors it. One search query = one call, one URL fetch =
one call; retries, failed, and blocked calls count too.

**Budget cap:** 10 web calls.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed title/authors; §1 builds-on quote; full References map | 1/10 |
| 2 | R0002 | fetch | https://arxiv.org/abs/2111.15141 | PIS identity C2 (Zhang & Chen) | 2/10 |
| 3 | R0002 | fetch | https://arxiv.org/abs/2302.13834 | DDS identity C2 (Vargas, Grathwohl, Doucet) | 3/10 |
| 4 | R0002 | fetch | https://arxiv.org/abs/2307.01050 | CMCD identity C2 (Vargas et al.) | 4/10 |
| 5 | R0002 | fetch | https://arxiv.org/abs/2410.02711 | NETS identity C2 (Albergo & Vanden-Eijnden) | 5/10 |
| 6 | R0003 | fetch | https://arxiv.org/abs/2307.01198 | learned diffusions identity C2 (Richter & Berner) | 6/10 |
| 7 | R0003 | fetch | https://arxiv.org/abs/1904.12072 | Albergo LFT NF identity C2 | 7/10 |
| 8 | R0003 | fetch | https://arxiv.org/abs/2309.17082 | Wang DM-as-SQ identity C2 | 8/10 |
| 9 | R0003 | fetch | https://arxiv.org/abs/2211.01364 | Berner optimal-control identity C2 | 9/10 |
| 10 | R0003 | fetch | https://arxiv.org/abs/2207.00283 | Gerdes equivariant CNF identity C2 | 10/10 |

## R0000

**Date:** 2026-08-12  
**Intent mode:** locate (secondary: evaluate)  
**Round goal:** initialize mandatory state files before first web call.  
**Current state summary:** output_manifest + four state files on disk; seed P0000 C0 only.

### Diagnosis

- Biggest missing risk: unknown predecessor set until seed related-work is read.

### Chosen Action

**Action:** initialize files; next = fetch seed abs.

### Execution Result

- New candidates: P0000 (seed, C0)
- New EvidenceIDs: none
- Calls: 0

### Stop Decision

**Stop status:** continue  

## R0001

**Date:** 2026-08-12  
**Intent mode:** locate  
**Round goal:** lock seed identity and extract named predecessor families.  

### Diagnosis

- Seed recall: need authoritative abs/fulltext.
- Biggest missing risk: mis-attributing parents without §1 + bib.

### Chosen Action

**Action:** fetch https://arxiv.org/abs/2606.13790  
**Expected cost:** 1 call  

### Execution Result

- Seed confirmed: Stochastic Path Sampler For Lattice Field Theory; Chen, Qian, Aarts, Lucini, Zhou; arXiv:2606.13790.
- Key §1 claim: SPS is SQ-inspired adaptation of path-space variational samplers (PIS, DDS, optimal-control, CMCD, NETS).
- LFT neighbors named: NF/CNF/autoregressive; DMs including Wang et al.; Albergo flows; Gerdes CNF; SNF.
- New EvidenceIDs: E0001–E0005
- Bib-only leads kept unconfirmed: P0010–P0012
- Calls: 1/10

### File Patches

- evidence_registry.md, candidate_pool.md, research_state.md, round_log.md, output_manifest.md

### Next Best Action

**Recommended next action:** independently fetch path-space parent abs pages.  
**Stop status:** continue  

## R0002

**Date:** 2026-08-12  
**Intent mode:** locate  
**Round goal:** verify core unnormalized path-space predecessors.  

### Chosen Action

**Action:** fetch abs pages for 2111.15141, 2302.13834, 2307.01050, 2410.02711  

### Execution Result

- Confirmed P0001–P0004 with C2 identity (title, authors, arXiv ID).
- New EvidenceIDs: E0006–E0013
- Calls: 5/10

### Next Best Action

Verify remaining §1 parents (Richter/Berner; Berner/Richter/Ullrich) and key LFT learned samplers (Albergo NF; Wang DM-SQ; Gerdes CNF).  

### Stop Decision

**Stop status:** continue  

## R0003

**Date:** 2026-08-12  
**Intent mode:** locate  
**Round goal:** verify remaining named parents within budget; stop at 10.  

### Chosen Action

**Action:** fetch 2307.01198, 1904.12072, 2309.17082, 2211.01364, 2207.00283  

### Execution Result

- Confirmed P0005–P0009 with C2 identity.
- New EvidenceIDs: E0014–E0022
- Left unverified (budget): P0010 Kanwar 2003.06413, P0011 Caselle 2201.08862, P0012 Wu SNF (no arXiv in bib) — remain C0/C1(bib-of-C4)
- Calls: 10/10 (budget exhausted)

### File Patches

- All mandatory state files finalized; validator next.

### Next Best Action

**Recommended next action:** none under budget; optional future fetches for ERQ0001–ERQ0003.  
**User input needed:** none  

### Stop Decision

**Stop status:** saturated_under_budget  
**Reason:** 10/10 calls used; key path-space and LFT parents identity-verified; residual bib leads recorded as unconfirmed.  
