# Round Log

| Round | Input | Action | New information | Decision |
|---|---|---|---|---|
| R0 identity | Oral clue only | Resolve title/authors/date/arXiv and fetch source | SPS = arXiv:2606.13790v1 | continue |
| R1 root extraction | Current SPS source/PDF | Extract 24 anchored terms and 58 references | 36 routes generated | continue |
| R2 expansion | Generated routes | Execute OpenAlex/Crossref/arXiv/author/backward/forward/topic routes | 671 raw records, 594 deduplicated candidates | continue |
| R3 full-text gate | Scored candidates and facet quotas | Select/download/read | 31 verified full texts, 155 evidence entries | continue to gap audit |
| R4 adversarial closure | Gaps from manual reading | Search diffusion criticality, exactness, cost and SPS descendants | Added 2605.12597; no new SPS descendant | stop main scan; monitor forward citations |
