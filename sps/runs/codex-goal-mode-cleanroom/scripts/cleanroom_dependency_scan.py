#!/usr/bin/env python3
"""Fail if a scientific artifact depends on an earlier SPS run or fixed generator."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT.parent
TEXT_SUFFIXES = {".md", ".csv", ".json", ".py", ".mjs", ".txt", ".tex", ".bib", ".xml", ".mmd", ".ndjson"}
EXCLUDED = {
    Path("cleanroom_contract.md"),
    Path("cleanroom_dependency_scan.md"),
    Path("cleanroom_dependency_scan.csv"),
    Path("scripts/cleanroom_dependency_scan.py"),
}


def old_sps_directories() -> list[Path]:
    return sorted(
        path
        for path in OUTPUTS.iterdir()
        if path.is_dir() and path != ROOT and "sps" in path.name.lower()
    )


def main() -> None:
    old_dirs = old_sps_directories()
    forbidden = [str(path) for path in old_dirs] + [path.name for path in old_dirs]
    forbidden.append("build_research_artifacts.py")
    scanned = 0
    hits: list[dict[str, str]] = []
    for path in sorted(ROOT.rglob("*")):
        if path.is_symlink() or not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(ROOT)
        if relative in EXCLUDED or "qa_workbook" in relative.parts or "node_modules" in relative.parts:
            continue
        scanned += 1
        content = path.read_text(encoding="utf-8", errors="replace")
        for token in forbidden:
            if token and token in content:
                hits.append({"file": str(relative), "forbidden_dependency": token})
    with (ROOT / "cleanroom_dependency_scan.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["file", "forbidden_dependency"])
        writer.writeheader()
        writer.writerows(hits)
    status = "PASS" if not hits else "FAIL"
    lines = [
        "# Clean-Room Dependency Scan",
        "",
        f"- Status: **{status}**",
        f"- Text artifacts/scripts scanned: **{scanned}**",
        f"- Earlier SPS directories checked: **{len(old_dirs)}**",
        f"- Forbidden references found: **{len(hits)}**",
        "",
        "The scan excludes `cleanroom_contract.md` because that file intentionally names the forbidden-input rule. It also excludes this report and scanner source so the declared patterns do not self-match.",
        "",
        "## Earlier directories checked",
        "",
    ]
    lines.extend(f"- `{path.name}`" for path in old_dirs)
    lines.extend(["", "## Result", ""])
    lines.append("No current scientific artifact, seed, script or report references an earlier SPS output directory or the fixed prior generator." if not hits else "Forbidden dependencies are listed in `cleanroom_dependency_scan.csv`.")
    (ROOT / "cleanroom_dependency_scan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"status={status} scanned={scanned} old_dirs={len(old_dirs)} hits={len(hits)}")
    if hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
