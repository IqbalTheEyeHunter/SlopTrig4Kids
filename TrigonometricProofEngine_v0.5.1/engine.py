"""Symbolic trigonometric identity engine (v0.5.1).

The proof engine is deliberately limited to the six elementary trigonometric
functions, arithmetic, real square roots and absolute values. It records symbolic
transformations, links recognised steps to identity IDs in SKILL.md, and preserves
the original domain ledger. Structural equation recognition is implemented in
recognition.py and remains separate from proof certification.
"""
from __future__ import annotations

import ast
import copy
import json
import math
import random
import re
from functools import lru_cache
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Iterable

import sympy as sp
from sympy.simplify.fu import fu

from geometry import (
    GEOMETRIC_CERTIFICATE_SCHEMA,
    build_f08_geometric_certificate,
    match_f08_claim,
    verify_geometric_certificate,
)

ENGINE_VERSION = "0.5.1"
DEFAULT_SKILL_PATH = Path(__file__).resolve().parent / "knowledge" / "SKILL.md"

ALLOWED_FUNCTIONS = {
    "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
    "cot": sp.cot, "sec": sp.sec, "csc": sp.csc,
    "sqrt": sp.sqrt, "abs": sp.Abs,
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
    theorem_ref: str = ""
    domain_conditions: tuple[str, ...] = ()
    substitution: tuple[tuple[str, str], ...] = ()


@dataclass
class ProofRoute:
    name: str
    steps: list[ProofStep] = field(default_factory=list)
    summary: str = ""
    rule_ids: tuple[str, ...] = ()
    used_theorems: tuple[str, ...] = ()
    domain_conditions: tuple[str, ...] = ()


@dataclass(frozen=True)
class TheoremPremise:
    """A previously established identity that may be used bidirectionally."""

    name: str
    lhs: sp.Expr
    rhs: sp.Expr
    source: str = "User supplied"
    domain_conditions: tuple[str, ...] = ()
    proof_certificate: dict | None = None
    identity_id: str = ""


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
    used_theorems: list[dict] = field(default_factory=list)
    certificate_override: dict | None = None

    def to_certificate(self) -> dict:
        """Return a portable certificate; GEO certificates are independently replayable."""
        if self.certificate_override is not None:
            return copy.deepcopy(self.certificate_override)
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
                "theorem_reference": step.theorem_ref or None,
                "domain_conditions": list(step.domain_conditions),
                "variable_substitution": {name: value for name, value in step.substitution},
                "symbolic_equivalence_check": valid,
            }

        return {
            "schema": "trigonometric-proof-certificate-v4",
            "engine_version": ENGINE_VERSION,
            "dependency_policy": "audited-catalogue-replayed-v4-and-v0.5.1-geo-certificates",
            "catalogue_dependency_manifest": {k: list(v) for k, v in AUDITED_DEPENDENCIES.items()},
            "dependency_provenance": _dependency_provenance(self.rule_ids),
            "trusted_foundations": {"F01-F04": "quotient/reciprocal definitions", "F08": "replayed G01 → G03 → G04 geometric certificate; not an unexplained root"},
            "scope": ["sin", "cos", "tan", "cot", "sec", "csc"],
            "claim": {"lhs": sp.sstr(self.lhs), "rhs": sp.sstr(self.rhs)},
            "status": self.status,
            "selected_route": self.selected_route,
            "domain_conditions": list(self.domain_conditions),
            "identity_ids": list(self.rule_ids),
            "used_theorems": self.used_theorems,
            "steps": [step_record(step) for step in self.steps],
            "alternative_routes": [
                {
                    "name": route.name,
                    "summary": route.summary,
                    "identity_ids": list(route.rule_ids),
                    "used_theorems": list(route.used_theorems),
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
        if self.certificate_override is not None:
            lines += [
                "", "## Independent geometric proof chain", "",
                "1. **G01 — Pythagorean theorem by dissection.** Four congruent right triangles tile a square of side `a+b`; the central square has side `c`. Exact area additivity gives `(a+b)^2 = 4(ab/2)+c^2`, hence `a^2+b^2=c^2`.",
                "2. **G03 — Cartesian squared distance.** Orthogonal projections of `P=(u,v)` have lengths `|u|` and `|v|`. G01 gives `OP^2=u^2+v^2`, including negative coordinates and axis cases.",
                f"3. **G04 — Unit-circle substitution.** For arbitrary real angle `θ={sp.sstr(self.certificate_override['angle_expression'])}`, construct `P=(cos θ,sin θ)` with `OP=1`. G03 gives `cos^2 θ+sin^2 θ=1`.",
                "4. **Goal matching.** The requested LHS−RHS is the exact non-trigonometric multiplier recorded in the certificate times the G04 relation. No F08/F09/F10 catalogue theorem is used as a premise.",
                "",
                "### Explicit trusted foundations",
                "- `AX.REAL`: ordered real arithmetic and real-valued angle expressions.",
                "- `AX.EUCLID`: Euclidean incidence, perpendicular projections and congruence.",
                "- `AX.AREA`: area additivity for the dissection.",
                "- `D.UNIT`: the unit-circle point has signed coordinates `(cos θ,sin θ)` and radius one.",
                "",
                "The certificate checker replays the fixed construction schema and exact algebraic obligations. This is a checked proof relative to these explicitly declared foundations, not a set-theoretic formalisation of all Euclidean geometry.",
            ]
        elif self.rule_ids:
            identity_count = sum(bool(step.theorem_ref) for step in self.steps)
            lines += [
                "", "## Derivation chain", "",
                f"- **Identity sequence:** {' → '.join(self.rule_ids)}",
                f"- **Identity applications:** {identity_count}",
                "- Each identity is applied as a separate, recorded substitution below.",
            ]
        if self.certificate_override is None:
            lines += ["", "## Proof / analysis steps", ""]
            for index, step in enumerate(self.steps, 1):
                ids = f" (Identity IDs: {', '.join(step.rule_ids)})" if step.rule_ids else ""
                lines.append(f"{index}. **{step.title}** — {step.side}{ids}")
                if step.previous_expression is not None:
                    lines.append(f"   - From: `{sp.sstr(step.previous_expression)}`")
                lines.append(f"   - To: `{sp.sstr(step.expression)}`")
                if step.note:
                    lines.append(f"   - Reason: {step.note}")
                if step.theorem_ref:
                    lines.append(f"   - Previously established result: **{step.theorem_ref}**")
                if step.substitution:
                    mapping = ", ".join(f"{name} → {value}" for name, value in step.substitution)
                    lines.append(f"   - Variable substitution: {mapping}")
                if step.domain_conditions:
                    lines.append(f"   - Conditions for this use: {', '.join(step.domain_conditions)}")
        else:
            lines += [
                "", "## Certificate replay", "",
                f"- **Schema:** `{self.certificate_override['schema']}`",
                f"- **Route:** `{self.certificate_override['selected_route']}`",
                f"- **Certificate digest:** `{self.certificate_override['certificate_digest']}`",
                "- **Replay status:** VERIFIED",
                "- **Trigonometric identity premises:** none",
            ]
        if self.alternative_routes:
            lines += ["", "## Alternative proof routes", ""]
            for route in self.alternative_routes:
                refs = f"; IDs: {', '.join(route.rule_ids)}" if route.rule_ids else ""
                theorem_refs = f"; theorems: {', '.join(route.used_theorems)}" if route.used_theorems else ""
                lines.append(f"- **{route.name}:** {route.summary}{refs}{theorem_refs}")
        if self.used_theorems:
            lines += ["", "## Identities / theorems used", ""]
            for theorem in self.used_theorems:
                lines.append(
                    f"- **{theorem.get('name', 'Unnamed theorem')}**: "
                    f"`{theorem.get('lhs', '')} = {theorem.get('rhs', '')}` "
                    f"({theorem.get('source', 'User supplied')})"
                )
        if self.rule_ids and self.certificate_override is None:
            provenance = _dependency_provenance(self.rule_ids)
            if provenance:
                lines += ["", "## Transitive dependency provenance", ""]
                lines.extend(f"- {item}" for item in provenance)
        if self.counterexample is not None:
            lines += ["", "## Counterexample", ""]
            lines.append(", ".join(f"{name} = {value:.12g}" for name, value in self.counterexample.items()))
            lines.append(f"- LHS ≈ {self.lhs_value:.12g}; RHS ≈ {self.rhs_value:.12g}")
        lines += ["", "## Conclusion", "", self.message, ""]
        lines.append("> Numerical sampling is used only to find counterexamples; it is never used to certify an identity.")
        return "\n".join(lines)


class _SafeSympyParser:
    """AST parser that accepts arithmetic and the six elementary trig functions only."""

    def __init__(self, evaluate: bool = True):
        self.symbols: dict[str, sp.Symbol] = {}
        self.evaluate = evaluate

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
        # Numeric degree notation is converted exactly to radians before parsing.
        # This supports textbook inputs such as sin(30°) without changing the
        # engine's internal radian convention.
        text = re.sub(
            r"(?<![A-Za-z0-9_.])(\d+(?:\.\d+)?)\s*°",
            lambda m: f"({m.group(1)}*pi/180)", text,
        )
        text = re.sub(
            r"(?<![A-Za-z0-9_])([A-Za-z][A-Za-z0-9_]*)\s*°",
            lambda m: f"({m.group(1)}*pi/180)", text,
        )
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
            if isinstance(node.op, ast.USub):
                return -value if self.evaluate else sp.Mul(-1, value, evaluate=False)
            raise ExpressionInputError("Only unary + and - are supported.")
        if isinstance(node, ast.BinOp):
            left, right = self._visit(node.left), self._visit(node.right)
            if isinstance(node.op, ast.Add):
                return left + right if self.evaluate else sp.Add(left, right, evaluate=False)
            if isinstance(node.op, ast.Sub):
                return left - right if self.evaluate else sp.Add(left, sp.Mul(-1, right, evaluate=False), evaluate=False)
            if isinstance(node.op, ast.Mult):
                return left * right if self.evaluate else sp.Mul(left, right, evaluate=False)
            if isinstance(node.op, ast.Div):
                return left / right if self.evaluate else sp.Mul(left, sp.Pow(right, -1, evaluate=False), evaluate=False)
            if isinstance(node.op, ast.Pow):
                if right.is_number and abs(float(right)) > 1000:
                    raise ExpressionInputError("Exponent is too large for this first version.")
                return left ** right if self.evaluate else sp.Pow(left, right, evaluate=False)
            raise ExpressionInputError("Supported operators are +, -, *, / and **.")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ExpressionInputError("Only direct calls to the six trig functions and sqrt are supported.")
            name = node.func.id
            if name not in ALLOWED_FUNCTIONS:
                raise ExpressionInputError(f"Unsupported function '{name}'. Use sin, cos, tan, cot, sec, csc, sqrt or abs.")
            if len(node.args) != 1 or node.keywords:
                raise ExpressionInputError(f"{name}() requires exactly one argument.")
            argument = self._visit(node.args[0])
            return ALLOWED_FUNCTIONS[name](argument) if self.evaluate else ALLOWED_FUNCTIONS[name](argument, evaluate=False)
        raise ExpressionInputError(f"Unsupported syntax: {type(node).__name__}.")


def parse_expression(text: str) -> sp.Expr:
    return _SafeSympyParser().parse(text)


def parse_theorem_premises(
    premises: Iterable[dict | str | tuple],
    _depth: int = 0,
    _seen: set[tuple[str, str]] | None = None,
) -> list[TheoremPremise]:
    """Parse and symbolically validate reusable identities.

    A premise may be a mapping with name/lhs/rhs/source, a string in the form
    ``Name: lhs = rhs`` (or simply ``lhs = rhs``), or a three-item tuple.
    Conditional statements are intentionally not accepted in this release:
    every premise must be an identity on the common domain of its two sides.
    """
    validated: list[TheoremPremise] = []
    seen = set() if _seen is None else set(_seen)
    for index, item in enumerate(premises, 1):
        if isinstance(item, dict):
            name = str(item.get("name") or f"Premise {index}").strip()
            left_text, right_text = str(item.get("lhs", "")).strip(), str(item.get("rhs", "")).strip()
            source = str(item.get("source") or "User supplied")
            saved_conditions = item.get("domain_conditions", item.get("conditions", [])) or []
            proof_certificate = item.get("proof_certificate")
            identity_id = str(item.get("identity_id") or "")
        elif isinstance(item, tuple) and len(item) >= 3:
            name, left_text, right_text = (str(value).strip() for value in item[:3])
            source = str(item[3]) if len(item) > 3 else "User supplied"
            saved_conditions = []
            proof_certificate = None
            identity_id = ""
        elif isinstance(item, str):
            line = item.strip()
            if not line or line.startswith("#"):
                continue
            label, equation = f"Premise {index}", line
            if ":" in line:
                possible_label, possible_equation = line.split(":", 1)
                if "=" in possible_equation:
                    label, equation = possible_label.strip(), possible_equation.strip()
            if equation.count("=") != 1:
                raise ExpressionInputError(
                    f"Premise {index} must contain exactly one '=' sign: {line}"
                )
            left_text, right_text = (part.strip() for part in equation.split("=", 1))
            name, source = label, "Proof workspace premise"
            saved_conditions = []
            proof_certificate = None
            identity_id = ""
        else:
            raise ExpressionInputError(f"Unsupported premise format at item {index}.")

        if not left_text or not right_text:
            raise ExpressionInputError(f"Premise '{name}' needs both sides of an identity.")
        lhs, rhs = parse_expression(left_text), parse_expression(right_text)
        if not _symbolically_equivalent(lhs, rhs):
            key = (sp.srepr(lhs), sp.srepr(rhs))
            if _depth >= 5 or key in seen or not isinstance(proof_certificate, dict):
                raise ExpressionInputError(
                    f"Premise '{name}' is not established as a trigonometric identity. "
                    "Only symbolically verified identities or replayable proof results can be used."
                )
            claim = proof_certificate.get("claim", {})
            if proof_certificate.get("status") != "PROVED" or not claim.get("lhs") or not claim.get("rhs"):
                raise ExpressionInputError(f"Saved proof certificate for '{name}' is incomplete or not PROVED.")
            cert_lhs, cert_rhs = parse_expression(claim["lhs"]), parse_expression(claim["rhs"])
            if not ((cert_lhs == lhs and cert_rhs == rhs) or (cert_lhs == rhs and cert_rhs == lhs)):
                raise ExpressionInputError(f"Saved proof certificate does not match theorem '{name}'.")
            nested_records = proof_certificate.get("used_theorems", [])
            if not nested_records:
                raise ExpressionInputError(f"Saved proof certificate for '{name}' has no replayable theorem chain.")
            nested = parse_theorem_premises(nested_records, _depth + 1, seen | {key})
            replay = (
                _theorem_rewrite_route(lhs, rhs, "LHS", nested)
                or _theorem_rewrite_route(rhs, lhs, "RHS", nested)
                or _theorem_common_form_route(lhs, rhs, nested)
            )
            if replay is None:
                raise ExpressionInputError(f"The saved proof certificate for '{name}' could not be replayed.")
        conditions = tuple(dict.fromkeys(
            _domain_conditions(lhs, rhs)
            + _domain_conditions_from_text(left_text, right_text)
            + [_normalize_condition_text(str(c)) for c in saved_conditions]
        ))
        validated.append(TheoremPremise(name, lhs, rhs, source, conditions, proof_certificate, identity_id))
    return validated


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


_CATALOGUE_CONDITIONAL_IDS = {
    # These entries are indexed in SKILL.md but need explicit logical assumptions,
    # integer parameters, branch choices, or a prior substitution declaration.
    "S04", "S05", "S06", "D13", "D14", "D15", "D16",
    "H03", "H04", "H16", "H17", "H18", "H19", "H20", "H21",
    "P11", "P12",
}
_CATALOGUE_FUNCTIONS = "sin|cos|tan|cot|sec|csc"


def _split_catalogue_equations(formula: str) -> list[str]:
    """Split comma-separated paired identities without splitting inside arguments."""
    cleaned = formula.replace("`", "").strip()
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    for char in cleaned:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        if char == "," and depth == 0:
            part = "".join(current).strip()
            if "=" in part:
                parts.append(part)
            current = []
        else:
            current.append(char)
    part = "".join(current).strip()
    if "=" in part:
        parts.append(part)
    return parts


def _raise_group_superscripts(text: str) -> str:
    """Turn (whole expression)²/³/⁴ into an explicit power, respecting nesting."""
    for superscript, power in (("²", 2), ("³", 3), ("⁴", 4)):
        while superscript in text:
            index = text.index(superscript)
            if index == 0 or text[index - 1] != ")":
                raise ExpressionInputError("Unsupported superscript placement in catalogue identity.")
            depth = 0
            opening = None
            for cursor in range(index - 1, -1, -1):
                if text[cursor] == ")":
                    depth += 1
                elif text[cursor] == "(":
                    depth -= 1
                    if depth == 0:
                        opening = cursor
                        break
            if opening is None:
                raise ExpressionInputError("Unbalanced superscript group in catalogue identity.")
            text = text[:opening] + "(" + text[opening:index] + f")**{power}" + text[index + 1:]
    return text


def _catalogue_expression_text(text: str) -> str:
    """Convert the compact textbook notation used in SKILL.md to parser syntax."""
    value = text.strip().replace("`", "")
    value = value.replace("−", "-").replace("–", "-").replace("·", "*")
    value = value.replace("π", "pi").replace("φ", "phi").replace("√2", "sqrt(2)")
    if any(token in value for token in ("U_", "T_", "±", "If ", "n≥", "R sin", "R cos")):
        raise ExpressionInputError("This catalogue entry requires a parameter or branch assumption.")

    # Function powers such as sin²x, cos³x, or sin²(x/2).
    for superscript, power in (("²", 2), ("³", 3), ("⁴", 4)):
        pattern = rf"(?<![A-Za-z_])({_CATALOGUE_FUNCTIONS}){superscript}\s*(\([^()]*\)|[-+]?(?:\d+)?[A-Za-z_]\w*|pi)"
        value = re.sub(
            pattern,
            lambda match, p=power: (
                f"({match.group(1)}({match.group(2)[1:-1] if match.group(2).startswith('(') else match.group(2)}))**{p}"
            ),
            value,
        )

    # Compact function notation such as sin x, sin 2x, cos(nx), or tan(x+y).
    pattern = rf"(?<![A-Za-z_])({_CATALOGUE_FUNCTIONS})\s+(\([^()]*\)|[-+]?(?:\d+)?[A-Za-z_]\w*|pi)"
    value = re.sub(
        pattern,
        lambda match: f"{match.group(1)}({match.group(2)[1:-1] if match.group(2).startswith('(') else match.group(2)})",
        value,
    )
    value = _raise_group_superscripts(value)

    # Explicitly insert multiplication where conventional notation omits it.
    value = re.sub(r"(?<![A-Za-z0-9_])(\d+(?:\.\d+)?)\s*(?=(?:sin|cos|tan|cot|sec|csc)\()", r"\1*", value)
    value = re.sub(r"(?<![A-Za-z0-9_])([A-Za-z_]\w*)\s+(?=(?:sin|cos|tan|cot|sec|csc)\()", r"\1*", value)
    value = re.sub(r"(?<=\d)(?=[A-Za-z_])", "*", value)
    value = re.sub(r"(?<=\d)\s*(?=\()", "*", value)
    value = re.sub(r"(?<=\))\s*(?=(?:sin|cos|tan|cot|sec|csc|sqrt)\()", "*", value)
    value = re.sub(r"(?<=\))\s*(?=\()", "*", value)
    value = re.sub(r"(?<=[A-Za-z0-9_])\s+(?=(?:sin|cos|tan|cot|sec|csc|sqrt)\()", "*", value)
    return value.replace(" ", "")


@lru_cache(maxsize=4)
def _load_catalogue_theorems_cached(path_string: str, modified_ns: int) -> tuple[TheoremPremise, ...]:
    """Build the directly executable, symbolically validated equality rules."""
    del modified_ns  # Included in the cache key so an edited SKILL.md is reloaded.
    path = Path(path_string)
    rules: list[TheoremPremise] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        fields = [field.strip() for field in line.strip().strip("|").split("|")]
        if len(fields) < 3 or not re.fullmatch(r"[A-Z]\d{2}", fields[0]):
            continue
        identity_id, formula, _condition = fields[:3]
        if identity_id.startswith("I") or identity_id in _CATALOGUE_CONDITIONAL_IDS:
            continue
        for equation in _split_catalogue_equations(formula):
            left_text, right_text = (part.strip() for part in equation.split("=", 1))
            try:
                lhs = parse_expression(_catalogue_expression_text(left_text))
                rhs = parse_expression(_catalogue_expression_text(right_text))
            except (ExpressionInputError, ValueError, TypeError):
                continue
            # Catalogue rules enter the proof search only after exact symbolic validation.
            if not _symbolically_equivalent(lhs, rhs):
                lhs_rewritten = _rewrite_six_functions(lhs)
                rhs_rewritten = _rewrite_six_functions(rhs)
                if not _symbolically_equivalent(lhs_rewritten, rhs_rewritten):
                    continue
            conditions = tuple(dict.fromkeys(_domain_conditions(lhs, rhs)))
            rules.append(TheoremPremise(
                name=f"{identity_id} — {equation.strip()}",
                lhs=lhs,
                rhs=rhs,
                source="Bundled SKILL.md identity catalogue",
                domain_conditions=conditions,
                identity_id=identity_id,
            ))
    return tuple(rules)


def load_catalogue_theorems(skill_path: str | Path = DEFAULT_SKILL_PATH) -> list[TheoremPremise]:
    """Return all directly applicable, exact-validated equality rules from SKILL.md."""
    path = Path(skill_path)
    if not path.exists():
        return []
    return list(_load_catalogue_theorems_cached(str(path.resolve()), path.stat().st_mtime_ns))


def catalogue_rule_statistics(skill_path: str | Path = DEFAULT_SKILL_PATH) -> dict[str, int]:
    """Summarise the indexed reference entries and executable equality rules."""
    indexed = load_rule_catalogue(skill_path)
    executable = load_catalogue_theorems(skill_path)
    conditional_ids = {rule_id for rule_id in _CATALOGUE_CONDITIONAL_IDS}
    conditional = sum(1 for item in indexed if item["id"] in conditional_ids)
    inequalities = sum(1 for item in indexed if item["id"].startswith("I"))
    return {
        "indexed_entries": len(indexed),
        "executable_equalities": len(executable),
        "conditional_entries": conditional,
        "inequality_entries": inequalities,
    }


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


def _nonzero_condition_base(expression: sp.Expr) -> sp.Expr:
    """Remove positive integer powers from a nonzero condition's base."""
    value = sp.simplify(expression)
    while (isinstance(value, sp.Pow) and value.exp.is_integer is True
           and value.exp.is_positive is True):
        value = sp.simplify(value.base)
    return value


def _normalize_condition_text(condition: str) -> str:
    """Simplify a displayed domain condition after theorem-variable substitution."""
    suffixes = (" ≥ 0 (real square root)", " ≠ 0")
    for suffix in suffixes:
        if condition.endswith(suffix):
            expression_text = condition[:-len(suffix)].strip()
            try:
                expression = sp.simplify(parse_expression(expression_text))
                if suffix == " ≠ 0":
                    expression = _nonzero_condition_base(expression)
                return f"{sp.sstr(expression)}{suffix}"
            except Exception:
                return condition
    return condition


def _domain_conditions(*expressions: sp.Expr) -> list[str]:
    """Collect visible original-domain restrictions without solving intervals."""
    nonzero: dict[str, str] = {}
    nonnegative: dict[str, str] = {}
    for expr in expressions:
        for node in sp.preorder_traversal(expr):
            if getattr(node, "func", None) in RECIPROCAL_DOMAIN_FUNCTIONS:
                base = sp.simplify(RECIPROCAL_DOMAIN_FUNCTIONS[node.func](node.args[0]))
                if not base.is_number:
                    nonzero[sp.srepr(base)] = sp.sstr(base)
            if isinstance(node, sp.Pow) and node.exp.is_negative:
                base = sp.simplify(node.base)
                if not base.is_number:
                    nonzero[sp.srepr(base)] = sp.sstr(base)
            if node.func == sp.sqrt:
                radicand = node.args[0]
                nonnegative[sp.srepr(radicand)] = sp.sstr(radicand)
    conditions = [f"{value} ≠ 0" for value in nonzero.values()]
    conditions += [f"{value} ≥ 0 (real square root)" for value in nonnegative.values()]
    return sorted(conditions, key=str.casefold)


def _domain_conditions_from_text(*texts: str) -> list[str]:
    """Collect restrictions before SymPy canonicalisation can cancel a denominator."""
    nonzero: dict[str, str] = {}
    nonnegative: dict[str, str] = {}
    for text in texts:
        parser = _SafeSympyParser()
        try:
            tree = ast.parse(parser._normalise(text), mode="eval")
        except (SyntaxError, TypeError, ValueError):
            continue

        def visit(node):
            try:
                if isinstance(node, ast.BinOp):
                    if isinstance(node.op, ast.Div):
                        denominator = _nonzero_condition_base(parser._visit(node.right))
                        if not denominator.is_number:
                            nonzero[sp.srepr(denominator)] = sp.sstr(denominator)
                    elif isinstance(node.op, ast.Pow):
                        exponent = parser._visit(node.right)
                        if exponent.is_negative:
                            base = _nonzero_condition_base(parser._visit(node.left))
                            if not base.is_number:
                                nonzero[sp.srepr(base)] = sp.sstr(base)
                elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and len(node.args) == 1:
                    argument = parser._visit(node.args[0])
                    if node.func.id in {"tan", "sec"}:
                        base = sp.simplify(sp.cos(argument))
                        if not base.is_number:
                            nonzero[sp.srepr(base)] = sp.sstr(base)
                    elif node.func.id in {"cot", "csc"}:
                        base = sp.simplify(sp.sin(argument))
                        if not base.is_number:
                            nonzero[sp.srepr(base)] = sp.sstr(base)
                    elif node.func.id == "sqrt":
                        nonnegative[sp.srepr(argument)] = sp.sstr(argument)
            except Exception:
                pass
            for child in ast.iter_child_nodes(node):
                visit(child)

        visit(tree.body)
    conditions = [f"{value} ≠ 0" for value in nonzero.values()]
    conditions += [f"{value} ≥ 0 (real square root)" for value in nonnegative.values()]
    return sorted(set(conditions), key=str.casefold)


def _symbolically_equivalent(left: sp.Expr, right: sp.Expr) -> bool:
    """Try exact symbolic equivalence only; never use floating-point sampling here."""
    difference = sp.together(left - right)
    if difference == 0:
        return True
    strategies = (
        sp.trigsimp,
        lambda e: sp.trigsimp(sp.expand_trig(e)),
        lambda e: sp.trigsimp(_rewrite_six_functions(e)),
        lambda e: sp.trigsimp(sp.expand_trig(_rewrite_six_functions(e))),
        lambda e: fu(_rewrite_six_functions(e)),
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


@lru_cache(maxsize=2048)
def _premise_pattern(expr: sp.Expr) -> tuple[sp.Expr, dict[sp.Symbol, sp.Wild]]:
    """Turn theorem variables into consistent wildcards for substitution matching."""
    symbols = sorted(expr.free_symbols, key=lambda symbol: symbol.name)
    symbol_to_wild = {
        symbol: sp.Wild(f"premise_{index}_{symbol.name}")
        for index, symbol in enumerate(symbols)
    }
    return expr.xreplace(symbol_to_wild), symbol_to_wild


def _premise_rewrites(
    expr: sp.Expr,
    theorem: TheoremPremise,
    context_symbols: Iterable[sp.Symbol] = (),
    target_expr: sp.Expr | None = None,
):
    """Yield safe, target-guided single-subexpression theorem rewrites.

    The theorem has already passed symbolic validation. Every variable in an
    instantiation must be bound by the matched source subexpression or by a
    structurally compatible subexpression of the requested target. The search
    deliberately does not guess arbitrary values for unbound theorem variables.
    """
    del context_symbols  # Retained for API compatibility with earlier versions.
    directions = ((theorem.lhs, theorem.rhs, "forward"),
                  (theorem.rhs, theorem.lhs, "reverse"))
    for source, replacement, direction in directions:
        pattern, symbol_to_wild = _premise_pattern(source)
        replacement_pattern, replacement_to_wild = _premise_pattern(replacement)
        theorem_symbols = theorem.lhs.free_symbols.union(theorem.rhs.free_symbols)
        for subexpression in sp.preorder_traversal(expr):
            if subexpression.func is not pattern.func:
                continue
            try:
                match = subexpression.match(pattern)
            except Exception:
                continue
            if match is None:
                continue
            symbol_values = {
                symbol: match[wild]
                for symbol, wild in symbol_to_wild.items()
                if wild in match
            }
            unbound = [symbol for symbol in theorem_symbols if symbol not in symbol_values]
            assignments: list[dict[sp.Symbol, sp.Expr]] = []
            if not unbound:
                assignments = [symbol_values]
            elif target_expr is not None:
                # Infer remaining variables only when the replacement side
                # matches an actual subexpression of the requested target.
                for target_subexpression in sp.preorder_traversal(target_expr):
                    if target_subexpression.func is not replacement_pattern.func:
                        continue
                    try:
                        target_match = target_subexpression.match(replacement_pattern)
                    except Exception:
                        continue
                    if target_match is None:
                        continue
                    proposed = dict(symbol_values)
                    consistent = True
                    for symbol, wild in replacement_to_wild.items():
                        if wild not in target_match:
                            continue
                        value = target_match[wild]
                        if symbol in proposed and proposed[symbol] != value:
                            consistent = False
                            break
                        proposed[symbol] = value
                    if consistent and all(symbol in proposed for symbol in unbound):
                        assignments.append(proposed)
            # Do not create speculative branches by assigning arbitrary
            # context variables. That behaviour made catalogue search slow and
            # could produce opaque substitutions unrelated to the target.
            unique_assignments = []
            seen_assignments = set()
            for values in assignments:
                signature = tuple(sorted((symbol.name, sp.srepr(value)) for symbol, value in values.items()))
                if signature not in seen_assignments:
                    seen_assignments.add(signature)
                    unique_assignments.append(values)
            for values in unique_assignments:
                instantiated = replacement.xreplace(values)
                if instantiated.has(sp.Wild):
                    continue
                candidate = expr.xreplace({subexpression: instantiated})
                if candidate == expr:
                    continue
                used_lhs = theorem.lhs.xreplace(values)
                used_rhs = theorem.rhs.xreplace(values)
                inherited_conditions = []
                for condition in theorem.domain_conditions:
                    rewritten_condition = condition
                    for symbol, value in sorted(values.items(), key=lambda item: len(item[0].name), reverse=True):
                        rewritten_condition = re.sub(
                            rf"\b{re.escape(symbol.name)}\b", sp.sstr(value), rewritten_condition
                        )
                    inherited_conditions.append(_normalize_condition_text(rewritten_condition))
                conditions = tuple(dict.fromkeys(
                    _domain_conditions(used_lhs, used_rhs) + inherited_conditions
                ))
                substitution = tuple(sorted((symbol.name, sp.sstr(value)) for symbol, value in values.items()))
                yield candidate, direction, conditions, substitution


def _algebraically_equivalent(left: sp.Expr, right: sp.Expr) -> bool:
    """Check equivalence using algebra only, treating trig subexpressions as atoms."""
    try:
        return sp.cancel(sp.together(left - right)) == 0
    except Exception:
        return False


def _factor_rational_form(expr: sp.Expr) -> sp.Expr:
    """Factor numerator and denominator separately without cancelling them."""
    numerator, denominator = sp.fraction(expr, exact=True)
    factored_numerator = sp.factor(numerator)
    factored_denominator = sp.factor(denominator)
    if factored_numerator == numerator and factored_denominator == denominator:
        return expr
    if factored_denominator == 1:
        return factored_numerator
    return sp.Mul(
        factored_numerator,
        sp.Pow(factored_denominator, -1, evaluate=False),
        evaluate=False,
    )


def _algebraic_cleanup(expr: sp.Expr, side: str) -> tuple[sp.Expr, list[ProofStep], tuple[str, ...]]:
    """Expose routine algebra between theorem applications as separate proof steps."""
    current = expr
    steps: list[ProofStep] = []
    conditions: list[str] = []

    def apply(title: str, transform: Callable[[sp.Expr], sp.Expr], note: str) -> None:
        nonlocal current
        try:
            candidate = transform(current)
            if candidate == current or sp.count_ops(candidate) > 120:
                return
            if not _algebraically_equivalent(current, candidate):
                return
            step_conditions = tuple(_domain_conditions(current, candidate))
            steps.append(ProofStep(
                title, candidate, note, (), side, current,
                domain_conditions=step_conditions,
            ))
            conditions.extend(step_conditions)
            current = candidate
        except Exception:
            return

    # Only combine fractions when the current expression is a sum of separate
    # rational terms. A single fraction is already over one denominator.
    if current.func == sp.Add:
        fractional_terms = 0
        for term in current.args:
            if any(isinstance(node, sp.Pow) and node.exp.is_negative
                   for node in sp.preorder_traversal(term)):
                fractional_terms += 1
        if fractional_terms > 1:
            apply(
                "Combine algebraic fractions", sp.together,
                "Combine rational terms over a common denominator without applying another trigonometric identity.",
            )

    apply(
        "Factor numerator and denominator", _factor_rational_form,
        "Factor the numerator and denominator separately; common factors are not cancelled in this step.",
    )
    apply(
        "Cancel common algebraic factors", sp.cancel,
        "Cancel common factors. The original and intermediate denominator restrictions remain in force.",
    )
    return current, steps, tuple(dict.fromkeys(conditions))


def _route_identity_ids(steps: Iterable[ProofStep]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(rule for step in steps for rule in step.rule_ids))


def _route_name(side: str, steps: list[ProofStep]) -> str:
    if any(step.rule_ids for step in steps):
        return f"{side} using identity catalogue"
    return f"{side} using supplied identities"


def _rule_match_priority(theorem: TheoremPremise, source: sp.Expr, target: sp.Expr) -> tuple:
    """Prioritise exact, simple, target-relevant identity applications."""
    source_nodes = list(sp.preorder_traversal(source))
    target_nodes = list(sp.preorder_traversal(target))
    best = (4, 4)
    for source_side, replacement_side in ((theorem.lhs, theorem.rhs), (theorem.rhs, theorem.lhs)):
        source_pattern, _ = _premise_pattern(source_side)
        target_pattern, _ = _premise_pattern(replacement_side)
        source_matches = []
        target_matches = []
        for node in source_nodes:
            if node.func is source_pattern.func:
                try:
                    matched = node.match(source_pattern) is not None
                except Exception:
                    matched = False
                if matched:
                    source_matches.append(node)
        for node in target_nodes:
            if node.func is target_pattern.func:
                try:
                    matched = node.match(target_pattern) is not None
                except Exception:
                    matched = False
                if matched:
                    target_matches.append(node)
        if source_matches:
            source_level = 0 if source in source_matches else 1
            target_level = 0 if target in target_matches else (1 if target_matches else 2)
            best = min(best, (source_level, target_level))
    variable_count = len(theorem.lhs.free_symbols.union(theorem.rhs.free_symbols))
    # Exact whole-expression identities with fewer variables are clearer and
    # more canonical than broad compound-angle patterns requiring x = y.
    return (*best, variable_count, theorem.identity_id, theorem.name)


def _theorem_rewrite_route(
    source: sp.Expr,
    target: sp.Expr,
    side: str,
    theorems: list[TheoremPremise],
    max_depth: int = 8,
    max_nodes: int = 260,
) -> ProofRoute | None:
    """Search a multi-identity derivation using breadth-first rewriting.

    One queue edge is one validated theorem application followed, where useful,
    by separately displayed algebraic cleanup. Breadth-first order favours the
    fewest identity applications. Variables are instantiated only from the
    source match or the requested target; no arbitrary variable guessing occurs.
    """
    if not theorems:
        return None
    ordered_theorems = sorted(
        theorems,
        key=lambda theorem: _rule_match_priority(theorem, source, target),
    )
    start = ProofStep(f"Start with the {side}", source,
                      "Original expression in the requested identity.", (), side, None)
    queue = [(source, [start], frozenset(), tuple())]
    visited = {sp.srepr(source)}
    examined = 0

    while queue and examined < max_nodes:
        current, path, used_names, path_conditions = queue.pop(0)
        examined += 1
        identity_depth = sum(bool(step.theorem_ref) for step in path)
        if identity_depth >= max_depth:
            continue
        for theorem in ordered_theorems:
            rewrites = list(_premise_rewrites(current, theorem, target.free_symbols, target))
            # Prefer the rewrite that most directly resembles the target; this
            # keeps a proof chain readable when several identities can apply.
            rewrites.sort(key=lambda item: (
                0 if item[0] == target else 1 if _algebraically_equivalent(item[0], target) else 2,
                sp.count_ops(item[0]), sp.sstr(item[0]),
            ))
            for candidate, direction, conditions, substitution in rewrites:
                if sp.count_ops(candidate) > 120:
                    continue
                note = (
                    f"Apply established identity {theorem.identity_id or theorem.name} in the {direction} direction "
                    "to the matched subexpression. The instantiated identity is checked against the recorded step."
                )
                display_name = theorem.name.split(" — ", 1)[1] if theorem.identity_id and " — " in theorem.name else theorem.name
                identity_step = ProofStep(
                    f"Apply identity {theorem.identity_id}: {display_name}" if theorem.identity_id
                    else f"Apply supplied identity: {theorem.name}",
                    candidate, note,
                    (theorem.identity_id,) if theorem.identity_id else (),
                    side, current, theorem.name, conditions, substitution,
                )
                next_path = path + [identity_step]
                next_names = used_names | {theorem.name}
                next_conditions = tuple(dict.fromkeys(
                    path_conditions + conditions + tuple(_domain_conditions(current, candidate))
                ))
                # Check the requested target immediately after the identity
                # substitution. This avoids inserting cosmetic factor/cancel
                # steps when the new form already matches the RHS.
                if candidate == target:
                    if candidate != target:
                        next_path.append(ProofStep(
                            "Rearrange algebraically to the target form", target,
                            "The expressions differ only by algebraic ordering or grouping; the trigonometric subexpressions are unchanged.",
                            (), side, candidate,
                        ))
                    next_path.append(ProofStep(
                        "Match the target side", target,
                        "The displayed identity substitutions establish the requested target form.",
                        (), side, target,
                    ))
                    full_path = next_path
                    return ProofRoute(
                        _route_name(side, full_path), full_path,
                        f"The {side.lower()} reaches the target through {sum(bool(step.theorem_ref) for step in full_path)} explicit identity application(s) and displayed algebraic steps.",
                        _route_identity_ids(full_path), tuple(sorted(next_names)), next_conditions,
                    )

                normal, algebra_steps, algebra_conditions = _algebraic_cleanup(candidate, side)
                next_path.extend(algebra_steps)
                next_conditions = tuple(dict.fromkeys(next_conditions + algebra_conditions))

                if normal == target or _algebraically_equivalent(normal, target):
                    if normal != target:
                        next_path.append(ProofStep(
                            "Rearrange algebraically to the target form", target,
                            "Reorder terms or rewrite the same algebraic fraction. The trigonometric subexpressions are unchanged.",
                            (), side, normal,
                        ))
                    next_path.append(ProofStep(
                        "Match the target side", target,
                        "The displayed identity substitutions and algebraic steps establish the requested target form.",
                        (), side, target,
                    ))
                    full_path = next_path
                    return ProofRoute(
                        _route_name(side, full_path), full_path,
                        f"The {side.lower()} reaches the target through {sum(bool(step.theorem_ref) for step in full_path)} explicit identity application(s) and displayed algebraic steps.",
                        _route_identity_ids(full_path), tuple(sorted(next_names)), next_conditions,
                    )

                key = sp.srepr(normal)
                if key in visited:
                    continue
                visited.add(key)
                queue.append((normal, next_path, frozenset(next_names), next_conditions))
    return None


def _theorem_common_form_route(
    lhs: sp.Expr,
    rhs: sp.Expr,
    theorems: list[TheoremPremise],
) -> ProofRoute | None:
    """Find a common form using explicit identity substitutions and algebra."""
    def reachable(source: sp.Expr, side: str, target: sp.Expr, max_depth: int = 3, max_nodes: int = 70):
        ordered = sorted(theorems, key=lambda theorem: (_rule_match_priority(theorem, source, target), theorem.identity_id, theorem.name))
        queue = [(source, [ProofStep(f"Start with the {side}", source,
                                     "Original expression in the claim.", (), side, None)],
                  frozenset(), tuple())]
        seen = {sp.srepr(source)}
        results = []
        examined = 0
        while queue and examined < max_nodes:
            current, path, used, conditions = queue.pop(0)
            examined += 1
            results.append((current, path, used, conditions))
            if sum(bool(step.theorem_ref) for step in path) >= max_depth:
                continue
            for theorem in ordered:
                for candidate, direction, local_conditions, substitution in _premise_rewrites(
                    current, theorem, lhs.free_symbols | rhs.free_symbols,
                    rhs if side == "LHS" else lhs
                ):
                    if sp.count_ops(candidate) > 120:
                        continue
                    display_name = theorem.name.split(" — ", 1)[1] if theorem.identity_id and " — " in theorem.name else theorem.name
                    step = ProofStep(
                        f"Apply identity {theorem.identity_id}: {display_name}" if theorem.identity_id
                        else f"Apply supplied identity: {theorem.name}",
                        candidate,
                        f"Apply established identity {theorem.identity_id or theorem.name} in the {direction} direction to a matching subexpression.",
                        (theorem.identity_id,) if theorem.identity_id else (),
                        side, current, theorem.name, local_conditions, substitution,
                    )
                    next_path = path + [step]
                    normal, algebra_steps, algebra_conditions = _algebraic_cleanup(candidate, side)
                    next_path.extend(algebra_steps)
                    next_conditions = tuple(dict.fromkeys(
                        conditions + local_conditions + tuple(_domain_conditions(current, candidate)) + algebra_conditions
                    ))
                    key = sp.srepr(normal)
                    if key in seen:
                        continue
                    seen.add(key)
                    queue.append((normal, next_path, used | {theorem.name}, next_conditions))
        return results

    left_reachable = reachable(lhs, "LHS", rhs)
    right_reachable = reachable(rhs, "RHS", lhs)
    right_by_form: dict[str, list[tuple]] = {}
    for item in right_reachable:
        right_by_form.setdefault(sp.srepr(item[0]), []).append(item)
    matches = []
    for left_expr, left_path, left_used, left_conditions in left_reachable:
        for right_expr, right_path, right_used, right_conditions in right_by_form.get(sp.srepr(left_expr), []):
            total_steps = len(left_path) + len(right_path)
            matches.append((total_steps, left_expr, left_path, right_path,
                            left_used | right_used,
                            tuple(dict.fromkeys(left_conditions + right_conditions))))
    if not matches:
        return None
    _, common, left_path, right_path, used, conditions = min(matches, key=lambda item: item[0])
    final_step = ProofStep(
        "Establish a common form", common,
        "Both sides reach exactly the same expression through the displayed identity and algebra steps.",
        (), "Both sides", None,
    )
    steps = left_path + right_path + [final_step]
    return ProofRoute(
        "Both sides to common form using identity catalogue",
        steps,
        "Both sides reach a common form using established catalogue identities and explicit algebraic steps.",
        _route_identity_ids(steps), tuple(sorted(used)), conditions,
    )


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


# Audited dependencies from SKILL.md B01--B04 and the v0.5 geometric kernel.
# F01-F04 are definitional roots. F08 is NOT a root: it depends on a replayed
# geometric certificate. Unlisted catalogue rules have UNKNOWN provenance.
AUDITED_DEPENDENCIES = {
    "F01": (), "F02": (), "F03": (), "F04": (), "F08": ("GEO.F08",),
    "F05": ("F01", "F02"), "F06": ("F04",), "F07": ("F03",),
    "F09": ("F08", "F01", "F03"),
    "F10": ("F08", "F02", "F04"),
    "F11": ("F09",), "F12": ("F10",),
}


def _verified_geometric_f08_foundation() -> bool:
    """Return true only if the canonical independent F08 GEO certificate replays."""
    try:
        lhs = parse_expression("sin(x)**2 + cos(x)**2")
        rhs = parse_expression("1")
        domain = _domain_conditions(lhs, rhs)
        certificate = build_f08_geometric_certificate(lhs, rhs, domain)
        if certificate is None:
            return False
        valid, _reason = verify_geometric_certificate(
            certificate, parse_expression, lhs, rhs, domain
        )
        return bool(valid)
    except Exception:
        return False


def _dependency_provenance(identity_ids: Iterable[str]) -> list[str]:
    """Return the transitive audited dependency trace, including geometric F08."""
    rows: list[str] = []
    visited: set[str] = set()

    def visit(identity_id: str):
        if identity_id in visited:
            return
        visited.add(identity_id)
        for dependency in AUDITED_DEPENDENCIES.get(identity_id, ()):
            rows.append(f"{identity_id} depends on {dependency}")
            if dependency == "GEO.F08":
                rows.append("GEO.F08 is admitted only after replaying G01 → G03 → G04")
            else:
                visit(dependency)

    for identity_id in identity_ids:
        visit(identity_id)
    return rows


def _same_claim(lhs, rhs, theorem):
    """Recognise instances, reversal, scaling and algebraic rearrangement.

    Never use trigsimp here: every true identity would then equal every other.
    Bind variables through trig arguments, then compare residuals by algebra.
    """
    bindings = [{}]
    symbols = theorem.lhs.free_symbols | theorem.rhs.free_symbols
    for symbol in sorted(symbols, key=str):
        arguments = {node.args[0] for expr in (lhs, rhs)
                     for node in sp.preorder_traversal(expr)
                     if node.func in TRIG_FUNCTIONS}
        arguments |= lhs.free_symbols | rhs.free_symbols
        bindings = [dict(b, **{str(symbol): arg}) for b in bindings for arg in arguments]
        if len(bindings) > 256:
            return True  # Conservative exclusion for oversized matching work.
    residual = sp.cancel(lhs - rhs)
    for binding in bindings:
        values = {symbol: binding[str(symbol)] for symbol in symbols}
        template = sp.cancel((theorem.lhs - theorem.rhs).xreplace(values))
        if template == 0:
            continue
        ratio = sp.cancel(residual / template)
        if ratio != 0 and not ratio.has(*TRIG_FUNCTIONS) and not ratio.has(sp.zoo, sp.nan):
            return True
    return False


def _independent_premises(lhs, rhs, supplied, catalogue, include_catalogue=True):
    """Admit only audited roots/descendants or replayed acyclic certificates."""
    by_id = {t.identity_id: t for t in catalogue}
    blocked = {t.identity_id for t in catalogue if _same_claim(lhs, rhs, t)}

    def safe_id(identity_id, stack=()):
        if identity_id == "GEO.F08":
            return _verified_geometric_f08_foundation()
        if identity_id in blocked or identity_id in stack or identity_id not in AUDITED_DEPENDENCIES:
            return False
        return all(safe_id(dep, stack + (identity_id,))
                   for dep in AUDITED_DEPENDENCIES[identity_id])

    def admit(t, stack=()):
        if _same_claim(lhs, rhs, t):
            return False
        key = (sp.srepr(t.lhs), sp.srepr(t.rhs))
        if key in stack or len(stack) >= 20:
            return False
        # Formula and ID must agree; a renamed F08 cannot masquerade as F03.
        if t.identity_id in by_id and t.proof_certificate is None:
            canonical = by_id[t.identity_id]
            if _same_claim(t.lhs, t.rhs, canonical) and safe_id(t.identity_id):
                return True
        cert = t.proof_certificate
        if isinstance(cert, dict) and cert.get("schema") == GEOMETRIC_CERTIFICATE_SCHEMA:
            valid, _reason = verify_geometric_certificate(
                cert, parse_expression, t.lhs, t.rhs, t.domain_conditions
            )
            return bool(valid)
        # A legacy/v4 status flag and symbolic oracle must never resurrect F08
        # as an assumed premise. F08-shaped claims require the GEO certificate.
        if match_f08_claim(t.lhs, t.rhs) is not None:
            return False
        if not isinstance(cert, dict) or cert.get("schema") != "trigonometric-proof-certificate-v4" or cert.get("status") != "PROVED":
            return False
        claim = cert.get("claim", {})
        try:
            if (parse_expression(claim["lhs"]), parse_expression(claim["rhs"])) != (t.lhs, t.rhs):
                return False
            nested = parse_theorem_premises(cert.get("used_theorems", []))
            # Check every dependency even if a symbolic oracle says t is true.
            if not all(admit(dep, stack + (key,)) for dep in nested):
                return False
            if _algebraically_equivalent(t.lhs, t.rhs):
                return True
            return bool(_theorem_rewrite_route(t.lhs, t.rhs, "LHS", nested)
                        or _theorem_rewrite_route(t.rhs, t.lhs, "RHS", nested)
                        or _theorem_common_form_route(t.lhs, t.rhs, nested))
        except (ValueError, TypeError, KeyError, RecursionError):
            return False

    accepted = [t for t in catalogue if safe_id(t.identity_id)] if include_catalogue else []
    accepted.extend(t for t in supplied if admit(t))
    # Names are certificate references, so do not allow ambiguous shadowing.
    names = {}
    for theorem in accepted:
        if theorem.name in names and names[theorem.name] != theorem:
            continue
        names[theorem.name] = theorem
    return list(names.values())


def prove_identity(
    lhs_text: str,
    rhs_text: str,
    method: str = "Automatic",
    premises: Iterable[dict | str | tuple] | None = None,
) -> ProofResult:
    lhs, rhs = parse_expression(lhs_text), parse_expression(rhs_text)
    domain = sorted(set(
        _normalize_condition_text(condition)
        for condition in (_domain_conditions(lhs, rhs) + _domain_conditions_from_text(lhs_text, rhs_text))
    ), key=str.casefold)
    allowed_methods = {"Automatic", "LHS to RHS", "RHS to LHS",
                       "Both sides to common form", "Difference method",
                       "Angle expansion first", "Fu transformations first",
                       "Algebraic reduction first", "Use supplied identities",
                       "Use full identity catalogue"}
    if method not in allowed_methods:
        raise ValueError(f"Unknown proof strategy: {method}")

    # Foundational F08 is attempted through the independent GEO kernel before
    # any catalogue, trigonometric simplifier, or saved theorem is considered.
    # This route is available in every proof mode and cannot use F08 as a premise.
    geometric_certificate = build_f08_geometric_certificate(lhs, rhs, domain)
    if geometric_certificate is not None:
        valid, _reason = verify_geometric_certificate(
            geometric_certificate, parse_expression, lhs, rhs, domain
        )
        if valid:
            return ProofResult(
                status="PROVED", lhs=lhs, rhs=rhs, steps=[],
                domain_conditions=domain,
                message=(
                    "An independent geometric proof establishes the identity through "
                    "G01 (Pythagorean dissection), G03 (Cartesian squared distance) "
                    "and G04 (unit-circle substitution). The replayable GEO certificate "
                    "passed. No trigonometric catalogue identity is used as a premise. "
                    "The result is relative to the explicit trusted foundations "
                    "AX.REAL, AX.EUCLID, AX.AREA and D.UNIT."
                ),
                selected_route="GEO: G01 → G03 → G04",
                rule_ids=("G01", "G03", "G04"),
                used_theorems=[],
                certificate_override=geometric_certificate,
            )

    supplied_theorems = parse_theorem_premises(premises or [])
    theorems = supplied_theorems
    if method == "Use full identity catalogue":
        # A numerical counterexample can safely disprove a claim, so run this
        # cheap diagnostic before the larger catalogue search. It never proves.
        counterexample = _find_counterexample(lhs, rhs)
        if counterexample is not None:
            point, lv, rv = counterexample
            return ProofResult(
                "DISPROVED", lhs, rhs, [], domain,
                "A valid numerical counterexample was found before catalogue search. The proposed identity is false.",
                point, lv, rv, selected_route=method,
            )
        # The complete directly applicable catalogue is always available in this mode.
        # User premises and the saved theorem bank are included as additional rules.
        theorems = supplied_theorems + load_catalogue_theorems()
    catalogue = load_catalogue_theorems()
    theorems = _independent_premises(lhs, rhs, supplied_theorems, catalogue,
                                   include_catalogue=method != "Use supplied identities")
    route_candidates: list[ProofRoute] = []
    if _algebraically_equivalent(lhs, rhs):
        route_candidates.append(ProofRoute(
            "Algebra only", [ProofStep("Algebraic equality", rhs,
            "Rational algebra with trigonometric expressions treated as atoms.",
            (), "LHS", lhs)], "The claim follows by algebra alone."))
    elif theorems:
        directions = [(lhs, rhs, "LHS"), (rhs, lhs, "RHS")]
        if method == "LHS to RHS":
            directions = directions[:1]
        elif method == "RHS to LHS":
            directions = directions[1:]
        if method != "Both sides to common form":
            for source, target, side in directions:
                route = _theorem_rewrite_route(source, target, side, theorems, 7, 260)
                if route:
                    route_candidates.append(route)
                    break
        if not route_candidates and method not in {"LHS to RHS", "RHS to LHS"}:
            route = _theorem_common_form_route(lhs, rhs, theorems)
            if route:
                route_candidates.append(route)

    if route_candidates:
        priority = {"LHS to other side": 0, "RHS to other side": 1,
                    "Both sides to common form": 2, "Difference method": 3,
                    "LHS using supplied identities": 4,
                    "RHS using supplied identities": 5,
                    "Both sides to common form using supplied identities": 6}
        if method in {"Use supplied identities", "Use full identity catalogue"}:
            route_candidates.sort(key=lambda route: (
                sum(bool(step.theorem_ref) for step in route.steps), len(route.steps),
                len(route.rule_ids), route.name
            ))
        else:
            route_candidates.sort(key=lambda route: (priority.get(route.name, 9), len(route.steps)))
        selected = route_candidates[0]
        alternatives = route_candidates[1:]
        # Preserve the actual derivation order in the theorem/reference list.
        used_order = list(dict.fromkeys(
            step.theorem_ref for step in selected.steps if step.theorem_ref
        ))
        theorem_by_name = {theorem.name: theorem for theorem in theorems}
        used_records = [
            {
                "name": theorem_by_name[name].name,
                "lhs": sp.sstr(theorem_by_name[name].lhs),
                "rhs": sp.sstr(theorem_by_name[name].rhs),
                "source": theorem_by_name[name].source,
                "domain_conditions": list(theorem_by_name[name].domain_conditions),
                "proof_certificate": theorem_by_name[name].proof_certificate,
                "identity_id": theorem_by_name[name].identity_id,
            }
            for name in used_order if name in theorem_by_name
        ]
        full_domain = sorted(set(domain).union(selected.domain_conditions), key=str.casefold)
        return ProofResult(
            "PROVED", lhs, rhs, selected.steps, full_domain,
            (f"The identity search found a derivation using {sum(bool(step.theorem_ref) for step in selected.steps)} explicit established identity application(s). Each substitution and algebraic transformation is recorded separately on the original common domain." if method == "Use full identity catalogue" else "A symbolic transformation route established equality on the original common domain. Every identity application and algebraic step is shown explicitly in the selected route."),
            selected_route=selected.name, alternative_routes=alternatives, rule_ids=selected.rule_ids,
            used_theorems=used_records,
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
                       "No independent derivation was found. The target, its dependent identities, uncertified premises, and catalogue rules with unaudited dependencies are unavailable. Symbolic simplification is not accepted as proof. This does not mean the claim is false.",
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
