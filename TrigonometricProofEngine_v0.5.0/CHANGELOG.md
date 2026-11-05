# Changelog

## v0.5.0

- Retain the v0.4.1 desktop UI and circularity-safe symbolic engine.
- Add `geometry.py` with a narrow GEO certificate checker for G01 → G03 → G04.
- Prove F08 from a non-trigonometric Euclidean dissection, Cartesian squared distance and signed unit-circle coordinates.
- Replace F08's former unexplained dependency root with a replayed `GEO.F08` foundation dependency.
- Permit F08 catalogue use in other proofs only after the canonical geometric certificate replays.
- Add replay support for saved v0.5 geometric certificates; reject tampered fields, wrong claims, changed domain ledgers and invalid digests.
- Add an offline `verify_certificate.py` command-line tool for exported F08 GEO certificates.
- Add Foundation Lab and v0.5 Handbook UI tabs.
- Bundle both the inherited SKILL identity database and the new v0.5 proof knowledge handbook.
- Add positive and adversarial geometric certificate regression tests.
- Explicitly document that G05–G30, M01–M20, AN01–AN10 and EQ01–EQ18 are documented knowledge, not all executable checkers in this release.

## v0.4.1

- Remove symbolic-oracle routes from `prove_identity`.
- Exclude target instances and audited transitive dependents before every search.
- Fail closed for unknown provenance; audit the F01–F12 dependency subset.
- Require replayable v4 certificates for saved proofs; reject legacy authority.
- Preserve algebra-only proofs, counterexamples, domain tracking and Windows UI.
- Add circularity regression tests and document reduced proof coverage.
