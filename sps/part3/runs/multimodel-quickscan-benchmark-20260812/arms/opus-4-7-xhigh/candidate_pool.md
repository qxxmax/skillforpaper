# Candidate Pool

All candidate predecessor papers appear here before being confirmed, marked
unconfirmed, or excluded. Every row is either the SPS root paper or a direct
predecessor explicitly cited by SPS in its Introduction as belonging to one
of the two families in the research question: (A) learned/neural samplers
for unnormalized target distributions, or (B) learned samplers for lattice
field theory. Each `confirmed` row is backed by a logged web fetch of the
arXiv landing page (see `round_log.md` and `evidence_registry.md`).

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Graph score | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P0000 | Stochastic Path Sampler for Lattice Field Theory | S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou | 2026 | arXiv | https://arxiv.org/abs/2606.13790 | arXiv | user | R0001 | root | C3 (full abstract page + intro + full reference list fetched) | — | — | high | target paper of the run; explicitly names predecessors in Introduction |
| P0001 | Path Integral Sampler: a stochastic control approach for sampling | Qinsheng Zhang, Yongxin Chen | 2022 | ICLR 2022 | https://arxiv.org/abs/2111.15141 | arXiv | SPS ref [55] | R0001 | confirmed | C2 | high | high | high | Family A — path-space KL / stochastic-control sampler for unnormalized densities |
| P0002 | Denoising Diffusion Samplers | Francisco Vargas, Will Grathwohl, Arnaud Doucet | 2023 | ICLR 2023 | https://arxiv.org/abs/2302.13834 | arXiv | SPS ref [48] | R0001 | confirmed | C2 | high | high | high | Family A — DDS: time-reversal-based sampler for unnormalized densities |
| P0003 | An optimal control perspective on diffusion-based generative modeling | Julius Berner, Lorenz Richter, Karen Ullrich | 2024 | TMLR | https://arxiv.org/abs/2211.01364 | arXiv | SPS ref [10] | R0001 | confirmed | C2 | high | high | high | Family A — optimal-control formulation of diffusion-based sampling; time-reversed diffusion sampler (DIS) |
| P0004 | Improved sampling via learned diffusions | Lorenz Richter, Julius Berner | 2024 | ICLR 2024 | https://arxiv.org/abs/2307.01198 | arXiv | SPS ref [43] | R0001 | confirmed | C2 | high | high | high | Family A — generalized-Schrödinger-bridge / log-variance loss for learned-diffusion samplers |
| P0005 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions (CMCD) | Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken | 2024 | ICLR 2024 | https://arxiv.org/abs/2307.01050 | arXiv | SPS ref [49] | R0001 | confirmed | C2 | high | high | high | Family A — SPS text calls out CMCD explicitly as also learning both forward and backward drifts, mirroring SPS's own design |
| P0006 | NETS: A Non-Equilibrium Transport Sampler | Michael S. Albergo, Eric Vanden-Eijnden | 2024 | arXiv | https://arxiv.org/abs/2410.02711 | arXiv | SPS ref [6] | R0001 | confirmed | C2 | high | high | high | Family A — non-equilibrium transport sampler; AIS + Jarzynski + learned drift; already tested on a lattice-field-theory target |
| P0007 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | M. S. Albergo, G. Kanwar, P. E. Shanahan | 2019 | Phys. Rev. D 100 (2019) 034515 | https://arxiv.org/abs/1904.12072 | arXiv | SPS ref [3] | R0001 | confirmed | C2 | high | high | high | Family B — seminal flow-based lattice sampler; benchmarked on 2D phi^4 (same target as SPS) |
| P0008 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | L. Wang, G. Aarts, K. Zhou | 2024 | JHEP 2024 (05) 060 | https://arxiv.org/abs/2309.17082 | arXiv | SPS ref [51] | R0001 | confirmed | C2 | high | high | high | Family B — closest same-group precursor: SPS is described as "stochastic-quantization-inspired"; two SPS authors (Aarts, Zhou) are authors here |
| P0009 | Stochastic normalizing flows as non-equilibrium transformations | M. Caselle, E. Cellini, A. Nada, M. Panero | 2022 | JHEP 07 (2022) 015 | https://arxiv.org/abs/2201.08862 | arXiv | SPS ref [12] | R0001 | confirmed | C2 | high | high | high | Family B — combines Langevin/Monte-Carlo steps with normalizing flows on lattice; direct methodological neighbor for SPS's Langevin-based dynamics |

## Deduplication Notes

None. All confirmed rows are distinct arXiv IDs.

## Family Coverage

- **Family A — learned/neural samplers for unnormalized target distributions
  (data-free path-space KL family):** P0001 PIS, P0002 DDS, P0003 Berner et al.
  (DIS / optimal-control), P0004 Richter–Berner improved-diffusion sampling,
  P0005 CMCD, P0006 NETS. This is exactly the set the SPS Introduction
  enumerates as "data-free diffusion-based samplers that minimize a path-space
  Kullback–Leibler objective closely related to the one employed in this
  work."
- **Family B — learned samplers for lattice field theory:** P0007 Albergo et al.
  2019 (seminal NF-for-lattice, same 2D phi^4 target as SPS), P0008
  Wang–Aarts–Zhou 2024 (diffusion-as-stochastic-quantization on lattice, same
  group as SPS), P0009 Caselle et al. 2022 (stochastic normalizing flows on
  lattice, combining Langevin with NFs — the closest methodological neighbor
  on the lattice side).

Additional lattice-sampler references named in SPS's Introduction — Nicoli
et al. [35] (arXiv:2007.07115), Gerdes et al. [23] (arXiv:2207.00283),
Wu–Köhler–Noé Stochastic Normalizing Flows [54] (NeurIPS 2020),
Rezende–Mohamed normalizing flows [42], and Zhou et al. 2019 [56]
(arXiv:1810.12879) — are documented in SPS's own reference list (C1
verification via context of an already-C3 verified full text; noted as
`C1(bib-of-C3)` in `evidence_registry.md`) but were **not independently
fetched within the 10-call quick-scan budget**. They remain in this pool as
context-only and are not promoted to `confirmed` in this arm.

## Promotion Rules

- Promote to confirmed only after an authoritative landing page verifies
  title + authors + identifier via a logged web call.
- Keep predecessors that could not be independently fetched within budget as
  `C1(bib-of-C3)` context-only rather than `confirmed`.
- Move out-of-scope suggestions to `excluded` with a reason (none this round).
