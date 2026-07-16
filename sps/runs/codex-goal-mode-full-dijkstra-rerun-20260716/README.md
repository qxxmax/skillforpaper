# Fresh SPS Part 1 Rerun

This directory is a new, independent Part 1 literature-research run for the
verbal clue `SPS / stochastic path sampler`. It was started on 2026-07-16 in
Codex Goal mode.

The prior 2026-07-13 SPS package is a historical comparison point only. This
run retrieves its own source metadata, preserves raw route responses, rebuilds
the candidate pool, and rechecks every C3/C4 source used in its final report.

The workflow is:

1. Fetch a root identity record and multi-round candidate routes from arXiv.
2. Gate candidates with C0-C2 checks before selecting full texts.
3. Download and read selected current PDFs for C3/C4 records.
4. Build source, claim, keyword, lineage, gap, and audit ledgers.
5. Run Dijkstra on the resulting navigation graph and compare it with a
   non-Dijkstra ranking at equal review budgets.

The graph is navigation metadata. It is never used as scientific evidence.

## Public export boundary

The local run preserved raw arXiv responses, downloaded PDFs, extracted text,
and transport-debug logs while the audit was being built. Those files are not
published. The GitHub packet keeps the query and retrieval tables, checksums,
screening decisions, C3/C4 ledgers, comparison tables, selected source-page
screenshots, rendered graphs, stopping record, and validation report.
