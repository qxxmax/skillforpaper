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
PART2 = SPS / "part2" / "sps-lineage-learning-draft-20260715"
PART2_GOAL = SPS / "part2" / "runs" / "sps-goal-mode-rerun-20260716"
PART2_T5 = SPS / "part2" / "runs" / "pis-t4-t5-minimal-reproduction-20260716"
FRESH_PART1 = RUNS / "codex-goal-mode-full-dijkstra-rerun-20260716"


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
    ROOT / "play-the-toy-with-children" / "scripts" / "validate_part2_learning_package.py",
    ROOT / "play-the-toy-with-children" / "references" / "38_native_paper_reading_protocol.md",
    ROOT / "play-the-toy-with-children" / "references" / "39_part2_technical_learning_and_innovation_audit.md",
    ROOT / "play-the-toy-with-children" / "templates" / "paper_reading_record_template.md",
    ROOT / "play-the-toy-with-children" / "templates" / "paper_reading_ledger_template.csv",
    ROOT / "play-the-toy-with-children" / "templates" / "paper_review_gate_template.md",
    SPS / "README.md",
    SPS / "comparison" / "cost_effect_summary.csv",
    SPS / "comparison" / "sol_xhigh_vs_goal_full_rerun_20260716.csv",
    SPS / "comparison" / "sol_xhigh_vs_goal_full_rerun_20260716.md",
    SPS / "comparison" / "dijkstra_effect_and_cost.csv",
    SPS / "scripts" / "build_sol_goal_rerun_comparison.py",
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
    FRESH_PART1 / "README.md",
    FRESH_PART1 / "run_report.md",
    FRESH_PART1 / "final_validation_report.md",
    FRESH_PART1 / "runtime_accounting.md",
    FRESH_PART1 / "numerical_ledger.csv",
    SPS / "part2" / "README.md",
    PART2 / "README.md",
    PART2 / "part2_learning_contract.md",
    PART2 / "part2_learning_report.md",
    PART2 / "innovation_delta.csv",
    PART2 / "equation_code_map.csv",
    PART2 / "review_core.md",
    PART2 / "lineage_learning_path.mmd",
    PART2 / "part2_learning_report.tex",
    PART2 / "part2_learning_report.pdf",
    PART2 / "part2_validation.json",
    PART2_GOAL / "README.md",
    PART2_GOAL / "part2_learning_contract.md",
    PART2_GOAL / "part2_learning_report.md",
    PART2_GOAL / "innovation_delta.csv",
    PART2_GOAL / "equation_code_map.csv",
    PART2_GOAL / "review_core.md",
    PART2_GOAL / "lineage_learning_path.mmd",
    PART2_GOAL / "part2_learning_report.tex",
    PART2_GOAL / "part2_learning_report.pdf",
    PART2_GOAL / "source_identity_ledger.csv",
    PART2_GOAL / "paper_reading_ledger.csv",
    PART2_GOAL / "paper_reading_record_P001.md",
    PART2_GOAL / "paper_reading_record_P002.md",
    PART2_GOAL / "paper_reading_record_P003.md",
    PART2_GOAL / "paper_reading_record_P004.md",
    PART2_GOAL / "paper_reading_record_P007.md",
    PART2_GOAL / "goal_usage_snapshots.csv",
    PART2_GOAL / "goal_usage_summary.md",
    PART2_GOAL / "invocation_manifest.json",
    PART2_GOAL / "run_log.md",
    PART2_GOAL / "output_manifest.md",
    PART2_GOAL / "artifact_refresh_manifest.md",
    PART2_GOAL / "part2_validation.json",
    PART2_T5 / "README.md",
    PART2_T5 / "part2_learning_contract.md",
    PART2_T5 / "part2_learning_report.md",
    PART2_T5 / "innovation_delta.csv",
    PART2_T5 / "equation_code_map.csv",
    PART2_T5 / "review_core.md",
    PART2_T5 / "code_source_ledger.csv",
    PART2_T5 / "cross_case_validation.csv",
    PART2_T5 / "lineage_learning_path.mmd",
    PART2_T5 / "minimal_reproduction_report.md",
    PART2_T5 / "reproduction_manifest.json",
    PART2_T5 / "reproduction_output.json",
    PART2_T5 / "scripts" / "verify_pis_loss_formula.py",
    PART2_T5 / "run_log.md",
    PART2_T5 / "output_manifest.md",
    PART2_T5 / "part2_validation.json",
]
for path in required:
    if not path.exists():
        fail(f"missing required artifact: {path.relative_to(ROOT)}")

