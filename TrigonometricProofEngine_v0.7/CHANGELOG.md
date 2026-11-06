# v0.7.0 — 2026-11-06

- Added a general, replayable rotation-coordinate and polynomial proof route for compound, multiple and rational half-angles.
- Solves all fourteen recovered exercises in Automatic and Full Catalogue modes without hard-coded answers or unaudited angle catalogue rules.
- Preserves original denominator restrictions; uses exact decimal literals.
- Adds certificate replay, theorem-bank compatibility, standalone verification, and complete generated reports for all fourteen exercises.
- Adds the fourteen exercises to the beginning of the desktop Load example sequence.
- Keeps independent geometric F08 proofs and circularity guards; preserves the historical question bank.
- Extends both batch runners and question-bank rendering to recognize the new certificate schema.
- Includes regression tests for false near-misses, generic identities, malformed certificates, exact input and domain safety.

# Changelog

## v0.6.1 — Explicit geometric proof reporting

- Add a dedicated geometric proof section to the desktop report for the G01 → G03 → G04 route.
- Display G01's four-congruent-triangle dissection, area equality, expansion and derivation of `a**2+b**2=c**2`.
- Display G03's Cartesian point, perpendicular projections and squared-distance derivation.
- Display G04's arbitrary-angle unit-circle construction, radius-one fact and substitution into G03.
- Display the exact goal multiplier and show how the requested LHS−RHS reduces to zero.
- Add certificate replay metadata and the explicit trusted-foundation list to the report.
- Remove misleading generic identity-application counts, empty symbolic-step notices and identity database references from geometric reports.
- Apply the same geometric proof-step presentation to Markdown exports.
- Keep ordinary catalogue proof reports unchanged.
- Keep the geometric certificate schema and checker semantics unchanged; preserve replay compatibility with v0.6.0 certificates.
- Add regression tests for desktop and Markdown report content, misleading-section suppression, non-geometric report compatibility and legacy certificate replay.

## v0.6.0 — Theorem reuse and training bank


- Fix theorem-goal blocking so F08/F09/F10 can be reused for genuinely different claims.
- Keep direct self-goals, angle-renamed/reversed variants and nonzero constant-scaled/rearranged instances excluded from their own premise set.
- Restrict the independent geometric F08 route to F08-shaped goals; non-F08 goals use F08 as an explicit catalogue premise when needed.
- Add targeted expansion/factorisation of squared additive expressions before theorem matching.
- Prove the corrected orthogonal linear-combination identity with an explicit F08 step.
- Add acceptance examples demonstrating F08, F09 and F10 reuse for distinct goals.
- Reject the originally typed parameter identity as false by counterexample.
- Split training data into `question-bank.md` (questions only) and `proof-solutions.md` (checked derivations).
- Rebuild the question bank from v0.6.0 proof results; only current `PROVED` entries are retained.
- Add a narrowly scoped reverse-F08 angle-binding rule: when a literal `1` is matched in reverse and exactly one angle is shared between source and target, bind that unique angle rather than guessing.
- Restore two valid legacy question-bank entries using F08 in reverse, bringing the finite bank to 255 template entries (150 unique proved claims) plus three supplementary theorem-reuse examples.
- Preserve all 146 unique v0.5.1 proved claims and add four additional unique proved claims; no prior proved claim was lost in the v0.6.0 bank.
