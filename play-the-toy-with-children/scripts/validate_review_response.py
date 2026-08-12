#!/usr/bin/env python3
"""Check a review-response package before the response letter is sent.

Checks (see references/45_review_response_and_revision_loop.md):

1. review_response_matrix.csv parses and has the required columns.
2. Every matrix row has a RowID, a known Class, a known Disposition, and a
   non-empty ResponseSummary; RowIDs are unique.
3. Every row with disposition `revised` references at least one DiffID that
   exists in revision_diff_ledger.md.
4. Every diff-ledger entry whose MatrixRows is not `self` references existing
   matrix rows; DiffIDs are unique.
5. No matrix row is left with status `open` (silence on a reviewer point is a
   blocker).

Exit code 0 = ready, 1 = blockers found.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

MATRIX_NAME = "review_response_matrix.csv"
LEDGER_NAME = "revision_diff_ledger.md"

REQUIRED_COLUMNS = {
    "RowID",
    "Reviewer",
    "CommentQuote",
    "Class",
    "Disposition",
    "ResponseSummary",
    "DiffRefs",
    "Status",
}
KNOWN_CLASSES = {
    "factual_error_ours",
    "misread",
    "scope_request",
    "new_experiment",
    "citation_request",
    "subjective",
}
KNOWN_DISPOSITIONS = {
    "revised",
    "declined_with_reason",
    "clarified_in_response",
    "pending",
}
EMPTY_REFS = {"", "-", "—", "none", "n/a"}


def read_matrix(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - fieldnames
        if missing:
            errors.append(
                f"{path.name} missing columns: {', '.join(sorted(missing))}"
            )
            return [], errors
        rows = [
            {k: (v or "").strip() for k, v in row.items()}
            for row in reader
            if any((v or "").strip() for v in row.values())
        ]
    return rows, errors


def read_diff_ledger(path: Path) -> tuple[dict[str, str], list[str]]:
    """Return {DiffID: MatrixRows cell} from the ledger's Markdown tables."""
    entries: dict[str, str] = {}
    errors: list[str] = []
    header: list[str] | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if cells and set(cells[0]) <= {"-", " ", ":"}:
            continue
        if header is None:
            header = cells
            continue
        row = dict(zip(header, cells))
        diff_id = row.get("DiffID", "").strip("`")
        if not diff_id:
            continue
        if diff_id in entries:
            errors.append(f"duplicate DiffID in {path.name}: {diff_id}")
        entries[diff_id] = row.get("MatrixRows", "").strip()
    return entries, errors


def split_refs(cell: str) -> list[str]:
    if cell.strip().lower() in EMPTY_REFS:
        return []
    return [r.strip().strip("`") for r in cell.replace(";", ",").split(",") if r.strip()]


def validate(matrix_path: Path, ledger_path: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    rows, matrix_errors = read_matrix(matrix_path)
    errors.extend(matrix_errors)
    if not rows and not matrix_errors:
        errors.append(f"{matrix_path.name} has no data rows")

    diff_entries: dict[str, str] = {}
    if ledger_path.is_file():
        diff_entries, ledger_errors = read_diff_ledger(ledger_path)
        errors.extend(ledger_errors)
    else:
        warnings.append(f"{LEDGER_NAME} not found; `revised` rows cannot be checked")

    row_ids: set[str] = set()
    for row in rows:
        row_id = row["RowID"]
        if not row_id:
            errors.append("matrix row with empty RowID")
            continue
        if row_id in row_ids:
            errors.append(f"duplicate RowID: {row_id}")
        row_ids.add(row_id)

        if row["Class"] not in KNOWN_CLASSES:
            errors.append(f"{row_id}: unknown class '{row['Class']}'")
        if row["Disposition"] not in KNOWN_DISPOSITIONS:
            errors.append(f"{row_id}: unknown disposition '{row['Disposition']}'")
        if not row["ResponseSummary"]:
            errors.append(f"{row_id}: empty ResponseSummary")
        if row["Status"].lower() != "done":
            errors.append(f"{row_id}: status is '{row['Status']}', not 'done'")
        if row["Disposition"] == "pending":
            errors.append(f"{row_id}: disposition still 'pending'")

        refs = split_refs(row["DiffRefs"])
        if row["Disposition"] == "revised":
            if not refs:
                errors.append(f"{row_id}: disposition 'revised' but no DiffRefs")
            for ref in refs:
                if diff_entries and ref not in diff_entries:
                    errors.append(f"{row_id}: DiffRef '{ref}' not in {LEDGER_NAME}")

    for diff_id, matrix_cell in diff_entries.items():
        if matrix_cell.lower() in EMPTY_REFS | {"self"}:
            continue
        for ref in split_refs(matrix_cell):
            if ref not in row_ids:
                errors.append(
                    f"{LEDGER_NAME} entry {diff_id} references unknown matrix row '{ref}'"
                )

    return {
        "matrix": str(matrix_path),
        "diff_ledger": str(ledger_path) if ledger_path.is_file() else None,
        "status": "READY" if not errors else "BLOCKED",
        "matrix_rows": len(rows),
        "diff_entries": len(diff_entries),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "run_directory",
        type=Path,
        help=f"directory containing {MATRIX_NAME} and {LEDGER_NAME}",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    args = parser.parse_args()

    matrix_path = args.run_directory / MATRIX_NAME
    if not matrix_path.is_file():
        print(f"error: {matrix_path} not found", file=sys.stderr)
        return 2
    ledger_path = args.run_directory / LEDGER_NAME

    result = validate(matrix_path, ledger_path)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"matrix: {result['matrix']}")
        print(f"status: {result['status']}")
        print(f"rows:   {result['matrix_rows']} matrix, {result['diff_entries']} diffs")
        for err in result["errors"]:
            print(f"  ERROR   {err}")
        for warn in result["warnings"]:
            print(f"  warning {warn}")
    return 0 if result["status"] == "READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
