---
name: six-trig-proof-engine
version: 1.0.0
description: >-
  Prove, simplify, verify, and diagnose identities involving only the six
  elementary trigonometric functions sin, cos, tan, cot, sec, and csc.
  Use rigorous domain tracking, an indexed identity database, proof templates,
  counterexample checks, and multiple algebraic methods.
---

# Six-Function Trigonometric Proof Engine

> **Scope.** A reusable, self-contained proof skill for real-angle expressions built from **only** `sin`, `cos`, `tan`, `cot`, `sec`, and `csc`, together with real constants, arithmetic, radicals, and angle combinations. No inverse, hyperbolic, exponential, or complex trigonometric functions are needed. The collection is **broad rather than literally exhaustive**: infinitely many identities and proofs can be generated from the six functions.

## 0. Operational instructions for an assistant

When asked to prove a trigonometric identity:

1. **Parse the statement exactly.** Record both sides, angle variables, stated restrictions, and whether it is an identity, conditional equality, equation, or inequality.
2. **Determine the original domain** before manipulating anything. State where every original denominator and every `tan`, `cot`, `sec`, or `csc` is defined. If radicals occur, also require real radicands and nonzero radical denominators.
3. **Check plausibility.** Test simple permissible angles or use the identities below. If the claim is false, provide a valid counterexample rather than a fabricated proof.
4. **Prefer a one-sided proof:** transform the more complicated side into the other without assuming the conclusion. If a two-sided reduction is shorter, reduce both sides to the same third expression.
5. **Use the least powerful suitable tool:** reciprocal/quotient/Pythagorean identities → common denominators and factoring → angle formulas → product-to-sum → substitutions or auxiliary identities.
6. **Show the decisive steps.** Cite database IDs where helpful; explicitly identify any cancellation, factoring, conjugate, or angle formula.
7. **Preserve domain logic.** Multiplying by a possibly zero expression, canceling factors, taking square roots, and squaring equations can change the solution set. A derived formula can have a smaller domain than the original identity.
8. **Conclude with a precise statement:** equality holds for every real angle in the original common domain, or state additional restrictions if the proof used them.
9. **If a problem asks for a particular method**, use it if valid (e.g., LHS-only, RHS-only, unit circle, angle addition, without converting all to sine/cosine).
10. **Never claim an identity at a point where one side is undefined.** Equal limits do not make an undefined expression defined.

### Default response format

**Claim:** write the exact identity. **Domain:** list restrictions. **Proof:** a logically ordered sequence of equalities with short justifications. **Conclusion:** identity verified on its common domain. For false claims, replace the proof with **Counterexample** and optionally a corrected identity.

### Notation

- Angles `x,y,z,A,B,C` are real; use radians unless a degree symbol is written.
- `sin²x` means `(sin x)²`; `sin 2x` means `sin(2x)`, not `(sin x)²`.
- `k ∈ ℤ`; `π` is the usual half-turn; `√` is the **nonnegative** real square root.
- `D(E)` denotes the real domain on which expression `E` is defined.
- An identity `L=R` means equality for all real assignments in `D(L) ∩ D(R)`; this **does not** assert that the two sides have identical domains.
- A reference to a denominator being nonzero includes denominators embedded in compound fractions.

---

# PART I — FOUNDATIONS AND MASTER IDENTITY INDEX

## 1. The six elementary functions and their domains

| Function | Definition from sine and cosine | Undefined when | Zeros (when defined) |
|---|---|---|---|
| `sin x` | unit-circle vertical coordinate | never | `x=kπ` |
| `cos x` | unit-circle horizontal coordinate | never | `x=π/2+kπ` |
| `tan x` | `sin x / cos x` | `cos x=0` | `x=kπ` |
| `cot x` | `cos x / sin x` | `sin x=0` | `x=π/2+kπ` |
| `sec x` | `1 / cos x` | `cos x=0` | never |
| `csc x` | `1 / sin x` | `sin x=0` | never |

**Geometric foundation:** For a point `(cos x, sin x)` on the unit circle, the radius is one, so `cos²x + sin²x = 1`. Signed rotation and reflection of the point yield the addition, parity, periodicity, and cofunction rules. Quotient and reciprocal definitions generate the other four functions.

### 1.1 Domain ledger

| Expression | Required condition |
|---|---|
| `1/sin x`, `cot x`, `csc x` | `sin x ≠ 0` |
| `1/cos x`, `tan x`, `sec x` | `cos x ≠ 0` |
| `1/tan x` | `sin x ≠ 0` **and** `cos x ≠ 0` |
| `1/cot x` | `sin x ≠ 0` **and** `cos x ≠ 0` |
| `1/(1−cos x)` | `cos x ≠ 1` |
| `1/(1+cos x)` | `cos x ≠ −1` |
| `1/(1−sin x)` | `sin x ≠ 1` |
| `1/(1+sin x)` | `sin x ≠ −1` |
| `√((1−cos x)/2)` | always real, but the square root alone is `|sin(x/2)|` |
| `√((1+cos x)/2)` | always real, but the square root alone is `|cos(x/2)|` |

**Domain trap:** `tan x · cot x = 1` only when **both** functions exist (`sin x cos x ≠ 0`), whereas `sin x · csc x = 1` requires only `sin x ≠ 0`.

## 2. Fundamental identity catalogue

### F — Quotient, reciprocal, and Pythagorean

| ID | Identity | Domain / caveat |
|---|---|---|
| F01 | `tan x = sin x / cos x` | `cos x ≠ 0` |
| F02 | `cot x = cos x / sin x` | `sin x ≠ 0` |
| F03 | `sec x = 1/cos x` | `cos x ≠ 0` |
| F04 | `csc x = 1/sin x` | `sin x ≠ 0` |
| F05 | `tan x · cot x = 1` | `sin x cos x ≠ 0` |
| F06 | `sin x · csc x = 1` | `sin x ≠ 0` |
| F07 | `cos x · sec x = 1` | `cos x ≠ 0` |
| F08 | `sin²x + cos²x = 1` | all real `x` |
| F09 | `1 + tan²x = sec²x` | `cos x ≠ 0` |
| F10 | `1 + cot²x = csc²x` | `sin x ≠ 0` |
| F11 | `sec²x − tan²x = 1` | `cos x ≠ 0` |
| F12 | `csc²x − cot²x = 1` | `sin x ≠ 0` |
| F13 | `sec²x + csc²x = sec²x csc²x` | `sin x cos x ≠ 0` |
| F14 | `tan²x + cot²x + 2 = sec²x csc²x` | `sin x cos x ≠ 0` |
| F15 | `tan x + cot x = sec x csc x` | `sin x cos x ≠ 0` |
| F16 | `(sec x−tan x)(sec x+tan x)=1` | `cos x ≠ 0` |
| F17 | `(csc x−cot x)(csc x+cot x)=1` | `sin x ≠ 0` |
| F18 | `sin²x = 1−cos²x` | all real `x` |
| F19 | `cos²x = 1−sin²x` | all real `x` |
| F20 | `tan²x = sec²x−1`, `cot²x = csc²x−1` | corresponding function domains |

### S — Symmetry, shifts, and periodicity

| ID | Identity | Domain convention |
|---|---|---|
| S01 | `sin(−x)=−sin x`, `cos(−x)=cos x` | all real `x` |
| S02 | `tan(−x)=−tan x`, `cot(−x)=−cot x` | where defined |
| S03 | `sec(−x)=sec x`, `csc(−x)=−csc x` | where defined |
| S04 | `sin(x+2kπ)=sin x`, `cos(x+2kπ)=cos x` | all real `x` |
| S05 | `tan(x+kπ)=tan x`, `cot(x+kπ)=cot x` | where defined |
| S06 | `sec(x+2kπ)=sec x`, `csc(x+2kπ)=csc x` | where defined |
| S07 | `sin(x+π)=−sin x`, `cos(x+π)=−cos x` | all real `x` |
| S08 | `tan(x+π)=tan x`, `cot(x+π)=cot x` | where defined |
| S09 | `sec(x+π)=−sec x`, `csc(x+π)=−csc x` | where defined |
| S10 | `sin(π−x)=sin x`, `cos(π−x)=−cos x` | all real `x` |
| S11 | `sin(π/2−x)=cos x`, `cos(π/2−x)=sin x` | all real `x` |
| S12 | `tan(π/2−x)=cot x`, `cot(π/2−x)=tan x` | both sides defined |
| S13 | `sec(π/2−x)=csc x`, `csc(π/2−x)=sec x` | both sides defined |
| S14 | `sin(π/2+x)=cos x`, `cos(π/2+x)=−sin x` | all real `x` |
| S15 | `tan(π/2+x)=−cot x`, `cot(π/2+x)=−tan x` | both sides defined |
| S16 | `sec(π/2+x)=−csc x`, `csc(π/2+x)=sec x` | both sides defined |
| S17 | `sin(2π−x)=−sin x`, `cos(2π−x)=cos x` | all real `x` |
| S18 | `sin(π+x)=−sin x`, `cos(π+x)=−cos x` | all real `x` |

### A — Addition and subtraction