tracked_output = subprocess.run(
    ["git", "-C", str(ROOT), "ls-files"],
    check=True,
    capture_output=True,
    text=True,
)
public_files = {
    (ROOT / relative).resolve()
    for relative in tracked_output.stdout.splitlines()
    if (ROOT / relative).is_file()
}
public_files.update(path.resolve() for path in required if path.is_file())

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
for path in public_files:
    if forbidden_parts.intersection(path.relative_to(ROOT).parts):
        fail(f"forbidden path in public export: {path.relative_to(ROOT)}")

forbidden_files = {"fulltext_reading_packets.md", "reading_packets.md", "section_extracts.md"}
for path in public_files:
    if path.name in forbidden_files:
        fail(f"long source-extract artifact found: {path.relative_to(ROOT)}")

json_count = 0
for path in public_files:
    if path.suffix.lower() != ".json":
        continue
    with path.open(encoding="utf-8") as handle:
        json.load(handle)
    json_count += 1

allowed_derived_pdfs = {
    (PART2 / "part2_learning_report.pdf").resolve(),
    (PART2_GOAL / "part2_learning_report.pdf").resolve(),
}
for path in public_files:
    if path.suffix.lower() != ".pdf":
        continue
    if (
        "graphs" not in path.relative_to(ROOT).parts
        and path.resolve() not in allowed_derived_pdfs
    ):
        fail(f"non-graph PDF found: {path.relative_to(ROOT)}")

text_suffixes = {
    ".md", ".json", ".csv", ".py", ".txt", ".yaml", ".yml", ".mmd", ".tex",
}
for path in public_files:
    if path.suffix.lower() not in text_suffixes:
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
    SPS / "comparison" / "sol_xhigh_vs_goal_full_rerun_20260716.md",
    SPS / "comparison" / "dijkstra_effect_and_cost.md",
    RUNS / "codex-goal-mode-full-dijkstra-20260713" / "README.md",
    FRESH_PART1 / "README.md",
    SPS / "part2" / "README.md",
    PART2_GOAL / "README.md",
    PART2_T5 / "README.md",
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
        str(
            ROOT
            / "play-the-toy-with-children"
            / "scripts"
            / "validate_part2_learning_package.py"
        ),
        str(PART2_T5),
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
    [
        sys.executable,
        str(
            ROOT
            / "play-the-toy-with-children"
            / "scripts"
            / "validate_keyword_query_graph.py"
        ),
        "--keyword-ledger",
        str(RUNS / "codex-goal-mode-full-dijkstra-20260713" / "keyword_ledger.csv"),
        "--query-matrix",
        str(RUNS / "codex-goal-mode-full-dijkstra-20260713" / "query_matrix.csv"),
        "--relation-ledger",
        str(RUNS / "codex-goal-mode-full-dijkstra-20260713" / "relation_ledger.csv"),
    ],
    check=True,
)

subprocess.run(
    [
        sys.executable,
        str(
            ROOT
            / "play-the-toy-with-children"
            / "scripts"
            / "validate_part2_learning_package.py"
        ),
        "--self-test",
    ],
    check=True,
)

subprocess.run(
    [
        sys.executable,
        str(
            ROOT
            / "play-the-toy-with-children"
            / "scripts"
            / "validate_part2_learning_package.py"
        ),
        str(PART2),
    ],
    check=True,
)

subprocess.run(
    [
        sys.executable,
        str(
            ROOT
            / "play-the-toy-with-children"
            / "scripts"
            / "validate_part2_learning_package.py"
        ),
        str(PART2_GOAL),
    ],
    check=True,
)

subprocess.run(
    [sys.executable, str(SPS / "scripts" / "validate_dijkstra_public_run.py")],
    check=True,
)

file_count = len(public_files)
print(f"PASS: {file_count} files, {json_count} JSON files, workbook valid, public boundary clean")
