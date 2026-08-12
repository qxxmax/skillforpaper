# Literature Matrix

| Work / arXiv | Facet | Learned mechanism | Correction / exactness | Evidence | Boundary / relation |
|---|---|---|---|---|---|---|
| SPS | 2606.13790 | path/LFT | paired stochastic drifts; entropy-production/path KL | trajectory IMH | E0002 | support + global-architecture scaling |
| Flow-based generative MCMC in LFT | 1904.12072 | LFT flow | tractable invertible flow proposal | independence MH | E0004 | endpoint-density comparator |
| PIS | 2111.15141 | path/control | Schrödinger control | path importance weights | E0006 | weighted debiasing differs from SPS IMH |
| Stochastic NFs as non-equilibrium transformations | 2201.08862 | SNF/LFT | flows + stochastic updates | Jarzynski reweighting/MH | E0008 | closest thermodynamic transport branch |
| DDS | 2302.13834 | diffusion | learned reverse diffusion | importance weights/unbiased Z | E0010 | endpoint remains approximate without correction |
| CMCD | 2307.01050 | path/control | paired controlled diffusions | Crooks/Jarzynski weights | E0012 | shared paired-drift idea |
| Improved sampling via learned diffusions | 2307.01198 | synthesis | time-reversed path divergences | reweighted estimators | E0014 | unifies PIS/DDS/DIS |
| Diffusion models as SQ in LFT | 2309.17082 | LFT diffusion | supervised score/reverse Langevin | likelihood-based MH | E0016 | same-group data-driven ancestor |
| AFT | 2102.07501 | flow+SMC | learned annealed maps | SMC weights/resampling/MCMC | E0022 | population correction |
| CRAFT | 2201.13117 | flow+SMC | continual annealed transport | SMC/particle MCMC | E0022 | AFT descendant |
| FAB | 2208.01893 | flow+AIS | AIS bootstrap, alpha=2 flow | AIS/reweighting | E0023 | mode-covering training |
| NETS | 2410.02711 | nonequilibrium | learned drift in quench | Jarzynski/Girsanov weights | E0024 | very close adjacent transport |
| SCLD | 2412.07081 | diffusion+SMC | controlled diffusion segments | weights/resampling/MCMC | E0024 | combines CMCD and SMC |
| Reverse diffusion SMC | 2508.05926 | diffusion+SMC | reverse diffusion proposal | SMC bias correction | E0024 | explicit diffusion correction |
| A-NICE-MC | 1706.07561 | neural MCMC | volume-preserving neural proposal | MH | E0025 | older learned exact kernel |
| Generative models for sampling LFT | 2012.01442 | neural MCMC/LFT | self-trained A-NICE | MH | E0025 | older LFT neural proposal |
| Fermionic LFT flow | 2106.05934 | LFT flow | flow with fermionic structure | MH or reweighting | E0021 | fermionic extension |
| Gauge-equivariant flow | 2003.06413 | LFT gauge flow | gauge-equivariant invertible flow | MH | E0021 | gauge extension |
| Multimodal LFT flow | 2107.00734 | LFT flow | mode-aware flow study | MH/reweighting | E0021 | support diagnostics |
| Schwinger critical flow | 2202.11712 | LFT flow | critical fermionic/gauge proposal | MH/reweighting | E0021 | criticality benchmark |
| Equivariant continuous flow | 2207.00283 | LFT CNF | continuous equivariant flow | tractable-density correction | E0021 | CNF branch |
| Flow-based sampling review | 2401.01297 | review | LFT flow taxonomy | MH or p/q weights | E0021 | review framing |
| SNF for LFT | 2210.03139 | SNF/LFT | lattice deployment | nonequilibrium weights | E0018 | C1 only |
| Physics-conditioned LGT diffusion | 2502.05504 | LFT diffusion | physics-conditioned score | reference validation; exact correction unverified | E0018 | C1 only |
| Group-equivariant LFT diffusion | 2510.26081 | LFT diffusion | symmetry-preserving score | empirical ESS/validation | E0021 | data-driven adjacent |
| PDNS | 2510.03824 | diffusion | proximal multimodal training | exactness unverified at C2 | E0020 | recent adjacent |
| Neural non-equilibrium HMC | 2607.15682 | forward adjacent | learned Hamiltonian transport | corrected Boltzmann sampling (details C2) | E0026 | post-SPS |
| Stochastic quantization as optimal control | 2607.21436 | forward adjacent | optimal-control SQ | details C2 | E0026 | post-SPS |
| LEAPS | 2502.10843 | discrete adjacent | learned CTMC rates | path RN weights | E0024 | discrete analogue |
| Boltzmann generators | no independently verified arXiv ID | flow/Boltzmann | equilibrium flow | reweighting/MCMC lineage | E0020 | C1 identity only |
| Stochastic Normalizing Flows | 2002.06707 | stochastic flow | deterministic + stochastic layers | path weighting | E0020 | general predecessor |
