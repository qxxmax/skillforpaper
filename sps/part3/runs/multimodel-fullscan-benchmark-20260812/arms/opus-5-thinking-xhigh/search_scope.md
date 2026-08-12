# Search Scope

## Task

- **Research question / search objective:** map the predecessor and adjacent-method
  landscape of *Stochastic Path Sampler for Lattice Field Theory* (arXiv:2606.13790)
  across three facets — learned/neural samplers for unnormalized targets, learned
  samplers for lattice field theory, and the correction/exactness mechanisms used.
- **Artifact target:** literature landscape (audit package), not a paper draft.
- **Scan level:** full (`cover` mode), `graph_mode` off.
- **Date started / stopped:** 2026-08-12 (single session).
- **Owner:** benchmark arm `opus-5-thinking-xhigh`.

## Eligibility

| Field | Definition |
|---|---|
| Relevant item | A method, or an analysis of a method, that (F1) learns a sampler/transport/control for a distribution known only up to normalization; or (F2) applies a learned sampler to lattice field or gauge theory; or (F3) supplies the mechanism that makes such a sampler exact, unbiased, or diagnosable. |
| Exclude even if related | Classical stochastic quantization / complex Langevin with no learned component; generative modelling of data distributions; GFlowNet or trajectory-balance work targeting language or vision; ML for collider event generation and phase-space integration. |
| Monitor rather than exclude | Molecular and materials Boltzmann-generator work: same F1 mechanism, different target system. Condensed-matter (Hubbard) flow work: same F2 mechanism, different action. |
| Required evidence type | An identifier (arXiv, DOI) returned by an API response saved under `sources/raw/`. Nothing enters any table on the strength of recall. |
| Time span | No lower bound (oldest include: 1998, physics/9803008). Upper bound: index state on 2026-08-12. |
| Language / geography / venue limits | English-language records only. No venue restriction; preprints are first-class. |
| Required identifiers | arXiv ID preferred; DOI where a published version exists. One INSPIRE record with neither is retained at C1 and excluded from claim use. |

## Objective Mode

- **Mode:** high-recall within a hard 40-call cap.
- **Target coverage:** every method family named in the seed's own related-work
  section must be recovered by at least one route that does **not** descend from
  the seed's bibliography; plus at least one family the seed does not cite.
- **Acceptable residual risk:** index-level gaps (no Google Scholar / OpenAlex /
  Web of Science), and depth-of-reading gaps (most includes read at abstract level).
  Both are named in `missing_risk_report.md`.
- **Budget:** 40 web calls total, searches and fetches alike. Used 29.
- **Stopping standard:** two consecutive rounds with no new method family, seed
  recall demonstrated on an independent route, all required channel families
  searched or marked blocked, and residual risk written down.

## Seed Set

The seed set is the target paper plus the six method families it names in its own
introduction. "Recovered?" means: returned by a route that is not the seed's own
bibliography.

| seed item | why relevant | expected source route | recovered? | notes |
|---|---|---|---|---|
| arXiv:2606.13790 (the paper itself) | root node | identifier + lexical | **yes** — returned independently by Q01 and Q03 | strongest single recall signal in this run |
| normalizing flows for LFT | family 1 named in the seed intro | Q01 lexical, hep-lat | yes | 1904.12072, 2003.06413, 2008.05456 and 25+ others |
| continuous normalizing flows | family 2 | Q01 | yes | 2207.00283, 2110.02673 |
| autoregressive networks | family 3 | Q00-bib only | **partly** — recovered by identifier route; the hep-lat lexical query did not surface 2005.04857 | recorded as a route gap |
| stochastic normalizing flows | family 4 | Q01, Q03 | yes | 2002.06707 (ML origin) and the Caselle/Cellini/Nada/Panero lattice line |
| data-driven GAN / diffusion models for LFT | family 5 | Q12 | yes | 2309.17082, 2311.03578, 2410.19602, 2601.19552, 2602.09045, 2605.06134 |
| path-space variational samplers (PIS/DDS/CMCD/NETS) | family 6, the closest ML ancestors | Q02, Q03, Q13 | yes | all four verified at C1–C4; PIS, DDS, CMCD and NETS read in full |
| a family the seed does **not** cite | novelty stress test | Q01, Q11 | **yes** — the Lüscher trivializing-map lineage (0907.5491 → 2105.12481 → 2112.15532 → 2211.12806/2302.08408 → 2212.08469 → 2410.13161) and the Annealed Flow Transport / CRAFT / FAB line | this is the main coverage gain over a bibliography-only scan |

## Facet Map

| facet | why it matters | minimum evidence needed | current status |
|---|---|---|---|
| F1 learned samplers for unnormalized targets | defines what SPS is, methodologically | ≥3 representative works, ≥2 read in full | **39 includes**, 5 read in full (2111.15141, 2302.13834, 2307.01050, 2410.02711, 2002.06707) |
| F2 learned samplers for lattice field theory | defines the application field and the direct baselines | ≥3 per sub-family (flows, trivializing maps, SNF, diffusion) | **67 includes** spread over 4 sub-families, 3 read in full (1904.12072, 2201.08862, 2309.17082) |
| F3 correction / exactness mechanisms | the axis the task explicitly asks about | mechanism sentence located in the actual text, not inferred | **30 includes**; 9 mechanism sentences anchored at C4; the rest labeled abstract-level |
| adversarial / negative evidence | prevents an over-positive landscape | ≥1 scaling critique, ≥1 failure-mode paper, ≥1 benchmark that questions claims | 2211.07541 (scaling), 2301.01504 (poor scaling), 2302.14082 (mode collapse), 2502.06685 (simulation-free training critique), 2302.04763 (approximate transport maps), 2604.20301 (tempering limits, monitor) |
| reviews / entry points | orientation and framing checks | ≥2 | 2101.08176, 2504.18126, 2401.01297, 2303.15136 |
