#!/usr/bin/env python3
"""Execute and retain the matched 30+6 query routes."""

from __future__ import annotations

import csv
import json
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "sources/metadata"
RAW.mkdir(parents=True, exist_ok=True)
UA = "SPS-literature-audit/1.0 (research reproducibility)"


def fetch_json(url: str) -> tuple[dict, int]:
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=45) as response:
        body = response.read()
    return json.loads(body), len(body)


def stamp() -> tuple[int, str]:
    epoch = int(time.time())
    return epoch, datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:%S%z")


def main() -> None:
    routes = list(csv.DictReader((ROOT / "query_matrix.csv").open(encoding="utf-8")))
    network_rows = []
    yield_rows = []
    result_rows = []
    root_id = ""
    op_index = 7

    for route in routes:
        query_id = route["QueryID"]
        source = route["TargetSource"]
        query = route["QueryString"]
        try:
            if query_id == "F04":
                if not root_id:
                    raise RuntimeError("root OpenAlex work ID unavailable")
                url = f"https://api.openalex.org/works/{root_id}"
                payload, byte_count = fetch_json(url)
                works = [{"id": item} for item in payload.get("referenced_works", [])]
                raw_hits = len(works)
            elif query_id == "F05":
                if not root_id:
                    raise RuntimeError("root OpenAlex work ID unavailable")
                short_id = root_id.rsplit("/", 1)[-1]
                url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": f"cites:{short_id}", "per-page": 50})
                payload, byte_count = fetch_json(url)
                works = payload.get("results", [])
                raw_hits = payload.get("meta", {}).get("count", len(works))
            elif source == "Crossref":
                url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.title": query, "rows": 20})
                payload, byte_count = fetch_json(url)
                works = payload.get("message", {}).get("items", [])
                raw_hits = payload.get("message", {}).get("total-results", len(works))
            elif source == "arXiv":
                url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "start": 0, "max_results": 25})
                request = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(request, timeout=45) as response:
                    body = response.read()
                payload = {"atom_xml": body.decode("utf-8", "replace")}
                byte_count = len(body)
                raw_hits = payload["atom_xml"].count("<entry>")
                works = []
            else:
                url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": query, "per-page": 25})
                payload, byte_count = fetch_json(url)
                works = payload.get("results", [])
                raw_hits = payload.get("meta", {}).get("count", len(works))
                if query_id == "F01" and works:
                    root_id = works[0].get("id", "")

            (RAW / f"{query_id}.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
            epoch, iso = stamp()
            network_rows.append({
                "operation_id": f"N{op_index:03d}", "epoch": epoch, "channel": source.lower(), "method": "GET",
                "endpoint_or_query": query, "outcome": "success", "result_count": raw_hits,
                "bytes": byte_count, "path_or_evidence": f"sources/metadata/{query_id}.json", "note": query_id,
            })
            yield_rows.append({
                "QueryID": query_id, "ExecutedAt": iso, "RawHits": raw_hits,
                "DeduplicatedHits": len(works), "ScreenedHits": len(works), "IncludedHits": "pending_pool_screen",
                "NewTerms": "", "NewFacets": route["ExpectedFacet"], "NoisePatterns": "",
                "Decision": "retain_for_screening", "NextAction": "deduplicate_and_screen",
            })
            for rank, work in enumerate(works, 1):
                ids = work.get("ids", {}) if isinstance(work, dict) else {}
                result_rows.append({
                    "QueryID": query_id,
                    "Rank": rank,
                    "SourceID": work.get("id", ""),
                    "DOI": work.get("DOI", "") or work.get("doi", "") or ids.get("doi", ""),
                    "Title": work.get("title", "") or work.get("display_name", ""),
                    "Year": work.get("publication_year", "") or work.get("published-print", "") or work.get("published-online", ""),
                    "CitedByCount": work.get("cited_by_count", ""),
                    "PrimaryURL": (work.get("primary_location") or {}).get("landing_page_url", "") if isinstance(work.get("primary_location"), dict) else work.get("URL", ""),
                })
        except Exception as exc:
            epoch, iso = stamp()
            network_rows.append({
                "operation_id": f"N{op_index:03d}", "epoch": epoch, "channel": source.lower(), "method": "GET",
                "endpoint_or_query": query, "outcome": f"failed:{type(exc).__name__}", "result_count": 0,
                "bytes": 0, "path_or_evidence": "", "note": f"{query_id}: {exc}",
            })
            yield_rows.append({
                "QueryID": query_id, "ExecutedAt": iso, "RawHits": 0, "DeduplicatedHits": 0,
                "ScreenedHits": 0, "IncludedHits": 0, "NewTerms": "", "NewFacets": "",
                "NoisePatterns": "request_failure", "Decision": "failed", "NextAction": "record limitation",
            })
        op_index += 1
        time.sleep(0.12)

    for path, rows in [
        (ROOT / "query_yield_log.csv", yield_rows),
        (ROOT / "route_results.csv", result_rows),
    ]:
        with path.open("w", newline="", encoding="utf-8") as handle:
            if rows:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)

    with (ROOT / "network_access_log.csv").open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "operation_id", "epoch", "channel", "method", "endpoint_or_query", "outcome",
            "result_count", "bytes", "path_or_evidence", "note",
        ])
        writer.writerows(network_rows)


if __name__ == "__main__":
    main()
