#!/usr/bin/env python3
"""Validate temporary recovery downloads and atomically restore selected PDFs."""

from __future__ import annotations

import csv
import hashlib
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "sources" / "pdfs"


def page_count(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True, errors="replace")
    for line in info.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1])
    raise ValueError(f"No page count for {path}")


def main() -> None:
    selected = list(csv.DictReader((ROOT / "selected_fulltexts.csv").open(encoding="utf-8")))
    rows: list[dict[str, str | int]] = []
    recovered: list[str] = []
    for item in selected:
        arxiv_id = item["arxiv_id"]
        target = PDF_DIR / f"{arxiv_id}.pdf"
        temporary = PDF_DIR / f"{arxiv_id}.pdf.part"
        if temporary.exists():
            page_count(temporary)
            temporary.replace(target)
            recovered.append(arxiv_id)
        pages = page_count(target)
        digest = hashlib.sha256(target.read_bytes()).hexdigest()
        rows.append(
            {
                "arxiv_id": arxiv_id,
                "title": item["title"],
                "selection_reason": item["selection_reason"],
                "status": "verified_pdf",
                "pages": pages,
                "bytes": target.stat().st_size,
                "sha256": digest,
                "pdf_path": str(target.relative_to(ROOT)),
                "error": "",
            }
        )
    fields = list(rows[0])
    with (ROOT / "fulltext_download_status.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"selected={len(rows)} verified={len(rows)} recovered={','.join(recovered)} pages={sum(int(r['pages']) for r in rows)}")


if __name__ == "__main__":
    main()
