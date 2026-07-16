#!/usr/bin/env python3
"""Validate a Part 2 technical-learning and innovation-audit package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import tempfile
from pathlib import Path


REQUIRED_FILES = {
    "contract": "part2_learning_contract.md",
    "report": "part2_learning_report.md",
    "innovation": "innovation_delta.csv",
    "code_map": "equation_code_map.csv",
    "review": "review_core.md",
}

T5_REQUIRED_FILES = {
    "reproduction_report": "minimal_reproduction_report.md",
    "reproduction_manifest": "reproduction_manifest.json",
    "reproduction_output": "reproduction_output.json",
}

CONTRACT_FIELDS = [
    "Topic or method",
    "Target capability",
    "Source Part 1 run",
    "Focal PaperIDs",
    "Mode",
    "Target competence",
    "Frontier cutoff",
    "Requested outputs",
    "Stop condition",
]

REPORT_HEADINGS = [
    "## Learning Question",
    "## Lineage Learning Path",
    "## Core Technical Difference",
    "## Technical Mechanism",
    "## Formula and Assumptions",
    "## Algorithm and Implementation",
    "## Evidence and Benchmarks",
    "## Technical Review",
    "## Checked Difference",
    "## Learning Status",
    "## Teach Back",
    "## Boundaries and Open Questions",
]

REVIEW_HEADINGS = [
    "## Entry Check",
    "## Method Comparison",
    "## Validity And Reproducibility",
    "## Core Claims",
    "## Reading Order",
    "## Decision",
]

INNOVATION_HEADER_ORDER = [
    "delta_id",
    "focal_paper_id",
    "predecessor_paper_id",
    "successor_paper_id",
    "dimension",
    "inherited_component",
    "changed_component",
    "claimed_or_observed_effect",
    "statement_layer",
    "evidence_id",
    "source_anchor",
    "reasoning",
    "confidence",
    "status",
]
INNOVATION_HEADERS = set(INNOVATION_HEADER_ORDER)

CODE_MAP_HEADER_ORDER = [
    "map_id",
    "paper_id",
    "equation_id",
    "equation_role",
    "latex",
    "source_anchor",
    "evidence_id",
    "algorithm_step",
    "code_repo",
    "code_version",
    "code_file",
    "code_symbol",
    "config_or_data",
    "implementation_status",
    "reproduction_test",
    "observed_result",
    "boundary",
    "status",
]
CODE_MAP_HEADERS = set(CODE_MAP_HEADER_ORDER)

ALLOWED_LAYERS = {
    "author_claim",
    "source_supported_synthesis",
    "reviewer_inference",
    "unresolved",
}

EVIDENCE_PATTERN = re.compile(r"\bE(?:\d{4,}|-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\b")
PAPER_ID_PATTERN = re.compile(r"\bP\d{3}\b")
RELATION_ID_PATTERN = re.compile(r"\bR\d{4}\b")
CITATION_EVIDENCE_PATTERN = re.compile(r"\bCIT-\d+-\d+\b")
ANCHOR_PATTERN = re.compile(
    r"(?:\bp\.\s*\d+|\bpp\.\s*\d+|\bSec\.\s*[A-Za-z0-9]|"
    r"\bEq\.\s*\(?[A-Za-z0-9]|\bFig\.\s*[A-Za-z0-9]|"
    r"\bTable\s*[A-Za-z0-9]|\bAppendix\s+[A-Za-z0-9])",
    re.IGNORECASE,
)
PLACEHOLDER_PATTERN = re.compile(r"<[^>\n]+>|\b(?:TODO|TBD)\b", re.IGNORECASE)


def table_field(text: str, field: str) -> str | None:
    match = re.search(
        rf"^\|\s*{re.escape(field)}\s*\|\s*(.*?)\s*\|\s*$",
        text,
        re.MULTILINE,
    )
    return match.group(1).strip(" `") if match else None


def declared_status(text: str, label: str, allowed: set[str]) -> str | None:
    match = re.search(rf"{re.escape(label)}:\s*`?([A-Z_]+)`?", text)
    if not match or match.group(1) not in allowed:
        return None
    return match.group(1)


def ordered_headings(text: str, headings: list[str], errors: list[str], label: str) -> None:
    positions = []
    for heading in headings:
        position = text.find(heading)
        if position < 0:
            errors.append(f"{label} missing heading: {heading}")
        positions.append(position)
    present = [position for position in positions if position >= 0]
    if present != sorted(present):
        errors.append(f"{label} headings are out of order")


def read_csv(path: Path, required: set[str], errors: list[str]) -> list[dict[str, str]]:
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            headers = set(reader.fieldnames or [])
            missing = sorted(required - headers)
            if missing:
                errors.append(f"{path.name} missing columns: {', '.join(missing)}")
            return list(reader)
    except (OSError, csv.Error) as exc:
        errors.append(f"cannot read {path.name}: {exc}")
        return []


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path, errors: list[str]) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot read {path.name}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path.name} must contain a JSON object")
        return {}
    return value


def resolve_part1_ledgers(
    directory: Path,
    contract: str,
    package_text: str,
    errors: list[str],
) -> dict[str, object]:
    source_value = table_field(contract, "Source Part 1 run")
    if not source_value:
        return {
            "source_part1_run": None,
            "evidence_refs": 0,
            "paper_refs": 0,
            "relation_refs": 0,
            "citation_evidence_refs": 0,
        }

    source_path = Path(source_value)
    source_run = source_path if source_path.is_absolute() else directory / source_path
    source_run = source_run.resolve()
    ledger_specs = {
        "evidence": (source_run / "evidence_registry.csv", {"evidence_id"}),
        "relation": (
            source_run / "relation_ledger.csv",
            {"edge_id", "evidence_id"},
        ),
        "paper": (
            source_run / "paper_verification_ledger.csv",
            {"paper_id"},
        ),
    }
    ledger_rows: dict[str, list[dict[str, str]]] = {}
    for name, (path, required_columns) in ledger_specs.items():
        if not path.is_file():
            errors.append(f"Source Part 1 run lacks {path.name}")
            ledger_rows[name] = []
            continue
        ledger_rows[name] = read_csv(path, required_columns, errors)

    evidence_refs = set(EVIDENCE_PATTERN.findall(package_text))
    paper_refs = set(PAPER_ID_PATTERN.findall(package_text))
    relation_refs = set(RELATION_ID_PATTERN.findall(package_text))
    citation_refs = set(CITATION_EVIDENCE_PATTERN.findall(package_text))

    available_evidence = {
        row.get("evidence_id", "").strip() for row in ledger_rows.get("evidence", [])
    }
    available_papers = {
        row.get("paper_id", "").strip() for row in ledger_rows.get("paper", [])
    }
    available_relations = {
        row.get("edge_id", "").strip() for row in ledger_rows.get("relation", [])
    }
    available_citations = {
        row.get("evidence_id", "").strip() for row in ledger_rows.get("relation", [])
    }

    unresolved = {
        "EvidenceID": sorted(evidence_refs - available_evidence),
        "PaperID": sorted(paper_refs - available_papers),
        "relation ID": sorted(relation_refs - available_relations),
        "citation EvidenceID": sorted(citation_refs - available_citations),
    }
    for label, identifiers in unresolved.items():
        if identifiers:
            errors.append(
                f"unresolved {label} references: {', '.join(identifiers)}"
            )

    return {
        "source_part1_run": source_value,
        "evidence_refs": len(evidence_refs),
        "paper_refs": len(paper_refs),
        "relation_refs": len(relation_refs),
        "citation_evidence_refs": len(citation_refs),
        "unresolved_source_refs": unresolved,
    }


def gate_status(report: str, gate: str) -> str | None:
    match = re.search(
        rf"^\|\s*{gate}\s*\|.*?\|\s*(pass|pending|blocked|not_requested)\s*\|\s*$",
        report,
        re.MULTILINE | re.IGNORECASE,
    )
    return match.group(1).lower() if match else None


def validate_package(directory: Path) -> dict[str, object]:
    errors: list[str] = []
    paths = {name: directory / filename for name, filename in REQUIRED_FILES.items()}
    for path in paths.values():
        if not path.is_file():
            errors.append(f"missing required file: {path.name}")
    if errors:
        return {
            "status": "FAIL",
            "package_status": None,
            "ready_for_use": False,
            "errors": errors,
        }

    contract = paths["contract"].read_text(encoding="utf-8")
    report = paths["report"].read_text(encoding="utf-8")
    review = paths["review"].read_text(encoding="utf-8")
    package_status = declared_status(
        contract, "Package status", {"DRAFT", "VERIFIED", "BLOCKED"}
    )
    report_status = declared_status(
        report, "Report status", {"DRAFT", "VERIFIED", "BLOCKED"}
    )
    review_status = declared_status(review, "Review status", {"BLOCKED", "READY"})

    if not contract.startswith("# Part 2 Learning Contract\n"):
        errors.append("contract missing exact top-level title")
    if not report.startswith("# Part 2 Technical Learning Report\n"):
        errors.append("report missing exact top-level title")
    if not review.startswith("# Part 2 Technical Review\n"):
        errors.append("review missing exact top-level title")
    if package_status is None:
        errors.append("missing or invalid Package status")
    if report_status is None:
        errors.append("missing or invalid Report status")
    if review_status is None:
        errors.append("missing or invalid Review status")

    for field in CONTRACT_FIELDS:
        if table_field(contract, field) is None:
            errors.append(f"contract missing field: {field}")
    report_headings = report.replace("## Frontier Delta", "## Checked Difference")
    ordered_headings(report_headings, REPORT_HEADINGS, errors, "report")
    ordered_headings(review, REVIEW_HEADINGS, errors, "review")

    innovation_rows = read_csv(paths["innovation"], INNOVATION_HEADERS, errors)
    code_rows = read_csv(paths["code_map"], CODE_MAP_HEADERS, errors)
    if not innovation_rows:
        errors.append("innovation_delta.csv has no data rows")
    if not code_rows:
        errors.append("equation_code_map.csv has no data rows")

    target = table_field(contract, "Target competence")
    if not target or not re.fullmatch(r"T[0-5]", target):
        errors.append("Target competence must be T0-T5")
        target_level = -1
    else:
        target_level = int(target[1])

    mode = (table_field(contract, "Mode") or "").lower()
    outputs = (table_field(contract, "Requested outputs") or "").lower()
    all_text = "\n".join(
        [contract, report, review]
        + [paths["innovation"].read_text(encoding="utf-8")]
        + [paths["code_map"].read_text(encoding="utf-8")]
    )
    evidence_ids = sorted(set(EVIDENCE_PATTERN.findall(all_text)))
    anchors = ANCHOR_PATTERN.findall(all_text)
    placeholders = PLACEHOLDER_PATTERN.findall(all_text)

    source_resolution = resolve_part1_ledgers(
        directory, contract, all_text, errors
    )

    if "tex" in outputs and not (directory / "part2_learning_report.tex").is_file():
        errors.append("TeX requested but part2_learning_report.tex is missing")
    if "pdf" in outputs and not (directory / "part2_learning_report.pdf").is_file():
        errors.append("PDF requested but part2_learning_report.pdf is missing")
    if "graph" in outputs and not (directory / "lineage_learning_path.mmd").is_file():
        errors.append("lineage graph requested but lineage_learning_path.mmd is missing")

    if package_status == "VERIFIED":
        if report_status != "VERIFIED":
            errors.append("verified package requires Report status VERIFIED")
        if review_status != "READY":
            errors.append("verified package requires Review status READY")
        if placeholders:
            errors.append(
                f"verified package contains {len(placeholders)} unresolved placeholders"
            )
        if len(evidence_ids) < 8:
            errors.append(
                f"verified package has only {len(evidence_ids)} distinct EvidenceIDs"
            )
        if len(anchors) < 8:
            errors.append(f"verified package has only {len(anchors)} source anchors")

        for row_number, row in enumerate(innovation_rows, start=2):
            layer = row.get("statement_layer", "").strip()
            if layer not in ALLOWED_LAYERS:
                errors.append(
                    f"innovation_delta.csv row {row_number} has invalid statement_layer"
                )
            if layer in {"author_claim", "source_supported_synthesis"}:
                if not EVIDENCE_PATTERN.search(row.get("evidence_id", "")):
                    errors.append(
                        f"innovation_delta.csv row {row_number} lacks EvidenceID"
                    )
                if not ANCHOR_PATTERN.search(row.get("source_anchor", "")):
                    errors.append(
                        f"innovation_delta.csv row {row_number} lacks source anchor"
                    )
            if row.get("status", "").strip().lower() not in {
                "verified",
                "inference",
                "unresolved",
            }:
                errors.append(
                    f"innovation_delta.csv row {row_number} has non-final status"
                )

        allowed_implementation = {
            "traced",
            "tested",
            "unavailable",
            "blocked",
            "not_requested",
        }
        for row_number, row in enumerate(code_rows, start=2):
            implementation = row.get("implementation_status", "").strip().lower()
            if implementation not in allowed_implementation:
                errors.append(
                    f"equation_code_map.csv row {row_number} has non-final implementation_status"
                )

        if target_level >= 4:
            traced_rows = [
                row
                for row in code_rows
                if row.get("implementation_status", "").strip().lower()
                in {"traced", "tested"}
            ]
            if not traced_rows:
                errors.append("T4 requires at least one traced or tested code row")
            required_code_fields = [
                "code_repo",
                "code_version",
                "code_file",
                "code_symbol",
                "config_or_data",
            ]
            non_values = {"", "unavailable", "not_requested", "pending", "blocked"}
            for row_number, row in enumerate(code_rows, start=2):
                implementation = row.get("implementation_status", "").strip().lower()
                if implementation not in {"traced", "tested"}:
                    continue
                for field in required_code_fields:
                    if row.get(field, "").strip().lower() in non_values:
                        errors.append(
                            f"equation_code_map.csv row {row_number} lacks traced {field}"
                        )

        if target_level >= 5:
            t5_paths = {
                name: directory / filename
                for name, filename in T5_REQUIRED_FILES.items()
            }
            for path in t5_paths.values():
                if not path.is_file():
                    errors.append(f"T5 missing required file: {path.name}")

            tested_rows = [
                row
                for row in code_rows
                if row.get("implementation_status", "").strip().lower() == "tested"
            ]
            if not tested_rows:
                errors.append("T5 requires at least one tested equation-code row")
            non_results = {"", "unavailable", "not_requested", "pending", "blocked"}
            for row_number, row in enumerate(code_rows, start=2):
                if row.get("implementation_status", "").strip().lower() != "tested":
                    continue
                for field in ("reproduction_test", "observed_result"):
                    if row.get(field, "").strip().lower() in non_results:
                        errors.append(
                            f"equation_code_map.csv row {row_number} lacks tested {field}"
                        )

            if all(path.is_file() for path in t5_paths.values()):
                manifest = read_json(t5_paths["reproduction_manifest"], errors)
                output = read_json(t5_paths["reproduction_output"], errors)
                required_manifest_fields = {
                    "schema_version",
                    "repository",
                    "code_version",
                    "command",
                    "output_file",
                    "output_sha256",
                    "status",
                }
                missing_manifest = sorted(
                    field
                    for field in required_manifest_fields
                    if not str(manifest.get(field, "")).strip()
                )
                if missing_manifest:
                    errors.append(
                        "reproduction_manifest.json missing fields: "
                        + ", ".join(missing_manifest)
                    )
                if str(manifest.get("status", "")).upper() != "PASS":
                    errors.append("reproduction manifest status is not PASS")
                if str(output.get("overall", "")).upper() != "PASS":
                    errors.append("reproduction output overall is not PASS")
                if manifest.get("output_file") != t5_paths["reproduction_output"].name:
                    errors.append("reproduction manifest output_file does not match package output")
                observed_hash = sha256(t5_paths["reproduction_output"])
                if manifest.get("output_sha256") != observed_hash:
                    errors.append("reproduction output SHA-256 does not match manifest")
                if manifest.get("code_version") != output.get("commit"):
                    errors.append("reproduction code version does not match machine output")
                if manifest.get("source_sha256") and (
                    manifest.get("source_sha256") != output.get("source_sha256")
                ):
                    errors.append("reproduction source SHA-256 does not match machine output")

        for level in range(target_level + 1):
            status = gate_status(report, f"T{level}")
            if status != "pass":
                errors.append(f"requested gate T{level} is not marked pass")
        for level in range(target_level + 1, 6):
            if gate_status(report, f"T{level}") is None:
                errors.append(f"report lacks competence row T{level}")

        if "reproduce" in mode and target_level < 5:
            errors.append("reproduce mode requires Target competence T5")
    result = {
        "status": "PASS" if not errors else "FAIL",
        "package_status": package_status,
        "report_status": report_status,
        "review_status": review_status,
        "ready_for_use": package_status == "VERIFIED" and not errors,
        "target_competence": target,
        "innovation_rows": len(innovation_rows),
        "equation_code_rows": len(code_rows),
        "evidence_ids": len(evidence_ids),
        "source_anchors": len(anchors),
        "unresolved_placeholders": len(placeholders),
        "errors": errors,
    }
    result.update(source_resolution)
    return result


def self_test() -> None:
    with tempfile.TemporaryDirectory() as temp:
        directory = Path(temp)
        source_run = directory / "run" / "part1"
        source_run.mkdir(parents=True)
        (source_run / "evidence_registry.csv").write_text(
            "evidence_id\n",
            encoding="utf-8",
        )
        (source_run / "relation_ledger.csv").write_text(
            "edge_id,evidence_id\n",
            encoding="utf-8",
        )
        (source_run / "paper_verification_ledger.csv").write_text(
            "paper_id\nP000\nP001\n",
            encoding="utf-8",
        )
        (directory / "part2_learning_contract.md").write_text(
            """# Part 2 Learning Contract

