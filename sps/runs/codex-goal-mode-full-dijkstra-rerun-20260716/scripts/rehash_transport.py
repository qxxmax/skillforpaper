#!/usr/bin/env python3
"""Fill SHA-256 fields from already downloaded raw transport files."""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    path = run_dir / "transport_status.tsv"
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
        fields = reader.fieldnames or []
    rehashed = 0
    for row in rows:
        if row.get("status") != "OK":
            continue
        source = run_dir / row["raw_file"]
        row["sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        rehashed += 1
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"rehashed={rehashed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
