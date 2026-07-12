# Graph Optimizer Evaluation

## Experiment Setup

| field | value |
|---|---|
| case name | |
| research question | |
| inclusion/exclusion rules | |
| seed/sentinel set | |
| token policy | |
| time/search-round budget | |
| candidate screening budget | |
| sources allowed | |
| date | |

## Arms

| arm | strategy | allowed signals | graph allowed? | notes |
|---|---|---|---|---|
| A | one-shot LLM search | model prior + web/search if enabled | no | |
| B | keyword/Boolean only | lexical | no | |
| C | semantic search only | semantic similarity | no | |
| D | high-recall optimizer | lexical + semantic + citation + route log | limited | |
| E | graph optimizer | D + PPR/HITS/path/community/MMR/gates | yes | |

## Metrics

| metric | A | B | C | D | E | interpretation |
|---|---:|---:|---:|---:|---:|---|
| wall-clock minutes | | | | | | |
| estimated tokens | | | | | | |
| sources queried | | | | | | |
| candidates retrieved | | | | | | |
| candidates screened | | | | | | |
| unique included | | | | | | |
| seed recall@k | | | | | | |
| facet coverage | | | | | | |
| route overlap | | | | | | |
| C3/C4 verification yield | | | | | | |
| green-check count | | | | | | |
| lineage ancestors found | | | | | | |
| descendants / follow-ups found | | | | | | |
| bridge papers found | | | | | | |
| redundancy rate | | | | | | |
| residual-risk clarity | | | | | | |

## Stop Decision

| arm | stop reason | remaining risk | next action if continued |
|---|---|---|---|