| ID | Identity | Conditions |
|---|---|---|
| A01 | `sin(x+y)=sin x cos y+cos x sin y` | all real |
| A02 | `sin(x−y)=sin x cos y−cos x sin y` | all real |
| A03 | `cos(x+y)=cos x cos y−sin x sin y` | all real |
| A04 | `cos(x−y)=cos x cos y+sin x sin y` | all real |
| A05 | `tan(x+y)=(tan x+tan y)/(1−tan x tan y)` | `cos x cos y cos(x+y) ≠ 0` |
| A06 | `tan(x−y)=(tan x−tan y)/(1+tan x tan y)` | `cos x cos y cos(x−y) ≠ 0` |
| A07 | `cot(x+y)=(cot x cot y−1)/(cot x+cot y)` | `sin x sin y sin(x+y) ≠ 0` |
| A08 | `cot(x−y)=(cot x cot y+1)/(cot y−cot x)` | `sin x sin y sin(x−y) ≠ 0` |
| A09 | `sin(x+y)+sin(x−y)=2sin x cos y` | all real |
| A10 | `sin(x+y)−sin(x−y)=2cos x sin y` | all real |
| A11 | `cos(x+y)+cos(x−y)=2cos x cos y` | all real |
| A12 | `cos(x−y)−cos(x+y)=2sin x sin y` | all real |
| A13 | `sin(x+y)sin(x−y)=sin²x−sin²y` | all real |
| A14 | `cos(x+y)cos(x−y)=cos²x−sin²y` | all real |
| A15 | `cos(x+y)cos(x−y)=cos²x+cos²y−1` | all real |
| A16 | `sin(x+y)cos(x−y)=sin x cos x+sin y cos y` | all real |
| A17 | `cos(x+y)sin(x−y)=sin x cos x−sin y cos y` | all real |
| A18 | `sec(x+y)=sec x sec y/(1−tan x tan y)` | `cos x cos y cos(x+y) ≠ 0` |
| A19 | `sec(x−y)=sec x sec y/(1+tan x tan y)` | `cos x cos y cos(x−y) ≠ 0` |
| A20 | `csc(x+y)=csc x csc y/(cot x+cot y)` | `sin x sin y sin(x+y) ≠ 0` |
| A21 | `csc(x−y)=csc x csc y/(cot y−cot x)` | `sin x sin y sin(x−y) ≠ 0` |

**Important:** The rational tangent and cotangent addition formulas have stricter domains than their sine/cosine counterparts. Do not use `tan(x+y)` in a proof at a point where `tan x` is undefined.

### D — Double, triple, and general multiple angles

| ID | Identity | Conditions |
|---|---|---|
| D01 | `sin 2x=2sin x cos x` | all real |
| D02 | `cos 2x=cos²x−sin²x` | all real |
| D03 | `cos 2x=1−2sin²x` | all real |
| D04 | `cos 2x=2cos²x−1` | all real |
| D05 | `tan 2x=2tan x/(1−tan²x)` | `cos x cos 2x ≠ 0` |
| D06 | `cot 2x=(cot²x−1)/(2cot x)` | `sin x cos x ≠ 0` |
| D07 | `sin 3x=3sin x−4sin³x` | all real |
| D08 | `cos 3x=4cos³x−3cos x` | all real |
| D09 | `tan 3x=(3tan x−tan³x)/(1−3tan²x)` | `cos x cos 3x ≠ 0` |
| D10 | `cot 3x=(cot³x−3cot x)/(3cot²x−1)` | `sin x sin 3x ≠ 0`, with denominator nonzero automatically |
| D11 | `sin 4x=4sin x cos x(cos²x−sin²x)` | all real |
| D12 | `cos 4x=1−8sin²x cos²x` | all real |
| D13 | `sin((n+1)x)=2cos x sin(nx)−sin((n−1)x)` | integer `n≥1`, all real |
| D14 | `cos((n+1)x)=2cos x cos(nx)−cos((n−1)x)` | integer `n≥1`, all real |
| D15 | `sin(nx)=sin x · U_(n−1)(cos x)` | integer `n≥1`; `U_0(t)=1`, `U_1(t)=2t`, `U_(m+1)=2tU_m−U_(m−1)` |
| D16 | `cos(nx)=T_n(cos x)` | integer `n≥0`; `T_0(t)=1`, `T_1(t)=t`, `T_(m+1)=2tT_m−T_(m−1)` |

The polynomials `T_n` and `U_n` are **algebraic notation**, not additional trigonometric functions.

### H — Half-angle, power reduction, and t-substitution

| ID | Identity | Conditions |
|---|---|---|
| H01 | `sin²(x/2)=(1−cos x)/2` | all real |
| H02 | `cos²(x/2)=(1+cos x)/2` | all real |
| H03 | `sin(x/2)=±√((1−cos x)/2)` | choose sign from the actual quadrant of `x/2` |
| H04 | `cos(x/2)=±√((1+cos x)/2)` | choose sign from the actual quadrant of `x/2` |
| H05 | `tan(x/2)=sin x/(1+cos x)` | `cos(x/2) ≠ 0` (so `1+cos x ≠ 0`) |
| H06 | `tan(x/2)=(1−cos x)/sin x` | `sin x ≠ 0`; this excludes some points where `tan(x/2)` exists |
| H07 | `tan(x/2)=tan x/(sec x+1)` | `cos x ≠ 0` and `cos(x/2) ≠ 0`; also `sec x+1 ≠ 0` |
| H08 | `cot(x/2)=(1+cos x)/sin x` | `sin x ≠ 0` |
| H09 | `cot(x/2)=sin x/(1−cos x)` | `sin(x/2) ≠ 0` |
| H10 | `sin²x=(1−cos 2x)/2` | all real |
| H11 | `cos²x=(1+cos 2x)/2` | all real |
| H12 | `sin x cos x=(sin 2x)/2` | all real |
| H13 | `sin⁴x=(3−4cos 2x+cos 4x)/8` | all real |
| H14 | `cos⁴x=(3+4cos 2x+cos 4x)/8` | all real |
| H15 | `sin²x cos²x=(1−cos 4x)/8` | all real |
| H16 | If `t=tan(x/2)`, `sin x=2t/(1+t²)` | `cos(x/2) ≠ 0` |
| H17 | If `t=tan(x/2)`, `cos x=(1−t²)/(1+t²)` | `cos(x/2) ≠ 0` |
| H18 | If `t=tan(x/2)`, `tan x=2t/(1−t²)` | `cos(x/2) ≠ 0`, `cos x ≠ 0` |
| H19 | If `t=tan(x/2)`, `cot x=(1−t²)/(2t)` | `cos(x/2) ≠ 0`, `sin x ≠ 0` |
| H20 | If `t=tan(x/2)`, `sec x=(1+t²)/(1−t²)` | `cos(x/2) ≠ 0`, `cos x ≠ 0` |
| H21 | If `t=tan(x/2)`, `csc x=(1+t²)/(2t)` | `cos(x/2) ≠ 0`, `sin x ≠ 0` |

**Half-angle caution:** H05 is valid at `x=2kπ` (`0/2=0`); H06 is not valid there (`0/0`). Neither is valid when `x=(2k+1)π` because `tan(x/2)` is undefined.

### P — Product-to-sum and sum-to-product

| ID | Identity | Conditions |
|---|---|---|
| P01 | `2sin x cos y=sin(x+y)+sin(x−y)` | all real |
| P02 | `2cos x sin y=sin(x+y)−sin(x−y)` | all real |
| P03 | `2cos x cos y=cos(x+y)+cos(x−y)` | all real |
| P04 | `2sin x sin y=cos(x−y)−cos(x+y)` | all real |
| P05 | `sin x+sin y=2sin((x+y)/2)cos((x−y)/2)` | all real |
| P06 | `sin x−sin y=2cos((x+y)/2)sin((x−y)/2)` | all real |
| P07 | `cos x+cos y=2cos((x+y)/2)cos((x−y)/2)` | all real |
| P08 | `cos x−cos y=−2sin((x+y)/2)sin((x−y)/2)` | all real |
| P09 | `sin x+cos x=√2 sin(x+π/4)` | all real |
| P10 | `cos x−sin x=√2 cos(x+π/4)` | all real |
| P11 | `a sin x+b cos x=R sin(x+φ)` | `R=√(a²+b²)>0`; choose `cos φ=a/R`, `sin φ=b/R` |
| P12 | `a cos x+b sin x=R cos(x−φ)` | `R=√(a²+b²)>0`; choose `cos φ=a/R`, `sin φ=b/R` |

When `a=b=0`, the linear combination is identically zero; P11/P12 need no phase angle.

### R — Rationalizations and paired expressions

