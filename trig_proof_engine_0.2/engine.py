"""Symbolic trigonometric identity engine (v0.2.0).

The engine is deliberately limited to the six elementary trigonometric
functions.  It records symbolic transformations, links recognised steps to
identity IDs in the bundled SKILL.md, and preserves the original domain ledger.
"""
from __future__ import annotations

import ast
import json
import math
import random
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Iterable

import sympy as sp
from sympy.simplify.fu import fu

ENGINE_VERSION = "0.2.0"
DEFAULT_SKILL_PATH = Path(__file__).resolve().parent / "knowledge" / "SKILL.md"

ALLOWED_FUNCTIONS = {
    "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
    "cot": sp.cot, "sec": sp.sec, "csc": sp.csc,
    "sqrt": sp.sqrt,
}
TRIG_FUNCTIONS = (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc)
RECIPROCAL_DOMAIN_FUNCTIONS = {
    sp.tan: sp.cos, sp.sec: sp.cos,
    sp.cot: sp.sin, sp.csc: sp.sin,
}


class ExpressionInputError(ValueError):
    """Raised when an expression uses unsupported or malformed syntax."""


@dataclass
class ProofStep:
    title: str
    expression: sp.Expr
    note: str = ""
    rule_ids: tuple[str, ...] = ()
    side: str = "Difference"
    previous_expression: sp.Expr | None = None


@dataclass
class ProofRoute:
    name: str
    steps: list[ProofStep] = field(default_factory=list)
    summary: str = ""
    rule_ids: tuple[str, ...] = ()


@dataclass
class ProofResult:
    status: str
    lhs: sp.Expr
    rhs: sp.Expr
    steps: list[ProofStep] = field(default_factory=list)
    domain_conditions: list[str] = field(default_factory=list)
    message: str = ""
    counterexample: dict[str, float] | None = None
    lhs_value: float | None = None
    rhs_value: float | None = None
    selected_route: str = ""
    alternative_routes: list[ProofRoute] = field(default_factory=list)
    rule_ids: tuple[str, ...] = ()

    def to_certificate(self) -> dict:
        """Return a portable JSON certificate with each step's symbolic check."""
        def step_record(step: ProofStep) -> dict:
            valid = None
            if step.previous_expression is not None:
                valid = _symbolically_equivalent(step.previous_expression, step.expression)
            return {
                "title": step.title,
                "side": step.side,
                "from": None if step.previous_expression is None else sp.sstr(step.previous_expression),
                "to": sp.sstr(step.expression),
                "justification": step.note,
                "identity_ids": list(step.rule_ids),
                "symbolic_equivalence_check": valid,
            }

        return {
            "schema": "trigonometric-proof-certificate-v1",
            "engine_version": ENGINE_VERSION,
            "scope": ["sin", "cos", "tan", "cot", "sec", "csc"],
            "claim": {"lhs": sp.sstr(self.lhs), "rhs": sp.sstr(self.rhs)},
            "status": self.status,
            "selected_route": self.selected_route,
            "domain_conditions": list(self.domain_conditions),
            "identity_ids": list(self.rule_ids),
            "steps": [step_record(step) for step in self.steps],
            "alternative_routes": [
                {
                    "name": route.name,
                    "summary": route.summary,
                    "identity_ids": list(route.rule_ids),
                    "steps": [step_record(step) for step in route.steps],
                }
                for route in self.alternative_routes
            ],
            "counterexample": self.counterexample,
            "counterexample_values": {"lhs": self.lhs_value, "rhs": self.rhs_value},
            "certificate_note": (
                "This is a symbolic transformation record, not a proof object for an independently "
                "verified theorem prover. Original-domain restrictions are retained throughout."
            ),
        }

    def to_markdown(self) -> str:
        lines = [
            "# Trigonometric Proof Report",
            "",
            f"- **Engine version:** {ENGINE_VERSION}",
            f"- **Status:** {self.status}",
            f"- **Selected route:** {self.selected_route or 'Not established'}",
            "",
            "## Claim",
            "",
            f"\\[ {sp.latex(self.lhs)} = {sp.latex(self.rhs)} \\]",
            "",
            "## Original common-domain conditions",
            "",
        ]
        if self.domain_conditions:
            lines.extend(f"- `{condition}`" for condition in self.domain_conditions)
        else:
            lines.append("- No additional restrictions detected.")
        lines += ["", "## Proof / analysis steps", ""]
        for index, step in enumerate(self.steps, 1):
            ids = f" (Identity IDs: {', '.join(step.rule_ids)})" if step.rule_ids else ""
            lines.append(f"{index}. **{step.title}** — {step.side}{ids}")
            if step.previous_expression is not None:
                lines.append(f"   - From: `{sp.sstr(step.previous_expression)}`")
            lines.append(f"   - To: `{sp.sstr(step.expression)}`")
            if step.note:
                lines.append(f"   - Reason: {step.note}")
        if self.alternative_routes:
            lines += ["", "## Alternative proof routes", ""]
            for route in self.alternative_routes:
                refs = f"; IDs: {', '.join(route.rule_ids)}" if route.rule_ids else ""
                lines.append(f"- **{route.name}:** {route.summary}{refs}")
        if self.counterexample is not None:
            lines += ["", "## Counterexample", ""]
            lines.append(", ".join(f"{name} = {value:.12g}" for name, value in self.counterexample.items()))
            lines.append(f"- LHS ≈ {self.lhs_value:.12g}; RHS ≈ {self.rhs_value:.12g}")
        lines += ["", "## Conclusion", "", self.message, ""]
        lines.append("> Numerical sampling is used only to find counterexamples; it is never used to certify an identity.")
        return "\n".join(lines)


