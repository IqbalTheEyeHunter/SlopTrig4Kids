# Trigonometric Proof Engine — Question Bank

**Filename:** `question_bank.md`  
**Engine target:** v0.5.1  
**Purpose:** training handbook of generated trigonometric identity questions with checked proof routes.

## 1. Search scope

To make “exhaustive” finite and reproducible, each metavariable `a`, `b`, `c`, `d`, and `e` is assigned exactly one atom from this alphabet, all at the same real angle `x`:

`sin(x)`, `cos(x)`, `tan(x)`, `cot(x)`, `sec(x)`, `csc(x)`, `1`.

Every ordered assignment was enumerated for each requested operation template. Exact duplicate parsed LHS/RHS pairs within a template were stored once. Powers and products can appear as a result of the requested operations, but are not additional input atoms.

This is exhaustive over the stated seven-atom alphabet and the eleven templates below. It is not exhaustive over arbitrary compound trigonometric expressions, multiple independent angles, or compound arguments such as `sin(2*x)`. Those would require a separately bounded grammar.

## 2. Proof-admission rules

- An entry is included only if the v0.5.1 proof route returned `PROVED`.
- The exact rational reduction using `S=sin(x)`, `C=cos(x)`, and `S**2+C**2=1` was used only to discover candidate identities. It did not assign proof status.
- F08-shaped claims require the replayed geometric route `G01 → G03 → G04`; F08 is never used to prove itself.
- Downstream identity rules may use F08 only after the geometric foundation has been replayed.
- The engine-reported original common-domain conditions are retained for every entry.
- `INCONCLUSIVE`, `DISPROVED`, and certificate-rejected claims are not listed.
- An omitted candidate is not thereby declared false; it may be mathematically true but not derivable by the enabled proof search.

**Execution provenance:** the v0.5.1 proof core used for this generation run was reconstructed from the available v0.4.1 source and updated with the v0.5.1 replayable `G01 → G03 → G04` certificate route and F08 dependency gate. The Windows GUI/executable was not run for this data-generation task.

## 3. Search summary

| Operation template | Raw assignments | Unique candidate claims checked | PROVED entries in this template |
|---|---:|---:|---:|
| `a + b = c` | 343 | 0 | 0 |
| `a - b = c` | 343 | 0 | 0 |
| `ab = c` | 343 | 16 | 16 |
| `a/b = c` | 343 | 25 | 21 |
| `ab + c = d` | 2,401 | 2 | 2 |
| `ab - c = d` | 2,401 | 2 | 2 |
| `abc = d` | 2,401 | 36 | 36 |
| `ab/c = d` | 2,401 | 52 | 48 |
| `ab + cd = e` | 16,807 | 5 | 5 |
| `ab - cd = e` | 16,807 | 10 | 4 |
| `ab/cd = e` | 16,807 | 121 | 117 |

**Raw assignments searched:** 61,397.  
**Unique candidate claims checked by the engine:** 156.  
**Unique claims returned as PROVED:** 146.  
**Template entries recorded (including repeats across templates):** 251.

A repeated identity may appear under more than one template because the variable assignment and original question structure differ. Each occurrence keeps its own assignment and domain ledger.

## 4. Proved question bank

Only engine-proved entries are included below.


---

## a + b = c

No assignments in this finite search space were returned as `PROVED` by v0.5.1.

---

## a - b = c

No assignments in this finite search space were returned as `PROVED` by v0.5.1.

---

## ab = c

### 1. `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 2. `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01`

**Proof**

**Step 1.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 3. `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 4. `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 5. `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 6. `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 7. `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F02`

**Proof**

**Step 1.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 8. `cos(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = cos(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 9. `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 10. `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04, F03`

**Proof**

