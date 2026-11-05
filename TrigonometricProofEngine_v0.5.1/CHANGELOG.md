# Changelog

## v0.5.1 — Restored geometric F08 proof + structural equation recognition

- Restore the independent F08 proof capability that was accidentally omitted from the first v0.5.1 package.
- Add `geometry.py` with the replayable `trigonometric-geometric-proof-certificate-v1` checker.
- Prove F08 through G01 (Pythagorean dissection) → G03 (Cartesian squared distance) → G04 (unit-circle substitution).
- Support reversed, rearranged, scaled and arbitrary-angle instances of the same geometric relation, while preserving original-domain restrictions.
- Run the GEO route before catalogue search; it does not call `trigsimp` and does not use F08/F09/F10 as premises.
- Change the audited dependency manifest so F08 depends on `GEO.F08`, which is admitted only after certificate replay; F09–F12 inherit this checked dependency.
- Add replay validation for saved v0.5.1 geometric theorem-bank certificates.
- Add the offline `verify_certificate.py` command-line checker.
- Retain `recognition.py` with structural recognition for all 55 EQREC classes from SKILL-2.md.
- Retain the Equation Recognition workspace and the Knowledge Base selector for all three knowledge sources.
- Update reports, README, dependency provenance and regression tests to distinguish GEO proof nodes from identity-catalogue IDs.
- Preserve the explicit trust boundary AX.REAL, AX.EUCLID, AX.AREA and D.UNIT; no claim of full set-theoretic Euclidean formalisation is made.

## Carried forward from v0.4.1

- Exclude open goals, equivalent variants and audited dependent theorems from proof search.
- Reject unknown dependency provenance and non-replayable legacy certificates.
- Preserve algebra-only proof routes, exact counterexample diagnostics, domain tracking and certificate export.
