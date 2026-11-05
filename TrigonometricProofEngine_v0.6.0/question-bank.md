# Trigonometric Proof Engine v0.6.0 — Question Bank

**File:** `question-bank.md`  
**Companion:** `proof-solutions.md`  
**Purpose:** a question-only training corpus. Full checked derivations are kept in the companion solutions file.

## 1. Finite search scope

Each metavariable `a`, `b`, `c`, `d`, or `e` is assigned one atom from the following seven-element alphabet, all at the same real angle `x`: 
`sin(x)`, `cos(x)`, `tan(x)`, `cot(x)`, `sec(x)`, `csc(x)`, `1`.

All ordered assignments were enumerated for the eleven requested operation templates. This is exhaustive only over this finite alphabet and those templates; it is not a claim of exhaustiveness over arbitrary compound trigonometric expressions, multiple angles, or compound arguments.

## 2. Admission rules

- Only claims whose v0.6.0 proof route returned `PROVED` are included.
- Candidate discovery is not proof: exact rational/unit-circle reduction only identifies candidates; the proof engine must construct and validate a derivation.
- F08 itself is admitted only through its independent geometric certificate `G01 → G03 → G04`.
- F08, F09 and F10 may be reused as established theorems for different goals, with their audited dependency chains.
- A goal that is F08/F09/F10 itself, including a constant-scaled or rearranged instance, cannot use that same theorem as a premise.
- Original common-domain conditions are retained. Omitted candidates are not thereby proved false.

## 3. Search summary

| Operation template | Raw assignments | Unique candidates checked | Proved entries |
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
| `ab - cd = e` | 16,807 | 10 | 8 |
| `ab/cd = e` | 16,807 | 121 | 117 |

**Raw assignments searched:** 61,397.  
**Unique candidate claims checked:** 156.  
**Unique claims returned as PROVED:** 150.  
**Template entries recorded (including repeated claims under different templates):** 255.

## 4. Proved questions

Only proved questions are listed below. Repeated claims under different operation templates retain separate IDs because the original question structure and variable assignments differ.


---

## a + b = c

No identity in this finite search space was returned as `PROVED` by v0.6.0.

---

## a - b = c

No identity in this finite search space was returned as `PROVED` by v0.6.0.

---

## ab = c

### QB-03-001 — `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-03-002 — `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-03-003 — `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`

**Original common domain:** `sin(x) ≠ 0`

### QB-03-004 — `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-03-005 — `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-03-006 — `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`

**Original common domain:** `cos(x) ≠ 0`

### QB-03-007 — `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-03-008 — `cos(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = cos(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-03-009 — `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-03-010 — `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-03-011 — `tan(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-03-012 — `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-03-013 — `cot(x) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-03-014 — `sec(x) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-03-015 — `csc(x) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-03-016 — `1 = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = 1`

**Original common domain:** All real values of the variables in the stated claim.


---

## a/b = c

### QB-04-001 — `1 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = 1`

**Original common domain:** All real values of the variables in the stated claim.

### QB-04-002 — `sin(x)/tan(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

### QB-04-003 — `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-04-004 — `cos(x)/cot(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cot(x)`
- `c = sin(x)`

