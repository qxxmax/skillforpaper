#!/usr/bin/env python3
"""Install or update the bundled Codex skill without silent overwrites."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


SKILL_NAME = "play-the-toy-with-children"
REPO_ROOT = Path(__file__).resolve().parent
SOURCE = REPO_ROOT / SKILL_NAME


def default_skills_dir() -> Path:
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()
    return codex_home / "skills"


def validate_skill(path: Path) -> list[str]:
    required = [
        path / "SKILL.md",
        path / "agents" / "openai.yaml",
        path / "scripts" / "smoke_test.py",
        path / "scripts" / "run_literature_dijkstra.py",
        path / "scripts" / "validate_paper_reading_record.py",
        path / "scripts" / "validate_keyword_query_graph.py",
        path / "references" / "33_literature_intent_modes_and_state_loop.md",
        path / "references" / "35_keyword_ontology_and_query_matrix.md",
        path / "references" / "36_multiview_literature_graph_contract.md",
        path / "references" / "37_observable_api_runner.md",
        path / "references" / "38_native_paper_reading_protocol.md",
        path / "templates" / "paper_reading_record_template.md",
        path / "templates" / "paper_reading_ledger_template.csv",
        path / "templates" / "paper_review_gate_template.md",
    ]
    errors = [f"missing {item.relative_to(path)}" for item in required if not item.is_file()]
    skill_file = path / "SKILL.md"
    if skill_file.is_file():
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n") or f"name: {SKILL_NAME}" not in text:
            errors.append("SKILL.md frontmatter has the wrong skill name")
    return errors


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        relative = item.relative_to(path).as_posix()
        if "__pycache__" in item.parts or item.suffix == ".pyc" or item.name == ".DS_Store":
            continue
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(item.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def run_check(destination: Path) -> int:
    if not destination.is_dir():
        print(f"NOT INSTALLED: {destination}", file=sys.stderr)
        return 2
    errors = validate_skill(destination)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    smoke = destination / "scripts" / "smoke_test.py"
    result = subprocess.run([sys.executable, str(smoke)], check=False)
    return result.returncode


def install(skills_dir: Path, update: bool, dry_run: bool) -> int:
    source_errors = validate_skill(SOURCE)
    if source_errors:
        for error in source_errors:
            print(f"SOURCE ERROR: {error}", file=sys.stderr)
        return 1

    destination = skills_dir / SKILL_NAME
    if SOURCE.resolve() == destination.resolve():
        print(f"Skill already lives at the installation path: {destination}")
        return 0

    if destination.is_dir() and tree_digest(SOURCE) == tree_digest(destination):
        print(f"Already up to date: {destination}")
        return 0

    if destination.exists() and not update:
        print(f"Installation already exists: {destination}", file=sys.stderr)
        print("Run install.py --update to replace it while keeping a backup.", file=sys.stderr)
        return 2

    print(f"Source:      {SOURCE}")
    print(f"Destination: {destination}")
    if dry_run:
        print("DRY RUN: no files changed")
        return 0

    skills_dir.mkdir(parents=True, exist_ok=True)
    staging = skills_dir / f".{SKILL_NAME}.installing-{os.getpid()}"
    if staging.exists():
        print(f"Temporary installation path already exists: {staging}", file=sys.stderr)
        return 1

    shutil.copytree(
        SOURCE,
        staging,
        symlinks=True,
        ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"),
    )
    staging_errors = validate_skill(staging)
    if staging_errors:
        shutil.rmtree(staging)
        for error in staging_errors:
            print(f"STAGING ERROR: {error}", file=sys.stderr)
        return 1

    backup: Path | None = None
    if destination.exists():
        backup_root = skills_dir.parent / "skill-backups"
        backup_root.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = backup_root / f"{SKILL_NAME}-{stamp}-{os.getpid()}"
        destination.rename(backup)

    try:
        staging.rename(destination)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        if backup and backup.exists() and not destination.exists():
            backup.rename(destination)
        raise

    print(f"Installed: {destination}")
    if backup:
        print(f"Previous version backed up at: {backup}")
    print(f"Check with: {sys.executable} {Path(__file__).name} --check")
    print("Use the skill in a new Codex turn with: Use $play-the-toy-with-children.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=default_skills_dir())
    parser.add_argument("--update", action="store_true", help="Replace an existing install and retain a backup")
    parser.add_argument("--check", action="store_true", help="Run the installed skill smoke test")
    parser.add_argument("--dry-run", action="store_true", help="Show paths without changing files")
    args = parser.parse_args()
    if args.check and (args.update or args.dry_run):
        parser.error("--check cannot be combined with --update or --dry-run")
    return args


def main() -> int:
    args = parse_args()
    skills_dir = args.skills_dir.expanduser().resolve()
    destination = skills_dir / SKILL_NAME
    if args.check:
        return run_check(destination)
    return install(skills_dir, args.update, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
