# Evidence Registry

| EvidenceID | PaperID | Evidence type | What it verifies | URL / DOI / Source | Page / Section | ScreenshotRef | Quote / Extract | Verification level | Checked by | RoundID | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E0001 | P0000 | E_LINK | Target paper metadata | https://arxiv.org/abs/2606.13790 | abs | — | Title: Stochastic Path Sampler For Lattice Field Theory; authors Chen, Qian, Aarts, Lucini, Zhou | C2 | arXiv fetch | R0001 | Call 1/10 |
| E0002 | P0000 | E_ABSTRACT | Predecessor families named | https://arxiv.org/abs/2606.13790 | §1 | — | Lists PIS, DDS, optimal-control diffusion, CMCD, NETS; LFT flows/CNFs/DMs | C4 | arXiv fetch | R0001 | Direct-build-on claim |
| E0003 | P0001 | E_LINK | PIS identity | https://arxiv.org/abs/2111.15141 | abs | — | Path Integral Sampler; Zhang & Chen | C2 | arXiv fetch | R0001 | Call 2/10 |
| E0004 | P0002 | E_LINK | DDS identity | https://arxiv.org/abs/2302.13834 | abs | — | Denoising Diffusion Samplers; Vargas, Grathwohl, Doucet | C2 | arXiv fetch | R0001 | Call 3/10 |
| E0005 | P0003 | E_LINK | CMCD identity | https://arxiv.org/abs/2307.01050 | abs | — | Controlled Monte Carlo Diffusions; Vargas et al. | C2 | arXiv fetch | R0001 | Call 4/10 |
| E0006 | P0004 | E_LINK | NETS identity | https://arxiv.org/abs/2410.02711 | abs | — | NETS; Albergo & Vanden-Eijnden | C2 | arXiv fetch | R0001 | Call 5/10 |
| E0007 | P0005 | E_LINK | Optimal-control diffusion identity | https://arxiv.org/abs/2211.01364 | abs | — | An optimal control perspective on diffusion-based generative modeling; Berner, Richter, Ullrich | C2 | arXiv fetch | R0001 | Call 6/10 |
| E0008 | P0006 | E_LINK | Learned diffusions identity | https://arxiv.org/abs/2307.01198 | abs | — | Improved sampling via learned diffusions; Richter & Berner | C2 | arXiv fetch | R0001 | Call 7/10 |
| E0009 | P0007 | E_LINK | LFT flow identity | https://arxiv.org/abs/1904.12072 | abs | — | Flow-based generative models for MCMC in LFT; Albergo, Kanwar, Shanahan | C2 | arXiv fetch | R0001 | Call 8/10 |
| E0010 | P0008 | E_LINK | LFT diffusion identity | https://arxiv.org/abs/2309.17082 | abs | — | Diffusion Models as Stochastic Quantization in LFT; Wang, Aarts, Zhou | C2 | arXiv fetch | R0001 | Call 9/10 |
| E0011 | P0009 | E_LINK | LFT CNF identity | https://arxiv.org/abs/2207.00283 | abs | — | Learning LQFT with Equivariant Continuous Flows; Gerdes et al. | C2 | arXiv fetch | R0001 | Call 10/10 |

## Evidence Rules

- `E_LINK` confirms existence or metadata.
- Final reports cite `EvidenceID`, not just `PaperID`.

## Unverified Evidence Requests

| RequestID | PaperID | Needed evidence | Why needed | Suggested action |
|---|---|---|---|---|
| ERQ0001 | P0010 | arXiv or publisher page for Trajectory balance | §2 cites trajectory-level balance foundation | extra fetch round |
| ERQ0002 | P0011 | arXiv:2007.07115 fetch | Nicoli et al. deep generative LFT baseline | extra fetch round |
