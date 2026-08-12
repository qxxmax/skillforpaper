# Output Manifest

Live run ledger for the fable5 arm of the multi-model full-scan benchmark
(2026-08-12). Created first, before any other run file. Update a row
immediately after its file lands on disk, never before (state write order,
reference 33). At full-scan scale, manifest rows may be batch-updated at the
end of each round, before the round's entry in `round_log.md` references
those files.

Status values: `planned` → `in_progress` → `on_disk` → `verified`, plus
`needs_update`.

## Run Files And Deliverables

| Output | Format | Source files | Evidence requirement | Status | Notes |
|---|---|---|---|---|---|
| output_manifest.md | markdown | — | live run ledger | on_disk | created first |
| research_state.md | markdown | — | mode, scope, budget mirror of round_log | on_disk |  |
| candidate_pool.md | markdown | search rounds | C-level per candidate | on_disk |  |
| evidence_registry.md | markdown | fetched sources | EvidenceID + anchors | on_disk |  |
| round_log.md | markdown | — | call ledger row for every web call, running total n/40 | on_disk |  |
| search_budget_contract.md | markdown | — | actual column backfilled at stop | on_disk |  |
| search_scope.md | markdown | — | eligibility, seeds, facets | on_disk |  |
| search_route_log.md | markdown | round_log.md | route plan + query log | on_disk |  |
| candidate_screening_table.md | markdown | candidate_pool.md | include/exclude/uncertain/monitor labels | on_disk |  |
| coverage_stopping_report.md | markdown | all state files | honest scope-limited stop rationale | on_disk |  |
| keyword_ledger.csv | csv | seed paper + retained papers | source anchors per seed term | on_disk |  |
| query_matrix.csv | csv | keyword_ledger.csv | axis-crossed queries with TermIDs | on_disk |  |
| query_yield_log.csv | csv | round_log.md | per-query yield counts | on_disk |  |
| sources/pdfs/2606.13790_sps.pdf | pdf | web fetch (call 2) | integrity note E0002 | on_disk | seed, 33 pp |
| sources/pdfs/1904.12072_flowmcmc_lft.pdf | pdf | web fetch (call 15) | integrity note E0006 | on_disk | 13 pp |
| sources/pdfs/2111.15141_path_integral_sampler.pdf | pdf | web fetch (call 16) | integrity note E0007 | on_disk | 26 pp |
| sources/pdfs/2002.06707_stochastic_normalizing_flows.pdf | pdf | web fetch (call 17) | integrity note E0008 | on_disk | 21 pp |
| sources/pdfs/2201.08862_snf_noneq_lattice.pdf | pdf | web fetch (call 18) | integrity note E0009 | on_disk | 32 pp |
| sources/pdfs/2309.17082_diffusion_stochastic_quantization.pdf | pdf | web fetch (call 19) | integrity note E0010 | on_disk | 31 pp |
| sources/pdfs/2302.13834_denoising_diffusion_samplers.pdf | pdf | web fetch (call 20) | integrity note E0011 | on_disk | 30 pp |
| sources/pdfs/1812.01729_boltzmann_generators.pdf | pdf | web fetch (call 21) | integrity note E0012 | on_disk | 46 pp |
| sources/pdfs/2309.01156_ml_sampling_latticeqcd_review.pdf | pdf | web fetch (call 22) | integrity note E0013 | on_disk | 11 pp |

## Export Rules

- Claims without EvidenceID go to notes, not main conclusions.
- C0/C1 papers can be listed but not used as strong claim evidence.
- C3/C4 papers can support substantive claims.
- Unverified candidates stay C0/C1 with explicit labels; identities never
  asserted without a logged web call.
