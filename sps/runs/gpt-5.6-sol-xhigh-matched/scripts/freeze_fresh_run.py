#!/usr/bin/env python3
"""Freeze the fresh pre-comparison state and record a content digest."""

from __future__ import annotations

import csv
import hashlib
import json
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    records = []
    aggregate = hashlib.sha256()
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or "comparison" in path.parts or path.name in {"fresh_freeze_manifest.json", "FRESH_RESULTS_FROZEN"}:
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        rel = str(path.relative_to(ROOT))
        records.append({"path": rel, "bytes": path.stat().st_size, "sha256": digest})
        aggregate.update(rel.encode())
        aggregate.update(digest.encode())
    epoch = int(time.time())
    pdf_rows = list(csv.DictReader((ROOT / "pdf_inventory.csv").open(encoding="utf-8")))
    payload = {
        "status": "FROZEN_BEFORE_PRIOR_RESULT_INSPECTION",
        "freeze_epoch": epoch,
        "freeze_iso8601": datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z"),
        "start_epoch": 1783850589,
        "elapsed_to_freeze_seconds": epoch - 1783850589,
        "fresh_files": len(records),
        "fresh_bytes": sum(r["bytes"] for r in records),
        "content_digest_sha256": aggregate.hexdigest(),
        "root_references_screened": 58,
        "fresh_query_routes": 30,
        "legacy_query_routes": 6,
        "closure_rounds": 2,
        "primary_pdfs": len(pdf_rows),
        "primary_pdf_pages": sum(int(r["Pages"]) for r in pdf_rows),
        "primary_pdf_bytes": sum(int(r["Bytes"]) for r in pdf_rows),
        "records": records,
    }
    (ROOT / "fresh_freeze_manifest.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    (ROOT / "FRESH_RESULTS_FROZEN").write_text(f"{payload['freeze_iso8601']}\n{payload['content_digest_sha256']}\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in payload if key != "records"}, indent=2))


if __name__ == "__main__":
    main()