| ID | Identity | Conditions |
|---|---|---|
| R01 | `(1−cos x)/sin x=sin x/(1+cos x)` | `sin x ≠ 0` |
| R02 | `(1+cos x)/sin x=sin x/(1−cos x)` | `sin x ≠ 0` |
| R03 | `(1−sin x)/cos x=cos x/(1+sin x)` | `cos x ≠ 0` |
| R04 | `(1+sin x)/cos x=cos x/(1−sin x)` | `cos x ≠ 0` |
| R05 | `1/(sec x+tan x)=sec x−tan x` | `cos x ≠ 0` |
| R06 | `1/(csc x+cot x)=csc x−cot x` | `sin x ≠ 0` |
| R07 | `(sec x+tan x)²=(1+sin x)/(1−sin x)` | `cos x ≠ 0` |
| R08 | `(csc x+cot x)²=(1+cos x)/(1−cos x)` | `sin x ≠ 0` |
| R09 | `(sec x−tan x)²=(1−sin x)/(1+sin x)` | `cos x ≠ 0` |
| R10 | `(csc x−cot x)²=(1−cos x)/(1+cos x)` | `sin x ≠ 0` |
| R11 | `tan x/(sec x+1)=sin x/(1+cos x)` | `cos x ≠ 0`, `1+cos x ≠ 0` |
| R12 | `cot x/(csc x+1)=cos x/(1+sin x)` | `sin x ≠ 0`, `1+sin x ≠ 0` |
| R13 | `1/(1−sin x)+1/(1+sin x)=2sec²x` | `cos x ≠ 0` |
| R14 | `1/(1−cos x)+1/(1+cos x)=2csc²x` | `sin x ≠ 0` |
| R15 | `1/(1−sin x)−1/(1+sin x)=2tan x sec x` | `cos x ≠ 0` |
| R16 | `1/(1−cos x)−1/(1+cos x)=2cot x csc x` | `sin x ≠ 0` |
| R17 | `(tan x+sec x)/(tan x−sec x)=−(sec x+tan x)²` | `cos x ≠ 0` |
| R18 | `(cot x+csc x)/(cot x−csc x)=−(csc x+cot x)²` | `sin x ≠ 0` |

### Q — Exact-angle values and reference angles

| Angle | `sin` | `cos` | `tan` | `cot` | `sec` | `csc` |
|---|---|---|---|---|---|---|
| `0` | `0` | `1` | `0` | undefined | `1` | undefined |
| `π/6` | `1/2` | `√3/2` | `√3/3` | `√3` | `2√3/3` | `2` |
| `π/4` | `√2/2` | `√2/2` | `1` | `1` | `√2` | `√2` |
| `π/3` | `√3/2` | `1/2` | `√3` | `√3/3` | `2` | `2√3/3` |
| `π/2` | `1` | `0` | undefined | `0` | undefined | `1` |

**Additional exact angles:**

- `sin(π/12)=(√6−√2)/4`; `cos(π/12)=(√6+√2)/4`; `tan(π/12)=2−√3`.
- `sin(5π/12)=(√6+√2)/4`; `cos(5π/12)=(√6−√2)/4`; `tan(5π/12)=2+√3`.
- Use S01–S18 to obtain other quadrants and cot/sec/csc where defined.

---

# PART II — DERIVATION BANK (EXPLICIT PROOFS)

The entries below provide **reusable proofs**, not merely formula statements. A formula in Part I can be invoked by ID once its domain has been checked.

## 3. Foundational proofs (B01–B16)

**B01 — Pythagorean identity (F08).** The unit-circle point `(cos x,sin x)` has distance 1 from the origin, hence `cos²x+sin²x=1`.

**B02 — Tangent Pythagorean identity (F09).** Divide B01 by `cos²x` (requiring `cos x≠0`): `1+sin²x/cos²x=1/cos²x`, i.e. `1+tan²x=sec²x`.

**B03 — Cotangent Pythagorean identity (F10).** Divide B01 by `sin²x` (requiring `sin x≠0`): `cos²x/sin²x+1=1/sin²x`, i.e. `cot²x+1=csc²x`.

**B04 — Reciprocal pair (F05).** `tan x cot x=(sin x/cos x)(cos x/sin x)=1`, provided `sin x cos x≠0`.

**B05 — Tangent-plus-cotangent (F15).** `tan x+cot x=(sin²x+cos²x)/(sin x cos x)=1/(sin x cos x)=sec x csc x`.

**B06 — Secant–tangent conjugates (F16).** `(sec x−tan x)(sec x+tan x)=sec²x−tan²x=1` by B02.

**B07 — Cosecant–cotangent conjugates (F17).** `(csc x−cot x)(csc x+cot x)=csc²x−cot²x=1` by B03.

**B08 — Secant and cosecant square sum (F13).** `sec²x+csc²x=(sin²x+cos²x)/(sin²x cos²x)=1/(sin²x cos²x)=sec²x csc²x`.

**B09 — Square of tangent-plus-cotangent (F14).** `(tan x+cot x)²=tan²x+cot²x+2=(sec x csc x)²` by B05.

**B10 — Complementary tangent and cotangent (S12).** `tan(π/2−x)=sin(π/2−x)/cos(π/2−x)=cos x/sin x=cot x` when `sin x≠0`.

**B11 — Complementary secant and cosecant (S13).** `sec(π/2−x)=1/sin x=csc x` when `sin x≠0`.

**B12 — Odd tangent and even secant (S02/S03).** `tan(−x)=sin(−x)/cos(−x)=−tan x`; `sec(−x)=1/cos(−x)=sec x`.

**B13 — Addition formula for sine (A01).** Rotating the unit-circle point `(cos x,sin x)` through `y` produces vertical coordinate `sin x cos y+cos x sin y`; it is also `sin(x+y)`.

**B14 — Addition formula for cosine (A03).** The same rotation produces horizontal coordinate `cos x cos y−sin x sin y`, which equals `cos(x+y)`.

**B15 — Subtraction formulas (A02/A04).** Substitute `−y` into B13/B14, then use `sin(−y)=−sin y`, `cos(−y)=cos y`.

**B16 — Tangent addition (A05).** `tan(x+y)=sin(x+y)/cos(x+y)=(sin x cos y+cos x sin y)/(cos x cos y−sin x sin y)`; divide numerator and denominator by `cos x cos y` (nonzero) to obtain `(tan x+tan y)/(1−tan x tan y)`.

## 4. Angle-formula proofs (B17–B36)

**B17 — Tangent subtraction (A06).** Apply B16 with `−y` and `tan(−y)=−tan y`.

**B18 — Cotangent addition (A07).** `cot(x+y)=cos(x+y)/sin(x+y)`. Divide the quotient from A03/A01 by `sin x sin y` to obtain `(cot x cot y−1)/(cot x+cot y)`; require `sin x sin y sin(x+y)≠0`.

**B19 — Cotangent subtraction (A08).** Substitute `−y` in the sine/cosine subtraction formulas and divide by `sin x sin y`: `(cot x cot y+1)/(cot y−cot x)`.

**B20 — Sine double-angle (D01).** A01 with `y=x`: `sin 2x=sin x cos x+cos x sin x=2sin x cos x`.

**B21 — Three cosine double-angle forms (D02–D04).** A03 with `y=x` gives `cos 2x=cos²x−sin²x`. Replace `cos²x` by `1−sin²x` for D03; replace `sin²x` by `1−cos²x` for D04.

**B22 — Tangent double-angle (D05).** Apply A05 with `y=x`: `tan 2x=2tan x/(1−tan²x)` on its stated domain.

**B23 — Cotangent double-angle (D06).** Apply A07 with `y=x`: `cot 2x=(cot²x−1)/(2cot x)`; this representation requires `sin x cos x≠0`.

**B24 — Sine triple-angle (D07).** `sin 3x=sin(2x+x)=sin 2x cos x+cos 2x sin x=2sin x cos²x+(1−2sin²x)sin x=3sin x−4sin³x`.

**B25 — Cosine triple-angle (D08).** `cos 3x=cos(2x+x)=cos 2x cos x−sin 2x sin x=(2cos²x−1)cos x−2sin²x cos x=4cos³x−3cos x`.

**B26 — Tangent triple-angle (D09).** Apply A05 to `tan(2x+x)`, insert D05, and simplify to `(3t−t³)/(1−3t²)` for `t=tan x`. This is valid whenever `cos x cos 3x≠0`; at an intermediate point with `cos 2x=0`, use direct sine/cosine expansion instead of the `tan 2x` intermediate.

**B27 — Cotangent triple-angle (D10).** From B24–B25, `cot 3x=(4cos³x−3cos x)/(3sin x−4sin³x)`. Divide numerator and denominator by `sin³x` to obtain `(cot³x−3cot x)/(3cot²x−1)` wherever `sin x sin 3x≠0`.

**B28 — Sine quadruple-angle (D11).** `sin 4x=2sin 2x cos 2x=4sin x cos x(cos²x−sin²x)`.

**B29 — Cosine quadruple-angle (D12).** `cos 4x=1−2sin²2x=1−8sin²x cos²x`.

**B30 — Sine recurrence (D13).** Add `sin((n+1)x)=sin(nx)cos x+cos(nx)sin x` and `sin((n−1)x)=sin(nx)cos x−cos(nx)sin x`; rearrange.

**B31 — Cosine recurrence (D14).** Add `cos((n+1)x)=cos(nx)cos x−sin(nx)sin x` and `cos((n−1)x)=cos(nx)cos x+sin(nx)sin x`; rearrange.

**B32 — Sine polynomial recurrence (D15).** Base cases: `sin x=sin x U_0(cos x)`, `sin 2x=sin x U_1(cos x)`. B30 proves the polynomial recurrence inductively.

**B33 — Cosine polynomial recurrence (D16).** Base cases: `cos 0=1=T_0(cos x)` and `cos x=T_1(cos x)`; B31 proves the polynomial recurrence inductively.

