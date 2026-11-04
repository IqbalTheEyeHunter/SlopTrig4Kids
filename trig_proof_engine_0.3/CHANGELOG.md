# Changelog

## 0.3.0 — 2026-11-04

- Added catalogue-guided proof generation using 125 directly executable equality formulas extracted from the bundled `SKILL.md`.
- Added exact symbolic validation of each executable catalogue rule before it enters the rewrite search.
- Added bidirectional identity matching on subexpressions, with consistent variable substitution and target-directed rule ordering.
- Added explicit proof steps for each applied identity, including identity IDs, theorem provenance, direction, and domain conditions.
- Added separate algebraic factor, fraction-combination, and cancellation steps between identity applications.
- Added a default `Use full identity catalogue` strategy that combines bundled rules with user-supplied and saved identities.
- Added counterexample-first diagnosis for catalogue mode to avoid spending proof-search time on readily disproved claims.
- Improved domain-condition handling by simplifying substituted conditions and omitting nonzero numeric constants.
- Added proof-certificate provenance for catalogue identities and their individual applications.
- Expanded automated test coverage from 25 to 31 tests.

## 0.2.0 — 2026-11-04

- Added directed proof routes (LHS → RHS, RHS → LHS, both sides to common form, and the difference method).
- Added automatic comparison of successful proof routes and display of alternatives.
- Added recognised identity ID references from the bundled `SKILL.md` specification.
- Added transformation-by-transformation proof traces with symbolic equivalence checks.
- Added Markdown report and JSON transformation-certificate export.
- Added support for superscript fourth powers and `Ctrl + Enter` proof execution.
- Corrected identity catalogue parsing to include formulas containing inline code formatting; 136 indexed entries are loaded.

## 0.1.0

- Initial offline desktop prototype with safe expression parsing, symbolic verification, domain-condition reporting, counterexample search, and searchable skill reference.
