#!/usr/bin/env python3
"""Parse raw arXiv transport files into preserved route and metadata tables."""

from __future__ import annotations

import argparse
import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path


ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean(value: str | None) -> str:
    return " ".join((value or "").split())


def split_id(value: str) -> tuple[str, str]:
    tail = value.rsplit("/", 1)[-1]
    if "v" in tail:
        base, version = tail.rsplit("v", 1)
        if version.isdigit():
            return base, "v" + version
    return tail, ""


def parse_feed(path: Path) -> list[dict[str, str]]:
    root = ET.parse(path).getroot()
    result: list[dict[str, str]] = []
    for entry in root.findall(f"{ATOM}entry"):
        arxiv_id, version = split_id(clean(entry.findtext(f"{ATOM}id")))
        primary = entry.find(f"{ARXIV}primary_category")
        result.append({
            "arxiv_id": arxiv_id,
            "version": version,
            "title": clean(entry.findtext(f"{ATOM}title")),
            "authors": "; ".join(clean(node.findtext(f"{ATOM}name")) for node in entry.findall(f"{ATOM}author")),
            "published": clean(entry.findtext(f"{ATOM}published")),
            "updated": clean(entry.findtext(f"{ATOM}updated")),
            "primary_category": primary.attrib.get("term", "") if primary is not None else "",
            "categories": ";".join(node.attrib.get("term", "") for node in entry.findall(f"{ATOM}category")),
            "abstract": clean(entry.findtext(f"{ATOM}summary")),
            "canonical_url": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}{version}",
        })
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    status_rows = read_tsv(run_dir / "transport_status.tsv")
    route_results: list[dict[str, object]] = []
    aggregate: dict[str, dict[str, object]] = {}
    parse_failures: list[str] = []
    for status in status_rows:
        if status["status"] != "OK":
            continue
        raw_path = run_dir / status["raw_file"]
        try:
            entries = parse_feed(raw_path)
        except (ET.ParseError, OSError) as exc:
            parse_failures.append(f"{status['route_id']}: {type(exc).__name__}: {exc}")
            continue
        for rank, entry in enumerate(entries, 1):
            route_results.append({
                "route_id": status["route_id"], "round": status["round"], "family": status["family"],
                "facet": status["facet"], "rank": rank, **entry, "raw_file": status["raw_file"],
            })
            row = aggregate.setdefault(entry["arxiv_id"], {
                **entry, "route_ids": set(), "families": set(), "rounds": set(), "raw_files": set(),
            })
            row["route_ids"].add(status["route_id"])
            row["families"].add(status["family"])
            row["rounds"].add(status["round"])
            row["raw_files"].add(status["raw_file"])
    metadata_rows = []
    for arxiv_id, row in sorted(aggregate.items()):
        metadata_rows.append({
            "arxiv_id": arxiv_id,
            "version": row["version"], "title": row["title"], "authors": row["authors"],
            "published": row["published"], "updated": row["updated"],
            "primary_category": row["primary_category"], "categories": row["categories"],
            "abstract": row["abstract"], "canonical_url": row["canonical_url"], "pdf_url": row["pdf_url"],
            "route_ids": ";".join(sorted(row["route_ids"])),
            "families": ";".join(sorted(row["families"])),
            "rounds": ";".join(sorted(row["rounds"])),
            "raw_files": ";".join(sorted(row["raw_files"])),
        })
    write_csv(run_dir / "route_results.csv", route_results, [
        "route_id", "round", "family", "facet", "rank", "arxiv_id", "version", "title", "authors",
        "published", "updated", "primary_category", "categories", "abstract", "canonical_url", "pdf_url", "raw_file",
    ])
    write_csv(run_dir / "fresh_arxiv_metadata.csv", metadata_rows, [
        "arxiv_id", "version", "title", "authors", "published", "updated", "primary_category", "categories",
        "abstract", "canonical_url", "pdf_url", "route_ids", "families", "rounds", "raw_files",
    ])
    write_csv(run_dir / "retrieval_log.csv", status_rows, [
        "route_id", "round", "family", "facet", "query_type", "expression", "url", "retrieved_at_utc",
        "http_status", "status", "bytes", "sha256", "raw_file", "error_file",
    ])
    yield_rows = []
    for status in status_rows:
        hits = [row for row in route_results if row["route_id"] == status["route_id"]]
        yield_rows.append({
            "route_id": status["route_id"], "round": status["round"], "family": status["family"],
            "facet": status["facet"], "raw_hits": len(hits), "unique_hits": len({row["arxiv_id"] for row in hits}),
            "status": status["status"],
        })
    write_csv(run_dir / "query_yield_log.csv", yield_rows, [
        "route_id", "round", "family", "facet", "raw_hits", "unique_hits", "status",
    ])
    summary = {
        "transport_routes": len(status_rows),
        "transport_ok": sum(row["status"] == "OK" for row in status_rows),
        "raw_hits": len(route_results),
        "deduplicated_records": len(metadata_rows),
        "parse_failures": parse_failures,
    }
    (run_dir / "fetch_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0 if not parse_failures and summary["transport_ok"] == len(status_rows) else 2


if __name__ == "__main__":
    raise SystemExit(main())
