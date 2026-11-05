"""Small, explicit geometric certificate kernel for Trigonometric Proof Engine v0.5.

The executable GEO profile currently supports the independent F08 route
G01 -> G03 -> G04.  It treats trigonometric functions as formal atoms while
matching the requested goal; no trigonometric simplifier is used to establish
F08.  The certificate is replayed against a fixed set of typed proof schemas.

Trust boundary:
- AX.REAL: ordered real arithmetic and exact polynomial algebra.
- AX.EUCLID: Euclidean construction, congruence, perpendicularity and angle facts.
- AX.AREA: area additivity and the elementary square/triangle area formulas.
- D.UNIT: sine/cosine are defined as signed coordinates of a unit-circle point.

The G01 checker verifies the exact area-algebra consequence of the dissection
schema.  The Euclidean construction/partition facts themselves belong to the
explicit AX.EUCLID / AX.AREA trusted base; this is not a full formalization of
Euclid's Elements from set-theoretic foundations.
"""
from __future__ import annotations

import hashlib
import json
from typing import Callable

import sympy as sp

GEOMETRIC_CERTIFICATE_SCHEMA = "trigonometric-geometric-proof-certificate-v1"
GEOMETRIC_ENGINE_PROFILE = "GEO"

_TRIG_FUNCTIONS = (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc)
_TRUSTED_FOUNDATIONS = {
    "AX.REAL": "Ordered real field, absolute-value laws and exact polynomial arithmetic.",
    "AX.EUCLID": "Euclidean congruence, angle-sum, perpendicular-projection and dissection-construction facts.",
    "AX.AREA": "Area additivity, square area s^2, and right-triangle area ab/2.",
    "D.UNIT": "For every real oriented angle θ, the unit-circle point has signed coordinates (cos θ, sin θ) and radius 1.",
}


def _contains_trig(expr: sp.Expr) -> bool:
    return any(getattr(node, "func", None) in _TRIG_FUNCTIONS
               for node in sp.preorder_traversal(expr))


def identify_f08_relation(lhs: sp.Expr, rhs: sp.Expr):
    """Return (angle, coefficient) iff lhs-rhs is k*(sin(angle)^2+cos(angle)^2-1).

    This is a formal polynomial match.  Sine/cosine are replaced by independent
    indeterminates; no trigonometric identity or SymPy trigsimp call is used.
    Only one common, trig-free angle argument is currently supported.
    """
    difference = sp.expand(lhs - rhs)
    sin_atoms = difference.atoms(sp.sin)
    cos_atoms = difference.atoms(sp.cos)
    all_trig_atoms = set().union(*(difference.atoms(f) for f in _TRIG_FUNCTIONS))
    if not sin_atoms or not cos_atoms:
        return None
    if len(sin_atoms) != 1 or len(cos_atoms) != 1:
        return None
    sin_node = next(iter(sin_atoms))
    cos_node = next(iter(cos_atoms))
    if sin_node.args[0] != cos_node.args[0]:
        return None
    if all_trig_atoms != {sin_node, cos_node}:
        return None
    angle = sin_node.args[0]
    if _contains_trig(angle):
        return None

    s, c = sp.symbols("_formal_s _formal_c")
    formal = sp.expand(difference.xreplace({sin_node: s, cos_node: c}))
    try:
        polynomial = sp.Poly(formal, s, c, domain="EX")
    except (sp.PolynomialError, TypeError, ValueError):
        return None

    coefficient = sp.cancel(polynomial.coeff_monomial(s**2))
    if coefficient == 0 or coefficient.has(s, c) or _contains_trig(coefficient):
        return None
    expected = {
        (2, 0): coefficient,
        (0, 2): coefficient,
        (0, 0): -coefficient,
    }
    for powers, value in polynomial.terms():
        if powers not in expected:
            return None
        if sp.cancel(value - expected[powers]) != 0:
            return None
    # A missing term has coefficient zero; all three expected coefficients
    # must be present algebraically, with the exact signs shown above.
    if sp.cancel(polynomial.coeff_monomial(c**2) - coefficient) != 0:
        return None
    if sp.cancel(polynomial.coeff_monomial(1) + coefficient) != 0:
        return None
    return angle, coefficient


