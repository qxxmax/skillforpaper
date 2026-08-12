# Search Scope

## Task

- Research question / search objective: Map the predecessor and adjacent-method landscape of "Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790), across three facets: (a) learned/neural samplers for unnormalized target distributions, (b) learned samplers for lattice field theory, (c) correction/exactness mechanisms.
- Artifact target: literature landscape record for a multi-model benchmark
- Scan level: full
- Date started: 2026-08-12
- Owner: arm=opus-4-7-xhigh (run=multimodel-fullscan-benchmark-20260812)

## Eligibility

| Field | Definition |
|---|---|
| Relevant item | Peer-reviewed, arXiv, or workshop paper whose contribution is (i) a learned sampler for a density that is only known up to normalization (target density p(x) ∝ exp(−S(x)) or Boltzmann/Gibbs form), and/or (ii) a learned sampler applied to lattice field theory / lattice gauge theory / lattice QCD, and/or (iii) an explicit correction/exactness mechanism (importance reweighting, independent MH, Jarzynski/AIS, non-equilibrium reweighting, exact-flow reweighting, extended-space MH). |
| Exclude even if related | Application-only lattice papers with no learned sampler component; pure MCMC methods without a learned proposal (unless cited as baseline); learned generative models for image/text/speech without exactness or reweighting and without lattice/physics targets. |
| Required evidence type | For confirmed rows: arXiv ID + INSPIRE record OR arXiv ID + DOI/publisher page (two independent metadata sources). For candidate-pool rows: at least a single-channel metadata record (INSPIRE search or arXiv API). |
| Time span | 2017 to present. Older foundational papers (e.g. Parisi-Wu 1981, Jarzynski 2013) admitted only when cited as ancestral by the seed. |
| Language / geography / venue limits | English; hep-lat, hep-ph, cs.LG, stat.ML, cond-mat.stat-mech, JHEP/PRD/PRL/SciPost/TMLR/ICLR/NeurIPS/JMLR. |
| Required identifiers | arXiv (preferred) or DOI. |

## Objective Mode

- Mode: high-recall under bounded budget
- Target recall or coverage: recover the full seed-cited predecessor set (58 references) AND probe INSPIRE/arXiv for pre-seed-date same-topic papers that the seed may have missed.
- Confidence or acceptable residual risk: residual risk = missed non-English or non-arXiv work; missed conference-only work; missed cross-domain papers from applied math or stochastic control literature outside our channels; missed post-June-2026 forward citations (verified as zero at this stop).
- Budget: 40 web calls total (hard cap), shared between searches and fetches.
- Stopping standard: (1) seed identity cross-validated on ≥2 channels; (2) ≥6 core PDFs on disk with integrity notes; (3) ≥3 distinct channels executed; (4) each of the three facets has ≥3 representative confirmed works; (5) forward-citation channel returns 0 citing papers (seed too recent) — recorded as scope limitation, not called complete; (6) budget exhausted or marginal yield from last three queries is decision-neutral.

## Seed Set

| seed item | why relevant | expected source route | recovered? | notes |
|---|---|---|---|---|
| arXiv:2606.13790 (SPS) | the seed itself | arXiv abs; INSPIRE; OpenAlex | yes | verified C2 on 3 channels |
| arXiv:2111.15141 (Zhang & Chen, PIS) | direct method ancestor for Facet A path-space objective | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:2302.13834 (Vargas et al., DDS) | direct method ancestor for Facet A | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:2410.02711 (Albergo & Vanden-Eijnden, NETS) | learn-both-drifts ancestor; SPS explicitly names as "like the present work" | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:1904.12072 (Albergo, Kanwar, Shanahan 2019) | foundational Facet B flow-for-LFT | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:2003.06413 (Kanwar et al. 2020) | equivariant flow for LGT | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:2007.07115 (Nicoli et al. 2021) | thermodynamic observable estimation with reweighted flows (Facet B + C bridge) | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:2201.08862 (Caselle et al. 2022) | Stochastic Normalizing Flows as non-equilibrium transformations (Facet B + C bridge) | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |
| arXiv:2309.17082 (Wang, Aarts, Zhou 2024) | diffusion-as-stochastic-quantization for LFT (Facet A + B bridge) | arXiv abs; INSPIRE ref | yes | C3, PDF on disk |

## Facet Map

| facet | why it matters | minimum evidence needed | current status |
|---|---|---|---|
| A. learned/neural samplers for unnormalized densities | SPS positions itself in this ML lineage (PIS/DDS/NETS/CMCD) | ≥3 confirmed papers with C1+ | ✓ PIS 2111.15141 (C3), DDS 2302.13834 (C3), NETS 2410.02711 (C3), CMCD 2307.01050 (C1), Berner 2211.01364 (C1), Richter-Berner 2307.01198 (C1), IWSM 2505.19431 (C1, potentially missed by seed) |
| B. learned samplers for lattice field theory | direct methodological competitors and predecessors on LFT targets | ≥3 confirmed papers with C1+ | ✓ Albergo 1904.12072 (C3), Kanwar 2003.06413 (C3), Nicoli 2007.07115 (C3), Caselle 2201.08862 (C3), Wang 2309.17082 (C3), plus 15+ additional C1 candidates including several potentially missed by seed |
| C. correction / exactness mechanisms | SPS uses trajectory-extended Independence MH; comparing exactness mechanisms defines the true predecessor set | ≥3 confirmed papers with C1+ | ✓ Independence MH → seed; importance reweighting → Nicoli 2007.07115 (C3), Caselle SNF 2201.08862 (C3) via Jarzynski; NETS 2410.02711 (C3) via annealed non-equilibrium reweighting; Jarzynski 2013 (C1 via INSPIRE); IWSM 2505.19431 (C1 potentially missed) |
