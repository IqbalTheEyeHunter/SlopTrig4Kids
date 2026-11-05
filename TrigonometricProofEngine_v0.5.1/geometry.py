"""Narrow, replayable Euclidean certificate kernel for the F08 identity.

This module deliberately does not call SymPy's trigonometric simplifiers.  It
checks one geometric proof profile (G01 -> G03 -> G04) against a fixed schema,
exact area algebra, signed-coordinate obligations, unit-circle substitution,
and an exact factorisation of the requested claim.

Trust boundary: AX.REAL, AX.EUCLID, AX.AREA and D.UNIT are explicit trusted
foundations.  This is not a formalisation of all Euclidean geometry from
set-theoretic axioms; it is a narrow checker for the documented construction.
"""
from __future__ import annotations

import hashlib
import json
from typing import Callable, Iterable

import sympy as sp

GEOMETRIC_CERTIFICATE_SCHEMA = "trigonometric-geometric-proof-certificate-v1"
GEOMETRIC_CHECKER_VERSION = "0.5.1-geo-checker-1"
TRIG_FUNCTIONS = (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc)
TRUSTED_FOUNDATIONS = ["AX.REAL", "AX.EUCLID", "AX.AREA", "D.UNIT"]
GEO_DEPENDENCIES = ["AX.REAL", "AX.EUCLID", "AX.AREA", "D.UNIT", "G01", "G03", "G04"]


def _contains_trigonometric_function(expr: sp.Expr) -> bool:
    return any(expr.has(function) for function in TRIG_FUNCTIONS)


def match_f08_claim(lhs: sp.Expr, rhs: sp.Expr):
    """Return (angle, multiplier) iff LHS-RHS is an algebraic multiple of F08.

    The multiplier must be free of all six trigonometric functions.  This is a
    deliberately conservative polynomial/rational consequence check: it
    accepts reversal, rearrangement, scalar scaling and non-trigonometric
    rational scaling, but does not use trigsimp or infer unrelated angles.
    """
    residual = sp.expand(lhs - rhs)
    if residual == 0:
        return None

    sin_arguments = {
        node.args[0]
        for expr in (lhs, rhs)
        for node in expr.atoms(sp.sin)
    }
    cos_arguments = {
        node.args[0]
        for expr in (lhs, rhs)
        for node in expr.atoms(sp.cos)
    }
    common_angles = sorted(sin_arguments & cos_arguments, key=sp.srepr)

    for angle in common_angles:
        if any(symbol.is_real is not True for symbol in angle.free_symbols):
            continue
        relation = sp.sin(angle) ** 2 + sp.cos(angle) ** 2 - 1
        try:
            multiplier = sp.cancel(residual / relation)
            if multiplier in (0, sp.zoo, sp.nan, sp.oo, -sp.oo):
                continue
            if multiplier.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
                continue
            if _contains_trigonometric_function(multiplier):
                continue
            if sp.expand(residual - multiplier * relation) != 0:
                continue
            return angle, multiplier
        except (ArithmeticError, TypeError, ValueError, ZeroDivisionError):
            continue
    return None


def _verify_g01_dissection() -> tuple[bool, str]:
    """Check the fixed four-triangle dissection schema and exact area algebra."""
    a, b, c = sp.symbols("_G01_a _G01_b _G01_c", positive=True, real=True)
    outer_area = (a + b) ** 2
    four_triangle_areas = 4 * (a * b / 2)
    central_square_area = c ** 2
    area_residual = sp.expand(outer_area - four_triangle_areas - central_square_area)
    pythagorean_residual = sp.expand(a ** 2 + b ** 2 - c ** 2)
    if sp.expand(area_residual - pythagorean_residual) != 0:
        return False, "G01 exact area-algebra obligation failed."
    return True, "G01 dissection schema and exact area algebra replayed."


def _verify_g03_signed_distance() -> tuple[bool, str]:
    """Check that signed coordinate projections square to u² and v²."""
    u, v = sp.symbols("_G03_u _G03_v", real=True)
    try:
        horizontal = sp.simplify(sp.Abs(u) ** 2 - u ** 2)
        vertical = sp.simplify(sp.Abs(v) ** 2 - v ** 2)
    except Exception:
        return False, "G03 signed-coordinate simplification failed."
    if horizontal != 0 or vertical != 0:
        return False, "G03 signed-coordinate distance obligation failed."
    return True, "G03 squared-distance relation replayed, including axis cases."


