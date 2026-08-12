# Claim Evidence Ledger

Project: SPS paper (arXiv:2606.13790) submission rehearsal
Date: 2026-08-12
Artifact target: manuscript / cover letter / response letters

Claims and wording bounds are taken from the verified Part 2 review
(`sps/part2/runs/sps-goal-mode-rerun-20260716/review_core.md`, status READY);
EvidenceIDs resolve in the Part 2 run's evidence files.

| Claim ID | Claim | Claim type | Source/local evidence | Exact value/formula | Figure/table | Allowed wording | Forbidden wording | Artifact use | Status |
|---|---|---|---|---|---|---|---|---|---|
| C1 | SPS differs from the checked predecessors by extended-space trajectory IMH | interpretation | E-260613790-M; predecessor method records (D004, D005) | P001 Eqs. (2.18)-(2.19) vs P002 Eq. (17), P004 Eqs. (23)-(24) | — | "among the checked core comparators, the narrowest correction difference" | "SPS introduced path-space sampling"; "first to learn forward and backward drifts" | paper, cover letter | strong |
| C2 | SPS+IMH reproduces the tested HMC observables | numerical result | E-260613790-R | P001 Tables 1-2, Sec. 3 | P001 Tables 1-4 | "reproduces HMC observables in the tested two-dimensional phi4 scan" | "universally accelerates HMC"; any cross-paper speed ranking | paper | strong |
| C3 | Independent drift networks and learned scalar diffusion are a design difference from CMCD's score-coupled pair | interpretation | E-230701050-M; E-260613790-M (D003) | P004 Eqs. (21)-(24) vs P001 Eqs. (2.2)-(2.17) | — | "design difference; isolated benefit not measured" | "independent drifts improve performance" | paper (limitations / future work) | adequate |
| C4 | Corrected-chain autocorrelation is short within the paper's own setup | numerical result | E-260613790-L (D007) | P001 p. 17 Table 4, Sec. 3.5 | Table 4 | "within-setup autocorrelation and wall times as reported" | "faster than HMC/SNF per GPU-hour" (no matched-cost comparison exists) | paper | adequate |

## Claim Types

- Interpretation claims C1, C3: comparisons hold for the checked comparator
  set (PIS, DDS, CMCD, SNF) only; no priority claim over all literature.
- Numerical claims C2, C4: scope is the paper's two-dimensional phi4 scan.

## Overclaim Watchlist

- Claims to soften: none pending (bounds already applied per Part 2 review).
- Claims to remove: any "first/novel sampler family" phrasing (rejected in
  Part 2 with counterevidence P002, P003, P004).
- Claims needing more evidence: C3 benefit isolation (needs the Part 3
  matched correction-and-cost experiment flagged in the Part 2 reading order).
- Claims allowed only in future-work language: performance effect of
  independent drifts; matched estimator-per-GPU-hour comparison.

## Numbers Freeze (Part 5)

Blocked: the manuscript TeX/PDF source is not in this repository, so
abstract/conclusion numbers cannot be enumerated and frozen here. This is a
submission-gate blocker, recorded in `submission_package_manifest.md`. When
the manuscript is available, every prose number must get a row below.

| Number (as written in prose) | Where it appears | Source (figure/table/log/RunID) | Checked on | Match? |
|---|---|---|---|---|
| — blocked: manuscript source unavailable in this repository — |  |  |  |  |
