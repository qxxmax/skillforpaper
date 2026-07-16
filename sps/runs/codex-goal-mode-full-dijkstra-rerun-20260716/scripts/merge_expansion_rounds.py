#!/usr/bin/env python3
"""Merge L5-L10 discovery outputs with the initial raw discovery tables."""

from __future__ import annotations

import argparse
import csv
import shutil
from pathlib import Path


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def split_set(value: str) -> set[str]:
    return {part for part in value.split(";") if part}


def expansion_relative_path(value: str) -> str:
    """Make paths from the expansion sub-run valid from the run root."""
    return value if value.startswith("expansion/") else f"expansion/{value}"


def normalize_expansion_file_set(value: str, expansion_ids: set[str]) -> str:
    normalized = []
    for item in split_set(value):
        route_id = Path(item).stem
        normalized.append(expansion_relative_path(item) if route_id in expansion_ids else item)
    return ";".join(normalized)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    expansion = run_dir / "expansion"
    logs = run_dir / "logs"
    logs.mkdir(exist_ok=True)
    for filename in ("route_results.csv", "fresh_arxiv_metadata.csv", "query_yield_log.csv", "retrieval_log.csv"):
        source = run_dir / filename
        target = logs / f"before_L5_L10_{filename}"
        if source.exists() and not target.exists():
            shutil.copy2(source, target)
    base_routes, route_fields = read_csv(run_dir / "route_results.csv")
    expansion_routes, _ = read_csv(expansion / "route_results.csv")
    expansion_ids = {row["route_id"] for row in expansion_routes}
    for row in base_routes:
        if row["route_id"] in expansion_ids:
            row["raw_file"] = expansion_relative_path(row["raw_file"])
    for row in expansion_routes:
        row["raw_file"] = expansion_relative_path(row["raw_file"])
    all_routes = base_routes + expansion_routes
    dedup_route: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in all_routes:
        dedup_route[(row["route_id"], row["arxiv_id"], row["version"])] = row
    merged_routes = sorted(
        dedup_route.values(),
        key=lambda row: (row["route_id"], int(row["rank"]), row["arxiv_id"]),
    )
    write_csv(run_dir / "route_results.csv", merged_routes, route_fields)

    base_meta, meta_fields = read_csv(run_dir / "fresh_arxiv_metadata.csv")
    for row in base_meta:
        row["raw_files"] = normalize_expansion_file_set(row["raw_files"], expansion_ids)
    expansion_meta, _ = read_csv(expansion / "fresh_arxiv_metadata.csv")
    for row in expansion_meta:
        row["raw_files"] = ";".join(
            expansion_relative_path(item) for item in split_set(row["raw_files"])
        )
    combined: dict[str, dict[str, object]] = {}
    for row in base_meta + expansion_meta:
        item = combined.setdefault(
            row["arxiv_id"],
            {**row, "route_ids": set(), "families": set(), "rounds": set(), "raw_files": set()},
        )
        for field in ("route_ids", "families", "rounds", "raw_files"):
            item[field].update(split_set(row[field]))
    merged_meta = []
    for arxiv_id, item in sorted(combined.items()):
        output = dict(item)
        for field in ("route_ids", "families", "rounds", "raw_files"):
            output[field] = ";".join(sorted(item[field]))
        merged_meta.append(output)
    write_csv(run_dir / "fresh_arxiv_metadata.csv", merged_meta, meta_fields)

    base_yields, yield_fields = read_csv(run_dir / "query_yield_log.csv")
    expansion_yields, _ = read_csv(expansion / "query_yield_log.csv")
    yield_map = {row["route_id"]: row for row in base_yields + expansion_yields}
    write_csv(run_dir / "query_yield_log.csv", [yield_map[key] for key in sorted(yield_map)], yield_fields)

    base_logs, log_fields = read_csv(run_dir / "retrieval_log.csv")
    expansion_logs, _ = read_csv(expansion / "retrieval_log.csv")
    for row in expansion_logs:
        row["raw_file"] = expansion_relative_path(row["raw_file"])
        row["error_file"] = expansion_relative_path(row["error_file"])
    all_logs = base_logs + expansion_logs
    write_csv(run_dir / "retrieval_log_all_rounds.csv", all_logs, log_fields)
    print(f"routes={len(merged_routes)} records={len(merged_meta)} added_routes={len(expansion_routes)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
