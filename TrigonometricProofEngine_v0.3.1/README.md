# Trigonometric Proof Engine

**Version:** 0.3.1  
**Target:** Windows 10/11 64-bit  
**Mode:** Offline at runtime  
**Scope:** Real-angle expressions using only `sin`, `cos`, `tan`, `cot`, `sec`, and `csc` (plus arithmetic, powers, `pi`, and real square roots).

## What's new in 0.3.1

- **Scrollable workspace:** the Proof Workspace, Theorem Bank, and Identity Library now each have a vertical scrollbar and mouse-wheel support.
- **Automatic report navigation:** after a proof is run, the workspace scrolls directly to the Proof Report.
- **Independent report scrolling:** long proof reports have their own scrollbar, so every proof step remains accessible without stretching the entire window.
- **Return-to-input control:** a Back to inputs button returns to the top of the Proof Workspace.
- **Smaller-screen layout:** the default window is 1180 × 760, with a minimum size of 900 × 600.

## What's new in 0.3.0 (proof engine)

- **Catalogue-guided proofs:** the default Proof Workspace strategy searches the bundled `SKILL.md` identity database instead of relying only on broad symbolic simplification.
- **125 executable equality rules:** 136 indexed entries in `SKILL.md` are read; paired formulas are split into individual rules and symbolically validated before entering the rewrite engine.
- **Step-by-step identity application:** every catalogue substitution is shown as its own proof step, with its identity ID, direction, source expression, resulting expression, and applicable domain conditions.
- **Visible algebra steps:** factoring, combining fractions, and cancellation are displayed separately from trigonometric identity applications. These algebraic operations do not silently replace a missing trigonometric identity.
- **Bidirectional rewriting:** each validated identity can be applied from left to right or right to left, including to matching subexpressions inside larger expressions.
- **User-supplied premises and saved results:** extra identities can be entered for a proof, saved to a local theorem bank, and reused offline.
- **Proof provenance:** Markdown reports and JSON certificates record the identity IDs and theorem references used in each proof step.
- **Domain preservation:** restrictions from original denominators, reciprocal functions, and theorem applications remain in the proof report even if later algebra cancels a factor.
- **Counterexample-first diagnosis:** catalogue mode first checks whether a valid numerical counterexample disproves the claim. Numerical sampling can disprove, but never prove, an identity.

### What is included in the automatic catalogue search?

- `136` indexed reference entries are bundled from `knowledge/SKILL.md`.
- `125` equality formulas are directly executable and symbolically validated as rewrite rules. Some indexed rows contain more than one formula.
- `17` conditional or parameterized entries are not blindly applied. They require extra assumptions such as an integer parameter, a selected square-root sign, a declared half-angle substitution, or phase-angle conditions.
- `10` inequality entries are not equality rewrite rules and are therefore not used to rewrite identities.

The engine searches the **applicable** catalogue rules and uses the relevant ones for a particular proof. It does not attempt to apply every identity to every expression. The search is bounded; a valid identity can still be reported as **INCONCLUSIVE** if the required chain is outside the search limits.

## What the application does

- Accepts left-hand and right-hand expressions.
- Parses expressions safely (no Python `eval` of user input).
- Uses a symbolic rewrite engine backed by the six-function identity catalogue.
- Shows each identity substitution and algebraic manipulation as an individual step.
- Supports automatic, LHS-to-RHS, RHS-to-LHS, common-form, difference, supplied-identity, and catalogue-guided strategies.
- Tracks visible original-domain restrictions from tangent, cotangent, secant, cosecant, denominators, and real square roots.
- Reports **PROVED**, **DISPROVED** (a valid numerical counterexample was found), or **INCONCLUSIVE**.
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

**Important:** Windows executables must be packaged on Windows. The project source is assembled in a Linux build environment, so the native Windows `.exe` is not generated here; the included Windows build script creates it on Windows.

## Scrolling and viewing proof reports (v0.3.1)

