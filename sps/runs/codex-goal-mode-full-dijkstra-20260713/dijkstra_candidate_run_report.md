# Candidate-Graph Dijkstra Run

This is an actual single-source Dijkstra calculation from the SPS root.
It uses current-run query hits, authorship, and facet membership.
Screen labels are not used as edge weights; they remain an eligibility gate.

## Graph

- nodes: 3300
- edges: 8187
- paper candidates: 593
- reachable paper candidates: 593
- eligible arXiv full texts: 51

## First 15 eligible reading paths

| rank | candidate | distance | screen score | path |
|---:|---|---:|---:|---|
| 1 | Stochastic Path Sampler For Lattice Field Theory | 0.0 | 121 | `paper:arxiv:2606.13790` |
| 14 | Generative Diffusion Models for Lattice Field Theory | 1.057259 | 15 | `paper:arxiv:2606.13790 -> query:Q08 -> paper:arxiv:2311.03578` |
| 24 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | 1.166704 | 13 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:1904.12072` |
| 25 | Stochastic normalizing flows for lattice field theory | 1.177259 | 18 | `paper:arxiv:2606.13790 -> query:Q28 -> paper:arxiv:2210.03139` |
| 26 | Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality | 1.177259 | 9 | `paper:arxiv:2606.13790 -> query:Q29 -> paper:arxiv:2604.10209` |
| 30 | Physics-Conditioned Diffusion Models for Lattice Gauge Theory | 1.219445 | 20 | `paper:arxiv:2606.13790 -> query:Q06 -> paper:arxiv:2502.05504` |
| 32 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | 1.228364 | 10 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2007.07115` |
| 53 | Flow-based sampling for fermionic lattice field theories | 1.281777 | 14 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2106.05934` |
| 58 | Equivariant flow-based sampling for lattice gauge theory | 1.32889 | 12 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2003.06413` |
| 63 | SCORENF: Score-based Normalizing Flows for Sampling Unnormalized distributions | 1.339445 | 12 | `paper:arxiv:2606.13790 -> query:Q27 -> paper:arxiv:2510.21330` |
| 74 | Flow-based sampling in the lattice Schwinger model at criticality | 1.409158 | 10 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2202.11712` |
| 90 | Diffusion model for SU(N) gauge theories | 1.423775 | 14 | `paper:arxiv:2606.13790 -> query:Q08 -> paper:arxiv:2605.06134` |
| 94 | Variational Autoregressive Networks Applied to $^4$ Field Theory Systems | 1.443963 | 9 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2512.19575` |
| 101 | Learning lattice quantum field theories with equivariant continuous flows | 1.47598 | 10 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2207.00283` |
| 107 | Scaling Up Machine Learning For Quantum Field Theory with Equivariant Continuous Flows | 1.505623 | 9 | `paper:arxiv:2606.13790 -> query:Q04 -> paper:arxiv:2110.02673` |

## Boundary

The distance is a search-navigation cost, not citation proof or claim evidence.
