#!/usr/bin/env python3
"""Register the deliberately small set of source-page screenshots."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()

    # This is a key-only visual check. Full-text checks for every selected source
    # live in the C3 gate; screenshots are not substituted for those checks.
    entries = [
        {
            "arxiv_id": "2606.13790",
            "role": "root_identity",
            "screenshot": "screenshots/2606.13790_p1_identity.png",
            "physical_pdf_page": "1",
            "checked_element": "title, authors, date/version, and abstract opening",
            "source_url": "https://arxiv.org/abs/2606.13790",
            "visual_result": "PASS",
        },
        {
            "arxiv_id": "2606.13790",
            "role": "root_direct_citation_page_1",
            "screenshot": "screenshots/2606.13790_p30_bibliography.png",
            "physical_pdf_page": "30 (printed p. 29)",
            "checked_element": "SPS References beginning and direct citation [5]",
            "source_url": "https://arxiv.org/abs/2606.13790",
            "visual_result": "PASS",
        },
        {
            "arxiv_id": "2606.13790",
            "role": "root_direct_citation_page_2",
            "screenshot": "screenshots/2606.13790_p31_bibliography.png",
            "physical_pdf_page": "31 (printed p. 30)",
            "checked_element": "direct citations [8], [11], [19], and [20]",
            "source_url": "https://arxiv.org/abs/2606.13790",
            "visual_result": "PASS",
        },
        {
            "arxiv_id": "2606.13790",
            "role": "root_direct_citation_page_3",
            "screenshot": "screenshots/2606.13790_p32_bibliography.png",
            "physical_pdf_page": "32 (printed p. 31)",
            "checked_element": "direct citations [25], [32], [33], [34], and [35]",
            "source_url": "https://arxiv.org/abs/2606.13790",
            "visual_result": "PASS",
        },
        {
            "arxiv_id": "2111.15141",
            "role": "path_space_control_anchor",
            "screenshot": "screenshots/2111.15141_p1_path_integral_sampler.png",
            "physical_pdf_page": "1",
            "checked_element": "title and abstract method scope",
            "source_url": "https://arxiv.org/abs/2111.15141",
            "visual_result": "PASS",
        },
        {
            "arxiv_id": "2309.17082",
            "role": "diffusion_anchor",
            "screenshot": "screenshots/2309.17082_p1_diffusion.png",
            "physical_pdf_page": "1",
            "checked_element": "title and abstract method scope",
            "source_url": "https://arxiv.org/abs/2309.17082",
            "visual_result": "PASS",
        },
        {
            "arxiv_id": "2607.08505",
            "role": "forward_neighbor_anchor",
            "screenshot": "screenshots/2607.08505_p1_closure.png",
            "physical_pdf_page": "1",
            "checked_element": "title and abstract scope as a post-root neighbor",
            "source_url": "https://arxiv.org/abs/2607.08505",
            "visual_result": "PASS",
        },
    ]
    missing = [entry["screenshot"] for entry in entries if not (run_dir / entry["screenshot"]).is_file()]
    if missing:
        raise SystemExit("Missing screenshot(s): " + ", ".join(missing))

    write_csv(
        run_dir / "visual_source_audit.csv",
        entries,
        ["arxiv_id", "role", "screenshot", "physical_pdf_page", "checked_element", "source_url", "visual_result"],
    )

    by_paper: dict[str, list[str]] = {}
    for entry in entries:
        by_paper.setdefault(entry["arxiv_id"], []).append(entry["screenshot"])
    source_rows = read_csv(run_dir / "source_link_verification.csv")
    for row in source_rows:
        screenshots = by_paper.get(row["arxiv_id"], [])
        if screenshots:
            row["visual_evidence"] = "; ".join(screenshots)
            row["status"] = "VERIFIED_C3_WITH_KEY_VISUAL"
        else:
            row["visual_evidence"] = "not_selected_by_key_only_policy"
    write_csv(run_dir / "source_link_verification.csv", source_rows, list(source_rows[0]))

    lines = [
        "# Key-Only Visual Source Audit",
        "",
        "The C3 gate verifies every selected PDF by checksum, page count, and text extraction.",
        "This file adds seven visual anchors for identity and citation inspection; it is not a claim that every source was screenshot.",
        "",
        "| Source | Role | Page | Visual check | Screenshot |",
        "|---|---|---|---|---|",
    ]
    for entry in entries:
        lines.append(
            f"| [{entry['arxiv_id']}]({entry['source_url']}) | {entry['role']} | {entry['physical_pdf_page']} | "
            f"{entry['checked_element']} | [{Path(entry['screenshot']).name}]({entry['screenshot']}) |"
        )
    lines += [
        "",
        "The direct-citation entries in `relation_ledger.csv` use the exact title and arXiv identifier in these root bibliography pages. ",
        "Their printed page and physical PDF page are explicitly separated.",
    ]
    (run_dir / "visual_source_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"visual_entries={len(entries)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