**B34 — Sine and cosine of an angle difference.** `sin(x−y)=sin x cos y−cos x sin y`; `cos(x−y)=cos x cos y+sin x sin y` follow from B15, and are safe even when tangent is undefined.

**B35 — Difference-of-squares in shifted sine (A13).** Multiply A01 and A02: `(sin x cos y+cos x sin y)(sin x cos y−cos x sin y)=sin²x cos²y−cos²x sin²y=sin²x−sin²y`.

**B36 — Difference-of-squares in shifted cosine (A14/A15).** Multiply A03 and A04: `cos²x cos²y−sin²x sin²y=cos²x−sin²y=cos²x+cos²y−1`.

## 5. Product, sum, half-angle, and phase proofs (B37–B58)

**B37 — Product `2sin x cos y` (P01).** Add A01 and A02: `sin(x+y)+sin(x−y)=2sin x cos y`.

**B38 — Product `2cos x sin y` (P02).** Subtract A02 from A01: `sin(x+y)−sin(x−y)=2cos x sin y`.

**B39 — Product `2cos x cos y` (P03).** Add A03 and A04: `cos(x+y)+cos(x−y)=2cos x cos y`.

**B40 — Product `2sin x sin y` (P04).** Subtract A03 from A04: `cos(x−y)−cos(x+y)=2sin x sin y`.

**B41 — Sum of two sines (P05).** Put `u=(x+y)/2`, `v=(x−y)/2` in P01: `sin x+sin y=sin(u+v)+sin(u−v)=2sin u cos v`.

**B42 — Difference of two sines (P06).** Use `u=(x+y)/2`, `v=(x−y)/2` in P02: `sin x−sin y=2cos u sin v`.

**B43 — Sum of two cosines (P07).** Use the same `u,v` in P03: `cos x+cos y=2cos u cos v`.

**B44 — Difference of two cosines (P08).** Use P04 and reverse order: `cos x−cos y=−2sin u sin v`.

**B45 — Sine half-angle square (H01).** `cos x=1−2sin²(x/2)` by D03 with input `x/2`. Rearrange.

**B46 — Cosine half-angle square (H02).** `cos x=2cos²(x/2)−1` by D04 with input `x/2`. Rearrange.

**B47 — Half-angle tangent, first form (H05).** `sin x/(1+cos x)=2sin(x/2)cos(x/2)/(2cos²(x/2))=tan(x/2)` if `cos(x/2)≠0`.

**B48 — Half-angle tangent, second form (H06).** `(1−cos x)/sin x=2sin²(x/2)/(2sin(x/2)cos(x/2))=tan(x/2)` when `sin x≠0`.

**B49 — Half-angle cotangent (H08/H09).** Invert H06 or H05 only on a domain where the relevant numerator is nonzero, or use the double-angle expansions directly.

**B50 — Power reduction for sine (H10).** Rearrange `cos 2x=1−2sin²x`.

**B51 — Power reduction for cosine (H11).** Rearrange `cos 2x=2cos²x−1`.

**B52 — Sine fourth power (H13).** `sin⁴x=[(1−cos 2x)/2]²=[1−2cos 2x+(1+cos 4x)/2]/4=(3−4cos 2x+cos 4x)/8`.

**B53 — Cosine fourth power (H14).** Similarly `cos⁴x=[(1+cos 2x)/2]²=(3+4cos 2x+cos 4x)/8`.

**B54 — Mixed fourth power (H15).** `sin²x cos²x=(sin²2x)/4=(1−cos 4x)/8`.

**B55 — Tangent-half-angle substitution (H16/H17).** With `t=tan(x/2)`, `sin x=2sin(x/2)cos(x/2)=2t/(1+t²)` and `cos x=cos²(x/2)−sin²(x/2)=(1−t²)/(1+t²)`. Obtain H18–H21 using quotient and reciprocal identities with their extra restrictions.

**B56 — Amplitude-phase for sine (P11).** Let `R=√(a²+b²)>0` and choose `cos φ=a/R`, `sin φ=b/R`. Then `R sin(x+φ)=R sin x cos φ+R cos x sin φ=a sin x+b cos x`.

**B57 — Amplitude-phase for cosine (P12).** Let `cos φ=a/R`, `sin φ=b/R`; `R cos(x−φ)=R cos x cos φ+R sin x sin φ=a cos x+b sin x`.

**B58 — Special 15° and 75° values.** Use `π/12=π/4−π/6` and `5π/12=π/4+π/6` in A01/A03/A05, then simplify radicals; `tan(π/12)=(1−1/√3)/(1+1/√3)=2−√3`.

## 6. Rationalization and compound reciprocal proofs (B59–B80)

**B59 — Cosine-conjugate fraction (R01).** `(1−cos x)/sin x=[(1−cos x)(1+cos x)]/[sin x(1+cos x)]=sin²x/[sin x(1+cos x)]=sin x/(1+cos x)`, for `sin x≠0`.

**B60 — Complementary cosine-conjugate fraction (R02).** `(1+cos x)/sin x=[(1−cos²x)]/[sin x(1−cos x)]=sin x/(1−cos x)`, for `sin x≠0`.

**B61 — Sine-conjugate fraction (R03).** `(1−sin x)/cos x=[(1−sin²x)]/[cos x(1+sin x)]=cos x/(1+sin x)`, for `cos x≠0`.

**B62 — Complementary sine-conjugate fraction (R04).** `(1+sin x)/cos x=cos x/(1−sin x)` by the same method, for `cos x≠0`.

**B63 — Reciprocal of `sec+tan` (R05).** `1/(sec x+tan x)=(sec x−tan x)/(sec²x−tan²x)=sec x−tan x`; `sec x+tan x` cannot vanish because its conjugate product is 1.

**B64 — Reciprocal of `csc+cot` (R06).** `1/(csc x+cot x)=csc x−cot x` because `csc²x−cot²x=1`.

**B65 — Square of `sec+tan` (R07).** `(sec x+tan x)²=[(1+sin x)/cos x]²=(1+sin x)²/(1−sin²x)=(1+sin x)/(1−sin x)`.

**B66 — Square of `csc+cot` (R08).** `(csc x+cot x)²=[(1+cos x)/sin x]²=(1+cos x)/(1−cos x)`.

**B67 — Square of `sec−tan` (R09).** `(sec x−tan x)²=(1−sin x)²/(1−sin²x)=(1−sin x)/(1+sin x)`.

**B68 — Square of `csc−cot` (R10).** `(csc x−cot x)²=(1−cos x)²/(1−cos²x)=(1−cos x)/(1+cos x)`.

**B69 — Secant-plus-one ratio (R11).** `tan x/(sec x+1)=[sin x/cos x]/[(1+cos x)/cos x]=sin x/(1+cos x)`.

**B70 — Cosecant-plus-one ratio (R12).** `cot x/(csc x+1)=[cos x/sin x]/[(1+sin x)/sin x]=cos x/(1+sin x)`.

**B71 — Reciprocal sine pair, sum (R13).** `1/(1−sin x)+1/(1+sin x)=2/(1−sin²x)=2/cos²x=2sec²x`.

**B72 — Reciprocal cosine pair, sum (R14).** `1/(1−cos x)+1/(1+cos x)=2/(1−cos²x)=2csc²x`.

**B73 — Reciprocal sine pair, difference (R15).** `1/(1−sin x)−1/(1+sin x)=2sin x/cos²x=2tan x sec x`.

**B74 — Reciprocal cosine pair, difference (R16).** `1/(1−cos x)−1/(1+cos x)=2cos x/sin²x=2cot x csc x`.

**B75 — Fraction of tangent and secant (R17).** Since `tan x−sec x=−(sec x−tan x)=−1/(sec x+tan x)`, the ratio is `−(sec x+tan x)²`.

**B76 — Fraction of cotangent and cosecant (R18).** Since `cot x−csc x=−(csc x−cot x)=−1/(csc x+cot x)`, the ratio is `−(csc x+cot x)²`.

**B77 — Secant addition (A18).** `sec(x+y)=1/[cos x cos y−sin x sin y]`. Factor `cos x cos y` from the denominator to obtain `sec x sec y/(1−tan x tan y)` on the stated domain.

**B78 — Secant subtraction (A19).** `sec(x−y)=1/[cos x cos y+sin x sin y]=sec x sec y/(1+tan x tan y)` on the stated domain.

**B79 — Cosecant addition (A20).** `csc(x+y)=1/[sin x cos y+cos x sin y]`. Factor `sin x sin y` from the denominator to obtain `csc x csc y/(cot x+cot y)` on the stated domain.

**B80 — Cosecant subtraction (A21).** `csc(x−y)=1/[sin x cos y−cos x sin y]=csc x csc y/(cot y−cot x)` on the stated domain.

---

# PART III — WORKED IDENTITY PROOF DATABASE

Each W-entry is a full model for a common exam-style pattern. **All equalities below hold only on the common domain of their displayed expressions.**

## 7. Reciprocal and Pythagorean transformations (W01–W20)

**W01.** Prove `(1−sin²x)/cos x=cos x`.

Domain: `cos x≠0`. Proof: `(1−sin²x)/cos x=cos²x/cos x=cos x`.

**W02.** Prove `(1−cos²x)/sin x=sin x`.

Domain: `sin x≠0`. Proof: `(1−cos²x)/sin x=sin²x/sin x=sin x`.