**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-005 — `cos(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = cos(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-04-006 — `tan(x)/sin(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = sin(x)`
- `c = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-007 — `tan(x)/sec(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = sec(x)`
- `c = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-04-008 — `tan(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-04-009 — `cot(x)/cos(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = cos(x)`
- `c = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-010 — `cot(x)/csc(x) = cos(x)`

**Variable assignment**
- `a = cot(x)`
- `b = csc(x)`
- `c = cos(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-011 — `cot(x) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-04-012 — `sec(x)/tan(x) = csc(x)`

**Variable assignment**
- `a = sec(x)`
- `b = tan(x)`
- `c = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-04-013 — `sec(x)/csc(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-014 — `sec(x) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-04-015 — `csc(x)/cot(x) = sec(x)`

**Variable assignment**
- `a = csc(x)`
- `b = cot(x)`
- `c = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-016 — `csc(x)/sec(x) = cot(x)`

**Variable assignment**
- `a = csc(x)`
- `b = sec(x)`
- `c = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-017 — `csc(x) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-04-018 — `1/tan(x) = cot(x)`

**Variable assignment**
- `a = 1`
- `b = tan(x)`
- `c = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-04-019 — `1/cot(x) = tan(x)`

**Variable assignment**
- `a = 1`
- `b = cot(x)`
- `c = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-04-020 — `1/sec(x) = cos(x)`

**Variable assignment**
- `a = 1`
- `b = sec(x)`
- `c = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-04-021 — `1/csc(x) = sin(x)`

**Variable assignment**
- `a = 1`
- `b = csc(x)`
- `c = sin(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`


---

## ab + c = d

### QB-05-001 — `sin(x)*tan(x) + cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cos(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-05-002 — `sin(x) + cos(x)*cot(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`

**Original common domain:** `sin(x) ≠ 0`


---

## ab - c = d

### QB-06-001 — `-tan(x) + csc(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-06-002 — `-cot(x) + csc(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`


---

## abc = d

### QB-07-001 — `sin(x)**2*csc(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = csc(x)`
- `d = sin(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-002 — `sin(x)*cos(x)*sec(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sec(x)`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-003 — `sin(x)*cos(x)*csc(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = csc(x)`
- `d = cos(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-004 — `sin(x)*tan(x)*cot(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cot(x)`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-005 — `sin(x)*tan(x)*csc(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = csc(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-006 — `sin(x)*cot(x)*sec(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-007 — `sin(x)*cot(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-008 — `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = 1`
- `d = cos(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-009 — `sin(x)*csc(x)*sec(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-010 — `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = 1`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-011 — `sin(x)*csc(x)**2 = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = csc(x)`
- `d = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-012 — `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-013 — `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = 1`
- `d = sin(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-07-014 — `cos(x)**2*sec(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cos(x)`
- `c = sec(x)`
- `d = cos(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-015 — `cos(x)*tan(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = cot(x)`
- `d = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-016 — `cos(x)*tan(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sec(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-017 — `cos(x)*tan(x)*csc(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = csc(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-018 — `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = 1`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-019 — `cos(x)*cot(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-020 — `cos(x)*sec(x)**2 = sec(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sec(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-021 — `cos(x)*csc(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-022 — `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-023 — `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = 1`
- `d = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-024 — `cos(x) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = 1`
- `d = cos(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-07-025 — `tan(x)**2*cot(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = tan(x)`
- `c = cot(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-026 — `tan(x)*cot(x)**2 = cot(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cot(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-027 — `tan(x)*cot(x)*sec(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-028 — `tan(x)*cot(x)*csc(x) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-029 — `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-030 — `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = 1`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-031 — `tan(x) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = 1`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-032 — `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = 1`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-07-033 — `cot(x) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = 1`
- `d = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-034 — `sec(x) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = 1`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-07-035 — `csc(x) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = 1`
- `d = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-07-036 — `1 = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = 1`
- `d = 1`

**Original common domain:** All real values of the variables in the stated claim.


---

## ab/c = d

### QB-08-001 — `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = sin(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-08-002 — `cos(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = cos(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-08-003 — `tan(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-08-004 — `cot(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-08-005 — `sin(x)*cot(x)/cos(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-006 — `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = 1`
- `d = cos(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-08-007 — `sec(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-08-008 — `sin(x)*sec(x)/tan(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

### QB-08-009 — `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = 1`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-08-010 — `csc(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-08-011 — `sin(x)*csc(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-012 — `sin(x)*csc(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-08-013 — `sin(x)*csc(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-014 — `sin(x)*csc(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-015 — `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`

**Original common domain:** `sin(x) ≠ 0`

### QB-08-016 — `1 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = 1`

**Original common domain:** All real values of the variables in the stated claim.

### QB-08-017 — `sin(x)/tan(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = tan(x)`
- `d = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

### QB-08-018 — `cos(x)*tan(x)/sin(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-019 — `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = 1`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-08-020 — `cos(x)*sec(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-021 — `cos(x)*sec(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-08-022 — `cos(x)*sec(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = cot(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-023 — `cos(x)*sec(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-024 — `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`

### QB-08-025 — `cos(x)*csc(x)/cot(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`

**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-026 — `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = 1`
- `d = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-08-027 — `cos(x)/cot(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = cot(x)`
- `d = sin(x)`

**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-028 — `tan(x)*cot(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-029 — `tan(x)*cot(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-030 — `tan(x)*cot(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-031 — `tan(x)*cot(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-032 — `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-033 — `tan(x)*csc(x)/sec(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-034 — `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = 1`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-035 — `tan(x)/sin(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-036 — `tan(x)/sec(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sec(x)`
- `d = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-08-037 — `cot(x)*sec(x)/csc(x) = 1`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = 1`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-038 — `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = 1`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-039 — `cot(x)/cos(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cos(x)`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-040 — `cot(x)/csc(x) = cos(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = csc(x)`
- `d = cos(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-041 — `sec(x)/tan(x) = csc(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = tan(x)`
- `d = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-08-042 — `sec(x)/csc(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = csc(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-043 — `csc(x)/cot(x) = sec(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cot(x)`
- `d = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-044 — `csc(x)/sec(x) = cot(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = sec(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-045 — `1/tan(x) = cot(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-08-046 — `1/cot(x) = tan(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cot(x)`
- `d = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-08-047 — `1/sec(x) = cos(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sec(x)`
- `d = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-08-048 — `1/csc(x) = sin(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = csc(x)`
- `d = sin(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`


---

## ab + cd = e

### QB-09-001 — `sin(x)**2 + cos(x)**2 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = cos(x)`
- `d = cos(x)`
- `e = 1`

**Original common domain:** All real values of the variables in the stated claim.

### QB-09-002 — `sin(x)*tan(x) + sin(x)*cot(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-09-003 — `sin(x)*tan(x) + cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = cos(x)`
- `d = 1`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-09-004 — `sin(x) + cos(x)*cot(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = cos(x)`
- `d = cot(x)`
- `e = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-09-005 — `cos(x)*tan(x) + cos(x)*cot(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = cos(x)`
- `d = cot(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`


---

## ab - cd = e

### QB-10-001 — `-sin(x)*tan(x) + tan(x)*csc(x) = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = tan(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-10-002 — `-cos(x)*cot(x) + cot(x)*sec(x) = sin(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = cos(x)`
- `d = cot(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-10-003 — `-sin(x)*sec(x) + csc(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-10-004 — `-cos(x)*csc(x) + csc(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-10-005 — `-tan(x) + csc(x)*sec(x) = cot(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = 1`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-10-006 — `-cot(x) + csc(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sec(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-10-007 — `-sin(x)*tan(x) + sec(x) = cos(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sin(x)`
- `d = tan(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-10-008 — `-cos(x)*cot(x) + csc(x) = sin(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cos(x)`
- `d = cot(x)`
- `e = sin(x)`

**Original common domain:** `sin(x) ≠ 0`


---

## ab/cd = e

### QB-11-001 — `1 = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = sin(x)`
- `e = 1`

**Original common domain:** All real values of the variables in the stated claim.

### QB-11-002 — `sin(x)/tan(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = tan(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-003 — `sin(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = sin(x)`
- `d = 1`
- `e = sin(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-11-004 — `sin(x)**2/(cos(x)*tan(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sin(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-005 — `cos(x)/cot(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sin(x)`

**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-006 — `cos(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = 1`
- `e = cos(x)`

**Original common domain:** All real values of the variables in the stated claim.

### QB-11-007 — `tan(x)/sin(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sin(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-008 — `tan(x)/sec(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-11-009 — `tan(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = 1`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-11-010 — `cot(x)/cos(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = cos(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-011 — `cot(x)/csc(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = cos(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-012 — `cot(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = 1`
- `e = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-11-013 — `sin(x)*cot(x)/cos(x)**2 = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = cos(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-014 — `sin(x)*cot(x)/(cos(x)*tan(x)) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-015 — `sin(x)*cot(x)/(cos(x)*sec(x)) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-016 — `sin(x)*cot(x)/(cos(x)*csc(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = sin(x)`

**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-017 — `sin(x)*cot(x)/cos(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-018 — `sin(x)*cot(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`
- `e = cos(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-11-019 — `sec(x)/tan(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = tan(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-020 — `sec(x)/csc(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-021 — `sec(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = 1`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-11-022 — `sin(x)*sec(x)/(cos(x)*tan(x)) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-023 — `sin(x)*sec(x)/tan(x)**2 = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = tan(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-024 — `sin(x)*sec(x)/(tan(x)*cot(x)) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-025 — `sin(x)*sec(x)/(tan(x)*csc(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = sin(x)`

**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-026 — `sin(x)*sec(x)/tan(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-027 — `sin(x)*sec(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-11-028 — `csc(x)/cot(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-029 — `csc(x)/sec(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-030 — `csc(x) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = 1`
- `e = csc(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-11-031 — `sin(x)*csc(x)/(cos(x)*tan(x)) = csc(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = tan(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-032 — `sin(x)*csc(x)/(cos(x)*sec(x)) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-033 — `sin(x)*csc(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = 1`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-034 — `sin(x)*csc(x)/(tan(x)*cot(x)) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-035 — `sin(x)*csc(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = 1`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-036 — `sin(x)*csc(x)/(cot(x)*sec(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = sin(x)`

**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-037 — `sin(x)*csc(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-038 — `sin(x)*csc(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = 1`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-039 — `sin(x)*csc(x) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
- `e = 1`

**Original common domain:** `sin(x) ≠ 0`

### QB-11-040 — `1/tan(x) = cot(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = tan(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-041 — `1/cot(x) = tan(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = cot(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-042 — `1/sec(x) = cos(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-11-043 — `1/csc(x) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = sin(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-044 — `sin(x)/(cos(x)*tan(x)) = 1`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = cos(x)`
- `d = tan(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-045 — `sin(x)/(cos(x)*sec(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-11-046 — `sin(x)/(tan(x)*cot(x)) = sin(x)`

**Variable assignment**
- `a = sin(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-047 — `cos(x)**2/(sin(x)*cot(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = cos(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-048 — `cos(x)*tan(x)/sin(x)**2 = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sin(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-049 — `cos(x)*tan(x)/(sin(x)*cot(x)) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-050 — `cos(x)*tan(x)/(sin(x)*sec(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-051 — `cos(x)*tan(x)/(sin(x)*csc(x)) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-052 — `cos(x)*tan(x)/sin(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-053 — `cos(x)*tan(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = tan(x)`
- `c = 1`
- `d = 1`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`

### QB-11-054 — `cos(x)*sec(x)/(sin(x)*cot(x)) = sec(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-055 — `cos(x)*sec(x)/(sin(x)*csc(x)) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-056 — `cos(x)*sec(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = 1`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-057 — `cos(x)*sec(x)/(tan(x)*cot(x)) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-058 — `cos(x)*sec(x)/(tan(x)*csc(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = cos(x)`

**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-059 — `cos(x)*sec(x)/tan(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = 1`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-060 — `cos(x)*sec(x)/cot(x) = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = cot(x)`
- `d = 1`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-061 — `cos(x)*sec(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = 1`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-062 — `cos(x)*sec(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`

### QB-11-063 — `cos(x)*csc(x)/(sin(x)*cot(x)) = csc(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = cot(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-064 — `cos(x)*csc(x)/(tan(x)*cot(x)) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = tan(x)`
- `d = cot(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-065 — `cos(x)*csc(x)/cot(x)**2 = tan(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = cot(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-066 — `cos(x)*csc(x)/(cot(x)*sec(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = cos(x)`

**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-067 — `cos(x)*csc(x)/cot(x) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = 1`
- `e = 1`

**Original common domain:** `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-068 — `cos(x)*csc(x) = cot(x)`

**Variable assignment**
- `a = cos(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
- `e = cot(x)`

**Original common domain:** `sin(x) ≠ 0`

### QB-11-069 — `cos(x)/(sin(x)*cot(x)) = 1`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = sin(x)`
- `d = cot(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-070 — `cos(x)/(sin(x)*csc(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = cos(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-071 — `cos(x)/(tan(x)*cot(x)) = cos(x)`

**Variable assignment**
- `a = cos(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-072 — `tan(x)**2/(sin(x)*sec(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = tan(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-073 — `tan(x)*cot(x)/(sin(x)*sec(x)) = cot(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-074 — `tan(x)*cot(x)/(sin(x)*csc(x)) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-075 — `tan(x)*cot(x)/sin(x) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sin(x)`
- `d = 1`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-076 — `tan(x)*cot(x)/(cos(x)*sec(x)) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-077 — `tan(x)*cot(x)/(cos(x)*csc(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = tan(x)`

**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-078 — `tan(x)*cot(x)/cos(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = 1`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-079 — `tan(x)*cot(x)/sec(x) = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = sec(x)`
- `d = 1`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-080 — `tan(x)*cot(x)/csc(x) = sin(x)`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = csc(x)`
- `d = 1`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-081 — `tan(x)*cot(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = cot(x)`
- `c = 1`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-082 — `tan(x)*csc(x)/(sin(x)*sec(x)) = csc(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sin(x)`
- `d = sec(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-083 — `tan(x)*csc(x)/(cos(x)*sec(x)) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = cos(x)`
- `d = sec(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-084 — `tan(x)*csc(x)/(cot(x)*sec(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = tan(x)`

**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-085 — `tan(x)*csc(x)/sec(x)**2 = cos(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = sec(x)`
- `e = cos(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-086 — `tan(x)*csc(x)/sec(x) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = sec(x)`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-087 — `tan(x)*csc(x) = sec(x)`

**Variable assignment**
- `a = tan(x)`
- `b = csc(x)`
- `c = 1`
- `d = 1`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-088 — `tan(x)/(sin(x)*sec(x)) = 1`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-089 — `tan(x)/(sin(x)*csc(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-090 — `tan(x)/(cos(x)*sec(x)) = tan(x)`

**Variable assignment**
- `a = tan(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = tan(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-11-091 — `cot(x)**2/(cos(x)*csc(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = cot(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = cot(x)`

**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-092 — `cot(x)*sec(x)/(sin(x)*csc(x)) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = sin(x)`
- `d = csc(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-093 — `cot(x)*sec(x)/(cos(x)*csc(x)) = sec(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = cos(x)`
- `d = csc(x)`
- `e = sec(x)`

**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-094 — `cot(x)*sec(x)/(tan(x)*csc(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = cot(x)`

**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-095 — `cot(x)*sec(x)/csc(x)**2 = sin(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = csc(x)`
- `e = sin(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-096 — `cot(x)*sec(x)/csc(x) = 1`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = csc(x)`
- `d = 1`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-097 — `cot(x)*sec(x) = csc(x)`

**Variable assignment**
- `a = cot(x)`
- `b = sec(x)`
- `c = 1`
- `d = 1`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-098 — `cot(x)/(sin(x)*csc(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = cot(x)`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-099 — `cot(x)/(cos(x)*sec(x)) = cot(x)`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-100 — `cot(x)/(cos(x)*csc(x)) = 1`

**Variable assignment**
- `a = cot(x)`
- `b = 1`
- `c = cos(x)`
- `d = csc(x)`
- `e = 1`

**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-101 — `sec(x)**2/(tan(x)*csc(x)) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = sec(x)`
- `c = tan(x)`
- `d = csc(x)`
- `e = sec(x)`

**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-102 — `sec(x)/(sin(x)*csc(x)) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-103 — `sec(x)/(tan(x)*cot(x)) = sec(x)`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-104 — `sec(x)/(tan(x)*csc(x)) = 1`

**Variable assignment**
- `a = sec(x)`
- `b = 1`
- `c = tan(x)`
- `d = csc(x)`
- `e = 1`

**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-105 — `csc(x)**2/(cot(x)*sec(x)) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = csc(x)`
- `c = cot(x)`
- `d = sec(x)`
- `e = csc(x)`

**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-106 — `csc(x)/(cos(x)*sec(x)) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-107 — `csc(x)/(tan(x)*cot(x)) = csc(x)`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-108 — `csc(x)/(cot(x)*sec(x)) = 1`

**Variable assignment**
- `a = csc(x)`
- `b = 1`
- `c = cot(x)`
- `d = sec(x)`
- `e = 1`

**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-109 — `1/(sin(x)*cot(x)) = sec(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sin(x)`
- `d = cot(x)`
- `e = sec(x)`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-110 — `1/(sin(x)*sec(x)) = cot(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sin(x)`
- `d = sec(x)`
- `e = cot(x)`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-111 — `1/(sin(x)*csc(x)) = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = sin(x)`
- `d = csc(x)`
- `e = 1`

**Original common domain:** `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-112 — `1/(cos(x)*tan(x)) = csc(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cos(x)`
- `d = tan(x)`
- `e = csc(x)`

**Original common domain:** `cos(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-113 — `1/(cos(x)*sec(x)) = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cos(x)`
- `d = sec(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `sec(x) ≠ 0`

### QB-11-114 — `1/(cos(x)*csc(x)) = tan(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cos(x)`
- `d = csc(x)`
- `e = tan(x)`

**Original common domain:** `1/tan(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`

### QB-11-115 — `1/(tan(x)*cot(x)) = 1`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = tan(x)`
- `d = cot(x)`
- `e = 1`

**Original common domain:** `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-116 — `1/(tan(x)*csc(x)) = cos(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = tan(x)`
- `d = csc(x)`
- `e = cos(x)`

**Original common domain:** `1/cos(x) ≠ 0`; `cos(x) ≠ 0`; `csc(x) ≠ 0`; `sin(x) ≠ 0`; `tan(x) ≠ 0`

### QB-11-117 — `1/(cot(x)*sec(x)) = sin(x)`

**Variable assignment**
- `a = 1`
- `b = 1`
- `c = cot(x)`
- `d = sec(x)`
- `e = sin(x)`

**Original common domain:** `1/sin(x) ≠ 0`; `cos(x) ≠ 0`; `cot(x) ≠ 0`; `sec(x) ≠ 0`; `sin(x) ≠ 0`


## 5. Supplementary theorem-reuse questions

### SUP-001 — Orthogonal linear-combination identity

**Question:** `(p*cos(x)+q*sin(x))**2+(p*sin(x)-q*cos(x))**2 = p**2+q**2`

**Purpose:** The corrected parameterised identity; it is not an F08/F09/F10 goal.

**Original common domain:** All real values of the variables in the stated claim.

---

### SUP-002 — Using F09 in a different identity

**Question:** `(1+tan(x)**2)*cos(x)**2 = sec(x)**2*cos(x)**2`

**Purpose:** F09 is used as a lemma for a distinct target.

**Original common domain:** `cos(x) ≠ 0`

---

### SUP-003 — Using F10 in a different identity

**Question:** `(1+cot(x)**2)*sin(x)**2 = csc(x)**2*sin(x)**2`

**Purpose:** F10 is used as a lemma for a distinct target.

**Original common domain:** `sin(x) ≠ 0`
