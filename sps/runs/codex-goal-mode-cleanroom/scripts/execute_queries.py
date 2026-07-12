#!/usr/bin/env python3
"""Execute the current-run query matrix and retain raw metadata and provenance."""

from __future__ import annotations

import csv
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "sources/metadata"
RAW.mkdir(parents=True, exist_ok=True)
UA = "cleanroom-sps-literature-research/1.0 (source audit)"
ATOM = {"a": "http://www.w3.org/2005/Atom"}


def fetch(url: str, accept: str = "application/json") -> tuple[bytes, int]:
    request = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    last: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read()
            return body, len(body)
        except Exception as exc:
            last = exc
            if attempt == 3:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError(last)


def invert_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positions = []
    for word, locs in index.items():
        for loc in locs:
            positions.append((int(loc), word))
    return " ".join(word for _, word in sorted(positions))


def extract_arxiv(*values: str) -> str:
    for value in values:
        if "arxiv" not in (value or "").lower():
            continue
        match = re.search(r"(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?", value or "")
        if match:
            candidate = match.group(1)
            month = int(candidate[2:4])
            if 1 <= month <= 12:
                return candidate
    return ""


def author_string(authorships: Any) -> str:
    if not isinstance(authorships, list):
        return ""
    return "; ".join((row.get("author") or {}).get("display_name", "") for row in authorships if row.get("author"))


def openalex_rows(payload: dict[str, Any], route: dict[str, str]) -> list[dict[str, Any]]:
    works = payload.get("results", [])
    if "id" in payload and "display_name" in payload:
        works = [payload]
    rows = []
    for rank, work in enumerate(works, 1):
        ids = work.get("ids") or {}
        location = work.get("primary_location") or {}
        landing = location.get("landing_page_url") or ""
        arxiv = extract_arxiv(ids.get("arxiv", ""), landing, work.get("doi", ""))
        rows.append({
            "query_id": route["query_id"], "family": route["family"], "facet": route["facet"],
            "rank": rank, "source": "OpenAlex", "source_id": work.get("id", ""),
            "doi": (work.get("doi") or "").replace("https://doi.org/", ""), "arxiv_id": arxiv,
            "title": work.get("display_name") or work.get("title") or "",
            "authors": author_string(work.get("authorships")), "year": work.get("publication_year") or "",
            "cited_by_count": work.get("cited_by_count") or 0,
            "abstract": invert_abstract(work.get("abstract_inverted_index")),
            "primary_url": landing or work.get("doi") or work.get("id", ""),
            "provenance": "current OpenAlex response",
        })
    return rows


def crossref_rows(payload: dict[str, Any], route: dict[str, str]) -> list[dict[str, Any]]:
    items = (payload.get("message") or {}).get("items", [])
    rows = []
    for rank, item in enumerate(items, 1):
        title = (item.get("title") or [""])[0]
        authors = "; ".join(" ".join(filter(None, [a.get("given"), a.get("family")])) for a in item.get("author", []))
        date_parts = ((item.get("published") or item.get("created") or {}).get("date-parts") or [[""]])[0]
        url = item.get("URL") or ""
        rows.append({
            "query_id": route["query_id"], "family": route["family"], "facet": route["facet"],
            "rank": rank, "source": "Crossref", "source_id": item.get("DOI", ""),
            "doi": item.get("DOI", ""), "arxiv_id": extract_arxiv(url, title), "title": title,
            "authors": authors, "year": date_parts[0] if date_parts else "",
            "cited_by_count": item.get("is-referenced-by-count", 0),
            "abstract": re.sub(r"<[^>]+>", " ", item.get("abstract", "")),
            "primary_url": url, "provenance": "current Crossref response",
        })
    return rows


def arxiv_rows(body: bytes, route: dict[str, str]) -> list[dict[str, Any]]:
    root = ET.fromstring(body)
    rows = []
    for rank, entry in enumerate(root.findall("a:entry", ATOM), 1):
        url = (entry.findtext("a:id", default="", namespaces=ATOM) or "").strip()
        authors = "; ".join((node.findtext("a:name", default="", namespaces=ATOM) or "").strip() for node in entry.findall("a:author", ATOM))
        published = entry.findtext("a:published", default="", namespaces=ATOM)
        rows.append({
            "query_id": route["query_id"], "family": route["family"], "facet": route["facet"],
            "rank": rank, "source": "arXiv", "source_id": url,
            "doi": "", "arxiv_id": extract_arxiv(url),
            "title": re.sub(r"\s+", " ", entry.findtext("a:title", default="", namespaces=ATOM)).strip(),
            "authors": authors, "year": published[:4], "cited_by_count": 0,
            "abstract": re.sub(r"\s+", " ", entry.findtext("a:summary", default="", namespaces=ATOM)).strip(),
            "primary_url": url, "provenance": "current arXiv API response",
        })
    return rows


def bibliography_rows(route: dict[str, str]) -> list[dict[str, Any]]:
    refs = list(csv.DictReader((ROOT / "root_bibliography.csv").open(encoding="utf-8")))
    rows = []
    for rank, ref in enumerate(refs, 1):
        rows.append({
            "query_id": route["query_id"], "family": route["family"], "facet": route["facet"],
            "rank": rank, "source": "root_bibliography", "source_id": ref["bibkey"],
            "doi": ref["doi"], "arxiv_id": ref["arxiv_id"], "title": ref["title"],
            "authors": ref["authors"], "year": ref["year"], "cited_by_count": 0,
            "abstract": "", "primary_url": ref["url"] or (f"https://arxiv.org/abs/{ref['arxiv_id']}" if ref["arxiv_id"] else ""),
            "provenance": f"current root bibliography ref {ref['ref_no']}",
        })
    return rows


