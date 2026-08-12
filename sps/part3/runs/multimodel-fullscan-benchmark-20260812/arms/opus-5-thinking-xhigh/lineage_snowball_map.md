# Lineage Snowball Map

Mandatory for a full scan (reference 18): keyword routes miss continuous work by
the same authors, the same lab, and the same method spectrum. All author names
below come from arXiv/Semantic Scholar/INSPIRE responses saved in `sources/raw/`.

## Seed Authorship

**arXiv:2606.13790** — Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini,
Kai Zhou (E0001). This author list is itself the strongest lineage signal in the
run: three of the five authors appear repeatedly across the lattice-generative
literature returned by independent routes.

## Same-Author / Same-Circle Trail

| author | earlier work found | later work found | how it was found | what it adds |
|---|---|---|---|---|
| Shiyang Chen | 2502.02127 *Exploring Generative Networks for Manifolds with Non-Trivial Topology* (with Aarts, Lucini) | — | seed bibliography [14], verified E0005 | the seed's own prior study of the mode-coverage failure it later corrects with IMH |
| Moxian Qian | 2512.19575 *Variational Autoregressive Networks Applied to φ⁴ Field Theory Systems* (with S. Chen); 2605.11199 *Operator Spectroscopy of Trained Lattice Samplers* (sole author) | 2607.15682 *Neural Non-Equilibrium Hamiltonian Monte Carlo for Corrected Boltzmann Sampling* (sole author) | bibliography [11], [32]; **forward citation** of the seed (E0011) and of NETS (E0040) | a continuous personal programme: autoregressive sampler → diagnostics for trained samplers → the seed → a follow-up that corrects a nonequilibrium proposal. 2607.15682 is the single strongest "same circle, next step" signal in the run |
| Gert Aarts | 2309.17082, 2311.03578, 2410.19602, 2412.13704, 2412.01919, 2410.21212, 2510.01328 | 2601.19552, 2607.08505 | bibliography, Q07 (INSPIRE), Q12 | the supervised-diffusion-for-LFT programme that the seed's data-free design reacts against; Aarts is on both sides |
| Kai Zhou | 1810.12879, 2005.04857, 2211.03470, 2303.15136 (review) | 2309.17082, 2502.05504 | bibliography, Q12 | the GAN/autoregressive/Fourier-flow line and the field review |
| Biagio Lucini | 2502.02127 | 2607.08505 | bibliography, forward citation E0011 | connects the seed to the near-criticality diffusion follow-up |
| Lingxiao Wang | 2005.04857, 2309.17082, 2311.03578 | 2607.21436 *Stochastic Quantization as Optimal Control* | Q12, forward citation of the seed (E0011) | the seed's stochastic-quantization framing is being pushed further by a co-author of its main precursor |

## Same-Lab / Same-Programme Trails (other groups)

