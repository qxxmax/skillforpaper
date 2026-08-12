# Research State

## Project

**Research question:** Map the predecessor and adjacent-method landscape of
"Stochastic Path Sampler for Lattice Field Theory" (arXiv:2606.13790):
learned/neural samplers for unnormalized targets, learned samplers for lattice
field theory, and their correction/exactness mechanisms.
**Primary intent:** cover
**Secondary intent:** learn
**Risk level:** high (benchmark-scored: zero fabricated citations; unverified stays C0/C1)
**Current round:** R0006 (final)
**Current status:** stopped

## Scope

See `search_scope.md` (authoritative). Full scan, graph_mode OFF.

### Human Budget

- Max rounds: 6 (all 6 executed)
- Max papers to screen: ~60 (screened records across routes ≈ 430; pooled: 77)
- Max full texts to verify: 8 (8 PDFs on disk incl. seed — C3 gate PASSED)
- Max screenshots to capture: 0 (policy: none; links + PDFs are the provenance)

## Web-Call Budget (mirror)

- HARD CAP: 40. Authoritative counter: call ledger in `round_log.md`.
- Used: 28/40 (27 successful + 1 failed 429 that was retried).

## Root Configuration For Graph

graph_mode OFF — no graph files in this run.
**Root node (conceptual):** arXiv:2606.13790 (verified C3, E0001–E0002)

## Final Funnel

- Raw hits touched across routes: ≈ 4,200 (lexical totalResults 3,979 incl. one noisy 3,762-hit query; 166 citation-channel records; 58 seed refs; 13 INSPIRE checks)
- Records actually screened: ≈ 430 (192 lexical retrieved + 16 adversarial + 166 citation + 58 bib)
- Deduplicated candidate pool: 77 (P0001–P0077)
- Screened include (core + facet-relevant): 59 include (8 of them core C3) / 18 monitor-tier in pool; + monitor/exclude tails in screening table
- Verified with arXiv IDs: 75 of 77 (2 pre-arXiv mechanism roots stay C1(bib-of-C3), labeled)
- C3 full texts: 8 PDFs in sources/pdfs/ with integrity notes (E0002, E0009–E0015)
- Channels: 4 families — arXiv identifier pages, arXiv API lexical, Semantic Scholar citation graph, INSPIRE-HEP domain DB

## Stop Status

**Current stop status:** stopped_with_known_risk (saturated under budget)
**Reason:** facet quotas exceeded (each facet ≥3 representatives, ≥2 at C3); seed recall passed; whole pool two-source cross-validated; final adversarial round added no new method family. See coverage_stopping_report.md.
**Remaining risks:** GAN-for-LFT line not recovered; C1 metadata-only tail (~65 papers) must pass C2 before being cited in prose; grey literature and non-arXiv venues unsearched; citation counts channel-scoped and dated 2026-08-12.

## Validator Result

`python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py ~/Desktop/skillforpaper/sps/part3/runs/multimodel-fullscan-benchmark-20260812/arms/fable5-thinking-max`
executed at stop (2026-08-12), after fixing two reconciliation findings from the
first pass (manifest rows split to one-path-per-row; budget-mirror wording):
**RESULT: status CONSISTENT, profile literature, no errors, no warnings.**
