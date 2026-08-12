# Candidate Pool

Status legend: confirmed / unconfirmed / excluded / monitor  
C-levels: C0 metadata-only → C1 single-channel → C2 dual-channel identity → C3 PDF on disk → C4 claim-anchored (not claimed here beyond PDF+abs)

| PaperID | Title | Authors (short) | Year | arXiv / DOI | Channels | Status | C-level | Relation to seed | Notes |
|---|---|---|---|---|---|---|---|---|---|
| P000 | Stochastic Path Sampler For Lattice Field Theory | Chen; Qian; Aarts; Lucini; Zhou | 2026 | 2606.13790 | arXiv, INSPIRE, PDF | confirmed | **C3** | **SEED** | Independence MH correction; path-space VFE |
| P001 | Flow-based generative models for MCMC in lattice field theory | Albergo; Kanwar; Shanahan | 2019 | 1904.12072 / 10.1103/PhysRevD.100.034515 | arXiv, INSPIRE, S2, OpenAlex, Crossref, PDF | confirmed | **C3** | foundational flow MCMC LFT | MH/reweight exactness |
| P002 | Introduction to Normalizing Flows for Lattice Field Theory | Albergo et al. (tutorial) | 2021 | 2101.08176 | arXiv, INSPIRE, OpenAlex, PDF | confirmed | **C3** | survey/tutorial neighbor | |
| P003 | Path Integral Sampler: a stochastic control approach for sampling | Zhang; Chen | 2022 | 2111.15141 | arXiv, PDF | confirmed | **C3** | method ancestor (seed cites) | stochastic control / path measure |
| P004 | Denoising Diffusion Samplers | Vargas; Grathwohl; Doucet | 2023 | 2302.13834 | arXiv, PDF | confirmed | **C3** | ML sampler ancestor (seed cites) | importance/weight correction class |
| P005 | Stochastic normalizing flows for lattice field theory | Caselle; Cellini; Nada; Panero | 2022 | 2210.03139 | arXiv, INSPIRE, OpenAlex, PDF | confirmed | **C3** | LFT SNF adjacent | non-eq + NF |
| P006 | Diffusion models as stochastic quantization in lattice field theory | Wang; Aarts; Zhou | 2024 | 2309.17082 | arXiv, INSPIRE, PDF | confirmed | **C3** | same-lab diffusion LFT | SQ lineage with seed authors |
| P007 | Equivariant flow-based sampling for lattice gauge theory | Kanwar et al. | 2020 | 2003.06413 | arXiv, INSPIRE, OpenAlex | confirmed | **C2** | gauge flow neighbor | seed cites; no PDF this run |
| P008 | Stochastic normalizing flows as non-equilibrium transformations | Caselle et al. | 2022 | 2201.08862 | arXiv, INSPIRE | confirmed | **C2** | SNF foundation → LFT | seed cites |
| P009 | Improved sampling via learned diffusions | Richter; Berner | 2024 | 2307.01198 | arXiv | confirmed | **C1** | learned diffusion sampler | seed cites; single-channel title verify |
| P010 | NETS: A Non-Equilibrium Transport Sampler | Albergo; Vanden-Eijnden | 2024 | 2410.02711 | arXiv, INSPIRE | confirmed | **C2** | non-eq transport neighbor | seed cites; cites Albergo |
| P011 | Continual Repeated Annealed Flow Transport Monte Carlo | Matthews et al. | 2022 | 2201.13117 | arXiv, INSPIRE | confirmed | **C2** | AIS/AFT correction family | CRAFT |
| P012 | Learning lattice QFTs with equivariant continuous flows | Gerdes et al. | 2023 | 2207.00283 | arXiv, INSPIRE | confirmed | **C2** | continuous-flow LFT | seed cites |
| P013 | Scaling Up ML for QFT with Equivariant Continuous Flows | de Haan et al. | 2021 | 2110.02673 | arXiv, INSPIRE | confirmed | **C2** | continuous-flow LFT | seed cites |
| P014 | Conditional NF for MCMC in critical region of LFT | (from INSPIRE/OpenAlex) | 2022 | 2207.00980 | arXiv, INSPIRE, OpenAlex | confirmed | **C2** | critical-region flow MCMC | |
| P015 | HMC with Normalizing Flows | (INSPIRE/arXiv) | 2021 | 2112.01586 | arXiv, INSPIRE | confirmed | **C2** | hybrid HMC+flow | |
| P016 | Multiscale Normalizing Flows for Gauge Theories | (arXiv/INSPIRE) | 2024 | 2404.10819 | arXiv, INSPIRE | confirmed | **C2** | gauge NF | |
| P017 | Learning Trivializing Flows in φ⁴ from coarser lattices | (arXiv/INSPIRE) | 2023 | 2310.03381 | arXiv, INSPIRE | confirmed | **C2** | trivializing flows φ⁴ | cites Albergo |
| P018 | Stochastic Normalizing Flows (NeurIPS foundation) | Wu; Köhler; Noé | 2020 | 2002.06707 / 2002.09547 | arXiv | confirmed | **C1** | SNF method ancestor | two arXiv ids in SNF search — treat as SNF family; verify which is canonical before strong cite |
| P019 | ScoreNF: Score-based NFs for Sampling Unnormalized distributions | (arXiv/INSPIRE) | 2025 | 2510.21330 | arXiv, INSPIRE | confirmed | **C2** | unnormalized-target facet | |
| P020 | Neural Non-Equilibrium HMC for Corrected Boltzmann Sampling | (INSPIRE/S2) | 2026 | 2607.15682 | INSPIRE, S2 | confirmed | **C2** | cites seed + Albergo | correction-focused neighbor |
| P021 | Diffusion Models for Sampling Near Criticality in LFT | (INSPIRE) | 2026 | 2607.08505 | INSPIRE | confirmed | **C1** | cites seed | single-channel |
| P022 | Stochastic Quantization as Optimal Control | (INSPIRE) | 2026 | 2607.21436 | INSPIRE | confirmed | **C1** | cites seed | single-channel |
| P023 | Physics-conditioned diffusion models for lattice gauge theory | Zhu; Aarts; Wang; Zhou; Wang | 2025 | 2502.05504 | INSPIRE | confirmed | **C1** | Zhou/Aarts lineage | |
| P024 | Estimation of Thermodynamic Observables… Deep Generative Models | Nicoli et al. | 2021 | 2007.07115 | seed PDF refs | confirmed | **C1** | seed-cited LFT generative | identity from seed refs+arXiv id in PDF; not re-fetched |
| P025 | Flow-based sampling for fermionic lattice field theories | Albergo et al. | 2021 | 2106.05934 | seed PDF refs | confirmed | **C1** | seed-cited | |
| P026 | Regressive and generative NNs for scalar field theory | Zhou et al. | 2019 | 1810.12879 | seed PDF refs + INSPIRE Zhou | confirmed | **C2** | early Zhou LFT ML | |
| P027 | Continuous-Mixture Autoregressive Networks… KT Transition | Wang; Jiang; He; Zhou | 2022 | 2005.04857 | INSPIRE Zhou | confirmed | **C1** | autoregressive lattice sampler | |
| P028 | Operator Spectroscopy of Trained Lattice Samplers | Qian | 2026 | 2605.11199 | INSPIRE, seed refs | confirmed | **C1** | same-author adjacent | |
| P029 | Exploring Generative Networks for Manifolds with Non-Trivial Topology | Chen; Aarts; Lucini | 2025 | 2502.02127 | seed refs, INSPIRE | confirmed | **C1** | overlapping authors | |
| P030 | Variational Autoregressive Networks Applied to φ⁴ | Qian; Chen | 2025 | 2512.19575 | seed refs | confirmed | **C1** | overlapping authors | |
| P031 | Sampling SU(3) with Stochastic Normalizing Flows | (arXiv SNF) | 2024 | 2409.18861 | arXiv | confirmed | **C1** | SNF gauge | |
| P032 | Scaling of SNF in SU(3) LGT | (arXiv SNF) | 2024 | 2412.00200 | arXiv | confirmed | **C1** | SNF gauge scaling | |
| P033 | Adaptive Monte Carlo augmented with normalizing flows | (INSPIRE forward) | 2021 | 2105.12603 | INSPIRE | confirmed | **C1** | NF-augmented MCMC | |
| P034 | Flow Sampling: Learning to Sample from Unnormalized Densities… | (S2 citing Albergo) | 2026 | 2605.03984 | S2 | confirmed | **C1** | unnormalized densities facet | title from S2 only |
| P035 | NeuLat: a toolbox for neural samplers in lattice field theories | (INSPIRE) | — | conf DOI 10.22323/1.453.0286 | INSPIRE | unconfirmed | **C0** | toolkit mention | **no arXiv id in hit**; identity not dual-verified |

