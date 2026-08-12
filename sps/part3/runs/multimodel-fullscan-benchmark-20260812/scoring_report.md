# Scoring Report: E2 (multi-model bounded full-scan benchmark)

Scored 2026-08-12 20:00 UTC+2, by the orchestrator, against the ground truth
frozen in `experiment_contract.md` before launch (20 verified core papers of
the July full rerun, root excluded). Orchestrator web calls during scoring: 0.

## Headline

All 8 arms completed the full-scan file contract with validator CONSISTENT
and an honest, scope-limited stopping report. Mean recall of the frozen core
set: **14.0/20 (70%)**, above the pre-registered 60% bar. No fabricated
citations detected within the locally adjudicable scope (see M2 note).

- **H1 (portability at full scale): PASS** — 8/8 ≥ 6/8.
- **H2 (recall at scale): PASS** — mean 14.0/20 ≥ 12/20; M2 = 0 detected
  (scope-limited adjudication, see below).
- **H3 (cost): recorded** below.

## Per-Arm Results

| arm (RunID) | recall /20 | C3 PDFs | verified IDs claimed | calls /40 | wall ≈ | transcript bytes | validator | stop wording honest? |
|---|---|---|---|---|---|---|---|---|
| opus-5-thinking-xhigh (E2-R005) | **19** | 9 | 298 distinct (112 include) | 29 | 30 min | 219,864 | CONSISTENT | yes (named residual channels + singleton fraction) |
| fable5-thinking-max (E2-R002) | **18** | 8 | 75 (dual-source) | 28 | 27 min | 176,388 | CONSISTENT | yes (named gaps: GAN-for-LFT, grey lit, C1 tail) |
| grok-4-5-high-fast (E2-R007) | 16 | 7 | 34 | 33 | 9 min | 106,349 | CONSISTENT | yes |
| fable5 (E2-R001) | 15 | 9 | 63 | 24 | 24 min | 157,195 | CONSISTENT | yes |
| gpt-5-6-sol-medium (E2-R008) | 14 | 8 | 30 | 32 | 17 min | 172,573 | CONSISTENT | yes |
| opus-4-7-xhigh (E2-R003) | 12 | 8 | 47 (8 C3, 39 C1) | 17 | 16 min | 152,579 | CONSISTENT | yes (kept 23-call reserve) |
| opus-4-8-high (E2-R004) | 10 | 7 | 19 | 14 | 15 min | 101,220 | CONSISTENT | yes |
| composer-2-5-fast (E2-R006) | 8 | 6 | 11 | 25 | 5 min | 46,557 | CONSISTENT | yes |

Wall times measured from launch ≈19:27 to each completion notification
(±2 min). Transcript bytes are an observable volume proxy, not tokens
(M8 tokens: dashboard backfill pending or `unavailable`).

## Per-Paper Hit Matrix (frozen 20-ID core set)

| arXiv ID | hits /8 | missed by |
|---|---|---|
| 1904.12072 | 8/8 | — |
| 2111.15141 (PIS) | 8/8 | — |
| 2302.13834 (DDS) | 8/8 | — |
| 2309.17082 | 8/8 | — |
| 2003.06413 | 7/8 | composer |
| 2201.08862 (SNF-lattice) | 7/8 | composer |
| 2210.03139 | 7/8 | composer |
| 2211.01364 | 7/8 | composer |
| 2512.19575 | 7/8 | composer |
| 2605.11199 | 7/8 | composer |
| 2101.08176 | 6/8 | opus-4-7, opus-4-8 |
| 2302.14082 (CMCD sib.) | 5/8 | opus-4-7, opus-4-8, composer |
| 2607.08505 | 6/8 | opus-4-8, composer |
| 2604.10209 | 5/8 | opus-4-8, composer, grok |
| 2201.13117 | 5/8 | opus-4-7, opus-4-8, composer |
| 2412.00200 | 4/8 | fable5, opus-4-7, opus-4-8, gpt |
| 2311.03578 | 3/8 | five arms |
| 2310.11979 | 2/8 | six arms |
| 2402.06561 | 2/8 | six arms |
| **2404.09723** | **0/8** | **all arms** |

## Findings

1. **The contract is portable at full scale.** Every model, including the
   cheapest (Composer), produced all 13 mandatory files, a parseable call
   ledger, and a validator-clean workspace. Nobody claimed completeness.
2. **Recall tracks invested effort, not just model tier.** The two thinking
   arms (Opus 5, Fable 5 Thinking) lead at 19 and 18/20 with the largest
   verified pools; Composer spent 25 calls but screened only 19 papers and
   recalled 8/20. Opus 4.7/4.8 leaned on seed-bibliography harvesting, which
   is call-efficient (14-17 calls) but misses papers the seed does not cite.
3. **A hard tail exists below the 40-call budget.** 2404.09723 was found by
   zero arms, and three more core papers by ≤2 arms. These were reached in
   the original run only via deep multi-hop citation traversal (~36 routes).
   The cap quantifies the floor: ~70% of the verified landscape is reachable
   at 40 calls; the last ~15-30% is what the unbounded budget buys.
4. **Verification discipline held under pressure.** Blocked channels
   (Semantic Scholar 429, arXiv listing 403, SciPost anti-bot) were ledgered
   as failures and substituted, not papered over. Unresolved identities
   stayed labeled C0/C1 in every arm.
5. **Recurring defect, second occurrence:** one arm again wrote a manifest
   wildcard row, got a validator MISMATCH, and self-fixed to per-file rows
   (first seen in E1). The manifest template should state per-file rows
   explicitly. Logged for the skill backlog.

## M2 Fabrication Adjudication (scope statement)

Method: every arXiv ID asserted in any arm file was cross-checked against a
321-ID locally verified corpus (July rerun workspace + SPS bibliographies).
Zero contradictions. IDs outside that corpus (largest arms: 220 for Opus 5,
100 for Fable 5) could not be re-resolved locally under the 0-call scoring
budget; for those, the arms' own recorded verification (dual-source
cross-validation, saved API responses) is the evidence of record. No claim
of exhaustive external re-resolution is made.
