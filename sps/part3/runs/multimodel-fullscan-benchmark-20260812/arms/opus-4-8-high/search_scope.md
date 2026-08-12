# Search Scope

## Task

- Research question / search objective: map predecessor + adjacent-method
  landscape of "Stochastic Path Sampler for Lattice Field Theory"
  (arXiv:2606.13790) across three facets — (F1) learned/neural samplers for
  unnormalized targets, (F2) learned samplers for lattice field theory,
  (F3) correction/exactness mechanisms.
- Artifact target: literature landscape (related-work / prior-art map).
- Scan level: full.
- Date started: 2026-08-12.
- Owner: benchmark arm opus-4-8-high.

## Eligibility

| Field | Definition |
|---|---|
| Relevant item | A paper/preprint proposing or analysing a learned sampler for an unnormalized target, a learned sampler for lattice field theory, or an exactness/correction mechanism for such samplers. |
| Exclude even if related | Pure classical MCMC without a learned component; generative modelling with no unnormalized-target sampling claim. |
| Required evidence type | arXiv/DOI identifier + at least one independent metadata source; C3 for the >=6 core PDFs. |
| Time span | 2018–2026 (no hard lower bound for foundational NEIS/MCMC). |
| Language / geography / venue limits | English; arXiv + ML venues (NeurIPS/ICML/ICLR) + physics venues (PRL/PRD/PRE/Nature). |
| Required identifiers | arXiv ID preferred; DOI where published. |

## Objective Mode

- Mode: high-recall (cover) under a hard 40-web-call cap.
- Target recall or coverage: >=3 verified representatives per facet F1/F2/F3.
- Confidence or acceptable residual risk: seed may be unverifiable; document it.
- Budget: 40 web calls (searches + fetches + PDF downloads all count).
- Stopping standard: facet quotas met AND two consecutive rounds add no new
  method family, OR the 40-call cap is reached.

## Seed Set

| seed item | why relevant | expected source route | recovered? | notes |
|---|---|---|---|---|
| arXiv:2606.13790 (SPS for LFT) | benchmark target / root | arXiv abs + HTML + web | YES | confirmed: Chen, Qian, Aarts, Lucini, Zhou; created 2026-06-11 (R0001) |
| Albergo-Kanwar-Shanahan 2019 (flow-based MCMC for LFT) | canonical F2 predecessor | arXiv/S2 | YES | 1904.12072 |
| Zhang-Chen 2021 (Path Integral Sampler) | canonical F1 stochastic-control predecessor | arXiv/S2 | YES | 2111.15141 |

## Facet Map

| facet | why it matters | minimum evidence needed | current status |
|---|---|---|---|
| F1 learned samplers for unnormalized targets | the method class SPS belongs to | >=3 C3 papers | met |
| F2 learned samplers for lattice field theory | the application domain | >=3 C3 papers | met |
| F3 correction / exactness mechanisms | SPS's claimed contribution type | >=3 verified mechanisms across papers | met |