def _proof_nodes(angle_text: str, coefficient_text: str) -> list[dict]:
    return [
        {
            "node_id": "G01",
            "rule_id": "G01_PYTHAGOREAN_DISSECTION",
            "depends_on": ["AX.REAL", "AX.EUCLID", "AX.AREA"],
            "preconditions": ["a>0", "b>0", "c>0", "right_triangle(a,b,c)"],
            "construction": {
                "outer_shape": "square",
                "outer_side": "a+b",
                "right_triangle_count": 4,
                "triangles_congruent": True,
                "triangle_legs": ["a", "b"],
                "triangle_hypotenuse": "c",
                "central_shape": "square",
                "central_side": "c",
                "central_angles": ["pi/2", "pi/2", "pi/2", "pi/2"],
                "central_angle_reason": "the two acute angles of each right triangle sum to pi/2",
                "interiors_disjoint": True,
                "covers_outer_square": True,
            },
            "area_equation": "(a+b)**2 = 4*(a*b/2) + c**2",
            "algebraic_conclusion": "a**2+b**2=c**2",
            "checker_obligation": "Verify the exact area expansion and the fixed Euclidean dissection schema.",
        },
        {
            "node_id": "G03",
            "rule_id": "G03_CARTESIAN_SQUARED_DISTANCE",
            "depends_on": ["G01", "AX.EUCLID", "AX.REAL"],
            "point": "P=(u,v)",
            "projection_legs": ["Abs(u)", "Abs(v)"],
            "projections_perpendicular": True,
            "signed_coordinates_preserved": True,
            "axis_cases_included": True,
            "absolute_value_square_laws": True,
            "conclusion": "OP**2=u**2+v**2",
        },
        {
            "node_id": "G04",
            "rule_id": "G04_UNIT_CIRCLE_F08",
            "depends_on": ["G03", "D.UNIT"],
            "angle": angle_text,
            "point_coordinates": {
                "horizontal": f"cos({angle_text})",
                "vertical": f"sin({angle_text})",
            },
            "radius": "1",
            "angle_range": "all real angles",
            "substitution": {
                "OP": "1",
                "u": f"cos({angle_text})",
                "v": f"sin({angle_text})",
            },
            "conclusion": f"cos({angle_text})**2+sin({angle_text})**2=1",
        },
        {
            "node_id": "GOAL",
            "rule_id": "EXACT_FORMAL_POLYNOMIAL_CONSEQUENCE",
            "depends_on": ["G04"],
            "coefficient": coefficient_text,
            "formal_residual": f"{coefficient_text}*(_formal_s**2+_formal_c**2-1)",
            "conclusion": "The requested equality follows by exact algebraic substitution.",
        },
    ]


def _certificate_digest(certificate: dict) -> str:
    payload = {key: value for key, value in certificate.items() if key != "certificate_digest"}
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_f08_certificate(
    lhs: sp.Expr,
    rhs: sp.Expr,
    lhs_text: str,
    rhs_text: str,
    domain_conditions: list[str] | tuple[str, ...] = (),
) -> dict | None:
    relation = identify_f08_relation(lhs, rhs)
    if relation is None:
        return None
    angle, coefficient = relation
    certificate = {
        "schema": GEOMETRIC_CERTIFICATE_SCHEMA,
        "engine_version": "0.5.0",
        "profile": GEOMETRIC_ENGINE_PROFILE,
        "claim_kind": "identity",
        "theorem_id": "F08",
        "claim": {"lhs": lhs_text, "rhs": rhs_text},
        "angle": sp.sstr(angle),
        "formal_coefficient": sp.sstr(coefficient),
        "original_domain_conditions": sorted(set(domain_conditions), key=str.casefold),
        "assumptions": [],
        "open_assumptions": [],
        "used_identity_ids": [],
        "dependencies": ["AX.REAL", "AX.EUCLID", "AX.AREA", "D.UNIT"],
        "trusted_foundations": dict(_TRUSTED_FOUNDATIONS),
        "proof_nodes": _proof_nodes(sp.sstr(angle), sp.sstr(coefficient)),
        "conclusion": "PROVED",
        "certificate_note": (
            "Replayed GEO certificate G01 -> G03 -> G04. The proof uses a non-trigonometric "
            "Euclidean dissection and signed unit-circle coordinates; it does not assume F08, F09 or F10. "
            "The Euclidean construction and area axioms are explicit trusted foundations."
        ),
    }
    certificate["certificate_digest"] = _certificate_digest(certificate)
    return certificate


