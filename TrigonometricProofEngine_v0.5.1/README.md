# Trigonometric Proof Engine v0.5.1

**Release focus:** structural recognition of unfamiliar trigonometric equations and proof prompts, while preserving the v0.4.1 proof-safety controls.

## 1. Download / run

This is the complete Windows source project. The executable must be built on Windows.

1. Extract the project folder.
2. Install Python 3.11 or newer.
3. Run `run_windows.bat`, or build the standalone executable with `build_windows.bat`.
4. The executable is created at `dist\TrigonometricProofEngine.exe`.

Runtime use is offline. The build script downloads/installs dependencies during the build stage.

## 2. What is new in v0.5.1

### A. Structural equation recognition

`recognition.py` implements deterministic structural matching for all 55 `EQREC-001` through `EQREC-055` classes in the bundled `knowledge/SKILL-2.md`.

Recognition is based on parsed expression trees, function/argument structure, variable roles, rational and radical structure, graph form, interval wording, parameter cues and task wording. It is not exact-string matching.

The recognition workspace accepts:

- One relation per line (equations or inequalities).
- Multiple relations for simultaneous systems or multipart tasks.
- Optional question wording (e.g. “solve”, “prove and hence solve”, “state the number of solutions”, “in quadrant II”).
- An optional requested interval.
- Six trigonometric functions, `sqrt`, `abs`, paired absolute-value bars, `pi`, and numeric degree suffixes such as `30°`.

The report provides candidate EQREC classes, KSSM/supporting/extension labels, DSKP links, method references from the v0.5 handbook, detected variables, original-domain restrictions and cautions.

### B. Recognition is not solving

v0.5.1 identifies the problem family and recommends candidate methods. It does **not** implement a complete general trigonometric equation solver. It does not report `SOLVED_COMPLETE` merely because an equation was recognised.

### C. Three bundled knowledge sources

The Knowledge Base tab exposes all three documents:

1. `knowledge/SKILL.md` — the original six-function identity catalogue and proof reference.
2. `knowledge/SKILL-2.md` — Malaysian KSSM Form 5 recognition taxonomy and 55 EQREC classes.
3. `knowledge/V0.5_Proof_Knowledge_Handbook.md` — geometric, algebraic, analytic and equation-solving methods, plus proof-safety requirements.

The original knowledge files are bundled as references. The v0.5.1 recogniser implements the EQREC routing map; it does not claim that every recipe in the handbook is an executable inference rule.

### D. Existing proof safeguards retained

The identity-proof engine is carried forward from v0.4.1. Its circularity protections remain active:

- The target and its equivalent variants are excluded as unproved premises.
- Audited transitive dependencies are excluded when they depend on the open target.
- Unknown provenance fails closed.
- Legacy certificate formats cannot bypass replay checks.
- Numerical sampling may find counterexamples but cannot certify identities.
- Original denominator conditions remain recorded after cancellation.

In particular, `sin(x)**2 + cos(x)**2 = 1` remains `INCONCLUSIVE` in the current proof engine when no independent geometric certificate checker is enabled. The geometric derivation in the v0.5 handbook is documented knowledge, not an implemented geometric kernel.

## 3. User interface

The desktop application has four tabs:

| Tab | Purpose |
|---|---|
| Proof Workspace | Prove or investigate identity claims using the existing audited catalogue routes |
| Equation Recognition | Recognise unfamiliar equation structures and receive method suggestions |
| Theorem Bank | Store previously established results under the existing certificate policy |
| Knowledge Base | Browse/search SKILL.md, SKILL-2.md and the v0.5 proof handbook |

### Recognition example

Input:

```text
sin(x) = x/pi
```

Prompt:

```text
Solve graphically and state the number of intersections.
```

The recogniser identifies a non-constant graph-intersection structure (`EQREC-039`) and a trigonometric equation containing the angle variable outside the trig function (`EQREC-053`). It recommends graph/intersection analysis and warns that numerical roots alone do not establish completeness.

## 4. Mathematical scope and boundaries

- Angles are represented internally in radians. Numeric degree notation such as `30°` is converted exactly. A degree-valued variable should be entered explicitly, e.g. `sin(x*pi/180)` or `sin(x°)`.
- `abs(...)` and `|...|` are available to the recognition parser. They do not add new theorem authority to the identity catalogue.
- A recognition match is a candidate classification, not proof that the input is true or false.
- The estimated TP-style cognitive label is an engineering hint, not an official KPM assessment.
- Graph sketches and approximate roots do not constitute exact proof or complete solution certificates.
- Geometry/analysis recipes are recommendations until their proof rules are independently checked and implemented.

## 5. Project layout

```text
TrigonometricProofEngine_v0.5.1/
├── app.py
├── engine.py
├── recognition.py
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

## 6. Tests

Run from the project folder:

```bash
python -m unittest discover -s tests -v
```

The suites can also be run independently:

```bash
python -m unittest discover -s tests -p "test_circularity.py" -v
python -m unittest discover -s tests -p "test_engine.py" -v
python -m unittest discover -s tests -p "test_recognition.py" -v
```

The recognition acceptance suite checks every one of the 55 EQREC classes. The circularity suite checks that F08 cannot be proved through itself or through dependent identities.
