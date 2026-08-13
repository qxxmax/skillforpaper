#!/usr/bin/env python3
"""Check a Part 6 talk package before the deck is given or shared.

Checks (see references/46 and 47), each with a numbered rule ID:

FILE001  mandatory files exist: presentation_contract.md,
         slide_claim_map.csv, figure_provenance.md, qa_bank.md.
CONTRACT001  the contract states a core message (non-placeholder sentence
         under "## Core Message").
MAP001   slide_claim_map.csv parses with the required columns; SlideIDs
         unique and non-empty.
MAP002   every row has a known Level; non-background rows have non-empty
         EvidenceRefs; Assertion is a sentence, not a topic fragment
         (heuristic: contains a space and does not end with ':').
MAP003   TimeSec is numeric where given; warn if the sum exceeds the
         contracted duration (parsed from "- Duration: {N}" when present).
FIG001   every FigureID referenced in the map resolves to a row in
         figure_provenance.md; no provenance row has status
         'needs_rederive' while its figure is on a slide.
QA001    qa_bank.md has at least one anticipated row; no row has an empty
         basis; no row is left 'needs_evidence'.
BOUND001 warn if no map row has Level 'boundary' (claiming completeness by
         omission).

Exit code 0 = ready, 1 = blockers found.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

CONTRACT_NAME = "presentation_contract.md"
MAP_NAME = "slide_claim_map.csv"
FIG_NAME = "figure_provenance.md"
QA_NAME = "qa_bank.md"
MANDATORY = [CONTRACT_NAME, MAP_NAME, FIG_NAME, QA_NAME]

MAP_COLUMNS = {"SlideID", "Assertion", "Level", "EvidenceRefs", "FigureIDs", "TimeSec", "Note"}
KNOWN_LEVELS = {"background", "observation", "candidate_claim", "validated_claim", "boundary"}
EMPTY_CELLS = {"", "-", "—", "n/a", "none"}


def split_refs(cell: str) -> list[str]:
    if cell.strip().lower() in EMPTY_CELLS:
        return []
    return [r.strip().strip("`") for r in cell.replace(";", ",").split(",") if r.strip()]


def read_md_table_rows(path: Path) -> list[dict[str, str]]:
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
        rows.append(dict(zip(header, cells)))
    return rows


def parse_duration_minutes(contract_text: str) -> int | None:
    m = re.search(r"^- Duration:\s*(\d+)", contract_text, flags=re.MULTILINE)
    return int(m.group(1)) if m else None


def validate(run_dir: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    for name in MANDATORY:
        if not (run_dir / name).is_file():
            errors.append(f"FILE001 mandatory file missing: {name}")
    if errors:
        return {"run": str(run_dir), "status": "BLOCKED", "errors": errors,
                "warnings": warnings, "slides": 0, "figures": 0, "qa_rows": 0}

    contract_text = (run_dir / CONTRACT_NAME).read_text(encoding="utf-8")
    core = ""
    m = re.search(r"## Core Message\s*\n+(.+)", contract_text)
    if m:
        core = m.group(1).strip()
    if not core or core.startswith("{"):
        errors.append("CONTRACT001 contract has no core message sentence")
    duration_min = parse_duration_minutes(contract_text)

    with (run_dir / MAP_NAME).open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        missing = MAP_COLUMNS - set(reader.fieldnames or [])
        if missing:
            errors.append(f"MAP001 {MAP_NAME} missing columns: {', '.join(sorted(missing))}")
            rows = []
        else:
            rows = [{k: (v or "").strip() for k, v in r.items()}
                    for r in reader if any((v or "").strip() for v in r.values())]
    if not rows and not any(e.startswith("MAP001") for e in errors):
        errors.append(f"MAP001 {MAP_NAME} has no data rows")

    slide_ids: set[str] = set()
    used_figs: set[str] = set()
    time_total = 0
    has_boundary = False
    for row in rows:
        sid = row.get("SlideID", "")
        if not sid:
            errors.append("MAP001 map row with empty SlideID")
            continue
        if sid in slide_ids:
            errors.append(f"MAP001 duplicate SlideID: {sid}")
        slide_ids.add(sid)

        level = row.get("Level", "")
        if level not in KNOWN_LEVELS:
            errors.append(f"MAP002 {sid}: unknown level '{level}'")
        if level == "boundary":
            has_boundary = True
        assertion = row.get("Assertion", "")
        if " " not in assertion or assertion.endswith(":"):
            errors.append(f"MAP002 {sid}: assertion is not a sentence: '{assertion[:40]}'")
        if level != "background" and not split_refs(row.get("EvidenceRefs", "")):
            errors.append(f"MAP002 {sid}: level '{level}' with empty EvidenceRefs")

        used_figs.update(split_refs(row.get("FigureIDs", "")))
        tsec = row.get("TimeSec", "")
        if tsec and tsec.lower() not in EMPTY_CELLS:
            if tsec.isdigit():
                time_total += int(tsec)
            else:
                errors.append(f"MAP003 {sid}: TimeSec '{tsec}' is not an integer")

    if duration_min is not None and time_total > duration_min * 60:
        warnings.append(
            f"MAP003 planned {time_total}s exceeds contracted {duration_min} min")

    fig_rows = read_md_table_rows(run_dir / FIG_NAME)
    fig_status = {r.get("FigureID", "").strip("`"): r.get("status", "")
                  for r in fig_rows if r.get("FigureID", "").strip("`")}
    for fid in sorted(used_figs):
        if fid not in fig_status:
            errors.append(f"FIG001 figure '{fid}' on a slide but not in {FIG_NAME}")
        elif "needs_rederive" in fig_status[fid]:
            errors.append(f"FIG001 figure '{fid}' is on a slide with status needs_rederive")

    qa_rows = [r for r in read_md_table_rows(run_dir / QA_NAME) if r.get("QID")]
    if not qa_rows:
        errors.append(f"QA001 {QA_NAME} has no anticipated questions")
    for r in qa_rows:
        qid = r.get("QID", "")
        if r.get("basis (ClaimID / EvidenceID / boundary)", r.get("basis", "")).lower() in EMPTY_CELLS:
            errors.append(f"QA001 {qid}: empty basis")
        if "needs_evidence" in r.get("status", ""):
            errors.append(f"QA001 {qid}: still needs_evidence")

    if rows and not has_boundary:
        warnings.append("BOUND001 no boundary slide in the map")

    return {"run": str(run_dir),
            "status": "READY" if not errors else "BLOCKED",
            "slides": len(rows), "figures": len(fig_status), "qa_rows": len(qa_rows),
            "errors": errors, "warnings": warnings}


GOOD_CONTRACT = """# Presentation Contract: demo