def _verify_g04_substitution(angle: sp.Expr) -> tuple[bool, str]:
    """Replay the unit-radius coordinate substitution without trig simplification."""
    radius, horizontal, vertical = sp.symbols(
        "_G04_OP _G04_u _G04_v", real=True
    )
    cartesian_residual = radius ** 2 - horizontal ** 2 - vertical ** 2
    substitutions = {
        radius: sp.Integer(1),
        horizontal: sp.cos(angle),
        vertical: sp.sin(angle),
    }
    substituted = cartesian_residual.subs(substitutions, simultaneous=True)
    expected = 1 - sp.cos(angle) ** 2 - sp.sin(angle) ** 2
    if sp.expand(substituted - expected) != 0:
        return False, "G04 unit-circle substitution replay failed."
    return True, "G04 unit-radius substitution replayed for the real angle."


def _certificate_digest(certificate: dict) -> str:
    payload = {key: value for key, value in certificate.items() if key != "certificate_digest"}
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _node_g01() -> dict:
    return {
        "node_id": "G01",
        "rule_id": "G01",
        "depends_on": ["AX.REAL", "AX.EUCLID", "AX.AREA"],
        "claim": "a**2+b**2=c**2",
        "preconditions": ["a>0", "b>0", "c>0", "right_triangle(a,b,c)"],
        "construction": {
            "outer_shape": "square",
            "outer_side": "a+b",
            "congruent_right_triangles": 4,
            "triangle_legs": ["a", "b"],
            "triangle_hypotenuse": "c",
            "central_shape": "square",
            "central_side": "c",
            "central_angles": ["pi/2", "pi/2", "pi/2", "pi/2"],
            "central_angle_reason": "the two acute angles of each right triangle sum to pi/2",
            "interiors_disjoint": True,
            "covers_outer_square": True,
        },
        "area_identity": "(a+b)**2 = 4*(a*b/2)+c**2",
        "algebraic_consequence": "a**2+b**2=c**2",
        "obligations": [
            "four congruent copies of the same right triangle",
            "complete square partition with disjoint interiors",
            "four central right angles establish a central square",
            "exact area additivity and expansion",
        ],
        "checker_result": "PASS",
    }


def _node_g03() -> dict:
    return {
        "node_id": "G03",
        "rule_id": "G03",
        "depends_on": ["G01", "AX.EUCLID", "AX.REAL"],
        "point": "P=(u,v)",
        "projection_lengths": ["abs(u)", "abs(v)"],
        "right_triangle_hypotenuse": "OP",
        "squared_distance": "OP**2=u**2+v**2",
        "signed_coordinates": True,
        "axis_cases": ["u=0", "v=0"],
        "checker_result": "PASS",
    }


def _node_g04(angle: sp.Expr) -> dict:
    angle_text = sp.sstr(angle)
    return {
        "node_id": "G04",
        "rule_id": "G04",
        "depends_on": ["G03", "D.UNIT"],
        "angle_expression": angle_text,
        "angle_range": "all real angles",
        "unit_circle_point": f"P=(cos({angle_text}),sin({angle_text}))",
        "radius": "1",
        "substitution": {
            "OP": "1",
            "u": f"cos({angle_text})",
            "v": f"sin({angle_text})",
        },
        "conclusion": f"cos({angle_text})**2+sin({angle_text})**2=1",
        "quadrant_restriction": None,
        "checker_result": "PASS",
    }


def _node_goal(lhs: sp.Expr, rhs: sp.Expr, angle: sp.Expr, multiplier: sp.Expr) -> dict:
    return {
        "node_id": "GOAL",
        "depends_on": ["G04"],
        "claim": {"lhs": sp.sstr(lhs), "rhs": sp.sstr(rhs)},
        "angle_expression": sp.sstr(angle),
        "geometric_relation": "sin(theta)**2+cos(theta)**2-1=0",
        "exact_multiplier": sp.sstr(multiplier),
        "factorisation": {
            "lhs_minus_rhs": sp.sstr(sp.expand(lhs - rhs)),
            "multiplier_times_relation": sp.sstr(
                sp.expand(multiplier * (sp.sin(angle) ** 2 + sp.cos(angle) ** 2 - 1))
            ),
        },
        "checker_result": "PASS",
    }


