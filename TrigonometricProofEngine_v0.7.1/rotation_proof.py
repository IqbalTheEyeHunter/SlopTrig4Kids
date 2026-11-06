"""Exact rational trigonometry over geometric rotation coordinates.

No trigsimp, expand_trig, fu, numerical sampling or catalogue theorem is used.
The certificate is replayed from the claim; its asserted status is never trusted.
"""
from __future__ import annotations
from functools import lru_cache
import sympy as sp
import copy
from geometry import build_f08_geometric_certificate, verify_geometric_certificate

SCHEMA = 'trigonometric-rotation-ring-certificate-v1'
TRIG = (sp.sin, sp.cos, sp.tan, sp.cot, sp.sec, sp.csc)
FOUNDATIONS = {
    'D.UNIT': 'sin(t), cos(t) are the coordinates of the point at oriented angle t on the unit circle.',
    'G.ROT': 'An oriented Euclidean rotation is linear, takes (1,0) to (cos(t),sin(t)), and takes (0,1) to (-sin(t),cos(t)). Composing rotations adds their oriented angles.',
    'G.SPECIAL': 'The positive coordinates at pi/4 and pi/6 follow from isosceles-right and equilateral triangles; quadrants determine signs.',
    'G.CIRCLE': 'G01 -> G03 -> G04 is replayed using the existing geometric checker.',
    'AX.REAL': 'Exact real-field arithmetic and polynomial ideal reduction.'
}
DERIVATION = [
    'The two columns of R(a) are (cos(a),sin(a)) and (-sin(a),cos(a)).',
    'Apply R(a) to (cos(b),sin(b)): its coordinates are (cos(a)*cos(b)-sin(a)*sin(b), sin(a)*cos(b)+cos(a)*sin(b)).',
    'By rotation composition this point has angle a+b. Thus the two addition formulas follow from geometry, without a catalogue identity.',
    'Repeated composition gives integer multiples. R(-a)=R(a)^T gives negative multiples.',
    'Choose each base angle as variable / LCM(coefficient denominators). This covers half-angles without a tangent substitution or extra division.',
    'Replace tan, cot, sec, csc by their coordinate definitions on the ORIGINAL common domain.',
    'Cross-multiply the rational forms on that domain and exhibit the numerator as a sum of polynomial multiples of circle relations.'
]

class Unsupported(ValueError):
    pass


def mul(p, q):
    c, s = p; d, t = q
    return sp.expand(c*d-s*t), sp.expand(s*d+c*t)


def power(p, n):
    if abs(n) > 24:
        raise Unsupported('Angle multiplier exceeds 24')
    if n < 0:
        p, n = (p[0], -p[1]), -n
    out = (sp.S.One, sp.S.Zero)
    for _ in range(n):
        out = mul(out, p)
    return out


def special(q):
    # pi/12 = pi/4 - pi/6; only exact radicals and rotation multiplication.
    k = q * 12
    if not k.is_Integer:
        raise Unsupported('Constant shift must be an integer multiple of pi/12')
    quarter = (sp.sqrt(2)/2, sp.sqrt(2)/2)
    minus_sixth = (sp.sqrt(3)/2, -sp.Rational(1,2))
    return power(mul(quarter, minus_sixth), int(k) % 24)


@lru_cache(maxsize=1)
def circle_foundation():
    from engine import parse_expression
    a, b = parse_expression('sin(t)**2+cos(t)**2'), sp.S.One
    cert = build_f08_geometric_certificate(a, b, [])
    ok, why = verify_geometric_certificate(cert, parse_expression, a, b, [])
    if not ok:
        raise Unsupported(why)
    return cert


def build_certificate(lhs, rhs, domain):
    """Return a deterministic witness, or None for false/unsupported goals.

    Symbols outside trig functions are exact coefficient parameters. Supported
    trig arguments are rational affine combinations of real symbols and pi.
    All symbolic powers must be integers (no unsafe square-root branch rules).
    """
    try:
        return _build(lhs, rhs, domain)
    except (Unsupported, sp.PolynomialError, ValueError, TypeError, ZeroDivisionError):
        return None


