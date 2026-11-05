# Trigonometric Proof Report

- **Engine version:** 0.5.1
- **Status:** PROVED
- **Selected route:** GEO: G01 → G03 → G04

## Claim

\[ \sin^{2}{\left(x \right)} + \cos^{2}{\left(x \right)} = 1 \]

## Original common-domain conditions

- No additional restrictions detected.

## Independent geometric proof chain

1. **G01 — Pythagorean theorem by dissection.** Four congruent right triangles tile a square of side `a+b`; the central square has side `c`. Exact area additivity gives `(a+b)^2 = 4(ab/2)+c^2`, hence `a^2+b^2=c^2`.
2. **G03 — Cartesian squared distance.** Orthogonal projections of `P=(u,v)` have lengths `|u|` and `|v|`. G01 gives `OP^2=u^2+v^2`, including negative coordinates and axis cases.
3. **G04 — Unit-circle substitution.** For arbitrary real angle `θ=x`, construct `P=(cos θ,sin θ)` with `OP=1`. G03 gives `cos^2 θ+sin^2 θ=1`.
4. **Goal matching.** The requested LHS−RHS is the exact non-trigonometric multiplier recorded in the certificate times the G04 relation. No F08/F09/F10 catalogue theorem is used as a premise.

### Explicit trusted foundations
- `AX.REAL`: ordered real arithmetic and real-valued angle expressions.
- `AX.EUCLID`: Euclidean incidence, perpendicular projections and congruence.
- `AX.AREA`: area additivity for the dissection.
- `D.UNIT`: the unit-circle point has signed coordinates `(cos θ,sin θ)` and radius one.

The certificate checker replays the fixed construction schema and exact algebraic obligations. This is a checked proof relative to these explicitly declared foundations, not a set-theoretic formalisation of all Euclidean geometry.

## Certificate replay

- **Schema:** `trigonometric-geometric-proof-certificate-v1`
- **Route:** `GEO: G01 → G03 → G04`
- **Certificate digest:** `d8195754444b913a9c4346fa457152772a8662587d2ca200b6d619ec03c3ac0b`
- **Replay status:** VERIFIED
- **Trigonometric identity premises:** none

## Conclusion

An independent geometric proof establishes the identity through G01 (Pythagorean dissection), G03 (Cartesian squared distance) and G04 (unit-circle substitution). The replayable GEO certificate passed. No trigonometric catalogue identity is used as a premise. The result is relative to the explicit trusted foundations AX.REAL, AX.EUCLID, AX.AREA and D.UNIT.

> Numerical sampling is used only to find counterexamples; it is never used to certify an identity.
