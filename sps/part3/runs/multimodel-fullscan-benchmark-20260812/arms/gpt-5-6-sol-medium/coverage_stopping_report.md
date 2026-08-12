# Coverage And Stopping Report

## Summary
- Scan level: full (`cover`, secondary `learn`), graph_mode OFF
- Date: 2026-08-12
- Stop decision: **stop with known risk under budget**
- Funnel: **434 raw route records → 368 deduplicated/screened groups → 31 includes → 8 C3 local PDFs**

## Traversed
- Seed identity and full text; 58 backward references; 3 index-scoped forward citations.
- PIS G1 graph (63 references, 197 citations), then scoped title screening.
- Lexical, domain-archive, domain-database, bibliographic-graph, author, publisher/venue, and adversarial routes.
- Method facets: endpoint normalizing flows; neural MCMC; stochastic/annealed flows; PIS/DDS/CMCD/NETS-type path samplers; SMC/AIS hybrids; data-driven LFT diffusion.
- Correction facets: independence/ordinary MH, extended-space trajectory MH, importance/work/Jarzynski/Girsanov weights, SMC resampling and MCMC rejuvenation.

## Diagnostics
| diagnostic | result | interpretation |
|---|---|---|
| seed recall | 1/1 exact seed in arXiv, INSPIRE, S2 | passed |
| route overlap | all 8 core papers appeared in at least two source/route contexts | adequate for core |
| facet coverage | ≥3 representatives for flow/LFT, path diffusion, and weighted/SMC branches; neural-MCMC boundary has 2 | sufficient with explicit thin-boundary note |
| consecutive closure | R0006 only hydrated known core; R0007 added instances but no new correction family | mechanism taxonomy stable for two focused rounds |
| adversarial pass | older A-NICE-MC; mode collapse/scaling; exactness semantics checked | major challenge classes represented |
| channel closure | arXiv/INSPIRE/S2/web/venue covered; one S2 429 and selective publisher coverage | stop with named blind spots |
| decision sufficiency | further calls likely add instances, not alter MH/weights/SMC taxonomy | stop justified under scope |

## Not Traversed
- Exhaustive abstract/full-text screening of all 368 groups.
- G2/G3 co-citation and bibliographic-coupling traversal; graph_mode was explicitly off.
- Exhaustive publisher/DOI, grey literature, theses, patents, non-English sources, and every 2026 citing paper.
- Full-text verification beyond the 8 core PDFs.

## Reopen Triggers
- A novelty/priority claim requiring exhaustive pre-2026 prior art.
- A reviewer names a missing sampler, exactness theorem, gauge/fermion baseline, or negative scaling study.
- New SPS citations or major revisions appear; Semantic Scholar access resumes; OpenAlex/Scopus/WoS becomes available.
- Need to distinguish “unbiased weighted estimator,” “consistent particle approximation,” and “exact invariant chain” theorem-by-theorem for every included paper.

## Stopping Decision
The scan has auditable, multi-channel coverage for the requested landscape and a stable three-family correction taxonomy, but **does not claim completeness**. Stop at 32/40 calls with the above residual risks; reserve the remaining 8 calls rather than spend them on low-marginal-yield instance accumulation.
