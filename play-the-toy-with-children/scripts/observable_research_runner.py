#!/usr/bin/env python3
"""Run a source-grounded research loop while recording exact API usage.

This runner complements the Codex skill. It uses the Responses API directly
because Codex subagent usage counters are not exposed to skill code.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_STAGES = [
    ("01_identity", "Confirm the target identity: title, authors, version, date, arXiv/DOI, and primary source URL. Mark ambiguity explicitly."),
    ("02_root_reading", "Read the root source and extract problem, method, central mechanism or formula, reported results, and limitations with section/page anchors when available."),
    ("03_backward", "Expand backward through the root bibliography. Identify foundational method families and verify direct-citation relationships."),
    ("04_forward", "Expand forward through citing papers. Distinguish a bibliography-only mention from body discussion, extension, or benchmark evidence."),
    ("05_authors", "Expand through authors and collaborators. Record shared authorship separately from method ancestry."),
    ("06_keywords", "Extract normalized keywords from source text, including synonyms, acronyms, mechanisms, failure modes, domains, and evaluation terms; then search them."),
    ("07_adjacent", "Search adjacent and adversarial methods, negative results, scaling limits, transfer limits, and alternative explanations."),
    ("08_closure", "Run a closure check: list unresolved facets, perform targeted searches, deduplicate candidates, and state a bounded stopping decision."),
    ("09_synthesis", "Synthesize an auditable report: confirmed facts, claim-source ledger, method and citation lineage, writable sentences, prohibited/weak claims, gaps, and next directions."),
]

SYSTEM_PROMPT = """You are executing the play-the-toy-with-children literature workflow.
The user often supplies only an oral clue. Confirm the object before summarizing.
Use primary sources whenever possible. Every number, date, identity, and performance
claim needs a source URL and an original-text anchor. Never invent missing history.
Keep candidates, verified sources, direct citations, conceptual similarities, and
shared-authorship relations in separate states. Search iteratively and return to
the original text after expansion. Write unresolved matters as pending confirmation.
At each stage, preserve enough structured detail for a later audit."""


@dataclass
class UsageRow:
    stage: str
    response_id: str
    elapsed_seconds: float
    input_tokens: int
    cached_input_tokens: int
    output_tokens: int
    reasoning_tokens: int
    total_tokens: int


def nested_int(data: dict[str, Any], *path: str) -> int:
    current: Any = data
    for key in path:
        if not isinstance(current, dict):
            return 0
        current = current.get(key)
    return int(current or 0)


def usage_from_response(stage: str, response: Any, elapsed: float) -> UsageRow:
    usage = response.usage.model_dump() if response.usage else {}
    return UsageRow(
        stage=stage,
        response_id=response.id,
        elapsed_seconds=round(elapsed, 3),
        input_tokens=int(usage.get("input_tokens", 0)),
        cached_input_tokens=nested_int(usage, "input_tokens_details", "cached_tokens"),
        output_tokens=int(usage.get("output_tokens", 0)),
        reasoning_tokens=nested_int(usage, "output_tokens_details", "reasoning_tokens"),
        total_tokens=int(usage.get("total_tokens", 0)),
    )


def totals(rows: list[UsageRow]) -> dict[str, int | float]:
    keys = ["input_tokens", "cached_input_tokens", "output_tokens", "reasoning_tokens", "total_tokens"]
    result: dict[str, int | float] = {key: sum(getattr(row, key) for row in rows) for key in keys}
    result["api_calls"] = len(rows)
    result["elapsed_seconds"] = round(sum(row.elapsed_seconds for row in rows), 3)
    return result


def load_prices(path: Path | None, model: str) -> dict[str, float] | None:
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    prices = payload.get(model)
    if not isinstance(prices, dict):
        raise ValueError(f"No pricing entry for model {model!r}")
    required = {"input_per_million", "cached_input_per_million", "output_per_million"}
    missing = required - prices.keys()
    if missing:
        raise ValueError(f"Pricing entry missing: {', '.join(sorted(missing))}")
    return {key: float(value) for key, value in prices.items()}


def calculate_cost(summary: dict[str, int | float], prices: dict[str, float] | None) -> dict[str, float] | None:
    if prices is None:
        return None
    cached = int(summary["cached_input_tokens"])
    uncached = max(0, int(summary["input_tokens"]) - cached)
    output = int(summary["output_tokens"])
    parts = {
        "uncached_input_usd": uncached * prices["input_per_million"] / 1_000_000,
        "cached_input_usd": cached * prices["cached_input_per_million"] / 1_000_000,
        "output_usd": output * prices["output_per_million"] / 1_000_000,
    }
    parts["total_usd"] = sum(parts.values())
    return {key: round(value, 8) for key, value in parts.items()}


def write_usage(output: Path, rows: list[UsageRow], metadata: dict[str, Any], cost: dict[str, float] | None) -> None:
    fieldnames = list(asdict(rows[0]).keys()) if rows else list(UsageRow.__annotations__)
    with (output / "token_usage_by_round.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)
    summary = totals(rows)
    payload = {"metadata": metadata, "totals": summary, "cost": cost, "rounds": [asdict(row) for row in rows]}
    (output / "token_usage.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Observable Run Summary", "",
        f"- model: `{metadata['model']}`", f"- reasoning effort: `{metadata['reasoning_effort']}`",
        f"- API calls: {summary['api_calls']}", f"- wall time: {metadata['wall_time_seconds']} s",
        f"- input tokens: {summary['input_tokens']}", f"- cached input tokens: {summary['cached_input_tokens']}",
        f"- output tokens: {summary['output_tokens']}", f"- reasoning tokens: {summary['reasoning_tokens']}",
        f"- total tokens: {summary['total_tokens']}",
    ]
    lines.append(f"- estimated API cost: ${cost['total_usd']:.6f}" if cost else "- API cost: not calculated; no explicit pricing file supplied")
    (output / "run_usage_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def run(args: argparse.Namespace) -> int:
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set. Configure it in the shell, then rerun.", file=sys.stderr)
        return 2
    from openai import OpenAI

    output = Path(args.output).expanduser().resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / "rounds").mkdir()
    client = OpenAI()
    rows: list[UsageRow] = []
    previous_response_id: str | None = None
    start = time.monotonic()
    started_iso = datetime.now(timezone.utc).isoformat()

    for index, (stage, instruction) in enumerate(DEFAULT_STAGES, start=1):
        prompt = f"Research topic or oral clue:\n{args.topic}\n\nCurrent stage ({index}/{len(DEFAULT_STAGES)}): {instruction}"
        kwargs: dict[str, Any] = {
            "model": args.model,
            "instructions": SYSTEM_PROMPT,
            "input": prompt,
            "reasoning": {"effort": args.reasoning_effort},
            "tools": [{"type": "web_search"}],
        }
        if previous_response_id:
            kwargs["previous_response_id"] = previous_response_id
        call_start = time.monotonic()
        response = client.responses.create(**kwargs)
        elapsed = time.monotonic() - call_start
        rows.append(usage_from_response(stage, response, elapsed))
        previous_response_id = response.id
        (output / "rounds" / f"{stage}.md").write_text(response.output_text + "\n", encoding="utf-8")
        (output / "rounds" / f"{stage}.response.json").write_text(response.model_dump_json(indent=2) + "\n", encoding="utf-8")

    metadata = {
        "topic": args.topic, "model": args.model, "reasoning_effort": args.reasoning_effort,
        "started_at_utc": started_iso, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "wall_time_seconds": round(time.monotonic() - start, 3), "usage_source": "Responses API response.usage",
    }
    prices = load_prices(Path(args.pricing) if args.pricing else None, args.model)
    write_usage(output, rows, metadata, calculate_cost(totals(rows), prices))
    (output / "final_report.md").write_text((output / "rounds" / "09_synthesis.md").read_text(encoding="utf-8"), encoding="utf-8")
    print(output)
    return 0


def self_test() -> int:
    class FakeUsage:
        def model_dump(self) -> dict[str, Any]:
            return {"input_tokens": 120, "input_tokens_details": {"cached_tokens": 20}, "output_tokens": 50,
                    "output_tokens_details": {"reasoning_tokens": 15}, "total_tokens": 170}
    class FakeResponse:
        id = "resp_test"
        usage = FakeUsage()
    row = usage_from_response("test", FakeResponse(), 1.25)
    assert row.cached_input_tokens == 20 and row.reasoning_tokens == 15 and row.total_tokens == 170
    assert totals([row, row])["total_tokens"] == 340
    print("PASS: usage parsing and aggregation")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", help="Research topic or oral clue")
    parser.add_argument("--output", help="New output directory")
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--reasoning-effort", default="xhigh", choices=["none", "low", "medium", "high", "xhigh"])
    parser.add_argument("--pricing", help="Optional JSON price table; prices are never hardcoded")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if not args.self_test and (not args.topic or not args.output):
        parser.error("--topic and --output are required unless --self-test is used")
    return args


if __name__ == "__main__":
    arguments = parse_args()
    raise SystemExit(self_test() if arguments.self_test else run(arguments))