**W03.** Prove `tan x cos x=sin x`.

Domain: `cos x≠0`. Proof: `tan x cos x=(sin x/cos x)cos x=sin x`.

**W04.** Prove `cot x sin x=cos x`.

Domain: `sin x≠0`. Proof: `cot x sin x=(cos x/sin x)sin x=cos x`.

**W05.** Prove `(1+tan²x)cos²x=1`.

Domain: `cos x≠0`. Proof: `(1+tan²x)cos²x=sec²x cos²x=1`.

**W06.** Prove `(1+cot²x)sin²x=1`.

Domain: `sin x≠0`. Proof: `(1+cot²x)sin²x=csc²x sin²x=1`.

**W07.** Prove `(sec²x−1)/tan²x=1`.

Domain: `sin x cos x≠0`. Proof: `sec²x−1=tan²x`; divide by nonzero `tan²x`.

**W08.** Prove `(csc²x−1)/cot²x=1`.

Domain: `sin x cos x≠0`. Proof: `csc²x−1=cot²x`; divide by nonzero `cot²x`.

**W09.** Prove `sec²x/(1+tan²x)=1`.

Domain: `cos x≠0`. Proof: denominator equals `sec²x`, which is nonzero.

**W10.** Prove `csc²x/(1+cot²x)=1`.

Domain: `sin x≠0`. Proof: denominator equals `csc²x`, which is nonzero.

**W11.** Prove `(tan x+cot x)sin x cos x=1`.

Domain: `sin x cos x≠0`. Proof: `(tan x+cot x)sin x cos x=(sin²x+cos²x)=1`.

**W12.** Prove `(tan x+cot x)/(sec x csc x)=1`.

Domain: `sin x cos x≠0`. Proof: F15 gives identical numerator and denominator.

**W13.** Prove `tan²x/(sec x+1)=sec x−1`.

Domain: `cos x≠0` and `sec x+1≠0` (equivalently `cos x≠−1`). Proof: `tan²x=sec²x−1=(sec x−1)(sec x+1)`; cancel the nonzero factor.

**W14.** Prove `cot²x/(csc x+1)=csc x−1`.

Domain: `sin x≠0` and `csc x+1≠0` (equivalently `sin x≠−1`). Proof: `cot²x=csc²x−1=(csc x−1)(csc x+1)`; cancel.

**W15.** Prove `(sec x−1)(sec x+1)=tan²x`.

Domain: `cos x≠0`. Proof: difference of squares `sec²x−1=tan²x`.

**W16.** Prove `(csc x−1)(csc x+1)=cot²x`.

Domain: `sin x≠0`. Proof: `csc²x−1=cot²x`.

**W17.** Prove `sec x−cos x=sin x tan x`.

Domain: `cos x≠0`. Proof: `sec x−cos x=(1−cos²x)/cos x=sin²x/cos x=sin x tan x`.

**W18.** Prove `csc x−sin x=cos x cot x`.

Domain: `sin x≠0`. Proof: `csc x−sin x=(1−sin²x)/sin x=cos²x/sin x=cos x cot x`.

**W19.** Prove `sec x+cos x tan²x=sec x`.

Domain: `cos x≠0`. Proof: `cos x tan²x=sin²x/cos x`; thus `sec x+cos x tan²x=(1+sin²x)/cos x`, **not** `sec x` in general. **This is intentionally a false-claim detector.** Counterexample `x=π/4`: LHS `3√2/2`, RHS `√2`. Correct identity: `sec x−cos x=sin x tan x` (W17).

**W20.** Prove `sec x(1−sin²x)=cos x`.

Domain: `cos x≠0`. Proof: `sec x(1−sin²x)=(1/cos x)cos²x=cos x`.

## 8. Common denominators and conjugates (W21–W38)

**W21.** Prove `sin x/(1+cos x)=(1−cos x)/sin x`.

Domain: `sin x≠0`. Proof: multiply the left by `(1−cos x)/(1−cos x)` to get `sin x(1−cos x)/(1−cos²x)=(1−cos x)/sin x`.

**W22.** Prove `cos x/(1+sin x)=(1−sin x)/cos x`.

Domain: `cos x≠0`. Proof: multiply by `(1−sin x)/(1−sin x)` and use `1−sin²x=cos²x`.

**W23.** Prove `1/(1−sin x)=sec²x+tan x sec x`.

Domain: `cos x≠0`. Proof: `(1+sin x)/(1−sin²x)=(1+sin x)/cos²x=sec²x+tan x sec x`.

**W24.** Prove `1/(1+sin x)=sec²x−tan x sec x`.

Domain: `cos x≠0`. Proof: `(1−sin x)/cos²x=sec²x−tan x sec x`.

**W25.** Prove `1/(1−cos x)=csc²x+cot x csc x`.

Domain: `sin x≠0`. Proof: `(1+cos x)/sin²x=csc²x+cot x csc x`.

**W26.** Prove `1/(1+cos x)=csc²x−cot x csc x`.

Domain: `sin x≠0`. Proof: `(1−cos x)/sin²x=csc²x−cot x csc x`.

**W27.** Prove `sec x+tan x=(1+sin x)/cos x`.

Domain: `cos x≠0`. Proof: `1/cos x+sin x/cos x=(1+sin x)/cos x`.

**W28.** Prove `csc x+cot x=(1+cos x)/sin x`.

Domain: `sin x≠0`. Proof: `1/sin x+cos x/sin x=(1+cos x)/sin x`.

**W29.** Prove `sec x−tan x=cos x/(1+sin x)`.

Domain: `cos x≠0`. Proof: `(1−sin x)/cos x=cos x/(1+sin x)` by R03.

**W30.** Prove `csc x−cot x=sin x/(1+cos x)`.

Domain: `sin x≠0`. Proof: `(1−cos x)/sin x=sin x/(1+cos x)` by R01.

**W31.** Prove `(1+sin x)/(1−sin x)=(sec x+tan x)²`.

Domain: `cos x≠0`. Proof: `[(1+sin x)/cos x]²=(1+sin x)²/(1−sin²x)=(1+sin x)/(1−sin x)`.

**W32.** Prove `(1+cos x)/(1−cos x)=(csc x+cot x)²`.

Domain: `sin x≠0`. Proof: `[(1+cos x)/sin x]²=(1+cos x)²/(1−cos²x)`.

**W33.** Prove `(1−sin x)/(1+sin x)=(sec x−tan x)²`.

Domain: `cos x≠0`. Proof: use R09 or square W29 after simplifying.

**W34.** Prove `(1−cos x)/(1+cos x)=(csc x−cot x)²`.

Domain: `sin x≠0`. Proof: use R10 or square W30 after simplifying.

**W35.** Prove `(sec x+tan x)+(sec x−tan x)=2sec x`.

Domain: `cos x≠0`. Proof: the tangent terms cancel.

**W36.** Prove `(csc x+cot x)−(csc x−cot x)=2cot x`.

Domain: `sin x≠0`. Proof: the cosecant terms cancel.

**W37.** Prove `1/(sec x−tan x)−1/(sec x+tan x)=2tan x`.

Domain: `cos x≠0`. Proof: apply R05 and its conjugate to obtain `(sec x+tan x)−(sec x−tan x)`.

**W38.** Prove `1/(csc x−cot x)+1/(csc x+cot x)=2csc x`.

Domain: `sin x≠0`. Proof: conjugate reciprocity gives `(csc x+cot x)+(csc x−cot x)`.

## 9. Angle addition, multiplication, and factoring (W39–W56)

**W39.** Prove `sin(x+y)+sin(x−y)=2sin x cos y`.

Domain: all real. Proof: expand both sines by A01/A02; `cos x sin y` cancels.

**W40.** Prove `cos(x−y)−cos(x+y)=2sin x sin y`.

Domain: all real. Proof: expand A04 minus A03.

**W41.** Prove `sin(x+y)sin(x−y)=sin²x−sin²y`.

Domain: all real. Proof: multiply the conjugate expansions; use F08.

**W42.** Prove `cos(x+y)cos(x−y)=cos²x−sin²y`.

Domain: all real. Proof: multiply A03 and A04, simplify by F08.

**W43.** Prove `sin 3x/sin x=3−4sin²x`.

Domain: `sin x≠0`. Proof: D07 gives `sin 3x=sin x(3−4sin²x)`; divide.

**W44.** Prove `cos 3x/cos x=4cos²x−3`.

Domain: `cos x≠0`. Proof: D08 gives `cos 3x=cos x(4cos²x−3)`.

**W45.** Prove `sin 3x=sin x(1+2cos 2x)`.

Domain: all real. Proof: `sin x(1+2cos 2x)=sin x[1+2(1−2sin²x)]=3sin x−4sin³x`.

**W46.** Prove `cos 3x=cos x(2cos 2x−1)`.

Domain: all real. Proof: `cos x[2(2cos²x−1)−1]=4cos³x−3cos x`.

**W47.** Prove `sin 2x/(1+cos 2x)=tan x`.

Domain: `cos x≠0`. Proof: `sin 2x/(1+cos 2x)=(2sin x cos x)/(2cos²x)=tan x`.

**W48.** Prove `(1−cos 2x)/sin 2x=tan x`.