## Setting

- Format: seminar
- Duration: 20 + 10 questions
- Audience tier: specialist

## Core Message

The learned sampler halves autocorrelation time within the tested range.
"""

GOOD_MAP = """SlideID,Assertion,Level,EvidenceRefs,FigureIDs,TimeSec,Note
S01,Lattice sampling stalls at criticality,background,—,—,120,setup
S02,The learned sampler halves autocorrelation time,validated_claim,C-1,F01,300,core
S03,We did not test fermionic actions,boundary,ledger row 4,—,60,honesty
"""

GOOD_FIG = """# Figure Provenance

| FigureID | file | produced by (script / run / manifest entry) | source run or paper | status |
|---|---|---|---|---|
| F01 | figs/tau.pdf | scripts/plot_tau.py, run E1-R002 | runs/demo | verified |
"""

GOOD_QA = """# QA Bank

## Anticipated

| QID | question | basis (ClaimID / EvidenceID / boundary) | answer (2 sentences max) | status |
|---|---|---|---|---|
| Q01 | Why no fermions? | boundary: not tested | Out of tested scope; planned next. | ready |

## Received At The Talk

| date | question | answered with | in the bank? | follow-up |
|---|---|---|---|---|
"""


def self_test() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as temp:
        run_dir = Path(temp)
        (run_dir / CONTRACT_NAME).write_text(GOOD_CONTRACT, encoding="utf-8")
        (run_dir / MAP_NAME).write_text(GOOD_MAP, encoding="utf-8")
        (run_dir / FIG_NAME).write_text(GOOD_FIG, encoding="utf-8")
        (run_dir / QA_NAME).write_text(GOOD_QA, encoding="utf-8")
        good = validate(run_dir)
        if good["status"] != "READY" or good["errors"]:
            print(f"self-test FAIL: good fixture not READY: {good['errors']}")
            return 1

        bad_map = GOOD_MAP.replace("validated_claim,C-1", "validated_claim,—").replace(
            "S03,We did not test fermionic actions,boundary",
            "S03,Results:,fact")
        (run_dir / MAP_NAME).write_text(bad_map, encoding="utf-8")
        (run_dir / QA_NAME).write_text(GOOD_QA.replace("| ready |", "| needs_evidence |"),
                                       encoding="utf-8")
        bad = validate(run_dir)
        joined = " | ".join(bad["errors"])
        expected = ["MAP002 S02", "unknown level 'fact'", "not a sentence", "needs_evidence"]
        missing = [f for f in expected if f not in joined]
        if bad["status"] != "BLOCKED" or missing:
            print(f"self-test FAIL: bad fixture missed: {missing}; got {bad['errors']}")
            return 1

    print("self-test PASS: good fixture READY, bad fixture BLOCKED with expected errors")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_directory", type=Path, nargs="?",
                        help=f"directory containing {', '.join(MANDATORY)}")
    parser.add_argument("--json", action="store_true", help="emit JSON only")
    parser.add_argument("--self-test", action="store_true", help="run built-in fixtures")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.run_directory is None:
        parser.error("run_directory is required unless --self-test is given")
    if not args.run_directory.is_dir():
        print(f"error: {args.run_directory} is not a directory", file=sys.stderr)
        return 2

    result = validate(args.run_directory)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"run:    {result['run']}")
        print(f"status: {result['status']}")
        print(f"rows:   {result['slides']} slides, {result['figures']} figures, "
              f"{result['qa_rows']} QA rows")
        for err in result["errors"]:
            print(f"  ERROR   {err}")
        for warn in result["warnings"]:
            print(f"  warning {warn}")
    return 0 if result["status"] == "READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
