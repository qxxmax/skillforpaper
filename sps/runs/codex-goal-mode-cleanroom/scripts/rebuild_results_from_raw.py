#!/usr/bin/env python3
"""Rebuild route results from successful raw responses retained in this run."""

from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("execute_queries", ROOT / "scripts/execute_queries.py")
module = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(module)


def main() -> None:
    routes = list(csv.DictReader((ROOT / "query_matrix.csv").open(encoding="utf-8")))
    rows = []
    yields = []
    missing = []
    for route in routes:
        qid = route["query_id"]
        if route["source"] == "root_bibliography":
            parsed = module.bibliography_rows(route)
        elif route["source"] in {"OpenAlex", "Crossref"}:
            path = ROOT / "sources/metadata" / f"{qid}.json"
            if not path.exists():
                missing.append(qid); continue
            payload = json.loads(path.read_text(encoding="utf-8"))
            parsed = module.openalex_rows(payload, route) if route["source"] == "OpenAlex" else module.crossref_rows(payload, route)
        elif route["source"] == "arXiv":
            path = ROOT / "sources/metadata" / f"{qid}.xml"
            if not path.exists():
                missing.append(qid); continue
            parsed = module.arxiv_rows(path.read_bytes(), route)
        else:
            missing.append(qid); continue
        rows.extend(parsed)
        yields.append({"query_id": qid, "raw_hits": len(parsed), "status": "success_from_current_raw",
                       "new_facet": route["facet"], "next_action": "deduplicate_and_score",
                       "raw_artifact": f"sources/metadata/{qid}" if route["source"] != "root_bibliography" else "root_bibliography.csv"})
    if missing:
        raise SystemExit(f"Missing current-run raw responses: {missing}")
    fields = ["query_id", "family", "facet", "rank", "source", "source_id", "doi", "arxiv_id", "title", "authors", "year", "cited_by_count", "abstract", "primary_url", "provenance"]
    rows.sort(key=lambda row: (int(row["query_id"][1:]), int(row["rank"] or 0)))
    with (ROOT / "route_results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(rows)
    with (ROOT / "query_yield_log.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(yields[0])); writer.writeheader(); writer.writerows(yields)
    print(f"routes={len(routes)} rows={len(rows)} missing=0")


if __name__ == "__main__":
    main()
