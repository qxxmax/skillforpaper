# Evidence Registry

Run: multimodel-quickscan-benchmark-20260812 / arm: fable5-thinking-max

Every verified URL/claim gets one row. Types per reference 33
(E_LINK, E_DOI, E_ABSTRACT, E_FULLTEXT, E_QUOTE, E_METADATA_ONLY).

| EvidenceID | PaperID | Type | Level | URL actually visited | CallLedger# | What it verifies | Date |
|---|---|---|---|---|---|---|---|
| E001 | P00 | E_FULLTEXT | C3 | https://arxiv.org/abs/2606.13790 | 1 | Root paper identity: "Stochastic Path Sampler For Lattice Field Theory", Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou; full HTML text retrieved | 2026-08-12 |
| E002 | P01-P10 | E_QUOTE | C4 (citation context) / C1(bib-of-C4) for cited entries | https://arxiv.org/abs/2606.13790 | 1 | Intro §1 names predecessor families and bibliography lists arXiv IDs: PIS 2111.15141, DDS 2302.13834, CMCD 2307.01050, NETS 2410.02711, optimal-control 2211.01364 & 2307.01198, flow-based MCMC 1904.12072, SNF-noneq 2201.08862, DM-as-SQ 2309.17082; Wu et al. SNF cited without arXiv ID | 2026-08-12 |
| E003 | P01 | E_ABSTRACT | C2 | http://export.arxiv.org/api/query?id_list=2111.15141,... (batch, ledger row 2) | 2 | "Path Integral Sampler: a stochastic control approach for sampling" — Qinsheng Zhang, Yongxin Chen, arXiv:2111.15141 | 2026-08-12 |
| E004 | P02 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Denoising Diffusion Samplers" — Francisco Vargas, Will Grathwohl, Arnaud Doucet, arXiv:2302.13834, ICLR 2023 | 2026-08-12 |
| E005 | P03 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Transport meets Variational Inference: Controlled Monte Carlo Diffusions" — Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken, arXiv:2307.01050 | 2026-08-12 |
| E006 | P04 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "NETS: A Non-Equilibrium Transport Sampler" — Michael S. Albergo, Eric Vanden-Eijnden, arXiv:2410.02711; abstract mentions lattice-field-theory benchmark | 2026-08-12 |
| E007 | P05 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "An optimal control perspective on diffusion-based generative modeling" — Julius Berner, Lorenz Richter, Karen Ullrich, arXiv:2211.01364, TMLR 2024 | 2026-08-12 |
| E008 | P06 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Improved sampling via learned diffusions" — Lorenz Richter, Julius Berner, arXiv:2307.01198, ICLR 2024 | 2026-08-12 |
| E009 | P07 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Flow-based generative models for Markov chain Monte Carlo in lattice field theory" — M. S. Albergo, G. Kanwar, P. E. Shanahan, arXiv:1904.12072, Phys. Rev. D 100, 034515 (2019) | 2026-08-12 |
| E010 | P08 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Stochastic Normalizing Flows" — Hao Wu, Jonas Köhler, Frank Noé, arXiv:2002.06707 (ID absent from SPS bib, independently confirmed here) | 2026-08-12 |
| E011 | P09 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Stochastic normalizing flows as non-equilibrium transformations" — Michele Caselle, Elia Cellini, Alessandro Nada, Marco Panero, arXiv:2201.08862, JHEP 07 (2022) 015 | 2026-08-12 |
| E012 | P10 | E_ABSTRACT | C2 | same batch API call as E003 | 2 | "Diffusion Models as Stochastic Quantization in Lattice Field Theory" — Lingxiao Wang, Gert Aarts, Kai Zhou, arXiv:2309.17082, JHEP 05 (2024) 060 | 2026-08-12 |
