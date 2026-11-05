# Trigonometric Proof Report

- **Engine version:** 0.5.0
- **Status:** PROVED
- **Selected route:** GEO: G01 → G03 → G04

## Claim

\[ \sin^{2}{\left(x \right)} + \cos^{2}{\left(x \right)} = 1 \]

## Original common-domain conditions

- No additional restrictions detected.

## Geometric proof chain

- **Route:** G01 → G03 → G04
- **Profile:** GEO
- **Catalogue identity premises:** none
- **Open assumptions:** none

## Proof / analysis steps

1. **G01 — Pythagorean theorem by dissection** — GEO
   - To: `a**2 + b**2 - c**2`
   - Reason: A square of side a+b is partitioned into four congruent right triangles and a central square of side c. Area additivity gives (a+b)^2 = 4(ab/2)+c^2; exact expansion yields a^2+b^2=c^2. The Euclidean construction and area facts are declared trusted foundations.
2. **G03 — Cartesian squared-distance relation** — GEO
   - To: `-r**2 + u**2 + v**2`
   - Reason: Orthogonal projections of P=(u,v) form a right triangle with legs |u| and |v|. G01 gives r^2=|u|^2+|v|^2=u^2+v^2; the axis cases are included.
3. **G04 — Unit-circle derivation of F08** — GEO
   - To: `sin(theta)**2 + cos(theta)**2 - 1`
   - Reason: For the arbitrary real angle θ=x, the unit-circle point has coordinates (cos(x), sin(x)) and radius 1. Substitution into G03 gives cos²(x)+sin²(x)=1. No quadrant restriction or division is used.
4. **Exact algebraic match to the requested claim** — GEO
   - From: `sin(x)**2 + cos(x)**2`
   - To: `1`
   - Reason: The formal difference is exactly 1·(sin²(x)+cos²(x)−1). The verified G04 relation therefore establishes the requested equality.

## Conclusion

An independently replayed Euclidean proof establishes the identity. The proof chain is G01 → G03 → G04; F08 is the conclusion, not a premise. Verified GEO certificate for F08 at angle x; formal coefficient 1. G01, G03 and G04 replayed with no trigonometric identity premises.

## Geometric certificate

- **Profile:** GEO
- **Certificate schema:** `trigonometric-geometric-proof-certificate-v1`
- **Proof chain:** G01 → G03 → G04 → GOAL
- **Trusted foundations:** AX.REAL, AX.EUCLID, AX.AREA, D.UNIT
- **Catalogue identity premises:** none
- **Certificate digest:** `ab576ad76fb8609116a1217ac9ca486d63d6896eb10e9dc428fe76f80ae38494`

The checker replays the geometric construction schema and exact algebraic obligations. The declared Euclidean and area foundations remain an explicit trust boundary.
> Numerical sampling is used only to find counterexamples; it is never used to certify an identity.
