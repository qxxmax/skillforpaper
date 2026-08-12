# Search Scope

## Task

- Research question / search objective: Map the predecessor and adjacent-method
  landscape of "Stochastic Path Sampler for Lattice Field Theory"
  (arXiv:2606.13790): (a) learned/neural samplers for unnormalized target
  distributions, (b) learned samplers for lattice field theory, (c) the
  correction/exactness mechanisms they use.
- Artifact target: literature landscape / audit package (benchmark arm)
- Scan level: full (graph_mode OFF)
- Date started: 2026-08-12
- Owner: fable5 benchmark arm

## Eligibility

| Field | Definition |
|---|---|
| Relevant item | Papers proposing or analyzing learned/neural samplers targeting a known unnormalized density (Boltzmann-type, lattice action), OR learned samplers applied to lattice field theory, OR the exactness/correction mechanism used by such samplers (reweighting, MH accept/reject, importance weights, Jarzynski/AIS-type work identities, SDE path-measure weights) |
| Exclude even if related | Generative modeling of data distributions with no unnormalized-target correction story; pure MCMC theory without a learned component; quantum-computing samplers; applications outside the sampler-method lineage (unless a direct lattice baseline) |
| Required evidence type | arXiv ID or DOI verified by a logged web call; C3 requires downloaded PDF in sources/pdfs/ with integrity note |
| Time span | ~2015–2026 (earlier canonical mechanism papers allowed as C0/C1 context) |
| Language / geography / venue limits | English; arXiv-centric fields (hep-lat, stat.ML, cs.LG, cond-mat) |
| Required identifiers | arXiv ID preferred; DOI acceptable |

## Objective Mode

- Mode: high-recall within hard budget (cover)
- Target recall or coverage: all major method families in the three facets;
  ≥3 representative works per major cluster or an explicit reason why fewer
- Confidence or acceptable residual risk: residual risk allowed and reported;
  no completeness claim
- Budget: HARD CAP 40 web calls (searches + fetches + PDF downloads, failures
  count); ≥3 distinct channels; ≥6 core PDFs at C3
- Stopping standard: budget exhaustion or facet saturation (no new method
  family for 2 consecutive rounds), plus honest coverage_stopping_report.md

## Seed Set

| seed item | why relevant | expected source route | recovered? | notes |
|---|---|---|---|---|
| arXiv:2606.13790 "Stochastic Path Sampler for Lattice Field Theory" | the focal paper | arXiv abs page + PDF | yes (calls 1-2, 13) | 3-channel identity (arXiv, INSPIRE; S2 call rate-limited); posted 2026-06-11, page dated 2026-08-11; PDF 33 pp on disk |
| flow-based sampler family for lattice field theory | canonical predecessor family | seed bib + arXiv search + INSPIRE | yes (P0002 etc., calls 1, 3, 10, 14) | 1904.12072 at C3 |
| learned path/diffusion samplers for unnormalized targets | adjacent ML family (seed names it explicitly, E0004) | seed bib + arXiv search | yes (P0030, P0031, P0034, P0035; calls 1, 10, 16, 20) | PIS + DDS at C3 |
| stochastic/annealed correction mechanisms for learned samplers | exactness-mechanism family | seed bib + arXiv search | yes (P0011, P0012; calls 5, 17, 18) | SNF (ML + lattice) at C3 |

## Facet Map

| facet | why it matters | minimum evidence needed | current status |
|---|---|---|---|
| F1: learned/neural samplers for unnormalized targets (general) | predecessor family of SPS | ≥3 works, ≥2 at C2+, ≥1 at C3 | covered: 21 includes; C3 = P0011, P0030, P0031, P0048; families: NF-VI, VAN, Boltzmann generators, SNF, PIS/DDS/DIS/OC, CMCD, NETS, AFT/CRAFT/FAB, GFlowNets, L2HMC, SLMC, adaptive flow-MCMC, benchmark (Beyond ELBOs) |
| F2: learned samplers for lattice field theory | direct application domain of SPS | ≥3 works, ≥2 at C2+, ≥1 at C3 | covered: 32 includes; C3 = P0001, P0002, P0012, P0023, P0065; families: flows (scalar/gauge/fermionic/CNF), SNF-lattice, autoregressive, diffusion-LFT, trivializing maps, learned-HMC, SLMC-lattice, limitation cluster |
| F3: correction/exactness mechanisms | the trust story | each mechanism attached to ≥1 verified paper | covered: independence MH (P0001 E0003, P0002), IS/reweighting (P0008, P0063, P0048), Jarzynski/NEQ-work (P0011, P0012, P0035, P0052), SMC weights/resampling (P0049, P0050), AIS-driven training (P0051), path-measure RN weights / SOC (P0030, P0031, P0032, P0034), trajectory balance (P0036, P0037), exact-MH-inside-learned-kernel (P0057, P0061) |