- Use the vertical scrollbar at the right edge of the active tab, or the mouse wheel, to move through long pages.
- After selecting **PROVE IDENTITY**, the Proof Workspace automatically scrolls to the **PROOF REPORT** section.
- Use the report's own scrollbar to inspect long step-by-step derivations and alternative proof routes.
- Select **Back to inputs** in the report header to return to the LHS/RHS fields.
- The same page-level scrolling is available in the Theorem Bank and Identity Library tabs.

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

## Catalogue-guided proof example

Target identity:

```text
LHS: sin(x)**2/(1-cos(x))
RHS: 1+cos(x)
```

Select **Use full identity catalogue**. The report displays a trace like this:

1. Start with the LHS: `sin(x)**2/(1-cos(x))`.
2. Apply **F18** (`sin²x = 1−cos²x`): `(1-cos(x)**2)/(1-cos(x))`.
3. Factor the numerator and denominator separately: `-(cos(x)-1)*(cos(x)+1)/(1-cos(x))`.
4. Cancel the common algebraic factor: `1+cos(x)`.
5. Match the RHS.

The report retains the original restriction `1-cos(x) ≠ 0`, even though that factor is cancelled during the proof.

A shorter example is:

```text
(1-cos(2*x))/sin(2*x) = tan(x)
```

The engine can apply **H06** directly with the substitution `x → 2*x`, displaying the identity reference and the exact target match. This is a valid one-identity proof; a proof does not need to use more identities than necessary.

## Using additional identities and derived results

### A. Supply premises for one proof

In the Proof Workspace, enter one identity per line:

```text
Pythagorean result: sin(t)**2 + cos(t)**2 = 1
Secant-tangent result: 1 = sec(u)**2 - tan(u)**2
```

Then enter the target:

```text
LHS: sin(x)**2 + cos(x)**2
RHS: sec(y)**2 - tan(y)**2
```

Select **Use supplied identities** to search only the supplied and saved theorems, or **Use full identity catalogue** to search those theorems together with the 125 bundled equality rules.

### B. Save a proved result

After a claim is proved, choose **Save proved result**, give it a name, and it will be stored in the local theorem bank. The next proof can use it automatically when **Include saved theorem bank** is checked.

### C. Manage the theorem bank

Open the **THEOREM BANK** tab to add a reusable identity, remove a selected item, or import/export the local theorem bank as JSON. Manually added identities are symbolically validated before they are accepted.

## Important limits

- The 125 catalogue rules are exact-symbolically validated before use; conditional and parameterized entries are not applied without their required assumptions.
- The proof search is bounded (up to eight identity substitutions and 140 visited expressions in a direct route). A valid proof may remain **INCONCLUSIVE** if it requires a longer or more specialised chain.
- The theorem bank is a reusable collection of claims and auditable proof records; it is not a formally verified proof-assistant kernel.
- The original denominator ledger is syntactic and conservative; it records visible nonzero and real-radical conditions but does not solve all resulting trigonometric domain sets.
- A **DISPROVED** result requires a valid counterexample at a point where both sides are defined. Failure to find a counterexample is never treated as proof.

## Proof strategies

- **Use full identity catalogue:** default strategy; searches all 125 directly executable equality rules plus supplied premises and saved theorems, and displays every selected identity and algebra step.
- **Automatic:** attempts the standard symbolic routes and then uses supplied theorem chains when present.
- **LHS to RHS / RHS to LHS:** transforms one side toward the other using the standard symbolic transformations.
- **Both sides to common form:** simplifies each side independently and compares the resulting forms.
- **Difference method:** simplifies `LHS - RHS` to zero.
- **Use supplied identities:** searches only user-supplied and saved identities.
- **Angle expansion first / Fu transformations first / Algebraic reduction first:** use alternate transformation ordering within the difference method.

The catalogue-guided strategy prioritises an explicit, reproducible derivation. It does not claim to find every possible proof or the mathematically shortest proof in every case.