Domain: `sin x cos x≠0`. Proof: `(2sin²x)/(2sin x cos x)=tan x`. This representation excludes `sin x=0`, where `tan x` itself is defined.

**W49.** Prove `sin 2x/(1−cos 2x)=cot x`.

Domain: `sin x≠0`. Proof: `(2sin x cos x)/(2sin²x)=cot x`.

**W50.** Prove `(1+cos 2x)/sin 2x=cot x`.

Domain: `sin x cos x≠0`. Proof: `(2cos²x)/(2sin x cos x)=cot x`.

**W51.** Prove `sin²x−sin²y=sin(x+y)sin(x−y)`.

Domain: all real. Proof: rewrite `sin²x−sin²y` as `sin²x(1−sin²y)−sin²y(1−sin²x)` and factor into the conjugate sine expansions.

**W52.** Prove `cos²x−cos²y=−sin(x+y)sin(x−y)`.

Domain: all real. Proof: `cos²x−cos²y=(1−sin²x)−(1−sin²y)=−(sin²x−sin²y)`; use W41.

**W53.** Prove `sin x+sin 3x=2sin 2x cos x`.

Domain: all real. Proof: P05 with angles `x,3x`: `2sin 2x cos(−x)=2sin 2x cos x`.

**W54.** Prove `cos x+cos 3x=2cos 2x cos x`.

Domain: all real. Proof: P07 with angles `x,3x`.

**W55.** Prove `sin 3x−sin x=2cos 2x sin x`.

Domain: all real. Proof: P06 with angles `3x,x`.

**W56.** Prove `cos x−cos 3x=2sin 2x sin x`.

Domain: all real. Proof: P08 with angles `x,3x`: `−2sin 2x sin(−x)=2sin 2x sin x`.

## 10. Multi-function and conditional identities (W57–W76)

**W57.** Prove `sec²x csc²x=(tan x+cot x)²`.

Domain: `sin x cos x≠0`. Proof: both sides equal `1/(sin²x cos²x)` by B05.

**W58.** Prove `tan²x+cot²x=sec²x csc²x−2`.

Domain: `sin x cos x≠0`. Proof: expand `(tan x+cot x)²` and use `tan x cot x=1`.

**W59.** Prove `tan x+cot x=2csc 2x`.

Domain: `sin x cos x≠0`. Proof: `tan x+cot x=1/(sin x cos x)=2/(2sin x cos x)=2csc 2x`.

**W60.** Prove `tan x−cot x=−2cot 2x`.

Domain: `sin x cos x≠0`. Proof: `tan x−cot x=(sin²x−cos²x)/(sin x cos x)=−cos 2x/((sin 2x)/2)=−2cot 2x`.

**W61.** Prove `sec x csc x=2csc 2x`.

Domain: `sin x cos x≠0`. Proof: both sides equal `1/(sin x cos x)`.

**W62.** Prove `(sec x+tan x)(1−sin x)=cos x`.

Domain: `cos x≠0`. Proof: `[(1+sin x)/cos x](1−sin x)=(1−sin²x)/cos x=cos x`.

**W63.** Prove `(csc x+cot x)(1−cos x)=sin x`.

Domain: `sin x≠0`. Proof: `[(1+cos x)/sin x](1−cos x)=sin x`.

**W64.** Prove `(sec x−tan x)(1+sin x)=cos x`.

Domain: `cos x≠0`. Proof: `[(1−sin x)/cos x](1+sin x)=cos x`.

**W65.** Prove `(csc x−cot x)(1+cos x)=sin x`.

Domain: `sin x≠0`. Proof: `[(1−cos x)/sin x](1+cos x)=sin x`.

**W66.** Prove `tan(x+y)(1−tan x tan y)=tan x+tan y`.

Domain: `cos x cos y cos(x+y)≠0`. Proof: multiply A05 by its nonzero denominator.

**W67.** Prove `tan(x−y)(1+tan x tan y)=tan x−tan y`.

Domain: `cos x cos y cos(x−y)≠0`. Proof: multiply A06 by its nonzero denominator.

**W68.** Prove `sin(x+y)cos(x−y)+cos(x+y)sin(x−y)=sin 2x`.

Domain: all real. Proof: A01 applied to `(x+y)+(x−y)=2x`.

**W69.** Prove `sin(x+y)cos(x−y)−cos(x+y)sin(x−y)=sin 2y`.

Domain: all real. Proof: A02 applied to `(x+y)−(x−y)=2y`.

**W70.** Prove `cos(x+y)cos(x−y)−sin(x+y)sin(x−y)=cos 2x`.

Domain: all real. Proof: A03 applied to `(x+y)+(x−y)=2x`.

**W71.** Prove `cos(x+y)cos(x−y)+sin(x+y)sin(x−y)=cos 2y`.

Domain: all real. Proof: A04 applied to `(x+y)−(x−y)=2y`.

**W72.** If `A+B+C=π`, prove `sin(A+B)=sin C`.

Domain: all real `A,B,C` satisfying the condition. Proof: `sin(A+B)=sin(π−C)=sin C`.

**W73.** If `A+B+C=π`, prove `tan A+tan B+tan C=tan A tan B tan C`.

Domain: `cos A cos B cos C≠0`. Proof: `sin(A+B+C)=0`. Expanding via A01 twice gives `sin A cos B cos C+cos A sin B cos C+cos A cos B sin C−sin A sin B sin C=0`. Divide by `cos A cos B cos C`.

**W74.** If `A+B+C=π`, prove `cot A cot B+cot B cot C+cot C cot A=1`.

Domain: `sin A sin B sin C≠0`. Proof: `sin(A+B+C)=0`. Divide the same four-term expansion in W73 by `sin A sin B sin C`, yielding `cot B cot C+cot A cot C+cot A cot B−1=0`.

**W75.** If `A+B+C=π`, prove `cos²A+cos²B+cos²C+2cos A cos B cos C=1`.

Domain: all real `A,B,C` satisfying the condition. Proof: `cos C=−cos(A+B)=sin A sin B−cos A cos B`. Let `p=cos A cos B`, `q=sin A sin B`. Then `cos²C+2p cos C=(q−p)²+2p(q−p)=q²−p²`. Therefore `cos²A+cos²B+cos²C+2p cos C=cos²A+cos²B+sin²A sin²B−cos²A cos²B=1` after using `sin²A=1−cos²A`, `sin²B=1−cos²B`.

**W76.** If `A+B+C=π`, prove `sin 2A+sin 2B+sin 2C=4sin A sin B sin C`.

Domain: all real `A,B,C` satisfying the condition. Proof: `sin 2A+sin 2B=2sin(A+B)cos(A−B)=2sin C cos(A−B)`; `sin 2C=2sin C cos C=−2sin C cos(A+B)`. Add and use `cos(A−B)−cos(A+B)=2sin A sin B`.

## 11. Advanced algebraic and compound-angle patterns (W77–W96)

**W77.** Prove `sin⁴x+cos⁴x=1−(1/2)sin²2x`.

Domain: all real. Proof: `(sin²x+cos²x)²−2sin²x cos²x=1−(1/2)sin²2x`.

**W78.** Prove `sin⁶x+cos⁶x=1−(3/4)sin²2x`.

Domain: all real. Proof: with `a=sin²x`, `b=cos²x`, `a³+b³=(a+b)³−3ab(a+b)=1−3sin²x cos²x`.

**W79.** Prove `sin⁴x−cos⁴x=−cos 2x`.

Domain: all real. Proof: `(sin²x−cos²x)(sin²x+cos²x)=−cos 2x`.

**W80.** Prove `cos⁴x−sin⁴x=cos 2x`.

Domain: all real. Proof: difference of squares and F08.

**W81.** Prove `sin²x cos²y−cos²x sin²y=sin²x−sin²y`.

Domain: all real. Proof: replace `cos²y=1−sin²y` and `cos²x=1−sin²x`; mixed terms cancel.

**W82.** Prove `(sin x+cos x)²=1+sin 2x`.

Domain: all real. Proof: expand to `sin²x+cos²x+2sin x cos x`.

**W83.** Prove `(sin x−cos x)²=1−sin 2x`.

Domain: all real. Proof: expand and use D01.

**W84.** Prove `(sin x+cos x)(sin x−cos x)=−cos 2x`.

Domain: all real. Proof: `sin²x−cos²x=−cos 2x`.

**W85.** Prove `(sin x+cos x)⁴+(sin x−cos x)⁴=2+8sin²x cos²x+2sin²2x`.

Domain: all real. Proof: Let `u=sin x+cos x`, `v=sin x−cos x`; `u²=1+sin 2x`, `v²=1−sin 2x`. Then `u⁴+v⁴=2+2sin²2x=2+8sin²x cos²x`. **The displayed proposed right side double-counts the same term and is false in general.** At `x=π/4`, LHS `4`, proposed RHS `6`. Correct identity: `(sin x+cos x)⁴+(sin x−cos x)⁴=2+2sin²2x`.

**W86.** Prove `sin⁴x+cos⁴x=(3+cos 4x)/4`.

Domain: all real. Proof: W77 gives `1−(1/2)sin²2x=1−(1−cos 4x)/4=(3+cos 4x)/4`.

**W87.** Prove `sin²x cos²x=(1−cos 4x)/8`.

Domain: all real. Proof: `sin²x cos²x=(1/4)sin²2x=(1/8)(1−cos 4x)`.

