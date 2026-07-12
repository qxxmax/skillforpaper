#!/usr/bin/env python3
"""Run final count, provenance, link, graph and workbook checks."""

from __future__ import annotations

import csv
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    selected = rows("selected_fulltexts.csv")
    pdfs = rows("fulltext_download_status.csv")
    notes = rows("manual_reading_notes.csv")
    evidence = rows("evidence_registry.csv")
    claims = rows("claim_source_ledger.csv")
    numbers = rows("numerical_ledger.csv")
    relations = rows("relation_ledger.csv")
    displayed = rows("display_relation_ledger.csv")
    links = rows("source_link_verification.csv")
    evidence_ids = {row["evidence_id"] for row in evidence}
    selected_ids = {row["arxiv_id"] for row in selected}

    checks = {
        "31_selected_fulltexts": len(selected) == 31,
        "31_verified_pdfs": len(pdfs) == 31 and all(row["status"] == "verified_pdf" for row in pdfs),
        "731_verified_pages": sum(int(row["pages"]) for row in pdfs) == 731,
        "31_manual_reading_rows": len(notes) == 31 and {row["arxiv_id"] for row in notes} == selected_ids,
        "155_evidence_entries": len(evidence) == 155,
        "all_claim_evidence_resolves": all(eid in evidence_ids for row in claims for eid in row["evidence_ids"].split(";")),
        "all_numbers_anchored": len(numbers) == 13 and all(row["source_anchor"] and row["boundary"] and row["evidence_id"] in evidence_ids for row in numbers),
        "all_core_links_canonical": len(links) == 31 and all(row["source_url"].startswith("https://arxiv.org/abs/") and row["status"] == "VERIFIED" for row in links),
        "all_relations_have_checked_basis": len(relations) == 124 and all(row["relation_type"] == "direct_citation" and row["relation_basis"] for row in relations),
        "public_graph_is_subset": len(displayed) == 29 and {(row["source_arxiv_id"], row["target_arxiv_id"]) for row in displayed}.issubset({(row["source_arxiv_id"], row["target_arxiv_id"]) for row in relations}),
        "keyword_query_relation_validator_pass": json.loads((ROOT / "keyword_query_graph_validation.json").read_text(encoding="utf-8"))["status"] == "PASS",
        "dependency_scan_pass": "Status: **PASS**" in (ROOT / "cleanroom_dependency_scan.md").read_text(encoding="utf-8"),
        "graphs_present": all((ROOT / name).stat().st_size > 10_000 for name in ["graphs/landscape_map.png", "graphs/citation_lineage_graph.png", "graphs/audit_funnel.png"]),
        "five_key_source_renders": len(list((ROOT / "screenshots").glob("*.png"))) == 5,
        "workbook_valid_zip": zipfile.is_zipfile(ROOT / "sps_literature_audit_cleanroom.xlsx"),
        "no_partial_downloads": not list((ROOT / "sources" / "pdfs").glob("*.part")),
    }
    result = {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks}
    (ROOT / "final_validation_report.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    lines = ["# Final Validation Report", "", "| Gate | Status |", "|---|---|"]
    lines.extend(f"| {name} | {'PASS' if passed else 'FAIL'} |" for name, passed in checks.items())
    lines.extend(["", f"Overall status: **{result['status']}**"])
    (ROOT / "final_validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
