# Key-Only Visual Source Audit

The C3 gate verifies every selected PDF by checksum, page count, and text extraction.
This file adds seven visual anchors for identity and citation inspection; it is not a claim that every source was screenshot.

| Source | Role | Page | Visual check | Screenshot |
|---|---|---|---|---|
| [2606.13790](https://arxiv.org/abs/2606.13790) | root_identity | 1 | title, authors, date/version, and abstract opening | [2606.13790_p1_identity.png](screenshots/2606.13790_p1_identity.png) |
| [2606.13790](https://arxiv.org/abs/2606.13790) | root_direct_citation_page_1 | 30 (printed p. 29) | SPS References beginning and direct citation [5] | [2606.13790_p30_bibliography.png](screenshots/2606.13790_p30_bibliography.png) |
| [2606.13790](https://arxiv.org/abs/2606.13790) | root_direct_citation_page_2 | 31 (printed p. 30) | direct citations [8], [11], [19], and [20] | [2606.13790_p31_bibliography.png](screenshots/2606.13790_p31_bibliography.png) |
| [2606.13790](https://arxiv.org/abs/2606.13790) | root_direct_citation_page_3 | 32 (printed p. 31) | direct citations [25], [32], [33], [34], and [35] | [2606.13790_p32_bibliography.png](screenshots/2606.13790_p32_bibliography.png) |
| [2111.15141](https://arxiv.org/abs/2111.15141) | path_space_control_anchor | 1 | title and abstract method scope | [2111.15141_p1_path_integral_sampler.png](screenshots/2111.15141_p1_path_integral_sampler.png) |
| [2309.17082](https://arxiv.org/abs/2309.17082) | diffusion_anchor | 1 | title and abstract method scope | [2309.17082_p1_diffusion.png](screenshots/2309.17082_p1_diffusion.png) |
| [2607.08505](https://arxiv.org/abs/2607.08505) | forward_neighbor_anchor | 1 | title and abstract scope as a post-root neighbor | [2607.08505_p1_closure.png](screenshots/2607.08505_p1_closure.png) |

The direct-citation entries in `relation_ledger.csv` use the exact title and arXiv identifier in these root bibliography pages.
Their printed page and physical PDF page are explicitly separated.
