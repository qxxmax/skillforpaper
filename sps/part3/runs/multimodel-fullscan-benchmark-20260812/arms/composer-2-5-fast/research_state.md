# Research State

## Intent

```yaml
intent_mode:
  primary: cover
  secondary: learn
risk_level: high
current_action: audit_exclusions
output_mode: audit_package
scan_level: full
graph_mode: off
token_policy: strict
screenshot_policy: none
```

## Root and question

- **Seed:** Stochastic Path Sampler For Lattice Field Theory — arXiv:2606.13790 (PaperID P0001)
- **Question:** Map predecessor and adjacent-method landscape for (1) learned/neural samplers for unnormalized targets, (2) learned samplers in lattice field theory, (3) correction/exactness mechanisms.

## Scope snapshot

- **Facets:** data-free path-space variational samplers; flow/normalizing-flow LFT; diffusion/score LFT (data-driven); stochastic normalizing flows; IMH/MH/reweighting correction families.
- **Channels used:** arXiv (search/abs/PDF), INSPIRE-HEP, Semantic Scholar API, web/Google Scholar-style search, publisher DOI landing (Springer JHEP metadata via search).
- **Blocked:** arXiv HTML search endpoint returned HTTP 403 on one attempt (logged).

## Budget mirror (ledger wins)

| field | value |
|---|---|
| hard cap | 40 web calls |
| Used: 25 | (mirror of call ledger) |
| C3 PDFs | 6 |
| verified arXiv papers | 11 |
| raw hits (est.) | ~95 |
| deduplicated candidates | 38 |
| screened include | 19 |
| stop | marginal yield low; cap not exhausted but facet saturation partial |

## Validator

- **Last run:** 2026-08-12 — see Validation section below after `validate_run_state.py`.

## Validation

```
run:     ~/Desktop/skillforpaper/sps/part3/runs/multimodel-fullscan-benchmark-20260812/arms/composer-2-5-fast
profile: literature
status:  CONSISTENT (validate_run_state.py 2026-08-12)
Used: 25
errors: []
warnings: []
```

## Next action if resumed

- Forward-citation chase on SPS citing papers (Semantic Scholar listed 3, not all fetched).
- G1 backward refs from INSPIRE seed page (58 refs, only title-level from index).
- Denoising Diffusion Samplers PDF verification (2302.13834) and Trajectory Balance GFlowNet paper (NeurIPS 2022) independent ID lock.
