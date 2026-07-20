#!/usr/bin/env python3
"""Reconcile a literature-run directory against its own state files.

Checks (see references/33_literature_intent_modes_and_state_loop.md):

1. Mandatory quick-scan files exist: output_manifest.md, research_state.md,
   candidate_pool.md, evidence_registry.md, round_log.md.
2. Manifest rows claiming `on_disk` or `verified` have a real file; files in
   the run directory have a manifest row (state write order).
3. The call-ledger count in round_log.md matches the budget mirror in
   research_state.md, when both are present.

Exit code 0 = consistent, 1 = mismatches found. Run this first when resuming
an interrupted run.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MANDATORY_FILES = [
    "output_manifest.md",
    "research_state.md",
    "candidate_pool.md",
    "evidence_registry.md",
    "round_log.md",
]

CLAIMED_PRESENT = {"on_disk", "verified", "generated"}
STATUS_VALUES = {
    "planned",
    "in_progress",
    "on_disk",
    "verified",
    "needs_update",
    "generated",
    "stale",
    "blocked",
    "not_applicable",
}

# Files that never need their own manifest row.
IGNORED_NAMES = {"output_manifest.md"}
IGNORED_SUFFIXES = {".pyc", ".DS_Store"}


def parse_manifest(text: str) -> dict[str, str]:
    """Return {output filename: status} from manifest table rows."""
    entries: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0] in {"Output", "---", ""}:
            continue
        if set(cells[0]) <= {"-", " ", ":"}:
            continue
        name = cells[0].strip("`")
        status_cell = cells[4].lower()
        statuses = [s.strip() for s in re.split(r"[/,]", status_cell) if s.strip()]
        # A template row lists alternatives; a live row has exactly one status.
        status = statuses[0] if len(statuses) == 1 else "template_row"
        entries[name] = status
    return entries


def parse_call_ledger_total(round_log: str) -> int | None:
    """Highest running-total numerator in the call ledger, or row count."""
    in_ledger = False
    max_total = None
    row_count = 0
    for line in round_log.splitlines():
        if re.match(r"##\s+Call Ledger", line):
            in_ledger = True
            continue
        if in_ledger and line.startswith("## "):
            break
        if in_ledger and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not cells or cells[0] in {"#", ""} or set(cells[0]) <= {"-", " ", ":"}:
                continue
            row_count += 1
            match = re.search(r"(\d+)\s*/\s*\d+", cells[-1])
            if match:
                total = int(match.group(1))
                max_total = total if max_total is None else max(max_total, total)
    if not in_ledger:
        return None
    return max_total if max_total is not None else row_count


def parse_state_budget_used(state: str) -> int | None:
    match = re.search(r"[Uu]sed[:\s*]+\**\s*(\d+)", state)
    return int(match.group(1)) if match else None


def validate(run_dir: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    for name in MANDATORY_FILES:
        if not (run_dir / name).is_file():
            errors.append(f"mandatory file missing: {name}")

    manifest_path = run_dir / "output_manifest.md"
    manifest: dict[str, str] = {}
    if manifest_path.is_file():
        manifest = parse_manifest(manifest_path.read_text(encoding="utf-8"))
        if not manifest:
            errors.append("output_manifest.md has no parseable table rows")
        for name, status in manifest.items():
            if status == "template_row":
                warnings.append(f"manifest row '{name}' still lists template alternatives")
                continue
            if status not in STATUS_VALUES:
                warnings.append(f"manifest row '{name}' has unknown status '{status}'")
            if status in CLAIMED_PRESENT and not (run_dir / name).is_file():
                errors.append(
                    f"manifest claims '{name}' is {status} but the file is not on disk"
                )
        on_disk = [
            p.name
            for p in run_dir.iterdir()
            if p.is_file()
            and p.name not in IGNORED_NAMES
            and p.suffix not in IGNORED_SUFFIXES
            and not p.name.startswith(".")
        ]
        for name in sorted(on_disk):
            if name not in manifest:
                errors.append(f"file on disk has no manifest row: {name}")

    round_log_path = run_dir / "round_log.md"
    state_path = run_dir / "research_state.md"
    if round_log_path.is_file():
        ledger_total = parse_call_ledger_total(
            round_log_path.read_text(encoding="utf-8")
        )
        if ledger_total is None:
            warnings.append("round_log.md has no Call Ledger section")
        elif state_path.is_file():
            mirror = parse_state_budget_used(state_path.read_text(encoding="utf-8"))
            if mirror is None:
                warnings.append("research_state.md has no parseable 'Used: n' budget mirror")
            elif mirror != ledger_total:
                errors.append(
                    f"budget mismatch: call ledger says {ledger_total} calls, "
                    f"research_state.md mirrors {mirror} (ledger wins)"
                )

    return {
        "run_directory": str(run_dir),
        "status": "CONSISTENT" if not errors else "MISMATCH",
        "errors": errors,
        "warnings": warnings,
        "manifest_rows": len(manifest),
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
        for err in result["errors"]:
            print(f"  ERROR   {err}")
        for warn in result["warnings"]:
            print(f"  warning {warn}")
    return 0 if result["status"] == "CONSISTENT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
