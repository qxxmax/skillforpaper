#!/usr/bin/env python3
"""Convert current-run CSV ledgers to structured JSON for workbook authoring."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SHEETS = [
    ("Sources", "source_matrix.csv"),
    ("Reading Notes", "manual_reading_notes.csv"),
    ("Evidence", "evidence_registry.csv"),
    ("Claims", "claim_source_ledger.csv"),
    ("Numbers", "numerical_ledger.csv"),
    ("Gaps", "gap_ledger.csv"),
    ("Relations Core", "display_relation_ledger.csv"),
    ("Relations All", "relation_ledger.csv"),
    ("Authors", "author_lineage_table.csv"),
    ("Funnel", "audit_funnel_counts.csv"),
    ("Candidates", "candidate_screening_table.csv"),
    ("Search Queries", "query_matrix.csv"),
]

NUMERIC_HEADERS = {
    "year", "pdf_pages", "pages", "bytes", "count", "paper_count",
    "route_occurrences", "score", "page",
}


def typed(header: str, value: str):
    if header in NUMERIC_HEADERS and value.strip():
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    return value


def main() -> None:
    payload: dict[str, object] = {"sheets": {}}
    for sheet_name, filename in SHEETS:
        with (ROOT / filename).open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            headers = list(reader.fieldnames or [])
            rows = [[typed(header, row.get(header, "")) for header in headers] for row in reader]
        payload["sheets"][sheet_name] = {
            "source_file": filename,
            "headers": headers,
            "rows": rows,
        }
    (ROOT / "workbook_data.json").write_text(json.dumps(payload, ensure_ascii=False) + "\n", encoding="utf-8")
    print("; ".join(f"{name}={len(payload['sheets'][name]['rows'])}" for name, _ in SHEETS))


if __name__ == "__main__":
    main()