## Duplicate / Ambiguity Groups

| Group | Kept | Dropped/flagged | Reason |
|---|---|---|---|
| SNF Wu/Noé 2020 | P018 family | 2002.06707 vs 2002.09547 both in arXiv SNF hits | need title-level disambiguation before BibTeX |
| OpenAlex all-orders QED NF | monitor | duplicate display rows | OpenAlex duplicate |

## Excluded (examples)

| PaperID | Title/signal | Reason |
|---|---|---|
| X001 | Wilson flow in lattice QCD (OpenAlex noise) | not learned sampler |
| X002 | QUANTUM ESPRESSO materials (OpenAlex noise) | out of scope |
| X003 | Many Call-12 diffusion imaging/SAR hits | not unnormalized-target samplers |

## Funnel Snapshot

| Stage | Count |
|---|---:|
| Raw hits (pre-dedup, cumulative logged) | ~510 (dominated by INSPIRE Albergo forward total=239 + arXiv NF total=73 + OpenAlex noisy 20 + other route returns) |
| Deduplicated candidates (unique arXiv/DOI retained in pool+monitor) | 36 pool rows + ~40 monitor overflow not fully listed |
| Screened include (active pool include tier) | 28 |
| Screened monitor | 7+ |
| C3 PDFs on disk | **7** |
| Distinct verified papers with arXiv IDs (C1+ and arXiv present) | **34** (P000–P034 excl. P035) |
