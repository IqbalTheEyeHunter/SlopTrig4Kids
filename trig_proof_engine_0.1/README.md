# Trigonometric Proof Engine

**Version:** 0.1.0  
**Target:** Windows 10/11 64-bit  
**Mode:** Offline after installation/build  
**Scope:** Real-angle expressions using only `sin`, `cos`, `tan`, `cot`, `sec`, and `csc` (plus arithmetic, powers, `pi`, and `sqrt`).

## What this first version does

- Accepts left-hand and right-hand expressions.
- Parses expressions safely (no Python `eval` of user input).
- Uses SymPy for symbolic trigonometric simplification.
- Attempts quotient/reciprocal rewrites, compound-angle expansion, trigonometric simplification, Fu transformations, and algebraic reduction.
- Tracks common domain restrictions from tangent, cotangent, secant, cosecant, denominators, and square roots.
- Reports one of three outcomes: **PROVED**, **DISPROVED** (a numerical counterexample was found), or **INCONCLUSIVE**.
- Includes a searchable, bundled copy of `knowledge/SKILL.md`.
- Does not call a web service, AI API, or cloud service.

## Windows quick start

1. Install Python 3.11 or newer (64-bit) from https://www.python.org/downloads/windows/.
2. During installation, enable **Add Python to PATH**.
3. Extract this project folder.
4. Double-click `run_windows.bat`.

The first run installs SymPy. After that, the application performs proof work offline.

## Build a standalone Windows executable

1. On a Windows 10/11 64-bit computer, double-click `build_windows.bat`.
2. The script installs SymPy and PyInstaller, then packages the application.
3. The executable is created at `dist/TrigonometricProofEngine.exe`.
4. Copy that EXE to a Windows computer. It does not need Python or internet access to run.

**Important:** Windows executables must be packaged on Windows. This project was assembled in a Linux build environment, so the Windows `.exe` itself is not generated here; the included build script creates it on Windows.

## Input syntax

Use explicit multiplication and function-call notation:

```text
sin(x)**2 + cos(x)**2
(1 - cos(2*x))/sin(2*x)
(sec(x) - tan(x))*(sec(x) + tan(x))
sin(x + y)
sqrt(1 - cos(x)**2)
```

Supported operators: `+`, `-`, `*`, `/`, `**`, parentheses. `^` is also accepted as a power symbol. `π` is accepted as `pi`.

Angles are in radians. For degrees, write the equivalent radian expression, e.g. `sin(30*pi/180)`.

## Interpreting results

- **PROVED:** A symbolic simplification route reduced `LHS - RHS` exactly to zero.
- **DISPROVED:** The engine found a numerical point in the common domain where the two sides differ. This is a counterexample, not a general theorem-prover result.
- **INCONCLUSIVE:** The current symbolic strategies did not prove the claim and no numerical counterexample was found. This does not mean the claim is true or false.

Numerical sampling is never used to certify an identity.

## Current limitations

- The proof search is heuristic and is not a complete decision procedure for all trigonometric identities.
- The first version does not yet generate a formal proof certificate with every elementary rewrite annotated by a unique database rule ID.
- Domain restrictions are reported as symbolic nonzero/nonnegative conditions; they are not always solved into complete interval descriptions.
- No inverse, hyperbolic, complex trigonometric functions, or equation-solving mode is included.
- The input parser requires explicit multiplication (for example, `2*sin(x)`).

## Project structure

```text
trig_proof_engine/
├── app.py
├── engine.py
├── requirements.txt
├── run_windows.bat
├── build_windows.bat
├── README.md
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