**W88.** Prove `sin x sin 2x sin 3x=[cos 2x−cos 4x−cos 0+cos 6x]/8`.

Domain: all real. **False-claim detector.** At `x=π/6`, LHS `1/2·√3/2·1=√3/4`, proposed RHS `(1/2−(−1/2)−1+(−1))/8=−1/8`. A correct product-to-sum expansion is `sin x sin 2x sin 3x=[sin 2x+sin 4x−sin 6x]/4`: first use `2sin x sin 3x=cos 2x−cos 4x`, multiply by `sin 2x`, then use P02 on both terms.

**W89.** Prove `sin x sin 2x sin 3x=[sin 2x+sin 4x−sin 6x]/4`.

Domain: all real. Proof: `4sin x sin 2x sin 3x=2sin 2x(cos 2x−cos 4x)=sin 4x−[sin 6x+sin(−2x)]=sin 2x+sin 4x−sin 6x`.

**W90.** Prove `cos x cos 2x cos 3x=[cos 0+cos 2x+cos 4x+cos 6x]/4`.

Domain: all real. Proof: `2cos x cos 3x=cos 4x+cos 2x`; multiply by `2cos 2x`: `4cos x cos 2x cos 3x=cos 6x+cos 2x+cos 4x+1`.

**W91.** Prove `sin x+sin 2x+sin 3x=sin 2x(1+2cos x)`.

Domain: all real. Proof: P05 gives `sin x+sin 3x=2sin 2x cos x`; add `sin 2x`.

**W92.** Prove `cos x+cos 2x+cos 3x=cos 2x(1+2cos x)`.

Domain: all real. Proof: P07 gives `cos x+cos 3x=2cos 2x cos x`; add `cos 2x`.

**W93.** Prove `sec(x+y)(1−tan x tan y)=sec x sec y`.

Domain: `cos x cos y cos(x+y)≠0`. Proof: apply A18 and multiply by its nonzero denominator.

**W94.** Prove `sec(x−y)(1+tan x tan y)=sec x sec y`.

Domain: `cos x cos y cos(x−y)≠0`. Proof: apply A19 and multiply by its nonzero denominator.

**W95.** Prove `csc(x+y)(cot x+cot y)=csc x csc y`.

Domain: `sin x sin y sin(x+y)≠0`. Proof: apply A20 and multiply by its nonzero denominator.

**W96.** Prove `csc(x−y)(cot y−cot x)=csc x csc y`.

Domain: `sin x sin y sin(x−y)≠0`. Proof: apply A21 and multiply by its nonzero denominator.

---

# PART IV — PROOF STRATEGIES, DECISION RULES, AND FAILURE MODES

## 12. Proof-method routing table

| Symptom in problem | First-choice move | Reference |
|---|---|---|
| Mix of `tan`, `cot`, `sec`, `csc` | Replace by sine/cosine, or apply Pythagorean pairs | F01–F17, B01–B12 |
| `1±sin x` or `1±cos x` in denominators | Multiply by conjugate | R01–R16, B59–B74 |
| `sec x±tan x` or `csc x±cot x` | Multiply paired factors; use difference of squares | F16–F17, R05–R10 |
| Two different denominators | Common denominator; factor `sin²+cos²` | W11, W21–W26 |
| `sin 2x`, `cos 2x` | Double-angle; choose convenient form | D01–D06 |
| `sin 3x`, `cos 3x` | Triple-angle polynomial or factor out sin/cos | D07–D10, W43–W46 |
| `sin x±sin y`, `cos x±cos y` | Sum-to-product | P05–P08 |
| Products `sin x cos y`, `sin x sin y` | Product-to-sum | P01–P04 |
| `sin²x`, `cos²x`, fourth powers | Power reduction | H10–H15, W77–W87 |
| `sin x+cos x` | Square, factor, or phase shift | P09–P12, W82–W84 |
| Expressions involving `x/2` | Half-angle, sign and domain check | H01–H21 |
| `sin(nx)` or `cos(nx)` | Addition and recurrences | D13–D16 |
| `A+B+C=π` | Replace `C=π−A−B` or expand `sin(A+B+C)=0` | W72–W76 |
| Asked to show expression is constant | Rewrite in terms of one trig function and simplify | F08–F10 |
| Equality looks suspicious | Numerical counterexample on common domain, then symbolic verification | Section 14 |
| Need to solve equation, not identity | Factor, enumerate zero cases, check periodic families and exclusions | Section 15 |

### 12.1 Proof discipline

- **LHS-only:** Start with `LHS = ... = RHS`. Do not start by writing `LHS=RHS` and transform it as though it were known true.
- **Common target:** `LHS = T` and separately `RHS = T` is valid.
- **Difference method:** `LHS−RHS=0` is valid if every step is reversible or is a direct simplification on the common domain.
- **Cross-multiplication:** `a/b=c/d` can be reduced to `ad=bc` only where `b≠0` and `d≠0`; reverse reasoning must retain those restrictions.
- **Squaring:** `L=R ⇒ L²=R²`, but `L²=R²` alone allows `L=−R`. Add sign information or check both possibilities.
- **Square roots:** `√(u²)=|u|`, **not** generally `u`.
- **Cancellation:** `ab/ac=b/c` only if `a≠0` and `c≠0`; keep the original domain even after simplifying.
- **Division by trig functions:** `sin x`, `cos x`, `tan x`, etc. may be zero; split into cases if proving an equation involving all possible `x`.
- **Identity vs equation:** An identity holds throughout its domain. An equation may hold only for a subset of angles; do not call a solved equation an identity.

## 13. Domain-safe transformation examples

**E01 — Removable expression hole.** `(sin²x)/sin x=sin x` is an identity only for `sin x≠0`; at `x=0`, the left side is undefined despite the simplified right side being zero.

**E02 — Different domains, same values on overlap.** `(1−cos x)/sin x=sin x/(1+cos x)` on `sin x≠0`; the right expression is defined at `x=0` but the left is not.

**E03 — Division can lose solutions.** `sin x cos x=sin x` implies `sin x(cos x−1)=0`, hence `x=kπ`. Dividing by `sin x` would discard all solutions because every solution has `sin x=0`.

**E04 — Square-root sign.** `√(1−sin²x)=|cos x|`, not always `cos x`; at `x=π`, the square root is `1` while `cos π=−1`.

**E05 — Tangent addition has a hidden hole.** At `x=y=π/4`, `tan x=tan y=1` but `tan(x+y)=tan(π/2)` is undefined, matching the zero denominator `1−tan x tan y=0`.

**E06 — Half-angle ambiguity.** `√((1−cos x)/2)=|sin(x/2)|`; at `x=3π`, the right-hand `sin(3π/2)=−1` while the square root is `1`.

**E07 — Avoid unjustified inverse steps.** From `sin x=sin y`, do not infer `x=y`. Valid families are `x=y+2kπ` or `x=π−y+2kπ`.

**E08 — Trig denominator created by substitution.** Replacing `tan x` with `sin x/cos x` requires `cos x≠0`; do not cancel `cos x` and then enlarge the original domain.

## 14. False identity / hallucination detector

The following are **not** identities. A proof assistant must refuse to prove them and provide a counterexample.

| False claim | Counterexample / correction |
|---|---|
| `sin(x+y)=sin x+sin y` | `x=y=π/2`: LHS `0`, RHS `2`; use A01 |
| `cos(x+y)=cos x+cos y` | `x=y=0`: LHS `1`, RHS `2`; use A03 |
| `tan(x+y)=tan x+tan y` | `x=y=π/6`: LHS `√3`, RHS `2/√3`; use A05 |
| `sin²x=sin(x²)` | `x=π/2`: LHS `1`, RHS generally not `1` |
| `sin²x+cos²x=2` | At `x=0`, LHS `1` |
| `sec²x+tan²x=1` | At `x=π/4`, LHS `3`; correct: `sec²x−tan²x=1` |
| `csc²x+cot²x=1` | At `x=π/4`, LHS `3`; correct: `csc²x−cot²x=1` |
| `√(sin²x)=sin x` | At `x=3π/2`, LHS `1`, RHS `−1` |
| `tan x=1/cot x` everywhere `tan` exists | At `x=0`, `tan x=0` but `cot x` undefined |
| `sin 2x=2sin x` | At `x=π/3`, LHS `√3/2`, RHS `√3`; correct: `2sin x cos x` |
| `cos 2x=2cos x` | At `x=0`, LHS `1`, RHS `2` |
| `sin x/sin x=1` for all real `x` | Undefined at `x=kπ`; valid only for `sin x≠0` |
| `sin x+cos x=1` | At `x=π/4`, LHS `√2` |
| `tan²x=sec²x+1` | At `x=0`, LHS `0`, RHS `2`; correct: `sec²x−1` |
| `sin(x−y)=sin x−sin y` | `x=π/2`, `y=π/6`: LHS `√3/2`, RHS `1/2` |

**Counterexample protocol:** Choose angles where *both* sides are defined; compute exact values where possible; a single mismatch disproves a proposed identity. A numerical agreement at a few angles does **not** prove an identity.

## 15. Equation-solving templates (use only when a problem is an equation)

The following are solution families, not identities:

