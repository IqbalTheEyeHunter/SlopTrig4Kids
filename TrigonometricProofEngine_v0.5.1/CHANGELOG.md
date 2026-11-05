# Changelog

## v0.5.1 — Structural equation recognition

- Add `recognition.py` with structural recognition for all 55 EQREC classes from SKILL-2.md.
- Add recognition of identity prompts, equation prompts, inequalities, graph equations, simultaneous relations, parameters, intervals, quadrant constraints and multipart “prove/hence solve” wording.
- Add a dedicated Equation Recognition workspace.
- Add a Knowledge Base selector for SKILL.md, SKILL-2.md and the v0.5 Proof Knowledge Handbook.
- Preserve unevaluated expression structure in the recognition parser so cofunction, special-angle and cancellation patterns are not erased before classification.
- Support `abs(...)`, paired `|...|` notation, and exact numeric degree suffixes such as `30°`.
- Preserve original denominator/radical domain restrictions in recognition reports.
- Keep recognition distinct from proof and complete equation solving.
- Retain the v0.4.1 circularity policy; F08 remains inconclusive without an independent geometric checker.

## Carried forward from v0.4.1

- Exclude open goals, equivalent variants and audited dependent theorems from proof search.
- Reject unknown dependency provenance and non-replayable legacy certificates.
- Preserve algebra-only proof routes, exact counterexample diagnostics, domain tracking and certificate export.
