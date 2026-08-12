# Literature Matrix

Core rows of the landscape. Every arXiv ID, title, author and journal reference in
this table came from a saved API response (`sources/raw/`), never from recall.

**Evidence discipline for the mechanism column.** Rows marked **[C4]** have the
mechanism sentence located in a downloaded PDF, with the anchor in
`evidence_registry.md`. Rows marked **[C2-abstract]** are described from the
title/abstract returned by the arXiv API: the method family is verified, the
mechanism description is *what the abstract says*, not a full-text check. Rows
marked **[C1-metadata]** have identity only. Nothing here is described from memory.

## F1 — Learned samplers for unnormalized targets (the ML lineage SPS belongs to)

| Work | arXiv | Year / venue | Learned object | Correction / exactness mechanism | Evidence | Relation to SPS |
|---|---|---|---|---|---|---|
| Boltzmann Generators (Noé, Wu et al.) | 1812.01729 | 2018; Science per S2 venue field "arXiv.org" | invertible flow from latent to configuration space | reweighting of flow samples | [C2-abstract], E0015, E0009 | earliest ancestor of "train a sampler for e^{-U}, then correct" |
| Stochastic Normalizing Flows (Wu, Köhler, Noé) | 2002.06707 | 2020; NeurIPS (S2 venue) | flow layers interleaved with stochastic (MC/Langevin) updates | "exact importance weights without having to marginalize out the randomness"; "asymptotically unbiased samples from a target distribution defined up to a normalization" | **[C4]** E0021–E0022, 21 pp | supplies the weight identity that the whole nonequilibrium-flow branch reuses |
| Annealed Flow Transport MC (Arbel, Matthews, Doucet) | 2102.07501 | 2021; ICML | per-temperature transport maps inside SMC | SMC importance weights + resampling | [C2-abstract], E0038/E0007 | annealing-based alternative to a single learned path; **not cited by the seed** |
| CRAFT (Matthews, Arbel, Rezende, Doucet) | 2201.13117 | 2022; ICML | repeated/continual annealed flow transport | same SMC weighting, amortized | [C2-abstract], E0007 | direct competitor family; **not cited by the seed** |
| Flow Annealed IS Bootstrap — FAB (Midgley et al.) | 2208.01893 | 2022; ICLR | flow trained with an AIS-bootstrapped objective | annealed importance sampling weights | [C2-abstract], E0015 | alternative answer to the same mode-collapse problem; **not cited by the seed** |
| Path Integral Sampler (Zhang, Chen) | 2111.15141 | 2021; ICLR | control drift of an SDE from prior to target | "importance weights of the samples to compensate for…"; "can generate unbiased samples over a finite time horizon" | **[C4]** E0023–E0024, 26 pp | the seed's ref [33]; nearest ML ancestor of the path-space objective |
| Denoising Diffusion Samplers (Vargas, Grathwohl, Doucet) | 2302.13834 | 2023; ICLR | reverse-diffusion control for an unnormalized target | "unbiased estimate of Z via the following importance sampling identity" | **[C4]** E0025–E0026, 30 pp | the seed's ref [34]; same data-free premise |
| Optimal-control view of diffusion generative modelling (Berner, Richter, Ullrich) | 2211.01364 | 2022; TMLR | control formulation (DIS) | control/Girsanov identity; importance weights | [C2-abstract], E0005 | the seed's ref [35]; theoretical scaffolding |
| Improved sampling via learned diffusions (Richter, Berner) | 2307.01198 | 2023; ICLR | log-variance objective for learned diffusions | log-variance loss reduces mode collapse; IS-based Z estimate | [C2-abstract], E0005 | the seed's ref [36]; loss-design alternative to entropy-production minimization |
| Controlled Monte Carlo Diffusions (Vargas, Padhy, Blessing, Nüsken) | 2307.01050 | 2023; ICLR | **both** forward and backward drifts | "estimate Z … unbiasedly"; "this implies Jarzynski's equality" | **[C4]** E0027–E0028, 43 pp | the seed itself calls this the work that, "like the present work, learns both the forward and the backward drifts" — the closest ML sibling |
| NETS (Albergo, Vanden-Eijnden) | 2410.02711 | 2024; ICML | learned drift added to an annealed process | "a variant of annealed importance sampling based on Jarzynski's equality"; "shown to be unbiased … tunable diffusion coefficient" | **[C4]** E0029–E0030, 31 pp | the seed's ref [38]; the nonequilibrium-transport formulation closest to SPS's thermodynamic framing |
| iDEM (Akhound-Sadegh et al.) | 2402.06121 | 2024 | energy-matching bootstrap | (abstract-level: iterated denoising energy matching) | [C2-abstract], E0016 | simulation-free alternative; surfaced only via the web→title route |
| Particle Denoising Diffusion Sampler (Phillips et al.) | 2402.06320 | 2024 | particle-based diffusion sampler | particle/SMC correction | [C2-abstract], E0016 | correction-by-particles branch |
| Sequential Controlled Langevin Diffusions (Chen et al.) | 2412.07081 | 2024 | control + SMC hybrid | SMC weights on controlled Langevin | [C2-abstract], E0016 | unifies the two correction families |
| Liouville Flow Importance Sampler (Tian et al.) | 2405.06672 | 2024 | learned velocity field | importance weights | [C2-abstract], E0016 | flow-transport branch |
| Adjoint Sampling (Havens et al.) | 2504.11713 | 2025 | scalable adjoint-matching sampler | (abstract-level) | [C2-abstract], E0016 | 2025 scaling frontier |
| Adjoint Schrödinger Bridge Sampler (Liu et al.) | 2506.22565 | 2025 | Schrödinger-bridge sampler | (abstract-level) | [C2-abstract], E0015 | 2025–26 frontier; benchmarks against PIS/DDS/SCLD/iDEM |
| Improved off-policy training of diffusion samplers (Sendera et al.) | 2402.05098 | 2024 | GFlowNet/diffusion sampler training | trajectory-balance objectives; replay buffers | [C2-abstract], E0015 | the benchmark paper that questions earlier claims — adversarial evidence |
| No Trick, No Treat (He et al.) | 2502.06685 | 2025 | critique of simulation-free neural-sampler training | — | [C2-abstract], E0007 | adversarial evidence against the family SPS joins |
| Annealed Importance Sampling (Neal) | physics/9803008 | 1998 | — (classical) | AIS weights; the origin of the whole weight-based correction family | [C2-abstract], E0038 | root of F3; recovered only by the adversarial title route |
| Nonequilibrium Candidate Monte Carlo (Nilmeier et al.) | 1105.2278 | 2011; PNAS | — (classical) | nonequilibrium proposal + MC acceptance | [C2-abstract], E0038 | the pre-ML statement of "drive a nonequilibrium process, then accept/reject" — structurally what SPS does |
| A-NICE-MC (Song, Zhao, Ermon) | 1706.07561 | 2017 | flow-based MCMC proposal, adversarially trained | Metropolis–Hastings acceptance | [C2-abstract], E0038 | earliest "learned proposal + MH" pattern |
| Independent MH with normalizing-flow proposals (Brofos et al.) | 2110.13216 | 2021; AISTATS | adaptation of an independence sampler | **independence Metropolis–Hastings** | [C2-abstract], E0015 | the ML-side study of exactly the correction SPS uses |