| Equation | General real solutions |
|---|---|
| `sin x=0` | `x=kπ` |
| `cos x=0` | `x=π/2+kπ` |
| `tan x=0` | `x=kπ` |
| `cot x=0` | `x=π/2+kπ` |
| `sin x=sin y` | `x=y+2kπ` or `x=π−y+2kπ` |
| `cos x=cos y` | `x=2kπ+y` or `x=2kπ−y` |
| `tan x=tan y` | `x=y+kπ`, with both tangents defined |
| `cot x=cot y` | `x=y+kπ`, with both cotangents defined |
| `sin²x=cos²x` | `x=π/4+kπ/2` |
| `sin 2x=0` | `x=kπ/2` |
| `cos 2x=0` | `x=π/4+kπ/2` |
| `tan x=1` | `x=π/4+kπ` |
| `tan x=−1` | `x=−π/4+kπ` |

For more general equations, transform using the proof identities, **factor without dividing away zeros**, enumerate all periodic families, and check against the **original** equation's domain.

## 16. Inequalities derivable from the six functions

These can support proofs of bounds, but they are not equality identities.

| ID | Statement | Proof idea / domain |
|---|---|---|
| I01 | `−1≤sin x≤1`, `−1≤cos x≤1` | unit circle |
| I02 | `0≤sin²x≤1`, `0≤cos²x≤1` | squares and F08 |
| I03 | `|sin x cos x|≤1/2` | `|sin 2x|≤1` |
| I04 | `|sin x+cos x|≤√2` | P09 and I01 |
| I05 | `|a sin x+b cos x|≤√(a²+b²)` | P11/P12; `a=b=0` trivial |
| I06 | `sec²x≥1` | F09 on `cos x≠0` |
| I07 | `csc²x≥1` | F10 on `sin x≠0` |
| I08 | `tan²x+cot²x≥2` | for `sin x cos x≠0`, `(tan x−cot x)²≥0` and `tan x cot x=1` |
| I09 | `|sin x|+|cos x|≥1` | square left; it is `1+2|sin x cos x|≥1` |
| I10 | `1≤|sin x|+|cos x|≤√2` | lower I09; upper square and I03 |

## 17. Common exam proof prompts and recommended routes

| Prompt type | Typical target | Suggested approach |
|---|---|---|
| Verify an identity | `sec x−cos x=sin x tan x` | sine/cosine substitution (W17) |
| Rationalize | `(1−cos x)/sin x=sin x/(1+cos x)` | conjugate (W21) |
| Double-angle simplification | `sin 2x/(1+cos 2x)=tan x` | D01/D04 (W47) |
| Prove a triple-angle | `sin 3x=3sin x−4sin³x` | addition formula (B24) |
| Convert sum to product | `sin x+sin 3x` | P05 (W53) |
| Convert product to sum | `sin x sin 3x` | P04 |
| High-power simplification | `sin⁶x+cos⁶x` | `a³+b³` factoring (W78) |
| Angle condition | `A+B+C=π` | W72–W76 |
| Detect a false statement | `sin(x+y)=sin x+sin y` | exact counterexample (Section 14) |
| General multiple angle | `sin(nx)`, `cos(nx)` | recurrence D13–D16 |

---

# PART V — QUALITY ASSURANCE AND EXTENSION RULES

## 18. Validation checklist

Before presenting a final proof, confirm:

- [ ] All six-function expressions and their original domains were parsed correctly.
- [ ] Every substitution is valid on the domain being considered.
- [ ] No denominator was assumed nonzero without checking.
- [ ] No square root lost an absolute value or sign.
- [ ] No step divided by a possibly zero factor while solving an equation.
- [ ] All angle addition and sign formulas use the correct signs.
- [ ] All introduced formulas are either derived or indexed above.
- [ ] The proof is not circular (the desired identity was not assumed).
- [ ] If the claim is false, a **permissible** counterexample is supplied.
- [ ] The conclusion states the common domain, not an unjustified larger set.

## 19. How to extend this database

When adding an identity, create a new entry with these fields:

```text
ID: [unique stable ID]
Claim: [exact symbolic identity]
Domain: [original common domain, including all restrictions]
Method: [reciprocal | Pythagorean | addition | multiple-angle | conjugate | factor | product-to-sum | other]
Dependencies: [IDs of previously justified formulas]
Proof: [finite, logically ordered equalities]
Edge cases: [holes, sign cases, zero factors, non-equivalent transformations]
Countercheck: [at least two allowed test angles, when useful]
```

**Extension policy:** Prefer adding genuinely new proof structures rather than endlessly repeating equivalent cosmetic variations. Maintain all six functions in scope; do not introduce inverse trigonometric, hyperbolic, complex, exponential, or calculus tools unless a future user explicitly expands the skill's scope.

## 20. Retrieval keywords / quick index

- **Basic:** F01–F20, B01–B12, W01–W20.
- **Parity and cofunctions:** S01–S18, B10–B12.
- **Addition and subtraction:** A01–A21, B13–B19, B77–B80, W39–W42, W66–W71, W93–W96.
- **Double and triple angles:** D01–D12, B20–B29, W43–W50.
- **Arbitrary multiple angles:** D13–D16, B30–B33.
- **Half angles:** H01–H09, B45–B49.
- **Power reduction:** H10–H15, B50–B54, W77–W87.
- **Weierstrass/tangent half-angle:** H16–H21, B55.
- **Product-to-sum and sum-to-product:** P01–P08, B37–B44, W53–W56, W89–W92.
- **Phase shifts and amplitude:** P09–P12, B56–B57.
- **Conjugates and rationalization:** R01–R18, B59–B76, W21–W38.
- **Triangle-angle conditions:** W72–W76.
- **Inequalities:** I01–I10.
- **False claims and pitfalls:** W19, W85, W88, Sections 13–14.
- **Equation solution families:** Section 15.

---

## 21. Integrity note

The indexed collection contains **20 fundamental, 18 symmetry, 21 addition, 16 multiple-angle, 21 half-angle/power/substitution, 12 product/sum/phase, and 18 rationalization identities**, plus **80 explicit derivation proofs, 96 worked examples (including three deliberately flagged false claims), 10 inequalities, and equation-solving templates**. These are a **finite proof library**, not a claim that all possible trigonometric identities have been enumerated. Treat the clearly labeled false claims as negative test cases, never as theorems.


---

# v0.6.0 — Reusable theorem admission and parameterised algebra

## 21. Reuse F08–F10 without circularity

Theorem admission distinguishes a theorem being used as a premise from the same theorem being assumed as its own proof.

1. **F08 target:** prove through the independent geometric certificate `G01 → G03 → G04`. Do not use F08, F09 or F10 as premises for an F08 goal or a constant-scaled/rearranged instance.
2. **F09 target:** derive from F08, F01 and F03. F09 itself is unavailable as a premise while its goal is open.
3. **F10 target:** derive from F08, F02 and F04. F10 itself is unavailable as a premise while its goal is open.
4. **Different target:** F08, F09 and F10 may be used when their exact theorem statements are genuine intermediate steps in proving another identity. Recursively check their dependency chains and domains.
5. **Goal matching:** block direct instances, reversals, angle renamings, and nonzero constant-scaled/rearranged forms. Do not block every identity whose residual is a nonconstant algebraic multiple of a theorem residual; that would prevent valid reuse. If instance matching exceeds its safety bound, fail closed.
6. **Provenance:** F08 is trusted only after replay of its geometric certificate. F09 and F10 inherit that foundation through their audited definitions. A catalogue label, old `PROVED` flag, or unverified prose proof is not authority.

## 22. Algebraic preprocessing for squared linear combinations

Before matching identities, the engine may apply a narrow exact-algebra preprocessing pass when a source expression contains a positive integer power of an additive base:

- expand squared sums using distributivity;
- collect terms by common parameter factors;
- expose a subexpression such as `sin(x)**2 + cos(x)**2`;
- apply the established identity as an explicit proof step.

This preprocessing is polynomial algebra only. It must not call `trigsimp`, silently use a trigonometric identity, or erase original domain restrictions.

### Worked reusable-theorem example

For real `p`, `q`, and `x`, prove

`(p*cos(x)+q*sin(x))**2 + (p*sin(x)-q*cos(x))**2 = p**2+q**2`.

Expand the squares and collect terms:

`p**2*cos(x)**2 + 2*p*q*sin(x)*cos(x) + q**2*sin(x)**2 + p**2*sin(x)**2 - 2*p*q*sin(x)*cos(x) + q**2*cos(x)**2`

`= (p**2+q**2)*(sin(x)**2+cos(x)**2)`

Apply F08 to obtain `p**2+q**2`. The proof certificate must list F08 as the explicit premise and retain its dependency on `G01 → G03 → G04`.

### False near-miss

`(p*cos(x)+q*sin(x))**2 + (p*sin(x)-p*cos(x))**2 = p**2+q**2` is false in general. At `p=1`, `q=0`, `x=0`, the two sides are `2` and `1`. Do not add it to the proved question bank.


**Angle-binding restriction for reverse F08:** when the reverse rule matches a literal `1`, the engine may infer the theorem angle only if exactly one trigonometric argument is shared by the current source expression and requested target. If there are zero or multiple shared angles, no contextual substitution is made. This is a narrow, deterministic binding rule, not arbitrary variable guessing.
