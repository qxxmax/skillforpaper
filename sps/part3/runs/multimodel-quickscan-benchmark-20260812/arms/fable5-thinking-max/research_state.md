# Research State

Run: multimodel-quickscan-benchmark-20260812 / arm: fable5-thinking-max
Scan level: quick
Date: 2026-08-12

## Research question

The paper "Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790)
proposes a learned stochastic sampler for lattice phi^4 theory. Identify the
key prior methods this paper directly builds on — (a) learned/neural samplers
for unnormalized target distributions and (b) learned samplers for lattice
field theory — and verify each one's identity (exact title, authors, arXiv ID)
with logged web calls.

## Intent mode

```yaml
intent_mode:
  primary: locate
  secondary: learn
risk_level: medium
current_action: locate_source
output_mode: evidence_table
```

## Budget (mirror; round_log.md call ledger is authoritative)

- Cap: 10 web calls (searches + fetches combined).
- Used: 2/10 (mirror of round_log.md ledger rows 1-2).

## Policies

- Token policy: strict.
- Screenshot policy: on-demand (quick-scan default; no screenshots captured).

## Root node

- arXiv:2606.13790 "Stochastic Path Sampler For Lattice Field Theory" — Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou. Verified C3 (E001, call 1).

## Findings summary

Direct predecessors of SPS (arXiv:2606.13790), all verified C2 via calls 1-2:

Family A — learned/neural samplers for unnormalized target distributions
(data-free path-space samplers named in SPS §1):

- P01 arXiv:2111.15141 — Path Integral Sampler (Qinsheng Zhang, Yongxin Chen)
- P02 arXiv:2302.13834 — Denoising Diffusion Samplers (Vargas, Grathwohl, Doucet)
- P03 arXiv:2307.01050 — Controlled Monte Carlo Diffusions (Vargas, Padhy, Blessing, Nüsken); SPS notes CMCD, like SPS, learns both forward and backward drifts
- P04 arXiv:2410.02711 — NETS: A Non-Equilibrium Transport Sampler (Albergo, Vanden-Eijnden)
- P05 arXiv:2211.01364 — An optimal control perspective on diffusion-based generative modeling (Berner, Richter, Ullrich)
- P06 arXiv:2307.01198 — Improved sampling via learned diffusions (Richter, Berner)
- P08 arXiv:2002.06707 — Stochastic Normalizing Flows (Wu, Köhler, Noé)

Family B — learned samplers for lattice field theory:

- P07 arXiv:1904.12072 — Flow-based generative models for MCMC in lattice field theory (Albergo, Kanwar, Shanahan)
- P09 arXiv:2201.08862 — Stochastic normalizing flows as non-equilibrium transformations (Caselle, Cellini, Nada, Panero)
- P10 arXiv:2309.17082 — Diffusion Models as Stochastic Quantization in Lattice Field Theory (Wang, Aarts, Zhou); cited in SPS §1 and §2.2 as the stochastic-quantization route SPS adapts

## Remaining risks

- Quick scan: only the predecessors explicitly named in SPS §1 were verified;
  the wider cited pool (gauge-theory flows, CNFs, autoregressive networks,
  supervised diffusion applications) remains at C1(bib-of-C4), recorded in
  E002 but not promoted.
- All verification is arXiv metadata-level (C2); no full-text reads of the
  predecessors were performed.

## Stop status

- Stopped. All named predecessors verified; 8/10 budget unspent.

## Validator result

- `scripts/validate_run_state.py` run 2026-08-12: profile `literature`,
  status `CONSISTENT`, no errors, no warnings, exit code 0.
- First attempt returned MISMATCH due to file-format issues only (manifest
  table lacked the 5-column status layout; ledger header was "Call ledger"
  instead of "Call Ledger"); both fixed and re-validated. No content errors.
