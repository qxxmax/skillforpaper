#!/usr/bin/env python3
"""Verify downloaded PDFs and create the C3 source and reading ledgers."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
from pathlib import Path


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def title_tokens(title: str) -> list[str]:
    return [
        token for token in re.findall(r"[A-Za-z]{4,}", title.lower())
        if token not in {"with", "from", "that", "into", "theory", "field"}
    ][:6]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    selected = read_csv(run_dir / "selected_fulltexts.csv")
    status = {row["arxiv_id"]: row for row in read_csv(run_dir / "fulltext_download_status.tsv", delimiter="\t")}
    screening = {row["arxiv_id"]: row for row in read_csv(run_dir / "candidate_screening_table.csv")}
    source_rows = []
    verification_rows = []
    packet_rows = []
    failures = []
    for row in selected:
        arxiv_id = row["arxiv_id"]
        download = status.get(arxiv_id)
        if not download:
            failures.append(f"{arxiv_id}: missing download status")
            continue
        pdf_path = run_dir / download["pdf_file"]
        text_path = run_dir / download["text_file"]
        expected_hash = download["sha256"]
        actual_hash = hashlib.sha256(pdf_path.read_bytes()).hexdigest() if pdf_path.exists() else ""
        text = text_path.read_text(encoding="utf-8", errors="replace") if text_path.exists() else ""
        tokens = title_tokens(row["title"])
        title_match = bool(tokens) and sum(token in text[:12000].lower() for token in tokens) >= max(2, len(tokens) // 2)
        status_ok = (
            download["status"] == "OK"
            and actual_hash == expected_hash
            and int(download["page_count"] or 0) > 0
            and len(text.strip()) > 500
        )
        if not status_ok:
            failures.append(f"{arxiv_id}: C3 integrity check failed")
        source_rows.append({
            "paper_id": row["paper_id"],
            "arxiv_id": arxiv_id,
            "title": row["title"],
            "authors": row["authors"],
            "published": row["published"],
            "version": row["version"],
            "family": row["cluster"],
            "target_level": row["target_level"],
            "source_relation": row["selection_reason"],
            "source_url": row["canonical_url"],
            "pdf_url": row["pdf_url"],
            "pdf_path": download["pdf_file"],
            "text_path": download["text_file"],
            "pdf_pages": download["page_count"],
            "pdf_sha256": actual_hash,
            "metadata_title_match": "PASS" if title_match else "FAIL",
            "full_text_integrity": "PASS" if status_ok else "FAIL",
            "full_text_read": "C3_pass" if status_ok else "C3_fail",
            "evidence_level": "C3_full_text",
        })
        verification_rows.append({
            "paper_id": row["paper_id"],
            "arxiv_id": arxiv_id,
            "title": row["title"],
            "C0_candidate": screening[arxiv_id]["C0_candidate"],
            "C1_metadata": screening[arxiv_id]["C1_metadata"],
            "C2_abstract": screening[arxiv_id]["C2_abstract"],
            "C3_full_text": "pass" if status_ok else "fail",
            "C4_claim_anchor": "pending" if row["target_level"] == "C4" else "not_planned",
            "source_url": row["canonical_url"],
            "pdf_sha256": actual_hash,
            "review_status": "full_text_downloaded_and_extracted" if status_ok else "download_or_extraction_failure",
        })
        packet_rows.append({
            "paper_id": row["paper_id"],
            "arxiv_id": arxiv_id,
            "title": row["title"],
            "planned_level": row["target_level"],
            "pdf_pages": download["page_count"],
            "text_characters": len(text),
            "status": "ready_for_anchor_reading" if status_ok else "blocked",
            "selection_reason": row["selection_reason"],
            "pdf_path": download["pdf_file"],
            "text_path": download["text_file"],
        })
    write_csv(run_dir / "source_matrix.csv", source_rows, list(source_rows[0]))
    write_csv(run_dir / "paper_verification_ledger.csv", verification_rows, list(verification_rows[0]))
    write_csv(run_dir / "reading_packet_index.csv", packet_rows, list(packet_rows[0]))
    source_link_rows = [
        {
            "paper_id": row["paper_id"],
            "arxiv_id": row["arxiv_id"],
            "title": row["title"],
            "source_url": row["source_url"],
            "pdf_url": row["pdf_url"],
            "pdf_sha256": row["pdf_sha256"],
            "metadata_title_match": row["metadata_title_match"],
            "full_text_integrity": row["full_text_integrity"],
            "visual_evidence": "pending_key_only_screenshot",
            "status": "VERIFIED_C3" if row["full_text_integrity"] == "PASS" else "FAILED",
        }
        for row in source_rows
    ]
    write_csv(run_dir / "source_link_verification.csv", source_link_rows, list(source_link_rows[0]))
    report = [
        "# C3 Full-Text Gate",
        "",
        f"- selected PDFs: {len(selected)}",
        f"- C3 source-integrity passes: {sum(row['full_text_integrity'] == 'PASS' for row in source_rows)}",
        f"- planned C4 anchor records: {sum(row['target_level'] == 'C4' for row in source_rows)}",
        f"- failures: {len(failures)}",
        "",
        "A C3 pass establishes that the current PDF was downloaded, checksum verified,",
        "page-counted, and text extracted. It does not establish a scientific claim.",
    ]
    if failures:
        report += ["", "## Failures", ""] + [f"- {failure}" for failure in failures]
    (run_dir / "fulltext_gate_report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"c3_pass={len(source_rows)} c4_pending={sum(row['target_level'] == 'C4' for row in source_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
