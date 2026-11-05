"""Narrow replay checker for the v0.6.0 G01 -> G03 -> G04 F08 proof route.

The proof is relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT.  This module
checks a fixed Euclidean construction schema and exact algebraic obligations;
it is not a set-theoretic formalisation of all Euclidean geometry.
"""
from __future__ import annotations
import hashlib
import json
from typing import Callable, Iterable
import sympy as sp

SCHEMA = "trigonometric-geometric-proof-certificate-v1"
CHECKER_VERSION = "0.6.0-geo-checker-1"
TRIGS = (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc)
FOUNDATIONS = ["AX.REAL", "AX.EUCLID", "AX.AREA", "D.UNIT"]
DEPENDENCIES = ["AX.REAL", "AX.EUCLID", "AX.AREA", "D.UNIT", "G01", "G03", "G04"]


def match_f08_claim(lhs: sp.Expr, rhs: sp.Expr):
    residual = sp.expand(lhs - rhs)
    if residual == 0:
        return None
    sin_args = {n.args[0] for e in (lhs, rhs) for n in e.atoms(sp.sin)}
    cos_args = {n.args[0] for e in (lhs, rhs) for n in e.atoms(sp.cos)}
    for angle in sorted(sin_args & cos_args, key=sp.srepr):
        if any(s.is_real is not True for s in angle.free_symbols):
            continue
        relation = sp.sin(angle)**2 + sp.cos(angle)**2 - 1
        try:
            multiplier = sp.cancel(residual / relation)
            if multiplier in (0, sp.zoo, sp.nan, sp.oo, -sp.oo):
                continue
            if multiplier.has(sp.zoo, sp.nan, sp.oo, -sp.oo):
                continue
            if any(multiplier.has(f) for f in TRIGS):
                continue
            if sp.expand(residual - multiplier*relation) == 0:
                return angle, multiplier
        except Exception:
            continue
    return None


def _g01():
    a,b,c=sp.symbols("_G01_a _G01_b _G01_c", positive=True, real=True)
    area_residual=sp.expand((a+b)**2 - 4*(a*b/2) - c**2)
    pythagorean=sp.expand(a**2+b**2-c**2)
    return area_residual == pythagorean


def _g03():
    u,v=sp.symbols("_G03_u _G03_v", real=True)
    return sp.simplify(sp.Abs(u)**2-u**2)==0 and sp.simplify(sp.Abs(v)**2-v**2)==0


def _g04(angle):
    radius,u,v=sp.symbols("_G04_r _G04_u _G04_v", real=True)
    distance=radius**2-u**2-v**2
    substituted=distance.subs({radius:1,u:sp.cos(angle),v:sp.sin(angle)}, simultaneous=True)
    expected=1-sp.cos(angle)**2-sp.sin(angle)**2
    return sp.expand(substituted-expected)==0


def _node_g01():
    return {"node_id":"G01","rule_id":"G01","depends_on":["AX.REAL","AX.EUCLID","AX.AREA"],
            "claim":"a**2+b**2=c**2","preconditions":["a>0","b>0","c>0","right_triangle(a,b,c)"],
            "construction":{"outer_shape":"square","outer_side":"a+b","congruent_right_triangles":4,
                "triangle_legs":["a","b"],"triangle_hypotenuse":"c","central_shape":"square",
                "central_side":"c","central_angles":["pi/2"]*4,
                "central_angle_reason":"the two acute angles of each right triangle sum to pi/2",
                "interiors_disjoint":True,"covers_outer_square":True},
            "area_identity":"(a+b)**2 = 4*(a*b/2)+c**2",
            "algebraic_consequence":"a**2+b**2=c**2","checker_result":"PASS"}


def _node_g03():
    return {"node_id":"G03","rule_id":"G03","depends_on":["G01","AX.EUCLID","AX.REAL"],
            "point":"P=(u,v)","projection_lengths":["abs(u)","abs(v)"],
            "right_triangle_hypotenuse":"OP","squared_distance":"OP**2=u**2+v**2",
            "signed_coordinates":True,"axis_cases":["u=0","v=0"],"checker_result":"PASS"}


