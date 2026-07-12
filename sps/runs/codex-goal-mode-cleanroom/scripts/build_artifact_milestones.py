#!/usr/bin/env python3
"""Record current-run artifact creation milestones from filesystem metadata."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
START_EPOCH = 1783868382
MILESTONES = [
    ("contract", "cleanroom_contract.md"),
    ("root_identity", "root_identity.md"),
    ("query_matrix", "query_matrix.csv"),
    ("fulltext_selection", "selected_fulltexts.csv"),
    ("pdf_verification", "fulltext_download_status.csv"),
    ("manual_evidence", "manual_reading_notes.csv"),
    ("research_report", "literature_research_report.md"),
    ("audit_workbook", "sps_literature_audit_cleanroom.xlsx"),
]


def main() -> None:
    rows = []
    for event, relative_path in MILESTONES:
        path = ROOT / relative_path
        epoch = int(path.stat().st_mtime)
        rows.append(
            {
                "event": event,
                "artifact": relative_path,
                "epoch": epoch,
                "iso8601_local": datetime.fromtimestamp(epoch).astimezone().isoformat(timespec="seconds"),
                "elapsed_from_cleanroom_start_seconds": epoch - START_EPOCH,
                "measurement_kind": "artifact_mtime_not_stage_runtime",
            }
        )
    with (ROOT / "logs" / "artifact_milestones.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"milestones={len(rows)}")


if __name__ == "__main__":
    main()
