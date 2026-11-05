# Trigonometric Proof Engine v0.6.0 — Proof Solutions

**Companion question bank:** `question-bank.md`  
**Purpose:** checked proof derivations for all entries in the v0.6.0 question bank.

## 1. Proof policy

- Every listed solution corresponds to a question whose engine status is `PROVED`.
- Each algebraic expansion, factorisation and theorem application is shown as a separate step.
- F08/F09/F10 are reusable premises only when the requested goal is not the same theorem (or a constant-scaled/rearranged version of it).
- F08 has an independent geometric certificate; F09 and F10 inherit that audited foundation through F01/F03 and F02/F04 respectively.
- Domain restrictions from the original expressions remain in force throughout the proof.

## 2. Solutions for the finite operation-template bank


---

## a + b = c

No proved entry was generated for this operation template in the stated finite search space.

---

## a - b = c

No proved entry was generated for this operation template in the stated finite search space.

---

## ab = c

### QB-03-001 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-002 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-003 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-004 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-005 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-006 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-007 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-008 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-009 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-010 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-011 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-012 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-013 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-014 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-015 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-03-016 — `1 = 1`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## a/b = c

### QB-04-001 — `1 = 1`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-002 — `sin(x)/tan(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-003 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-004 — `cos(x)/cot(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-005 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-006 — `tan(x)/sin(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-007 — `tan(x)/sec(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-008 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-009 — `cot(x)/cos(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-010 — `cot(x)/csc(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-011 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-012 — `sec(x)/tan(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-013 — `sec(x)/csc(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F01`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-014 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-015 — `csc(x)/cot(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-016 — `csc(x)/sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-017 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-018 — `1/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-019 — `1/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-020 — `1/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-04-021 — `1/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab + c = d

### QB-05-001 — `sin(x)*tan(x) + cos(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F08`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/cos(x)` → `(sin(x)**2 + cos(x)**2)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*sec(x)` → `sec(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-05-002 — `sin(x) + cos(x)*cot(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F08`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `sin(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/sin(x)` → `(sin(x)**2 + cos(x)**2)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*csc(x)` → `csc(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04


---

## ab - c = d

