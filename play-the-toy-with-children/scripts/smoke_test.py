#!/usr/bin/env python3
"""Smoke-test the installed skill and report optional capability readiness."""

from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_NAME = "play-the-toy-with-children"
SKILL_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_DIR.parent


def check_required_files() -> list[str]:
    required = [
        SKILL_DIR / "SKILL.md",
        SKILL_DIR / "agents" / "openai.yaml",
        SKILL_DIR / "scripts" / "observable_research_runner.py",
        SKILL_DIR / "scripts" / "render_literature_views.py",
        SKILL_DIR / "scripts" / "validate_keyword_query_graph.py",
        SKILL_DIR / "references" / "33_literature_intent_modes_and_state_loop.md",
        SKILL_DIR / "references" / "35_keyword_ontology_and_query_matrix.md",
        SKILL_DIR / "references" / "36_multiview_literature_graph_contract.md",
        SKILL_DIR / "references" / "37_observable_api_runner.md",
    ]
    errors = [f"missing {path.relative_to(SKILL_DIR)}" for path in required if not path.is_file()]
    if (SKILL_DIR / "SKILL.md").is_file():
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        if not text.startswith("---\n") or f"name: {SKILL_NAME}" not in text:
            errors.append("invalid SKILL.md frontmatter")
    if (SKILL_DIR / "agents" / "openai.yaml").is_file():
        metadata = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        if "$$play-the-toy-with-children" in metadata or "$play-the-toy-with-children" not in metadata:
            errors.append("agents/openai.yaml default prompt does not name the skill")
    return errors


def run_command(command: list[str], label: str) -> list[str]:
    result = subprocess.run(command, text=True, capture_output=True, check=False)
    if result.returncode == 0:
        lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        detail = next((line for line in lines if "PASS" in line), lines[-1] if lines else "PASS")
        print(f"{label}: PASS ({detail})")
        return []
    detail = (result.stderr or result.stdout).strip()
    return [f"{label} failed: {detail}"]


def run_sample_contract() -> list[str]:
    sample = REPO_ROOT / "sps" / "runs" / "codex-goal-mode-cleanroom"
    if not sample.is_dir():
        print("SPS CONTRACT: SKIPPED (sample case is not part of the installed skill)")
        return []
    validator = SKILL_DIR / "scripts" / "validate_keyword_query_graph.py"
    with tempfile.TemporaryDirectory() as temp_dir:
        output = Path(temp_dir) / "validation.json"
        return run_command(
            [
                sys.executable,
                str(validator),
                "--keyword-ledger",
                str(sample / "keyword_ledger_contract.csv"),
                "--query-matrix",
                str(sample / "query_matrix_contract.csv"),
                "--relation-ledger",
                str(sample / "relation_ledger_contract.csv"),
                "--json-output",
                str(output),
            ],
            "SPS CONTRACT",
        )


def optional_status() -> None:
    visuals = all(importlib.util.find_spec(name) is not None for name in ("matplotlib", "networkx"))
    openai_package = importlib.util.find_spec("openai") is not None
    api_key = bool(os.environ.get("OPENAI_API_KEY"))
    print(f"VISUALS: {'READY' if visuals else 'OPTIONAL PACKAGES MISSING'}")
    print(
        "API USAGE: "
        + ("READY" if openai_package and api_key else "OPTIONAL PACKAGE OR OPENAI_API_KEY MISSING")
    )


def main() -> int:
    errors = check_required_files()
    errors.extend(
        run_command(
            [sys.executable, str(SKILL_DIR / "scripts" / "observable_research_runner.py"), "--self-test"],
            "USAGE PARSER",
        )
    )
    errors.extend(run_sample_contract())
    optional_status()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print("CORE: FAIL", file=sys.stderr)
        return 1
    print("CORE: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
