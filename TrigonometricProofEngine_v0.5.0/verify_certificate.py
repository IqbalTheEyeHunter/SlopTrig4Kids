"""Replay a Trigonometric Proof Engine v0.5 GEO certificate from a JSON file."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from engine import parse_expression
from geometry import verify_geometric_certificate


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replay a v0.5 geometric F08 proof certificate."
    )
    parser.add_argument("certificate", type=Path, help="Path to exported GEO certificate JSON")
    args = parser.parse_args()

    try:
        certificate = json.loads(args.certificate.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"REJECTED: cannot read certificate: {exc}")
        return 2

    claim = certificate.get("claim", {}) if isinstance(certificate, dict) else {}
    try:
        lhs = parse_expression(claim["lhs"])
        rhs = parse_expression(claim["rhs"])
    except Exception as exc:
        print(f"REJECTED: invalid claim: {exc}")
        return 2

    valid, reason = verify_geometric_certificate(
        certificate,
        parse_expression,
        lhs,
        rhs,
        certificate.get("original_domain_conditions", []),
    )
    print(("VERIFIED: " if valid else "REJECTED: ") + reason)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
