# Research State

## Project

**Research question:** Map the predecessor and adjacent-method landscape of
"Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790):
learned/neural samplers for unnormalized target distributions, learned
samplers for lattice field theory, and the correction/exactness mechanisms
they use.
**Primary intent:** cover
**Secondary intent:** learn
**Risk level:** medium (benchmark; missed families reduce score, fabrication is disqualifying)
**Current round:** R0005 (final)
**Current status:** stopped

## Scope

See `search_scope.md` (authoritative). Summary: three facets — F1 learned
samplers for unnormalized targets, F2 learned samplers for lattice field
theory, F3 correction/exactness mechanisms. Time span ~2015–2026, arXiv-centric.

## Budget Mirror (authoritative counter = round_log.md call ledger)

- HARD CAP: 40 web calls (searches + fetches + PDF downloads; failures count)
- Calls used: 24/40 (1 failed call — S2 429 at row 11 — counted)
- C3 gate: 9 core PDFs in sources/pdfs/ with integrity notes (E0002, E0006–E0013) — gate ≥6 satisfied
- Channels required: ≥3 distinct; covered: arXiv (page + API), Semantic Scholar API, INSPIRE-HEP API, general web search (4 families)

## Root Configuration For Graph

graph_mode OFF for this run (per task). No graph files produced.
**Root node(s):** arXiv:2606.13790 (identity pending verification)

## Current Optimization Target

Cover: maximize recall + facet coverage + verification − call cost − missed risk.

## Current Next Best Action

**Action:** none — run stopped; if reopened, first verify the 9 remaining C1(bib-of-C3) single-source IDs and expand G2 (co-citation/author) generations
**Required user input:** none

## Stop Status

**Current stop status:** saturated_under_budget
**Reason:** two consecutive discovery rounds with zero new method families; all facets have ≥3 representatives with ≥1 C3 anchor; 4 channel families used; 24/40 calls spent
**Remaining risks:** see coverage_stopping_report.md (non-arXiv ML venues, 2026 indexing lag, 9 single-source C1 entries, unenumerated forward citations of core predecessors)

## Funnel (mirror of coverage_stopping_report.md)

raw ~173 → deduplicated pool 73 → screened include 53 → C3 PDFs 9

## Validator Result

`scripts/validate_run_state.py <run-dir>` executed 2026-08-12:
- profile: literature
- status: **CONSISTENT** (exit code 0)
- Note: a first run reported MISMATCH because the manifest used a wildcard row
  `sources/pdfs/*.pdf`; fixed by listing all 9 PDF files as individual rows,
  then re-ran → CONSISTENT.
