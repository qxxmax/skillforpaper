# Round Log

| Round | Input | Action | Result | Decision |
|---|---|---|---|---|
| R0 identity | oral clue | verify title, authors, version, date and files | SPS root fixed | continue |
| R1 root reading | root PDF/source | extract problem, method, references and 24 anchored terms | 36 query routes | continue |
| R2 expansion | query matrix | execute arXiv, OpenAlex, Crossref, author and lineage routes | 667 raw, 593 deduplicated | continue |
| R3 candidate graph | screened pool | run single-source Dijkstra and apply a fixed 30-paper reading budget | 10 papers enter and 10 leave | continue |
| R4 full text | Dijkstra set | verify PDFs and read problem/method/result/limitation | first 30 C4 records | continue |
| R5 gap closure | unresolved criticality/scaling/correction gaps | run G01-G06 and read seven additions | 37 verified papers total | continue |
| R6 verified graph | checked citations/authors/methods | rerun Dijkstra on evidence-bearing graph | all 37 papers reachable; citation paths dominate | stop main scan; monitor forward citations |
