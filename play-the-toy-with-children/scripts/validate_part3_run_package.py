#!/usr/bin/env python3
"""Check a Part 3 run package before results are handed to Part 5.

Checks (see references/41_experiment_design_and_run_ledger.md and
references/42_diagnosis_and_claim_promotion_gate.md):

1. Mandatory files exist: experiment_contract.md, compute_budget.md,
   run_ledger.csv, claim_promotion_ledger.md.
2. run_ledger.csv parses with required columns; RunIDs are unique; Status is
   known; failed/crashed/discarded rows keep a Note and an ArtifactPath;
   completed rows have a KeyMetric.
3. claim_promotion_ledger.md rows have unique ClaimIDs, known levels, and
   RunRefs that exist in the run ledger; validated_claim rows have non-empty
   GateNotes.
4. Every ExperimentID in the run ledger is mentioned in
   experiment_contract.md (one file may hold several contracts).

Errors carry rule IDs (FILE/RUN/CLAIM/EXP families) so reports can cite
them per rule. Exit code 0 = consistent, 1 = blockers found.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

MANDATORY_FILES = [
    "experiment_contract.md",
    "compute_budget.md",
    "run_ledger.csv",
    "claim_promotion_ledger.md",
]

LEDGER_COLUMNS = {
    "RunID",
    "ExperimentID",
    "Command",
    "ConfigRef",
    "Seed",
    "Env",
    "Status",
    "KeyMetric",
    "ArtifactPath",
    "Note",
}
KNOWN_STATUSES = {"completed", "failed", "crashed", "killed", "discarded", "running"}
FAILURE_STATUSES = {"failed", "crashed", "discarded"}
KNOWN_LEVELS = {"observation", "candidate_claim", "validated_claim", "retracted"}
EMPTY_CELLS = {"", "-", "—", "n/a", "none"}


def read_run_ledger(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        missing = LEDGER_COLUMNS - set(reader.fieldnames or [])
        if missing:
            errors.append(
                f"RUN001 run_ledger.csv missing columns: {', '.join(sorted(missing))}"
            )
            return [], errors
        rows = [
            {k: (v or "").strip() for k, v in row.items()}
            for row in reader
            if any((v or "").strip() for v in row.values())
        ]
    return rows, errors


def read_claim_tables(path: Path) -> list[dict[str, str]]:
    """Rows from every Markdown table in the file that has a ClaimID column."""
    rows: list[dict[str, str]] = []
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
        if row.get("ClaimID", "").strip("`"):
            rows.append(row)
    return rows


def split_refs(cell: str) -> list[str]:
    if cell.strip().lower() in EMPTY_CELLS:
        return []
    return [r.strip().strip("`") for r in cell.replace(";", ",").split(",") if r.strip()]


def validate(run_dir: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    for name in MANDATORY_FILES:
        if not (run_dir / name).is_file():
            errors.append(f"FILE001 mandatory file missing: {name}")

    run_rows: list[dict[str, str]] = []
    run_ids: set[str] = set()
    experiment_ids: set[str] = set()
    ledger_path = run_dir / "run_ledger.csv"
    if ledger_path.is_file():
        run_rows, ledger_errors = read_run_ledger(ledger_path)
        errors.extend(ledger_errors)
        for row in run_rows:
            run_id = row["RunID"]
            if not run_id:
                errors.append("RUN001 run ledger row with empty RunID")
                continue
            if run_id in run_ids:
                errors.append(f"RUN001 duplicate RunID: {run_id}")
            run_ids.add(run_id)
            experiment_ids.add(row["ExperimentID"])

            status = row["Status"].lower()
            if status not in KNOWN_STATUSES:
                errors.append(f"RUN002 {run_id}: unknown status '{row['Status']}'")
            if status == "running":
                warnings.append(f"{run_id}: still 'running'; finalize before handoff")
            if status in FAILURE_STATUSES:
                if row["Note"].lower() in EMPTY_CELLS:
                    errors.append(f"RUN003 {run_id}: {status} run has no diagnosis Note")
                if row["ArtifactPath"].lower() in EMPTY_CELLS:
                    errors.append(f"RUN003 {run_id}: {status} run has no ArtifactPath")
            if status == "completed" and row["KeyMetric"].lower() in EMPTY_CELLS:
                errors.append(f"RUN004 {run_id}: completed run has no KeyMetric")

    claims_path = run_dir / "claim_promotion_ledger.md"
    claim_rows: list[dict[str, str]] = []
    if claims_path.is_file():
        claim_rows = read_claim_tables(claims_path)
        if not claim_rows:
            warnings.append("claim_promotion_ledger.md has no claim rows")
        claim_ids: set[str] = set()
        for row in claim_rows:
            claim_id = row.get("ClaimID", "").strip("`")
            if claim_id in claim_ids:
                errors.append(f"CLAIM001 duplicate ClaimID: {claim_id}")
            claim_ids.add(claim_id)

            level = row.get("Level", "").strip()
            if level and level not in KNOWN_LEVELS:
                errors.append(f"CLAIM002 {claim_id}: unknown level '{level}'")
            if level == "validated_claim" and row.get("GateNotes", "").strip().lower() in EMPTY_CELLS:
                errors.append(f"CLAIM003 {claim_id}: validated_claim with empty GateNotes")

            for ref in split_refs(row.get("RunRefs", "")):
                if run_ids and ref not in run_ids:
                    errors.append(f"CLAIM004 {claim_id}: RunRef '{ref}' not in run_ledger.csv")

    contract_path = run_dir / "experiment_contract.md"
    if contract_path.is_file() and experiment_ids:
        contract_text = contract_path.read_text(encoding="utf-8")
        for exp_id in sorted(experiment_ids):
            if exp_id and exp_id not in contract_text:
                errors.append(
                    f"EXP001 ExperimentID '{exp_id}' has run ledger rows but no mention "
                    "in experiment_contract.md"
                )

    return {
        "run_directory": str(run_dir),
        "status": "CONSISTENT" if not errors else "MISMATCH",
        "run_rows": len(run_rows),
        "claim_rows": len(claim_rows),
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path)
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    args = parser.parse_args()

    if not args.run_directory.is_dir():
        print(f"error: not a directory: {args.run_directory}", file=sys.stderr)
        return 2

    result = validate(args.run_directory)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"run:    {result['run_directory']}")
        print(f"status: {result['status']}")
        print(f"rows:   {result['run_rows']} runs, {result['claim_rows']} claims")
        for err in result["errors"]:
            print(f"  ERROR   {err}")
        for warn in result["warnings"]:
            print(f"  warning {warn}")
    return 0 if result["status"] == "CONSISTENT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
