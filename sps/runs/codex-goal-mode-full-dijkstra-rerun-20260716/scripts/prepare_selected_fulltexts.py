#!/usr/bin/env python3
"""Build the fixed full-text reading plan from fresh metadata."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str], delimiter: str = ",") -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter=delimiter, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    metadata = {row["arxiv_id"]: row for row in read_csv(run_dir / "fresh_arxiv_metadata.csv")}
    screen = {row["arxiv_id"]: row for row in read_csv(run_dir / "candidate_screening_table.csv")}
    targets = read_csv(run_dir / "reading_targets.csv")
    rows = []
    jobs = []
    for index, target in enumerate(targets, 1):
        arxiv_id = target["arxiv_id"]
        if arxiv_id not in metadata:
            raise SystemExit(f"Reading target was not found in current metadata: {arxiv_id}")
        if screen[arxiv_id]["decision"] not in {"include", "candidate"}:
            raise SystemExit(f"Reading target did not pass C0-C2: {arxiv_id}")
        item = metadata[arxiv_id]
        row = {
            "paper_id": f"P{index:03d}",
            "arxiv_id": arxiv_id,
            "target_level": target["target_level"],
            "cluster": target["cluster"],
            "selection_reason": target["selection_reason"],
            "title": item["title"],
            "authors": item["authors"],
            "published": item["published"],
            "version": item["version"],
            "canonical_url": item["canonical_url"],
            "pdf_url": item["pdf_url"],
            "screen_rank": screen[arxiv_id]["screen_rank"],
            "screen_score": screen[arxiv_id]["screen_score"],
            "screen_decision": screen[arxiv_id]["decision"],
            "route_ids": item["route_ids"],
        }
        rows.append(row)
        jobs.append({
            "paper_id": row["paper_id"],
            "arxiv_id": arxiv_id,
            "pdf_url": item["pdf_url"],
            "pdf_file": f"sources/pdfs/{arxiv_id}.pdf",
            "text_file": f"sources/text/{arxiv_id}.txt",
        })
    write_csv(run_dir / "selected_fulltexts.csv", rows, list(rows[0]))
    write_csv(run_dir / "download_jobs.tsv", jobs, list(jobs[0]), delimiter="\t")
    c4 = sum(row["target_level"] == "C4" for row in rows)
    lines = [
        "# Full-Text Reading Plan",
        "",
        f"- selected papers: {len(rows)}",
        f"- C4 claim-anchor targets: {c4}",
        f"- C3 source-check targets: {len(rows) - c4}",
        "",
        "The C4 label is a planned reading depth, not a claim that a paper has already",
        "been read. A paper changes to C3 only after the current PDF, page count, checksum,",
        "and text extraction are recorded; it changes to C4 only after an anchored note exists.",
        "",
        "| paper | level | cluster | reason |",
        "|---|---|---|---|",
    ]
    for row in rows:
        lines.append(f"| {row['arxiv_id']} | {row['target_level']} | {row['cluster']} | {row['selection_reason']} |")
    (run_dir / "reading_plan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"selected={len(rows)} planned_c4={c4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