## F2 — Learned samplers for lattice field theory

| Work | arXiv | Year / journal (verified) | Method | Correction / exactness mechanism | Evidence | Relation to SPS |
|---|---|---|---|---|---|---|
| Albergo, Kanwar, Shanahan | 1904.12072 | 2019; Phys. Rev. D 100, 034515; DOI 10.1103/PhysRevD.100.034515 | normalizing flow proposals for φ⁴ | "To guarantee asymptotic exactness … a Markov chain is constructed using Metropolis-Hastings steps with p̃_f taken as a proposal distribution" | **[C4]** E0019–E0020, 13 pp; Crossref E0035 | the founding paper of the field; establishes flow-proposal + MH, the same exactness contract SPS adopts |
| Kanwar et al., equivariant flows | 2003.06413 | 2020; Phys. Rev. Lett. 125, 121601 | gauge-equivariant flows | MH acceptance (abstract-level) | [C2-abstract] + Crossref E0035 | gauge generalization |
| Boyda et al., SU(N) equivariant flows | 2008.05456 | 2020; Phys. Rev. D 103, 074504 | SU(N) flows | MH acceptance (abstract-level) | [C2-abstract], E0038 | the seed cites this **without an eprint number**; recovered by title route |
| Albergo et al., fermionic flows | 2106.05934 | 2021; Phys. Rev. D 104, 114507 | flows with fermion determinants | MH acceptance (abstract-level) | [C2-abstract] + Crossref E0035 | extends the family to dynamical fermions |
| Albergo et al., Schwinger model at criticality | 2202.11712 | 2022; Phys. Rev. D 106, 014514 | flows near criticality | MH acceptance (abstract-level) | [C2-abstract] E0005 | the criticality regime SPS also targets |
| Hackett et al., multimodal / extended-mode | 2107.00734 | 2021 | flow training for multimodal targets | mode-coverage diagnostics | [C2-abstract] E0005 | the mode-collapse failure the seed cites as motivation |
| Nicoli et al., thermodynamic observables | 2007.07115 | 2020; Phys. Rev. Lett. 126, 032001 | deep generative estimation of observables | asymptotically unbiased estimators | [C2-abstract] + Crossref E0035; **title variant across channels**, E0010 | the observable-estimation side of exactness |
| Nicoli et al., asymptotically unbiased neural samplers | 1910.13496 | 2019; Phys. Rev. E 101, 023304 | neural sampler with reweighting | **asymptotically unbiased estimation** | [C2-abstract], E0015 | the direct statement of the F3 contract in a physics venue |
| Nicoli et al., mode collapse | 2302.14082 | 2023 | detection/mitigation of mode collapse | diagnostics, not a correction | [C2-abstract], E0015 | adversarial evidence for the whole flow family |
| Lüscher, trivializing maps | 0907.5491 | 2009; Commun. Math. Phys. 293, 899 | field transformation trivializing the action | exactness by construction of the change of variables | [C2-abstract] + Crossref E0035 | **not cited by the seed**; the pre-ML ancestor of learned transport for lattice actions |
| Del Debbio, Marsh Rossney, Wilson | 2105.12481 | 2021; Phys. Rev. D 104, 094507 | flows as approximate trivializing maps for φ⁴ | MH correction; scalability study | [C2-abstract], E0015 | scalability critique inside the flow family |
| Albandea et al., learning trivializing flows | 2211.12806 / 2302.08408 | 2022–23; EPJC (S2 DOI) | learned trivializing flows | MH; HMC in the trivialized field | [C2-abstract], E0015; probable version pair DEDUP0001 | the trivializing-flow branch |
| Bacchio et al., trivializing gradient flows | 2212.08469 | 2022; Phys. Rev. D 107, L051504 | gradient-flow-based trivialization | exactness by construction + HMC | [C2-abstract], E0015 | gauge-theory version |
| Gerdes et al., non-perturbative trivializing flows | 2410.13161 | 2024; Phys. Rev. D 112, 094516 | non-perturbative trivialization | (abstract-level) | [C2-abstract], E0015 | 2024 state of that branch |
| Caselle, Cellini, Nada, Panero — SNF as nonequilibrium transformations | 2201.08862 | 2022; JHEP 07 (2022) 015; DOI 10.1007/JHEP07(2022)015 | stochastic normalizing flows for lattice models | "the same that underlies out-of-equilibrium simulations based on Jarzynski's equality"; "an exact equality in nonequilibrium statistical mechanics" | **[C4]** E0031–E0032, 32 pp; Crossref E0035; **publisher page** E0036 | the closest *lattice* analogue of SPS's nonequilibrium framing — but weight-based rather than IMH-based |
| Caselle et al., SNF for LFT / effective string / SU(3) | 2210.03139, 2412.19109, 2409.15937, 2412.00200, 2409.18861 | 2022–2025; two with JHEP/PRD refs | SNF applied and scaled | Jarzynski-type weights | [C2-abstract], E0005/E0015 | the sustained programme SPS must be positioned against |
| Wang, Aarts, Zhou — diffusion models as stochastic quantization | 2309.17082 | 2023; JHEP 05 (2024) 060 | diffusion model for LFT, supervised | "…makes the algorithm not exact … This can be remedied by introducing such an accept/reject step" | **[C4]** E0033–E0034, 31 pp; Crossref E0035 | same author circle as the seed; the seed's data-free design is a direct response to this supervised line |
| Aarts/Wang/Zhu/Habibi diffusion line | 2311.03578, 2410.19602, 2502.05504, 2510.01328, 2601.19552 | 2023–2026; several with JHEP refs | diffusion models for lattice gauge theory | supervised training; MH where applied | [C2-abstract], E0005/E0015 | the seed's refs [26], [28], [31] plus two the seed does not cite |
| Other diffusion-for-lattice groups | 2510.26081, 2602.09045, 2605.06134, 2607.08505 | 2025–2026; two with journal refs | group-equivariant / SU(2) / SU(N) / near-criticality diffusion | (abstract-level) | [C2-abstract], E0005/E0015 | shows the branch is crowded in 2026 |
| Fukushima, Kamata — stochastic quantization and diffusion models | 2411.11297 | 2024; J. Phys. Soc. Jpn. 94, 031010 | conceptual link | — | [C2-abstract], E0015 | **not cited by the seed**; same conceptual bridge the seed's title claims |
| Abbott et al., aspects of scaling and scalability | 2211.07541 | 2022 | scaling study of flow-based sampling for lattice QCD | — | [C2-abstract], E0038 | the principal scaling critique; adversarial evidence |
| Komijani, Marinković — poor scaling of generative models | 2301.01504 | 2023 | scaling critique for scalar theories | — | [C2-abstract], E0039 | second independent scaling critique |
| Reviews / entry points | 2101.08176, 2504.18126, 2401.01297, 2303.15136 | 2021–2026; SciPost Lect. Notes 110 for one | introductions and reviews | — | [C2-abstract] | framing checks |