def verify_geometric_certificate(
    certificate: dict,
    parse_expression: Callable[[str], sp.Expr],
    expected_lhs: sp.Expr | None = None,
    expected_rhs: sp.Expr | None = None,
    expected_domain_conditions: list[str] | tuple[str, ...] | None = None,
) -> tuple[bool, str]:
    """Replay a GEO F08 certificate against fixed proof schemas and exact algebra."""
    if not isinstance(certificate, dict):
        return False, "Certificate is not an object."
    if certificate.get("schema") != GEOMETRIC_CERTIFICATE_SCHEMA:
        return False, "Unsupported geometric certificate schema."
    claim = certificate.get("claim")
    if not isinstance(claim, dict) or not isinstance(claim.get("lhs"), str) or not isinstance(claim.get("rhs"), str):
        return False, "Certificate claim is incomplete."
    try:
        lhs = parse_expression(claim["lhs"])
        rhs = parse_expression(claim["rhs"])
    except Exception as exc:
        return False, f"Certificate claim cannot be parsed: {exc}"

    if expected_lhs is not None and expected_rhs is not None:
        same_order = (sp.srepr(lhs) == sp.srepr(expected_lhs) and sp.srepr(rhs) == sp.srepr(expected_rhs))
        reverse_order = (sp.srepr(lhs) == sp.srepr(expected_rhs) and sp.srepr(rhs) == sp.srepr(expected_lhs))
        if not (same_order or reverse_order):
            return False, "Certificate claim does not match the theorem record."

    relation = identify_f08_relation(lhs, rhs)
    if relation is None:
        return False, "Claim is not an exact formal instance of the F08 relation."
    angle, coefficient = relation
    angle_text, coefficient_text = sp.sstr(angle), sp.sstr(coefficient)
    expected = build_f08_certificate(
        lhs, rhs, claim["lhs"], claim["rhs"],
        certificate.get("original_domain_conditions", []),
    )
    if expected is None:
        return False, "Could not reconstruct the expected geometric proof."

    # These are proof-relevant fields.  Human-readable notes and status labels
    # are not treated as proof authority.
    if set(certificate) != set(expected):
        return False, "Certificate contains missing or unexpected fields."

    required_fields = (
        "engine_version", "profile", "claim_kind", "theorem_id", "angle",
        "formal_coefficient", "original_domain_conditions", "assumptions",
        "open_assumptions", "used_identity_ids", "dependencies",
        "trusted_foundations", "proof_nodes", "conclusion", "certificate_note",
    )
    for field in required_fields:
        if certificate.get(field) != expected.get(field):
            return False, f"Certificate field '{field}' does not match the replayed proof schema."

    if certificate.get("profile") != GEOMETRIC_ENGINE_PROFILE or certificate.get("theorem_id") != "F08":
        return False, "Certificate uses the wrong foundation profile or theorem ID."
    if certificate.get("claim_kind") != "identity":
        return False, "Only identity certificates are accepted by this checker."
    if certificate.get("engine_version") != "0.5.0" or certificate.get("conclusion") != "PROVED":
        return False, "Certificate version or conclusion field is invalid."
    if certificate.get("assumptions") != [] or certificate.get("open_assumptions") != []:
        return False, "The F08 geometric proof must not have unresolved assumptions."
    if certificate.get("used_identity_ids") != []:
        return False, "The F08 geometric proof cannot use catalogue identities as premises."
    if any(item in {"F08", "F09", "F10", "F11", "F12"} for item in certificate.get("dependencies", [])):
        return False, "Circular trigonometric dependency detected."

    # Independently check the algebraic core of G01's dissection.  The area
    # additivity equation reduces exactly to a^2+b^2=c^2.
    a, b, c = sp.symbols("a b c", real=True)
    area_residual = sp.expand((a + b)**2 - 4 * (a * b / 2) - c**2)
    pythagorean_residual = sp.expand(a**2 + b**2 - c**2)
    if sp.expand(area_residual - pythagorean_residual) != 0:
        return False, "G01 area-algebra replay failed."

    # G03 uses signed Cartesian coordinates; the square of an absolute value
    # is the square of the signed coordinate, including zero-axis cases.
    u, v = sp.symbols("u v", real=True)
    if sp.simplify(sp.Abs(u)**2 - u**2) != 0 or sp.simplify(sp.Abs(v)**2 - v**2) != 0:
        return False, "G03 signed-coordinate distance replay failed."

    # G04 substitutes the unit-circle coordinate definitions into the G03
    # distance relation with radius exactly one.  This is checked as formal
    # substitution, not as a trigonometric simplification.
    angle_symbol = sp.Symbol("_angle", real=True)
    radius, horizontal, vertical = sp.symbols("_OP _u _v", real=True)
    distance_residual = radius**2 - horizontal**2 - vertical**2
    substituted = distance_residual.subs({
        radius: sp.Integer(1),
        horizontal: sp.cos(angle_symbol),
        vertical: sp.sin(angle_symbol),
    })
    expected_substitution = 1 - sp.cos(angle_symbol)**2 - sp.sin(angle_symbol)**2
    if sp.expand(substituted - expected_substitution) != 0:
        return False, "G04 unit-radius substitution replay failed."

    if expected_domain_conditions is not None:
        wanted = sorted(set(expected_domain_conditions), key=str.casefold)
        got = sorted(set(certificate.get("original_domain_conditions", [])), key=str.casefold)
        if got != wanted:
            return False, "Certificate original-domain ledger does not match the theorem record."

    digest = certificate.get("certificate_digest")
    if not isinstance(digest, str) or digest != _certificate_digest(certificate):
        return False, "Certificate digest is missing or does not match its contents."
    return True, (
        f"Verified GEO certificate for F08 at angle {angle_text}; formal coefficient {coefficient_text}. "
        "G01, G03 and G04 replayed with no trigonometric identity premises."
    )
