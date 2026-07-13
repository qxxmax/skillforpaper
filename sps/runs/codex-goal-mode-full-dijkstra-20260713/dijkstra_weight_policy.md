# Dijkstra Weight Policy

## Candidate pass

- Root-to-query costs encode route cost: exact/root and backward routes are
  cheaper than keyword, adjacent, adversarial, or extension routes.
- Query-to-paper cost is `0.25 + log(1 + rank)/2.5 + source_penalty`.
- arXiv and the live root bibliography have zero source penalty; OpenAlex and
  Crossref carry small metadata penalties.
- Paper-author and author-paper edges permit auditable coauthor expansion.
- Paper-facet and facet-paper edges permit a higher-cost topic bridge.
- Screening score is not an edge weight. It is used only as a relevance gate
  and a small secondary reading-priority term.

All weights are positive, so ordinary Dijkstra assumptions hold. Distances
rank inspection cost only and cannot promote a candidate to evidence.


## Verified graph pass

- citing paper to cited ancestor: `0.20` (backward direct-citation traversal);
- cited ancestor to citing paper: `0.30` (forward direct-citation traversal);
- paper to author / author to paper: `0.45 / 0.60`;
- paper to method / method to paper: `0.65 / 0.75`.

Citation edges use exact identifiers extracted from current full text. Author
and method edges are retained as different relation types so that a shortest
path cannot be misreported as citation ancestry.


## Verified graph pass

- citing paper to cited ancestor: `0.20` (backward direct-citation traversal);
- cited ancestor to citing paper: `0.30` (forward direct-citation traversal);
- paper to author / author to paper: `0.45 / 0.60`;
- paper to method / method to paper: `0.65 / 0.75`.

Citation edges use exact identifiers extracted from current full text. Author
and method edges are retained as different relation types so that a shortest
path cannot be misreported as citation ancestry.


## Verified graph pass

- citing paper to cited ancestor: `0.20` (backward direct-citation traversal);
- cited ancestor to citing paper: `0.30` (forward direct-citation traversal);
- paper to author / author to paper: `0.45 / 0.60`;
- paper to method / method to paper: `0.65 / 0.75`.

Citation edges use exact identifiers extracted from current full text. Author
and method edges are retained as different relation types so that a shortest
path cannot be misreported as citation ancestry.
