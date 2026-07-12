# SPS Literature Research Report

## 1. Object confirmed

The oral clue resolves to **Stochastic Path Sampler For Lattice Field Theory**, Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini and Kai Zhou, arXiv:2606.13790v1, submitted 11 June 2026. The identity is checked against the current arXiv record, source archive and a locally hashed PDF.

## 2. Why this work exists

The target Boltzmann density is known only up to a partition function, while conventional lattice Markov chains become strongly correlated near phase transitions or the continuum limit. Existing learned terminal proposals may require target data, collapse modes or leave large correction weights. SPS instead learns an entire stochastic path from prior to target and asks that forward and auxiliary backward trajectory measures become close.

## 3. What SPS does

1. Parameterize forward and backward Langevin drifts.
2. Minimize a path-space variational free energy, equivalently the paper's entropy-production upper bound.
3. Generate independent forward trajectories and terminal proposals without target-distributed training data.
4. Apply extended-space independence Metropolis-Hastings. This is the correctness gate; the raw proposal is not promoted as exact.
5. Validate magnetization, susceptibility, free energy, acceptance and autocorrelation against HMC in 2D phi4.

The safe headline is: **SPS combines a learned low-irreversibility path with an explicit exactness gate.**

## 4. Method family

The family has four converging branches:

- **Path-space control and diffusion:** Path Integral Sampler, Denoising Diffusion Samplers, Controlled Monte Carlo Diffusions and NETS optimize trajectories or controlled dynamics for unnormalized targets.
- **Flow-based lattice proposals:** normalizing flows move from scalar theory to gauge and fermion systems, with MH or reweighting providing correctness.
- **Stochastic nonequilibrium flows:** learned invertible layers are interleaved with stochastic transitions and corrected through Jarzynski/path weights.
- **Physics-aware diffusion and multiscale models:** symmetry, force information, locality, cross-volume training and coarse-to-fine structure attack the slow modes and scaling problem.

The checked graph is in `graphs/citation_lineage_graph.png`; the broader method map is in `graphs/landscape_map.png`.

## 5. What the literature says about limitations

- Diffusion is not automatically free of critical slowing. In the controlled Gaussian O(n) analysis of arXiv:2605.12597, a one-layer model inherits slowing in training and generation; depth plus locality changes the reported scaling from L^2 to log L.
- Good ESS is not sufficient. Missed tails, zero modes, operator sectors and training cost can change the physical conclusion.
- Exact correction can restore correctness but may consume the apparent speedup. Acceptance, weight variance and correction cost must be measured together.
- Most evidence remains in scalar or Abelian systems. A few 4D SU(3) studies exist, but production-scale dynamical-fermion QCD is not established.
- Cross-volume, multiscale and localized-defect strategies are promising but have different assumptions and cannot be collapsed into one generic scaling claim.

## 6. What can be done next

The most evidence-grounded SPS extensions are:

1. Add momentum/zero-mode and operator-resolved diagnostics before accepting aggregate ESS.
2. Compare architecture depth and physical locality while holding the correction and compute budget fixed.
3. Report observable-level block errors per total GPU-hour, including training, generation and IMH.
4. Test cross-volume or coarse-to-fine SPS paths to amortize training and isolate long-distance modes.
5. Extend in stages from scalar theory to U(1), SU(2), SU(3), then dynamical fermions, preserving an explicit correction gate at every stage.

## 7. Author and collaborator recurrence

Recurring authors are a search route, not proof of method ancestry:

- Alessandro Nada: 6 selected papers (2201.08862;2210.03139;2409.15937;2409.18861;2412.19109;2601.20708)
- Elia Cellini: 6 selected papers (2201.08862;2210.03139;2409.15937;2409.18861;2412.19109;2601.20708)
- Daniel C. Hackett: 5 selected papers (2003.06413;2106.05934;2107.00734;2208.03832;2211.07541)
- Denis Boyda: 5 selected papers (2003.06413;2106.05934;2107.00734;2208.03832;2211.07541)
- Michael S. Albergo: 5 selected papers (2003.06413;2106.05934;2107.00734;2208.03832;2211.07541)
- Phiala E. Shanahan: 5 selected papers (2003.06413;2106.05934;2107.00734;2208.03832;2211.07541)
- Gert Aarts: 4 selected papers (2311.03578;2502.05504;2606.13790;2607.08505)
- Gurtej Kanwar: 4 selected papers (2003.06413;2106.05934;2107.00734;2208.03832)
- Michele Caselle: 4 selected papers (2201.08862;2210.03139;2409.15937;2412.19109)
- Sébastien Racanière: 4 selected papers (2003.06413;2106.05934;2208.03832;2211.07541)
- Danilo Jimenez Rezende: 3 selected papers (2003.06413;2208.03832;2211.07541)
- Julian M. Urban: 3 selected papers (2106.05934;2208.03832;2211.07541)

## 8. Audit boundary

This run executed 36 first-round routes and a gap-driven closure round, screened 594 deduplicated candidates, and manually read 31 verified PDFs (731 pages). The scan stops because every declared facet has full-text evidence and closure produced no second new family. SPS forward citations remain a monitor item because the preprint is recent.

The package does **not** claim absolute completeness, production-QCD readiness, or a universal speedup.