class _SafeSympyParser:
    """AST parser that accepts arithmetic and the six elementary trig functions only."""

    def __init__(self):
        self.symbols: dict[str, sp.Symbol] = {}

    def parse(self, text: str) -> sp.Expr:
        cleaned = self._normalise(text)
        if not cleaned.strip():
            raise ExpressionInputError("Please enter an expression.")
        try:
            tree = ast.parse(cleaned, mode="eval")
            return self._visit(tree.body)
        except ExpressionInputError:
            raise
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as exc:
            raise ExpressionInputError(f"Cannot read this expression: {exc}") from exc

    @staticmethod
    def _normalise(text: str) -> str:
        names = r"sin|cos|tan|cot|sec|csc"
        text = re.sub(
            rf"\b({names})\s*(?:\^|\*\*)\s*(\d+)\s*\(([^()]*)\)",
            lambda m: f"({m.group(1)}({m.group(3)}))**{m.group(2)}", text,
        )
        for power, superscript in ((2, "²"), (3, "³"), (4, "⁴")):
            text = re.sub(
                rf"\b({names}){superscript}\s*\(([^()]*)\)",
                lambda m, p=power: f"({m.group(1)}({m.group(2)}))**{p}", text,
            )
        text = re.sub(rf"(?<![A-Za-z0-9_])(\d+(?:\.\d+)?)\s*({names})\s*\(", r"\1*\2(", text)
        replacements = {
            "π": "pi", "Π": "pi", "−": "-", "–": "-", "—": "-",
            "×": "*", "·": "*", "÷": "/", "√(": "sqrt(",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text.replace("^", "**")

    def _visit(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
                raise ExpressionInputError("Only real numeric constants are supported.")
            return sp.Integer(node.value) if isinstance(node.value, int) else sp.Float(node.value)
        if isinstance(node, ast.Name):
            if node.id == "pi":
                return sp.pi
            if node.id in ALLOWED_FUNCTIONS:
                raise ExpressionInputError(f"Use {node.id}(...) with an argument.")
            if node.id in {"e", "E", "I", "oo", "zoo", "nan"}:
                raise ExpressionInputError(f"The constant '{node.id}' is outside this application's input scope.")
            if not node.id.isidentifier() or node.id.startswith("__"):
                raise ExpressionInputError("Invalid variable name.")
            if node.id not in self.symbols:
                self.symbols[node.id] = sp.Symbol(node.id, real=True)
            return self.symbols[node.id]
        if isinstance(node, ast.UnaryOp):
            value = self._visit(node.operand)
            if isinstance(node.op, ast.UAdd): return value
            if isinstance(node.op, ast.USub): return -value
            raise ExpressionInputError("Only unary + and - are supported.")
        if isinstance(node, ast.BinOp):
            left, right = self._visit(node.left), self._visit(node.right)
            if isinstance(node.op, ast.Add): return left + right
            if isinstance(node.op, ast.Sub): return left - right
            if isinstance(node.op, ast.Mult): return left * right
            if isinstance(node.op, ast.Div): return left / right
            if isinstance(node.op, ast.Pow):
                if right.is_number and abs(float(right)) > 1000:
                    raise ExpressionInputError("Exponent is too large for this first version.")
                return left ** right
            raise ExpressionInputError("Supported operators are +, -, *, / and **.")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ExpressionInputError("Only direct calls to the six trig functions and sqrt are supported.")
            name = node.func.id
            if name not in ALLOWED_FUNCTIONS:
                raise ExpressionInputError(f"Unsupported function '{name}'. Use sin, cos, tan, cot, sec, csc or sqrt.")
            if len(node.args) != 1 or node.keywords:
                raise ExpressionInputError(f"{name}() requires exactly one argument.")
            return ALLOWED_FUNCTIONS[name](self._visit(node.args[0]))
        raise ExpressionInputError(f"Unsupported syntax: {type(node).__name__}.")


def parse_expression(text: str) -> sp.Expr:
    return _SafeSympyParser().parse(text)


def load_rule_catalogue(skill_path: str | Path = DEFAULT_SKILL_PATH) -> list[dict[str, str]]:
    """Read indexed identity rows directly from the bundled Markdown specification."""
    path = Path(skill_path)
    if not path.exists():
        return []
    records: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        fields = [field.strip() for field in line.strip().strip("|").split("|")]
        if len(fields) < 3 or not re.fullmatch(r"[A-Z]\d{2}", fields[0]):
            continue
        # Some skill rows contain inline code ticks inside the formula cell.
        identity = fields[1].strip().strip("`").replace("`", "")
        conditions = fields[2].strip().strip("`").replace("`", "")
        records.append({"id": fields[0], "identity": identity, "conditions": conditions})
    return records


def _rewrite_six_functions(expr: sp.Expr) -> sp.Expr:
    replacements = {
        sp.tan: lambda a: sp.sin(a) / sp.cos(a),
        sp.cot: lambda a: sp.cos(a) / sp.sin(a),
        sp.sec: lambda a: 1 / sp.cos(a),
        sp.csc: lambda a: 1 / sp.sin(a),
    }
    out = expr
    for function, replacement in replacements.items():
        out = out.replace(lambda node, f=function: getattr(node, "func", None) == f,
                          lambda node, r=replacement: r(node.args[0]))
    return out


def _domain_conditions(*expressions: sp.Expr) -> list[str]:
    """Collect visible original-domain restrictions without solving intervals."""
    nonzero: dict[str, str] = {}
    nonnegative: dict[str, str] = {}
    for expr in expressions:
        for node in sp.preorder_traversal(expr):
            if getattr(node, "func", None) in RECIPROCAL_DOMAIN_FUNCTIONS:
                base = RECIPROCAL_DOMAIN_FUNCTIONS[node.func](node.args[0])
                nonzero[sp.srepr(base)] = sp.sstr(base)
            if isinstance(node, sp.Pow) and node.exp.is_negative:
                nonzero[sp.srepr(node.base)] = sp.sstr(node.base)
            if node.func == sp.sqrt:
                radicand = node.args[0]
                nonnegative[sp.srepr(radicand)] = sp.sstr(radicand)
    conditions = [f"{value} ≠ 0" for value in nonzero.values()]
    conditions += [f"{value} ≥ 0 (real square root)" for value in nonnegative.values()]
    return sorted(conditions, key=str.casefold)


def _symbolically_equivalent(left: sp.Expr, right: sp.Expr) -> bool:
    """Try exact symbolic equivalence only; never use floating-point sampling here."""
    difference = sp.together(left - right)
    if difference == 0:
        return True
    strategies = (
        sp.trigsimp,
        lambda e: sp.trigsimp(sp.expand_trig(e)),
        fu,
        sp.simplify,
    )
    for transform in strategies:
        try:
            value = transform(difference)
            if value == 0 or value.is_zero is True:
                return True
        except Exception:
            continue
    return False


def _float_value(expr: sp.Expr, substitutions: dict[sp.Symbol, float]) -> float:
    value = complex(sp.N(expr.subs(substitutions), 16))
    if abs(value.imag) > 1e-8:
        raise ValueError("non-real value")
    result = float(value.real)
    if not math.isfinite(result):
        raise ValueError("non-finite value")
    return result


def _find_counterexample(lhs: sp.Expr, rhs: sp.Expr, attempts: int = 120):
    symbols = sorted(lhs.free_symbols | rhs.free_symbols, key=lambda s: s.name)
    if not symbols:
        try:
            lv, rv = _float_value(lhs, {}), _float_value(rhs, {})
            if not math.isclose(lv, rv, rel_tol=1e-9, abs_tol=1e-9):
                return {}, lv, rv
        except Exception:
            pass
        return None
    rng = random.Random(20261104)
    fixed = [-2.7, -2.1, -1.3, -0.8, -0.37, 0.23, 0.61, 1.1, 1.7, 2.4, 3.2]
    for k in range(attempts):
        point = {
            symbol: fixed[(k + index * 3) % len(fixed)] if k < len(fixed) else rng.uniform(-5.8, 5.8)
            for index, symbol in enumerate(symbols)
        }
        try:
            lv, rv = _float_value(lhs, point), _float_value(rhs, point)
            if not math.isclose(lv, rv, rel_tol=1e-8, abs_tol=1e-8):
                return {s.name: v for s, v in point.items()}, lv, rv
        except Exception:
            continue
    return None


def _rule_ids_for_change(before: sp.Expr, after: sp.Expr, title: str) -> tuple[str, ...]:
    """Attach conservative SKILL.md rule references to recognisable transformations."""
    found: list[str] = []
    if "quotient and reciprocal" in title.casefold():
        pairs = ((sp.tan, "F01"), (sp.cot, "F02"), (sp.sec, "F03"), (sp.csc, "F04"))
        for function, rule_id in pairs:
            if before.has(function) and not after.has(function):
                found.append(rule_id)
    if "compound angle" in title.casefold() or "expand angle" in title.casefold():
        for node in before.atoms(*TRIG_FUNCTIONS):
            arg = node.args[0]
            if isinstance(arg, sp.Add):
                if node.func == sp.sin:
                    found.append("A02" if any(term.could_extract_minus_sign() for term in arg.args) else "A01")
                elif node.func == sp.cos:
                    found.append("A04" if any(term.could_extract_minus_sign() for term in arg.args) else "A03")
            elif (sp.simplify(arg / 2).is_integer is True
                  or (arg.is_Mul and sp.Integer(2) in arg.args)):
                if node.func == sp.sin: found.append("D01")
                elif node.func == sp.cos: found.append("D02")
    if before.has(sp.sec) and before.has(sp.tan):
        expanded_pair = sp.expand(before)
        if isinstance(before, sp.Mul) and _symbolically_equivalent(before, sp.Integer(1)):
            found.append("F16")
        if expanded_pair.has(sp.sec) and expanded_pair.has(sp.tan):
            if _symbolically_equivalent(before, sp.sec(before.atoms(sp.sec).pop().args[0])**2):
                found.append("F09")
    if before.has(sp.csc) and before.has(sp.cot) and isinstance(before, sp.Mul):
        if _symbolically_equivalent(before, sp.Integer(1)):
            found.append("F17")
    if "trigonometric identit" in title.casefold() or "fu" in title.casefold() or "simplif" in title.casefold():
        expanded = sp.expand(before)
        if after == 0 or after == 1 or after == -1:
            # Recognise only an actual squared sine/cosine pair at the same angle.
            sin_args = {n.args[0] for n in expanded.atoms(sp.sin)}
            cos_args = {n.args[0] for n in expanded.atoms(sp.cos)}
            for angle in sin_args & cos_args:
                if expanded.has(sp.sin(angle)**2) and expanded.has(sp.cos(angle)**2):
                    found.append("F08")
    if "cancel" in title.casefold() or "algebraic" in title.casefold():
        if before.has(sp.sec) and before.has(sp.tan): found.append("F16")
        if before.has(sp.csc) and before.has(sp.cot): found.append("F17")
    # Keep only unique references from the current specification.
    valid_ids = {item["id"] for item in load_rule_catalogue()}
    return tuple(dict.fromkeys(item for item in found if item in valid_ids))



def _direct_rule_ids(lhs: sp.Expr, rhs: sp.Expr) -> tuple[str, ...]:
    """Recognise a small set of exact catalogue identities in the original claim."""
    x = sp.Wild("angle")
    pairs = (
        (1 + sp.tan(x)**2, sp.sec(x)**2, "F09"),
        (1 + sp.cot(x)**2, sp.csc(x)**2, "F10"),
        (sp.sec(x)**2 - sp.tan(x)**2, sp.Integer(1), "F11"),
        (sp.csc(x)**2 - sp.cot(x)**2, sp.Integer(1), "F12"),
        ((sp.sec(x) - sp.tan(x)) * (sp.sec(x) + sp.tan(x)), sp.Integer(1), "F16"),
        ((sp.csc(x) - sp.cot(x)) * (sp.csc(x) + sp.cot(x)), sp.Integer(1), "F17"),
    )
    found = []
    for left_pattern, right_pattern, rule_id in pairs:
        for first, second in ((lhs, rhs), (rhs, lhs)):
            match = first.match(left_pattern)
            if match is not None and second == right_pattern.xreplace(match):
                found.append(rule_id)
    # The F08 pattern is written separately to avoid a syntactically redundant 1.
    pythagorean = sp.sin(x)**2 + sp.cos(x)**2
    for first, second in ((lhs, rhs), (rhs, lhs)):
        match = first.match(pythagorean)
        if match is not None and second == sp.Integer(1):
            found.append("F08")
    valid_ids = {item["id"] for item in load_rule_catalogue()}
    return tuple(dict.fromkeys(item for item in found if item in valid_ids))

def _candidate_steps(method: str = "Automatic") -> list[tuple[str, Callable[[sp.Expr], sp.Expr], str]]:
    base = [
        ("Apply quotient and reciprocal identities", _rewrite_six_functions,
         "Use F01–F04 to express tangent, cotangent, secant and cosecant using sine and cosine."),
        ("Expand compound angles", sp.expand_trig,
         "Use angle addition, subtraction and multiple-angle identities where applicable."),
        ("Apply trigonometric identities", sp.trigsimp,
         "Simplify using the six-function identity catalogue, especially Pythagorean relationships."),
        ("Apply Fu trigonometric transformations", fu,
         "Apply an independent set of trigonometric transformation rules."),
        ("Combine algebraic fractions", sp.together,
         "Put rational terms over a common denominator."),
        ("Cancel common algebraic factors", sp.cancel,
         "Cancel common factors while retaining the original domain restrictions."),
        ("Factor algebraic expressions", sp.factor,
         "Factor the resulting algebraic expression."),
        ("Final symbolic simplification", sp.simplify,
         "Apply exact symbolic simplification."),
    ]
    if method == "Angle expansion first":
        order = [1, 0, 2, 3, 4, 5, 6, 7]
    elif method == "Fu transformations first":
        order = [3, 2, 0, 1, 4, 5, 6, 7]
    elif method == "Algebraic reduction first":
        order = [4, 5, 6, 0, 1, 2, 3, 7]
    else:
        order = list(range(len(base)))
    return [base[index] for index in order]


def _make_step(title: str, before: sp.Expr | None, after: sp.Expr, note: str,
               side: str, rule_ids: Iterable[str] = ()) -> ProofStep:
    return ProofStep(title, after, note, tuple(rule_ids), side, before)


def _simplify_side(source: sp.Expr, target: sp.Expr, side: str, order_method: str = "Automatic") -> ProofRoute | None:
    steps = [ProofStep(f"Start with the {side}", source, "Original expression from the claim.", (), side, None)]
    current = source
    seen = {sp.srepr(current)}
    for title, transform, note in _candidate_steps(order_method):
        try:
            candidate = transform(current)
            if candidate is None or candidate == current:
                continue
            if not _symbolically_equivalent(current, candidate):
                continue
            key = sp.srepr(candidate)
            if key in seen:
                continue
            ids = _rule_ids_for_change(current, candidate, title)
            steps.append(_make_step(title, current, candidate, note, side, ids))
            current = candidate
            seen.add(key)
            if _symbolically_equivalent(current, target):
                direct_ids = _direct_rule_ids(source, target)
                steps.append(_make_step("Match the other side", current, target,
                                        "The transformed expression is symbolically equivalent to the target side.", side, direct_ids))
                route_ids = tuple(dict.fromkeys(rule for step in steps for rule in step.rule_ids))
                return ProofRoute(f"{side} to other side", steps,
                                  f"The {side.lower()} was transformed into the other side.", route_ids)
        except Exception:
            continue
    if _symbolically_equivalent(current, target):
        direct_ids = _direct_rule_ids(source, target)
        steps.append(_make_step("Match the other side", current, target,
                                "The transformed expression is symbolically equivalent to the target side.", side, direct_ids))
        route_ids = tuple(dict.fromkeys(rule for step in steps for rule in step.rule_ids))
        return ProofRoute(f"{side} to other side", steps, "The transformed side matches its target.", route_ids)
    return None


def _common_form_route(lhs: sp.Expr, rhs: sp.Expr, order_method: str = "Automatic") -> ProofRoute | None:
    steps: list[ProofStep] = [
        ProofStep("Start with the LHS", lhs, "First expression in the claim.", (), "LHS", None),
        ProofStep("Start with the RHS", rhs, "Second expression in the claim.", (), "RHS", None),
    ]
    final: dict[str, sp.Expr] = {"LHS": lhs, "RHS": rhs}
    for side in ("LHS", "RHS"):
        current = final[side]
        seen = {sp.srepr(current)}
        for title, transform, note in _candidate_steps(order_method):
            try:
                candidate = transform(current)
                if candidate is None or candidate == current or not _symbolically_equivalent(current, candidate):
                    continue
                key = sp.srepr(candidate)
                if key in seen:
                    continue
                ids = _rule_ids_for_change(current, candidate, title)
                steps.append(_make_step(title, current, candidate, note, side, ids))
                current = candidate
                seen.add(key)
            except Exception:
                continue
        final[side] = current
    if _symbolically_equivalent(final["LHS"], final["RHS"]):
        direct_ids = _direct_rule_ids(lhs, rhs)
        steps.append(_make_step("Establish a common form", final["LHS"], final["RHS"],
                                "Both sides reduce to symbolically equivalent expressions.", "Both sides", direct_ids))
        route_ids = tuple(dict.fromkeys(rule for step in steps for rule in step.rule_ids))
        return ProofRoute("Both sides to common form", steps,
                          "Both expressions reduce to the same symbolic form.", route_ids)
    return None


def _difference_route(lhs: sp.Expr, rhs: sp.Expr, order_method: str = "Automatic") -> ProofRoute | None:
    difference = sp.together(lhs - rhs)
    steps = [ProofStep("Form LHS − RHS", difference,
                       "An identity is established when the difference is exactly zero on the original common domain.",
                       (), "Difference", None)]
    if difference == 0:
        return ProofRoute("Difference method", steps, "The initial symbolic difference is zero.", ())
    current = difference
    seen = {sp.srepr(current)}
    for title, transform, note in _candidate_steps(order_method):
        try:
            candidate = transform(current)
            if candidate is None or candidate == current or not _symbolically_equivalent(current, candidate):
                continue
            key = sp.srepr(candidate)
            if key in seen:
                continue
            ids = _rule_ids_for_change(current, candidate, title)
            steps.append(_make_step(title, current, candidate, note, "Difference", ids))
            current = candidate
            seen.add(key)
            if current == 0 or current.is_zero is True:
                return ProofRoute("Difference method", steps,
                                  "The symbolic difference reduces exactly to zero.",
                                  tuple(dict.fromkeys(rule for step in steps for rule in step.rule_ids)))
        except Exception:
            continue
    # Independent routes are run from the original difference, not from a potentially
    # unhelpful intermediate expression.
    independent = [
        ("Direct trigonometric simplification", sp.trigsimp,
         "An independent trigonometric simplification route."),
        ("Fu trigonometric algorithm", fu, "An independent Fu transformation route."),
        ("Expand angles, then simplify", lambda e: sp.trigsimp(sp.expand_trig(e)),
         "Apply compound-angle identities before simplifying."),
        ("Rewrite quotient functions, then simplify", lambda e: sp.trigsimp(_rewrite_six_functions(e)),
         "Apply quotient and reciprocal definitions before simplifying."),
        ("Simplify a common-denominator form", lambda e: sp.simplify(sp.together(e)),
         "Combine fractions before exact simplification."),
    ]
    for title, transform, note in independent:
        try:
            candidate = transform(difference)
            if _symbolically_equivalent(difference, candidate) and (candidate == 0 or candidate.is_zero is True):
                ids = _rule_ids_for_change(difference, candidate, title)
                steps.append(_make_step(title, difference, candidate, note, "Difference", ids))
                return ProofRoute("Difference method", steps,
                                  "An independent symbolic route reduces the difference exactly to zero.",
                                  tuple(dict.fromkeys(rule for step in steps for rule in step.rule_ids)))
        except Exception:
            continue
    return None


def prove_identity(lhs_text: str, rhs_text: str, method: str = "Automatic") -> ProofResult:
    lhs, rhs = parse_expression(lhs_text), parse_expression(rhs_text)
    domain = _domain_conditions(lhs, rhs)
    order_method = method if method in {"Angle expansion first", "Fu transformations first", "Algebraic reduction first"} else "Automatic"
    route_candidates: list[ProofRoute] = []

    if method == "Automatic":
        for route in (
            _simplify_side(lhs, rhs, "LHS"),
            _simplify_side(rhs, lhs, "RHS"),
            _common_form_route(lhs, rhs),
            _difference_route(lhs, rhs),
        ):
            if route is not None:
                route_candidates.append(route)
    elif method == "LHS to RHS":
        route = _simplify_side(lhs, rhs, "LHS", order_method)
        if route: route_candidates.append(route)
    elif method == "RHS to LHS":
        route = _simplify_side(rhs, lhs, "RHS", order_method)
        if route: route_candidates.append(route)
    elif method == "Both sides to common form":
        route = _common_form_route(lhs, rhs, order_method)
        if route: route_candidates.append(route)
    elif method == "Difference method":
        route = _difference_route(lhs, rhs, order_method)
        if route: route_candidates.append(route)
    elif method in {"Angle expansion first", "Fu transformations first", "Algebraic reduction first"}:
        route = _difference_route(lhs, rhs, order_method)
        if route: route_candidates.append(route)
    else:
        raise ValueError(f"Unknown proof strategy: {method}")

    if route_candidates:
        priority = {"LHS to other side": 0, "RHS to other side": 1,
                    "Both sides to common form": 2, "Difference method": 3}
        route_candidates.sort(key=lambda route: (priority.get(route.name, 9), len(route.steps)))
        selected = route_candidates[0]
        alternatives = route_candidates[1:]
        return ProofResult(
            "PROVED", lhs, rhs, selected.steps, domain,
            "A symbolic transformation route established equality on the original common domain.",
            selected_route=selected.name, alternative_routes=alternatives, rule_ids=selected.rule_ids,
        )

    # Even when a specific strategy is selected, counterexample checking remains a
    # diagnostic. It can disprove a claim but can never certify it.
    counterexample = _find_counterexample(lhs, rhs)
    if counterexample is not None:
        point, lv, rv = counterexample
        return ProofResult("DISPROVED", lhs, rhs, [], domain,
                           "A valid numerical counterexample was found. The proposed identity is false.",
                           point, lv, rv, selected_route=method)
    return ProofResult("INCONCLUSIVE", lhs, rhs, [], domain,
                       "The selected symbolic proof strategy did not establish the identity, and no counterexample was found. This is not a proof that the claim is false.",
                       selected_route=method)


def simplify_expression(text: str) -> tuple[sp.Expr, list[ProofStep], list[str]]:
    expr = parse_expression(text)
    domain = _domain_conditions(expr)
    steps = [ProofStep("Original expression", expr, side="Expression")]
    current = expr
    seen = {sp.srepr(current)}
    for title, transform, note in _candidate_steps("Automatic"):
        try:
            candidate = transform(current)
            if candidate != current and _symbolically_equivalent(current, candidate):
                ids = _rule_ids_for_change(current, candidate, title)
                steps.append(_make_step(title, current, candidate, note, "Expression", ids))
                current = candidate
                if sp.srepr(current) in seen:
                    break
                seen.add(sp.srepr(current))
        except Exception:
            continue
    return current, steps, domain