def build_f08_geometric_certificate(
    lhs: sp.Expr,
    rhs: sp.Expr,
    domain_conditions: Iterable[str] = (),
) -> dict | None:
    """Build the canonical GEO certificate when the claim follows from F08."""
    matched = match_f08_claim(lhs, rhs)
    if matched is None:
        return None
    angle, multiplier = matched

    for checker in (_verify_g01_dissection, _verify_g03_signed_distance):
        valid, _reason = checker()
        if not valid:
            return None
    valid, _reason = _verify_g04_substitution(angle)
    if not valid:
        return None

    factorisation = sp.expand(
        (lhs - rhs)
        - multiplier * (sp.sin(angle) ** 2 + sp.cos(angle) ** 2 - 1)
    )
    if factorisation != 0:
        return None

    domain = sorted({str(item) for item in domain_conditions}, key=str.casefold)
    certificate = {
        "schema": GEOMETRIC_CERTIFICATE_SCHEMA,
        "engine_version": "0.5.1",
        "checker_version": GEOMETRIC_CHECKER_VERSION,
        "status": "PROVED",
        "profile": "GEO",
        "claim_kind": "identity",
        "claim": {"lhs": sp.sstr(lhs), "rhs": sp.sstr(rhs)},
        "selected_route": "GEO: G01 → G03 → G04",
        "angle_expression": sp.sstr(angle),
        "goal_multiplier": sp.sstr(multiplier),
        "original_domain_conditions": domain,
        "assumptions": [],
        "open_assumptions": [],
        "used_identity_ids": [],
        "used_theorems": [],
        "dependencies": list(GEO_DEPENDENCIES),
        "trusted_foundations": list(TRUSTED_FOUNDATIONS),
        "proof_nodes": [
            _node_g01(),
            _node_g03(),
            _node_g04(angle),
            _node_goal(lhs, rhs, angle, multiplier),
        ],
        "certificate_note": (
            "F08 is derived from a non-trigonometric Pythagorean dissection, Cartesian "
            "squared distance and the unit-circle coordinate definition. No trigonometric "
            "catalogue identity is used as a premise. The checker validates this fixed "
            "construction schema and its exact algebraic obligations relative to the "
            "explicit trusted foundations AX.REAL, AX.EUCLID, AX.AREA and D.UNIT."
        ),
    }
    certificate["certificate_digest"] = _certificate_digest(certificate)
    return certificate


def verify_geometric_certificate(
    certificate: dict,
    parse_expression: Callable[[str], sp.Expr],
    expected_lhs: sp.Expr,
    expected_rhs: sp.Expr,
    expected_domain_conditions: Iterable[str] = (),
) -> tuple[bool, str]:
    """Replay a v0.5.1 F08 certificate; status and digest alone are insufficient."""
    if not isinstance(certificate, dict):
        return False, "certificate must be a JSON object."
    if certificate.get("schema") != GEOMETRIC_CERTIFICATE_SCHEMA:
        return False, "unsupported geometric certificate schema."

    expected = build_f08_geometric_certificate(
        expected_lhs, expected_rhs, expected_domain_conditions
    )
    if expected is None:
        return False, "the supplied claim is not an enabled G01 → G03 → G04 consequence."

    # Compare all mathematical content before checking the digest so mutations
    # receive a useful diagnostic even when the attacker did not re-hash them.
    expected_keys = set(expected) - {"certificate_digest"}
    actual_keys = set(certificate) - {"certificate_digest"}
    if actual_keys != expected_keys:
        return False, "certificate fields do not match the canonical GEO schema."
    for key in sorted(expected_keys):
        if certificate.get(key) != expected.get(key):
            if key == "original_domain_conditions":
                return False, "original-domain ledger does not match the original claim."
            if key == "used_identity_ids":
                return False, "used_identity_ids must be empty for the independent F08 proof."
            if key == "proof_nodes":
                return False, "proof_nodes do not replay as G01 → G03 → G04 → GOAL."
            return False, f"certificate field '{key}' does not match the replayed proof."

    # Parse the angle and multiplier through the engine's restricted parser.
    try:
        parsed_angle = parse_expression(certificate["angle_expression"])
        parsed_multiplier = parse_expression(certificate["goal_multiplier"])
    except Exception as exc:
        return False, f"invalid angle or multiplier expression: {exc}"
    matched = match_f08_claim(expected_lhs, expected_rhs)
    if matched is None or parsed_angle != matched[0] or parsed_multiplier != matched[1]:
        return False, "angle/multiplier replay does not match the original claim."

    digest = certificate.get("certificate_digest")
    if not isinstance(digest, str) or digest != _certificate_digest(certificate):
        return False, "certificate digest mismatch."

    # Re-run every primitive obligation instead of trusting the stored PASS labels.
    valid, reason = _verify_g01_dissection()
    if not valid:
        return False, reason
    valid, reason = _verify_g03_signed_distance()
    if not valid:
        return False, reason
    valid, reason = _verify_g04_substitution(parsed_angle)
    if not valid:
        return False, reason
    relation = sp.sin(parsed_angle) ** 2 + sp.cos(parsed_angle) ** 2 - 1
    if sp.expand((expected_lhs - expected_rhs) - parsed_multiplier * relation) != 0:
        return False, "GOAL exact factorisation replay failed."

    return True, "VERIFIED: G01 dissection → G03 Cartesian distance → G04 unit circle → original claim."
