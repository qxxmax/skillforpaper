# Candidate Pool

Target paper and predecessors identified from arXiv:2606.13790 §1–§2 and verified via logged arXiv fetches.

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Graph score | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---:|---:|---|---|
| P0000 | Stochastic Path Sampler For Lattice Field Theory | Shiyang Chen; Moxian Qian; Gert Aarts; Biagio Lucini; Kai Zhou | 2026 | arXiv preprint | https://arxiv.org/abs/2606.13790 | arXiv fetch | manual seed | R0001 | confirmed | C2 | 1.0 | 1.0 | high | Focal paper |
| P0001 | Path Integral Sampler: a stochastic control approach for sampling | Qinsheng Zhang; Yongxin Chen | 2022 | ICLR (arXiv) | https://arxiv.org/abs/2111.15141 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.95 | 0.95 | high | Closest path-space KL predecessor; SPS calls this family |
| P0002 | Denoising Diffusion Samplers | Francisco Vargas; Will Grathwohl; Arnaud Doucet | 2023 | ICLR (arXiv) | https://arxiv.org/abs/2302.13834 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.90 | 0.90 | high | Data-free diffusion sampler for unnormalized π |
| P0003 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | Francisco Vargas; Shreyas Padhy; Denis Blessing; Nikolas Nüsken | 2024 | ICLR (arXiv) | https://arxiv.org/abs/2307.01050 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.90 | 0.88 | high | Learns forward and backward drifts (like SPS) |
| P0004 | NETS: A Non-Equilibrium Transport Sampler | Michael S. Albergo; Eric Vanden-Eijnden | 2024 | arXiv preprint | https://arxiv.org/abs/2410.02711 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.85 | 0.85 | high | Non-equilibrium transport for unnormalized targets |
| P0005 | An optimal control perspective on diffusion-based generative modeling | Julius Berner; Lorenz Richter; Karen Ullrich | 2024 | TMLR (arXiv) | https://arxiv.org/abs/2211.01364 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.85 | 0.82 | high | Path-space KL / DIS sampling framework |
| P0006 | Improved sampling via learned diffusions | Lorenz Richter; Julius Berner | 2024 | ICLR (arXiv) | https://arxiv.org/abs/2307.01198 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.85 | 0.82 | high | Generalized Schrödinger-bridge sampling losses |
| P0007 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | M. S. Albergo; G. Kanwar; P. E. Shanahan | 2019 | Phys. Rev. D (arXiv) | https://arxiv.org/abs/1904.12072 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.90 | 0.88 | high | Foundational NF + MHMCMC for 2D φ⁴ LFT |
| P0008 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | L. Wang; G. Aarts; K. Zhou | 2024 | JHEP (arXiv) | https://arxiv.org/abs/2309.17082 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.88 | 0.85 | high | Supervised DM baseline for 2D φ⁴; shared author line |
| P0009 | Learning Lattice Quantum Field Theories with Equivariant Continuous Flows | Mathis Gerdes; Pim de Haan; Corrado Rainone; Roberto Bondesan; Miranda C. N. Cheng | 2023 | SciPost Phys. (arXiv) | https://arxiv.org/abs/2207.00283 | arXiv fetch | backward from P0000 §1 | R0001 | confirmed | C2 | 0.85 | 0.80 | high | CNF / neural ODE sampler for LFT including φ⁴ |
| P0010 | Trajectory balance: improved credit assignment in GFlowNets | N. Malkin; M. Jain; E. Bengio; C. Sun; Y. Bengio | 2022 | NeurIPS | NeurIPS proceedings link only | bib-of-C4 from P0000 | backward from P0000 §2 | R0001 | unconfirmed | C0 | 0.80 | 0.75 | medium | Cited for trajectory-level balance; no arXiv fetch (budget) |
| P0011 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | K. A. Nicoli et al. | 2021 | Phys. Rev. Lett. | arXiv:2007.07115 (bib only) | bib-of-C4 from P0000 | backward from P0000 §1, §3 | R0001 | unconfirmed | C0 | 0.75 | 0.70 | medium | Deep generative φ⁴; geometry reference in §3; not fetched |
| P0012 | Variational Autoregressive Networks Applied to φ⁴ Field Theory Systems | M. Qian; S. Chen | 2025 | arXiv preprint | arXiv:2512.19575 (bib only) | bib-of-C4 from P0000 | backward from P0000 §1 | R0001 | unconfirmed | C0 | 0.70 | 0.65 | low | VAE-style LFT sampler; budget exhausted |

## Deduplication Notes

| Duplicate group | PaperIDs | Decision | Reason |
|---|---|---|---|
| — | — | — | No duplicates |

## Promotion Rules

- Promote to confirmed only after source and relevance evidence pass the required gates for the current intent mode.
- Keep important but inaccessible papers as unconfirmed, with next action and omission risk.
- Move out-of-scope or duplicate papers to excluded with a reason.
