#!/usr/bin/env python3
"""Render the bounded Dijkstra navigation replay comparison."""

from __future__ import annotations

import argparse
import csv
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-cache")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    with (run_dir / "dijkstra_selection_comparison.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    budgets = [int(row["budget_papers"]) for row in rows]
    dijkstra = [int(row["dijkstra_C4_anchors"]) for row in rows]
    screen = [int(row["screen_C4_anchors"]) for row in rows]
    total = max(dijkstra + screen)
    fig, ax = plt.subplots(figsize=(9.4, 5.4))
    ax.plot(budgets, dijkstra, marker="o", linewidth=2.5, color="#376A9A", label="Dijkstra navigation")
    ax.plot(budgets, screen, marker="s", linewidth=2.2, color="#C75B4A", label="Screen-only order")
    ax.axhline(total, linestyle="--", linewidth=1.2, color="#5E6570", label=f"All {total} C4 anchors")
    ax.set_xticks(budgets)
    ax.set_ylim(0, total + 1)
    ax.set_xlabel("Paper-reading budget")
    ax.set_ylabel("C4 anchors reached")
    ax.set_title("Navigation replay at equal reading budget", loc="left", weight="bold")
    ax.grid(axis="y", alpha=0.22)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, loc="lower right")
    for x, y in zip(budgets, dijkstra):
        ax.annotate(str(y), (x, y), xytext=(0, 8), textcoords="offset points", ha="center", fontsize=9)
    for x, y in zip(budgets, screen):
        ax.annotate(str(y), (x, y), xytext=(0, -15), textcoords="offset points", ha="center", fontsize=9)
    output = run_dir / "graphs" / "dijkstra_selection_effect"
    fig.savefig(output.with_suffix(".png"), dpi=220, bbox_inches="tight", facecolor="white")
    fig.savefig(output.with_suffix(".pdf"), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"rendered {output.with_suffix('.png')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
