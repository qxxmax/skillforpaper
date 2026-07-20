# Round Log

Each round records diagnosis, action, result, file updates, and next step.

## Call Ledger

This table is the only authoritative budget counter; the budget line in
`research_state.md` mirrors it. One search query = one call, one URL fetch =
one call; retries and failed calls count too. Local file reads are free.

| # | RoundID | type (search/fetch) | target | yield | running total |
|---|---|---|---|---|---|
| 1 | R0001 | fetch | https://example.org/abs/XXXX.XXXXX | full text | 1/8 |

## R0001

**Date:**  
**Intent mode:** locate / learn / evaluate / cover  
**Round goal:**  
**Current state summary:**  

### Diagnosis

- Seed recall:
- Topic coverage:
- Author coverage:
- Citation closure:
- Confirmed/unconfirmed ratio:
- Biggest missing risk:

### Chosen Action

**Action:**  
**Why this action was chosen:**  
**Expected gain:**  
**Expected cost:**  

### Execution Result

- New candidates:
- New confirmed papers:
- New unconfirmed papers:
- New excluded papers:
- New EvidenceIDs:
- New graph edges:
- New risks found:

### File Patches

Files updated this round:

- research_state.md:
- candidate_pool.md:
- search_log.md:
- confirmed_literature.md:
- unconfirmed_literature.md:
- evidence_registry.md:
- genealogy_graph.md:
- missing_risk_report.md:

### Next Best Action

**Recommended next action:**  
**Reason:**  
**User input needed:** none / PDF / confirmation / scope choice  

### Stop Decision

**Stop status:** continue / pause_for_human / saturated_under_budget / stopped_with_known_risk  
**Reason:**  
