# Trigonometric Proof Engine

**Version:** 0.2.0  
**Target:** Windows 10/11 64-bit  
**Mode:** Offline at runtime  
**Scope:** Real-angle expressions using only `sin`, `cos`, `tan`, `cot`, `sec`, and `csc` (plus arithmetic, powers, `pi`, and real square roots).

## What's new in 0.2.0

- **Directed proof strategies:** LHS to RHS, RHS to LHS, both sides to a common form, and the difference method.
- **Automatic route comparison:** attempts multiple proof paths and selects a preferred concise route; successful alternatives are listed in the report.
- **Identity ID references:** recognised transformations are linked to IDs from the bundled `knowledge/SKILL.md` database. The app reads the Markdown source directly and currently indexes **136 identity entries**.
- **Step-level trace:** each transformation records its previous expression, resulting expression, side, explanation, and any recognised identity IDs.
- **Symbolic step checks:** each recorded transformation is checked for exact symbolic equivalence. Numerical samples are not used to prove identities.
- **Export:** save a human-readable Markdown proof report or a JSON transformation certificate.
- **Expanded notation:** supports superscript powers through fourth power, including `sin⁴(x)`.
- **Keyboard shortcut:** `Ctrl + Enter` runs the proof.

## What the application does

- Accepts left-hand and right-hand expressions.
- Parses expressions safely (no Python `eval` of user input).
- Uses SymPy for symbolic trigonometric transformations.
- Attempts quotient/reciprocal rewrites, compound-angle expansion, trigonometric simplification, Fu transformations, common-denominator reduction, cancellation and factoring.
- Tracks visible original-domain restrictions from tangent, cotangent, secant, cosecant, denominators and real square roots.
- Reports **PROVED**, **DISPROVED** (a numerical counterexample was found), or **INCONCLUSIVE**.
- Bundles and searches the mathematical specification from `knowledge/SKILL.md`.
- Does not call a web service, AI API, or cloud service.

## Windows quick start (Python runtime)

1. Install Python 3.11 or newer (64-bit) from https://www.python.org/downloads/windows/.
2. During installation, enable **Add Python to PATH**.
3. Extract this project folder.
4. Double-click `run_windows.bat`.

The first run installs SymPy. After dependencies are installed, the application performs proof work offline.

## Build a standalone Windows executable

1. On a Windows 10/11 64-bit computer, double-click `build_windows.bat`.
2. The script installs SymPy and PyInstaller, then packages the application.
3. The executable is created at `dist/TrigonometricProofEngine.exe`.
4. Copy the EXE to a Windows computer. It does not need Python or internet access at runtime.

**Important:** Windows executables must be packaged on Windows. This project is assembled in a Linux build environment, so the native Windows `.exe` is not generated here; the included Windows build script and GitHub Actions workflow can create it.

## Input syntax

Use explicit multiplication and function-call notation:

```text
sin(x)**2 + cos(x)**2
(1 - cos(2*x))/sin(2*x)
(sec(x) - tan(x))*(sec(x) + tan(x))
sin(x + y)
sqrt(1 - cos(x)**2)
```

Textbook power notation is also accepted:

```text
sin^2(x) + cos²(x)
sin⁴(x)
```

Supported operators: `+`, `-`, `*`, `/`, `**`, parentheses. `^` is also accepted as a power symbol. `π` is accepted as `pi`. Numeric coefficient shorthand such as `2sin(x)` is accepted. General implicit multiplication is not yet supported.

Angles are in radians. For degrees, write the equivalent radian expression, e.g. `sin(30*pi/180)`.

## Proof strategies

- **Automatic:** attempts both one-sided directions, a two-sided common-form route, and the difference method.
- **LHS to RHS:** transforms only the left-hand side.
- **RHS to LHS:** transforms only the right-hand side.
- **Both sides to common form:** simplifies each side independently and compares the resulting forms.
- **Difference method:** simplifies `LHS - RHS` to zero.
- **Angle expansion first / Fu transformations first / Algebraic reduction first:** use alternate transformation ordering within the difference method.

The engine prefers a one-sided route when multiple successful routes are found. Alternative successful routes remain visible in the report.

## Interpreting results

- **PROVED:** a symbolic transformation route reduced the claim to equivalent expressions. Every recorded transformation is checked symbolically, and original domain restrictions are retained.
- **DISPROVED:** the engine found a numerical point in the common domain where the two sides differ. This is a counterexample, not a general theorem-prover result.
- **INCONCLUSIVE:** the selected symbolic strategy did not prove the claim and no numerical counterexample was found. This does not mean the claim is true or false.

Numerical sampling is never used to certify an identity. The JSON export is a trace of symbolic transformations, **not** a formally verified proof object for an independent theorem prover. Identity IDs are attached when the engine recognises a supported pattern; unrecognised transformations may have no ID.

## Current limitations

- The proof search is heuristic and is not a complete decision procedure for all trigonometric identities.
- The engine recognises a subset of the 136 indexed identities as executable proof-step references; the entire Markdown database is searchable, but not every catalogue row has a dedicated rewrite implementation yet.
- Domain restrictions are reported symbolically (for example, `cos(x) ≠ 0`); they are not always solved into complete interval descriptions.
- Some general-purpose SymPy transformations may be difficult to explain as a single elementary identity. The report identifies these as symbolic transformations rather than inventing a rule ID.
- No inverse, hyperbolic, exponential, or complex trigonometric functions are included.
- General implicit multiplication (such as `2x` or `x sin(x)`) is not yet supported; use `2*x` and `x*sin(x)`.

## Project structure

```text
trig_proof_engine/
├── app.py
├── engine.py
├── requirements.txt
├── run_windows.bat
├── build_windows.bat
├── README.md
├── TEST_RESULTS.txt
├── .github/workflows/build-windows.yml
├── knowledge/
│   └── SKILL.md
└── tests/
    └── test_engine.py
```

## Run tests

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```
