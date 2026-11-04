# Changelog

## 0.3.1 — 2026-11-04

- Made Proof Workspace, Theorem Bank, and Identity Library vertically scrollable using dedicated canvas-backed page containers.
- Added mouse-wheel scrolling for Windows/macOS-style wheel events and Linux button 4/5 wheel events.
- Routed wheel input to inner report/library text widgets and theorem tables when the pointer is over them.
- Added an independent vertical scrollbar to the proof report so long derivations and alternative routes can be inspected.
- Automatically scrolls to the Proof Report after a proof or input/engine error is returned.
- Added a Back to inputs control in the report header.
- Adjusted the default window geometry and minimum size for smaller displays.
- Updated the proof-certificate engine version to 0.3.1.


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


## v0.4.0 — 2026-11-04

- Implemented bounded breadth-first search across the full validated identity catalogue.
- Searches LHS-to-RHS first and searches RHS-to-LHS if the first direction cannot establish the claim; each identity itself is available in both directions.
- Supports explicit multi-identity chains, including F09 → F03 for `1 + tan(x)^2 = 1/cos(x)^2`.
- Removed arbitrary variable-assignment fallback from catalogue rewriting; remaining variables must be inferred from the target pattern.
- Added variable-substitution metadata to proof steps, Markdown output, and JSON certificates.
- Added a DERIVATION CHAIN section to the desktop report.
