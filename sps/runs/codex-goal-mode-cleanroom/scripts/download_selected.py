#!/usr/bin/env python3
"""Download and validate full texts selected by the current screening table."""

from __future__ import annotations

import csv
import hashlib
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "sources/pdfs"
PDF_DIR.mkdir(parents=True, exist_ok=True)


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True, errors="replace")
    for line in output.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1])
    raise ValueError("Pages field missing")


def main() -> None:
    selected = list(csv.DictReader((ROOT / "selected_fulltexts.csv").open(encoding="utf-8")))
    statuses = []
    network = []
    for index, row in enumerate(selected, 1):
        arxiv_id = row["arxiv_id"]
        target = PDF_DIR / f"{arxiv_id}.pdf"
        epoch = int(time.time())
        try:
            if target.exists() and target.stat().st_size > 10_000:
                page_count = pages(target)
                route = "reuse current-run verified PDF"
            elif arxiv_id == "2606.13790":
                shutil.copyfile(ROOT / "sources/root/2606.13790.pdf", target)
                route = "copy current-run root PDF"
            else:
                temporary = target.with_suffix(".pdf.part")
                subprocess.run([
                    "curl", "-sS", "-L", "--fail", "--retry", "5", "--retry-delay", "3",
                    row["pdf_url"], "-o", str(temporary),
                ], check=True)
                pages(temporary)
                temporary.replace(target)
                route = row["pdf_url"]
            page_count = pages(target)
            digest = hashlib.sha256(target.read_bytes()).hexdigest()
            status = "verified_pdf"
            error = ""
            outcome = "success"
        except Exception as exc:
            page_count = 0; digest = ""; status = "failed"; error = f"{type(exc).__name__}: {exc}"; outcome = "failed"
            temporary = target.with_suffix(".pdf.part")
            if temporary.exists():
                temporary.unlink()
        statuses.append({
            "arxiv_id": arxiv_id, "title": row["title"], "selection_reason": row["selection_reason"],
            "status": status, "pages": page_count, "bytes": target.stat().st_size if target.exists() else 0,
            "sha256": digest, "pdf_path": str(target.relative_to(ROOT)) if target.exists() else "", "error": error,
        })
        network.append({
            "operation_id": f"D{index:03d}", "epoch": epoch, "channel": "arXiv", "method": "GET",
            "query_or_url": route, "outcome": outcome, "result_count": int(outcome == "success"),
            "bytes": target.stat().st_size if target.exists() else 0,
            "artifact": str(target.relative_to(ROOT)) if target.exists() else "", "note": arxiv_id,
        })
        time.sleep(0.8)
    with (ROOT / "fulltext_download_status.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(statuses[0])); writer.writeheader(); writer.writerows(statuses)
    with (ROOT / "logs/network_access_log.csv").open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(network[0])); writer.writerows(network)
    good = sum(row["status"] == "verified_pdf" for row in statuses)
    print(f"selected={len(selected)} verified={good} failed={len(selected)-good}")
    if good < 24:
        raise SystemExit("Fewer than 24 verified full texts")


if __name__ == "__main__":
    main()
