"""Structural recogniser for Malaysian Form 5 trigonometric problems.

Recognition is deliberately separate from proof and equation solving. A match
suggests a mathematical family and candidate route; it never certifies a claim.
The implementation uses the bundled SKILL-2.md as the recognition catalogue,
SKILL.md as the six-function identity reference, and the v0.5 handbook as the
proof-method and safety reference.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable

import sympy as sp

from engine import (
    ExpressionInputError,
    TRIG_FUNCTIONS,
    _domain_conditions,
    _domain_conditions_from_text,
    parse_expression,
    _SafeSympyParser,
)

ENGINE_VERSION = "0.5.1"
KNOWLEDGE_DIR = Path(__file__).resolve().parent / "knowledge"
DEFAULT_SKILL2_PATH = KNOWLEDGE_DIR / "SKILL-2.md"
DEFAULT_SKILL_PATH = KNOWLEDGE_DIR / "SKILL.md"
DEFAULT_HANDBOOK_PATH = KNOWLEDGE_DIR / "V0.5_Proof_Knowledge_Handbook.md"

TRIG_NAME = {
    sp.sin: "sin", sp.cos: "cos", sp.tan: "tan",
    sp.cot: "cot", sp.sec: "sec", sp.csc: "csc",
}
FUNCTION_CLASS = {
    "sin": "EQREC-001", "cos": "EQREC-002", "tan": "EQREC-003",
    "cot": "EQREC-004", "sec": "EQREC-005", "csc": "EQREC-005",
}

# The ID and method map is the executable routing index. Titles are loaded from
# SKILL-2.md so the human-readable knowledge source remains authoritative.
CLASS_META: dict[str, dict] = {
    "EQREC-001": {"band": "KSSM core", "standard": "6.6.1", "methods": ["EQ02", "EQ03", "EQ04"]},
    "EQREC-002": {"band": "KSSM core", "standard": "6.6.1", "methods": ["EQ02", "EQ03", "EQ04"]},
    "EQREC-003": {"band": "KSSM core", "standard": "6.6.1", "methods": ["EQ02", "EQ03", "EQ11"]},
    "EQREC-004": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ02", "EQ03", "EQ04"]},
    "EQREC-005": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ02", "EQ03"]},
    "EQREC-006": {"band": "KSSM core", "standard": "6.6.1", "methods": ["EQ03", "EQ04"]},
    "EQREC-007": {"band": "KSSM core", "standard": "6.6.1", "methods": ["EQ04", "G28"]},
    "EQREC-008": {"band": "KSSM core", "standard": "6.6.1", "methods": ["EQ04", "G28"]},
    "EQREC-009": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ04", "EQ11"]},
    "EQREC-010": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ04"]},
    "EQREC-011": {"band": "KSSM core", "standard": "6.2.1 / 6.6.1", "methods": ["G10", "S11-S16", "EQ04"]},
    "EQREC-012": {"band": "Supporting method", "standard": "6.6.1", "methods": ["G23", "EQ10", "G24"]},
    "EQREC-013": {"band": "Supporting method", "standard": "6.6.1", "methods": ["G23", "EQ10", "EQ02"]},
    "EQREC-014": {"band": "Supporting method", "standard": "6.5.1 / 6.6.1", "methods": ["G12", "G23", "EQ10"]},
    "EQREC-015": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ12", "M04", "EQ02"]},
    "EQREC-016": {"band": "Supporting method", "standard": "6.4.2 / 6.6.1", "methods": ["G04", "M04", "EQ12"]},
    "EQREC-017": {"band": "KSSM core", "standard": "6.4.2 / 6.6.1", "methods": ["G04", "G21", "EQ09"]},
    "EQREC-018": {"band": "KSSM core", "standard": "6.5.3 / 6.6.1", "methods": ["G21", "D01", "EQ05"]},
    "EQREC-019": {"band": "KSSM core", "standard": "6.4.2 / 6.5.3", "methods": ["G04", "G21", "M10"]},
    "EQREC-020": {"band": "Supporting method", "standard": "6.6.1", "methods": ["M02", "M03", "EQ12"]},
    "EQREC-021": {"band": "Supporting method", "standard": "6.4.2 / 6.6.1", "methods": ["M02", "M03", "M06"]},
    "EQREC-022": {"band": "KSSM core", "standard": "6.5.2 / 6.5.3", "methods": ["G21", "D01-D04", "EQ05"]},
    "EQREC-023": {"band": "KSSM core", "standard": "6.5.1", "methods": ["G12", "A01-A04", "EQ04"]},
    "EQREC-024": {"band": "Extension recognition", "standard": "Beyond explicit core", "methods": ["M08", "M09", "D13-D16"]},
    "EQREC-025": {"band": "KSSM core / supporting", "standard": "6.5.2", "methods": ["G21", "H01-H09", "EQ08"]},
    "EQREC-026": {"band": "KSSM core", "standard": "6.2.2 / 6.5.1", "methods": ["G20", "G09", "G10"]},
    "EQREC-027": {"band": "Supporting method", "standard": "6.6.1", "methods": ["M02", "M03", "M06", "EQ16"]},
    "EQREC-028": {"band": "Supporting method", "standard": "6.4.2 / 6.6.1", "methods": ["G07", "G08", "M02", "M03"]},
    "EQREC-029": {"band": "Supporting method", "standard": "6.4.2 / 6.6.1", "methods": ["M03", "G21", "EQ07"]},
    "EQREC-030": {"band": "KSSM core graph / supporting equation", "standard": "6.3.1 / 6.3.2", "methods": ["G24", "EQ13", "EQ06"]},
    "EQREC-031": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ13", "M19"]},
    "EQREC-032": {"band": "Supporting method", "standard": "6.6.1", "methods": ["M03", "M06", "EQ07"]},
    "EQREC-033": {"band": "Extension recognition", "standard": "Beyond explicit core", "methods": ["G22", "M11", "EQ08"]},
    "EQREC-034": {"band": "KSSM core", "standard": "6.3.1 / 6.3.2", "methods": ["G25", "EQ02", "EQ03"]},
    "EQREC-035": {"band": "KSSM core", "standard": "6.3.1 / 6.3.2", "methods": ["G25", "EQ02", "EQ03"]},
    "EQREC-036": {"band": "KSSM core", "standard": "6.3.1 / 6.3.2", "methods": ["G25", "EQ02", "EQ11"]},
    "EQREC-037": {"band": "KSSM core", "standard": "6.3.1 / 6.3.2", "methods": ["G24", "G25", "EQ13"]},
    "EQREC-038": {"band": "KSSM core", "standard": "6.3.2", "methods": ["G25", "EQ02"]},
    "EQREC-039": {"band": "KSSM core", "standard": "6.3.2", "methods": ["G25", "AN10", "EQ18"]},
    "EQREC-040": {"band": "KSSM core", "standard": "6.3.2", "methods": ["G24", "G25", "EQ10"]},
    "EQREC-041": {"band": "KSSM core", "standard": "6.3.2", "methods": ["G25", "EQ18", "AN10"]},
    "EQREC-042": {"band": "KSSM core", "standard": "6.3.2", "methods": ["G24", "M18", "AN09"]},
    "EQREC-043": {"band": "KSSM core", "standard": "6.1.1 / 6.6.1", "methods": ["G09", "EQ02", "EQ03"]},
    "EQREC-044": {"band": "KSSM core", "standard": "6.1.1 / 6.6.1", "methods": ["G09", "EQ02", "EQ03"]},
    "EQREC-045": {"band": "KSSM core", "standard": "6.1.1 / 6.2.2", "methods": ["G09", "G10", "G20"]},
    "EQREC-046": {"band": "KSSM core / supporting", "standard": "6.6.1 / 6.6.2", "methods": ["EQ10", "EQ17", "G24"]},
    "EQREC-047": {"band": "Supporting method", "standard": "6.6.2", "methods": ["G26", "EQ14"]},
    "EQREC-048": {"band": "Supporting method", "standard": "6.5.1", "methods": ["M07", "G12", "EQ04"]},
    "EQREC-049": {"band": "Supporting method", "standard": "6.6.1", "methods": ["EQ05", "M03", "M19"]},
    "EQREC-050": {"band": "Supporting method", "standard": "6.4.2 / 6.6.1", "methods": ["M02", "M03", "G07", "G08"]},
    "EQREC-051": {"band": "Extension recognition", "standard": "Beyond explicit core", "methods": ["M05", "EQ17", "M04"]},
    "EQREC-052": {"band": "Extension recognition", "standard": "Beyond explicit core", "methods": ["AN10", "EQ18"]},
    "EQREC-053": {"band": "Extension recognition", "standard": "Beyond explicit core", "methods": ["G25", "AN10", "EQ18"]},
    "EQREC-054": {"band": "Supporting method", "standard": "6.4.2 / 6.5.3 / 6.6.1", "methods": ["M01", "M02", "M07", "M08"]},
    "EQREC-055": {"band": "KSSM core", "standard": "6.4.2 / 6.5.3 / 6.6.1", "methods": ["proof dependency graph", "EQ01", "certificate replay"]},
}

# Compact descriptions of why a pattern matched and what to inspect next.
METHOD_NOTES = {
    "EQREC-001": "Use the complete sine solution families, then filter by the requested interval.",
    "EQREC-002": "Use the complete cosine solution families and check endpoint duplication.",
    "EQREC-003": "Use tangent's period π and exclude every pole.",
    "EQREC-004": "Use cotangent's period π and exclude every zero of sine.",
    "EQREC-005": "Convert secant/cosecant to cosine/sine only while retaining reciprocal domains.",
    "EQREC-006": "Solve in the inner angle first, then invert the affine argument with exact interval filtering.",
    "EQREC-007": "Split sine equality into its two periodic branches; prove completeness.",
    "EQREC-008": "Use the two cosine-equality branches and merge overlaps.",
    "EQREC-009": "Equal defined tangents have arguments differing by an integer multiple of π.",
    "EQREC-010": "Equal defined cotangents have arguments differing by an integer multiple of π.",
    "EQREC-011": "Check the cofunction shift and its domain before converting sine to cosine or vice versa.",
    "EQREC-012": "Consider phase-amplitude form and compare the target level with the amplitude.",
    "EQREC-013": "Compare the amplitude of the linear combination with the range of the other trig function.",
    "EQREC-014": "Use a phase shift, but preserve the exact sign and quadrant of the phase.",
    "EQREC-015": "Substitute one trig function as an algebraic variable and enforce its range.",
    "EQREC-016": "Reduce with the circle relation only after it is independently established; keep the angle shared.",
    "EQREC-017": "Factor the difference of squares or use a double-angle equation; retain both sign branches.",
    "EQREC-018": "Use the double-angle product relation and keep every zero-factor case.",
    "EQREC-019": "Use the fundamental norm relation or power reduction with the correct shared angle.",
    "EQREC-020": "Use t=tan(x) or u=cot(x) only on its chart and check excluded poles/zeros separately.",
    "EQREC-021": "Clear denominators only after recording all original nonzero conditions.",
    "EQREC-022": "Apply double-angle formulas directly; avoid dividing by factors that may vanish.",
    "EQREC-023": "Expand or compare compound angles using the addition/subtraction formulas.",
    "EQREC-024": "Use recurrence or multiple-angle polynomials; confirm the integer multiplier.",
    "EQREC-025": "Use half-angle relations with absolute-value/sign handling and omitted-point checks.",
    "EQREC-026": "Reduce to exact special-angle ratios and use quadrant signs.",
    "EQREC-027": "Form a rational expression with a denominator ledger; split zero factors before cancellation.",
    "EQREC-028": "Try conjugate pairs and Pythagorean relations; check every reciprocal domain.",
    "EQREC-029": "Use a conjugate or half-angle relation, then check the excluded angle where the factor is zero.",
    "EQREC-030": "Split absolute-value branches or analyse reflected graph branches; do not drop sign cases.",
    "EQREC-031": "Require nonnegative radicands and nonnegative principal-root sides before squaring.",
    "EQREC-032": "Record the original denominator before cancelling and restore excluded values afterwards.",
    "EQREC-033": "Use the rational half-angle chart and test every omitted odd-π point in the original equation.",
    "EQREC-034": "Read amplitude, period, midline and range; handle a=0 separately.",
    "EQREC-035": "Read amplitude, period, midline and range; account for cosine key-point placement.",
    "EQREC-036": "Find period and vertical asymptotes; tangent has no finite amplitude.",
    "EQREC-037": "Track the placement of each absolute-value bar, cusps, zeros and asymptotes.",
    "EQREC-038": "Count valid intersections with the horizontal line on the stated interval.",
    "EQREC-039": "Treat both sides as graphs; do not assume the right-hand side is constant.",
    "EQREC-040": "Find attained extrema and check open endpoints, holes, poles and tangencies.",
    "EQREC-041": "Count distinct x-values, including tangencies once and excluding undefined points.",
    "EQREC-042": "Partition the interval at intersections and test the sign on each region.",
    "EQREC-043": "Generate every periodic branch before filtering to the full multi-turn interval.",
    "EQREC-044": "Retain negative representatives required by the interval; do not shift the requested answer range.",
    "EQREC-045": "Use quadrant signs and reference angles without losing the original angle representative.",
    "EQREC-046": "Separate parameters from angle variables and split zero-coefficient cases.",
    "EQREC-047": "Use the triangle angle-sum and positivity hypotheses; do not assume the converse without proof.",
    "EQREC-048": "Use sum-to-product or product-to-sum and retain every factor branch.",
    "EQREC-049": "Split each product factor, then deduplicate the union of solution families.",
    "EQREC-050": "Inspect reciprocal/conjugate pairs and preserve their domains.",
    "EQREC-051": "Solve the algebraic system, restore angle branches and check all equations together.",
    "EQREC-052": "Preserve the nested function structure; only use a dedicated supported module.",
    "EQREC-053": "Prefer graph or certified root-isolation methods; numerical roots alone are incomplete.",
    "EQREC-054": "Search for a hidden certified identity before applying a general equation method.",
    "EQREC-055": "Build a dependency graph: prove the earlier claim before using it in the later equation.",
}


def _load_catalogue_titles(path: Path = DEFAULT_SKILL2_PATH) -> dict[str, str]:
    titles: dict[str, str] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"\s*###\s+`(EQREC-\d{3})`\s+—\s+(.+?)\s*$", line)
            if match:
                titles[match.group(1)] = match.group(2).strip()
    return titles


CATALOGUE_TITLES = _load_catalogue_titles()


@dataclass(frozen=True)
class EquationRecord:
    original: str
    lhs_text: str
    relation: str
    rhs_text: str
    lhs: sp.Expr
    rhs: sp.Expr

    @property
    def difference(self) -> sp.Expr:
        return sp.simplify(self.lhs - self.rhs)


@dataclass(frozen=True)
class RecognitionMatch:
    id: str
    title: str
    band: str
    standard: str
    reasons: tuple[str, ...] = ()
    methods: tuple[str, ...] = ()


@dataclass
class RecognitionResult:
    status: str
    task_type: str
    equations: list[EquationRecord]
    angle_variables: tuple[str, ...]
    parameter_variables: tuple[str, ...]
    interval_text: str
    angle_unit: str
    cognitive_level: str
    complexity_notes: tuple[str, ...]
    matches: list[RecognitionMatch] = field(default_factory=list)
    domain_conditions: tuple[str, ...] = ()
    cautions: tuple[str, ...] = ()
    workflow: tuple[str, ...] = ()
    knowledge_sources: tuple[str, ...] = (
        "knowledge/SKILL.md",
        "knowledge/SKILL-2.md",
        "knowledge/V0.5_Proof_Knowledge_Handbook.md",
    )

    @property
    def primary_match(self) -> RecognitionMatch | None:
        return self.matches[0] if self.matches else None

    def to_dict(self) -> dict:
        return {
            "schema": "trigonometric-problem-recognition-v1",
            "engine_version": ENGINE_VERSION,
            "status": self.status,
            "task_type": self.task_type,
            "equations": [
                {"original": e.original, "lhs": sp.sstr(e.lhs), "relation": e.relation,
                 "rhs": sp.sstr(e.rhs)} for e in self.equations
            ],
            "angle_variables": list(self.angle_variables),
            "parameter_variables": list(self.parameter_variables),
            "interval": self.interval_text,
            "angle_unit": self.angle_unit,
            "estimated_cognitive_level": self.cognitive_level,
            "complexity_notes": list(self.complexity_notes),
            "matches": [asdict(m) for m in self.matches],
            "domain_conditions": list(self.domain_conditions),
            "cautions": list(self.cautions),
            "suggested_workflow": list(self.workflow),
            "knowledge_sources": list(self.knowledge_sources),
            "proof_or_solution_status": "NOT_ESTABLISHED_BY_RECOGNITION",
        }

    def to_markdown(self) -> str:
        lines = [
            "TRIGONOMETRIC PROBLEM RECOGNITION REPORT",
            "=" * 88,
            f"Engine version: {ENGINE_VERSION}",
            f"Recognition status: {self.status}",
            f"Task type: {self.task_type}",
            f"Angle unit: {self.angle_unit}",
            f"Estimated cognitive demand: {self.cognitive_level}",
            "",
            "INPUT RELATIONS",
            "-" * 88,
        ]
        for index, equation in enumerate(self.equations, 1):
            lines.append(f"{index}. {equation.lhs_text} {equation.relation} {equation.rhs_text}")
        lines += ["", "VARIABLE ANALYSIS", "-" * 88,
                  f"Angle variables: {', '.join(self.angle_variables) or 'Not determined'}",
                  f"Other / parameter variables: {', '.join(self.parameter_variables) or 'None detected'}",
                  f"Requested interval: {self.interval_text or 'Not supplied / not detected'}"]
        lines += ["", "RECOGNITION CANDIDATES", "-" * 88]
        if not self.matches:
            lines.append("No specific EQREC pattern matched. The input remains an unclassified trigonometric relation.")
        for index, match in enumerate(self.matches, 1):
            lines += [
                f"{index}. {match.id} — {match.title}",
                f"   Curriculum band: {match.band}",
                f"   DSKP link: {match.standard}",
                f"   Why recognised: {'; '.join(match.reasons)}",
                f"   Candidate knowledge routes: {', '.join(match.methods)}",
                f"   Method note: {METHOD_NOTES.get(match.id, 'Inspect the structure and domain before choosing a route.')}",
            ]
        lines += ["", "DOMAIN / BRANCH CONDITIONS", "-" * 88]
        lines.extend(f"- {condition}" for condition in self.domain_conditions) if self.domain_conditions else lines.append("- No explicit denominator or radical restrictions were detected by the current parser.")
        lines += ["", "COGNITIVE / STRUCTURAL NOTES", "-" * 88]
        lines.extend(f"- {note}" for note in self.complexity_notes) if self.complexity_notes else lines.append("- The expression is structurally straightforward; this is not an official KPM TP assignment.")
        lines += ["", "SUGGESTED WORKFLOW", "-" * 88]
        lines.extend(f"{index}. {step}" for index, step in enumerate(self.workflow, 1)) if self.workflow else lines.append("No specialised route was selected; inspect the equation manually.")
        lines += ["", "CAUTIONS", "-" * 88]
        lines.extend(f"- {caution}" for caution in self.cautions)
        lines += ["", "KNOWLEDGE SOURCES", "-" * 88]
        lines.extend(f"- {source}" for source in self.knowledge_sources)
        lines += [
            "",
            "IMPORTANT: RECOGNITION IS NOT A PROOF OR A COMPLETE SOLUTION.",
            "A pattern match only identifies a candidate mathematical family and route. No identity has been certified and no solution set has been established by this report.",
            "Geometric and analytic recipes from the v0.5 handbook remain documented methods unless an independent checker is implemented and enabled.",
            "",
        ]
        return "\n".join(lines)


def _normalise_abs_bars(text: str) -> str:
    """Convert paired |...| notation to abs(...), preserving ordinary division syntax."""
    out: list[str] = []
    inside = False
    for char in text:
        if char == "|":
            out.append("abs(" if not inside else ")")
            inside = not inside
        else:
            out.append(char)
    if inside:
        raise ExpressionInputError("Absolute-value bars must be paired. Use abs(expression) if preferred.")
    return "".join(out)


def split_relation(text: str) -> tuple[str, str, str]:
    """Split one equality/inequality without interpreting it as an identity."""
    cleaned = text.strip().replace("≤", "<=").replace("≥", ">=").replace("≠", "!=")
    cleaned = cleaned.replace("==", "=")
    parts = re.split(r"(<=|>=|!=|=|<|>)", cleaned)
    if len(parts) != 3 or not parts[0].strip() or not parts[2].strip():
        raise ExpressionInputError(
            "Enter one relation per line, for example sin(2*x) = 1/2 or |cos(x)| <= 1/2."
        )
    return parts[0].strip(), parts[1], parts[2].strip()


def parse_equation_line(text: str) -> EquationRecord:
    lhs_text, relation, rhs_text = split_relation(text)
    # Preserve source structure for recognition (e.g. sin(pi/6), cancelled
    # factors and cofunction arguments) before SymPy performs evaluation.
    parser = _SafeSympyParser(evaluate=False)
    lhs = parser.parse(_normalise_abs_bars(lhs_text))
    rhs = parser.parse(_normalise_abs_bars(rhs_text))
    return EquationRecord(text.strip(), lhs_text, relation, rhs_text, lhs, rhs)


def _trig_nodes(expr: sp.Expr) -> list[sp.Expr]:
    return [node for node in sp.preorder_traversal(expr) if getattr(node, "func", None) in TRIG_FUNCTIONS]


def _all_trig_nodes(equations: Iterable[EquationRecord]) -> list[sp.Expr]:
    nodes: list[sp.Expr] = []
    for equation in equations:
        nodes.extend(_trig_nodes(equation.lhs))
        nodes.extend(_trig_nodes(equation.rhs))
    return nodes


def _free_symbols(expr: sp.Expr) -> set[sp.Symbol]:
    return set(expr.free_symbols)


def _angle_symbol_counts(nodes: Iterable[sp.Expr]) -> Counter:
    counts: Counter = Counter()
    for node in nodes:
        for symbol in node.args[0].free_symbols:
            counts[symbol.name] += 1
    return counts


def _choose_angle_variables(nodes: list[sp.Expr]) -> tuple[str, ...]:
    counts = _angle_symbol_counts(nodes)
    if not counts:
        return ()
    preferred = {"x": 0, "theta": 1, "θ": 2, "t": 3, "A": 4, "B": 5, "C": 6}
    return tuple(name for name, _ in sorted(counts.items(), key=lambda item: (-item[1], preferred.get(item[0], 99), item[0])))


def _is_zero(value: sp.Expr) -> bool:
    try:
        return sp.simplify(value) == 0
    except Exception:
        return False


def _linear_coefficients(argument: sp.Expr, variable: sp.Symbol) -> tuple[sp.Expr, sp.Expr] | None:
    try:
        poly = sp.Poly(sp.expand(argument), variable)
        if poly.degree() <= 1:
            a = sp.simplify(poly.coeff_monomial(variable))
            b = sp.simplify(poly.coeff_monomial(1))
            # Coefficients may be symbolic parameters (e.g. b*x+c), but they
            # must not themselves contain the angle variable.
            if variable not in a.free_symbols and variable not in b.free_symbols:
                return a, b
    except (sp.PolynomialError, TypeError, ValueError):
        pass
    return None


def _special_angle(argument: sp.Expr) -> bool:
    try:
        ratio = sp.simplify(argument / sp.pi)
        if ratio.is_Rational:
            return ratio.q in {1, 2, 3, 4, 6, 8, 12, 18, 24}
    except Exception:
        pass
    return False


def _has_rational_trig(expr: sp.Expr, original: str = "") -> bool:
    try:
        numerator, denominator = sp.fraction(expr, exact=True)
        if denominator != 1 and bool(_trig_nodes(denominator)):
            return True
    except Exception:
        pass
    for node in sp.preorder_traversal(expr):
        if isinstance(node, sp.Pow) and node.exp.is_negative and bool(_trig_nodes(node.base)):
            return True
    return False


def _contains_multiple_angle(nodes: list[sp.Expr], variable: sp.Symbol | None, target: int | None = None) -> bool:
    if variable is None:
        return False
    for node in nodes:
        linear = _linear_coefficients(node.args[0], variable)
        if linear is None:
            continue
        coefficient, _offset = linear
        if coefficient.is_Integer:
            n = int(coefficient)
            if target is not None and abs(n) == target:
                return True
            if target is None and abs(n) >= 2:
                return True
    return False


def _has_half_angle(nodes: list[sp.Expr], variable: sp.Symbol | None) -> bool:
    if variable is None:
        return False
    for node in nodes:
        linear = _linear_coefficients(node.args[0], variable)
        if linear and sp.simplify(linear[0] - sp.Rational(1, 2)) == 0:
            return True
    return False


def _same_argument_pair(nodes: list[sp.Expr], first, second) -> bool:
    args_first = {n.args[0] for n in nodes if n.func == first}
    args_second = {n.args[0] for n in nodes if n.func == second}
    return bool(args_first & args_second)


def _has_linear_sin_cos(expr: sp.Expr) -> tuple[bool, bool]:
    """Return (found, found in both sine and cosine at a shared argument)."""
    for argument in {n.args[0] for n in _trig_nodes(expr)}:
        sin_atom = sp.sin(argument)
        cos_atom = sp.cos(argument)
        try:
            poly = sp.Poly(sp.expand(expr), sin_atom, cos_atom)
            if poly.total_degree() <= 1 and poly.degree(sin_atom) <= 1 and poly.degree(cos_atom) <= 1:
                if poly.degree(sin_atom) == 1 and poly.degree(cos_atom) == 1:
                    return True, True
                if poly.degree(sin_atom) == 1 or poly.degree(cos_atom) == 1:
                    return True, False
        except (sp.PolynomialError, TypeError, ValueError):
            continue
    return False, False


def _is_linear_combination_sin_cos(expr: sp.Expr, variable: sp.Symbol | None) -> bool:
    if variable is None:
        return False
    found, both = _has_linear_sin_cos(expr)
    return both


def _has_single_function_polynomial(expr: sp.Expr, allowed: set) -> bool:
    nodes = _trig_nodes(expr)
    unique = list(dict.fromkeys(nodes))
    if len(unique) != 1 or unique[0].func not in allowed:
        return False
    try:
        poly = sp.Poly(sp.expand(expr), unique[0])
        return poly.degree() >= 2
    except (sp.PolynomialError, TypeError, ValueError):
        return False


def _has_quadratic_sin_cos(expr: sp.Expr) -> bool:
    nodes = _trig_nodes(expr)
    for arg in {n.args[0] for n in nodes}:
        s, c = sp.sin(arg), sp.cos(arg)
        if s in nodes and c in nodes:
            try:
                poly = sp.Poly(sp.expand(expr), s, c)
                if poly.total_degree() == 2:
                    return True
            except (sp.PolynomialError, TypeError, ValueError):
                continue
    return False


def _has_equal_squares(lhs: sp.Expr, rhs: sp.Expr) -> bool:
    left_nodes, right_nodes = _trig_nodes(lhs), _trig_nodes(rhs)
    if len(left_nodes) == 1 and len(right_nodes) == 1:
        return sp.simplify(left_nodes[0]**2 - lhs) == 0 and sp.simplify(right_nodes[0]**2 - rhs) == 0
    try:
        diff = sp.expand(lhs - rhs)
        return any(
            sp.simplify(diff - (a**2 - b**2)) == 0 or sp.simplify(diff + (a**2 - b**2)) == 0
            for a in left_nodes for b in right_nodes
        )
    except Exception:
        return False


def _contains_reciprocal_pair(nodes: list[sp.Expr]) -> bool:
    functions = {node.func for node in nodes}
    return bool(
        ({sp.sec, sp.tan} <= functions)
        or ({sp.csc, sp.cot} <= functions)
        or ({sp.tan, sp.cot} <= functions)
    )


def _contains_one_plus_minus(expr: sp.Expr) -> bool:
    # Inspect every additive subexpression so 1±cos(x) is recognised even
    # when it occurs inside a denominator or a larger product.
    for subexpr in sp.preorder_traversal(expr):
        if not isinstance(subexpr, sp.Add):
            continue
        for trig in _trig_nodes(subexpr):
            if trig.func not in {sp.sin, sp.cos}:
                continue
            for sign in (-1, 1):
                if _is_zero(subexpr - (1 + sign * trig)):
                    return True
    return False



def _is_basic_transformed_graph(expr: sp.Expr, trig_atom: sp.Expr, variable: sp.Symbol | None) -> bool:
    """Check y=a*f(bx)+c structurally, not merely by seeing one trig node."""
    if variable is None:
        return False
    try:
        coefficient = sp.simplify(expr.coeff(trig_atom))
        remainder = sp.simplify(expr - coefficient * trig_atom)
        if coefficient == 0 or coefficient.has(trig_atom) or remainder.has(trig_atom):
            return False
        if variable in coefficient.free_symbols or variable in remainder.free_symbols:
            return False
        if _trig_nodes(coefficient) or _trig_nodes(remainder):
            return False
        return _linear_coefficients(trig_atom.args[0], variable) is not None
    except Exception:
        return False

def _has_product_of_trig(expr: sp.Expr) -> bool:
    for node in sp.preorder_traversal(expr):
        if not isinstance(node, sp.Mul):
            continue
        positive_atoms = []
        for factor in sp.Mul.make_args(node):
            if isinstance(factor, sp.Pow) and factor.exp.is_negative:
                continue
            positive_atoms.extend(_trig_nodes(factor))
        if len(set(positive_atoms)) >= 2:
            return True
    return False


def _has_sum_product_structure(equation: EquationRecord) -> bool:
    nodes = _trig_nodes(equation.lhs) + _trig_nodes(equation.rhs)
    if len(nodes) < 2:
        return False
    args = {node.args[0] for node in nodes}
    return len(args) >= 2


def _is_nested(nodes: list[sp.Expr]) -> bool:
    for node in nodes:
        if _trig_nodes(node.args[0]):
            return True
    return False


def _has_parameter(symbols: set[sp.Symbol], angle_variables: tuple[str, ...]) -> bool:
    return any(symbol.name not in angle_variables for symbol in symbols)


def _has_degree_notation(text: str, prompt: str) -> bool:
    combined = f"{text} {prompt}".casefold()
    return "°" in combined or "degree" in combined or "degrees" in combined


def _interval_flags(interval_text: str, prompt_text: str) -> tuple[bool, bool]:
    combined = f"{interval_text} {prompt_text}".casefold()
    negative = bool(re.search(r"(?:^|[<≤,\[(])\s*-\s*(?:\d|pi|π)", combined))
    multi = bool(re.search(r"(?:720\s*°|540\s*°|360\s*°|4\s*\*\s*pi|3\s*\*\s*pi|2\s*\*\s*pi|4π|3π|2π)", combined))
    # A clearly supplied interval wider than one revolution is enough; the
    # expression is only a heuristic flag, never an interval proof.
    return multi, negative


def _extract_special_prompt_flags(prompt: str) -> dict[str, bool]:
    p = prompt.casefold()
    return {
        "solve": bool(re.search(r"\b(solve|find the solution|find all roots|determine x)\b", p)),
        "exact_value": bool(re.search(r"\b(exact value|evaluate|find the value|simplify exactly)\b", p)),
        "prove": bool(re.search(r"\b(prove|show that|verify|establish|derive)\b", p)),
        "hence": bool(re.search(r"\b(hence|therefore|using the result|using your answer|from part)\b", p)),
        "count": bool(re.search(r"\b(number of solutions|how many solutions|count the roots|number of roots|number of intersections)\b", p)),
        "no_solution": bool(re.search(r"\b(no solution|no real solution|has no roots|without a solution)\b", p)),
        "parameter": bool(re.search(r"\b(parameter|range of k|range of m|values of k|values of m|constant m)\b", p)),
        "quadrant": bool(re.search(r"\b(quadrant|reference angle|acute angle|obtuse angle)\b", p)),
        "triangle": bool(re.search(r"\b(triangle|interior angles|angle sum)\b", p)),
        "graph": bool(re.search(r"\b(graph|sketch|plot|intersection|curve)\b", p)),
        "inequality": bool(re.search(r"\b(inequality|greater than|less than|at least|at most)\b", p)),
        "cancel": bool(re.search(r"\b(cancel|cancellation|divide both sides)\b", p)),
        "system": bool(re.search(r"\b(simultaneous|system of equations|solve together)\b", p)),
    }


def _detect_interval_text(interval_text: str, prompt_text: str) -> str:
    if interval_text.strip():
        return interval_text.strip()
    pattern = re.compile(
        r"([+-]?(?:\d+(?:\.\d+)?\s*(?:\*\s*)?\s*(?:pi|π)?|pi|π)\s*°?)\s*(?:<=|≤|<)\s*([A-Za-zθ][A-Za-z0-9_]*)\s*(?:<=|≤|<)\s*([+-]?(?:\d+(?:\.\d+)?\s*(?:\*\s*)?\s*(?:pi|π)?|pi|π)\s*°?)",
        re.IGNORECASE,
    )
    match = pattern.search(prompt_text)
    return match.group(0) if match else ""


def _build_workflow(matches: list[RecognitionMatch], task_type: str) -> tuple[str, ...]:
    steps: list[str] = []
    if task_type in {"Identity proof", "Derivation / proof"}:
        steps.append("Preserve the exact target and original common domain before selecting any theorem.")
        steps.append("Choose a proof route whose dependency tree does not contain the open target as an assumption.")
    elif task_type == "Graphical equation / intersection":
        steps.append("Identify the interval and sketch or analyse both sides as separate functions.")
        steps.append("Count only valid intersections; handle poles, holes, tangencies and included endpoints.")
    elif task_type == "Trigonometric inequality":
        steps.append("Move all terms to one side, locate critical zeros and domain breaks, then analyse signs by interval.")
    elif task_type == "Simultaneous trigonometric system":
        steps.append("Use shared variables and certified relations; solve all equations jointly and restore angle branches.")
    else:
        steps.append("Classify the angle variable, parameters, angle unit and requested interval before solving.")
        steps.append("Generate all necessary periodic branches, then filter against the original interval.")
    method_ids = []
    for match in matches[:4]:
        for method in match.methods:
            if method not in method_ids:
                method_ids.append(method)
    if method_ids:
        steps.append("Candidate knowledge routes: " + ", ".join(method_ids) + ".")
    steps.append("Verify every candidate in the original relation and retain all original denominator/radical restrictions.")
    steps.append("Do not mark the task PROVED or SOLVED_COMPLETE until a checked derivation and completeness argument exist.")
    return tuple(steps)


def _classify_equation(
    equations: list[EquationRecord], prompt: str, interval: str,
    angle_variables: tuple[str, ...],
) -> tuple[list[RecognitionMatch], str, list[str], list[str]]:
    prompt_flags = _extract_special_prompt_flags(prompt)
    nodes = _all_trig_nodes(equations)
    all_exprs = [e.lhs for e in equations] + [e.rhs for e in equations]
    all_symbols = set().union(*(_free_symbols(expr) for expr in all_exprs)) if all_exprs else set()
    angle_symbols = {s for s in all_symbols if s.name in angle_variables}
    parameter_symbols = all_symbols - angle_symbols
    symbol_by_name = {symbol.name: symbol for symbol in all_symbols}
    variable = symbol_by_name.get(angle_variables[0]) if angle_variables else None
    matches: dict[str, list[str]] = {}

    def add(class_id: str, reason: str) -> None:
        matches.setdefault(class_id, [])
        if reason not in matches[class_id]:
            matches[class_id].append(reason)

    combined_text = "\n".join(e.original for e in equations)
    has_trig = bool(nodes)
    has_abs = any(expr.has(sp.Abs) for expr in all_exprs)
    has_sqrt = any(
        isinstance(node, sp.Pow) and sp.simplify(node.exp - sp.Rational(1, 2)) == 0
        for expr in all_exprs for node in sp.preorder_traversal(expr)
    )
    has_rational = any(_has_rational_trig(expr) for expr in all_exprs)
    funcs = {node.func for node in nodes}
    function_names = {TRIG_NAME[f] for f in funcs}
    all_variables = set().union(*(_free_symbols(expr) for expr in all_exprs)) if all_exprs else set()
    # A graph dependent variable y is not an angle parameter.
    is_y_graph = any(
        (e.lhs == sp.Symbol("y", real=True) or e.rhs == sp.Symbol("y", real=True))
        and bool(_trig_nodes(e.lhs) + _trig_nodes(e.rhs)) for e in equations
    )
    if is_y_graph:
        parameter_symbols.discard(sp.Symbol("y", real=True))
    multi_turn, negative_interval = _interval_flags(interval, prompt)

    # Prompt/task-level and system recognition.
    if len(equations) >= 2 or prompt_flags["system"]:
        add("EQREC-051", "Two or more relations are supplied or the prompt explicitly requests simultaneous solving.")
    if prompt_flags["hence"] and prompt_flags["prove"] and prompt_flags["solve"]:
        add("EQREC-055", "The wording links a proof/derivation to a later equation through 'hence' or an earlier result.")
    if prompt_flags["count"]:
        add("EQREC-041", "The prompt asks for the number of roots, solutions or intersections rather than exact roots.")
    if prompt_flags["no_solution"] and (prompt_flags["parameter"] or parameter_symbols):
        add("EQREC-040", "The prompt asks for a no-solution parameter range or a level with no graph intersection.")
    if prompt_flags["quadrant"]:
        add("EQREC-045", "The prompt supplies a quadrant, reference-angle or acute/obtuse constraint.")
    if prompt_flags["triangle"]:
        add("EQREC-047", "Triangle-angle language indicates positivity and an angle-sum condition.")
    if prompt_flags["cancel"]:
        add("EQREC-032", "The prompt explicitly refers to cancellation or division by a factor.")
    if prompt_flags["parameter"] or parameter_symbols:
        if has_trig:
            add("EQREC-046", "A symbol other than the detected angle variable or parameter wording occurs in the problem.")

    # Relation-level graph and inequality patterns.
    if any(e.relation in {"<", ">", "<=", ">="} for e in equations) and has_trig:
        add("EQREC-042", "The input relation is an inequality containing trigonometric terms.")
    for equation in equations:
        if equation.relation not in {"=", "=="}:
            continue
        y_symbol = sp.Symbol("y", real=True)
        graph_expr = None
        if equation.lhs == y_symbol and _trig_nodes(equation.rhs):
            graph_expr = equation.rhs
        elif equation.rhs == y_symbol and _trig_nodes(equation.lhs):
            graph_expr = equation.lhs
        if graph_expr is not None:
            if graph_expr.has(sp.Abs):
                add("EQREC-037", "The dependent variable y is equated to a trigonometric expression containing absolute value.")
            trig_graphs = _trig_nodes(graph_expr)
            if len(trig_graphs) == 1 and not graph_expr.has(sp.Abs) and _is_basic_transformed_graph(graph_expr, trig_graphs[0], variable):
                function = TRIG_NAME[trig_graphs[0].func]
                if function == "sin": add("EQREC-034", "The graph is y = a sin(bx) + c or a structurally equivalent form.")
                elif function == "cos": add("EQREC-035", "The graph is y = a cos(bx) + c or a structurally equivalent form.")
                elif function == "tan": add("EQREC-036", "The graph is y = a tan(bx) + c or a structurally equivalent form.")

        lhs_nodes, rhs_nodes = _trig_nodes(equation.lhs), _trig_nodes(equation.rhs)
        lhs_functions = {n.func for n in lhs_nodes}
        rhs_functions = {n.func for n in rhs_nodes}
        lhs_constant = not equation.lhs.free_symbols
        rhs_constant = not equation.rhs.free_symbols
        is_graph_relation = (equation.lhs == sp.Symbol("y", real=True) or equation.rhs == sp.Symbol("y", real=True))
        if has_trig and (lhs_constant ^ rhs_constant):
            add("EQREC-038", "One side is constant, giving a horizontal-line intersection problem.")
        elif has_trig and equation.lhs.free_symbols and equation.rhs.free_symbols and not is_graph_relation:
            add("EQREC-039", "Both sides depend on variables, so the equation is a non-constant intersection problem.")

        if len(lhs_nodes) == 1 and not rhs_nodes and rhs_constant:
            add(FUNCTION_CLASS[TRIG_NAME[lhs_nodes[0].func]], f"A single {TRIG_NAME[lhs_nodes[0].func]} expression is equated to a constant.")
        if len(rhs_nodes) == 1 and not lhs_nodes and lhs_constant:
            add(FUNCTION_CLASS[TRIG_NAME[rhs_nodes[0].func]], f"A single {TRIG_NAME[rhs_nodes[0].func]} expression is equated to a constant.")

        # Same-function and cofunction equalities.
        if len(lhs_nodes) == 1 and len(rhs_nodes) == 1:
            first, second = lhs_nodes[0], rhs_nodes[0]
            if first.func == second.func:
                id_for = {sp.sin: "EQREC-007", sp.cos: "EQREC-008", sp.tan: "EQREC-009", sp.cot: "EQREC-010"}
                if first.func in id_for:
                    add(id_for[first.func], f"Both sides use the same {TRIG_NAME[first.func]} function, potentially with different arguments.")
            if {first.func, second.func} == {sp.sin, sp.cos}:
                if _is_zero(first.args[0] + second.args[0] - sp.pi/2) or _is_zero(first.args[0] - second.args[0] - sp.pi/2):
                    add("EQREC-011", "The sine and cosine arguments have a quarter-turn cofunction relationship.")

        # Linear combination and phase structures.
        equation_function_set = {n.func for n in lhs_nodes + rhs_nodes}
        equation_argument_set = {n.args[0] for n in lhs_nodes + rhs_nodes}
        one_function_one_argument = len(equation_function_set) == 1 and len(equation_argument_set) == 1
        for expr in (equation.lhs, equation.rhs, equation.lhs - equation.rhs):
            found, both = _has_linear_sin_cos(expr)
            if both:
                add("EQREC-012", "A linear combination of sine and cosine at a shared angle is present.")
            if one_function_one_argument and _has_single_function_polynomial(expr, {sp.sin, sp.cos}):
                add("EQREC-015", "The expression is polynomial in one sine or cosine value.")
            if _has_quadratic_sin_cos(expr):
                add("EQREC-016", "Sine and cosine at the same angle occur in a quadratic algebraic expression.")
            if _has_product_of_trig(expr) and _same_argument_pair(_trig_nodes(expr), sp.sin, sp.cos):
                add("EQREC-018", "A product of sine and cosine with the same argument is present.")
            if _contains_one_plus_minus(expr):
                add("EQREC-029", "A factor or term of the form 1 ± sin(angle) or 1 ± cos(angle) is present.")
            if one_function_one_argument and _has_single_function_polynomial(expr, {sp.tan, sp.cot}):
                add("EQREC-020", "The expression is polynomial in one tangent or cotangent value.")

        if _is_linear_combination_sin_cos(equation.lhs, variable) or _is_linear_combination_sin_cos(equation.rhs, variable):
            if lhs_nodes and rhs_nodes:
                add("EQREC-013", "A sine-cosine linear combination is equated to another trigonometric expression.")
        for node in nodes:
            arg = node.args[0]
            if isinstance(arg, sp.Add) and len(arg.args) >= 2:
                if any(term.free_symbols for term in arg.args) and len(set().union(*(term.free_symbols for term in arg.args))) >= 2:
                    add("EQREC-023", "A trigonometric argument contains a sum or difference of angle variables/terms.")
                if any(term.is_number for term in arg.args) and any(term.free_symbols for term in arg.args):
                    add("EQREC-014", "A trigonometric argument includes an angle variable shifted by a constant phase.")

        if _has_equal_squares(equation.lhs, equation.rhs):
            add("EQREC-017", "Both sides are single squared trigonometric values or their difference factors as equal squares.")
        expanded_difference = sp.expand(equation.lhs - equation.rhs)
        if any(
            expanded_difference.has(sp.sin(arg)**2) and expanded_difference.has(sp.cos(arg)**2)
            for arg in {n.args[0] for n in nodes}
        ):
            add("EQREC-019", "A sum or difference of sine-square and cosine-square terms is present.")

        cofunction_pair = (
            len(lhs_nodes + rhs_nodes) == 2
            and {lhs_nodes[0].func, rhs_nodes[0].func} == {sp.sin, sp.cos}
            and (_is_zero(lhs_nodes[0].args[0] + rhs_nodes[0].args[0] - sp.pi/2)
                 or _is_zero(lhs_nodes[0].args[0] - rhs_nodes[0].args[0] - sp.pi/2))
        ) if len(lhs_nodes) == 1 and len(rhs_nodes) == 1 else False
        if _has_sum_product_structure(equation) and not cofunction_pair:
            add("EQREC-048", "Sums/products of trigonometric functions with multiple arguments suggest sum-to-product or product-to-sum.")
        if _has_product_of_trig(equation.lhs) or _has_product_of_trig(equation.rhs):
            add("EQREC-049", "At least one side contains a product of multiple trigonometric factors.")

    # Global structural fingerprints.
    if has_abs:
        add("EQREC-030", "An absolute-value operator encloses a trigonometric expression.")
    if has_sqrt:
        add("EQREC-031", "A square-root expression is present; principal-root sign conditions may matter.")
    if _is_nested(nodes):
        add("EQREC-052", "A trigonometric function occurs inside the argument of another trigonometric function.")
    if has_rational:
        add("EQREC-027", "A quotient or negative power contains trigonometric terms.")
    if _contains_reciprocal_pair(nodes):
        add("EQREC-028", "A recognised reciprocal/quotient pair (sec–tan, csc–cot or tan–cot) occurs.")
    if ({sp.sec, sp.tan} <= funcs or {sp.csc, sp.cot} <= funcs or {sp.tan, sp.cot} <= funcs) and any(isinstance(expr, sp.Add) for expr in all_exprs):
        add("EQREC-050", "A sum of reciprocal or quotient trigonometric functions is present.")
    for equation in equations:
        for side_text in (equation.lhs_text, equation.rhs_text):
            if "/" in side_text and re.search(r"(?:sin|cos|tan|cot|sec|csc)\s*\([^)]*\).*?/.*?(?:sin|cos|tan|cot|sec|csc)\s*\(", side_text, re.IGNORECASE):
                add("EQREC-032", "A trigonometric quotient may contain a factor that must be cancelled only after checking its zero set.")
    if has_rational and {sp.sin, sp.cos} <= funcs:
        add("EQREC-021", "A rational expression mixes sine and cosine and may benefit from quotient conversion or conjugate rationalisation.")
    if _contains_one_plus_minus(sum(all_exprs, sp.Integer(0))):
        add("EQREC-029", "The combined relation contains 1 ± sin(angle) or 1 ± cos(angle).")

    if variable is not None:
        if _contains_multiple_angle(nodes, variable, target=2) and not is_y_graph:
            add("EQREC-022", "At least one trigonometric argument is a double angle of the main variable.")
        if _contains_multiple_angle(nodes, variable, target=None) and not is_y_graph:
            if not _contains_multiple_angle(nodes, variable, target=2):
                add("EQREC-024", "At least one argument is an integer multiple of the main angle with magnitude at least two.")
            else:
                if _contains_multiple_angle(nodes, variable, target=3):
                    add("EQREC-024", "A triple-angle or higher multiple-angle structure is present alongside a double-angle term.")
        if any(
            _linear_coefficients(node.args[0], variable)
            and sp.simplify(abs(_linear_coefficients(node.args[0], variable)[0]) - sp.Rational(1, 2)) == 0
            for node in nodes
        ):
            add("EQREC-025", "A trigonometric argument contains one-half of the main angle.")
        if any(
            _linear_coefficients(node.args[0], variable)
            and (sp.simplify(_linear_coefficients(node.args[0], variable)[0] - 1) != 0
                 or sp.simplify(_linear_coefficients(node.args[0], variable)[1]) != 0)
            for node in nodes
        ):
            add("EQREC-006", "A trigonometric argument is affine in the main variable, with a scale or shift.")
        if any(node.func == sp.tan and _has_half_angle([node], variable) for node in nodes):
            add("EQREC-033", "The tangent half-angle substitution tan(x/2) is explicit in the expression.")
        if has_trig and any(
            variable in (expr.free_symbols - (set().union(*(set(n.args[0].free_symbols) for n in _trig_nodes(expr))) if _trig_nodes(expr) else set()))
            for expr in all_exprs
        ):
            add("EQREC-053", "The angle variable also appears algebraically outside a trigonometric argument.")

    if prompt_flags["parameter"] and has_trig:
        add("EQREC-040", "The prompt asks for a parameter range or a number of intersections as a level changes.")
    if multi_turn:
        add("EQREC-043", "The supplied interval or prompt visibly spans multiple revolutions.")
    if negative_interval:
        add("EQREC-044", "The requested interval includes a negative angle bound.")
    if prompt_flags["quadrant"] or re.search(r"\b(?:quadrant\s+[IV1-4]|QI{1,3}|QIV)\b", prompt, re.IGNORECASE):
        add("EQREC-045", "A quadrant or reference-angle condition is present.")
    if prompt_flags["triangle"]:
        add("EQREC-047", "Triangle constraints are part of the mathematical context.")
    if prompt_flags["count"] and has_trig:
        add("EQREC-041", "The requested output is a count of distinct solutions.")
    if prompt_flags["no_solution"] and (prompt_flags["parameter"] or parameter_symbols):
        add("EQREC-040", "The requested output is a parameter range with no intersection/solution.")

    # Tangent half-angle substitution is also detected from prompt wording.
    if re.search(r"tan\s*\(\s*[a-zA-Zθ]\s*/\s*2\s*\)", combined_text + " " + prompt, re.IGNORECASE):
        add("EQREC-033", "The expression or prompt explicitly names tan(angle/2).")

    # A hidden identity may simplify an unfamiliar equation; this is a route hint,
    # not an assertion that the original equation is true.
    if any(_special_angle(node.args[0]) for node in nodes):
        add("EQREC-026", "A constant angle or phase is a rational multiple of π associated with exact-angle work.")

    if has_trig and "EQREC-011" not in matches and any(
        len(_trig_nodes(e.lhs - e.rhs)) >= 2
        and (any(_contains_multiple_angle(_trig_nodes(e.lhs - e.rhs), v, 2) for v in [variable] if v is not None)
             or _has_rational_trig(e.lhs - e.rhs))
        for e in equations
    ):
        add("EQREC-054", "The equation contains compound, multiple-angle or rational structure that may conceal a simpler certified identity.")

    # Identity / derivation / equation task labels are determined from the prompt,
    # not from whether SymPy happens to simplify the relation.
    if prompt_flags["prove"] and prompt_flags["solve"] and prompt_flags["hence"]:
        task_type = "Multi-part proof followed by equation"
    elif prompt_flags["prove"]:
        task_type = "Identity proof" if any(e.relation == "=" for e in equations) else "Derivation / proof"
    elif any(e.relation in {"<", ">", "<=", ">="} for e in equations):
        task_type = "Trigonometric inequality"
    elif len(equations) >= 2 or prompt_flags["system"]:
        task_type = "Simultaneous trigonometric system"
    elif prompt_flags["graph"] or any(e.lhs == sp.Symbol("y", real=True) or e.rhs == sp.Symbol("y", real=True) for e in equations):
        task_type = "Graphical equation / intersection"
    elif "EQREC-047" in matches:
        task_type = "Conditional triangle-angle relation"
    elif prompt_flags["exact_value"]:
        task_type = "Exact trigonometric value"
    elif "EQREC-041" in matches:
        task_type = "Graphical equation / solution count"
    elif "EQREC-053" in matches:
        task_type = "Graphical equation / intersection"
    elif prompt_flags["solve"]:
        task_type = "Trigonometric equation"
    elif has_trig:
        task_type = "Trigonometric equation / relation"
    else:
        task_type = "General algebraic relation"

    # Candidate ranking: exact graph/task structures first, then specific algebraic
    # fingerprints, then broad context matches. This ranking is not a probability.
    priority = {
        "EQREC-055": 0, "EQREC-051": 1, "EQREC-037": 2, "EQREC-034": 3,
        "EQREC-035": 3, "EQREC-036": 3, "EQREC-042": 4, "EQREC-039": 5,
        "EQREC-040": 6, "EQREC-041": 7, "EQREC-033": 8, "EQREC-052": 9,
        "EQREC-031": 10, "EQREC-030": 11, "EQREC-027": 12, "EQREC-021": 13,
        "EQREC-028": 14, "EQREC-048": 15, "EQREC-049": 16, "EQREC-012": 17,
        "EQREC-013": 18, "EQREC-016": 19, "EQREC-015": 20, "EQREC-022": 21,
        "EQREC-023": 22, "EQREC-024": 23, "EQREC-025": 24, "EQREC-026": 25,
        "EQREC-017": 26, "EQREC-018": 27, "EQREC-019": 28, "EQREC-020": 29,
        "EQREC-029": 30, "EQREC-032": 31, "EQREC-046": 32, "EQREC-047": 33,
        "EQREC-043": 34, "EQREC-044": 35, "EQREC-045": 36, "EQREC-053": 37,
        "EQREC-054": 38, "EQREC-014": 39, "EQREC-006": 40, "EQREC-007": 41,
        "EQREC-008": 42, "EQREC-009": 43, "EQREC-010": 44, "EQREC-011": 45,
        "EQREC-001": 46, "EQREC-002": 47, "EQREC-003": 48, "EQREC-004": 49,
        "EQREC-005": 50, "EQREC-038": 51,
    }
    catalogue_titles = CATALOGUE_TITLES
    ordered_ids = sorted(matches, key=lambda class_id: (priority.get(class_id, 99), class_id))
    match_records = [
        RecognitionMatch(
            class_id,
            catalogue_titles.get(class_id, class_id),
            CLASS_META[class_id]["band"],
            CLASS_META[class_id]["standard"],
            tuple(matches[class_id]),
            tuple(CLASS_META[class_id]["methods"]),
        )
        for class_id in ordered_ids
    ]

    complexity_notes: list[str] = []
    if len(equations) > 1:
        complexity_notes.append("Multiple relations require a shared-variable consistency check.")
    if len(nodes) >= 4:
        complexity_notes.append("Several trigonometric occurrences are present; a multi-step route may be needed.")
    if parameter_symbols:
        complexity_notes.append("Parameter symbols must not be confused with the angle variable.")
    if any(_has_rational_trig(expr) for expr in all_exprs):
        complexity_notes.append("Rational trigonometric terms require an original-denominator ledger.")
    if has_abs or has_sqrt:
        complexity_notes.append("Absolute values or principal square roots introduce sign/branch conditions.")
    if multi_turn or negative_interval:
        complexity_notes.append("The requested interval is not the default single positive revolution.")
    if task_type in {"Graphical equation / intersection", "Multi-part proof followed by equation"}:
        complexity_notes.append("A graph or multi-part structure requires completeness across the stated interval/subparts.")

    # Estimated cognitive level is an engineering hint only, not an official KPM grade.
    if len(equations) > 1 or task_type == "Multi-part proof followed by equation":
        cognitive = "TP5–TP6-style structure (engineering estimate; not an official assignment)"
    elif len(matches) >= 4 or has_abs or has_sqrt or has_rational or prompt_flags["parameter"]:
        cognitive = "TP5-style structure (engineering estimate; not an official assignment)"
    elif len(matches) >= 2 or multi_turn or negative_interval or prompt_flags["quadrant"]:
        cognitive = "TP4-style structure (engineering estimate; not an official assignment)"
    elif has_trig:
        cognitive = "TP3-style structure (engineering estimate; not an official assignment)"
    else:
        cognitive = "TP1–TP2-style structure (engineering estimate; not an official assignment)"

    return match_records, task_type, complexity_notes, sorted(s.name for s in parameter_symbols)


def recognize_problem(
    equation_text: str,
    prompt_text: str = "",
    interval_text: str = "",
) -> RecognitionResult:
    """Recognise one or more trigonometric equations from their structure.

    `equation_text` accepts one relation per line. `prompt_text` supplies task
    wording such as 'solve', 'prove and hence solve', 'number of solutions', or
    'in quadrant II'. `interval_text` is optional and is retained verbatim.
    """
    raw_lines = [line.strip() for line in equation_text.splitlines() if line.strip()]
    if not raw_lines:
        raise ExpressionInputError("Enter at least one equation or inequality.")
    equations = [parse_equation_line(line) for line in raw_lines]
    nodes = _all_trig_nodes(equations)
    angle_variables = _choose_angle_variables(nodes)
    if not angle_variables and re.search(r"\btriangle\b|\binterior angles\b", prompt_text, re.IGNORECASE):
        symbols = set().union(*(set(e.lhs.free_symbols) | set(e.rhs.free_symbols) for e in equations))
        triangle_names = [name for name in ("A", "B", "C") if any(symbol.name == name for symbol in symbols)]
        angle_variables = tuple(triangle_names)
    interval = _detect_interval_text(interval_text, prompt_text)
    unit = "degrees" if _has_degree_notation(equation_text, prompt_text + " " + interval) else "radians"
    matches, task_type, complexity_notes, parameter_names = _classify_equation(
        equations, prompt_text, interval, angle_variables
    )

    domain: list[str] = []
    for equation in equations:
        domain.extend(_domain_conditions(equation.lhs, equation.rhs))
        domain.extend(_domain_conditions_from_text(equation.lhs_text, equation.rhs_text))
    domain = list(dict.fromkeys(domain))

    cautions: list[str] = [
        "Recognition is structural guidance only; it does not prove the relation or solve it.",
        "All original denominator, reciprocal-function and radical restrictions remain in force.",
    ]
    if any(e.relation in {"<", ">", "<=", ">="} for e in equations):
        cautions.append("Inequality transformations require sign-aware reasoning; multiplying by an unknown-sign expression may reverse the inequality.")
    if any("tan" in str(e.lhs) + str(e.rhs) or "cot" in str(e.lhs) + str(e.rhs) for e in equations):
        cautions.append("Tangent/cotangent equations must exclude poles and zeros of their defining denominators.")
    if any("sqrt" in e.lhs_text or "sqrt" in e.rhs_text or "√" in e.original for e in equations):
        cautions.append("For square roots, enforce radicand ≥ 0 and the nonnegative principal-root condition before squaring.")
    if any("abs" in e.lhs_text.casefold() or "abs" in e.rhs_text.casefold() or "|" in e.original for e in equations):
        cautions.append("Absolute-value equations require sign branches or an equivalent graph reflection analysis.")
    if any(match.id == "EQREC-033" for match in matches):
        cautions.append("The finite tangent-half-angle chart omits odd multiples of π; test those angles separately.")
    if any(match.id in {"EQREC-039", "EQREC-053"} for match in matches):
        cautions.append("Numerical graph roots are approximations; completeness requires a separate root-count or interval argument.")
    if any(match.id == "EQREC-055" for match in matches):
        cautions.append("A later subpart may use an earlier result only after that result has an accepted proof certificate.")
    if any(match.id in {"EQREC-052", "EQREC-053"} for match in matches):
        cautions.append("Nested or mixed transcendental equations may exceed the exact capabilities of the current engine.")

    workflow = _build_workflow(matches, task_type)
    return RecognitionResult(
        status="RECOGNISED" if matches else "UNCLASSIFIED",
        task_type=task_type,
        equations=equations,
        angle_variables=angle_variables,
        parameter_variables=tuple(parameter_names),
        interval_text=interval,
        angle_unit=unit,
        cognitive_level=_classify_equation_cognitive(matches, complexity_notes, task_type),
        complexity_notes=tuple(complexity_notes),
        matches=matches,
        domain_conditions=tuple(domain),
        cautions=tuple(dict.fromkeys(cautions)),
        workflow=workflow,
    )


def _classify_equation_cognitive(matches, complexity_notes, task_type) -> str:
    """Centralised display hook; deliberately describes structure, not student ability."""
    ids = {m.id for m in matches}
    if task_type == "Multi-part proof followed by equation" or "EQREC-051" in ids:
        return "TP5–TP6-style structure (engineering estimate; not an official assignment)"
    if ids & {"EQREC-030", "EQREC-031", "EQREC-039", "EQREC-040", "EQREC-041", "EQREC-046", "EQREC-052", "EQREC-053", "EQREC-054", "EQREC-055"}:
        return "TP5–TP6-style structure (engineering estimate; not an official assignment)"
    if len(ids) >= 3 or any("interval" in note.casefold() for note in complexity_notes):
        return "TP4–TP5-style structure (engineering estimate; not an official assignment)"
    if ids:
        return "TP3–TP4-style structure (engineering estimate; not an official assignment)"
    return "TP1–TP2-style structure (engineering estimate; not an official assignment)"


def recognition_catalogue_stats(skill2_path: str | Path = DEFAULT_SKILL2_PATH) -> dict[str, int]:
    titles = _load_catalogue_titles(Path(skill2_path))
    return {
        "knowledge_entries": len(titles),
        "implemented_class_routes": len(CLASS_META),
        "missing_implementations": len(set(titles) - set(CLASS_META)),
        "unlisted_routes": len(set(CLASS_META) - set(titles)),
    }


def recognition_catalogue(skill2_path: str | Path = DEFAULT_SKILL2_PATH) -> list[dict]:
    titles = _load_catalogue_titles(Path(skill2_path))
    return [
        {"id": class_id, "title": titles.get(class_id, class_id), **CLASS_META[class_id]}
        for class_id in sorted(CLASS_META)
    ]


def save_recognition_report(result: RecognitionResult, markdown_path: str | Path, json_path: str | Path | None = None) -> None:
    Path(markdown_path).write_text(result.to_markdown(), encoding="utf-8")
    if json_path is not None:
        Path(json_path).write_text(json.dumps(result.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
