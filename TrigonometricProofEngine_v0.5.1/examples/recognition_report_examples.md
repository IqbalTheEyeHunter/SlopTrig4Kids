# v0.5.1 Recognition Report Examples

These are illustrative inputs. The recogniser identifies candidate structures only; it does not prove or solve them.

## Single-function equation

**Input**
```text
sin(2*x)=1/2
```

**Prompt:** Solve for 0 <= x <= 2*pi.

**Recognised classes:** EQREC-022, EQREC-043, EQREC-006, EQREC-001, EQREC-038

**Task type:** Trigonometric equation

**Cautions:**
- Recognition is structural guidance only; it does not prove the relation or solve it.
- All original denominator, reciprocal-function and radical restrictions remain in force.

## Non-constant graph intersection

**Input**
```text
sin(x)=x/pi
```

**Prompt:** Solve graphically and state the number of intersections.

**Recognised classes:** EQREC-039, EQREC-041, EQREC-053

**Task type:** Graphical equation / solution count

**Cautions:**
- Recognition is structural guidance only; it does not prove the relation or solve it.
- All original denominator, reciprocal-function and radical restrictions remain in force.
- Numerical graph roots are approximations; completeness requires a separate root-count or interval argument.
- Nested or mixed transcendental equations may exceed the exact capabilities of the current engine.

## Rational equation with a cancellation hazard

**Input**
```text
sin(x)/sin(x)=1
```

**Prompt:** Identify the original domain before cancellation.

**Recognised classes:** EQREC-027, EQREC-032, EQREC-054, EQREC-038

**Task type:** Trigonometric equation / relation

**Cautions:**
- Recognition is structural guidance only; it does not prove the relation or solve it.
- All original denominator, reciprocal-function and radical restrictions remain in force.

## Multipart proof followed by equation

**Input**
```text
sin(x)**2+cos(x)**2=1
sin(x)=1/2
```

**Prompt:** Prove the identity, hence solve the equation.

**Recognised classes:** EQREC-055, EQREC-051, EQREC-016, EQREC-019, EQREC-001, EQREC-038

**Task type:** Multi-part proof followed by equation

**Cautions:**
- Recognition is structural guidance only; it does not prove the relation or solve it.
- All original denominator, reciprocal-function and radical restrictions remain in force.
- A later subpart may use an earlier result only after that result has an accepted proof certificate.
