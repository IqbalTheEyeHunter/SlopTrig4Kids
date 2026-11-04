"""Symbolic trigonometric identity engine for the six elementary functions."""
from __future__ import annotations

import math
import random
import re
from dataclasses import dataclass, field
from typing import Callable

import sympy as sp
from sympy.simplify.fu import fu


ALLOWED_FUNCTIONS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "cot": sp.cot,
    "sec": sp.sec,
    "csc": sp.csc,
    "sqrt": sp.sqrt,
}
TRIG_FUNCTIONS = (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc)
RECIPROCAL_DOMAIN_FUNCTIONS = {
    sp.tan: sp.cos,
    sp.sec: sp.cos,
    sp.cot: sp.sin,
    sp.csc: sp.sin,
}


class ExpressionInputError(ValueError):
    """Raised when an expression uses unsupported or malformed syntax."""


@dataclass
class ProofStep:
    title: str
    expression: sp.Expr
    note: str = ""


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


class _SafeSympyParser:
    """AST parser that accepts arithmetic and the six elementary trig functions only."""

    def __init__(self):
        self.symbols: dict[str, sp.Symbol] = {}

    def parse(self, text: str) -> sp.Expr:
        cleaned = self._normalise(text)
        if not cleaned.strip():
            raise ExpressionInputError("Please enter an expression.")
        try:
            import ast
            tree = ast.parse(cleaned, mode="eval")
            return self._visit(tree.body)
        except ExpressionInputError:
            raise
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as exc:
            raise ExpressionInputError(f"Cannot read this expression: {exc}") from exc

    @staticmethod
    def _normalise(text: str) -> str:
        # Convert the common textbook notation sin^2(x) / sin²(x) to Python-style
        # function-call notation before normalising superscript characters.
        names = r"sin|cos|tan|cot|sec|csc"
        text = re.sub(rf"\b({names})\s*(?:\^|\*\*)\s*(\d+)\s*\(([^()]*)\)",
                      lambda m: f"({m.group(1)}({m.group(3)}))**{m.group(2)}", text)
        text = re.sub(rf"\b({names})²\s*\(([^()]*)\)",
                      lambda m: f"({m.group(1)}({m.group(2)}))**2", text)
        text = re.sub(rf"\b({names})³\s*\(([^()]*)\)",
                      lambda m: f"({m.group(1)}({m.group(2)}))**3", text)
        # Permit a numeric coefficient immediately before a trig function, e.g. 2sin(x).
        text = re.sub(rf"(?<![A-Za-z0-9_])(\d+(?:\.\d+)?)\s*({names})\s*\(",
                      r"\1*\2(", text)
        replacements = {
            "π": "pi", "Π": "pi", "−": "-", "–": "-", "—": "-",
            "×": "*", "·": "*", "÷": "/", "√(": "sqrt(",
        }
        for old, new in replacements.items():
            text = text.replace(old, new)
        return text.replace("^", "**")

    def _visit(self, node):
        import ast
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
            if isinstance(node.op, ast.UAdd):
                return value
            if isinstance(node.op, ast.USub):
                return -value
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


def _rewrite_six_functions(expr: sp.Expr) -> sp.Expr:
    """Apply quotient and reciprocal definitions while retaining original-domain notes."""
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


def _float_value(expr: sp.Expr, substitutions: dict[sp.Symbol, float]) -> float:
    value = complex(sp.N(expr.subs(substitutions), 16))
    if abs(value.imag) > 1e-8:
        raise ValueError("non-real value")
    result = float(value.real)
    if not math.isfinite(result):
        raise ValueError("non-finite value")
    return result


def _find_counterexample(lhs: sp.Expr, rhs: sp.Expr, attempts: int = 80):
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
    candidates = []
    for k in range(attempts):
        point = {}
        for index, symbol in enumerate(symbols):
            if k < len(fixed):
                point[symbol] = fixed[(k + index * 3) % len(fixed)]
            else:
                point[symbol] = rng.uniform(-5.8, 5.8)
        candidates.append(point)
    for point in candidates:
        try:
            lv, rv = _float_value(lhs, point), _float_value(rhs, point)
            if not math.isclose(lv, rv, rel_tol=1e-8, abs_tol=1e-8):
                return {s.name: v for s, v in point.items()}, lv, rv
        except Exception:
            continue
    return None


