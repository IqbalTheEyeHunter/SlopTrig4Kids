# Trigonometric Proof Engine v0.5.1

**Release focus:** Malaysian KSSM trigonometric equation recognition, plus the restored independent geometric proof route for the foundational identity F08.

## 1. Download / run

This is the complete Windows source project. The executable must be built on Windows.

1. Extract the project folder.
2. Install Python 3.11 or newer.
3. Run `run_windows.bat`, or build the standalone executable with `build_windows.bat`.
4. The executable is created at `dist\\TrigonometricProofEngine.exe`.

Runtime use is offline. The build script installs dependencies during the build stage.

## 2. What is included in v0.5.1

### A. Restored independent F08 geometric proof

The F08 target is proved through the independently checked route:

**G01 → G03 → G04**

- **G01 — Pythagorean theorem by dissection:** four congruent right triangles tile a square; exact area additivity yields the non-trigonometric Pythagorean theorem.
- **G03 — Cartesian squared distance:** orthogonal projections give `OP**2 = u**2 + v**2`, including signed coordinates and axis cases.
- **G04 — Unit-circle substitution:** the point `P=(cos(theta), sin(theta))` has radius one, so G03 establishes `cos(theta)**2 + sin(theta)**2 = 1` for every real angle.

The engine recognises the same geometric relation when reversed, rearranged, multiplied by a non-trigonometric coefficient, or evaluated at a compound angle. The original domain ledger is preserved.

The geometric route runs before catalogue search and does not call `trigsimp`. F08 is the conclusion, never an assumed premise.

### B. Replayable geometric certificate

`geometry.py` implements `trigonometric-geometric-proof-certificate-v1`. The checker validates:

- The fixed G01 dissection schema and exact area-algebra consequence.
- G03 signed-coordinate projection and axis-case obligations.
- G04 unit-radius substitution without trigonometric simplification.
- The exact factorisation connecting the original LHS−RHS to the geometric relation.
- The original-domain ledger, dependency list, proof-node sequence and SHA-256 digest.
- Absence of F08/F09/F10 identity premises and open assumptions.

The explicit trust boundary is **AX.REAL, AX.EUCLID, AX.AREA and D.UNIT**. The checker validates this fixed proof schema relative to those foundations; it does not claim to formalise all Euclidean geometry from set-theoretic axioms.

### C. Circularity-safe theorem dependencies

F08 is no longer an unexplained root in the dependency manifest. Its dependency is `GEO.F08`, admitted only after the canonical G01→G03→G04 certificate successfully replays. F09–F12 can depend on F08 only after that replay. If geometric replay fails, those descendants fail closed.

Saved v0.5.1 geometric certificates are replayed before theorem-bank admission. Legacy v3 certificates remain untrusted; v4 symbolic certificates retain their existing replay path.

### D. Structural equation recognition

`recognition.py` implements deterministic structural matching for all 55 `EQREC-001` through `EQREC-055` classes in the bundled `knowledge/SKILL-2.md`.

The recogniser uses parsed expression trees, function/argument structure, variable roles, rational and radical structure, graph form, interval wording, parameter cues and task wording. It is not exact-string matching.

The recognition workspace accepts:

- One relation per line (equations or inequalities).
- Multiple relations for simultaneous systems or multipart tasks.
- Optional question wording and requested interval.
- Six trigonometric functions, `sqrt`, `abs`, paired absolute-value bars, `pi`, and numeric degree suffixes such as `30°`.

Recognition remains separate from proof and complete equation solving.

### E. Three bundled knowledge sources

1. `knowledge/SKILL.md` — the original six-function identity catalogue and proof reference.
2. `knowledge/SKILL-2.md` — Malaysian KSSM Form 5 recognition taxonomy and 55 EQREC classes.
3. `knowledge/V0.5_Proof_Knowledge_Handbook.md` — geometric, algebraic, analytic and equation-solving methods, plus proof-safety requirements.

The handbook's other geometric and analytic recipes remain documented knowledge unless a dedicated checker is enabled. The enabled new geometric proof route in this release is G01/G03/G04 for F08.

## 3. User interface

The desktop application has four tabs:

| Tab | Purpose |
|---|---|
| Proof Workspace | Prove identity claims, including the independent F08 geometric route |
| Equation Recognition | Recognise unfamiliar equation structures and receive method suggestions |
| Theorem Bank | Store previously established results under the certificate policy |
| Knowledge Base | Browse/search SKILL.md, SKILL-2.md and the v0.5 proof handbook |

For F08, the Proof Workspace report displays the geometric chain, trusted foundations, certificate schema and digest.

## 4. Verify an exported F08 certificate

```bash
python verify_certificate.py examples/F08_geometric_proof_certificate.json
```

The checker replays the schema and mathematical obligations. A `PROVED` status label or digest alone is never treated as proof authority.

## 5. Mathematical scope and boundaries

- Angles are represented internally in radians. Numeric degree notation such as `30°` is converted exactly.
- A recognition match is a candidate classification, not proof that the input is true or false.
- The recogniser is not a complete general trigonometric equation solver.
- Graph sketches and approximate roots do not constitute exact proof or complete solution certificates.
- The F08 GEO certificate is a checked proof relative to AX.REAL, AX.EUCLID, AX.AREA and D.UNIT.
- Other geometry/analysis recipes are recommendations until their proof rules are independently checked and implemented.

## 6. Project layout

```text
TrigonometricProofEngine_v0.5.1/
├── app.py
├── engine.py
├── geometry.py
├── recognition.py
├── verify_certificate.py
├── requirements.txt
├── run_windows.bat
├── build_windows.bat
├── README.md
├── CHANGELOG.md
├── TEST_RESULTS.txt
├── knowledge/
│   ├── SKILL.md
│   ├── SKILL-2.md
│   └── V0.5_Proof_Knowledge_Handbook.md
├── examples/
└── tests/
```

## 7. Tests

Run from the project folder. The suites are intentionally run independently so each can be validated in a fresh process:

```bash
python -m unittest tests.test_circularity -v
python -m unittest tests.test_engine -v
python -m unittest tests.test_geometry -v
python -m unittest tests.test_recognition -v
```

The test suites cover circularity protection, geometric certificate replay/tampering, the existing identity engine and all 55 EQREC recognition classes.
