# SPS Literature Research Report

## 1. Object confirmed

The oral clue resolves to **Stochastic Path Sampler For Lattice Field Theory**, Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini and Kai Zhou, arXiv:2606.13790v1, submitted 11 June 2026. The current arXiv metadata, source archive and local PDF hash agree. [`E-260613790-I`]

## 2. Why the paper exists

Near criticality, conventional lattice chains develop long autocorrelation times, while learned terminal proposals can miss support or require target data. SPS learns a stochastic path between an easy prior and the unnormalized target, then corrects independent path proposals with extended-space IMH. [`E-260613790-P`, `E-260613790-M`]

## 3. Method lineage

Four branches meet around SPS: path-space stochastic control and diffusion samplers; lattice normalizing-flow proposals with MH or reweighting; stochastic nonequilibrium flows with Jarzynski/path weights; and physics-aware diffusion/multiscale models. The public genealogy uses only checked direct-citation edges; author and method bridges remain navigation metadata.

## 4. Main boundary

Diffusion is not automatically free of critical slowing. In the controlled Gaussian O(n to infinity) study, a one-layer model inherits critical slowing, while added depth/locality changes the reported training scaling. This is a theory boundary, not a universal interacting-field result. [`E-260512597-R`, `E-260512597-L`]

Likewise, high ESS alone cannot establish physical or computational efficiency. Training, proposal generation, exact correction and observable-level uncertainty must be compared together. [`E-221107541-R`, `E-240918861-L`, `E-260410209-R`]

## 5. Dijkstra result

The candidate Dijkstra pass ran on 3,300 nodes and 8,187 weighted edges. Under an equal 30-paper budget it exchanged ten papers relative to relevance-only ranking and retained two more exact root-bibliography papers, but coarse facet coverage stayed unchanged. The gap loop recovered five useful baseline papers and added two new boundary/frontier papers. Therefore Dijkstra is retained as a navigation prior, not as evidence or a completeness guarantee.

## 6. Defensible next directions

1. Add support, tail, momentum and zero-mode diagnostics before promoting aggregate ESS.
2. Compare architecture depth and physical locality under a fixed correction and compute budget.
3. Report observable block errors per total GPU-hour, including training, generation and IMH/reweighting.
4. Test cross-volume, coarse-to-fine and localized-defect paths beyond scalar theory.
5. Extend in stages from scalar models to U(1), SU(2), SU(3) and dynamical fermions while preserving an explicit correction gate.

## 7. Recurring authors as search routes

- Alessandro Nada: 7 selected papers (2201.08862;2210.03139;2309.14983;2409.15937;2409.18861;2412.19109;2601.20708)
- Elia Cellini: 7 selected papers (2201.08862;2210.03139;2309.14983;2409.15937;2409.18861;2412.19109;2601.20708)
- Daniel C. Hackett: 6 selected papers (2003.06413;2101.08176;2106.05934;2107.00734;2208.03832;2211.07541)
- Denis Boyda: 6 selected papers (2003.06413;2101.08176;2106.05934;2107.00734;2208.03832;2211.07541)
- Michael S. Albergo: 6 selected papers (2003.06413;2101.08176;2106.05934;2107.00734;2208.03832;2211.07541)
- Phiala E. Shanahan: 6 selected papers (2003.06413;2101.08176;2106.05934;2107.00734;2208.03832;2211.07541)
- Gert Aarts: 5 selected papers (2309.17082;2311.03578;2502.05504;2606.13790;2607.08505)
- Gurtej Kanwar: 5 selected papers (2003.06413;2101.08176;2106.05934;2107.00734;2208.03832)
- Michele Caselle: 5 selected papers (2201.08862;2210.03139;2309.14983;2409.15937;2412.19109)
- Sébastien Racanière: 5 selected papers (2003.06413;2101.08176;2106.05934;2208.03832;2211.07541)

## 8. Audit boundary

This run executed 36 first-round routes, screened 593 deduplicated candidates, verified and read 37 PDFs (776 pages), registered 185 evidence entries and checked 199 exact-identifier citation edges. It does **not** claim absolute completeness, universal Dijkstra improvement, production-QCD readiness or a universal speedup.
