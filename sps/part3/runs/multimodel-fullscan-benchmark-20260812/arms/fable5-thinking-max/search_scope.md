# Search Scope

## Task

- Research question / search objective: Map the predecessor and adjacent-method
  landscape of "Stochastic Path Sampler for Lattice Field Theory"
  (arXiv:2606.13790): (a) learned/neural samplers for unnormalized target
  distributions, (b) learned samplers for lattice field theory, and (c) the
  correction/exactness mechanisms they use.
- Artifact target: literature landscape (benchmark audit package; no final
  polished report requested)
- Scan level: full (graph_mode OFF)
- Date started: 2026-08-12
- Owner: benchmark arm fable5-thinking-max

## Eligibility

| Field | Definition |
|---|---|
| Relevant item | Papers proposing or analyzing learned/neural samplers that target a known unnormalized density (Boltzmann/lattice action), OR learned samplers applied to lattice field theory, OR the correction/exactness mechanism used by such samplers (reweighting, MH accept/reject, AIS/Jarzynski, exact likelihood, SDE/control-based weights) |
| Exclude even if related | Pure generative modeling of data (no unnormalized target), pure VAE/GAN image work, quantum-computing samplers, classical (non-learned) MCMC algorithm papers unless they are the exactness mechanism a learned sampler relies on (those enter as mechanism predecessors) |
| Required evidence type | arXiv/DOI identifier + abstract check (C2) for pool; full PDF (C3) for core set |
| Time span | ~1996 (Jarzynski/AIS mechanism roots) to 2026-08 |
| Language / geography / venue limits | English; ML venues + hep-lat/cond-mat/stat arXiv |
| Required identifiers | arXiv ID preferred; DOI where available |

## Objective Mode

- Mode: high-recall within a hard 40-call budget (scoping-review quality, not systematic-review completeness)
- Target recall or coverage: recover the recognized method families in all 3 facets; ≥3 representative works per facet
- Confidence or acceptable residual risk: residual risk explicitly recorded in coverage_stopping_report.md; no completeness claim
- Budget: 40 web calls total (searches + fetches + PDF downloads); ≤60 screened candidates; ≥6 core PDFs
- Stopping standard: budget exhausted or marginal yield per facet low with lineage recovered; adversarial pass for older/negative/limitation work attempted within budget

## Seed Set

| seed item | why relevant | expected source route | recovered? | notes |
|---|---|---|---|---|
| arXiv:2606.13790 "Stochastic Path Sampler for Lattice Field Theory" | the target paper | arXiv abs + PDF | pending | identity to be verified by fetch |
| Flow-based MCMC for lattice field theory (Albergo/Kanwar/Shanahan line) | canonical learned-sampler-for-LFT predecessor family | arXiv search + citation expansion | pending | hypothesis seed; must verify |
| Stochastic normalizing flows / nonequilibrium (Jarzynski) samplers | closest adjacent mechanism family to a "stochastic path sampler" | arXiv search + citation expansion | pending | hypothesis seed; must verify |
| Path-integral / diffusion / control-based neural samplers for unnormalized targets | adjacent-method family outside LFT | arXiv search | pending | hypothesis seed; must verify |

## Facet Map

| facet | why it matters | minimum evidence needed | current status |
|---|---|---|---|
| F1: learned/neural samplers for unnormalized targets (general) | adjacent-method landscape | ≥3 representatives at C2+, ≥2 at C3 | open |
| F2: learned samplers for lattice field theory | direct predecessor landscape | ≥3 representatives at C2+, ≥2 at C3 | open |
| F3: correction/exactness mechanisms (reweighting, MH, AIS/Jarzynski, SNF, exact weights) | what makes these samplers exact | ≥3 representatives at C2+, ≥2 at C3 | open |
