# Trigonometric Proof Report

- **Engine version:** 0.6.1
- **Status:** PROVED
- **Selected route:** GEO: G01 → G03 → G04

## Claim

\[ \sin^{2}{\left(x \right)} + \cos^{2}{\left(x \right)} = 1 \]

## Original common-domain conditions

- No additional restrictions detected.

## Geometric proof steps

1. **G01 — Pythagorean theorem by geometric dissection**
   - Let a right triangle have perpendicular legs a and b, and hypotenuse c.
   - Arrange four congruent copies inside a square whose side is a+b. Their hypotenuses form the four sides of a central square of side c.
   - Each central angle is 90° because the two acute angles of a right triangle sum to 90°.
   - Area of the outer square = area of four triangles + area of the central square:
   - (a+b)² = 4(ab/2) + c².
   - Expand: a² + 2ab + b² = 2ab + c².
   - Subtract 2ab from both sides: a² + b² = c².
   - Therefore G01 establishes the Pythagorean theorem from Euclidean geometry and area additivity.

2. **G03 — Cartesian squared-distance theorem**
   - Take an arbitrary Cartesian point P=(u,v), with O=(0,0).
   - Perpendicular projections onto the coordinate axes have lengths |u| and |v|; OP is the hypotenuse of the resulting right triangle.
   - Apply G01: OP² = |u|² + |v|² = u² + v².
   - The same formula holds on either axis (u=0 or v=0) by direct evaluation.

3. **G04 — Unit-circle substitution**
   - Let θ = x be any real angle and choose the unit-circle point P=(cos(x), sin(x)).
   - By D.UNIT, the point has radius OP=1 and signed Cartesian coordinates u=cos(x), v=sin(x).
   - Apply G03: OP² = u² + v².
   - Substitute: 1² = cos²(x) + sin²(x).
   - Hence cos²(x) + sin²(x) = 1, for every real angle x.

4. **Final step — Match the geometric theorem to the requested claim**
   - The certificate's exact factorisation is: LHS − RHS = sin(x)**2 + cos(x)**2 - 1.
   - This residual equals (1) × (cos²(x) + sin²(x) − 1).
   - By G04, the parenthesised expression is zero; therefore LHS − RHS = (1)×0 = 0.
   - Thus sin(x)**2 + cos(x)**2 = 1 on the original common domain.

## Certificate replay

- **Schema:** `trigonometric-geometric-proof-certificate-v1`
- **Checker:** `0.6.0-geo-checker-1`
- **Digest:** `56547fd1b3faab6f4050265e0f560e5cfd93c8fe2f3e0979d004a1fcd8f3811c`
- **Replay:** VERIFIED
- **Trigonometric catalogue premises:** none
- **Trusted foundations:** AX.REAL, AX.EUCLID, AX.AREA, D.UNIT

## Conclusion

The independently replayed geometric certificate establishes the requested equality on the original common domain. The conclusion follows from G01 → G03 → G04, relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT. No F08/F09/F10 catalogue identity is assumed as a premise.

> Numerical sampling is used only to find counterexamples; it is never used to certify an identity.
