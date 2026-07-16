#!/usr/bin/env python3
"""Prepare encoded API jobs; no network access occurs in this step."""

from __future__ import annotations

import argparse
import csv
import urllib.parse
from pathlib import Path


API = "https://export.arxiv.org/api/query"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    protocol = read_csv(run_dir / "search_protocol.csv")
    probes = read_csv(run_dir / "identifier_probes.csv")
    jobs = list(protocol)
    for probe in probes:
        jobs.append({
            "query_id": probe["probe_id"],
            "round": probe["round"],
            "family": probe["family"],
            "facet": "identifier_probe",
            "query_type": "id_list",
            "expression": probe["arxiv_id"],
            "max_results": "1",
        })
    output = run_dir / "transport_jobs.tsv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            lineterminator="\n",
            fieldnames=[
                "route_id", "round", "family", "facet", "query_type",
                "expression", "url", "raw_file",
            ],
        )
        writer.writeheader()
        for job in jobs:
            if job["query_type"] == "id_list":
                parameters = {"id_list": job["expression"], "max_results": job["max_results"]}
            else:
                parameters = {
                    "search_query": job["expression"],
                    "start": "0",
                    "max_results": job["max_results"],
                    "sortBy": "submittedDate",
                    "sortOrder": "descending",
                }
            writer.writerow({
                "route_id": job["query_id"],
                "round": job["round"],
                "family": job["family"],
                "facet": job["facet"],
                "query_type": job["query_type"],
                "expression": job["expression"],
                "url": API + "?" + urllib.parse.urlencode(parameters),
                "raw_file": f"raw/arxiv/{job['query_id']}.xml",
            })
    print(f"prepared {len(jobs)} arXiv transport jobs in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
