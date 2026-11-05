# Trigonometric Proof Engine v0.6.0

A Windows desktop proof assistant for identities involving the six elementary trigonometric functions. This release includes the v0.6 theorem-admission correction, a question-only training bank, and a separate companion file containing the checked proof solutions.

## Files

- `question-bank.md` — 255 proved entries from the eleven finite operation templates, plus three supplementary theorem-reuse questions (258 total entries).
- `proof-solutions.md` — checked derivations for every question-bank entry, including the parameterised identity proof and a rejected false near-miss.
- `V0.6_Proof_Knowledge_Handbook.md` — release-level mathematical and implementation policy.
- `knowledge/SKILL.md` — six-function identity catalogue and proof knowledge.
- `build_candidate_catalog.py` — exhaustive enumeration of the finite seven-atom candidate set.
- `generate_question_bank.py` / `render_question_bank.py` — proof replay and Markdown corpus generation.
- `candidate_catalog.json` — the finite candidate set used by the question-bank run.
- `candidate_proofs.json` — v0.6.0 engine results and certificates for the finite candidate set.
- `question_bank_generation_summary.json` — counts and per-template generation results.
- `archive/` — historical v0.5.1 question bank and v0.4.1 example reports, retained separately from current v0.6.0 artifacts.

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
