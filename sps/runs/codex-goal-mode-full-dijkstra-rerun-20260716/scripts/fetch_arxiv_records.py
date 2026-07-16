#!/usr/bin/env python3
"""Fetch and preserve fresh arXiv metadata for an auditable search protocol."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"
API = "https://export.arxiv.org/api/query"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean(value: str | None) -> str:
    return " ".join((value or "").split())


def arxiv_id_from_url(url: str) -> tuple[str, str]:
    tail = url.rsplit("/", 1)[-1]
    if "v" in tail:
        base, version = tail.rsplit("v", 1)
        if version.isdigit():
            return base, "v" + version
    return tail, ""


def fetch(url: str) -> tuple[bytes, str]:
    # urllib cannot resolve DNS in this desktop sandbox. curl has the approved
    # network transport here and is intentionally invoked with fixed arguments.
    command = [
        "curl", "--fail", "--silent", "--show-error", "--location",
        "--max-time", "90", "--user-agent",
        "play-the-toy-with-children/part1-audit (contact: local-codex-run)",
        "--write-out", "\n%{http_code}", url,
    ]
    completed = subprocess.run(command, check=True, capture_output=True)
    payload, status = completed.stdout.rsplit(b"\n", 1)
    return payload, status.decode("ascii", errors="replace")


def parse_feed(payload: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(payload)
    entries: list[dict[str, str]] = []
    for entry in root.findall(f"{ATOM}entry"):
        id_url = clean(entry.findtext(f"{ATOM}id"))
        arxiv_id, version = arxiv_id_from_url(id_url)
        categories = [node.attrib.get("term", "") for node in entry.findall(f"{ATOM}category")]
        primary = entry.find(f"{ARXIV}primary_category")
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}{version}"
        entries.append(
            {
                "arxiv_id": arxiv_id,
                "version": version,
                "title": clean(entry.findtext(f"{ATOM}title")),
                "authors": "; ".join(clean(node.findtext(f"{ATOM}name")) for node in entry.findall(f"{ATOM}author")),
                "published": clean(entry.findtext(f"{ATOM}published")),
                "updated": clean(entry.findtext(f"{ATOM}updated")),
                "primary_category": primary.attrib.get("term", "") if primary is not None else "",
                "categories": ";".join(category for category in categories if category),
                "abstract": clean(entry.findtext(f"{ATOM}summary")),
                "canonical_url": f"https://arxiv.org/abs/{arxiv_id}",
                "pdf_url": pdf_url,
            }
        )
    return entries


def query_url(query: dict[str, str]) -> str:
    if query["query_type"] == "id_list":
        parameters = {"id_list": query["expression"], "max_results": query["max_results"]}
    else:
        parameters = {
            "search_query": query["expression"],
            "start": "0",
            "max_results": query["max_results"],
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    return API + "?" + urllib.parse.urlencode(parameters)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--delay-seconds", type=float, default=3.1)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    raw_dir = run_dir / "raw" / "arxiv"
    raw_dir.mkdir(parents=True, exist_ok=True)
    protocol = read_csv(run_dir / "search_protocol.csv")
    probes = read_csv(run_dir / "identifier_probes.csv")
    jobs: list[dict[str, str]] = []
    jobs.extend(protocol)
    for probe in probes:
        jobs.append({
            "query_id": probe["probe_id"], "round": probe["round"], "family": probe["family"],
            "facet": "identifier_probe", "query_type": "id_list", "expression": probe["arxiv_id"],
            "max_results": "1", "why": probe["reason"],
        })

    fetched_at = datetime.now(timezone.utc).isoformat()
    retrieval_log: list[dict[str, object]] = []
    route_results: list[dict[str, object]] = []
    records: dict[str, dict[str, object]] = {}
    route_meta = {row["query_id"]: row for row in jobs}
    for index, job in enumerate(jobs):
        url = query_url(job)
        raw_path = raw_dir / f"{job['query_id']}.xml"
        started = time.monotonic()
        status = "OK"
        error = ""
        entries: list[dict[str, str]] = []
        payload = b""
        try:
            payload, http_status = fetch(url)
            raw_path.write_bytes(payload)
            entries = parse_feed(payload)
        except (subprocess.CalledProcessError, ET.ParseError, TimeoutError, ValueError) as exc:
            status = "ERROR"
            http_status = ""
            error = f"{type(exc).__name__}: {exc}"
        retrieval_log.append({
            "route_id": job["query_id"], "round": job["round"], "family": job["family"],
            "query_type": job["query_type"], "expression": job["expression"], "url": url,
            "retrieved_at_utc": fetched_at, "http_status": http_status, "status": status,
            "entries": len(entries), "raw_file": str(raw_path.relative_to(run_dir)),
            "sha256": hashlib.sha256(payload).hexdigest() if payload else "", "elapsed_seconds": round(time.monotonic() - started, 3),
            "error": error,
        })
        for rank, entry in enumerate(entries, 1):
            route_results.append({
                "route_id": job["query_id"], "round": job["round"], "family": job["family"],
                "facet": job["facet"], "rank": rank, "arxiv_id": entry["arxiv_id"],
                "version": entry["version"], "title": entry["title"], "authors": entry["authors"],
                "published": entry["published"], "primary_category": entry["primary_category"],
                "abstract": entry["abstract"], "canonical_url": entry["canonical_url"],
                "pdf_url": entry["pdf_url"], "raw_file": str(raw_path.relative_to(run_dir)),
            })
            aggregate = records.setdefault(entry["arxiv_id"], {**entry, "route_ids": set(), "families": set(), "rounds": set(), "raw_files": set()})
            aggregate["route_ids"].add(job["query_id"])
            aggregate["families"].add(job["family"])
            aggregate["rounds"].add(job["round"])
            aggregate["raw_files"].add(str(raw_path.relative_to(run_dir)))
        if index + 1 < len(jobs):
            time.sleep(args.delay_seconds)

    metadata_rows = []
    for arxiv_id, row in sorted(records.items(), key=lambda item: item[0]):
        metadata_rows.append({
            "arxiv_id": arxiv_id,
            "version": row["version"], "title": row["title"], "authors": row["authors"],
            "published": row["published"], "updated": row["updated"],
            "primary_category": row["primary_category"], "categories": row["categories"],
            "abstract": row["abstract"], "canonical_url": row["canonical_url"], "pdf_url": row["pdf_url"],
            "route_ids": ";".join(sorted(row["route_ids"])), "families": ";".join(sorted(row["families"])),
            "rounds": ";".join(sorted(row["rounds"])), "raw_files": ";".join(sorted(row["raw_files"])),
            "retrieved_at_utc": fetched_at,
        })
    write_csv(run_dir / "retrieval_log.csv", retrieval_log, [
        "route_id", "round", "family", "query_type", "expression", "url", "retrieved_at_utc", "http_status", "status", "entries", "raw_file", "sha256", "elapsed_seconds", "error",
    ])
    write_csv(run_dir / "route_results.csv", route_results, [
        "route_id", "round", "family", "facet", "rank", "arxiv_id", "version", "title", "authors", "published", "primary_category", "abstract", "canonical_url", "pdf_url", "raw_file",
    ])
    write_csv(run_dir / "fresh_arxiv_metadata.csv", metadata_rows, [
        "arxiv_id", "version", "title", "authors", "published", "updated", "primary_category", "categories", "abstract", "canonical_url", "pdf_url", "route_ids", "families", "rounds", "raw_files", "retrieved_at_utc",
    ])
    yield_rows = []
    for route_id, meta in route_meta.items():
        hits = [row for row in route_results if row["route_id"] == route_id]
        yield_rows.append({
            "route_id": route_id, "round": meta["round"], "family": meta["family"], "facet": meta["facet"],
            "raw_hits": len(hits), "unique_hits": len({row["arxiv_id"] for row in hits}),
            "status": next((row["status"] for row in retrieval_log if row["route_id"] == route_id), "MISSING"),
        })
    write_csv(run_dir / "query_yield_log.csv", yield_rows, ["route_id", "round", "family", "facet", "raw_hits", "unique_hits", "status"])
    summary = {
        "retrieved_at_utc": fetched_at,
        "routes_requested": len(jobs),
        "routes_ok": sum(row["status"] == "OK" for row in retrieval_log),
        "raw_hits": len(route_results),
        "deduplicated_records": len(metadata_rows),
        "error_routes": [row["route_id"] for row in retrieval_log if row["status"] != "OK"],
    }
    (run_dir / "fetch_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, sort_keys=True))
    return 0 if summary["routes_ok"] == len(jobs) else 2


if __name__ == "__main__":
    raise SystemExit(main())