**Step 1.** `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 11. `tan(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 12. `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 13. `cot(x) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 14. `sec(x) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 15. `csc(x) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 16. `1 = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = 1`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## a/b = c

### 1. `1 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = 1`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 2. `sin(x)/tan(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 3. `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 4. `cos(x)/cot(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cot(x)`
- `c = sin(x)`
**Original common-domain conditions**
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 5. `cos(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = cos(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 6. `tan(x)/sin(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = sin(x)`
- `c = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 7. `tan(x)/sec(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = sec(x)`
- `c = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 8. `tan(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 9. `cot(x)/cos(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = cos(x)`
- `c = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 10. `cot(x)/csc(x) = cos(x)`

**Variable assignment**
- `a = cot(x)`
- `b = csc(x)`
- `c = cos(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 11. `cot(x) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 12. `sec(x)/tan(x) = csc(x)`

**Variable assignment**
- `a = sec(x)`
- `b = tan(x)`
- `c = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 13. `sec(x)/csc(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04, F01`

**Proof**

**Step 1.** `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 14. `sec(x) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 15. `csc(x)/cot(x) = sec(x)`

**Variable assignment**
- `a = csc(x)`
- `b = cot(x)`
- `c = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F03`

**Proof**

**Step 1.** `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 16. `csc(x)/sec(x) = cot(x)`

**Variable assignment**
- `a = csc(x)`
- `b = sec(x)`
- `c = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04, F02`

**Proof**

**Step 1.** `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 17. `csc(x) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 18. `1/tan(x) = cot(x)`

**Variable assignment**
- `a = 1`
- `b = tan(x)`
- `c = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 19. `1/cot(x) = tan(x)`

**Variable assignment**
- `a = 1`
- `b = cot(x)`
- `c = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F01`

**Proof**

**Step 1.** `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 20. `1/sec(x) = cos(x)`

**Variable assignment**
- `a = 1`
- `b = sec(x)`
- `c = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 21. `1/csc(x) = sin(x)`

**Variable assignment**
- `a = 1`
- `b = csc(x)`
- `c = sin(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab + c = d

### 1. `sin(x)*tan(x) + cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cos(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F08, F03`

**Proof**

**Step 1.** `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(sin(x)**2 + cos(x)**2)/cos(x)` → `1/cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### 2. `sin(x) + cos(x)*cot(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F08, F04`

**Proof**

**Step 1.** `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(sin(x)**2 + cos(x)**2)/sin(x)` → `1/sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04


---

## ab - c = d

### 1. `-tan(x) + csc(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04, F09, F02`

**Proof**

**Step 1.** `-tan(x) + csc(x)*sec(x)` → `-sin(x)/cos(x) + csc(x)*sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `-sin(x)/cos(x) + csc(x)*sec(x)` → `(-sin(x) + cos(x)*csc(x)*sec(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(-sin(x) + cos(x)*csc(x)*sec(x))/cos(x)` → `(-sin(x) + cos(x)*csc(x)*sec(x))*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `(-sin(x) + cos(x)*csc(x)*sec(x))*sec(x)` → `-sin(x)*sec(x) + cos(x)*csc(x)*sec(x)**2`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 5.** `-sin(x)*sec(x) + cos(x)*csc(x)*sec(x)**2` → `-sin(x)*sec(x) + cos(x)*sec(x)**2/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 6.** `-sin(x)*sec(x) + cos(x)*sec(x)**2/sin(x)` → `(-sin(x)**2 + cos(x)*sec(x))*sec(x)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 7.** `(-sin(x)**2 + cos(x)*sec(x))*sec(x)/sin(x)` → `(-sin(x)**2*sec(x) + cos(x)*sec(x)**2)/sin(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 8.** `(-sin(x)**2*sec(x) + cos(x)*sec(x)**2)/sin(x)` → `((tan(x)**2 + 1)*cos(x) - sin(x)**2*sec(x))/sin(x)` — **F09**
   - Applied theorem: F09 — 1 + tan²x = sec²x
   - Apply established identity F09 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 9.** `((tan(x)**2 + 1)*cos(x) - sin(x)**2*sec(x))/sin(x)` → `(-sin(x)**2*sec(x) + cos(x)*tan(x)**2 + cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 10.** `(-sin(x)**2*sec(x) + cos(x)*tan(x)**2 + cos(x))/sin(x)` → `(-sin(x)**2*sec(x) + sin(x)**2/cos(x) + cos(x))/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 11.** `(-sin(x)**2*sec(x) + sin(x)**2/cos(x) + cos(x))/sin(x)` → `((-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 12.** `((-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/cos(x))/sin(x)` → `(-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/(sin(x)*cos(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 13.** `(-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 14.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F09 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F09 depends on F01
- F09 depends on F03

### 2. `-cot(x) + csc(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04, F10, F01`

**Proof**

**Step 1.** `-cot(x) + csc(x)*sec(x)` → `csc(x)*sec(x) - cos(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `csc(x)*sec(x) - cos(x)/sin(x)` → `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)` → `(sin(x)*csc(x)*sec(x) - cos(x))/sin(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 4.** `(sin(x)*csc(x)*sec(x) - cos(x))/sin(x)` → `(sin(x)*csc(x)/cos(x) - cos(x))/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `(sin(x)*csc(x)/cos(x) - cos(x))/sin(x)` → `(-(-sin(x)*csc(x) + cos(x)**2)/cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 6.** `(-(-sin(x)*csc(x) + cos(x)**2)/cos(x))/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 7.** `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))` → `(sin(x)*csc(x) - cos(x)**2)*csc(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 8.** `(sin(x)*csc(x) - cos(x)**2)*csc(x)/cos(x)` → `(-(-sin(x)*csc(x) + cos(x)**2)*csc(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 9.** `(-(-sin(x)*csc(x) + cos(x)**2)*csc(x))/cos(x)` → `(sin(x)*csc(x)**2 - cos(x)**2*csc(x))/cos(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 10.** `(sin(x)*csc(x)**2 - cos(x)**2*csc(x))/cos(x)` → `((cot(x)**2 + 1)*sin(x) - cos(x)**2*csc(x))/cos(x)` — **F10**
   - Applied theorem: F10 — 1 + cot²x = csc²x
   - Apply established identity F10 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 11.** `((cot(x)**2 + 1)*sin(x) - cos(x)**2*csc(x))/cos(x)` → `(sin(x)*cot(x)**2 + sin(x) - cos(x)**2*csc(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 12.** `(sin(x)*cot(x)**2 + sin(x) - cos(x)**2*csc(x))/cos(x)` → `(sin(x) - cos(x)**2*csc(x) + cos(x)**2/sin(x))/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 13.** `(sin(x) - cos(x)**2*csc(x) + cos(x)**2/sin(x))/cos(x)` → `(-(-sin(x)**2 + sin(x)*cos(x)**2*csc(x) - cos(x)**2)/sin(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 14.** `(-(-sin(x)**2 + sin(x)*cos(x)**2*csc(x) - cos(x)**2)/sin(x))/cos(x)` → `(sin(x)**2 - sin(x)*cos(x)**2*csc(x) + cos(x)**2)/(sin(x)*cos(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 15.** `(sin(x)**2 - sin(x)*cos(x)**2*csc(x) + cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 16.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F10 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F10 depends on F02
- F10 depends on F04


---

## abc = d

### 1. `sin(x)**2*csc(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = csc(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)**2*csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 2. `sin(x)*cos(x)*sec(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sec(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `sin(x)*cos(x)*sec(x)` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 3. `sin(x)*cos(x)*csc(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = csc(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 4. `sin(x)*tan(x)*cot(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cot(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `sin(x)*tan(x)*cot(x)` → `sin(x)**2*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2*cot(x)/cos(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 5. `sin(x)*tan(x)*csc(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = csc(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*tan(x)*csc(x)` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 6. `sin(x)*cot(x)*sec(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03`

**Proof**

**Step 1.** `sin(x)*cot(x)*sec(x)` → `cos(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 7. `sin(x)*cot(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*cot(x)*csc(x)` → `cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 8. `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = 1`
- `d = cos(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 9. `sin(x)*csc(x)*sec(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 10. `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = 1`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01`

**Proof**

**Step 1.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 11. `sin(x)*csc(x)**2 = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = csc(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*csc(x)**2` → `1/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 12. `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 13. `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = 1`
- `d = sin(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 14. `cos(x)**2*sec(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cos(x)`
- `c = sec(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)**2*sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 15. `cos(x)*tan(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = cot(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `cos(x)*tan(x)*cot(x)` → `sin(x)*cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 16. `cos(x)*tan(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sec(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*tan(x)*sec(x)` → `tan(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 17. `cos(x)*tan(x)*csc(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = csc(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04`

**Proof**

**Step 1.** `cos(x)*tan(x)*csc(x)` → `sin(x)*csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 18. `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = 1`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 19. `cos(x)*cot(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*cot(x)*sec(x)` → `cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 20. `cos(x)*sec(x)**2 = sec(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sec(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*sec(x)**2` → `1/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 21. `cos(x)*csc(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 22. `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 23. `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = 1`
- `d = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F02`

**Proof**

**Step 1.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 24. `cos(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = 1`
- `d = cos(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 25. `tan(x)**2*cot(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = tan(x)`
- `c = cot(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)**2*cot(x)` → `sin(x)**2*cot(x)/cos(x)**2` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2*cot(x)/cos(x)**2` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 26. `tan(x)*cot(x)**2 = cot(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cot(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)**2` → `sin(x)*cot(x)**2/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)**2/cos(x)` → `cos(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 27. `tan(x)*cot(x)*sec(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 28. `tan(x)*cot(x)*csc(x) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 29. `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 30. `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = 1`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04, F03`

**Proof**

**Step 1.** `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 31. `tan(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = 1`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 32. `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = 1`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 33. `cot(x) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = 1`
- `d = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 34. `sec(x) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = 1`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 35. `csc(x) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = 1`
- `d = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 36. `1 = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = 1`
- `d = 1`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab/c = d

### 1. `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = sin(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 2. `cos(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = cos(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 3. `tan(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 4. `cot(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 5. `sin(x)*cot(x)/cos(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 6. `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = 1`
- `d = cos(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 7. `sec(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 8. `sin(x)*sec(x)/tan(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `sin(x)*sec(x)/tan(x)` → `cos(x)*sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 9. `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = 1`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01`

**Proof**

**Step 1.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 10. `csc(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 11. `sin(x)*csc(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 12. `sin(x)*csc(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04, F02`

**Proof**

**Step 1.** `sin(x)*csc(x)/tan(x)` → `cos(x)*csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 13. `sin(x)*csc(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F01`

**Proof**

**Step 1.** `sin(x)*csc(x)/cot(x)` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 14. `sin(x)*csc(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 15. `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 16. `1 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = 1`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 17. `sin(x)/tan(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = tan(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 18. `cos(x)*tan(x)/sin(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `cos(x)*tan(x)/sin(x)` → `1` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 19. `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = 1`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 20. `cos(x)*sec(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F03`

**Proof**

**Step 1.** `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 21. `cos(x)*sec(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F02`

**Proof**

**Step 1.** `cos(x)*sec(x)/tan(x)` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 22. `cos(x)*sec(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = cot(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F01`

**Proof**

**Step 1.** `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 23. `cos(x)*sec(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 24. `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 25. `cos(x)*csc(x)/cot(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
**Original common-domain conditions**
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 26. `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = 1`
- `d = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F02`

**Proof**

**Step 1.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 27. `cos(x)/cot(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = cot(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 28. `tan(x)*cot(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)/sin(x)` → `tan(x)*cot(x)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 29. `tan(x)*cot(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)/cos(x)` → `tan(x)*cot(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 30. `tan(x)*cot(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F03`

**Proof**

**Step 1.** `tan(x)*cot(x)/sec(x)` → `sin(x)*cot(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 31. `tan(x)*cot(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F04`

**Proof**

**Step 1.** `tan(x)*cot(x)/csc(x)` → `sin(x)*cot(x)/(cos(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 32. `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 33. `tan(x)*csc(x)/sec(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `tan(x)*csc(x)/sec(x)` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 34. `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = 1`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04, F03`

**Proof**

**Step 1.** `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 35. `tan(x)/sin(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 36. `tan(x)/sec(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sec(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 37. `cot(x)*sec(x)/csc(x) = 1`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)/csc(x)` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 38. `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = 1`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 39. `cot(x)/cos(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cos(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 40. `cot(x)/csc(x) = cos(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = csc(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 41. `sec(x)/tan(x) = csc(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = tan(x)`
- `d = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 42. `sec(x)/csc(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = csc(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04, F01`

**Proof**

**Step 1.** `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 43. `csc(x)/cot(x) = sec(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cot(x)`
- `d = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F03`

**Proof**

**Step 1.** `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 44. `csc(x)/sec(x) = cot(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = sec(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04, F02`

**Proof**

**Step 1.** `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 45. `1/tan(x) = cot(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 46. `1/cot(x) = tan(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cot(x)`
- `d = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F01`

**Proof**

**Step 1.** `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 47. `1/sec(x) = cos(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sec(x)`
- `d = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 48. `1/csc(x) = sin(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = csc(x)`
- `d = sin(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.


---

## ab + cd = e

### 1. `sin(x)**2 + cos(x)**2 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = cos(x)`
- `d = cos(x)`
- `e = 1`
**Original common domain:** all real `x`.

**Selected engine route:** `GEO: G01 → G03 → G04`
**Identity/proof IDs:** `G01, G03, G04`

**Proof**

**Independent geometric proof — G01 → G03 → G04**

1. **G01 — Pythagorean theorem by dissection.** Four congruent right triangles tile a square of side `p+q`; the central square has side `r`. Exact area additivity gives `(p+q)**2 = 4*(p*q/2) + r**2`, hence `p**2 + q**2 = r**2`.
2. **G03 — Cartesian squared distance.** For a point `P=(u,v)`, its perpendicular projection lengths are `abs(u)` and `abs(v)`. The Pythagorean theorem gives `OP**2 = u**2 + v**2`, including negative coordinates and axis cases.
3. **G04 — Unit-circle substitution.** The unit-circle point `P=(cos(x), sin(x))` has `OP=1`. Therefore `cos(x)**2 + sin(x)**2 = 1` for every real `x`.

No F08/F09/F10 catalogue identity is used as a premise. The certificate is checked relative to `AX.REAL`, `AX.EUCLID`, `AX.AREA`, and `D.UNIT`.

**Certificate:** `trigonometric-geometric-proof-certificate-v1` — `PROVED`.

### 2. `sin(x)*tan(x) + sin(x)*cot(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F08, F03`

**Proof**

**Step 1.** `sin(x)*tan(x) + sin(x)*cot(x)` → `sin(x)**2/cos(x) + sin(x)*cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2/cos(x) + sin(x)*cot(x)` → `(sin(x) + cos(x)*cot(x))*sin(x)/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(sin(x) + cos(x)*cot(x))*sin(x)/cos(x)` → `(sin(x)**2 + sin(x)*cos(x)*cot(x))/cos(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 4.** `(sin(x)**2 + sin(x)*cos(x)*cot(x))/cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `(sin(x)**2 + cos(x)**2)/cos(x)` → `1/cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 6.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### 3. `sin(x)*tan(x) + cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cos(x)`
- `d = 1`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F08, F03`

**Proof**

**Step 1.** `sin(x)*tan(x) + cos(x)` → `sin(x)**2/cos(x) + cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2/cos(x) + cos(x)` → `(sin(x)**2 + cos(x)**2)/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(sin(x)**2 + cos(x)**2)/cos(x)` → `1/cos(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### 4. `sin(x) + cos(x)*cot(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = cos(x)`
- `d = cot(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F08, F04`

**Proof**

**Step 1.** `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(sin(x)**2 + cos(x)**2)/sin(x)` → `1/sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04

### 5. `cos(x)*tan(x) + cos(x)*cot(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = cos(x)`
- `d = cot(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F08, F04`

**Proof**

**Step 1.** `cos(x)*tan(x) + cos(x)*cot(x)` → `sin(x) + cos(x)*cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x) + cos(x)*cot(x)` → `sin(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x) + cos(x)**2/sin(x)` → `(sin(x)**2 + cos(x)**2)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 4.** `(sin(x)**2 + cos(x)**2)/sin(x)` → `1/sin(x)` — **F08**
   - Applied theorem: F08 — sin²x + cos²x = 1
   - Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04


---

## ab - cd = e

### 1. `-tan(x) + csc(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = 1`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04, F09, F02`

**Proof**

**Step 1.** `-tan(x) + csc(x)*sec(x)` → `-sin(x)/cos(x) + csc(x)*sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `-sin(x)/cos(x) + csc(x)*sec(x)` → `(-sin(x) + cos(x)*csc(x)*sec(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(-sin(x) + cos(x)*csc(x)*sec(x))/cos(x)` → `(-sin(x) + cos(x)*csc(x)*sec(x))*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `(-sin(x) + cos(x)*csc(x)*sec(x))*sec(x)` → `-sin(x)*sec(x) + cos(x)*csc(x)*sec(x)**2`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 5.** `-sin(x)*sec(x) + cos(x)*csc(x)*sec(x)**2` → `-sin(x)*sec(x) + cos(x)*sec(x)**2/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 6.** `-sin(x)*sec(x) + cos(x)*sec(x)**2/sin(x)` → `(-sin(x)**2 + cos(x)*sec(x))*sec(x)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 7.** `(-sin(x)**2 + cos(x)*sec(x))*sec(x)/sin(x)` → `(-sin(x)**2*sec(x) + cos(x)*sec(x)**2)/sin(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 8.** `(-sin(x)**2*sec(x) + cos(x)*sec(x)**2)/sin(x)` → `((tan(x)**2 + 1)*cos(x) - sin(x)**2*sec(x))/sin(x)` — **F09**
   - Applied theorem: F09 — 1 + tan²x = sec²x
   - Apply established identity F09 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 9.** `((tan(x)**2 + 1)*cos(x) - sin(x)**2*sec(x))/sin(x)` → `(-sin(x)**2*sec(x) + cos(x)*tan(x)**2 + cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 10.** `(-sin(x)**2*sec(x) + cos(x)*tan(x)**2 + cos(x))/sin(x)` → `(-sin(x)**2*sec(x) + sin(x)**2/cos(x) + cos(x))/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 11.** `(-sin(x)**2*sec(x) + sin(x)**2/cos(x) + cos(x))/sin(x)` → `((-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 12.** `((-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/cos(x))/sin(x)` → `(-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/(sin(x)*cos(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 13.** `(-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/(sin(x)*cos(x))` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 14.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F09 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F09 depends on F01
- F09 depends on F03

### 2. `-cot(x) + csc(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04, F10, F01`

**Proof**

**Step 1.** `-cot(x) + csc(x)*sec(x)` → `csc(x)*sec(x) - cos(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `csc(x)*sec(x) - cos(x)/sin(x)` → `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `-(-sin(x)*csc(x)*sec(x) + cos(x))/sin(x)` → `(sin(x)*csc(x)*sec(x) - cos(x))/sin(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 4.** `(sin(x)*csc(x)*sec(x) - cos(x))/sin(x)` → `(sin(x)*csc(x)/cos(x) - cos(x))/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `(sin(x)*csc(x)/cos(x) - cos(x))/sin(x)` → `(-(-sin(x)*csc(x) + cos(x)**2)/cos(x))/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 6.** `(-(-sin(x)*csc(x) + cos(x)**2)/cos(x))/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 7.** `(sin(x)*csc(x) - cos(x)**2)/(sin(x)*cos(x))` → `(sin(x)*csc(x) - cos(x)**2)*csc(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 8.** `(sin(x)*csc(x) - cos(x)**2)*csc(x)/cos(x)` → `(-(-sin(x)*csc(x) + cos(x)**2)*csc(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 9.** `(-(-sin(x)*csc(x) + cos(x)**2)*csc(x))/cos(x)` → `(sin(x)*csc(x)**2 - cos(x)**2*csc(x))/cos(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 10.** `(sin(x)*csc(x)**2 - cos(x)**2*csc(x))/cos(x)` → `((cot(x)**2 + 1)*sin(x) - cos(x)**2*csc(x))/cos(x)` — **F10**
   - Applied theorem: F10 — 1 + cot²x = csc²x
   - Apply established identity F10 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 11.** `((cot(x)**2 + 1)*sin(x) - cos(x)**2*csc(x))/cos(x)` → `(sin(x)*cot(x)**2 + sin(x) - cos(x)**2*csc(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 12.** `(sin(x)*cot(x)**2 + sin(x) - cos(x)**2*csc(x))/cos(x)` → `(sin(x) - cos(x)**2*csc(x) + cos(x)**2/sin(x))/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 13.** `(sin(x) - cos(x)**2*csc(x) + cos(x)**2/sin(x))/cos(x)` → `(-(-sin(x)**2 + sin(x)*cos(x)**2*csc(x) - cos(x)**2)/sin(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 14.** `(-(-sin(x)**2 + sin(x)*cos(x)**2*csc(x) - cos(x)**2)/sin(x))/cos(x)` → `(sin(x)**2 - sin(x)*cos(x)**2*csc(x) + cos(x)**2)/(sin(x)*cos(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 15.** `(sin(x)**2 - sin(x)*cos(x)**2*csc(x) + cos(x)**2)/(sin(x)*cos(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 16.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F10 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F10 depends on F02
- F10 depends on F04

### 3. `-sin(x)*tan(x) + sec(x) = cos(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sin(x)`
- `d = tan(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F09`

**Proof**

**Step 1.** `-sin(x)*tan(x) + sec(x)` → `-sin(x)**2/cos(x) + sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `-sin(x)**2/cos(x) + sec(x)` → `(-sin(x)**2 + cos(x)*sec(x))/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(-sin(x)**2 + cos(x)*sec(x))/cos(x)` → `(-sin(x)**2 + cos(x)*sec(x))*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `(-sin(x)**2 + cos(x)*sec(x))*sec(x)` → `-sin(x)**2*sec(x) + cos(x)*sec(x)**2`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 5.** `-sin(x)**2*sec(x) + cos(x)*sec(x)**2` → `(tan(x)**2 + 1)*cos(x) - sin(x)**2*sec(x)` — **F09**
   - Applied theorem: F09 — 1 + tan²x = sec²x
   - Apply established identity F09 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 6.** `(tan(x)**2 + 1)*cos(x) - sin(x)**2*sec(x)` → `-sin(x)**2*sec(x) + cos(x)*tan(x)**2 + cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 7.** `-sin(x)**2*sec(x) + cos(x)*tan(x)**2 + cos(x)` → `-sin(x)**2*sec(x) + sin(x)**2/cos(x) + cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 8.** `-sin(x)**2*sec(x) + sin(x)**2/cos(x) + cos(x)` → `(-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/cos(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 9.** `(-sin(x)**2*cos(x)*sec(x) + sin(x)**2 + cos(x)**2)/cos(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F09 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F09 depends on F01
- F09 depends on F03

### 4. `-cos(x)*cot(x) + csc(x) = sin(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cos(x)`
- `d = cot(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F10`

**Proof**

**Step 1.** `-cos(x)*cot(x) + csc(x)` → `csc(x) - cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `csc(x) - cos(x)**2/sin(x)` → `-(-sin(x)*csc(x) + cos(x)**2)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `-(-sin(x)*csc(x) + cos(x)**2)/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)/sin(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 4.** `(sin(x)*csc(x) - cos(x)**2)/sin(x)` → `(sin(x)*csc(x) - cos(x)**2)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `(sin(x)*csc(x) - cos(x)**2)*csc(x)` → `-(-sin(x)*csc(x) + cos(x)**2)*csc(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 6.** `-(-sin(x)*csc(x) + cos(x)**2)*csc(x)` → `sin(x)*csc(x)**2 - cos(x)**2*csc(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 7.** `sin(x)*csc(x)**2 - cos(x)**2*csc(x)` → `(cot(x)**2 + 1)*sin(x) - cos(x)**2*csc(x)` — **F10**
   - Applied theorem: F10 — 1 + cot²x = csc²x
   - Apply established identity F10 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 8.** `(cot(x)**2 + 1)*sin(x) - cos(x)**2*csc(x)` → `sin(x)*cot(x)**2 + sin(x) - cos(x)**2*csc(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 9.** `sin(x)*cot(x)**2 + sin(x) - cos(x)**2*csc(x)` → `sin(x) - cos(x)**2*csc(x) + cos(x)**2/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 10.** `sin(x) - cos(x)**2*csc(x) + cos(x)**2/sin(x)` → `-(-sin(x)**2 + sin(x)*cos(x)**2*csc(x) - cos(x)**2)/sin(x)`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 11.** `-(-sin(x)**2 + sin(x)*cos(x)**2*csc(x) - cos(x)**2)/sin(x)` → `(sin(x)**2 - sin(x)*cos(x)**2*csc(x) + cos(x)**2)/sin(x)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 12.** `(sin(x)**2 - sin(x)*cos(x)**2*csc(x) + cos(x)**2)/sin(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F10 depends on F08
- F08 depends on GEO.F08
- GEO.F08 is admitted only after replaying G01 -> G03 -> G04
- F10 depends on F02
- F10 depends on F04


---

## ab/cd = e

### 1. `1 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = sin(x)`
- `e = 1`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 2. `sin(x)/tan(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = tan(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)/tan(x)` → `cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 3. `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = 1`
- `e = sin(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 4. `sin(x)**2/(cos(x)*tan(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)**2/(cos(x)*tan(x))` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 5. `cos(x)/cot(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 6. `cos(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = 1`
- `e = cos(x)`
**Original common domain:** all real `x`.

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 7. `tan(x)/sin(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sin(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/sin(x)` → `1/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 8. `tan(x)/sec(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/sec(x)` → `sin(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 9. `tan(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = 1`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 10. `cot(x)/cos(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = cos(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/cos(x)` → `1/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 11. `cot(x)/csc(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/csc(x)` → `cos(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 12. `cot(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = 1`
- `e = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 13. `sin(x)*cot(x)/cos(x)**2 = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = cos(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03`

**Proof**

**Step 1.** `sin(x)*cot(x)/cos(x)**2` → `1/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 14. `sin(x)*cot(x)/(cos(x)*tan(x)) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)*cot(x)/(cos(x)*tan(x))` → `cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 15. `sin(x)*cot(x)/(cos(x)*sec(x)) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03`

**Proof**

**Step 1.** `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 16. `sin(x)*cot(x)/(cos(x)*csc(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `1/tan(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 17. `sin(x)*cot(x)/cos(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 18. `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`
- `e = cos(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `sin(x)*cot(x)` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 19. `sec(x)/tan(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = tan(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `sec(x)/tan(x)` → `cos(x)*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 20. `sec(x)/csc(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04, F01`

**Proof**

**Step 1.** `sec(x)/csc(x)` → `1/(cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 21. `sec(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = 1`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 22. `sin(x)*sec(x)/(cos(x)*tan(x)) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)*sec(x)/(cos(x)*tan(x))` → `sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 23. `sin(x)*sec(x)/tan(x)**2 = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = tan(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F02`

**Proof**

**Step 1.** `sin(x)*sec(x)/tan(x)**2` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 24. `sin(x)*sec(x)/(tan(x)*cot(x)) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F03`

**Proof**

**Step 1.** `sin(x)*sec(x)/(tan(x)*cot(x))` → `cos(x)*sec(x)/cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 25. `sin(x)*sec(x)/(tan(x)*csc(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `sin(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)*sec(x)/csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 26. `sin(x)*sec(x)/tan(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `sin(x)*sec(x)/tan(x)` → `cos(x)*sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 27. `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01`

**Proof**

**Step 1.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 28. `csc(x)/cot(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F03`

**Proof**

**Step 1.** `csc(x)/cot(x)` → `sin(x)*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 29. `csc(x)/sec(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04, F02`

**Proof**

**Step 1.** `csc(x)/sec(x)` → `cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 30. `csc(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = 1`
- `e = csc(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `Algebra only`

**Proof**

The engine verified the equality by exact algebraic normalization, treating the six trigonometric functions as formal atoms.

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 31. `sin(x)*csc(x)/(cos(x)*tan(x)) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)*csc(x)/(cos(x)*tan(x))` → `csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 32. `sin(x)*csc(x)/(cos(x)*sec(x)) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 33. `sin(x)*csc(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = 1`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 34. `sin(x)*csc(x)/(tan(x)*cot(x)) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/(tan(x)*cot(x))` → `cos(x)*csc(x)/cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 35. `sin(x)*csc(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = 1`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04, F02`

**Proof**

**Step 1.** `sin(x)*csc(x)/tan(x)` → `cos(x)*csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 36. `sin(x)*csc(x)/(cot(x)*sec(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `1/sin(x) ≠ 0`
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)**2*csc(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2*csc(x)/(cos(x)*sec(x))` → `sin(x)**2*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)**2*csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 37. `sin(x)*csc(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F01`

**Proof**

**Step 1.** `sin(x)*csc(x)/cot(x)` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 38. `sin(x)*csc(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = 1`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 39. `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 40. `1/tan(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = tan(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `1/tan(x)` → `cos(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 41. `1/cot(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = cot(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F01`

**Proof**

**Step 1.** `1/cot(x)` → `sin(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 42. `1/sec(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 43. `1/csc(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 44. `sin(x)/(cos(x)*tan(x)) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = cos(x)`
- `d = tan(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `sin(x)/(cos(x)*tan(x))` → `1` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 45. `sin(x)/(cos(x)*sec(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 46. `sin(x)/(tan(x)*cot(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `sin(x)/(tan(x)*cot(x))` → `cos(x)/cot(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/cot(x)` → `sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 47. `cos(x)**2/(sin(x)*cot(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)**2/(sin(x)*cot(x))` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 48. `cos(x)*tan(x)/sin(x)**2 = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sin(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04`

**Proof**

**Step 1.** `cos(x)*tan(x)/sin(x)**2` → `1/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 49. `cos(x)*tan(x)/(sin(x)*cot(x)) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)*tan(x)/(sin(x)*cot(x))` → `tan(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 50. `cos(x)*tan(x)/(sin(x)*sec(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `cos(x)*tan(x)/(sin(x)*sec(x))` → `1/sec(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 51. `cos(x)*tan(x)/(sin(x)*csc(x)) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04`

**Proof**

**Step 1.** `cos(x)*tan(x)/(sin(x)*csc(x))` → `1/csc(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 52. `cos(x)*tan(x)/sin(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `cos(x)*tan(x)/sin(x)` → `1` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 53. `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = 1`
- `d = 1`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01`

**Proof**

**Step 1.** `cos(x)*tan(x)` → `sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 54. `cos(x)*sec(x)/(sin(x)*cot(x)) = sec(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)*sec(x)/(sin(x)*cot(x))` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 55. `cos(x)*sec(x)/(sin(x)*csc(x)) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 56. `cos(x)*sec(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = 1`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F03`

**Proof**

**Step 1.** `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 57. `cos(x)*sec(x)/(tan(x)*cot(x)) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F03`

**Proof**

**Step 1.** `cos(x)*sec(x)/(tan(x)*cot(x))` → `cos(x)**2*sec(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2*sec(x)/(sin(x)*cot(x))` → `cos(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 58. `cos(x)*sec(x)/(tan(x)*csc(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `cos(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)**2*sec(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2*sec(x)/(sin(x)*csc(x))` → `cos(x)/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 59. `cos(x)*sec(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = 1`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F02`

**Proof**

**Step 1.** `cos(x)*sec(x)/tan(x)` → `cos(x)**2*sec(x)/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2*sec(x)/sin(x)` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 60. `cos(x)*sec(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = cot(x)`
- `d = 1`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F01`

**Proof**

**Step 1.** `cos(x)*sec(x)/cot(x)` → `sin(x)*sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*sec(x)` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 61. `cos(x)*sec(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = 1`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F04`

**Proof**

**Step 1.** `cos(x)*sec(x)/csc(x)` → `1/csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 62. `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cos(x)*sec(x)` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 63. `cos(x)*csc(x)/(sin(x)*cot(x)) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)*csc(x)/(sin(x)*cot(x))` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 64. `cos(x)*csc(x)/(tan(x)*cot(x)) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F04`

**Proof**

**Step 1.** `cos(x)*csc(x)/(tan(x)*cot(x))` → `cos(x)**2*csc(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2*csc(x)/(sin(x)*cot(x))` → `cos(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 65. `cos(x)*csc(x)/cot(x)**2 = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = cot(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04, F01`

**Proof**

**Step 1.** `cos(x)*csc(x)/cot(x)**2` → `sin(x)**2*csc(x)/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)**2*csc(x)/cos(x)` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 66. `cos(x)*csc(x)/(cot(x)*sec(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `1/sin(x) ≠ 0`
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cos(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)*csc(x)/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/sec(x)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 67. `cos(x)*csc(x)/cot(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cos(x)*csc(x)/cot(x)` → `sin(x)*csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 68. `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
- `e = cot(x)`
**Original common-domain conditions**
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F02`

**Proof**

**Step 1.** `cos(x)*csc(x)` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 69. `cos(x)/(sin(x)*cot(x)) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = sin(x)`
- `d = cot(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02`

**Proof**

**Step 1.** `cos(x)/(sin(x)*cot(x))` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 70. `cos(x)/(sin(x)*csc(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 71. `cos(x)/(tan(x)*cot(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `cos(x)/(tan(x)*cot(x))` → `cos(x)**2/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)**2/(sin(x)*cot(x))` → `cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 72. `tan(x)**2/(sin(x)*sec(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)**2/(sin(x)*sec(x))` → `sin(x)/(cos(x)**2*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/(cos(x)**2*sec(x))` → `sin(x)/cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 73. `tan(x)*cot(x)/(sin(x)*sec(x)) = cot(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)*cot(x)/(sin(x)*sec(x))` → `cot(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cot(x)/(cos(x)*sec(x))` → `cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 74. `tan(x)*cot(x)/(sin(x)*csc(x)) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F05`

**Proof**

**Step 1.** `tan(x)*cot(x)/(sin(x)*csc(x))` → `tan(x)*cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*cot(x)` → `1` — **F05**
   - Applied theorem: F05 — tan x · cot x = 1
   - Apply established identity F05 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F05 depends on F01
- F05 depends on F02

### 75. `tan(x)*cot(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = 1`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)/sin(x)` → `tan(x)*cot(x)*csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*cot(x)*csc(x)` → `sin(x)*cot(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*cot(x)*csc(x)/cos(x)` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 76. `tan(x)*cot(x)/(cos(x)*sec(x)) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F05`

**Proof**

**Step 1.** `tan(x)*cot(x)/(cos(x)*sec(x))` → `tan(x)*cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*cot(x)` → `1` — **F05**
   - Applied theorem: F05 — tan x · cot x = 1
   - Apply established identity F05 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.
**Dependency provenance:**
- F05 depends on F01
- F05 depends on F02

### 77. `tan(x)*cot(x)/(cos(x)*csc(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `1/tan(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `tan(x)*cot(x)/(cos(x)*csc(x))` → `tan(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)/(sin(x)*csc(x))` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 78. `tan(x)*cot(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = 1`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)/cos(x)` → `tan(x)*cot(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*cot(x)*sec(x)` → `sin(x)*cot(x)*sec(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*cot(x)*sec(x)/cos(x)` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 79. `tan(x)*cot(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = 1`
- `e = cos(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F03`

**Proof**

**Step 1.** `tan(x)*cot(x)/sec(x)` → `sin(x)*cot(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/(cos(x)*sec(x))` → `1/sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sec(x)` → `cos(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 80. `tan(x)*cot(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = 1`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02, F04`

**Proof**

**Step 1.** `tan(x)*cot(x)/csc(x)` → `sin(x)*cot(x)/(cos(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/(cos(x)*csc(x))` → `1/csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/csc(x)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 81. `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `tan(x)*cot(x)` → `sin(x)*cot(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*cot(x)/cos(x)` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 82. `tan(x)*csc(x)/(sin(x)*sec(x)) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)*csc(x)/(sin(x)*sec(x))` → `csc(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `csc(x)/(cos(x)*sec(x))` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 83. `tan(x)*csc(x)/(cos(x)*sec(x)) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F01, F04`

**Proof**

**Step 1.** `tan(x)*csc(x)/(cos(x)*sec(x))` → `tan(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*csc(x)/cos(x)` → `sin(x)*csc(x)*sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `sin(x)*csc(x)*sec(x)` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 84. `tan(x)*csc(x)/(cot(x)*sec(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `1/sin(x) ≠ 0`
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `tan(x)*csc(x)/(cot(x)*sec(x))` → `sin(x)*tan(x)*csc(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*tan(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*tan(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*tan(x)*csc(x)` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 85. `tan(x)*csc(x)/sec(x)**2 = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = sec(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `tan(x)*csc(x)/sec(x)**2` → `sin(x)*csc(x)/(cos(x)*sec(x)**2)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/(cos(x)*sec(x)**2)` → `(sin(x)*csc(x))/((cos(x)*sec(x)**2))`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `(sin(x)*csc(x))/((cos(x)*sec(x)**2))` → `sin(x)*csc(x)/(cos(x)*sec(x)**2)`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 4.** `sin(x)*csc(x)/(cos(x)*sec(x)**2)` → `sin(x)*cos(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `sin(x)*cos(x)*csc(x)` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 86. `tan(x)*csc(x)/sec(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `tan(x)*csc(x)/sec(x)` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 87. `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04, F03`

**Proof**

**Step 1.** `tan(x)*csc(x)` → `sin(x)*csc(x)/cos(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/cos(x)` → `1/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 88. `tan(x)/(sin(x)*sec(x)) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03`

**Proof**

**Step 1.** `tan(x)/(sin(x)*sec(x))` → `1/(cos(x)*sec(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/(cos(x)*sec(x))` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 89. `tan(x)/(sin(x)*csc(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `tan(x)/(sin(x)*csc(x))` → `tan(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 90. `tan(x)/(cos(x)*sec(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `tan(x)/(cos(x)*sec(x))` → `tan(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 91. `cot(x)**2/(cos(x)*csc(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `1/tan(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)**2/(cos(x)*csc(x))` → `cos(x)/(sin(x)**2*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/(sin(x)**2*csc(x))` → `cos(x)/((sin(x)**2*csc(x)))`
   - Factor the numerator and denominator separately; common factors are not cancelled in this step.
**Step 3.** `cos(x)/((sin(x)**2*csc(x)))` → `cos(x)/(sin(x)**2*csc(x))`
   - Cancel common factors. The original and intermediate denominator restrictions remain in force.
**Step 4.** `cos(x)/(sin(x)**2*csc(x))` → `cos(x)/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 5.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 92. `cot(x)*sec(x)/(sin(x)*csc(x)) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F02, F03`

**Proof**

**Step 1.** `cot(x)*sec(x)/(sin(x)*csc(x))` → `cot(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cos(x)*sec(x)/sin(x)` → `cos(x)*csc(x)*sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `cos(x)*csc(x)*sec(x)` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 93. `cot(x)*sec(x)/(cos(x)*csc(x)) = sec(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `1/tan(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)/(cos(x)*csc(x))` → `sec(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 94. `cot(x)*sec(x)/(tan(x)*csc(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)/(tan(x)*csc(x))` → `cos(x)*cot(x)*sec(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*cot(x)*sec(x)/(sin(x)*csc(x))` → `cot(x)/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `cot(x)/(sin(x)*csc(x))` → `cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 95. `cot(x)*sec(x)/csc(x)**2 = sin(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = csc(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)/csc(x)**2` → `cos(x)*sec(x)/(sin(x)*csc(x)**2)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/(sin(x)*csc(x)**2)` → `1/(sin(x)*csc(x)**2)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/(sin(x)*csc(x)**2)` → `sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 96. `cot(x)*sec(x)/csc(x) = 1`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = 1`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)/csc(x)` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 97. `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `cot(x)*sec(x)` → `cos(x)*sec(x)/sin(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/sin(x)` → `1/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 98. `cot(x)/(sin(x)*csc(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `cot(x)/(sin(x)*csc(x))` → `cot(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 99. `cot(x)/(cos(x)*sec(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `cot(x)/(cos(x)*sec(x))` → `cot(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 100. `cot(x)/(cos(x)*csc(x)) = 1`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cos(x)`
- `d = csc(x)`
- `e = 1`
**Original common-domain conditions**
- `1/tan(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F04`

**Proof**

**Step 1.** `cot(x)/(cos(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 101. `sec(x)**2/(tan(x)*csc(x)) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `sec(x)**2/(tan(x)*csc(x))` → `cos(x)*sec(x)**2/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)**2/(sin(x)*csc(x))` → `1/(sin(x)*cos(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/(sin(x)*cos(x)*csc(x))` → `sec(x)/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 102. `sec(x)/(sin(x)*csc(x)) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `sec(x)/(sin(x)*csc(x))` → `sec(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 103. `sec(x)/(tan(x)*cot(x)) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `sec(x)/(tan(x)*cot(x))` → `cos(x)*sec(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/(sin(x)*cot(x))` → `sec(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 104. `sec(x)/(tan(x)*csc(x)) = 1`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = tan(x)`
- `d = csc(x)`
- `e = 1`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F03, F04`

**Proof**

**Step 1.** `sec(x)/(tan(x)*csc(x))` → `cos(x)*sec(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*sec(x)/(sin(x)*csc(x))` → `1/(sin(x)*csc(x))` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 105. `csc(x)**2/(cot(x)*sec(x)) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `1/sin(x) ≠ 0`
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `csc(x)**2/(cot(x)*sec(x))` → `sin(x)*csc(x)**2/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)**2/(cos(x)*sec(x))` → `sin(x)*csc(x)**2` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*csc(x)**2` → `1/sin(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 4.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 106. `csc(x)/(cos(x)*sec(x)) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `csc(x)/(cos(x)*sec(x))` → `csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 107. `csc(x)/(tan(x)*cot(x)) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `csc(x)/(tan(x)*cot(x))` → `cos(x)*csc(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)*csc(x)/(sin(x)*cot(x))` → `csc(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 108. `csc(x)/(cot(x)*sec(x)) = 1`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cot(x)`
- `d = sec(x)`
- `e = 1`
**Original common-domain conditions**
- `1/sin(x) ≠ 0`
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03, F04`

**Proof**

**Step 1.** `csc(x)/(cot(x)*sec(x))` → `sin(x)*csc(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)*csc(x)/(cos(x)*sec(x))` → `sin(x)*csc(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 3.** `sin(x)*csc(x)` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 109. `1/(sin(x)*cot(x)) = sec(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03`

**Proof**

**Step 1.** `1/(sin(x)*cot(x))` → `1/cos(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/cos(x)` → `sec(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 110. `1/(sin(x)*sec(x)) = cot(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03, F02`

**Proof**

**Step 1.** `1/(sin(x)*sec(x))` → `cos(x)/sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/sin(x)` → `cot(x)` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 111. `1/(sin(x)*csc(x)) = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = 1`
**Original common-domain conditions**
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04`

**Proof**

**Step 1.** `1/(sin(x)*csc(x))` → `1` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 112. `1/(cos(x)*tan(x)) = csc(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cos(x)`
- `d = tan(x)`
- `e = csc(x)`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04`

**Proof**

**Step 1.** `1/(cos(x)*tan(x))` → `1/sin(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `1/sin(x)` → `csc(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 113. `1/(cos(x)*sec(x)) = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `sec(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F03`

**Proof**

**Step 1.** `1/(cos(x)*sec(x))` → `1` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 114. `1/(cos(x)*csc(x)) = tan(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cos(x)`
- `d = csc(x)`
- `e = tan(x)`
**Original common-domain conditions**
- `1/tan(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F04, F01`

**Proof**

**Step 1.** `1/(cos(x)*csc(x))` → `sin(x)/cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/cos(x)` → `tan(x)` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 115. `1/(tan(x)*cot(x)) = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = 1`
**Original common-domain conditions**
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F02`

**Proof**

**Step 1.** `1/(tan(x)*cot(x))` → `cos(x)/(sin(x)*cot(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/(sin(x)*cot(x))` → `1` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 116. `1/(tan(x)*csc(x)) = cos(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = tan(x)`
- `d = csc(x)`
- `e = cos(x)`
**Original common-domain conditions**
- `1/cos(x) ≠ 0`
- `cos(x) ≠ 0`
- `csc(x) ≠ 0`
- `sin(x) ≠ 0`
- `tan(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F01, F04`

**Proof**

**Step 1.** `1/(tan(x)*csc(x))` → `cos(x)/(sin(x)*csc(x))` — **F01**
   - Applied theorem: F01 — tan x = sin x / cos x
   - Apply established identity F01 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `cos(x)/(sin(x)*csc(x))` → `cos(x)` — **F04**
   - Applied theorem: F04 — csc x = 1/sin x
   - Apply established identity F04 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

### 117. `1/(cot(x)*sec(x)) = sin(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cot(x)`
- `d = sec(x)`
- `e = sin(x)`
**Original common-domain conditions**
- `1/sin(x) ≠ 0`
- `cos(x) ≠ 0`
- `cot(x) ≠ 0`
- `sec(x) ≠ 0`
- `sin(x) ≠ 0`

**Selected engine route:** `LHS using identity catalogue`
**Identity/proof IDs:** `F02, F03`

**Proof**

**Step 1.** `1/(cot(x)*sec(x))` → `sin(x)/(cos(x)*sec(x))` — **F02**
   - Applied theorem: F02 — cot x = cos x / sin x
   - Apply established identity F02 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`
**Step 2.** `sin(x)/(cos(x)*sec(x))` → `sin(x)` — **F03**
   - Applied theorem: F03 — sec x = 1/cos x
   - Apply established identity F03 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Substitution: `x → x`

**Certificate:** `trigonometric-proof-certificate-v4` — `PROVED`.