| group | records | route | why it matters |
|---|---|---|---|
| Caselle, Cellini, Nada, Panero (Turin) | 2201.08862, 2210.03139, 2409.15937, 2412.19109; with Bulgarelli 2409.18861, 2412.00200; Bonanno et al. 2310.11979, 2402.06561, 2510.25704, 2601.20708 | bibliography + Q01 + Q03 | a decade-long nonequilibrium/Jarzynski programme in lattice field theory. This is the group whose framing is closest to the seed's, and its correction mechanism (work weights) differs from the seed's (IMH) — the sharpest baseline contrast available |
| Albergo, Kanwar, Shanahan, Boyda, Racanière, Rezende, Cranmer, Hackett, Abbott (MIT/DeepMind circle) | 1904.12072, 2003.06413, 2008.05456, 2106.05934, 2202.11712, 2107.00734, 2101.08176, 2211.07541, 2305.02402, 2404.10819, 2502.00263, 2401.01297 | bibliography + Q01 + Q11 | the flow-based lattice programme and its own scaling critique (2211.07541). Note that M. S. Albergo also authors NETS (2410.02711), which is an F1 record — the same person bridges the lattice and ML sides |
| Del Debbio, Marsh Rossney, Wilson (Edinburgh) | 2105.12481, 2112.15532, plus a grey-literature INSPIRE record | Q01 + Q06 | the trivializing-map-as-flow line, including a thesis-type record that only the INSPIRE channel surfaced |
| Albandea, Bacchio, Gerdes and co-authors | 2211.12806, 2302.08408, 2212.08469, 2410.13161, 2601.10774 | Q01 | the trivializing-flow branch the seed does not cite |
| Nicoli, Kessler, Nakajima, Funcke, Jansen and co-authors | 1910.13496, 2007.07115, 2302.14082 | bibliography + Q02 + Q03 | the unbiasedness-and-mode-collapse line: the diagnostic conscience of the field |
| Vargas, Doucet, Blessing, Nüsken, Richter, Berner | 2302.13834, 2307.01050, 2307.01198, 2211.01364, 2208.07698, 2503.01006, 2603.00530 | bibliography + Q02 + Q03 | the ML path-space sampler circle; Doucet also authors AFT (2102.07501), linking the control branch to the annealing branch |
| Bialas, Korcyl, Stebel (NeuMC) | 2308.13294, 2503.11482, 2604.27738 | Q01 | the software/tooling branch, easy to miss with method-only keywords |

## Method-Family Neighbours By Other Groups

- **Exactness by construction**: the Lüscher trivializing-map lineage (0907.5491,
  1102.1852) predates every learned sampler here and answers the same question
  without a Metropolis correction. The seed does not cite it; recovered by Q01/Q11.
- **Annealing rather than a single learned path**: AFT (2102.07501), CRAFT
  (2201.13117), FAB (2208.01893). Not cited by the seed; recovered by Q02.
- **Discrete-state analogues**: LEAPS (2502.10843), MDNS (2508.10684). Same
  path-measure alignment idea on discrete spaces.

## Citing Works That Change Novelty Or Reviewer Risk

| citing work | arXiv | why it matters | verification |
|---|---|---|---|
| Neural Non-Equilibrium Hamiltonian MC for Corrected Boltzmann Sampling | 2607.15682 | cites both the seed and NETS; sole author is a seed co-author; the title states the same "nonequilibrium proposal + correction" contract | C2 (arXiv, E0015) + C1 forward-citation evidence from two S2 queries (E0011, E0041) |
| Diffusion Models for Sampling Near Criticality in Lattice Field Theories | 2607.08505 | Tan, Aarts, Habibi, Lucini, Wang — overlapping authors, same critical-region claim the seed makes | C2 (E0015) + C1 (E0011) |
| Stochastic Quantization as Optimal Control | 2607.21436 | L. Wang alone; pushes the seed's own framing | C2 (E0015) + C1 (E0011) |

## Lineage Verdict Per Record Type

| record | verdict |
|---|---|
| 2201.08862 (Caselle et al. SNF) | **must-cite** — closest lattice nonequilibrium framing, different correction |
| 2307.01050 (CMCD) | **must-cite** — the seed itself flags it as learning both drifts |
| 2410.02711 (NETS) | **must-cite** — nonequilibrium transport with Jarzynski weights |
| 1904.12072 (Albergo et al.) | **must-cite** — origin of flow-proposal + MH exactness in LFT |
| 0907.5491 (Lüscher) | **should-cite, currently uncited** — the exactness-by-construction alternative |
| 2102.07501 / 2201.13117 / 2208.01893 | **should-cite, currently uncited** — the annealing alternative |
| 2110.13216 (independence MH with flow proposals) | **should-cite, currently uncited** — the ML study of the seed's own correction |
| 2607.15682 | **monitor** — same-author follow-up; will change novelty framing |
| Marsh Rossney thesis (no eprint) | **monitor, unverified** — single-channel grey literature |

## Limitation Of This Pass

Author expansion was done from author names appearing in already-retrieved
records, not from a dedicated author-channel query (no ORCID, no author homepage,
no `au:` search was spent from the budget). A same-author paper that no retrieved
record cites and no keyword route matched would still be missed.
