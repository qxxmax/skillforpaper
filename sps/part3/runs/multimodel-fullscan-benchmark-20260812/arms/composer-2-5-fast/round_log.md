# Round Log

## Round R0001 — Initialize full scan

**Diagnosis:** Seed arXiv:2606.13790 identified; need predecessor/adjacent landscape under 40-call cap.

**Action:** Lock seed metadata; open keyword ledger from abstract §1–2; route arXiv + INSPIRE + Semantic Scholar.

**Result:** Seed verified C2 (abstract); 38 deduplicated candidates; 6 C3 PDFs downloaded.

**Next:** Write screening table, coverage report, run validator.

---

## Call Ledger

| # | RoundID | type | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://arxiv.org/abs/2606.13790 | seed abstract, authors, intro refs | 1/40 |
| 2 | R0001 | search | "arXiv:2606.13790 Stochastic Path Sampler Lattice Field Theory" | seed cross-check | 2/40 |
| 3 | R0001 | fetch | https://inspirehep.net/literature/3168332 | INSPIRE record, 58 ref titles | 3/40 |
| 4 | R0001 | search | site:arxiv.org neural sampler lattice field theory Metropolis-Hastings learned | NeuMC, multilevel, flow review hits | 4/40 |
| 5 | R0001 | search | normalizing flow lattice gauge theory exact sampling arxiv | equivariant flow, proceedings hits | 5/40 |
| 6 | R0001 | search | Path Integral Sampler unnormalized target distribution arxiv | arXiv:2111.15141 PIS | 6/40 |
| 7 | R0001 | search | trajectory level balance neural sampler Metropolis-Hastings arxiv | TB/GFlowNet, SPS HTML hit | 7/40 |
| 8 | R0001 | search | diffusion model lattice field theory stochastic quantization arxiv | arXiv:2309.17082, JHEP DOI | 8/40 |
| 9 | R0001 | fetch | Semantic Scholar API graph/v1/paper/arXiv:2606.13790 | 3 forward cites metadata | 9/40 |
| 10 | R0001 | search | Controlled Monte Carlo Diffusions arxiv unnormalized sampling backward drift | arXiv:2307.01050 CMCD | 10/40 |
| 11 | R0001 | fetch | https://arxiv.org/abs/1904.12072 | Albergo flow+IMH metadata | 11/40 |
| 12 | R0001 | fetch | https://arxiv.org/abs/2309.17082 | diffusion LFT metadata | 12/40 |
| 13 | R0001 | fetch | https://arxiv.org/abs/2111.15141 | PIS metadata | 13/40 |
| 14 | R0001 | search | stochastic normalizing flows lattice field theory arxiv | SNF proceedings, arXiv:2412.00200 | 14/40 |
| 15 | R0001 | pdf | https://arxiv.org/pdf/2606.13790.pdf | 2263775 B, 33 pp | 15/40 |
| 16 | R0001 | pdf | https://arxiv.org/pdf/1904.12072.pdf | 884944 B, 13 pp | 16/40 |
| 17 | R0001 | pdf | https://arxiv.org/pdf/2309.17082.pdf | 2486741 B, 31 pp | 17/40 |
| 18 | R0001 | pdf | https://arxiv.org/pdf/2111.15141.pdf | 2713763 B, 26 pp | 18/40 |
| 19 | R0001 | pdf | https://arxiv.org/pdf/2307.01050.pdf | 3598216 B, 43 pp | 19/40 |
| 20 | R0001 | pdf | https://arxiv.org/pdf/2002.02428.pdf | 2889175 B, 16 pp | 20/40 |
| 21 | R0001 | fetch | https://arxiv.org/abs/2002.02428 | equivariant flow LGT metadata | 21/40 |
| 22 | R0001 | search | NeuMC neural sampling lattice field theories arxiv 2503.11482 | package paper + INSPIRE | 22/40 |
| 23 | R0001 | fetch | https://arxiv.org/search/?query=Denoising+Diffusion+Sampler+unnormalized | **FAILED HTTP 403** | 23/40 |
| 24 | R0001 | fetch | https://inspirehep.net/literature?q=Stochastic%20Path%20Sampler | noisy broad results (not useful) | 24/40 |
| 25 | R0001 | search | Denoising Diffusion Samplers arxiv unnormalized density 2023 | arXiv:2302.13834 metadata | 25/40 |
