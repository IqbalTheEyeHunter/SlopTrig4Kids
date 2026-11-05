"""Replay an exported v0.5.1 geometric F08 certificate from JSON."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from engine import (
    parse_expression,
    _domain_conditions,
    _domain_conditions_from_text,
    _normalize_condition_text,
)
from geometry import verify_geometric_certificate


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replay a Trigonometric Proof Engine v0.5.1 GEO/F08 certificate."
    )
    parser.add_argument("certificate", type=Path, help="Path to exported geometric certificate JSON")
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

    # Reconstruct the domain from the original claim text. Never trust the
    # certificate to tell the verifier which domain it is supposed to check.
    domain = sorted(set(
        _normalize_condition_text(condition)
        for condition in (_domain_conditions(lhs, rhs)
                          + _domain_conditions_from_text(claim["lhs"], claim["rhs"]))
    ), key=str.casefold)
    valid, reason = verify_geometric_certificate(
        certificate, parse_expression, lhs, rhs, domain
    )
    print(reason)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
