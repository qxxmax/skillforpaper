# Verified-Graph Dijkstra Run

This is the second Dijkstra pass. It starts at SPS and traverses checked
direct-citation edges, current metadata authorship edges, and screened
method-membership edges. Evidence types remain explicit in every path.

## Graph and reachability

- nodes: 164
- directed weighted edges: 944
- selected paper nodes: 37
- reachable paper nodes: 37
- citation-only paths: 36
- author-bridge paths: 0
- method-bridge paths: 0

## Shortest paths from SPS

| rank | paper | distance | path type | shortest path |
|---:|---|---:|---|---|
| 1 | Stochastic Path Sampler For Lattice Field Theory | 0.0 | root | `paper:2606.13790` |
| 2 | Flow-based generative models for Markov chain Monte Carlo in lattice field theory | 0.2 | citation_only | `paper:2606.13790 -> paper:1904.12072` |
| 3 | Regressive and generative neural networks for scalar field theory | 0.2 | citation_only | `paper:2606.13790 -> paper:1810.12879` |
| 4 | Equivariant flow-based sampling for lattice gauge theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2003.06413` |
| 5 | Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models | 0.2 | citation_only | `paper:2606.13790 -> paper:2007.07115` |
| 6 | Flow-based sampling for fermionic lattice field theories | 0.2 | citation_only | `paper:2606.13790 -> paper:2106.05934` |
| 7 | Scaling Up Machine Learning For Quantum Field Theory with Equivariant Continuous Flows | 0.2 | citation_only | `paper:2606.13790 -> paper:2110.02673` |
| 8 | Flow-based sampling in the lattice Schwinger model at criticality | 0.2 | citation_only | `paper:2606.13790 -> paper:2202.11712` |
| 9 | Path Integral Sampler: a stochastic control approach for sampling | 0.2 | citation_only | `paper:2606.13790 -> paper:2111.15141` |
| 10 | Stochastic normalizing flows as non-equilibrium transformations | 0.2 | citation_only | `paper:2606.13790 -> paper:2201.08862` |
| 11 | Stochastic normalizing flows for lattice field theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2210.03139` |
| 12 | Denoising Diffusion Samplers | 0.2 | citation_only | `paper:2606.13790 -> paper:2302.13834` |
| 13 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2309.17082` |
| 14 | Fourier-flow model generating Feynman paths | 0.2 | citation_only | `paper:2606.13790 -> paper:2211.03470` |
| 15 | Learning lattice quantum field theories with equivariant continuous flows | 0.2 | citation_only | `paper:2606.13790 -> paper:2207.00283` |
| 16 | NETS: A Non-Equilibrium Transport Sampler | 0.2 | citation_only | `paper:2606.13790 -> paper:2410.02711` |
| 17 | Numerical determination of the width and shape of the effective string using Stochastic Normalizing Flows | 0.2 | citation_only | `paper:2606.13790 -> paper:2409.15937` |
| 18 | Stochastic normalizing flows for Effective String Theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2412.19109` |
| 19 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | 0.2 | citation_only | `paper:2606.13790 -> paper:2307.01050` |
| 20 | Flow-based sampling for multimodal and extended-mode distributions in lattice field theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2107.00734` |
| 21 | Group-Equivariant Diffusion Models for Lattice Field Theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2510.26081` |
| 22 | Physics-Conditioned Diffusion Models for Lattice Gauge Theory | 0.2 | citation_only | `paper:2606.13790 -> paper:2502.05504` |
| 23 | Variational Autoregressive Networks Applied to $^4$ Field Theory Systems | 0.2 | citation_only | `paper:2606.13790 -> paper:2512.19575` |
| 24 | Diffusion model for SU(N) gauge theories | 0.2 | citation_only | `paper:2606.13790 -> paper:2605.06134` |
| 25 | Diffusion Models for Sampling Near Criticality in Lattice Field Theories | 0.3 | citation_only | `paper:2606.13790 -> paper:2607.08505` |
| 26 | Introduction to Normalizing Flows for Lattice Field Theory | 0.4 | citation_only | `paper:2606.13790 -> paper:2106.05934 -> paper:2101.08176` |
| 27 | Aspects of scaling and scalability for flow-based sampling of lattice QCD | 0.4 | citation_only | `paper:2606.13790 -> paper:2107.00734 -> paper:2211.07541` |
| 28 | Sampling QCD field configurations with gauge-equivariant flow models | 0.4 | citation_only | `paper:2606.13790 -> paper:2107.00734 -> paper:2208.03832` |
| 29 | Generative Diffusion Models for Lattice Field Theory | 0.4 | citation_only | `paper:2606.13790 -> paper:2502.05504 -> paper:2311.03578` |
| 30 | Sampling SU(3) pure gauge theory with Stochastic Normalizing Flows | 0.4 | citation_only | `paper:2606.13790 -> paper:2412.19109 -> paper:2409.18861` |
| 31 | Sampling Nambu-Goto theory using Normalizing Flows | 0.5 | citation_only | `paper:2606.13790 -> paper:2201.08862 -> paper:2309.14983` |
| 32 | Simulating the Hubbard Model with Equivariant Normalizing Flows | 0.5 | citation_only | `paper:2606.13790 -> paper:1904.12072 -> paper:2501.07371` |
| 33 | A scalable flow-based approach to mitigate topological freezing | 0.5 | citation_only | `paper:2606.13790 -> paper:1904.12072 -> paper:2601.20708` |
| 34 | Machine learning for four-dimensional SU(3) lattice gauge theories | 0.5 | citation_only | `paper:2606.13790 -> paper:2003.06413 -> paper:2604.12416` |
| 35 | Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality | 0.5 | citation_only | `paper:2606.13790 -> paper:2003.06413 -> paper:2604.10209` |
| 36 | The critical slowing down in diffusion models | 0.5 | citation_only | `paper:2606.13790 -> paper:2110.02673 -> paper:2605.12597` |
| 37 | SCORENF: Score-based Normalizing Flows for Sampling Unnormalized distributions | 0.7 | citation_only | `paper:2606.13790 -> paper:2003.06413 -> paper:2604.10209 -> paper:2510.21330` |

## Interpretation boundary

A citation-only path is supported by exact arXiv identifiers in current
full text. Author and method bridges are navigation aids and are never
reported as direct citation ancestry. Dijkstra distance is not evidence
that a scientific claim is true.
