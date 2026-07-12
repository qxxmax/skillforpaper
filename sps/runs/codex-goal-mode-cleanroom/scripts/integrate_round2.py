#!/usr/bin/env python3
"""Integrate candidates discovered by the current run's gap-driven closure round."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    closure = read_csv(ROOT / "round2_discovered_candidates.csv")
    selected_path = ROOT / "selected_fulltexts.csv"
    selected = read_csv(selected_path)
    fields = list(selected[0])
    existing = {row["candidate_id"] for row in selected}
    before = len(selected)

    for row in closure:
        if row["decision"] != "include" or row["candidate_id"] in existing:
            continue
        selected.append(
            {
                "candidate_id": row["candidate_id"],
                "title": row["title"],
                "authors": row["authors"],
                "year": row["year"],
                "doi": "",
                "arxiv_id": row["arxiv_id"],
                "primary_url": row["primary_url"],
                "facets": "adversarial;evaluation;limitation",
                "families": "closure;diffusion",
                "method_groups": "diffusion;failure;scaling",
                "query_ids": row["query_ids"],
                "route_occurrences": "1",
                "score": "closure",
                "decision": "include",
                "screen_reason": row["reason"],
                "provenance": row["provenance"],
                "selection_reason": "round2_gap_closure",
                "pdf_url": f"https://arxiv.org/pdf/{row['arxiv_id']}",
            }
        )
        existing.add(row["candidate_id"])

    write_csv(selected_path, selected, fields)
    print(f"selected={len(selected)}; closure_added={len(selected) - before}")


if __name__ == "__main__":
    main()