def _build(lhs, rhs, domain):
    if any(e.has(sp.Float, sp.zoo, sp.nan, sp.oo, -sp.oo) for e in (lhs, rhs)):
        raise Unsupported('Exact finite expressions required')
    if sum(sp.count_ops(e) for e in (lhs, rhs)) > 350:
        raise Unsupported('Expression operation limit exceeded')
    atoms = sorted(lhs.atoms(*TRIG) | rhs.atoms(*TRIG), key=sp.default_sort_key)
    if not atoms or len(atoms) > 48:
        raise Unsupported('Requires 1..48 trig atoms')
    variables = sorted(set().union(*(a.args[0].free_symbols for a in atoms)), key=str)
    if not variables or len(variables) > 4:
        raise Unsupported('Requires 1..4 base variables')
    scales = {v: 1 for v in variables}
    angle_parts = {}
    for atom in atoms:
        angle = sp.expand(atom.args[0])
        coefficients = [angle.coeff(v) for v in variables]
        rest = sp.expand(angle - sum((v*c for v,c in zip(variables,coefficients)), sp.S.Zero))
        q = sp.cancel(rest/sp.pi)
        if not all(c.is_Rational for c in coefficients) or not q.is_Rational:
            raise Unsupported('Non-affine argument')
        for v,c in zip(variables, coefficients):
            scales[v] = int(sp.ilcm(scales[v], c.q))
            if scales[v] > 120:
                raise Unsupported('Base denominator exceeds 120')
        angle_parts[atom] = coefficients, q
    # Dummy objects cannot collide with user parameter names.
    pairs = {v: (sp.Dummy('C'+str(i)), sp.Dummy('S'+str(i))) for i,v in enumerate(variables)}
    generators = tuple(z for v in variables for z in reversed(pairs[v]))
    relations = [pairs[v][0]**2+pairs[v][1]**2-1 for v in variables]
    basis = sp.groebner(relations, *generators, domain='EX')
    replacements, expansions = {}, []
    for atom in atoms:
        coeffs,q = angle_parts[atom]
        pair = special(q)
        for v,c in zip(variables,coeffs):
            pair = mul(pair, power(pairs[v], int(c*scales[v])))
        c,s = pair
        replacement = {sp.sin: lambda:s, sp.cos:lambda:c,
                       sp.tan:lambda:s/c, sp.cot:lambda:c/s,
                       sp.sec:lambda:1/c, sp.csc:lambda:1/s}[atom.func]()
        replacements[atom] = replacement
        expansions.append((atom, replacement))
    left, right = lhs.xreplace(replacements), rhs.xreplace(replacements)
    if left.has(*TRIG) or right.has(*TRIG):
        raise Unsupported('Nested trigonometry')
    for expr in (left,right):
        for node in sp.preorder_traversal(expr):
            if node.is_Pow and node.base.free_symbols and not node.exp.is_Integer:
                raise Unsupported('Non-rational symbolic power')
    ln,ld = sp.fraction(sp.together(left)); rn,rd = sp.fraction(sp.together(right))
    numerator = sp.expand(ln*rd-rn*ld)
    if sp.count_ops(numerator) > 15000:
        raise Unsupported('Polynomial expansion limit exceeded')
    # An identically vanishing denominator is not a nonempty-domain proof.
    if basis.reduce(sp.expand(ld))[1] == 0 or basis.reduce(sp.expand(rd))[1] == 0:
        raise Unsupported('Identically zero denominator')
    quotients, remainder = basis.reduce(numerator)
    if remainder != 0:
        return None
    gs = [g.as_expr() for g in basis.polys]
    if sp.expand(numerator-sum((q*g for q,g in zip(quotients,gs)),sp.S.Zero)) != 0:
        raise Unsupported('Polynomial witness failed')
    geo = circle_foundation()
    # Stable printed names: Dummy internal indices must never enter a certificate.
    prefix = 'coord_'
    names = {str(v) for v in lhs.free_symbols | rhs.free_symbols}
    while any(prefix+str(z).lstrip('_') in names for z in generators):
        prefix = '_' + prefix
    stable = {z:sp.Symbol(prefix+str(z).lstrip('_')) for z in generators}
    def text(expr):
        return sp.sstr(expr.xreplace(stable))
    return {
        'schema': SCHEMA, 'engine_version':'0.7.1', 'status':'PROVED',
        'claim': {'lhs':sp.sstr(lhs), 'rhs':sp.sstr(rhs)},
        'domain_conditions':list(domain), 'trusted_foundations':dict(FOUNDATIONS),
        'foundation_derivation':list(DERIVATION),
        'circle_certificate':copy.deepcopy(geo),
        'base_angles':[{'variable':str(v), 'angle':sp.sstr(v/scales[v]),
                        'cosine':text(pairs[v][0]), 'sine':text(pairs[v][1])} for v in variables],
        'angle_expansions':[{'from':sp.sstr(a),'to':text(b)} for a,b in expansions],
        'rational_forms':{'lhs':text(left),'rhs':text(right)},
        'denominators':[text(ld),text(rd)],
        'cross_multiplied_numerator':text(numerator),
        'circle_relations':[text(g) for g in gs],
        'quotients':[text(q) for q in quotients], 'remainder':'0',
        'certificate_note':'Replayable exact polynomial witness relative to the listed geometric foundations; not a Lean/Coq proof object. Original domain restrictions remain in force.'
    }


