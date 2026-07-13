#!/usr/bin/env python3
"""Validate the small, shareable skill + SPS repository export."""

from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPS = ROOT / "sps"
RUNS = SPS / "runs"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


required = [
    ROOT / "README.md",
    ROOT / "DESIGN_PROVENANCE.md",
    ROOT / "install.py",
    ROOT / "requirements-optional.txt",
    ROOT / "play-the-toy-with-children" / "SKILL.md",
    ROOT / "play-the-toy-with-children" / "agents" / "openai.yaml",
    ROOT / "play-the-toy-with-children" / "scripts" / "smoke_test.py",
    ROOT / "play-the-toy-with-children" / "scripts" / "validate_paper_reading_record.py",
    ROOT / "play-the-toy-with-children" / "references" / "38_native_paper_reading_protocol.md",
    ROOT / "play-the-toy-with-children" / "templates" / "paper_reading_record_template.md",
    ROOT / "play-the-toy-with-children" / "templates" / "paper_reading_ledger_template.csv",
    ROOT / "play-the-toy-with-children" / "templates" / "paper_review_gate_template.md",
    SPS / "README.md",
    SPS / "comparison" / "cost_effect_summary.csv",
    SPS / "comparison" / "dijkstra_effect_and_cost.csv",
    SPS / "scripts" / "validate_dijkstra_public_run.py",
    RUNS / "gpt-5.6-sol-xhigh-matched" / "run_metrics.json",
    RUNS / "codex-goal-mode-matched" / "run_metrics.json",
    RUNS / "codex-goal-mode-cleanroom" / "goal_mode_usage.md",
    RUNS / "codex-goal-mode-cleanroom" / "final_validation_report.md",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "README.md",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "native_paper_reading_record_sps.md",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "native_paper_reading_ledger.csv",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "native_paper_review_gate_sps.md",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "final_validation_report.md",
]
for path in required:
    if not path.exists():
        fail(f"missing required artifact: {path.relative_to(ROOT)}")

allowed_top = {
    ".git",
    ".gitignore",
    "README.md",
    "DESIGN_PROVENANCE.md",
    "install.py",
    "requirements-optional.txt",
    "play-the-toy-with-children",
    "sps",
}
unexpected_top = sorted(path.name for path in ROOT.iterdir() if path.name not in allowed_top)
if unexpected_top:
    fail(f"unexpected top-level entries: {unexpected_top}")

forbidden_parts = {"examples", "research-to-publication", "sources", "source_pdfs", "fulltext_cache"}
for path in ROOT.rglob("*"):
    if forbidden_parts.intersection(path.relative_to(ROOT).parts):
        fail(f"forbidden path in public export: {path.relative_to(ROOT)}")

forbidden_files = {"fulltext_reading_packets.md", "reading_packets.md", "section_extracts.md"}
for path in ROOT.rglob("*"):
    if path.name in forbidden_files:
        fail(f"long source-extract artifact found: {path.relative_to(ROOT)}")

json_count = 0
for path in ROOT.rglob("*.json"):
    with path.open(encoding="utf-8") as handle:
        json.load(handle)
    json_count += 1

for path in ROOT.rglob("*.pdf"):
    if "graphs" not in path.relative_to(ROOT).parts:
        fail(f"non-graph PDF found: {path.relative_to(ROOT)}")

text_suffixes = {".md", ".json", ".csv", ".py", ".txt", ".yaml", ".yml", ".mmd"}
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes:
        continue
    if path.resolve() == Path(__file__).resolve():
        continue
    text = path.read_text(encoding="utf-8", errors="replace")
    if "/Users/mxq" in text or "C:\\Users\\mxq" in text:
        fail(f"absolute user path found in {path.relative_to(ROOT)}")

for document in [
    ROOT / "README.md",
    ROOT / "DESIGN_PROVENANCE.md",
    SPS / "README.md",
    SPS / "comparison" / "cost_effect_summary.md",
    SPS / "comparison" / "dijkstra_effect_and_cost.md",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "README.md",
]:
    text = document.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        resolved = (document.parent / target).resolve()
        if not resolved.exists():
            fail(f"broken relative link in {document.relative_to(ROOT)}: {target}")

with (SPS / "comparison" / "cost_effect_summary.csv").open(newline="", encoding="utf-8") as handle:
    rows = {row["run_id"]: row for row in csv.DictReader(handle)}

gpt_metrics = json.loads((RUNS / "gpt-5.6-sol-xhigh-matched" / "run_metrics.json").read_text())
goal_metrics = json.loads((RUNS / "codex-goal-mode-matched" / "run_metrics.json").read_text())

checks = [
    (rows["gpt56_xhigh_matched"]["elapsed_seconds"], gpt_metrics["timing"]["elapsed_seconds"]),
    (rows["gpt56_xhigh_matched"]["deduplicated_candidates"], gpt_metrics["coverage"]["deduplicated_route_candidates"]),
    (rows["gpt56_xhigh_matched"]["verified_pages"], gpt_metrics["coverage"]["local_pdf_pages"]),
    (rows["codex_goal_matched"]["elapsed_seconds"], goal_metrics["timing"]["elapsed_seconds"]),
    (rows["codex_goal_matched"]["deduplicated_candidates"], goal_metrics["coverage"]["deduplicated_route_candidates"]),
    (rows["codex_goal_matched"]["verified_pages"], goal_metrics["coverage"]["local_pdf_pages"]),
]
for recorded, source_value in checks:
    if int(recorded) != int(source_value):
        fail(f"comparison metric mismatch: recorded={recorded}, source={source_value}")

workbook = RUNS / "codex-goal-mode-cleanroom" / "sps_literature_audit_cleanroom.xlsx"
with zipfile.ZipFile(workbook) as archive:
    bad_member = archive.testzip()
    if bad_member:
        fail(f"invalid workbook member: {bad_member}")

subprocess.run(
    [
        sys.executable,
        str(ROOT / "play-the-toy-with-children" / "scripts" / "validate_paper_reading_record.py"),
        "--self-test",
    ],
    check=True,
)

subprocess.run(
    [
        sys.executable,
        str(ROOT / "play-the-toy-with-children" / "scripts" / "validate_paper_reading_record.py"),
        str(
            RUNS
            / "codex-goal-mode-full-dijkstra-20260713"
            / "native_paper_reading_record_sps.md"
        ),
    ],
    check=True,
)

subprocess.run(
    [sys.executable, str(SPS / "scripts" / "validate_dijkstra_public_run.py")],
    check=True,
)

file_count = sum(
    1
    for path in ROOT.rglob("*")
    if path.is_file() and ".git" not in path.relative_to(ROOT).parts
)
print(f"PASS: {file_count} files, {json_count} JSON files, workbook valid, public boundary clean")
