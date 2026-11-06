"""Build the finite seven-atom candidate catalogue for v0.6.0.

The unit-circle relation is used only as a candidate-discovery filter. Every
candidate still needs a proof from engine.py before it enters the question bank.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import product
from math import comb
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
ATOM_NAMES = ["sin(x)", "cos(x)", "tan(x)", "cot(x)", "sec(x)", "csc(x)", "1"]
x = sp.Symbol("x", real=True)
ATOMS = [sp.sin(x), sp.cos(x), sp.tan(x), sp.cot(x), sp.sec(x), sp.csc(x), sp.Integer(1)]
Z = {(0, 0): 1}
S = {(1, 0): 1}
C = {(0, 1): 1}
RAT = [(S, Z), (C, Z), (S, C), (C, S), (Z, C), (Z, S), (Z, Z)]


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def padd(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = out.get(key, 0) + value
    return clean(out)


def pneg(a):
    return {key: -value for key, value in a.items()}


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = defaultdict(int)
    for (i, j), u in a.items():
        for (k, ell), v in b.items():
            out[(i + k, j + ell)] += u * v
    return clean(out)


def reduce_circle(poly):
    out = defaultdict(int)
    for (i, j), value in poly.items():
        q, r = divmod(j, 2)
        for k in range(q + 1):
            out[(i + 2 * k, r)] += value * comb(q, k) * ((-1) ** k)
    return clean(out)


def radd(a, b):
    return (padd(pmul(a[0], b[1]), pmul(b[0], a[1])), pmul(a[1], b[1]))


def rsub(a, b):
    return (psub(pmul(a[0], b[1]), pmul(b[0], a[1])), pmul(a[1], b[1]))


def rmul(a, b):
    return (pmul(a[0], b[0]), pmul(a[1], b[1]))


def rdiv(a, b):
    return (pmul(a[0], b[1]), pmul(a[1], b[0]))


def is_candidate_identity(rational_form):
    return not reduce_circle(rational_form[0])


TEMPLATES = [
    ("a + b = c", 3, lambda a, b, c: (a + b, c), lambda a, b, c: rsub(radd(a, b), c)),
    ("a - b = c", 3, lambda a, b, c: (a - b, c), lambda a, b, c: rsub(rsub(a, b), c)),
    ("ab = c", 3, lambda a, b, c: (a * b, c), lambda a, b, c: rsub(rmul(a, b), c)),
    ("a/b = c", 3, lambda a, b, c: (a / b, c), lambda a, b, c: rsub(rdiv(a, b), c)),
    ("ab + c = d", 4, lambda a, b, c, d: (a * b + c, d), lambda a, b, c, d: rsub(radd(rmul(a, b), c), d)),
    ("ab - c = d", 4, lambda a, b, c, d: (a * b - c, d), lambda a, b, c, d: rsub(rsub(rmul(a, b), c), d)),
    ("abc = d", 4, lambda a, b, c, d: (a * b * c, d), lambda a, b, c, d: rsub(rmul(rmul(a, b), c), d)),
    ("ab/c = d", 4, lambda a, b, c, d: (a * b / c, d), lambda a, b, c, d: rsub(rdiv(rmul(a, b), c), d)),
    ("ab + cd = e", 5, lambda a, b, c, d, e: (a * b + c * d, e), lambda a, b, c, d, e: rsub(radd(rmul(a, b), rmul(c, d)), e)),
    ("ab - cd = e", 5, lambda a, b, c, d, e: (a * b - c * d, e), lambda a, b, c, d, e: rsub(rsub(rmul(a, b), rmul(c, d)), e)),
    ("ab/cd = e", 5, lambda a, b, c, d, e: (a * b / (c * d), e), lambda a, b, c, d, e: rsub(rdiv(rmul(a, b), rmul(c, d)), e)),
]

per_template = []
global_candidates = {}
for template, arity, build, build_rational in TEMPLATES:
    entries = {}
    filter_matches = 0
    for indexes in product(range(7), repeat=arity):
        if not is_candidate_identity(build_rational(*(RAT[index] for index in indexes))):
            continue
        filter_matches += 1
        lhs, rhs = build(*(ATOMS[index] for index in indexes))
        key = [sp.srepr(lhs), sp.srepr(rhs)]
        key_string = "|".join(key)
        assignment = {name: ATOM_NAMES[index] for name, index in zip(("a", "b", "c", "d", "e"), indexes)}
        entries.setdefault(key_string, {
            "template": template,
            "indexes": list(indexes),
            "assignment": assignment,
            "lhs": sp.sstr(lhs),
            "rhs": sp.sstr(rhs),
            "key": key,
        })
        global_candidates.setdefault(key_string, entries[key_string])
    per_template.append({
        "template": template,
        "raw_assignments": 7 ** arity,
        "filter_matches": filter_matches,
        "unique_candidates": len(entries),
        "entries": list(entries.values()),
    })

payload = {"global": list(global_candidates.values()), "per_template": per_template}
(ROOT / "candidate_catalog.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Built {len(global_candidates)} unique candidates across {len(per_template)} templates.")
print(f"Raw assignments: {sum(row['raw_assignments'] for row in per_template):,}")
for row in per_template:
    print(f"{row['template']}: {row['raw_assignments']:,} raw; {row['unique_candidates']} candidates")
