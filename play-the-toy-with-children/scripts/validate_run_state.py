#!/usr/bin/env python3
"""Reconcile a run directory against its own state files.

Checks (see references/33_literature_intent_modes_and_state_loop.md and the
Minimal Run Contract in SKILL.md):

1. The run profile's mandatory files exist. The profile (literature, part2,
   part3, part5) is auto-detected from marker files and can be overridden
   with --profile; a directory with markers from several parts must satisfy
   the union of their mandatory sets.
2. Manifest rows claiming `on_disk` or `verified` have a real file; files in
   the run directory have a manifest row (state write order). Only top-level
   files are reconciled: subdirectory artifacts (e.g. dijkstra/, sources/,
   scripts_local/) are covered by a manifest row for the directory's key
   output or are treated as internal working data.
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

BASE_FILES = [
    "output_manifest.md",
    "research_state.md",
    "round_log.md",
]

# Mandatory files per run profile, on top of BASE_FILES.
PROFILE_FILES: dict[str, list[str]] = {
    "literature": ["candidate_pool.md", "evidence_registry.md"],
    "part2": [
        "candidate_pool.md",
        "evidence_registry.md",
        "part2_learning_contract.md",
    ],
    "part3": [
        "experiment_contract.md",
        "compute_budget.md",
        "run_ledger.csv",
        "claim_promotion_ledger.md",
    ],
    "part5": ["claim_evidence_ledger.md"],
    "part6": [
        "presentation_contract.md",
        "slide_claim_map.csv",
        "figure_provenance.md",
        "qa_bank.md",
    ],
}

# Marker files whose presence pulls a profile into the mandatory union.
PROFILE_MARKERS: dict[str, list[str]] = {
    "part2": ["part2_learning_contract.md", "part2_learning_report.md"],
    "part3": [
        "experiment_contract.md",
        "run_ledger.csv",
        "claim_promotion_ledger.md",
        "compute_budget.md",
    ],
    "part5": [
        "submission_package_manifest.md",
        "review_response_matrix.csv",
        "revision_diff_ledger.md",
    ],
    "part6": ["presentation_contract.md", "slide_claim_map.csv"],
}


def detect_profiles(run_dir: Path) -> list[str]:
    """Profiles pulled in by marker files; literature when nothing else matches."""
    detected = [
        profile
        for profile, markers in PROFILE_MARKERS.items()
        if any((run_dir / marker).is_file() for marker in markers)
        or (profile == "part5" and list(run_dir.glob("venue_profile*.md")))
    ]
    return detected or ["literature"]


def mandatory_files(profiles: list[str]) -> list[str]:
    names = list(BASE_FILES)
    for profile in profiles:
        for name in PROFILE_FILES[profile]:
            if name not in names:
                names.append(name)
    return names

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


def validate(run_dir: Path, profile: str | None = None) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    profiles = [profile] if profile else detect_profiles(run_dir)
    for name in mandatory_files(profiles):
        if not (run_dir / name).is_file():
            errors.append(f"mandatory file missing ({'+'.join(profiles)}): {name}")

    if "part5" in profiles and not list(run_dir.glob("venue_profile*.md")):
        warnings.append("part5 run has no venue_profile*.md yet")

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
        "profiles": profiles,
        "status": "CONSISTENT" if not errors else "MISMATCH",
        "errors": errors,
        "warnings": warnings,
        "manifest_rows": len(manifest),
    }


def self_test() -> int:
    import tempfile

    part3_files = {
        "research_state.md": "Budget\nUsed: 0\n",
        "round_log.md": "## Call Ledger\n\n| # | call | note |\n|---|---|---|\n",
        "experiment_contract.md": "# Experiment Contract: E1\n",
        "compute_budget.md": "# Compute Budget\n",
        "run_ledger.csv": "RunID,Status\n",
        "claim_promotion_ledger.md": "# Claims\n",
    }
    manifest_rows = "\n".join(
        f"| {name} | file | — | — | on_disk |  |" for name in part3_files
    )
    manifest = (
        "| Output | Format | Source files | Evidence requirement | Status | Notes |\n"
        "|---|---|---|---|---|---|\n" + manifest_rows + "\n"
    )

    with tempfile.TemporaryDirectory() as temp:
        part3_dir = Path(temp) / "part3"
        part3_dir.mkdir()
        for name, content in part3_files.items():
            (part3_dir / name).write_text(content, encoding="utf-8")
        (part3_dir / "output_manifest.md").write_text(manifest, encoding="utf-8")
        good = validate(part3_dir)
        if good["profiles"] != ["part3"] or good["status"] != "CONSISTENT":
            print(f"self-test FAIL: part3 fixture: {good['profiles']} {good['errors']}")
            return 1

        lit_dir = Path(temp) / "lit"
        lit_dir.mkdir()
        (lit_dir / "research_state.md").write_text("Used: 0\n", encoding="utf-8")
        bad = validate(lit_dir)
        joined = " | ".join(bad["errors"])
        if (
            bad["profiles"] != ["literature"]
            or bad["status"] != "MISMATCH"
            or "candidate_pool.md" not in joined
        ):
            print(f"self-test FAIL: literature fixture: {bad['profiles']} {bad['errors']}")
            return 1

    print("self-test PASS: part3 profile CONSISTENT, bare literature dir flagged")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path, nargs="?")
    parser.add_argument(
        "--profile",
        choices=sorted({"literature", *PROFILE_FILES}),
        help="override run-profile auto-detection",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    parser.add_argument("--self-test", action="store_true", help="run built-in fixtures")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.run_directory is None:
        parser.error("run_directory is required unless --self-test is given")

    if not args.run_directory.is_dir():
        print(f"error: not a directory: {args.run_directory}", file=sys.stderr)
        return 2

    result = validate(args.run_directory, args.profile)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"run:     {result['run_directory']}")
        print(f"profile: {'+'.join(result['profiles'])}")
        print(f"status:  {result['status']}")
        for err in result["errors"]:
            print(f"  ERROR   {err}")
        for warn in result["warnings"]:
            print(f"  warning {warn}")
    return 0 if result["status"] == "CONSISTENT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
