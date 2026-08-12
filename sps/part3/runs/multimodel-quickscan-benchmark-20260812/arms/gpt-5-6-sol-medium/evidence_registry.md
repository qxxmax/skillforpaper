# Evidence Registry

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | Quote / Extract | Verification level | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0001 | E_FULLTEXT | Focal identity, authors, and direct path-space predecessor family | https://arxiv.org/abs/2606.13790 | Introduction, paragraphs beginning “In the broader machine-learning literature” and “In recent years” | Names PIS, DDS, two optimal-control works, CMCD, and NETS; calls SPS an adaptation of this path-space variational family to LFT. Also surveys flow, diffusion, and autoregressive LFT samplers. | C4 | R0001 | Rendered full arXiv text and bibliography visited in call 1. |
| E0002 | P0002 | E_ABSTRACT | Exact title, authors, arXiv identity, and unnormalized-target sampling role | https://arxiv.org/abs/2111.15141 | title/authors/abstract | PIS draws samples from unnormalized probability density functions using stochastic control. | C2 | R0001 | Visited in call 2. |
| E0003 | P0003 | E_ABSTRACT | Exact title, authors, arXiv identity, and unnormalized-target sampling role | https://arxiv.org/abs/2302.13834 | title/authors/abstract | DDS approximately samples unnormalized densities and estimates normalizing constants. | C2 | R0001 | Visited in call 3. |
| E0004 | P0004 | E_ABSTRACT | Exact title, authors, arXiv identity, and path-space optimal-control role | https://arxiv.org/abs/2211.01364 | title/authors/abstract | Formulates diffusion generative modeling through path-space KL and introduces sampling from unnormalized densities. | C2 | R0001 | Visited in call 4. |
| E0005 | P0005 | E_ABSTRACT | Exact title, authors, arXiv identity, and learned-diffusion role | https://arxiv.org/abs/2307.01198 | title/authors/abstract | Learns controlled diffusions from unnormalized target densities using divergences between time-reversed path measures. | C2 | R0001 | Visited in call 5. |
| E0006 | P0006 | E_ABSTRACT | Exact title, authors, arXiv identity, and bidirectional-drift role | https://arxiv.org/abs/2307.01050 | title/authors/abstract | CMCD uses path-space divergences and adapts both forward and backward diffusion dynamics. | C2 | R0001 | Visited in call 6. |
| E0007 | P0007 | E_ABSTRACT | Exact title, authors, arXiv identity, and non-equilibrium transport role | https://arxiv.org/abs/2410.02711 | title/authors/abstract | NETS samples unnormalized distributions using a learned drift in non-equilibrium transport. | C2 | R0001 | Visited in call 7. |
| E0008 | P0008 | E_ABSTRACT | Exact title, authors, arXiv identity, and learned LFT sampler role | https://arxiv.org/abs/1904.12072 | title/authors/abstract | Data-free flow-based MCMC proposals with MH exactness, tested in 2D phi4. | C2 | R0001 | Visited in call 8. |
| E0009 | P0009 | E_ABSTRACT | Exact title, authors, arXiv identity, and learned LFT sampler role | https://arxiv.org/abs/2309.17082 | title/authors/abstract | Connects diffusion models to stochastic quantization and samples 2D phi4 configurations. | C2 | R0001 | Visited in call 9. |
| E0010 | P0010 | E_ABSTRACT | Exact title, authors, arXiv identity, and learned LFT sampler role | https://arxiv.org/abs/2512.19575 | title/authors/abstract | Data-free variational autoregressive sampling for continuous phi4 with MH corrections. | C2 | R0001 | Visited in call 10. |

## Evidence Rules

- Every claimed predecessor must cite a URL actually visited in a logged web call.
- C0/C1 records cannot support an asserted direct-predecessor relationship.
