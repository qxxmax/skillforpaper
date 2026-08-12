# Search Route Log

| RouteID | Channel family | QueryID / trigger | Generation | Notes |
|---|---|---|---|---|
| RT001 | arXiv identifier | seed arXiv:2606.13790 | G0 | abs fetch call 1 |
| RT002 | web search | Q001 | G0 | seed identity |
| RT003 | INSPIRE domain DB | literature/3168332 | G0 | seed cross-val |
| RT004 | arXiv lexical (via web) | Q002–Q004 | G1 topic | LFT neural sampler |
| RT005 | arXiv lexical | Q005 | G1 backward | PIS predecessor family |
| RT006 | web / ACM | Q006 | G1 adjacent | trajectory balance (TB) |
| RT007 | arXiv + publisher DOI | Q007 | G1 adjacent | diffusion-as-SQ LFT |
| RT008 | Semantic Scholar API | arXiv:2606.13790 | G1 forward | 3 citing papers metadata |
| RT009 | arXiv abs | Q008–Q011 | G1 | CMCD, flow MCMC, equivariant flow |
| RT010 | arXiv PDF | C3 gate | G0 core reads | 6 PDFs |
| RT011 | INSPIRE | NeuMC Q009 | G2 tooling | package record |
| RT012 | web search | Q010 DDS | G1 ML sampler | 2302.13834 metadata only |

## Channel coverage

| channel | status | calls |
|---|---|---|
| arXiv (abs/html/pdf) | searched | 1,11–13,15–21 + pdf batch |
| INSPIRE-HEP | searched | 3,24 |
| Semantic Scholar | searched | 9 |
| Google Scholar / general web search | searched | 2,4–8,10,14,22,25 |
| Publisher (Springer JHEP DOI via search) | partial metadata | 8 |
| arXiv search UI | **blocked** (403) | 23 |

## Citation generations executed

- **G0:** seed lock.
- **G1 forward:** Semantic Scholar citations (titles only, not all verified).
- **G1 backward:** INSPIRE reference list titles (58 entries, not individually verified).
- **G2 topic:** keyword queries for flow/diffusion/SNF/NeuMC.

Not executed: G2 co-citation, G3 bridge, full author-network expansion for Albergo/Rezende/Aarts clusters.