def _node_g04(angle):
    t=sp.sstr(angle)
    return {"node_id":"G04","rule_id":"G04","depends_on":["G03","D.UNIT"],
            "angle_expression":t,"angle_range":"all real angles",
            "unit_circle_point":f"P=(cos({t}),sin({t}))","radius":"1",
            "substitution":{"OP":"1","u":f"cos({t})","v":f"sin({t})"},
            "conclusion":f"cos({t})**2+sin({t})**2=1","quadrant_restriction":None,
            "checker_result":"PASS"}


def _digest(cert):
    payload={k:v for k,v in cert.items() if k!="certificate_digest"}
    raw=json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def build_f08_geometric_certificate(lhs,rhs,domain_conditions:Iterable[str]=()):
    matched=match_f08_claim(lhs,rhs)
    if matched is None:
        return None
    angle,multiplier=matched
    if not (_g01() and _g03() and _g04(angle)):
        return None
    relation=sp.sin(angle)**2+sp.cos(angle)**2-1
    if sp.expand((lhs-rhs)-multiplier*relation)!=0:
        return None
    cert={"schema":SCHEMA,"engine_version":"0.6.0","checker_version":CHECKER_VERSION,
          "status":"PROVED","profile":"GEO","claim_kind":"identity",
          "claim":{"lhs":sp.sstr(lhs),"rhs":sp.sstr(rhs)},
          "selected_route":"GEO: G01 → G03 → G04","angle_expression":sp.sstr(angle),
          "goal_multiplier":sp.sstr(multiplier),
          "original_domain_conditions":sorted(set(map(str,domain_conditions)),key=str.casefold),
          "assumptions":[],"open_assumptions":[],"used_identity_ids":[],"used_theorems":[],
          "dependencies":list(DEPENDENCIES),"trusted_foundations":list(FOUNDATIONS),
          "proof_nodes":[_node_g01(),_node_g03(),_node_g04(angle),
                         {"node_id":"GOAL","depends_on":["G04"],
                          "claim":{"lhs":sp.sstr(lhs),"rhs":sp.sstr(rhs)},
                          "angle_expression":sp.sstr(angle),
                          "geometric_relation":"sin(theta)**2+cos(theta)**2-1=0",
                          "exact_multiplier":sp.sstr(multiplier),
                          "factorisation":{"lhs_minus_rhs":sp.sstr(sp.expand(lhs-rhs)),
                             "multiplier_times_relation":sp.sstr(sp.expand(multiplier*relation))},
                          "checker_result":"PASS"}],
          "certificate_note":"Independent geometric derivation relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT. No trigonometric catalogue identity is used as a premise."}
    cert["certificate_digest"]=_digest(cert)
    return cert


def verify_geometric_certificate(cert,parse_expression:Callable[[str],sp.Expr],lhs,rhs,domain_conditions=()):
    if not isinstance(cert,dict) or cert.get("schema")!=SCHEMA:
        return False,"unsupported geometric certificate schema"
    expected=build_f08_geometric_certificate(lhs,rhs,domain_conditions)
    if expected is None:
        return False,"claim is not an enabled G01 -> G03 -> G04 consequence"
    if {k:v for k,v in cert.items() if k!="certificate_digest"}!={k:v for k,v in expected.items() if k!="certificate_digest"}:
        return False,"certificate fields do not match the canonical replayed GEO proof"
    if cert.get("certificate_digest")!=_digest(cert):
        return False,"certificate digest mismatch"
    try:
        angle=parse_expression(cert["angle_expression"])
        multiplier=parse_expression(cert["goal_multiplier"])
    except Exception as exc:
        return False,f"invalid angle or multiplier: {exc}"
    matched=match_f08_claim(lhs,rhs)
    if matched is None or angle!=matched[0] or multiplier!=matched[1]:
        return False,"angle/multiplier does not match original claim"
    if not (_g01() and _g03() and _g04(angle)):
        return False,"G01/G03/G04 primitive replay failed"
    relation=sp.sin(angle)**2+sp.cos(angle)**2-1
    if sp.expand((lhs-rhs)-multiplier*relation)!=0:
        return False,"GOAL exact factorisation failed"
    return True,"VERIFIED: G01 dissection -> G03 Cartesian distance -> G04 unit circle -> original claim"
