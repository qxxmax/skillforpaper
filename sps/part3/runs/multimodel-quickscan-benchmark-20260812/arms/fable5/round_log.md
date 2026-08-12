# Round Log

Run: multimodel-quickscan-benchmark-20260812 / arm fable5
Budget: 10 web calls (searches + fetches). This ledger is the authoritative counter.

## Call Ledger

| # | RoundID | type | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0002 | fetch | https://arxiv.org/abs/2606.13790 | full HTML text of focal paper: title, authors, abstract, intro, bibliography; 10 predecessor candidates extracted | 1/10 |
| 2 | R0003 | fetch | https://arxiv.org/abs/2111.15141 | P01 verified: "Path Integral Sampler: a stochastic control approach for sampling", Qinsheng Zhang, Yongxin Chen | 2/10 |
| 3 | R0003 | fetch | https://arxiv.org/abs/2302.13834 | P02 verified: "Denoising Diffusion Samplers", Francisco Vargas, Will Grathwohl, Arnaud Doucet | 3/10 |
| 4 | R0003 | fetch | https://arxiv.org/abs/2307.01050 | P03 verified: "Transport meets Variational Inference: Controlled Monte Carlo Diffusions", Vargas, Padhy, Blessing, Nüsken | 4/10 |
| 5 | R0003 | fetch | https://arxiv.org/abs/2410.02711 | P04 verified: "NETS: A Non-Equilibrium Transport Sampler", Michael S. Albergo, Eric Vanden-Eijnden | 5/10 |
| 6 | R0003 | fetch | https://arxiv.org/abs/2211.01364 | P05 verified: "An optimal control perspective on diffusion-based generative modeling", Julius Berner, Lorenz Richter, Karen Ullrich | 6/10 |
| 7 | R0003 | fetch | https://arxiv.org/abs/1904.12072 | P07 verified: "Flow-based generative models for Markov chain Monte Carlo in lattice field theory", M. S. Albergo, G. Kanwar, P. E. Shanahan | 7/10 |
| 8 | R0003 | fetch | https://arxiv.org/abs/2309.17082 | P08 verified: "Diffusion Models as Stochastic Quantization in Lattice Field Theory", L. Wang, G. Aarts, K. Zhou | 8/10 |
| 9 | R0003 | fetch | https://arxiv.org/abs/2002.06707 | P09 verified: "Stochastic Normalizing Flows", Hao Wu, Jonas Köhler, Frank Noé; arXiv ID (absent from SPS bib) confirmed as 2002.06707 | 9/10 |
| 10 | R0003 | fetch | https://arxiv.org/abs/2201.08862 | P10 verified: "Stochastic normalizing flows as non-equilibrium transformations", Michele Caselle, Elia Cellini, Alessandro Nada, Marco Panero | 10/10 |

## Rounds

### R0001 — setup

- Diagnosis: no state yet; focal paper identity unverified.
- Action: created run directory and five mandatory state files in write order
  (output_manifest.md first).
- Result: state files on disk; 0/10 calls used.
- Next step: fetch focal paper arXiv abs page.

### R0002 — focal paper identity + reference extraction

- Diagnosis: focal paper unverified; predecessor list unknown.
- Action: 1 fetch (ledger row 1) of arxiv.org/abs/2606.13790, which returned
  the full HTML paper text including the bibliography.
- Result: focal paper confirmed at C3 ("Stochastic Path Sampler For Lattice
  Field Theory", S. Chen, M. Qian, G. Aarts, B. Lucini, K. Zhou, dated
  2026-08-11). Intro §1 names the direct predecessor families: data-free
  path-space-KL diffusion samplers (PIS, DDS, optimal-control formulations,
  CMCD, NETS) and learned LFT samplers (flow-based MCMC, stochastic normalizing
  flows, diffusion models as stochastic quantization). 10 candidates P01-P10
  registered at C1(bib-of-C3).
- File patches: candidate_pool.md (P00-P10), evidence_registry.md (E01),
  round_log.md (row 1).
- Next step: independently verify predecessors' arXiv abs pages with remaining
  budget, priority P01-P05, P07-P10.

### R0003 — predecessor identity verification

- Diagnosis: 10 predecessor candidates at C1(bib-of-C3); identities need
  independent verification within remaining 9 calls.
- Action: 9 fetches (ledger rows 2-10) of the candidates' own arXiv abs pages,
  covering P01-P05 and P07-P10. P06 deliberately left unfetched (lowest
  priority: same author pair as verified P05, same method family).
- Result: all 9 fetched candidates verified — title and authors on each arXiv
  page match the SPS bibliography entry exactly; P09's arXiv ID, which the SPS
  bibliography omits, confirmed as 2002.06707. Budget exhausted at 10/10.
- File patches: round_log.md (rows 2-10), evidence_registry.md (E02-E10),
  candidate_pool.md (P01-P05, P07-P10 → confirmed C2; P06 stays unconfirmed
  C1), research_state.md (budget mirror 10/10, stop status).
- Next step: run validate_run_state.py and record result; stop.
