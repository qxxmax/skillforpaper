#!/usr/bin/env python3
"""Validate direct-citation edges against the live root bibliography/context."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    refs = list(csv.DictReader((ROOT / "root_bibliography_screening.csv").open(encoding="utf-8")))
    edges = list(csv.DictReader((ROOT / "relation_ledger.csv").open(encoding="utf-8")))
    direct = [edge for edge in edges if edge["EdgeType"] == "direct_citation"]
    errors = []
    ref_by_num = {int(row["ref_no"]): row for row in refs}
    seen = set()
    for edge in direct:
        match = re.fullmatch(r"ROOT-BIB-(\d{2})", edge["EvidenceID"])
        if not match:
            errors.append(f"{edge['EdgeID']}: malformed direct evidence ID")
            continue
        number = int(match.group(1))
        row = ref_by_num.get(number)
        if not row:
            errors.append(f"{edge['EdgeID']}: missing root bibliography row {number}")
            continue
        expected = f"P_{row['arxiv_id'].replace('.', '_')}" if row["arxiv_id"] else f"BIB_{number:02d}"
        if edge["TargetID"] != expected:
            errors.append(f"{edge['EdgeID']}: target {edge['TargetID']} != {expected}")
        if row["bibkey"] not in row["root_context"]:
            errors.append(f"{edge['EdgeID']}: bibkey absent from captured citation context")
        if edge["DirectlyCited"].lower() != "yes" or edge["HumanReviewStatus"] != "reviewed":
            errors.append(f"{edge['EdgeID']}: direct/review status invalid")
        seen.add(number)
    forward = [edge for edge in edges if edge["EdgeType"] == "forward_citation"]
    if seen != set(range(1, 59)):
        errors.append(f"direct edge coverage mismatch: {len(seen)}/58")
    result = {
        "status": "PASS" if not errors else "FAIL",
        "root_references": len(refs),
        "direct_edges": len(direct),
        "direct_edges_validated": len(direct) - len(errors),
        "bibliography_confirmed_forward_edges": len(forward),
        "forward_note": "One confirmed bibliography-only edge: 2607.08505 ref. 40 names SPS, but [40] is absent from the body. It is held from the public direct-lineage graph.",
        "errors": errors,
    }
    (ROOT / "validation_direct_citation_edges.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