Package status: `DRAFT`

| Field | Value |
|---|---|
| Topic or method | Test method |
| Target capability | Explain the method |
| Source Part 1 run | run/part1 |
| Focal PaperIDs | P001 |
| Mode | understand |
| Target competence | T2 |
| Frontier cutoff | 2026-01-01 |
| Requested outputs | md |
| Stop condition | T0-T2 supporting records |
""",
            encoding="utf-8",
        )
        report_sections = "\n\n".join(f"{heading}\n\nPending." for heading in REPORT_HEADINGS)
        (directory / "part2_learning_report.md").write_text(
            "# Part 2 Technical Learning Report\n\nReport status: `DRAFT`\n\n"
            + report_sections
            + "\n\n| T0 | object | proof | pending |\n"
            + "| T1 | concept | proof | pending |\n"
            + "| T2 | formula | proof | pending |\n"
            + "| T3 | algorithm | proof | not_requested |\n"
            + "| T4 | code | proof | not_requested |\n"
            + "| T5 | reproduce | proof | not_requested |\n",
            encoding="utf-8",
        )
        review_sections = "\n\n".join(f"{heading}\n\nPending." for heading in REVIEW_HEADINGS)
        (directory / "review_core.md").write_text(
            "# Part 2 Technical Review\n\nReview status: `BLOCKED`\n\n"
            + review_sections
            + "\n",
            encoding="utf-8",
        )
        (directory / "innovation_delta.csv").write_text(
            ",".join(INNOVATION_HEADER_ORDER)
            + "\n"
            + ",".join(["D001", "P001", "P000", "", "objective", "old", "new", "effect", "unresolved", "pending", "pending", "reason", "low", "pending"])
            + "\n",
            encoding="utf-8",
        )
        (directory / "equation_code_map.csv").write_text(
            ",".join(CODE_MAP_HEADER_ORDER)
            + "\n"
            + ",".join(["M001", "P001", "F01", "role", "x=y", "pending", "pending", "step", "unavailable", "", "unavailable", "unavailable", "", "pending", "not_requested", "pending", "boundary", "pending"])
            + "\n",
            encoding="utf-8",
        )
        valid = validate_package(directory)
        (directory / "review_core.md").unlink()
        invalid = validate_package(directory)
    if valid["status"] != "PASS" or invalid["status"] != "FAIL":
        raise SystemExit(f"self-test failed: valid={valid} invalid={invalid}")

    with tempfile.TemporaryDirectory() as temp:
        directory = Path(temp)
        source_run = directory / "run" / "part1"
        source_run.mkdir(parents=True)
        evidence_ids = [f"E{index}" for index in range(1000, 1008)]
        (source_run / "evidence_registry.csv").write_text(
            "evidence_id\n" + "\n".join(evidence_ids) + "\n",
            encoding="utf-8",
        )
        (source_run / "relation_ledger.csv").write_text(
            "edge_id,evidence_id\n",
            encoding="utf-8",
        )
        (source_run / "paper_verification_ledger.csv").write_text(
            "paper_id\nP001\n",
            encoding="utf-8",
        )
        (directory / "part2_learning_contract.md").write_text(
            """# Part 2 Learning Contract