### QB-06-001 — `-tan(x) + csc(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F01, F08, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-tan(x) + csc(x)*sec(x)` → `-tan(x) + csc(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `-tan(x) + csc(x)/cos(x)` → `-(cos(x)*tan(x) - csc(x))/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x)*tan(x) - csc(x))/cos(x)` → `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` → `-tan(x) + 1/(sin(x)*cos(x))`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-tan(x) + 1/(sin(x)*cos(x))` → `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))` → `-(sin(x)**2 - 1)/(sin(x)*cos(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
7. `-(sin(x)**2 - 1)/(sin(x)*cos(x))` → `-sin(x)/cos(x) + 1/(sin(x)*cos(x))`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
8. `-sin(x)/cos(x) + 1/(sin(x)*cos(x))` → `(1 - sin(x)**2)/(sin(x)*cos(x))`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
9. `(1 - sin(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
10. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-06-002 — `-cot(x) + csc(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04, F08, F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-cot(x) + csc(x)*sec(x)` → `csc(x)*sec(x) - cos(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `csc(x)*sec(x) - cos(x)/sin(x)` → `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)` → `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` → `csc(x)/cos(x) - cos(x)/sin(x)`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `csc(x)/cos(x) - cos(x)/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))` → `(1 - cos(x)**2)/(sin(x)*cos(x))` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
7. `(1 - cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
8. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04


---

## abc = d

### QB-07-001 — `sin(x)**2*csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)**2*csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-002 — `sin(x)*cos(x)*sec(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*cos(x)*sec(x)` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-003 — `sin(x)*cos(x)*csc(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-004 — `sin(x)*tan(x)*cot(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*tan(x)*cot(x)` → `sin(x)**2*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)**2*cot(x)/cos(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-005 — `sin(x)*tan(x)*csc(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*tan(x)*csc(x)` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-006 — `sin(x)*cot(x)*sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)*sec(x)` → `cos(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-007 — `sin(x)*cot(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)*csc(x)` → `cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-008 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-009 — `sin(x)*csc(x)*sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-010 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-011 — `sin(x)*csc(x)**2 = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)**2` → `1/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-012 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-013 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-014 — `cos(x)**2*sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)**2*sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-015 — `cos(x)*tan(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)*cot(x)` → `sin(x)*cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-016 — `cos(x)*tan(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)*sec(x)` → `tan(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-017 — `cos(x)*tan(x)*csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)*csc(x)` → `sin(x)*csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-018 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-019 — `cos(x)*cot(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*cot(x)*sec(x)` → `cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-020 — `cos(x)*sec(x)**2 = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)**2` → `1/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-021 — `cos(x)*csc(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-022 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-023 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-024 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-025 — `tan(x)**2*cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)**2*cot(x)` → `sin(x)**2*cot(x)/cos(x)**2` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)**2*cot(x)/cos(x)**2` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-026 — `tan(x)*cot(x)**2 = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)**2` → `sin(x)*cot(x)**2/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)**2/cos(x)` → `cos(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-027 — `tan(x)*cot(x)*sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-028 — `tan(x)*cot(x)*csc(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-029 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-030 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-031 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-032 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-033 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-034 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-035 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-07-036 — `1 = 1`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab/c = d

### QB-08-001 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-002 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-003 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-004 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-005 — `sin(x)*cot(x)/cos(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-006 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-007 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-008 — `sin(x)*sec(x)/tan(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)/tan(x)` → `cos(x)*sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-009 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-010 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-011 — `sin(x)*csc(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-012 — `sin(x)*csc(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/tan(x)` → `cos(x)*csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-013 — `sin(x)*csc(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/cot(x)` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-014 — `sin(x)*csc(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-015 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-016 — `1 = 1`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-017 — `sin(x)/tan(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-018 — `cos(x)*tan(x)/sin(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)/sin(x)` → `1` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-019 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-020 — `cos(x)*sec(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-021 — `cos(x)*sec(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/tan(x)` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-022 — `cos(x)*sec(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-023 — `cos(x)*sec(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-024 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-025 — `cos(x)*csc(x)/cot(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-026 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-027 — `cos(x)/cot(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-028 — `tan(x)*cot(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/sin(x)` → `tan(x)*cot(x)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-029 — `tan(x)*cot(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/cos(x)` → `tan(x)*cot(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-030 — `tan(x)*cot(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/sec(x)` → `sin(x)*cot(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-031 — `tan(x)*cot(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/csc(x)` → `sin(x)*cot(x)/(cos(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-032 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-033 — `tan(x)*csc(x)/sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)/sec(x)` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-034 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-035 — `tan(x)/sin(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-036 — `tan(x)/sec(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-037 — `cot(x)*sec(x)/csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)/csc(x)` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-038 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-039 — `cot(x)/cos(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-040 — `cot(x)/csc(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-041 — `sec(x)/tan(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-042 — `sec(x)/csc(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F01`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-043 — `csc(x)/cot(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-044 — `csc(x)/sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-045 — `1/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-046 — `1/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-047 — `1/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-08-048 — `1/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab + cd = e

### QB-09-001 — `sin(x)**2 + cos(x)**2 = 1`

**Status:** `PROVED`  
**Selected route:** `GEO: G01 → G03 → G04`  
**Identity/proof IDs:** `G01, G03, G04`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

1. **G01 — Euclidean Pythagorean theorem.** A square-dissection proof establishes the non-trigonometric relation `u**2 + v**2 = r**2` for a right triangle.
2. **G03 — Cartesian squared distance.** Perpendicular projections of a point `(u,v)` give `OP**2 = u**2 + v**2`, with signed coordinates and axis cases handled.
3. **G04 — Unit-circle substitution.** The point `(cos(x), sin(x))` has radius `1`; hence `cos(x)**2 + sin(x)**2 = 1` for every real `x`.
4. **Conclusion.** The requested F08 instance follows from the checked geometric certificate. F08 is not used as a premise in its own proof.

**Certificate:** `trigonometric-geometric-proof-certificate-v1` — `PROVED`.

### QB-09-002 — `sin(x)*tan(x) + sin(x)*cot(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F01, F03, F08`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*tan(x) + sin(x)*cot(x)` → `sin(x)*tan(x) + cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)/cos(x)` → `(sin(x)**2 + cos(x)**2)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
5. `(sin(x)**2 + cos(x)**2)*sec(x)` → `sec(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-09-003 — `sin(x)*tan(x) + cos(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F08`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/cos(x)` → `(sin(x)**2 + cos(x)**2)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*sec(x)` → `sec(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-09-004 — `sin(x) + cos(x)*cot(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F08`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `sin(x) ≠ 0`
3. `(sin(x)**2 + cos(x)**2)/sin(x)` → `(sin(x)**2 + cos(x)**2)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)*csc(x)` → `csc(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-09-005 — `cos(x)*tan(x) + cos(x)*cot(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F04, F08`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x) + cos(x)*cot(x)` → `sin(x) + cos(x)*cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `sin(x) ≠ 0`
4. `(sin(x)**2 + cos(x)**2)/sin(x)` → `(sin(x)**2 + cos(x)**2)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
5. `(sin(x)**2 + cos(x)**2)*csc(x)` → `csc(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04


---

## ab - cd = e

### QB-10-001 — `-sin(x)*tan(x) + tan(x)*csc(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F01, F08`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-sin(x)*tan(x) + tan(x)*csc(x)` → `-sin(x)*tan(x) + tan(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `-sin(x)*tan(x) + tan(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)*tan(x)/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(sin(x) - 1)*(sin(x) + 1)*tan(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `-(sin(x) - 1)*(sin(x) + 1)/cos(x)` → `-sin(x)**2/cos(x) + 1/cos(x)`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`
5. `-sin(x)**2/cos(x) + 1/cos(x)` → `(1 - sin(x)**2)/cos(x)`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`
6. `(1 - sin(x)**2)/cos(x)` → `cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-002 — `-cos(x)*cot(x) + cot(x)*sec(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F02, F08`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-cos(x)*cot(x) + cot(x)*sec(x)` → `-cos(x)*cot(x) + cot(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `-cos(x)*cot(x) + cot(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)*cot(x)/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x) - 1)*(cos(x) + 1)*cot(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `-(cos(x) - 1)*(cos(x) + 1)/sin(x)` → `-cos(x)**2/sin(x) + 1/sin(x)`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `sin(x) ≠ 0`
5. `-cos(x)**2/sin(x) + 1/sin(x)` → `(1 - cos(x)**2)/sin(x)`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `sin(x) ≠ 0`
6. `(1 - cos(x)**2)/sin(x)` → `sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-003 — `-sin(x)*sec(x) + csc(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F03, F08, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-sin(x)*sec(x) + csc(x)*sec(x)` → `-sin(x)*sec(x) + sec(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `-sin(x)*sec(x) + sec(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)*sec(x)/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(sin(x) - 1)*(sin(x) + 1)*sec(x)/sin(x)` → `-(sin(x) - 1)*(sin(x) + 1)/(sin(x)*cos(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `-(sin(x) - 1)*(sin(x) + 1)/(sin(x)*cos(x))` → `-sin(x)/cos(x) + 1/(sin(x)*cos(x))`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-sin(x)/cos(x) + 1/(sin(x)*cos(x))` → `(1 - sin(x)**2)/(sin(x)*cos(x))`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(1 - sin(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
7. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-004 — `-cos(x)*csc(x) + csc(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F08, F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-cos(x)*csc(x) + csc(x)*sec(x)` → `-cos(x)*csc(x) + csc(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `-cos(x)*csc(x) + csc(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)*csc(x)/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x) - 1)*(cos(x) + 1)*csc(x)/cos(x)` → `-(cos(x) - 1)*(cos(x) + 1)/(sin(x)*cos(x))` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `-(cos(x) - 1)*(cos(x) + 1)/(sin(x)*cos(x))` → `-cos(x)/sin(x) + 1/(sin(x)*cos(x))`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-cos(x)/sin(x) + 1/(sin(x)*cos(x))` → `(1 - cos(x)**2)/(sin(x)*cos(x))`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(1 - cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
7. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-005 — `-tan(x) + csc(x)*sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F01, F08, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-tan(x) + csc(x)*sec(x)` → `-tan(x) + csc(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `-tan(x) + csc(x)/cos(x)` → `-(cos(x)*tan(x) - csc(x))/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(cos(x)*tan(x) - csc(x))/cos(x)` → `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `-(cos(x)*tan(x) - 1/sin(x))/cos(x)` → `-tan(x) + 1/(sin(x)*cos(x))`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `-tan(x) + 1/(sin(x)*cos(x))` → `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `-(sin(x)*cos(x)*tan(x) - 1)/(sin(x)*cos(x))` → `-(sin(x)**2 - 1)/(sin(x)*cos(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
7. `-(sin(x)**2 - 1)/(sin(x)*cos(x))` → `-sin(x)/cos(x) + 1/(sin(x)*cos(x))`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
8. `-sin(x)/cos(x) + 1/(sin(x)*cos(x))` → `(1 - sin(x)**2)/(sin(x)*cos(x))`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
9. `(1 - sin(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
10. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-006 — `-cot(x) + csc(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04, F08, F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `-cot(x) + csc(x)*sec(x)` → `csc(x)*sec(x) - cos(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `csc(x)*sec(x) - cos(x)/sin(x)` → `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
3. `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)` → `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `-(-sin(x)*csc(x)/cos(x) + cos(x))/sin(x)` → `csc(x)/cos(x) - cos(x)/sin(x)`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
5. `csc(x)/cos(x) - cos(x)/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`
6. `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))` → `(1 - cos(x)**2)/(sin(x)*cos(x))` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
7. `(1 - cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
8. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-007 — `-sin(x)*tan(x) + sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F08`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `-sin(x)*tan(x) + sec(x)` → `-sin(x)**2/cos(x) + sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `-sin(x)**2/cos(x) + sec(x)` → `(-sin(x)**2 + cos(x)*sec(x))/cos(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `cos(x) ≠ 0`
3. `(-sin(x)**2 + cos(x)*sec(x))/cos(x)` → `(1 - sin(x)**2)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `(1 - sin(x)**2)/cos(x)` → `cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### QB-10-008 — `-cos(x)*cot(x) + csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F08`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `-cos(x)*cot(x) + csc(x)` → `csc(x) - cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `csc(x) - cos(x)**2/sin(x)` → `-(-sin(x)*csc(x) + cos(x)**2)/sin(x)`
   - Justification: Factor a sum of rational terms to expose common algebraic structure; no trigonometric identity is used.
   - Conditions: `sin(x) ≠ 0`
3. `-(-sin(x)*csc(x) + cos(x)**2)/sin(x)` → `-(cos(x)**2 - 1)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `-(cos(x)**2 - 1)/sin(x)` → `-cos(x)**2/sin(x) + 1/sin(x)`
   - Justification: Distribute the factor -1 over an additive expression; no trigonometric identity is used.
   - Conditions: `sin(x) ≠ 0`
5. `-cos(x)**2/sin(x) + 1/sin(x)` → `(1 - cos(x)**2)/sin(x)`
   - Justification: Combine rational terms over a common denominator without applying another trigonometric identity.
   - Conditions: `sin(x) ≠ 0`
6. `(1 - cos(x)**2)/sin(x)` → `sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04


---

## ab/cd = e

### QB-11-001 — `1 = 1`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-002 — `sin(x)/tan(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-003 — `sin(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-004 — `sin(x)**2/(cos(x)*tan(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)**2/(cos(x)*tan(x))` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-005 — `cos(x)/cot(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-006 — `cos(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-007 — `tan(x)/sin(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-008 — `tan(x)/sec(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-009 — `tan(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-010 — `cot(x)/cos(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-011 — `cot(x)/csc(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-012 — `cot(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-013 — `sin(x)*cot(x)/cos(x)**2 = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)/cos(x)**2` → `1/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-014 — `sin(x)*cot(x)/(cos(x)*tan(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)/(cos(x)*tan(x))` → `cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-015 — `sin(x)*cot(x)/(cos(x)*sec(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-016 — `sin(x)*cot(x)/(cos(x)*csc(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-017 — `sin(x)*cot(x)/cos(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-018 — `sin(x)*cot(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-019 — `sec(x)/tan(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-020 — `sec(x)/csc(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F01`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-021 — `sec(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-022 — `sin(x)*sec(x)/(cos(x)*tan(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)/(cos(x)*tan(x))` → `sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-023 — `sin(x)*sec(x)/tan(x)**2 = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)/tan(x)**2` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-024 — `sin(x)*sec(x)/(tan(x)*cot(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)/(tan(x)*cot(x))` → `cos(x)*sec(x)/cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-025 — `sin(x)*sec(x)/(tan(x)*csc(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)*sec(x)/csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-026 — `sin(x)*sec(x)/tan(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)/tan(x)` → `cos(x)*sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-027 — `sin(x)*sec(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-028 — `csc(x)/cot(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-029 — `csc(x)/sec(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-030 — `csc(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `Algebra only`  
**Identity/proof IDs:** `Algebra only`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

The claim is established by exact algebraic equality; the certificate records the checked transformation.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-031 — `sin(x)*csc(x)/(cos(x)*tan(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/(cos(x)*tan(x))` → `csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-032 — `sin(x)*csc(x)/(cos(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-033 — `sin(x)*csc(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-034 — `sin(x)*csc(x)/(tan(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/(tan(x)*cot(x))` → `cos(x)*csc(x)/cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-035 — `sin(x)*csc(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/tan(x)` → `cos(x)*csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-036 — `sin(x)*csc(x)/(cot(x)*sec(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)**2*csc(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/(cos(x)*sec(x))` → `sin(x)**2*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)**2*csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-037 — `sin(x)*csc(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/cot(x)` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-038 — `sin(x)*csc(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-039 — `sin(x)*csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-040 — `1/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-041 — `1/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-042 — `1/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-043 — `1/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-044 — `sin(x)/(cos(x)*tan(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)/(cos(x)*tan(x))` → `1` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-045 — `sin(x)/(cos(x)*sec(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-046 — `sin(x)/(tan(x)*cot(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sin(x)/(tan(x)*cot(x))` → `cos(x)/cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-047 — `cos(x)**2/(sin(x)*cot(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)**2/(sin(x)*cot(x))` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-048 — `cos(x)*tan(x)/sin(x)**2 = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)/sin(x)**2` → `1/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-049 — `cos(x)*tan(x)/(sin(x)*cot(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)/(sin(x)*cot(x))` → `tan(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-050 — `cos(x)*tan(x)/(sin(x)*sec(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)/(sin(x)*sec(x))` → `1/sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-051 — `cos(x)*tan(x)/(sin(x)*csc(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)/(sin(x)*csc(x))` → `1/csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-052 — `cos(x)*tan(x)/sin(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)/sin(x)` → `1` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-053 — `cos(x)*tan(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-054 — `cos(x)*sec(x)/(sin(x)*cot(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/(sin(x)*cot(x))` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-055 — `cos(x)*sec(x)/(sin(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-056 — `cos(x)*sec(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-057 — `cos(x)*sec(x)/(tan(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/(tan(x)*cot(x))` → `cos(x)**2*sec(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/(sin(x)*cot(x))` → `cos(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-058 — `cos(x)*sec(x)/(tan(x)*csc(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)**2*sec(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/(sin(x)*csc(x))` → `cos(x)/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-059 — `cos(x)*sec(x)/tan(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/tan(x)` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-060 — `cos(x)*sec(x)/cot(x) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-061 — `cos(x)*sec(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-062 — `cos(x)*sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-063 — `cos(x)*csc(x)/(sin(x)*cot(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)/(sin(x)*cot(x))` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-064 — `cos(x)*csc(x)/(tan(x)*cot(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)/(tan(x)*cot(x))` → `cos(x)**2*csc(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2*csc(x)/(sin(x)*cot(x))` → `cos(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-065 — `cos(x)*csc(x)/cot(x)**2 = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04, F01`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)/cot(x)**2` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-066 — `cos(x)*csc(x)/(cot(x)*sec(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)*csc(x)/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-067 — `cos(x)*csc(x)/cot(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-068 — `cos(x)*csc(x) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F02`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-069 — `cos(x)/(sin(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)/(sin(x)*cot(x))` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-070 — `cos(x)/(sin(x)*csc(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-071 — `cos(x)/(tan(x)*cot(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cos(x)/(tan(x)*cot(x))` → `cos(x)**2/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)**2/(sin(x)*cot(x))` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-072 — `tan(x)**2/(sin(x)*sec(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `tan(x)**2/(sin(x)*sec(x))` → `sin(x)/(cos(x)**2*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)/(cos(x)**2*sec(x))` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-073 — `tan(x)*cot(x)/(sin(x)*sec(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/(sin(x)*sec(x))` → `cot(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cot(x)/(cos(x)*sec(x))` → `cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-074 — `tan(x)*cot(x)/(sin(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F05`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/(sin(x)*csc(x))` → `tan(x)*cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `tan(x)*cot(x)` → `1` — **F05**
   - Applied theorem: F05 — tan x · cot x = 1
   - Justification: Apply established identity F05 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F05 depends on F01
- F05 depends on F02

### QB-11-075 — `tan(x)*cot(x)/sin(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/sin(x)` → `tan(x)*cot(x)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-076 — `tan(x)*cot(x)/(cos(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F05`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/(cos(x)*sec(x))` → `tan(x)*cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `tan(x)*cot(x)` → `1` — **F05**
   - Applied theorem: F05 — tan x · cot x = 1
   - Justification: Apply established identity F05 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F05 depends on F01
- F05 depends on F02

### QB-11-077 — `tan(x)*cot(x)/(cos(x)*csc(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/(cos(x)*csc(x))` → `tan(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `tan(x)/(sin(x)*csc(x))` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-078 — `tan(x)*cot(x)/cos(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/cos(x)` → `tan(x)*cot(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-079 — `tan(x)*cot(x)/sec(x) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/sec(x)` → `sin(x)*cot(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-080 — `tan(x)*cot(x)/csc(x) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)/csc(x)` → `sin(x)*cot(x)/(cos(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-081 — `tan(x)*cot(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-082 — `tan(x)*csc(x)/(sin(x)*sec(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)/(sin(x)*sec(x))` → `csc(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `csc(x)/(cos(x)*sec(x))` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-083 — `tan(x)*csc(x)/(cos(x)*sec(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F01, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)/(cos(x)*sec(x))` → `tan(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-084 — `tan(x)*csc(x)/(cot(x)*sec(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)*tan(x)*csc(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*tan(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*tan(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*tan(x)*csc(x)` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-085 — `tan(x)*csc(x)/sec(x)**2 = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)/sec(x)**2` → `sin(x)*csc(x)/(cos(x)*sec(x)**2)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x)**2)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-086 — `tan(x)*csc(x)/sec(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)/sec(x)` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-087 — `tan(x)*csc(x) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-088 — `tan(x)/(sin(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `tan(x)/(sin(x)*sec(x))` → `1/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/(cos(x)*sec(x))` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-089 — `tan(x)/(sin(x)*csc(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `tan(x)/(sin(x)*csc(x))` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-090 — `tan(x)/(cos(x)*sec(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `tan(x)/(cos(x)*sec(x))` → `tan(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-091 — `cot(x)**2/(cos(x)*csc(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)**2/(cos(x)*csc(x))` → `cos(x)/(sin(x)**2*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)/(sin(x)**2*csc(x))` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-092 — `cot(x)*sec(x)/(sin(x)*csc(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)/(sin(x)*csc(x))` → `cot(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
3. `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-093 — `cot(x)*sec(x)/(cos(x)*csc(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)/(cos(x)*csc(x))` → `sec(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-094 — `cot(x)*sec(x)/(tan(x)*csc(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)*cot(x)*sec(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*cot(x)*sec(x)/(sin(x)*csc(x))` → `cot(x)/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `cot(x)/(sin(x)*csc(x))` → `cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-095 — `cot(x)*sec(x)/csc(x)**2 = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)/csc(x)**2` → `cos(x)*sec(x)/(sin(x)*csc(x)**2)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x)**2)` → `1/(sin(x)*csc(x)**2)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x)**2)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-096 — `cot(x)*sec(x)/csc(x) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)/csc(x)` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-097 — `cot(x)*sec(x) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-098 — `cot(x)/(sin(x)*csc(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/(sin(x)*csc(x))` → `cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-099 — `cot(x)/(cos(x)*sec(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/(cos(x)*sec(x))` → `cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-100 — `cot(x)/(cos(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F04`  
**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `cot(x)/(cos(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-101 — `sec(x)**2/(tan(x)*csc(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sec(x)**2/(tan(x)*csc(x))` → `cos(x)*sec(x)**2/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)**2/(sin(x)*csc(x))` → `1/(sin(x)*cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/(sin(x)*cos(x)*csc(x))` → `sec(x)/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
4. `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-102 — `sec(x)/(sin(x)*csc(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-103 — `sec(x)/(tan(x)*cot(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sec(x)/(tan(x)*cot(x))` → `cos(x)*sec(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*cot(x))` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-104 — `sec(x)/(tan(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F03, F04`  
**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `sec(x)/(tan(x)*csc(x))` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-105 — `csc(x)**2/(cot(x)*sec(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)**2/(cot(x)*sec(x))` → `sin(x)*csc(x)**2/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)**2/(cos(x)*sec(x))` → `sin(x)*csc(x)**2` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*csc(x)**2` → `1/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
4. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-106 — `csc(x)/(cos(x)*sec(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/(cos(x)*sec(x))` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-107 — `csc(x)/(tan(x)*cot(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `csc(x)/(tan(x)*cot(x))` → `cos(x)*csc(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)*csc(x)/(sin(x)*cot(x))` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-108 — `csc(x)/(cot(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03, F04`  
**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `csc(x)/(cot(x)*sec(x))` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
3. `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-109 — `1/(sin(x)*cot(x)) = sec(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/(sin(x)*cot(x))` → `1/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-110 — `1/(sin(x)*sec(x)) = cot(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03, F02`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/(sin(x)*sec(x))` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-111 — `1/(sin(x)*csc(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04`  
**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-112 — `1/(cos(x)*tan(x)) = csc(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04`  
**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/(cos(x)*tan(x))` → `1/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-113 — `1/(cos(x)*sec(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F03`  
**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

**Proof**

1. `1/(cos(x)*sec(x))` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-114 — `1/(cos(x)*csc(x)) = tan(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F04, F01`  
**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-115 — `1/(tan(x)*cot(x)) = 1`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F02`  
**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/(tan(x)*cot(x))` → `cos(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/(sin(x)*cot(x))` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-116 — `1/(tan(x)*csc(x)) = cos(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F01, F04`  
**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

**Proof**

1. `1/(tan(x)*csc(x))` → `cos(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Justification: Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`
2. `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Justification: Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### QB-11-117 — `1/(cot(x)*sec(x)) = sin(x)`

**Status:** `PROVED`  
**Selected route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F02, F03`  
**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

**Proof**

1. `1/(cot(x)*sec(x))` → `sin(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Justification: Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`
2. `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Justification: Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


## 3. Supplementary solutions demonstrating theorem reuse

### SUP-001 — Orthogonal linear-combination identity

**Claim:** `(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2 = p**2+q**2`

**Status:** `PROVED`  
**Route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F08`  
**Original common domain:** All real values of the variables in the stated claim.

**Proof**

1. `(p*sin(x) - q*cos(x))**2 + (p*cos(x) + q*sin(x))**2` → `p**2*sin(x)**2 + p**2*cos(x)**2 + q**2*sin(x)**2 + q**2*cos(x)**2`
   - Justification: Apply the distributive law to expand squared linear combinations; trigonometric functions are treated as algebraic factors.
2. `p**2*sin(x)**2 + p**2*cos(x)**2 + q**2*sin(x)**2 + q**2*cos(x)**2` → `(p**2 + q**2)*(sin(x)**2 + cos(x)**2)`
   - Justification: Collect common parameter factors to expose the sum sin(x)**2 + cos(x)**2 for an established identity application.
3. `(p**2 + q**2)*(sin(x)**2 + cos(x)**2)` → `p**2 + q**2` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Justification: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

---

### SUP-002 — Using F09 in a different identity

**Claim:** `(1+tan(x)**2)*cos(x)**2 = sec(x)**2*cos(x)**2`

**Status:** `PROVED`  
**Route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F09`  
**Original common domain:** `cos(x) ≠ 0`

**Proof**

1. `(tan(x)**2 + 1)*cos(x)**2` → `cos(x)**2*sec(x)**2` — **F09**
   - Applied theorem: F09 — 1 + tan²x = sec²x
   - Justification: Apply established identity F09 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `cos(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F09 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F09 depends on F01
- F09 depends on F03

---

### SUP-003 — Using F10 in a different identity

**Claim:** `(1+cot(x)**2)*sin(x)**2 = csc(x)**2*sin(x)**2`

**Status:** `PROVED`  
**Route:** `LHS using identity catalogue`  
**Identity/proof IDs:** `F10`  
**Original common domain:** `sin(x) ≠ 0`

**Proof**

1. `(cot(x)**2 + 1)*sin(x)**2` → `sin(x)**2*csc(x)**2` — **F10**
   - Applied theorem: F10 — 1 + cot²x = csc²x
   - Justification: Apply established identity F10 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Variable substitution: `x → x`
   - Conditions: `sin(x) ≠ 0`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance**
- F10 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F10 depends on F02
- F10 depends on F04

## 4. Rejected near-miss — not a proved question

**Claim as originally typed:** `(p*cos(x)+q*sin(x))**2+(p*sin(x)-p*cos(x))**2 = p**2+q**2`

**Status:** `DISPROVED`

The second bracket contains `p*cos(x)` instead of `q*cos(x)`. A single exact counterexample is sufficient:

Take `p = 1`, `q = 0`, `x = 0`.

- LHS = `(1*1 + 0*0)**2 + (1*0 - 1*1)**2 = 1 + 1 = 2`.
- RHS = `1**2 + 0**2 = 1`.
- Therefore the statement is false as written and must not be marked `PROVED`.

The corrected identity in `SUP-001` is proved using F08.
