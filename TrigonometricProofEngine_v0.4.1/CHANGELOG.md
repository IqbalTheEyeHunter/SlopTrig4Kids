# v0.4.1

- Remove symbolic-oracle routes from prove_identity.
- Exclude target instances and audited transitive dependents before every search.
- Fail closed for unknown provenance; audit the F01–F12 dependency subset.
- Require replayable v4 certificates for saved proofs; reject legacy authority.
- Preserve algebra-only proofs, counterexamples, domain tracking and Windows UI.
- Add circularity regression tests and document reduced coverage.
