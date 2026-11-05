# Trigonometric Proof Engine v0.4.1 — circularity safety patch

Extract this project and run `run_windows.bat`, or build the executable using
`build_windows.bat`. Replace the old project files together; do not keep the old
engine.py beside the updated interface. Windows executable building is unchanged.

## What changed

All proof modes use explicit identity rewrites and algebraic steps. Opaque SymPy
simplification is retained only as a diagnostic/simplify tool, never a proof route.
The target is excluded by formula, including reversal, variable substitution,
constant scaling and algebraic rearrangement. Audited transitive dependencies are
excluded too. Unknown dependency information fails closed.

F08 now returns INCONCLUSIVE when asked to prove itself. F09–F12 cannot be used
to get around this because they depend on F08. This patch does not implement a
geometric proof of F08. As an established theorem for OTHER claims, F08's stated
external foundation is the unit-circle argument in knowledge/SKILL.md B01.
F01–F04 are external definitions. F05–F07 and F09–F12 have audited dependencies.
All other catalogue entries remain browsable but are unavailable as proof rules
until their dependencies are audited. This deliberately reduces proof coverage.

Uncertified supplied premises and v3 saved certificates are not proof authority.
New v4 certificates are recursively checked and their admitted premises replayed;
unknown dependencies and cycles are rejected. Symbolic truth alone is insufficient.
Certificates describe the trusted foundations and dependency manifest. They are
still transformation records, not independently kernel-verified proof objects.
The existing strategy selector is retained for compatibility; heuristic labels
such as Fu now use the same restricted explicit search. LHS/RHS direction is
respected. Search bounds can return INCONCLUSIVE for an independently provable claim.

## Validation

Run `python -m unittest discover -s tests -v`.
The original 33-test suite initially had 16 failures because it expected circular,
opaque or unaudited proofs and the old certificate schema. Those expectations were
updated to require INCONCLUSIVE; the original assertions are preserved in
`tests/legacy_v040_expectations.txt`. Ten additional regression tests cover all
proof modes, variants, dependency cycles, old certificates, valid chaining and
certificate reuse. See TEST_RESULTS.txt for the actual run.

