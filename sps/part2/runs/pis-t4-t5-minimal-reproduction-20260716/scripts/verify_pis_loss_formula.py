#!/usr/bin/env python3
"""Reproduce the PIS objective decomposition from the locked official code."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


EXPECTED_COMMIT = "c1cbc1f3f28f69aa001df44762fb919de5804ebb"
EXPECTED_SOURCE_SHA256 = (
    "28fa5ab4ec8a00d9897ead9c55f66bbe0877f00d202b859181b136c05817af0e"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_commit(repo: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def load_loss_module(path: Path):
    spec = importlib.util.spec_from_file_location("locked_pis_loss", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-commit", default=EXPECTED_COMMIT)
    args = parser.parse_args()

    import torch

    repo = args.repo.resolve()
    source = repo / "src" / "models" / "loss.py"
    commit = git_commit(repo)
    source_hash = sha256(source)
    module = load_loss_module(source)

    dx = torch.tensor([[3.0, 4.0]])
    quad = module.quad_reg(None, dx, None)

    y1 = torch.tensor([[1.0, 2.0, 6.0], [3.0, 4.0, 12.0]])
    y0 = torch.zeros_like(y1)

    def sdeint_fn(state, times):
        del times
        return torch.stack((state, y1))

    def target_nll(state):
        return (state * state).sum(dim=1)

    def prior_nll(state):
        return torch.zeros(state.shape[0])

    _, loss, info = module.loss_pis(
        sdeint_fn,
        torch.tensor([0.0, 1.0]),
        target_nll,
        prior_nll,
        y0,
        1,
    )

    checks = [
        {
            "name": "locked_commit",
            "observed": commit,
            "expected": args.expected_commit,
            "status": "PASS" if commit == args.expected_commit else "FAIL",
        },
        {
            "name": "locked_source_hash",
            "observed": source_hash,
            "expected": EXPECTED_SOURCE_SHA256,
            "status": "PASS" if source_hash == EXPECTED_SOURCE_SHA256 else "FAIL",
        },
        {
            "name": "quadratic_control_cost",
            "observed": float(quad.item()),
            "expected": 12.5,
            "status": "PASS"
            if torch.allclose(quad, torch.tensor([[12.5]]))
            else "FAIL",
        },
        {
            "name": "objective_decomposition",
            "observed": float(loss.item()),
            "expected": 8.0,
            "status": "PASS"
            if torch.allclose(loss, torch.tensor(8.0))
            else "FAIL",
        },
    ]
    overall = "PASS" if all(row["status"] == "PASS" for row in checks) else "FAIL"
    payload = {
        "schema_version": "part2-minimal-reproduction-v1",
        "overall": overall,
        "repository": "https://github.com/qsh-zh/pis",
        "commit": commit,
        "source_file": "src/models/loss.py",
        "source_sha256": source_hash,
        "python_version": sys.version.split()[0],
        "torch_version": torch.__version__,
        "observed": {
            "quad_reg": float(quad.item()),
            "reg_loss": float(info["reg_loss"].item()),
            "sample_nll": float(info["sample_nll"].item()),
            "prior_nll": float(info["prior_nll"].item()),
            "total_loss": float(loss.item()),
        },
        "checks": checks,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
