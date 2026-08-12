# Candidate Pool

All candidate papers appear here before being confirmed, marked unconfirmed, or
excluded.  Do not delete candidates silently.

| PaperID | Title | Authors | Year | Venue | DOI / URL | Source | Found by | RoundID | Status | Verification | Relevance score | Graph score | Priority | Notes |
|---|---|---|---:|---|---|---|---|---|---|---|---:|---:|---|---|
| P0000 | Stochastic Path Sampler For Lattice Field Theory | Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou | 2026 | arXiv | https://arxiv.org/abs/2606.13790 | arXiv | manual (user seed) | R0001 | confirmed | C4 | 1.0 | | high | Seed; E0001–E0005 |
| P0001 | Path Integral Sampler: a stochastic control approach for sampling | Qinsheng Zhang, Yongxin Chen | 2022 | ICLR (arXiv) | https://arxiv.org/abs/2111.15141 | arXiv | backward from P0000 §1 / bib [55] | R0002 | confirmed | C2 | 0.98 | | high | Key unnormalized path-space parent; E0006–E0007 |
| P0002 | Denoising Diffusion Samplers | Francisco Vargas, Will Grathwohl, Arnaud Doucet | 2023 | ICLR (arXiv) | https://arxiv.org/abs/2302.13834 | arXiv | backward from P0000 §1 / bib [48] | R0002 | confirmed | C2 | 0.96 | | high | Key unnormalized DDS parent; E0008–E0009 |
| P0003 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken | 2024 | ICLR (arXiv) | https://arxiv.org/abs/2307.01050 | arXiv | backward from P0000 §1 / bib [49] | R0002 | confirmed | C2 | 0.97 | | high | Learns forward+backward drifts (explicit SPS parallel); E0010–E0011 |
| P0004 | NETS: A Non-Equilibrium Transport Sampler | Michael S. Albergo, Eric Vanden-Eijnden | 2024 | arXiv | https://arxiv.org/abs/2410.02711 | arXiv | backward from P0000 §1 / bib [6] | R0002 | confirmed | C2 | 0.95 | | high | Non-eq transport sampler for unnormalized targets; E0012–E0013 |
| P0005 | Improved sampling via learned diffusions | Lorenz Richter, Julius Berner | 2024 | ICLR (arXiv) | https://arxiv.org/abs/2307.01198 | arXiv | backward from P0000 §1 / bib [43] | R0003 | confirmed | C2 | 0.94 | | high | Path-space variational learned diffusion sampler; E0014–E0015 |
| P0006 | An optimal control perspective on diffusion-based generative modeling | Julius Berner, Lorenz Richter, Karen Ullrich | 2024 | TMLR (arXiv) | https://arxiv.org/abs/2211.01364 | arXiv | backward from P0000 §1 / bib [10] | R0003 | confirmed | C2 | 0.92 | | high | Optimal-control / path-space KL; DIS unnormalized sampler; E0020–E0021 |
| P0007 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | M. S. Albergo, G. Kanwar, P. E. Shanahan | 2019 | Phys. Rev. D | https://arxiv.org/abs/1904.12072 | arXiv | backward from P0000 §1 / bib [3] | R0003 | confirmed | C2 | 0.93 | | high | Foundational learned NF sampler for LFT/φ⁴; E0016–E0017 |
| P0008 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | L. Wang, G. Aarts, K. Zhou | 2024 | JHEP | https://arxiv.org/abs/2309.17082 | arXiv | backward from P0000 §1 / bib [51] | R0003 | confirmed | C2 | 0.94 | | high | LFT diffusion ↔ stochastic quantization; closest SQ-inspired LFT neighbor; E0018–E0019 |
| P0009 | Learning Lattice Quantum Field Theories with Equivariant Continuous Flows | Mathis Gerdes, Pim de Haan, Corrado Rainone, Roberto Bondesan, Miranda C. N. Cheng | 2023 | SciPost Phys. | https://arxiv.org/abs/2207.00283 | arXiv | backward from P0000 §1 / bib [23] | R0003 | confirmed | C2 | 0.88 | | medium | Equivariant CNF for LFT; E0022 |
| P0010 | Equivariant flow-based sampling for lattice gauge theory | G. Kanwar et al. | 2020 | PRL (bib) | bib of P0000 cites 2003.06413 | arXiv bib-of-C3 | bib [28] of P0000 | R0001 | unconfirmed | C1(bib-of-C4) | 0.80 | | medium | Budget exhausted; ERQ0001 |
| P0011 | Stochastic normalizing flows as non-equilibrium transformations | M. Caselle, E. Cellini, A. Nada, M. Panero | 2022 | JHEP (bib) | bib of P0000 cites 2201.08862 | arXiv bib-of-C3 | bib [12] of P0000 | R0001 | unconfirmed | C1(bib-of-C4) | 0.82 | | medium | Budget exhausted; ERQ0002 |
| P0012 | Stochastic normalizing flows | H. Wu, J. Köhler, F. Noé | 2020 | NeurIPS (bib) | Link-only in P0000 bib [54] | bib-of-C3 | bib [54] of P0000 | R0001 | unconfirmed | C0 | 0.75 | | low | No independent URL fetch; ERQ0003 |

## Deduplication Notes

| Duplicate group | PaperIDs | Decision | Reason |
|---|---|---|---|
| — | — | — | no duplicates |

## Promotion Rules

- Promote to confirmed only after independent logged fetch of authoritative page (this run).
- Keep important but unfetched bib leads as unconfirmed C0/C1(bib-of-C4).
- Predecessor claims in answers cite only confirmed rows with EvidenceIDs.
