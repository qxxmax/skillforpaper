# Research State

Run: multimodel-quickscan-benchmark-20260812 / arm fable5
Date: 2026-08-12

## Question

The paper "Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790)
proposes a learned stochastic sampler for lattice phi^4 theory. Identify the key
prior methods this paper directly builds on — (a) learned/neural samplers for
unnormalized target distributions and (b) learned samplers for lattice field
theory — and verify each one's identity (exact title, authors, arXiv ID) with
logged web calls.

## Mode

```yaml
intent_mode:
  primary: locate
  secondary: learn
risk_level: medium
current_action: locate_source
output_mode: evidence_table
```

Scan level: quick
Token policy: strict (10 web calls max)
Screenshot policy: none (links + metadata only)

## Budget mirror (authoritative counter is round_log.md call ledger)

- Budget: 10 calls
- Used: 10/10 (1 fetch of focal paper, 9 fetches of predecessor arXiv pages;
  0 failed calls)

## Findings summary

Focal paper confirmed at C3 (E01): "Stochastic Path Sampler For Lattice Field
Theory", S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou, arXiv:2606.13790.

Verified direct predecessors (all C2, identity checked on each paper's own
arXiv page; see evidence_registry.md and candidate_pool.md):

Facet A — data-free path-space-KL neural samplers for unnormalized targets:
- P01 Path Integral Sampler (Zhang & Chen), arXiv:2111.15141 (E02)
- P02 Denoising Diffusion Samplers (Vargas, Grathwohl, Doucet), arXiv:2302.13834 (E03)
- P03 Controlled Monte Carlo Diffusions (Vargas, Padhy, Blessing, Nüsken), arXiv:2307.01050 (E04)
- P04 NETS: A Non-Equilibrium Transport Sampler (Albergo & Vanden-Eijnden), arXiv:2410.02711 (E05)
- P05 An optimal control perspective on diffusion-based generative modeling (Berner, Richter, Ullrich), arXiv:2211.01364 (E06)

Facet B — learned samplers for lattice field theory:
- P07 Flow-based generative models for MCMC in lattice field theory (Albergo, Kanwar, Shanahan), arXiv:1904.12072 (E07)
- P08 Diffusion Models as Stochastic Quantization in Lattice Field Theory (Wang, Aarts, Zhou), arXiv:2309.17082 (E08)
- P09 Stochastic Normalizing Flows (Wu, Köhler, Noé), arXiv:2002.06707 (E09)
- P10 Stochastic normalizing flows as non-equilibrium transformations (Caselle, Cellini, Nada, Panero), arXiv:2201.08862 (E10)

Unverified (budget exhausted, kept at C1(bib-of-C3), not asserted):
- P06 Improved sampling via learned diffusions (Richter & Berner), bib-claimed
  arXiv:2307.01198.

## Stop status

Stopped: quick-scan objective met (both requested predecessor families
identified from the focal paper's own §1 and independently verified), budget
exhausted at 10/10. Remaining risk: P06 identity unverified; classic non-arXiv
foundations (Parisi & Wu 1981 stochastic quantization) noted but out of scope
for arXiv verification.

## Validator result

`validate_run_state.py` run 2026-08-12 (actual output):

```text
profile: literature
status:  CONSISTENT
```

First attempt returned MISMATCH because the manifest used a 3-column table the
validator cannot parse; the manifest was rewritten to the 6-column template
format and the re-run returned CONSISTENT with no errors or warnings.