def _candidate_steps(difference: sp.Expr, method: str) -> list[tuple[str, Callable[[sp.Expr], sp.Expr], str]]:
    base = [
        ("Apply quotient and reciprocal identities", _rewrite_six_functions,
         "tan = sin/cos, cot = cos/sin, sec = 1/cos and csc = 1/sin."),
        ("Expand compound angles", sp.expand_trig,
         "Use angle addition and subtraction formulas where applicable."),
        ("Apply trigonometric identities", sp.trigsimp,
         "Simplify using trigonometric relationships, including Pythagorean identities."),
        ("Apply advanced trigonometric transformations", fu,
         "Apply the Fu trigonometric transformation rules."),
        ("Combine algebraic fractions", sp.together,
         "Put rational terms over a common denominator."),
        ("Cancel common algebraic factors", sp.cancel,
         "Cancel common factors without changing the recorded original domain."),
        ("Final symbolic simplification", sp.simplify,
         "Simplify the remaining symbolic expression."),
    ]
    if method == "Angle expansion first":
        order = [1, 0, 2, 3, 4, 5, 6]
    elif method == "Fu transformations first":
        order = [3, 2, 0, 1, 4, 5, 6]
    elif method == "Algebraic reduction first":
        order = [4, 5, 0, 1, 2, 3, 6]
    else:
        order = list(range(len(base)))
    return [base[i] for i in order]


def prove_identity(lhs_text: str, rhs_text: str, method: str = "Automatic") -> ProofResult:
    lhs = parse_expression(lhs_text)
    rhs = parse_expression(rhs_text)
    domain = _domain_conditions(lhs, rhs)
    difference = sp.together(lhs - rhs)
    steps = [ProofStep("Start with the difference LHS − RHS", difference,
                       "An identity is established if this difference simplifies to zero on the original common domain.")]

    if difference == 0:
        steps.append(ProofStep("Exact symbolic cancellation", sp.S.Zero,
                               "Both sides are symbolically identical."))
        return ProofResult("PROVED", lhs, rhs, steps, domain,
                           "The two expressions are symbolically identical on their common domain.")

    current = difference
    seen = {sp.srepr(current)}
    for title, transform, note in _candidate_steps(difference, method):
        try:
            candidate = transform(current)
            if candidate is None:
                continue
            candidate = sp.factor(candidate) if title == "Cancel common algebraic factors" else candidate
            key = sp.srepr(candidate)
            if key not in seen and candidate != current:
                steps.append(ProofStep(title, candidate, note))
                current = candidate
                seen.add(key)
            if candidate == 0 or sp.simplify(candidate) == 0:
                if candidate != 0:
                    steps.append(ProofStep("Verify the final zero expression", sp.S.Zero,
                                           "The remaining expression simplifies exactly to zero."))
                return ProofResult("PROVED", lhs, rhs, steps, domain,
                                   "A symbolic derivation reduced LHS − RHS exactly to zero.")
        except Exception:
            # A failed strategy must not invalidate other independent strategies.
            continue

    # Run independent simplification routes from the original difference. A route
    # can succeed even when an earlier heuristic made the expression less simple.
    independent_routes = [
        ("Direct trigonometric simplification", lambda e: sp.trigsimp(e)),
        ("Fu trigonometric algorithm", fu),
        ("Expand angles, then simplify", lambda e: sp.trigsimp(sp.expand_trig(e))),
        ("Rewrite quotient functions, then simplify", lambda e: sp.trigsimp(_rewrite_six_functions(e))),
        ("Simplify a common-denominator form", lambda e: sp.simplify(sp.together(e))),
    ]
    for title, transform in independent_routes:
        try:
            candidate = transform(difference)
            if candidate == 0 or sp.simplify(candidate) == 0:
                if not any(step.expression == candidate for step in steps):
                    steps.append(ProofStep(title, candidate,
                                           "An independent symbolic route reduced the difference to zero."))
                return ProofResult("PROVED", lhs, rhs, steps, domain,
                                   "A symbolic derivation reduced LHS − RHS exactly to zero.")
        except Exception:
            continue

    counterexample = _find_counterexample(lhs, rhs)
    if counterexample is not None:
        point, lv, rv = counterexample
        return ProofResult("DISPROVED", lhs, rhs, steps, domain,
                           "A valid numerical counterexample was found. The proposed identity is false.",
                           point, lv, rv)

    return ProofResult("INCONCLUSIVE", lhs, rhs, steps, domain,
                       "The current symbolic strategies did not prove the identity, and no counterexample was found. This is not a proof that the claim is false.")


def simplify_expression(text: str) -> tuple[sp.Expr, list[ProofStep], list[str]]:
    expr = parse_expression(text)
    domain = _domain_conditions(expr)
    steps = [ProofStep("Original expression", expr)]
    current = expr
    for title, transform, note in _candidate_steps(expr, "Automatic"):
        try:
            candidate = transform(current)
            if candidate != current:
                steps.append(ProofStep(title, candidate, note))
                current = candidate
        except Exception:
            continue
    return current, steps, domain