## F3 — Correction and exactness mechanisms, as a taxonomy

Derived from the C4 rows above plus abstract-level rows; each mechanism is listed
with the record where it was actually read.

| mechanism | what it corrects | representative record read in full | SPS's relation |
|---|---|---|---|
| Metropolis–Hastings on flow proposals | proposal/target mismatch, exactly | 1904.12072 [C4] | same contract, but SPS's proposal is a *trajectory*, not a single configuration |
| **Independence** Metropolis–Hastings in an extended space | mismatch at the level of whole paths | 2606.13790 [C4] (the seed itself); studied in 2110.13216 [C2] | the seed's stated mechanism |
| Exact importance weights over stochastic paths | randomness injected between flow layers | 2002.06707 [C4] | SPS's path-measure log-ratio is the same object, used as a *loss* rather than a weight |
| Jarzynski / nonequilibrium work weights | finite-time driving away from equilibrium | 2201.08862 [C4], 2410.02711 [C4], 2307.01050 [C4] | SPS minimizes the entropy production these methods reweight by, then still corrects with IMH |
| Annealed importance sampling + resampling | accumulated weight variance | physics/9803008, 2102.07501, 2201.13117 [C2] | not used by SPS; the main alternative design |
| Asymptotically unbiased estimators / reweighting | observable bias without an accept/reject step | 1910.13496 [C2] | complementary |
| Exactness by construction (trivializing maps) | removes the need for correction if exact | 0907.5491 [C2] | a different answer to the same problem, absent from the seed's citations |
| Accept/reject added to a diffusion model | finite-step-size and training error | 2309.17082 [C4] | the supervised-diffusion precedent inside the seed's own author circle |

## Boundary Statement

This matrix asserts a correction mechanism at full-text level for **9** records
only. For every other row the mechanism cell reflects the abstract as returned by
the arXiv API and is labeled `[C2-abstract]`. Turning those into C4 rows requires
PDF acquisition, which is logged as ERQ0003.