def verify_certificate(cert, lhs, rhs, domain):
    """Reconstruct every expansion and witness; reject altered claims or ledgers."""
    if not isinstance(cert,dict) or cert.get('schema') != SCHEMA:
        return False, 'Wrong schema'
    expected = build_certificate(lhs,rhs,domain)
    core = dict(cert)
    if core.get('engine_version') not in ('0.7.0', '0.7.1'):
        return False, 'Unsupported engine version'
    core['engine_version']='0.7.1'
    student_proof = core.pop('student_proof', None)
    if 'student_proof' in cert:
        from school_algebra import verify_trace
        if not verify_trace(student_proof, lhs, rhs):
            return False, 'Student algebraic explanation did not replay'
    if expected is not None and isinstance(core.get('circle_certificate'),dict):
        from engine import parse_expression
        geo_lhs=parse_expression('sin(t)**2+cos(t)**2')
        geo_ok,_=verify_geometric_certificate(core['circle_certificate'],parse_expression,geo_lhs,sp.S.One,[])
        if not geo_ok:
            return False, 'Geometric foundation did not replay'
        core['circle_certificate']=expected['circle_certificate']
    if expected is None or core != expected:
        return False, 'Claim, foundations, domain or polynomial witness did not replay'
    return True, 'Exact rotation expansions and polynomial witness replayed'


def report_lines(cert):
    lines = ['ROTATION AND POLYNOMIAL PROOF', '']
    lines.extend(f'{i}. {line}' for i,line in enumerate(DERIVATION,1))
    lines += ['', 'BASE ANGLES']
    lines.extend(f"{a['cosine']} = cos({a['angle']}), {a['sine']} = sin({a['angle']})" for a in cert['base_angles'])
    lines += ['', 'EXACT ANGLE / DEFINITION EXPANSIONS']
    lines.extend(f"{a['from']} = {a['to']}" for a in cert['angle_expansions'])
    lines += ['', 'RATIONAL FORMS', 'LHS = '+cert['rational_forms']['lhs'], 'RHS = '+cert['rational_forms']['rhs'],
              '', 'CROSS-MULTIPLICATION ON THE ORIGINAL DOMAIN', 'N = '+cert['cross_multiplied_numerator'],
              'Original denominators stay nonzero. No new restriction is imposed.', '', 'POLYNOMIAL WITNESS']
    terms = [f'({q}) * ({g})' for q,g in zip(cert['quotients'],cert['circle_relations']) if q != '0']
    lines += ['N = '+(' + '.join(terms) if terms else '0'), 'Each circle relation is zero by the replayed geometric foundation.',
              'Remainder = 0; hence LHS - RHS = 0.', '', 'CERTIFICATE REPLAY: VERIFIED',
              'No catalogue target or dependent identity is used as a premise.',
              'Foundations: '+', '.join(FOUNDATIONS), cert['certificate_note']]
    return lines