def main() -> None:
    routes = list(csv.DictReader((ROOT / "query_matrix.csv").open(encoding="utf-8")))
    previous_rows = []
    previous_path = ROOT / "route_results.csv"
    if previous_path.exists():
        previous_rows = list(csv.DictReader(previous_path.open(encoding="utf-8")))
    previous_by_query: dict[str, list[dict[str, Any]]] = {}
    for row in previous_rows:
        previous_by_query.setdefault(row["query_id"], []).append(row)
    all_rows: list[dict[str, Any]] = []
    yields = []
    network = []
    root_openalex_id = ""
    for op, route in enumerate(routes, 6):
        started = int(time.time())
        query = route["query"]
        try:
            if route["source"] == "root_bibliography":
                rows = bibliography_rows(route); body_len = 0; artifact = "root_bibliography.csv"
            elif route["family"] == "forward":
                if not root_openalex_id:
                    lookup = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": "Stochastic Path Sampler For Lattice Field Theory", "per-page": 10})
                    body, _ = fetch(lookup); lookup_payload = json.loads(body)
                    matches = [w for w in lookup_payload.get("results", []) if extract_arxiv(((w.get("ids") or {}).get("arxiv", "")), (w.get("primary_location") or {}).get("landing_page_url", "")) == "2606.13790"]
                    root_openalex_id = matches[0]["id"].rsplit("/", 1)[-1] if matches else ""
                if not root_openalex_id:
                    rows = []; body_len = 0; artifact = "no_indexed_root"
                else:
                    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": f"cites:{root_openalex_id}", "per-page": 50})
                    body, body_len = fetch(url); payload = json.loads(body)
                    rows = openalex_rows(payload, route); artifact = f"sources/metadata/{route['query_id']}.json"
                    (ROOT / artifact).write_text(json.dumps(payload, indent=2), encoding="utf-8")
            elif route["source"] == "OpenAlex":
                url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"search": query.strip('"'), "per-page": 25})
                body, body_len = fetch(url); payload = json.loads(body)
                rows = openalex_rows(payload, route); artifact = f"sources/metadata/{route['query_id']}.json"
                (ROOT / artifact).write_text(json.dumps(payload, indent=2), encoding="utf-8")
                if route["query_id"] == "Q01":
                    matches = [r for r in rows if r["arxiv_id"] == "2606.13790"]
                    if matches:
                        root_openalex_id = matches[0]["source_id"].rsplit("/", 1)[-1]
            elif route["source"] == "Crossref":
                url = "https://api.crossref.org/works?" + urllib.parse.urlencode({"query.bibliographic": query.strip('"'), "rows": 20})
                body, body_len = fetch(url); payload = json.loads(body)
                rows = crossref_rows(payload, route); artifact = f"sources/metadata/{route['query_id']}.json"
                (ROOT / artifact).write_text(json.dumps(payload, indent=2), encoding="utf-8")
            elif route["source"] == "arXiv":
                url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": query, "start": 0, "max_results": 25})
                body, body_len = fetch(url, "application/atom+xml")
                rows = arxiv_rows(body, route); artifact = f"sources/metadata/{route['query_id']}.xml"
                (ROOT / artifact).write_bytes(body)
            else:
                raise ValueError(f"Unsupported source {route['source']}")
            all_rows.extend(rows)
            network.append({"operation_id": f"N{op:03d}", "epoch": started, "channel": route["source"], "method": "GET", "query_or_url": query,
                            "outcome": "success", "result_count": len(rows), "bytes": body_len, "artifact": artifact, "note": route["query_id"]})
            yields.append({"query_id": route["query_id"], "executed_at": datetime.now().astimezone().isoformat(), "raw_hits": len(rows),
                           "status": "success", "new_facet": route["facet"], "next_action": "deduplicate_and_score"})
        except Exception as exc:
            network.append({"operation_id": f"N{op:03d}", "epoch": started, "channel": route["source"], "method": "GET", "query_or_url": query,
                            "outcome": f"failed:{type(exc).__name__}", "result_count": 0, "bytes": 0, "artifact": "", "note": f"{route['query_id']}: {exc}"})
            yields.append({"query_id": route["query_id"], "executed_at": datetime.now().astimezone().isoformat(), "raw_hits": 0,
                           "status": "failed", "new_facet": route["facet"], "next_action": "retry_or_record_limit"})
        time.sleep(0.2)

    fields = ["query_id", "family", "facet", "rank", "source", "source_id", "doi", "arxiv_id", "title", "authors", "year", "cited_by_count", "abstract", "primary_url", "provenance"]
    current_success = {row["query_id"] for row in yields if row["status"] == "success"}
    current_failed = {row["query_id"] for row in yields if row["status"] == "failed"}
    for query_id in current_failed:
        retained = previous_by_query.get(query_id, [])
        if retained:
            all_rows.extend(retained)
            for row in yields:
                if row["query_id"] == query_id:
                    row["status"] = "retained_previous_success"
                    row["raw_hits"] = len(retained)
                    row["next_action"] = "retry_for_freshness; retained current-run earlier success"
    all_rows.sort(key=lambda row: (int(row["query_id"][1:]), int(row["rank"] or 0)))
    with (ROOT / "route_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(all_rows)
    with (ROOT / "query_yield_log.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(yields[0])); writer.writeheader(); writer.writerows(yields)
    with (ROOT / "logs/network_access_log.csv").open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(network[0])); writer.writerows(network)
    print(f"queries={len(routes)} results={len(all_rows)} failures={sum(r['status']=='failed' for r in yields)} retained={sum(r['status']=='retained_previous_success' for r in yields)}")


if __name__ == "__main__":
    main()
