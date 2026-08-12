# Coverage And Stopping Report

## Summary

- Scan level: full (graph_mode OFF).
- Objective mode: high-recall (cover) under a 40-web-call hard cap.
- Stop decision: stop (saturated_under_budget, with recorded residual risk).
- Date: 2026-08-12.
- Calls used: 14 / 40.
- Channels covered (4, >=3 required): arXiv (abs/HTML + 7 PDF downloads),
  Semantic Scholar Graph API (2 batches), INSPIRE-HEP (1 record), web search
  (Google-style, surfacing Science / PMLR / DOI-resolver / Zenodo pages).

## What Was Traversed

- G0 seed: arXiv:2606.13790 fully read (method + correction mechanism + full
  reference list). Seed recall = 1/1.
- G1 backward: the seed's ~57-entry bibliography harvested; the sampler/
  mechanism subset promoted via S2/INSPIRE/PDF.
- Adversarial / topic expansion (out-of-bib): Boltzmann Generators, FAB /
  Bootstrap-Your-Flow, Annealed Flow Transport — three adjacent families the
  lattice-centric bibliography did not cite.

## Diagnostics

| diagnostic | result | interpretation | action |
|---|---|---|---|
| seed recall | 1/1 seed + full bib recovered | seed lineage captured | none |
| route overlap | RT1 bib vs RT3 S2: high overlap, consistent | metadata cross-validated | none |
| estimated missing items | moderate (forward citations of seed not searched) | 2026 seed has few/no citing works indexed yet | reopen if citing works appear |
| singleton / doubleton pattern | out-of-bib families found only via RT6 | keyword expansion mattered | done |
| consecutive no-new-include rounds | R0004 added 3 new families -> not yet 2 clean rounds | mild residual recall risk | recorded as risk |
| facet coverage | F1>=8, F2>=12, F3>=6 verified representatives | quotas met | none |
| decision sufficiency | landscape stable for a related-work map | sufficient for the stated task | stop |

## Funnel

62 raw hits -> 58 deduplicated -> 19 screened include -> 7 C3 PDFs.
Distinct verified papers with arXiv IDs (C2+): 19.

## Residual Risks

| risk | likely impact | mitigation / monitor trigger |
|---|---|---|
| Forward citations not searched (graph_mode OFF) | may miss 2026 works building on SPS | run S2/INSPIRE cited-by next round |
| 9 lineage entries remain C1 bib-of-C4 (P0004,P0009,P0011,P0013–P0018,P0026–P0028) | identity single-source | S2/INSPIRE batch to reach C2 |
| AFT (P0034) arXiv id unverified | one adjacent record weakly identified | resolve arXiv/Crossref |
| Molecular-dynamics + SMC sampler subfields only lightly probed | some F1 neighbors possibly missed | targeted queries if scope widens |
| Adversarial round still yielded new families | recall not fully saturated | one more RT6 round would reduce risk |

## Stop Rationale

The three requested facets each have >=3 independently cross-validated
representatives and 7 full-text PDFs anchor the core mechanisms, so the
predecessor/adjacent-method map is stable enough for a related-work landscape.
The scan is stopped under budget (14/40). This is auditable coverage **under the
stated scope**, NOT a claim of completeness: forward-citation closure was not
performed (graph_mode OFF), and several bibliography entries remain
single-source. Reopen the search if (a) citing works of 2606.13790 appear,
(b) the task requires the C1 entries promoted to C2, or (c) scope widens to
molecular / SMC learned samplers.
