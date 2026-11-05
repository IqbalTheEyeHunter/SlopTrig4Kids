# v0.5 Knowledge Sources

The engine keeps two distinct knowledge databases rather than flattening every formula into an executable rule list.

1. `SKILL.md` — inherited six-function identity catalogue from v0.4.1. Catalogue membership is not proof authority. Only formulas whose dependency chains pass the engine's admission policy can be used in a proof.
2. `V0.5_Proof_Knowledge_Handbook.md` — geometric, algebraic/discrete, analytic and equation-solving knowledge, plus foundation profiles, dependency safety rules, proof-certificate requirements and the inherited reference corpus.

The v0.5 checker currently executes and replays the specific GEO certificate chain G01 → G03 → G04 for F08. Other handbook methods are documented knowledge and remain unavailable as automatic proof rules until their own typed checkers and acceptance tests are implemented.

Trusted GEO base used by the F08 certificate:
- AX.REAL — ordered real arithmetic and exact polynomial algebra.
- AX.EUCLID — Euclidean congruence, angle, perpendicularity and dissection-construction facts.
- AX.AREA — area additivity, square area and right-triangle area.
- D.UNIT — sine and cosine are defined as signed coordinates of the point on the unit circle.

The geometric certificate explicitly records these foundations. It does not use F08, F09, F10, or any trigonometric identity as a premise when proving F08.

3. `v0.5_manifest.json` — machine-readable inventory of enabled geometric certificate rules, documented-only methods, trusted foundations and F08 dependency policy.
