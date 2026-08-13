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
4. The current round in research_state.md matches the latest round heading in
   round_log.md; every RoundID cited in the call ledger has a narrative round
   entry.
5. Every EvidenceID cited in round_log.md exists in evidence_registry.md.
6. Files in one-level subdirectories (sources/, figures/, ...) have a manifest
   row, unless the directory itself has one (warning only).
7. When the run is closed (stop status is not `continue`), the actual column
   of the search-budget-contract allocation table is backfilled.

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


EVIDENCE_ID_RE = re.compile(r"\bE-[A-Z]+-\d{4}\b|\bE\d{4}\b")


def parse_state_current_round(state: str) -> str | None:
    match = re.search(r"Current round[:*\s]+[^\n]*?(R\d{4})", state)
    return match.group(1) if match else None


def parse_round_headings(round_log: str) -> list[str]:
    return re.findall(r"^##\s+(R\d{4})", round_log, flags=re.MULTILINE)


def parse_ledger_round_ids(round_log: str) -> list[str]:
    return sorted(set(re.findall(r"^\|\s*\d+\s*\|\s*(R\d{4})", round_log, flags=re.MULTILINE)))


def parse_stop_status(state: str) -> str | None:
    match = re.search(
        r"Current stop status[:*]*\s*([^\n]+)", state, flags=re.IGNORECASE
    )
    return match.group(1).strip().lstrip("* ") if match else None


EMPTY_CELL_VALUES = {"", "-", "—", "–", "n/a"}


def parse_unfilled_actual_stages(contract: str) -> list[str]:
    """Stage names in the allocation table whose actual column is empty."""
    unfilled: list[str] = []
    actual_col: int | None = None
    for line in contract.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if actual_col is None:
            for idx, cell in enumerate(cells):
                if "actual" in cell.lower():
                    actual_col = idx
                    break
            continue
        if not cells or set(cells[0]) <= {"-", " ", ":"}:
            continue
        if len(cells) > actual_col and cells[actual_col].lower() in EMPTY_CELL_VALUES:
            unfilled.append(cells[0])
    return unfilled


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
        # One-level subdirectory files: covered by an own row or a row for
        # the directory itself; anything else is flagged as a warning.
        for subdir in sorted(p for p in run_dir.iterdir() if p.is_dir() and not p.name.startswith(".")):
            dir_key_present = any(
                key.rstrip("/") == subdir.name for key in manifest
            )
            if dir_key_present:
                continue
            uncovered = [
                f"{subdir.name}/{f.name}"
                for f in sorted(subdir.iterdir())
                if f.is_file()
                and f.suffix not in IGNORED_SUFFIXES
                and not f.name.startswith(".")
                and f"{subdir.name}/{f.name}" not in manifest
            ]
            if uncovered:
                warnings.append(
                    f"subdirectory files without a manifest row (add rows or one row for '{subdir.name}/'): "
                    + ", ".join(uncovered)
                )

    round_log_path = run_dir / "round_log.md"
    state_path = run_dir / "research_state.md"
    round_log_text = round_log_path.read_text(encoding="utf-8") if round_log_path.is_file() else None
    state_text = state_path.read_text(encoding="utf-8") if state_path.is_file() else None
    if round_log_text is not None:
        ledger_total = parse_call_ledger_total(round_log_text)
        if ledger_total is None:
            warnings.append("round_log.md has no Call Ledger section")
        elif state_text is not None:
            mirror = parse_state_budget_used(state_text)
            if mirror is None:
                warnings.append("research_state.md has no parseable 'Used: n' budget mirror")
            elif mirror != ledger_total:
                errors.append(
                    f"budget mismatch: call ledger says {ledger_total} calls, "
                    f"research_state.md mirrors {mirror} (ledger wins)"
                )

        headings = parse_round_headings(round_log_text)
        if state_text is not None and headings:
            state_round = parse_state_current_round(state_text)
            latest = max(headings)
            if state_round is None:
                warnings.append("research_state.md has no parseable 'Current round: Rnnnn'")
            elif state_round < latest:
                errors.append(
                    f"research_state.md current round {state_round} is behind "
                    f"round_log.md latest round {latest} (stale state)"
                )
            elif state_round > latest:
                errors.append(
                    f"research_state.md current round {state_round} is ahead of "
                    f"round_log.md latest round {latest} (state leads disk)"
                )
        for round_id in parse_ledger_round_ids(round_log_text):
            if round_id not in headings:
                errors.append(
                    f"call ledger cites {round_id} but round_log.md has no "
                    f"'## {round_id}' narrative entry (reconstruct and mark it)"
                )

        registry_path = run_dir / "evidence_registry.md"
        if registry_path.is_file():
            registry_ids = set(EVIDENCE_ID_RE.findall(registry_path.read_text(encoding="utf-8")))
            cited = set(EVIDENCE_ID_RE.findall(round_log_text))
            for evidence_id in sorted(cited - registry_ids):
                errors.append(
                    f"round_log.md cites {evidence_id} but evidence_registry.md "
                    f"has no such entry (state leads disk)"
                )

    contract_path = run_dir / "search_budget_contract.md"
    if contract_path.is_file():
        unfilled = parse_unfilled_actual_stages(contract_path.read_text(encoding="utf-8"))
        if unfilled:
            stop_status = parse_stop_status(state_text) if state_text else None
            run_closed = stop_status is not None and "continue" not in stop_status.lower()
            message = (
                "search_budget_contract.md actual column not backfilled for: "
                + ", ".join(unfilled)
            )
            if run_closed:
                errors.append(message + f" (run closed: {stop_status})")
            else:
                warnings.append(message)

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

        stale_dir = Path(temp) / "stale"
        stale_dir.mkdir()
        (stale_dir / "research_state.md").write_text(
            "**Current round:** R0001\nUsed: 2\n"
            "**Current stop status:** saturated_under_budget\n",
            encoding="utf-8",
        )
        (stale_dir / "round_log.md").write_text(
            "## Call Ledger\n\n"
            "| # | RoundID | type | target | yield | running total |\n"
            "|---|---|---|---|---|---|\n"
            "| 1 | R0002 | fetch | x | ok (E0001) | 1/10 |\n"
            "| 2 | R0003 | fetch | y | ok | 2/10 |\n\n"
            "## R0003\n\nnarrative\n",
            encoding="utf-8",
        )
        (stale_dir / "evidence_registry.md").write_text("# Registry\n(no rows)\n", encoding="utf-8")
        (stale_dir / "candidate_pool.md").write_text("# Pool\n", encoding="utf-8")
        (stale_dir / "search_budget_contract.md").write_text(
            "| stage | planned budget | actual budget | notes |\n"
            "|---|---:|---:|---|\n"
            "| retrieval | 14 | — | |\n",
            encoding="utf-8",
        )
        stale = validate(stale_dir)
        joined = " | ".join(stale["errors"])
        expected_fragments = [
            "R0001 is behind",
            "no '## R0002' narrative entry",
            "cites E0001 but evidence_registry.md",
            "actual column not backfilled",
        ]
        missing = [frag for frag in expected_fragments if frag not in joined]
        if stale["status"] != "MISMATCH" or missing:
            print(f"self-test FAIL: stale fixture missing {missing}: {stale['errors']}")
            return 1

    print(
        "self-test PASS: part3 profile CONSISTENT, bare literature dir flagged, "
        "stale-state fixture raises round/narrative/evidence/backfill errors"
    )
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
