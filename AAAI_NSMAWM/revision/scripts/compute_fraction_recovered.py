"""Recompute `fraction recovered` per the definition fixed in revision/QUESTIONS.md (E1).

Expected input CSV schema (one row per seed x model x horizon):
    seed, environment, model, horizon, error
where `model` in {"B1", "B2", "M"} and `error` is the mean squared per-feature
open-loop prediction error over the joint observation at that horizon (Figure 2's
y-axis quantity).

Usage:
    python compute_fraction_recovered.py logs.csv --environment GridCraft

With no argument, runs a synthetic self-test that reproduces (approximately, since
it is a self-consistency check rather than a literal fit) the Table 2 / Figure 2
numbers used in the current illustrative draft, so the statistical procedure can be
verified before being pointed at real per-seed logs.

No experiment logs exist in this repository (see revision/code_map.md); this script
is the reusable computation, not a source of new results.
"""
from __future__ import annotations

import argparse
import csv
import math
import statistics
from collections import defaultdict
from dataclasses import dataclass


DEGENERATE_DENOMINATOR_FRACTION = 0.05  # exclude seed if (B1-B2) < 5% of B1's own AUC error


@dataclass
class SeedResult:
    seed: str
    fraction_recovered: float | None  # None if excluded (degenerate denominator)
    numerator: float  # Err_AUC(B1) - Err_AUC(M), always reported even if excluded
    denominator: float  # Err_AUC(B1) - Err_AUC(B2)


def area_under_curve(points: list[tuple[float, float]]) -> float:
    """Trapezoidal AUC over (horizon, error) points sorted by horizon."""
    points = sorted(points)
    auc = 0.0
    for (h0, e0), (h1, e1) in zip(points, points[1:]):
        auc += 0.5 * (e0 + e1) * (h1 - h0)
    return auc


def load_curves(rows: list[dict]) -> dict[tuple[str, str], list[tuple[float, float]]]:
    """Group rows into (seed, model) -> [(horizon, error), ...]."""
    curves: dict[tuple[str, str], list[tuple[float, float]]] = defaultdict(list)
    for row in rows:
        key = (row["seed"], row["model"])
        curves[key].append((float(row["horizon"]), float(row["error"])))
    return curves


def compute(rows: list[dict]) -> tuple[list[SeedResult], dict]:
    curves = load_curves(rows)
    seeds = sorted({seed for seed, _ in curves})
    results: list[SeedResult] = []
    for seed in seeds:
        auc = {}
        for model in ("B1", "B2", "M"):
            key = (seed, model)
            if key not in curves:
                raise ValueError(f"missing curve for seed={seed} model={model}")
            auc[model] = area_under_curve(curves[key])
        numerator = auc["B1"] - auc["M"]
        denominator = auc["B1"] - auc["B2"]
        excluded = denominator < DEGENERATE_DENOMINATOR_FRACTION * auc["B1"]
        fr = None if excluded else numerator / denominator
        results.append(SeedResult(seed=seed, fraction_recovered=fr,
                                   numerator=numerator, denominator=denominator))

    kept = [r.fraction_recovered for r in results if r.fraction_recovered is not None]
    summary = {
        "n_seeds": len(results),
        "n_excluded": sum(1 for r in results if r.fraction_recovered is None),
        "mean": statistics.mean(kept) if kept else None,
        "se": (statistics.stdev(kept) / math.sqrt(len(kept))) if len(kept) > 1 else None,
    }
    return results, summary


def _self_test() -> None:
    """Synthetic curves matching this draft's Figure 2 shape (B1/B2/M), replicated
    across 5 synthetic seeds with small jitter, as a self-consistency check of the
    AUC + per-seed-ratio procedure -- NOT a substitute for real logs."""
    import random

    random.seed(0)
    horizons = [0, 20, 40, 60, 80, 100]
    base = {
        "B1": [0.02, 0.14, 0.27, 0.38, 0.46, 0.52],
        "B2": [0.01, 0.05, 0.08, 0.11, 0.12, 0.13],
        "M": [0.01, 0.06, 0.11, 0.16, 0.19, 0.21],
    }
    rows = []
    for seed_idx in range(5):
        for model, values in base.items():
            for h, e in zip(horizons, values):
                jitter = random.uniform(-0.01, 0.01)
                rows.append({"seed": str(seed_idx), "environment": "GridCraft",
                             "model": model, "horizon": h, "error": max(0.0, e + jitter)})

    results, summary = compute(rows)
    print("Self-test (synthetic, jittered curves -- see docstring):")
    for r in results:
        flag = " (EXCLUDED: degenerate denominator)" if r.fraction_recovered is None else ""
        print(f"  seed={r.seed}: fraction_recovered="
              f"{r.fraction_recovered if r.fraction_recovered is not None else 'NA'}{flag}")
    print(f"  mean={summary['mean']:.3f}  se={summary['se']:.3f}  "
          f"(n_seeds={summary['n_seeds']}, n_excluded={summary['n_excluded']})")
    print("  Endpoint-only (H=100) comparison, for reference: "
          f"{(base['B1'][-1]-base['M'][-1])/(base['B1'][-1]-base['B2'][-1]):.3f} "
          "-- expected to differ from the AUC-based mean above; see QUESTIONS.md.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", nargs="?", default=None,
                         help="Path to per-seed log CSV; omit to run the synthetic self-test.")
    parser.add_argument("--environment", default=None,
                         help="Filter rows to this environment before computing.")
    args = parser.parse_args()

    if args.csv_path is None:
        _self_test()
        return

    with open(args.csv_path, newline="") as f:
        rows = list(csv.DictReader(f))
    if args.environment:
        rows = [r for r in rows if r["environment"] == args.environment]

    results, summary = compute(rows)
    for r in results:
        flag = " (EXCLUDED: degenerate denominator)" if r.fraction_recovered is None else ""
        print(f"seed={r.seed}: fraction_recovered="
              f"{r.fraction_recovered if r.fraction_recovered is not None else 'NA'}{flag}")
    print(f"mean={summary['mean']}  se={summary['se']}  "
          f"(n_seeds={summary['n_seeds']}, n_excluded={summary['n_excluded']})")


if __name__ == "__main__":
    main()
