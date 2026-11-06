# Trigonometric Proof Engine v0.6.1

A Windows desktop proof assistant for identities involving the six elementary trigonometric functions. v0.6.1 is a report-generation patch: geometric F08 proofs now display the complete G01 → G03 → G04 mathematical derivation in both the desktop report and Markdown export. The v0.6.0 theorem-admission correction and training corpus are retained.

## Files

- `question-bank.md` — 255 proved entries from the eleven finite operation templates, plus three supplementary theorem-reuse questions (258 total entries).
- `proof-solutions.md` — checked derivations for every question-bank entry, including the parameterised identity proof and a rejected false near-miss.
- `V0.6_Proof_Knowledge_Handbook.md` — release-level mathematical and implementation policy.
- `knowledge/SKILL.md` — six-function identity catalogue and proof knowledge.
- `build_candidate_catalog.py` — exhaustive enumeration of the finite seven-atom candidate set.
- `generate_question_bank.py` / `render_question_bank.py` — proof replay and Markdown corpus generation.
- `candidate_catalog.json` — the finite candidate set used by the question-bank run.
- `candidate_proofs.json` — historical v0.6.0 engine results and certificates for the finite candidate set; retained unchanged by this report-only patch.
- `question_bank_generation_summary.json` — counts and per-template generation results.
- `archive/` — historical v0.5.1 question bank and v0.4.1 example reports, retained separately from the v0.6.0 training corpus.
- `examples/F08_geometric_proof_report_v0.6.1.txt` — sample desktop-format report showing every geometric proof step.
- `examples/F08_geometric_proof_report_v0.6.1.md` — sample Markdown export with the same geometric derivation.

## v0.6.1 report patch

### Explicit geometric proof steps

When the selected route is `GEO: G01 → G03 → G04`, the report now uses a dedicated geometric-proof layout instead of treating G01/G03/G04 as ordinary catalogue identity rewrites. It displays:

1. **G01 — Pythagorean theorem by dissection:** the four-triangle construction, area equation, expansion and cancellation yielding `a**2+b**2=c**2`.
2. **G03 — Cartesian squared distance:** the point `P=(u,v)`, perpendicular projections, and `OP**2=u**2+v**2`.
3. **G04 — Unit-circle substitution:** the arbitrary real angle, unit-circle point `P=(cos(theta),sin(theta))`, radius `OP=1`, and the substitution yielding the Pythagorean trigonometric identity.
4. **Goal matching:** the exact certificate multiplier shows why the requested LHS−RHS is zero.

The report also shows the certificate schema, checker, digest, replay status and trusted foundations. It no longer displays misleading statements such as “0 identity applications”, “No symbolic proof steps”, or catalogue identity references for geometric nodes. The Markdown export uses the same proof-step content. Non-geometric catalogue reports retain their existing identity-step layout.

The geometric checker/schema remains unchanged; v0.6.0 certificates remain replayable. New certificates identify the v0.6.1 engine version.

## v0.6.0 mathematical changes

### 1. Safe reuse of F08–F10

F08, F09 and F10 are no longer blocked merely because a different goal is an algebraic consequence of one of them. The goal-matching guard now blocks only direct instances, reversals, angle renamings, and nonzero constant-scaled/rearranged forms of the same theorem. A derived goal with a nonconstant multiplier may use the theorem as a premise.

- F08 itself is proved only through the replayed geometric certificate `G01 → G03 → G04`.
- F09 is derived from F08, F01 and F03.
- F10 is derived from F08, F02 and F04.
- F08/F09/F10 may then be reused for distinct goals, with transitive dependencies checked.
- Reverse F08 angle binding is permitted only when exactly one angle is shared by the source and target.
- Cycles, unknown dependencies, untrusted legacy certificates and self-premises remain rejected.

### 2. Algebraic preprocessing before theorem matching

A narrowly scoped preprocessing pass expands squared additive bases and factors by parameter groups. It is ordinary distributive/factor algebra, not a trigonometric simplifier. This exposes identities such as `sin(x)**2 + cos(x)**2` inside squared linear combinations, allowing an explicit F08 application.

### 3. Parameterised example

The corrected identity

`(p*cos(x)+q*sin(x))**2 + (p*sin(x)-q*cos(x))**2 = p**2+q**2`

is proved with the visible chain:

1. Expand both squares.
2. Factor by `p**2 + q**2`.
3. Apply F08.

The originally typed version with `p*cos(x)` in the second bracket is false and is explicitly rejected in `proof-solutions.md`.

## Regenerate the question bank

From this project directory, run:

```bash
python generate_question_bank.py
```

This rebuilds the finite candidate catalogue, reuses any cached proof results, checks for missing candidate proofs, and writes `question-bank.md` and `proof-solutions.md`. To discard the cache and replay all 156 candidates from scratch, run `python generate_question_bank.py --clean`.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Windows build

Run `build_windows.bat` on Windows with Python 3.11 or newer. The generated executable is `dist/TrigonometricProofEngine.exe`. The project is offline-capable at runtime.

## Proof trust boundary

The geometric F08 certificate is a narrow replay checker relative to `AX.REAL`, `AX.EUCLID`, `AX.AREA` and `D.UNIT`. Other catalogue proofs are explicit symbolic transformation records with audited dependencies and domain tracking. This is not a general-purpose kernel-verified formal theorem prover; an engine status is only as strong as the enabled proof rules and their stated foundations.
