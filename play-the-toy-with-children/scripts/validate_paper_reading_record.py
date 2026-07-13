#!/usr/bin/env python3
"""Validate the native paper-reading Markdown contract."""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path


REQUIRED_HEADINGS = [
    "## Identity Lock",
    "## Paper Map",
    "## Problem and Position",
    "## Mechanism",
    "## Equations",
    "## Experiments and Numbers",
    "## Boundaries",
    "## Safe Output",
    "## Search Leads",
]

IDENTITY_FIELDS = [
    "Title",
    "Authors",
    "Version and date",
    "arXiv / DOI",
    "Canonical URL",
    "Local full text",
    "Pages",
    "Reading level",
]

ANCHOR_PATTERN = re.compile(
    r"(?:\bp\.\s*\d+|\bpp\.\s*\d+|\bSec\.\s*[A-Za-z0-9]|"
    r"\bEq\.\s*\(?[A-Za-z0-9]|\bFig\.\s*[A-Za-z0-9]|"
    r"\bTable\s*[A-Za-z0-9]|\bAppendix\s+[A-Za-z0-9])",
    re.IGNORECASE,
)
EVIDENCE_PATTERN = re.compile(r"\bE(?:\d{4,}|-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\b")
PLACEHOLDER_PATTERN = re.compile(r"<[^>\n]+>|\b(?:TODO|TBD)\b", re.IGNORECASE)


def record_status(text: str) -> str | None:
    match = re.search(r"Record status:\s*`?(DRAFT|VERIFIED|BLOCKED)`?", text)
    return match.group(1) if match else None


def validate_text(text: str) -> dict[str, object]:
    errors: list[str] = []
    status = record_status(text)
    if not text.startswith("# Paper Reading Record\n"):
        errors.append("missing exact top-level title")
    if status is None:
        errors.append("missing or invalid Record status")

    positions = []
    for heading in REQUIRED_HEADINGS:
        position = text.find(heading)
        if position < 0:
            errors.append(f"missing heading: {heading}")
        positions.append(position)
    present_positions = [position for position in positions if position >= 0]
    if present_positions != sorted(present_positions):
        errors.append("required headings are out of order")

    for field in IDENTITY_FIELDS:
        if not re.search(rf"\|\s*{re.escape(field)}\s*\|", text):
            errors.append(f"missing identity field: {field}")

    for boundary in ("Author-stated", "Reviewer inference", "Unresolved"):
        if not re.search(rf"\|\s*{re.escape(boundary)}\s*\|", text):
            errors.append(f"missing boundary layer: {boundary}")
    for output_type in ("Allowed sentence", "Prohibited sentence"):
        if not re.search(rf"\|\s*{re.escape(output_type)}\s*\|", text):
            errors.append(f"missing safe-output row: {output_type}")

    evidence_ids = sorted(set(EVIDENCE_PATTERN.findall(text)))
    anchors = ANCHOR_PATTERN.findall(text)
    placeholders = PLACEHOLDER_PATTERN.findall(text)
    identifier_ok = bool(
        re.search(r"\b\d{4}\.\d{4,5}(?:v\d+)?\b", text)
        or re.search(r"\b10\.\d{4,9}/\S+", text)
    )
    canonical_url_ok = bool(re.search(r"https://\S+", text))
    reading_level_ok = bool(re.search(r"\|\s*Reading level\s*\|\s*C[234]\s*\|", text))
    pages_ok = bool(re.search(r"\|\s*Pages\s*\|\s*\d+\s*\|", text))

    if status == "VERIFIED":
        if placeholders:
            errors.append(f"verified record contains {len(placeholders)} unresolved placeholders")
        if not identifier_ok:
            errors.append("verified record lacks a DOI or arXiv identifier")
        if not canonical_url_ok:
            errors.append("verified record lacks an HTTPS canonical URL")
        if not reading_level_ok:
            errors.append("verified record lacks a C2-C4 reading level")
        if not pages_ok:
            errors.append("verified record lacks an integer page count")
        if len(evidence_ids) < 5:
            errors.append(f"verified record has only {len(evidence_ids)} distinct EvidenceIDs")
        if len(anchors) < 6:
            errors.append(f"verified record has only {len(anchors)} source anchors")

    return {
        "status": "PASS" if not errors else "FAIL",
        "record_status": status,
        "ready_for_claims": status == "VERIFIED" and not errors,
        "evidence_ids": len(evidence_ids),
        "source_anchors": len(anchors),
        "unresolved_placeholders": len(placeholders),
        "errors": errors,
    }


def self_test() -> None:
    valid = """# Paper Reading Record

Record status: `VERIFIED`

## Identity Lock
| Field | Value | Evidence |
|---|---|---|
| Title | A checked paper | E0001 |
| Authors | A. Author; B. Author | E0001 |
| Version and date | v1; 2026-01-01 | E0001 |
| arXiv / DOI | 2601.12345v1 | E0001 |
| Canonical URL | https://arxiv.org/abs/2601.12345 | E0001 |
| Local full text | papers/2601.12345.pdf | E0002 |
| Pages | 20 | E0002 |
| Reading level | C4 | E0002 |

## Paper Map
| Region | Purpose | Anchor | EvidenceID |
|---|---|---|---|
| Introduction | problem | p. 1, Sec. 1 | E0003 |

## Problem and Position
| Role | Statement | Anchor | EvidenceID |
|---|---|---|---|
| Problem | statement | p. 2, Sec. 1 | E0004 |

## Mechanism
| Step | Definition | Assumption | Anchor | EvidenceID |
|---|---|---|---|---|
| update | action | finite cost | p. 5, Sec. 3 | E0005 |

## Equations
| Object | Formula | Symbols | Role | Anchor | EvidenceID |
|---|---|---|---|---|---|
| weight | w=x | x defined | correction | p. 6, Eq. (2) | E0006 |

## Experiments and Numbers
| Test | Setup | Result | Cost | Anchor | EvidenceID |
|---|---|---|---|---|---|
| benchmark | baseline | result | reported | p. 9, Table 1 | E0007 |

## Boundaries
| Boundary type | Statement | Anchor | EvidenceID / status |
|---|---|---|---|
| Author-stated | limitation | p. 12, Sec. 5 | E0008 |
| Reviewer inference | concern | p. 9, Fig. 2 | inference |
| Unresolved | question | Appendix B | pending |

## Safe Output
| Output type | Wording | Support / reason |
|---|---|---|
| Allowed sentence | bounded claim | E0005; E0007 |
| Prohibited sentence | universal claim | E0008 |

## Search Leads
| Lead | Why | Route | Status |
|---|---|---|---|
| cited baseline | comparison | backward | pending |
"""
    invalid = valid.replace("Record status: `VERIFIED`", "Record status: `UNKNOWN`")
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "record.md"
        path.write_text(valid, encoding="utf-8")
        valid_result = validate_text(path.read_text(encoding="utf-8"))
        invalid_result = validate_text(invalid)
    if valid_result["status"] != "PASS" or invalid_result["status"] != "FAIL":
        raise SystemExit(
            f"self-test failed: valid={valid_result['errors']} invalid={invalid_result['errors']}"
        )
    print("PASS: native paper-reading record validator self-test")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path, nargs="?")
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    if args.record is None:
        parser.error("record is required unless --self-test is used")

    result = validate_text(args.record.read_text(encoding="utf-8"))
    rendered = json.dumps(result, indent=2)
    if args.json_output:
        args.json_output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