Package status: `VERIFIED`

| Field | Value |
|---|---|
| Topic or method | Test method |
| Target capability | Trace and test code |
| Source Part 1 run | run/part1 |
| Focal PaperIDs | P001 |
| Mode | reproduce |
| Target competence | T5 |
| Frontier cutoff | 2026-01-01 |
| Requested outputs | md / csv / json / code |
| Stop condition | T0-T5 pass |
""",
            encoding="utf-8",
        )
        evidence_block = "; ".join(evidence_ids)
        report_sections = "\n\n".join(
            f"{heading}\n\nChecked at p. {index + 1}. {evidence_block}"
            for index, heading in enumerate(REPORT_HEADINGS)
        )
        gate_rows = "\n".join(
            f"| T{level} | gate | proof | pass |" for level in range(6)
        )
        (directory / "part2_learning_report.md").write_text(
            "# Part 2 Technical Learning Report\n\nReport status: `VERIFIED`\n\n"
            + report_sections
            + "\n\n"
            + gate_rows
            + "\n",
            encoding="utf-8",
        )
        review_sections = "\n\n".join(
            f"{heading}\n\nChecked at p. {index + 1}."
            for index, heading in enumerate(REVIEW_HEADINGS)
        )
        (directory / "review_core.md").write_text(
            "# Part 2 Technical Review\n\nReview status: `READY`\n\n"
            + review_sections
            + "\n",
            encoding="utf-8",
        )
        with (directory / "innovation_delta.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=INNOVATION_HEADER_ORDER)
            writer.writeheader()
            writer.writerow(
                {
                    "delta_id": "D001",
                    "focal_paper_id": "P001",
                    "dimension": "objective",
                    "inherited_component": "old",
                    "changed_component": "new",
                    "claimed_or_observed_effect": "checked",
                    "statement_layer": "source_supported_synthesis",
                    "evidence_id": "E1000",
                    "source_anchor": "PDF p. 1, Eq. (1)",
                    "reasoning": "source comparison",
                    "confidence": "high",
                    "status": "verified",
                }
            )
        with (directory / "equation_code_map.csv").open(
            "w", newline="", encoding="utf-8"
        ) as handle:
            writer = csv.DictWriter(handle, fieldnames=CODE_MAP_HEADER_ORDER)
            writer.writeheader()
            writer.writerow(
                {
                    "map_id": "M001",
                    "paper_id": "P001",
                    "equation_id": "Eq. (1)",
                    "equation_role": "objective",
                    "latex": "x=y",
                    "source_anchor": "PDF p. 1, Eq. (1)",
                    "evidence_id": "E1000",
                    "algorithm_step": "evaluate",
                    "code_repo": "https://example.org/repo",
                    "code_version": "abc",
                    "code_file": "loss.py",
                    "code_symbol": "loss",
                    "config_or_data": "config.yaml",
                    "implementation_status": "tested",
                    "reproduction_test": "test.py",
                    "observed_result": "PASS",
                    "boundary": "minimal check",
                    "status": "verified",
                }
            )
        (directory / "minimal_reproduction_report.md").write_text(
            "# Minimal Reproduction\n\nStatus: `PASS`\n",
            encoding="utf-8",
        )
        output = {"overall": "PASS", "commit": "abc", "source_sha256": "def"}
        output_path = directory / "reproduction_output.json"
        output_path.write_text(json.dumps(output) + "\n", encoding="utf-8")
        manifest = {
            "schema_version": "test-v1",
            "repository": "https://example.org/repo",
            "code_version": "abc",
            "source_sha256": "def",
            "command": "python test.py",
            "output_file": "reproduction_output.json",
            "output_sha256": sha256(output_path),
            "status": "PASS",
        }
        (directory / "reproduction_manifest.json").write_text(
            json.dumps(manifest) + "\n", encoding="utf-8"
        )
        valid_t5 = validate_package(directory)
        output_path.unlink()
        invalid_t5 = validate_package(directory)
    if valid_t5["status"] != "PASS" or invalid_t5["status"] != "FAIL":
        raise SystemExit(
            f"T5 self-test failed: valid={valid_t5} invalid={invalid_t5}"
        )
    print("PASS: Part 2 learning-package validator self-test")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, nargs="?")
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if args.directory is None:
        parser.error("directory is required unless --self-test is used")

    result = validate_package(args.directory)
    rendered = json.dumps(result, indent=2)
    if args.json_output:
        args.json_output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
