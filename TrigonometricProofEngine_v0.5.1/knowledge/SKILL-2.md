---
name: malaysian-additional-mathematics-trigonometric-recognition
version: 1.0.0
status: knowledge-specification
intended_engine: Trigonometric Proof Engine v0.5.5 (future target; not implemented by this file)
language: English with Malaysian KSSM terminology and bilingual notation aliases
scope: KSSM Additional Mathematics Form 5, Topic 6.0 Trigonometric Functions, with explicitly labelled recognition extensions
companion: SKILL.md
---

# SKILL-2 — Malaysian Form 5 Additional Mathematics: Trigonometric Equation and Proof Recognition

## Purpose and authority

This file is a **recognition and classification knowledge base** intended to complement the existing `SKILL.md`. Its principal goal is to let a future version of the Trigonometric Proof Engine recognise the mathematical structure of trigonometric equations and proof prompts even when the exact expression, arrangement, wording, or formula is not listed in `SKILL.md`.

It is designed around the Malaysian **KSSM Additional Mathematics Form 5, Topic 6.0 — Trigonometric Functions**. It also records wider six-function equation patterns that are natural extensions of that curriculum. The extension material is labelled so that the engine does not misrepresent it as a specific KSSM learning standard.

This file does not implement v0.5.5, alter the engine, add executable code, or certify any theorem. It specifies what a future recogniser should detect, what mathematical route it should consider, and what safeguards must remain in force.

### Recognition is not proof

A pattern match means only that an expression resembles a known mathematical problem family. It does **not** establish that:

- the equation is true;
- a proposed identity is valid;
- a transformation is reversible;
- every solution has been found;
- a formula is an independent theorem;
- a saved theorem is safe to reuse.

The engine must keep separate states for **recognised**, **candidate method identified**, **symbolically checked**, **certificate verified**, **proved**, **solved completely**, **disproved**, and **inconclusive**. A recognised pattern must never be promoted directly to `PROVED` or `SOLVED`.

A finite skill file cannot enumerate every possible trigonometric equation. The intended form of exhaustiveness is therefore **structural coverage**: recognise broad expression families by syntax-tree features, variable/angle structure, domain, transformations, graph behaviour, and task wording rather than by exact-string lookup alone.

---

# PART A — MALAYSIAN CURRICULUM AND COGNITIVE SCOPE

## A1. Curriculum anchor: KSSM Additional Mathematics Form 5

The relevant curriculum unit is:

- Learning area: Trigonometry
- Topic: **6.0 Trigonometric Functions**
- Content standards: 6.1 through 6.6

The DSKP learning standards are summarised below. The codes are curriculum references, not proof-rule IDs.

| DSKP standard | Official competency in substance | Recognition implications |
|---|---|---|
| 6.1.1 | Represent positive and negative angles in the Cartesian plane | Recognise signed angles, clockwise/anticlockwise rotation, quadrant, coterminal angles, angles beyond one revolution, degree/radian notation. |
| 6.2.1 | Relate secant, cosecant and cotangent to sine, cosine and tangent for any angle | Recognise all six elementary functions, reciprocal/quotient structure, cofunction relations and denominator restrictions. |
| 6.2.2 | Determine trigonometric ratios for any angle | Recognise reference-angle evaluation, quadrant signs, special angles and exact-value questions. |
| 6.3.1 | Draw/sketch `y = a sin bx + c`, `y = a cos bx + c`, and `y = a tan bx + c`, where `a,b,c` are constants and `b > 0` | Recognise amplitude, period, vertical translation, reflection, tangent asymptotes, and transformed graphs. |
| 6.3.2 | Solve trigonometric equations using the graphical method | Recognise equations as graph intersections, including cases where the second graph is **not a constant**; recognise solution-count questions. |
| 6.4.1 | Derive the basic identities using a right-angled triangle or unit circle | Recognise requests to derive foundational identities; route to an independent geometric foundation, not to the identity being derived. |
| 6.4.2 | Prove trigonometric identities using basic identities | Recognise identity-proof tasks whose natural route uses Pythagorean, quotient, or reciprocal relations. |
| 6.5.1 | Prove identities using addition formulae for `sin(A ± B)`, `cos(A ± B)`, and `tan(A ± B)` | Recognise compound-angle expansions and disguised `A+B` / `A−B` structures. |
| 6.5.2 | Derive double-angle formulae for `sin 2A`, `cos 2A`, and `tan 2A`; half-angle formulae are to be discussed | Recognise double-angle derivations and half-angle consequences. |
| 6.5.3 | Prove identities using double-angle formulae | Recognise expressions with `2A`, squares, products `sin A cos A`, and half-angle arguments. |
| 6.6.1 | Solve trigonometric equations | Recognise equations with specified intervals, exact/general solutions, periodic branches, and restrictions. |
| 6.6.2 | Solve problems involving trigonometric functions | Recognise multi-part, contextual, graphical, and mixed-representation applications. |

### A1.1 Curriculum notes that materially affect recognition

The DSKP notes require or emphasise the following:

1. Angles greater than `360°` or `2π` radians are to be involved throughout the topic.
2. Quadrant positions and degree/radian relationships in terms of `π` are emphasised.
3. Cofunction relationships include all six pairings:
   - `sin θ = cos(90° − θ)`
   - `cos θ = sin(90° − θ)`
   - `tan θ = cot(90° − θ)`
   - `csc θ = sec(90° − θ)`
   - `sec θ = csc(90° − θ)`
   - `cot θ = tan(90° − θ)`
4. Exact ratios for `30°`, `45°`, and `60°` are supported by right-triangle reasoning.
5. The transformed graphs use constants `a`, `b`, and `c`, with `b > 0` in the stated standard form.
6. Absolute-value trigonometric functions are included in graph work.
7. Graphical equation questions must include non-constant `y` expressions, not only horizontal lines `y = k`.
8. Sketches are used to determine the number of solutions.
9. The three basic identities are to be explored through a right-angled triangle or unit circle.
10. Half-angle formulae are to be discussed with double-angle formulae.

These notes mean that a recogniser limited to `sin x = k`, `cos x = k`, and `tan x = k` is not adequate for the Malaysian Form 5 scope.

### A1.2 Core curriculum versus supporting extensions

To avoid overstating what the syllabus explicitly prescribes, classify recognition knowledge into three bands:

| Band | Meaning | Examples in this file |
|---|---|---|
| **KSSM core** | Directly named in Topic 6.0 or its notes | Positive/negative and multi-turn angles; quadrants; six ratios; cofunctions; special-angle ratios; transformed sine/cosine/tangent graphs; absolute-value trig graphs; graphical equations with non-constant right sides; basic identities; compound-angle formulas; double-angle formulas; half-angle discussion; equation solving and applications. |
| **Supporting methods** | Algebraic techniques naturally needed to solve or prove core questions, but not separately listed as a learning standard | Factoring; polynomial substitutions in sine/cosine/tangent; rational expressions; conjugates; domain-aware cancellation; branch splitting; amplitude-phase rewriting; interval enumeration; exact-value simplification. |
| **Extension recognition** | Useful wider mathematics, not to be labelled as an explicit Form 5 requirement | Triple-angle and arbitrary higher-angle polynomial methods; tangent half-angle rational parameterisation; product-to-sum as a general method; systems of trig equations; nested trig functions; advanced root isolation. |

A future engine may recognise all three bands. Its report should identify the band so that a user can distinguish syllabus-aligned knowledge from a supplementary route.

## A2. Cognitive extent: Performance Levels TP1–TP6

The DSKP gives six performance levels for Trigonometric Functions. The descriptors move from basic knowledge and understanding to simple tasks, simple routine problems, complex routine problems, and non-routine problems solved creatively.

The following is an **engineering interpretation** of those descriptors for problem recognition. It is not a claim that KPM assigns each example below to a fixed TP level.

| Level | DSKP cognitive description | Recognition behaviour expected |
|---|---|---|
| TP1 | Demonstrate basic knowledge of trigonometric functions | Identify function names, symbols, angle units, quadrants, periods, and basic graph/identity forms. |
| TP2 | Demonstrate understanding | Explain equivalent notation, reciprocal/quotient relationships, reference angles, signs, periodicity, and the difference between an identity and an equation. |
| TP3 | Apply understanding to simple tasks | Recognise and route direct equations such as `sin x = 1/2`, `cos 2x = 0`, or `tan(x−30°) = 1`. |
| TP4 | Apply appropriate knowledge and skills to simple routine problems | Identify one or two transformations, a specified interval, an elementary proof followed by a solve step, or a straightforward graph intersection. |
| TP5 | Apply appropriate knowledge and skills to complex routine problems | Identify multi-stage expressions involving reciprocal functions, compound/double angles, rationalisation, absolute values, multiple branches, transformed graphs, and non-constant right-hand sides. |
| TP6 | Apply appropriate knowledge and skills to non-routine problems creatively | Detect unfamiliar disguises, choose among algebraic/geometric/graphical routes, combine representations, handle parameters or unusual intervals, and explain why a standard method is insufficient. |

### A2.1 Cognitive complexity is not the same as expression length

A short equation can be cognitively difficult if it hides a domain issue or a branch loss. A long expression can be routine if it reduces immediately to one known identity.

For recognition, estimate complexity from the mathematical decisions required:

- number of distinct trig functions;
- number of distinct angle arguments;
- whether arguments are affine, compound, nested, or non-linear;
- power and product structure;
- reciprocal/rational structure;
- absolute values or radicals;
- interval width and number of periods;
- need to split cases or preserve excluded points;
- presence of a non-constant right-hand side;
- graph intersection or parameter-count requirements;
- number of different proof families likely to be combined;
- whether the problem supplies a prior result using “hence”.

A future engine may assign an estimated cognitive band, but it must label it as a heuristic estimate, not as an official KPM grade or a prediction of marks.

## A3. What Malaysian SPM-style tasks demonstrate

A review of publicly re-typeset SPM Add Maths questions illustrates recurring combinations of proof, equation solving, and graph interpretation. These examples are evidence of **question structures**, not a statistical claim about how often each structure appears in all examination papers. The cited question pages are secondary learning resources and state that they are not affiliated with Lembaga Peperiksaan Malaysia.

| Year / paper example | Observed structure | Recognition lesson |
|---|---|---|
| SPM 2017 Paper 2 Q10 | Prove `2 tan θ cos² θ = sin 2θ`; hence solve a related equation on `0 ≤ θ ≤ 2π`; then use the graph of `sin 2θ` with a straight-line relation to count solutions | A proof can be a prerequisite for an equation; argument scaling doubles the interval; the final task may be an intersection count rather than an exact root list. |
| SPM 2019 Paper 2 Q10 | Prove a half-angle identity for `tan(A/2)`; obtain an exact value; then use a transformed expression involving `cot(A/2)` and a variable-dependent right-hand side in a graph question | Half-angle recognition, exact special-angle evaluation, and non-constant graph intersections can appear in one question. |
| SPM 2020 Paper 2 Q10 | Prove a rational expression involving `cos 2x`, `sin 2x`, and `sin x` equals `2 tan x`; sketch the reduced function; solve an equation against `cot(x/2)` | A complicated rational equation may conceal a simple function; graphing must retain the original domain and compare two non-identical functions. |
| SPM 2021 Paper 2 Q5 | Prove `2 cot² A sin² A = 1 + cos 2A`; hence solve a related equation on `0 ≤ A ≤ 2π`; sketch an absolute-value cosine graph | Reciprocal functions, cancellation, double-angle identities, interval enumeration, and absolute-value graphs are combined. |
| SPM 2022 Paper 2 Q6 | Prove `cot(x/2) − tan(x/2) = 2 cot x`; sketch an absolute-value graph; determine parameter values for which a horizontal line has no intersection | Half-angle expressions can simplify to a full-angle function; parameter-range questions require extrema, range, and asymptote analysis. |
| SPM 2023 Paper 2 Q4 | Read constants from a transformed tangent graph; solve `2 cos x = −1` on an interval spanning more than one revolution; use a graph to find an inequality interval | Graph parameters, quadrant selection, repeated periods, and inequalities must be recognised together. |
| SPM 2024 Paper 2 Q8 | Prove a double-angle identity; hence solve an equation involving `cos² θ` and `sin² θ` on `180° ≤ θ ≤ 360°`; analyse an absolute-value double-angle graph and a horizontal parameter | The engine must recognise an equation hidden in equal squares, double-angle conversion, a non-standard interval, and parameterised graph intersections. |
| SPM 2024 Paper 1 Q8 | Given a sine ratio and a compound-angle difference with acute-angle conditions, express another ratio in a parameter | Conditional angle information and sign selection affect the correct square-root branch. |

### A3.1 Implications from these question structures

A useful recogniser must detect at least these recurring pipelines:

1. **Prove → hence solve:** establish a formula, then substitute it into a separate equation.
2. **Prove → exact value:** use a derived half-angle or compound-angle relation to evaluate a special angle without a calculator.
3. **Prove → graph:** simplify a complicated expression before sketching its function.
4. **Graph → intersection count:** solve `f(x)=g(x)` by counting crossings over a stated interval.
5. **Absolute-value graph → parameter range:** fold a graph and analyse horizontal levels.
6. **Equation → interval filtering:** find all periodic branches first, then retain only those in the specified range.
7. **Conditional angle → sign choice:** use acute/obtuse/quadrant conditions to select the correct sign of a radical.

The recogniser must not classify a whole multi-part question as only an identity proof because part (a) begins with “Prove”. It should build a task tree for each subpart and link the dependencies between them.

---

# PART B — INPUT NORMALISATION AND STRUCTURAL PARSING

## B1. Supported function vocabulary and aliases

The engine should recognise the following forms as equivalent function names where context makes the meaning unambiguous.

| Canonical function | Common English / symbolic forms | Malaysian / textbook forms |
|---|---|---|
| `sin` | `sin`, `sine`, `\sin` | sinus |
| `cos` | `cos`, `cosine`, `\cos` | kos, kosinus |
| `tan` | `tan`, `tangent`, `\tan` | tangen |
| `cot` | `cot`, `cotan`, `cotangent`, `\cot` | kot, kotangen |
| `sec` | `sec`, `secant`, `\sec` | sek, sekan |
| `csc` | `csc`, `cosec`, `cosecant`, `\csc` | kosek, kosekan |

Additional notation to normalise:

- `sin² x`, `sin^2 x`, `(sin x)^2` → `(sin(x))^2`.
- `sin 2x`, `sin(2x)` → `sin(2*x)`; this is **not** `(sin(x))^2`.
- `cos 2A`, `cos(2A)` → `cos(2*A)`.
- `2sin x`, `2 sin x` → `2*sin(x)`.
- `π`, `pi` → the same exact constant.
- `θ`, `theta`, `A`, `B`, `x`, `t` are variable symbols, not fixed numerical values unless explicitly assigned.
- `°`, `deg`, `degrees` identify degree measure.
- `rad`, `radian`, or a context such as an interval containing `π` identifies radian measure.
- `≡` and the wording “identity” usually indicate universal equality; `=` alone does not determine whether a statement is an identity or an equation.

### B1.1 Important ambiguity: inverse versus reciprocal

The notation `sin⁻¹ x` is commonly used for inverse sine, whereas `csc x` means reciprocal sine. The parser must not silently interpret `sin^-1(x)` as `1/sin(x)` or as `csc(x)`.

If inverse trigonometric functions (`arcsin`, `arccos`, `arctan`, or `sin^{-1}` in inverse-function context) occur, classify them as an **extension/out-of-core expression** unless the active engine explicitly enables an inverse-trigonometric module. Preserve the distinction between reciprocal powers and inverse functions.

## B2. Syntax-tree features

The recogniser should parse both sides into expression trees and record these features before selecting a route.

| Feature | Examples | Why it matters |
|---|---|---|
| `trig_functions` | `{sin, cos, tan}` | Determines function families present. |
| `argument_set` | `{x, 2x, x/2, 2x−30°}` | Detects shared angles, multiple angles, half angles and compound angles. |
| `argument_shape` | constant, affine, polynomial, rational, nested | Determines whether a standard solution family can be inverted directly. |
| `power_set` | powers 1, 2, 3, 4 | Detects polynomial substitutions and power reduction. |
| `product_nodes` | `sin x cos x`, `tan x sec x` | Detects double-angle or factorisation patterns. |
| `sum_difference_nodes` | `sin A ± sin B`, `cos A ± cos B` | Detects compound-angle or product-sum patterns. |
| `quotient_nodes` | `sin x/cos x`, `(1−cos x)/sin x` | Detects quotient definitions, rationalisation and domain restrictions. |
| `denominator_set` | `cos x`, `1−cos x`, `tan x+1` | Creates permanent exclusion conditions. |
| `absolute_value_nodes` | `|cos 2x|`, `|cot(x/2)−2cot x|` | Triggers branch splitting or graph folding. |
| `radical_nodes` | `sqrt(1−cos²x)` | Triggers radicand and principal-root sign checks. |
| `parameter_symbols` | `a,b,c,m,k,p` | Detects parameterised families and range questions. |
| `interval` | `0≤x≤2π`, `−π≤x≤π` | Controls branch enumeration and endpoint inclusion. |
| `unit` | degrees, radians, unknown | Controls period and conversion rules. |
| `rhs_variable_dependence` | `sin x = x/π`, `tan x = cos x` | Detects non-constant graph intersections. |
| `task_verbs` | prove, solve, sketch, hence, determine | Distinguishes the requested mathematical operation. |

### B2.1 Canonical expression normalisation

Normalisation may reorder commutative sums/products, standardise aliases, and make implicit multiplication explicit. It must not:

- change `sin(2x)` into `sin²(x)`;
- remove parentheses that alter function arguments;
- cancel a factor before recording its zero set;
- discard a denominator restriction;
- replace a principal square root with a signed root;
- treat `|f(x)|` as `f(x)`;
- change degrees into radians without exact conversion;
- treat a displayed approximate decimal as an exact angle;
- rename variables in a way that causes variable capture.

## B3. Language and instruction cues

The recogniser should support English and common Malaysian Bahasa Melayu task language.

| English cue | BM cue | Likely task type |
|---|---|---|
| Prove / Show that / Verify the identity | Buktikan / Tunjukkan bahawa / Sahkan identiti | Identity proof or derivation. |
| Hence solve | Seterusnya selesaikan / Maka selesaikan | Dependent equation-solving task. |
| Solve / Find all values | Selesaikan / Cari semua nilai | Equation solving. |
| For `a ≤ x ≤ b` | Bagi julat `a ≤ x ≤ b` | Interval-restricted solution set. |
| Sketch / Draw the graph | Lakarkan / Lukiskan graf | Graph construction. |
| Number of solutions | Bilangan penyelesaian | Intersection/root counting. |
| State the range of `m` | Nyatakan julat nilai `m` | Parameter/range analysis. |
| Without calculator / table | Tanpa kalkulator / jadual | Exact-value route preferred. |
| In terms of `π` | Dalam sebutan `π` | Exact radian answer. |
| Acute angles | Sudut tirus | Sign branch / positive cosine and sine conditions. |
| Obtuse angles | Sudut cakah | Sign branch. |
| Positive / negative angle | Sudut positif / negatif | Rotation orientation. |
| Reference angle | Sudut rujukan | Quadrant reduction. |
| Absolute value | Nilai mutlak | Branch splitting / graph reflection. |
| Asymptote | Asimptot | Tangent, cotangent, secant, cosecant or rational graph. |

The wording “show that” is not enough to infer a proof of an identity. Inspect the variables, quantifiers, domain, and question context.

---

# PART C — TASK-TYPE RECOGNITION

## C1. Distinguish the mathematical task before solving

The same equation-shaped text can play different roles. The engine must classify the task from both syntax and instructions.

| Class ID | Task class | Recognition condition | Expected output |
|---|---|---|---|
| `TASK.IDENTITY_PROOF` | Identity proof | Universal variables or explicit identity/prove instruction | Proof obligation over the original common domain. |
| `TASK.FORMULA_DERIVATION` | Formula derivation | “Derive”, “show formula”, “deduce” a relation | Derivation from declared independent foundations. |
| `TASK.EQUATION_SOLVE` | Trigonometric equation | Unknown variable with equality and solve/find-values instruction | Complete solution set, exact or approximate as requested. |
| `TASK.GRAPH_SKETCH` | Graph sketch | Sketch/draw `y=f(x)` or graph of trig function | Graph features, key points, discontinuities and interval. |
| `TASK.GRAPH_INTERSECTION` | Graphical equation | `f(x)=g(x)` or “draw suitable graph/line” | Intersection points or number of intersections on interval. |
| `TASK.PARAMETER_RANGE` | Parameter range | “Find range of m/k/a such that…” | Parameter intervals based on range/extrema/intersection count. |
| `TASK.INEQUALITY` | Trigonometric inequality | `<`, `≤`, `>`, `≥`, “range of x” | Interval union with endpoint and domain analysis. |
| `TASK.CONDITIONAL` | Conditional trigonometric statement | Acute/obtuse/triangle/specified quadrant assumptions | Proof/solution under explicit assumptions. |
| `TASK.SYSTEM` | System of trigonometric equations | Two or more simultaneous equations | Joint solution set and shared-domain check. |
| `TASK.COUNTEREXAMPLE` | Test/refute claim | “Is this true?”, “disprove”, or universal claim fails | Valid counterexample or corrected statement. |
| `TASK.UNSUPPORTED_EXTENSION` | Out-of-core trig task | Inverse/hyperbolic/complex/nested unsupported functions | Recognise and explain the missing module; do not force a six-function proof. |

### C1.1 Identity versus equation

An identity is true for every allowed value in the original common domain. An equation asks for values that make equality true. A recogniser must not use a finite root list to prove an identity, and must not answer an equation by merely showing a general identity.

Examples:

- `sin²x + cos²x = 1` with “prove” is an identity-proof task.
- `sin²x + cos²x = 1` with “solve for `0≤x≤2π`” is an equation whose every point in the interval is a solution (subject to the interval convention).
- `sin x = 1/2` is an equation, not an identity.
- `sin x = sin x` is an identity on all real `x`.
- `tan x = sin x/cos x` is a definitional equality only where `cos x ≠ 0`.

## C2. Multi-part and dependent task trees

Recognise question structures such as:

```text
Part (a): Prove identity I.
Part (b): Hence solve equation E on interval J.
Part (c): Sketch graph G and determine the number/range of solutions.
```

Represent them as separate nodes:

- proof node `I`;
- equation node `E`, optionally depending on `I`;
- graph node `G`;
- intersection/parameter node depending on `G`.

The “hence” link permits use of the earlier result only after that result has been proved or independently admitted. It does not authorise assuming the target equation as a theorem.

A proof subpart and a solve subpart may use different methods. For example, part (a) may be a symbolic identity proof, part (b) may be exact branch enumeration, and part (c) may be graphical counting.

---

# PART D — EQUATION RECOGNITION TAXONOMY

The following catalogue is a **pattern recogniser**, not a list of automatically valid transformations. Each pattern supplies a signature, likely route, and required safeguards.

## D1. Single-function equations

### `EQREC-001` — Sine equals a constant

**Signature:** `sin(u(x)) = k`.

Recognise:

- direct sine equations;
- affine argument `ax+b`;
- multiple-angle argument `nx`;
- shifted argument `ax+b°`;
- a constant parameter `k`;
- a stated interval in degrees or radians.

**Candidate route:** range check `−1≤k≤1`, choose a principal/reference angle `α`, generate both sine branches, solve the argument equations, and filter against the original interval.

For a real angle `u` in radians:

- `sin u = k`, `−1≤k≤1`;
- let `α` be the principal angle with `sin α=k` and `−π/2≤α≤π/2`;
- `u=α+2nπ` or `u=π−α+2nπ`, `n∈ℤ`.

In degrees replace `2π` by `360°` and `π` by `180°`.

**Edge cases:** `k=1` or `k=−1` can make the two families coincide; `k` outside `[-1,1]` gives no real solution. If `u(x)` is non-linear, do not assume it is one-to-one.

### `EQREC-002` — Cosine equals a constant

**Signature:** `cos(u(x)) = k`.

Range check `−1≤k≤1`. Let `α∈[0,π]` satisfy `cos α=k`. Then:

- `u=α+2nπ` or `u=−α+2nπ`.

In degrees use `α+360°n` and `−α+360°n`.

Check duplicate branches at `k=±1`. Use the stated quadrant/interval to retain valid values.

### `EQREC-003` — Tangent equals a constant

**Signature:** `tan(u(x)) = k`.

For real `k`, let `α` be the principal tangent angle in `(-π/2,π/2)`. Then:

- `u=α+nπ`, `n∈ℤ`.

In degrees the period is `180°`.

The original equation requires `cos(u)≠0`. The generated tangent family normally excludes poles, but the verifier must still retain the original-domain ledger.

### `EQREC-004` — Cotangent equals a constant

**Signature:** `cot(u(x)) = k`.

Use a fixed principal branch `α∈(0,π)` with `cot α=k`; then:

- `u=α+nπ`, `n∈ℤ`.

The original equation requires `sin(u)≠0`. Define the arccot branch explicitly; do not rely on a software library's undocumented convention.

### `EQREC-005` — Secant or cosecant equals a constant

**Signatures:** `sec(u)=k` or `csc(u)=k`.

Reduce by reciprocal definitions, retaining domain conditions:

- `sec u=k` requires `k≠0` and `cos u=1/k`; real solutions require `|k|≥1`.
- `csc u=k` requires `k≠0` and `sin u=1/k`; real solutions require `|k|≥1`.

Do not treat `sec u=0` or `csc u=0` as solvable. Neither secant nor cosecant can equal zero on its domain.

### `EQREC-006` — Affine and scaled arguments

**Signature:** any of `sin(ax+b)=k`, `cos(ax+b)=k`, `tan(ax+b)=k`, or reciprocal-function variants.

First solve in the angle variable `u=ax+b`. If `a≠0`, map each branch back to `x`. If `a=0`, the equation is constant and must be evaluated separately. For `a<0`, branch ordering and interval endpoints need care.

When an interval is specified, enumerate integer branch indices exactly:

- for a family `x=p+nq`, `q>0`, determine integer `n` satisfying the interval bounds;
- preserve open/closed endpoints;
- avoid floating-point decisions for exact multiples of `π` or `180°`.

## D2. Equality between trigonometric functions

### `EQREC-007` — Sine equals sine

**Signature:** `sin(u)=sin(v)`.

Recognise two complete branches:

- `u=v+2nπ`;
- `u=π−v+2nπ`.

These are equations in the underlying variable(s). If `u` and `v` are expressions in `x`, solve both branch equations and verify the original statement.

### `EQREC-008` — Cosine equals cosine

**Signature:** `cos(u)=cos(v)`.

Branches:

- `u=v+2nπ`;
- `u=−v+2nπ`.

### `EQREC-009` — Tangent equals tangent

**Signature:** `tan(u)=tan(v)`.

Candidate branch:

- `u=v+nπ`.

Both original tangent expressions must be defined. This equivalence must not erase pole restrictions.

### `EQREC-010` — Cotangent equals cotangent

**Signature:** `cot(u)=cot(v)`.

Candidate branch:

- `u=v+nπ`.

Both original cotangent expressions must be defined.

### `EQREC-011` — Sine/cosine cofunction equality

**Signatures:** `sin(u)=cos(v)`, `cos(u)=sin(v)`, `tan(u)=cot(v)`, `sec(u)=csc(v)`, `csc(u)=sec(v)`.

Use a quarter-turn relation to convert to a same-function equation, then apply the relevant periodic branch. Keep all denominator restrictions for reciprocal functions.

Example recognition:

`sin x = cos 2x` is not a direct “sine equals constant” problem. Convert `cos 2x` to `sin(π/2−2x)` and solve the two sine-equality branches.

## D3. Linear combinations and phase forms

### `EQREC-012` — Linear sine/cosine combination

**Signature:** `a sin(u)+b cos(u)=c`.

Recognise the amplitude-phase pattern:

`a sin u+b cos u = R sin(u+φ)`,

where `R=√(a²+b²)`, `cos φ=a/R`, and `sin φ=b/R`, when `R>0`.

Range test: `|c|≤R` is necessary for real solutions. If `R=0`, handle the constant equation separately. Generate the complete sine solution family after phase reduction.

Also recognise equivalent forms:

- `a cos u+b sin u=c`;
- `R sin(u+φ)=c`;
- `R cos(u−δ)=c`;
- `a sin u−b cos u=c`.

Do not infer a unique phase from `tan φ=b/a` alone without quadrant information.

### `EQREC-013` — Linear combination equals another trigonometric function

**Signature:** `a sin u+b cos u = f(x)` where the right side is not constant.

Do not apply the constant amplitude range test as if `f(x)` were fixed. Recognise a graph-intersection problem or an algebraic system depending on the form.

### `EQREC-014` — Sine/cosine shifted phase

**Signature:** `sin(u+φ)=k`, `cos(u−φ)=k`, or `R sin(u+φ)=g(x)`.

Detect phase shift before root enumeration. Keep the angle unit and periodicity explicit.

## D4. Polynomial and algebraic trigonometric equations

### `EQREC-015` — Polynomial in one trig function

**Signature:** `P(sin u)=0`, `P(cos u)=0`, `P(tan u)=0`, or the reciprocal-function analogue.

Route:

1. Introduce a temporary algebraic variable, such as `s=sin u`.
2. Solve `P(s)=0` exactly where possible.
3. Enforce the range: `−1≤s≤1` for sine/cosine; all real values for tangent, subject to its angle-domain poles.
4. Reject algebraic roots outside the trig range.
5. Convert each retained value into complete angle branches.
6. Apply the original interval and domain.

Do not treat an algebraic root as an angle solution before range checking.

### `EQREC-016` — Quadratic in sine/cosine

**Signature examples:**

- `a sin²x+b sin x+c=0`;
- `a cos²x+b cos x+c=0`;
- `a sin²x+b cos²x=c`;
- `a sin²x+b sin x cos x+c cos²x=d`.

Detect whether the equation is a polynomial in one function, a homogeneous quadratic, or a combination reducible by `sin²x+cos²x=1`. Candidate methods include substitution, factoring, circle identity, double-angle conversion, or amplitude-phase reduction.

### `EQREC-017` — Equal squares / opposite signs

**Signatures:** `sin²u=cos²v`, `sin²u=sin²v`, `cos²u=cos²v`, or `f²=g²`.

Recognise that `f²=g²` gives **both** `f=g` and `f=−g`. Do not take only the positive square-root branch.

Useful identities include:

- `sin²x=cos²x` ⇔ `cos 2x=0`;
- `sin²x=(1−cos 2x)/2`;
- `cos²x=(1+cos 2x)/2`.

### `EQREC-018` — Product of sine and cosine

**Signature:** `sin u cos u`, `2 sin u cos u`, or powers/products containing both.

Recognise `2 sin u cos u=sin 2u`. Also detect factorisation opportunities such as:

- `sin x(2 cos x−1)=0`;
- `cos x(2 sin x−1)=0`;
- `sin x cos x = 0`.

When solving a product equation, keep every zero-factor branch. Dividing by one factor before checking its zero case is a prohibited shortcut.

### `EQREC-019` — Difference or sum of squares

**Signature examples:** `cos²x−sin²x`, `1−2sin²x`, `2cos²x−1`.

Recognise each as a possible representation of `cos 2x`. Select the representation that best fits the remaining expression, but do not alter the equation's domain or sign.

### `EQREC-020` — Polynomial in `tan x` / `cot x`

**Signature:** a polynomial or rational equation in `tan u` or `cot u`.

Substitute `t=tan u` or `q=cot u`, solve the algebraic equation, and map values back to angle families. Preserve the tangent/cotangent poles and check all roots in the original equation.

### `EQREC-021` — Mixed sine and cosine rationalisation

**Signature:** rational expressions containing both `sin x` and `cos x`, often with powers or linear factors.

Candidate routes:

- quotient conversion to tangent where cosine is nonzero;
- divide numerator and denominator by a common power only if the divisor is nonzero;
- use `sin²+cos²=1`;
- factor a common `sin x`, `cos x`, `1±sin x`, or `1±cos x` factor;
- use a double-angle identity;
- use a half-angle substitution if the equation's structure supports it.

Every division creates a branch obligation or a justified nonzero condition.

## D5. Multiple-angle and compound-angle equations

### `EQREC-022` — Double-angle equation

**Signature:** `sin 2u`, `cos 2u`, `tan 2u`, or a mixture of `u` and `2u`.

Recognise the three double-angle formula families:

- `sin 2u=2 sin u cos u`;
- `cos 2u=cos²u−sin²u=1−2sin²u=2cos²u−1`;
- `tan 2u=2tan u/(1−tan²u)` on its exact domain.

When solving an equation in `2u`, double the interval before finding branches, then divide the resulting angle values by two. Do not solve only over the original interval by mistake.

### `EQREC-023` — Compound-angle equation

**Signature:** `sin(A±B)`, `cos(A±B)`, `tan(A±B)`.

Recognise the addition formulae and determine whether `A` and `B` are constants, the same variable, affine functions, or independent variables.

- `sin(A+B)=sin A cos B+cos A sin B`;
- `sin(A−B)=sin A cos B−cos A sin B`;
- `cos(A+B)=cos A cos B−sin A sin B`;
- `cos(A−B)=cos A cos B+sin A sin B`;
- `tan(A+B)=(tan A+tan B)/(1−tan A tan B)` with all component and result domains checked;
- `tan(A−B)=(tan A−tan B)/(1+tan A tan B)` with all component and result domains checked.

If `A` or `B` contains a parameter or a non-linear function of `x`, retain it symbolically and solve the resulting branch equation; do not assume the angles are independent.

### `EQREC-024` — Triple-angle and higher multiple-angle equation

**Signature:** `sin 3x`, `cos 3x`, `tan 3x`, or `sin(nx)` / `cos(nx)` with integer `n`.

The triple-angle formulas are useful extension patterns:

- `sin 3x=3sin x−4sin³x`;
- `cos 3x=4cos³x−3cos x`;
- `tan 3x=(3tan x−tan³x)/(1−3tan²x)` on the required domain.

For integer `n`, recognise recurrence or Chebyshev-polynomial structures as optional advanced methods. Do not label these as an explicit Form 5 requirement merely because the general multiple-angle pattern is recognised.

### `EQREC-025` — Half-angle equation

**Signature:** `sin(x/2)`, `cos(x/2)`, `tan(x/2)`, `cot(x/2)`, or equations involving `1±cos x` and `sin x`.

Recognise:

- `sin²(x/2)=(1−cos x)/2`;
- `cos²(x/2)=(1+cos x)/2`;
- `tan(x/2)=sin x/(1+cos x)=(1−cos x)/sin x`, with the exact domain of each form;
- `cot(x/2)=sin x/(1−cos x)=(1+cos x)/sin x`, with the exact domain of each form.

The square-root versions are absolute values:

- `√((1−cos x)/2)=|sin(x/2)|`;
- `√((1+cos x)/2)=|cos(x/2)|`.

Do not silently remove the absolute value.

### `EQREC-026` — Special-angle compound equations

**Signature:** fixed angles such as `15°`, `30°`, `45°`, `60°`, `75°`, `105°`, `135°`, `150°`, or expressions like `x±45°`.

Recognise decomposition into sums/differences of special angles. Prefer exact radicals when the prompt says “without calculator”, “exact value”, or “in surd form”. Use quadrant signs for non-acute angles.

## D6. Rational, reciprocal, radical and absolute-value equations

### `EQREC-027` — Rational trigonometric equation

**Signature:** `F(x)/G(x)=k`, `F(x)/G(x)=H(x)/J(x)`, or a sum of trig fractions.

Before cross-multiplication, record:

- `G(x)≠0`;
- `J(x)≠0`;
- all internal `tan`, `cot`, `sec`, and `csc` restrictions;
- any additional denominator introduced by a rewrite.

If the equation is a fraction equal to zero, it is equivalent to numerator zero only on the original domain where the denominator is nonzero. A cancelled factor can create a hole; that point remains excluded even if the simplified expression has a finite value there.

### `EQREC-028` — Reciprocal-pair equation

**Signature examples:**

- `sec x±tan x`;
- `csc x±cot x`;
- `1/(sec x−tan x)`;
- `1/(1±cos x)`;
- `1/(1±sin x)`;
- `tan x+cot x`;
- `sec²x+csc²x`.

Recognise conjugate pairs and rationalisations:

- `(sec x−tan x)(sec x+tan x)=1`;
- `(csc x−cot x)(csc x+cot x)=1`;
- `tan x+cot x=1/(sin x cos x)=2csc 2x`, where all factors are defined.

Do not cancel a reciprocal pair unless the original domain permits it.

### `EQREC-029` — Equation containing `1±cos x` or `1±sin x`

**Signature:** a numerator/denominator or factor `1−cos x`, `1+cos x`, `1−sin x`, `1+sin x`.

Candidate half-angle routes:

- `1−cos x=2sin²(x/2)`;
- `1+cos x=2cos²(x/2)`;
- `sin x=2sin(x/2)cos(x/2)`.

Check zero sets before cancellation. These factors vanish at specific periodic points and can remove all or part of a solution family if mishandled.

### `EQREC-030` — Absolute-value equation

**Signatures:** `|f(x)|=k`, `|f(x)|=g(x)`, `|f(x)|+c=k`, or `|a sin bx+c|` in a graph.

Rules:

- `|f|=k` requires `k≥0` and splits into `f=k` or `f=−k`;
- `|f|=g` requires `g≥0` and splits into `f=g` or `f=−g`;
- `|f|≤k` requires `k≥0` and is equivalent to `−k≤f≤k`;
- `|f|≥k` for `k≥0` is equivalent to `f≤−k` or `f≥k`.

For graph recognition, the negative portions of `y=f(x)` are reflected above the x-axis. Preserve the order of operations: `|f(x)+c|` is not generally the same as `|f(x)|+c`.

### `EQREC-031` — Radical trigonometric equation

**Signature:** `sqrt(f(x))=g(x)`, `sqrt(sin²x)`, or radicals containing `1±cos x`.

For `√f=g`, require `f≥0` and `g≥0`, then solve `f=g²` under these conditions. Squaring is not automatically reversible without the nonnegative condition on the right side.

For example:

`√(1−cos²x)=sin x`

reduces to `|sin x|=sin x`, hence `sin x≥0`, not to all real `x`.

### `EQREC-032` — Trigonometric equation after a cancellation

**Signature:** an equation where the same trig factor occurs in every term or in numerator and denominator.

The recogniser must inspect the zero set of the proposed cancellation factor. If the original equation is defined when that factor is zero, split into:

1. factor equals zero;
2. factor is nonzero, so cancellation is valid.

If the original expression is undefined at the factor's zero, record that exclusion instead.

### `EQREC-033` — Equation using tangent half-angle substitution

**Signature:** rational expression in `sin x`, `cos x` that may simplify under `t=tan(x/2)`.

Use the rational parameterisation:

- `sin x=2t/(1+t²)`;
- `cos x=(1−t²)/(1+t²)`;
- `tan x=2t/(1−t²)` where defined.

**Mandatory missing-point check:** the chart `t=tan(x/2)` omits `x=(2n+1)π` (or `180°+360°n`). Test these points directly in the original equation. Never claim completeness from the finite `t` chart alone.

This is an optional algebraic route, not the default for every equation.

## D7. Graph and intersection equation families

### `EQREC-034` — Basic transformed sine graph

**Signature:** `y=a sin(bx)+c`, `b>0` in the DSKP form.

Recognise and report:

- amplitude `|a|` when `a≠0`;
- period `2π/b` radians or `360°/b` degrees;
- midline `y=c`;
- range `[c−|a|, c+|a|]`;
- reflection when `a<0`;
- vertical translation by `c`;
- zeros from `a sin(bx)+c=0` only when the level lies in the range.

If `a=0`, the graph is the constant `y=c`, not a sinusoid with nonzero amplitude.

### `EQREC-035` — Basic transformed cosine graph

**Signature:** `y=a cos(bx)+c`.

Use the same amplitude, period, midline, range and reflection rules as sine. The phase/key-point placement differs: cosine begins at its maximum when `a>0` and `x=0`.

### `EQREC-036` — Basic transformed tangent graph

**Signature:** `y=a tan(bx)+c`.

Recognise:

- period `π/b` radians or `180°/b` degrees for `b>0`;
- vertical asymptotes at `bx=π/2+nπ`, i.e. `x=(π/2+nπ)/b`;
- vertical translation `c`;
- vertical scaling/reflection through `a`;
- no finite global maximum or minimum when `a≠0`;
- domain excludes all tangent poles.

Do not assign a sine/cosine amplitude to tangent.

### `EQREC-037` — Graph with absolute value

**Signatures:** `y=|a sin bx+c|`, `y=|a cos bx+c|`, `y=|a tan bx+c|`, `y=a|sin bx|+c`, or more complicated absolute-value trig expressions.

Recognise the exact placement of the absolute-value bars. Determine zeros/cusps, reflected branches, periodicity, range, and any pre-existing asymptotes. Do not assume `|a sin bx+c|` and `a|sin bx|+c` have the same graph.

### `EQREC-038` — Constant horizontal-line intersection

**Signature:** `f(x)=m` or graph of `y=f(x)` with `y=m`.

This is an intersection problem. The number of solutions is the number of valid intersections on the specified interval, counting a tangency as one distinct solution. Exclude points where the original function is undefined.

### `EQREC-039` — Non-constant graph intersection

**Signature:** `f(x)=g(x)` where both sides depend on `x`.

This is explicitly within the DSKP graphical-equation scope. Recognise examples such as:

- `sin x = x/π`;
- `−tan 2x = 3x/π`;
- `2cos x = sin(x/2)`;
- `|cos 2x| = 1−x/π`;
- a transformed trig expression equal to a linear or another trig graph.

A suitable graph pair may be obtained by rearranging to `y=f(x)` and `y=g(x)`. Do not force the right side to be a constant. If an algebraic exact solution is unavailable, a graph can establish a solution count only if the graph/interval argument is sufficiently controlled; a rough sketch alone is not a proof of exact coordinates.

### `EQREC-040` — Graph parameter range / no-solution levels

**Signature:** “There is no solution if `y=m` is drawn”; “find the range of `m` for which the equation has no solution”; or “there are exactly `r` intersections”.

Recognise parameter values as horizontal levels. Determine:

- global/local extrema;
- open range endpoints caused by asymptotes or excluded points;
- closed endpoints attained at interval endpoints;
- tangencies and repeated intersections;
- changes in intersection count at critical levels;
- whether the interval includes or excludes endpoints.

For a continuous graph on a closed interval, a no-intersection horizontal level lies strictly outside the attained range. Do not automatically apply this simple statement to discontinuous graphs, open intervals, or functions with holes; determine the actual range on each branch.

### `EQREC-041` — Count solutions without solving exact roots

**Signature:** “State the number of solutions”, “how many roots”, or “number of points of intersection”.

Route to interval partition and graph/intersection analysis. Count distinct `x` values, not algebraic multiplicities. A tangent contact is one solution. A root at an included endpoint counts once. An asymptote or undefined point is not a solution.

### `EQREC-042` — Graph inequality

**Signature:** `f(x)<g(x)`, `f(x)≤g(x)`, or wording asking for the range of `x` satisfying a trig inequality.

Recognise sign regions between intersection points. Include or exclude endpoints according to the inequality and original domain. A graph inequality is not the same task as counting roots.

## D8. Periodic, interval and quadrant recognition

### `EQREC-043` — Multi-revolution interval

**Signature:** interval wider than one basic period, e.g. `0≤x≤2π`, `−π≤x≤3π`, `0°≤x≤720°`.

Generate all integer branches before filtering. Never assume one solution per interval or reduce the interval modulo one period and forget the number of repeated copies.

### `EQREC-044` — Negative-angle interval

**Signature:** negative lower/upper bounds, e.g. `−π≤x≤π`.

Retain negative representatives as required. Coterminal reduction may help sign analysis but must not alter the requested answer interval.

### `EQREC-045` — Quadrant and reference-angle constraint

**Signature:** quadrant, acute/obtuse, positive/negative ratio, or angle between two cardinal angles.

Use quadrant signs:

| Quadrant | `sin` | `cos` | `tan` |
|---|---:|---:|---:|
| I | + | + | + |
| II | + | − | − |
| III | − | − | + |
| IV | − | + | − |

For a reference angle `α`:

- QI: `α`;
- QII: `π−α`;
- QIII: `π+α`;
- QIV: `2π−α`.

Use exact degree equivalents when the question is in degrees. For negative or multi-turn angles, first locate the coterminal position, then retain the original angle representation if needed.

### `EQREC-046` — Parameter in a trig equation

**Signature:** `a sin x=b`, `sin(kx)=m`, `cos x=p`, or equation with unknown parameter plus interval/count constraint.

Separate unknown angle variables from parameters. Determine parameter range using the trig function range, amplitude, discriminant, graph intersections, or branch consistency. Avoid treating a parameter as a free angle variable.

### `EQREC-047` — Conditional triangle-angle equation

**Signature:** `A+B+C=180°` or `π`, with `A,B,C` constrained to be triangle angles.

Recognise that triangle conditions supply additional domain and sum constraints. A tangent identity valid for a triangle may not have a converse without the angle constraints. Do not generalise a conditional triangle identity to arbitrary real angles.

## D9. Products, sums, systems and less common forms

### `EQREC-048` — Sum-to-product or product-to-sum equation

**Signatures:** `sin u±sin v`, `cos u±cos v`, `sin u sin v`, `cos u cos v`, `sin u cos v`.

Candidate formula families:

- `sin u+sin v=2 sin((u+v)/2) cos((u−v)/2)`;
- `sin u−sin v=2 cos((u+v)/2) sin((u−v)/2)`;
- `cos u+cos v=2 cos((u+v)/2) cos((u−v)/2)`;
- `cos u−cos v=−2 sin((u+v)/2) sin((u−v)/2)`.

Use product-to-sum in the reverse direction when it reduces the number of distinct arguments. Retain all zero-factor branches.

### `EQREC-049` — Product equation with several angle factors

**Signature:** `sin u sin v=0`, `(sin x−a)(cos x−b)=0`, or products of trig terms.

Split the product into factor equations and solve each branch. Deduplicate overlapping solutions and preserve the original domain.

### `EQREC-050` — Sum of reciprocal functions

**Signature examples:** `sec x+tan x`, `csc x+cot x`, `tan x+cot x`, `sec²x+csc²x`.

Look for conjugate identities, Pythagorean relations, and conversion to sine/cosine. Do not assume a reciprocal sum is monotone or has a single root.

### `EQREC-051` — Simultaneous trigonometric equations

**Signature:** two or more equations in one or more angle variables.

Recognise possible substitutions:

- `s=sin x`, `c=cos x`, with `s²+c²=1`;
- `t=tan x`, only on the `cos x≠0` chart;
- sum/difference variables for `x+y` and `x−y`;
- phase-amplitude form.

Solve the algebraic system, restore angle branches, enforce shared variables, and check every original equation and domain condition.

### `EQREC-052` — Nested or composite trigonometric function

**Signature:** `sin(cos x)`, `tan(sin x)`, `sin(tan x)`, or a trig function whose argument is another trig function.

Recognise the nested structure, but mark it as **beyond the standard Form 5 core** unless the specific task is supported by an enabled module. Do not flatten it using an invalid identity such as `sin(cos x)=...`.

### `EQREC-053` — Trigonometric equation with polynomial/rational `x`

**Signature:** `sin x = x`, `cos 2x = x/π−1`, `tan 2x + x = 0`, etc.

Recognise that standard inverse-angle families do not directly solve the full equation. Candidate route: graph intersection, numerical root isolation, monotonicity/interval analysis, or a special exact argument if one exists. Numerical roots are approximations and must be labelled as such; they do not by themselves prove that all roots have been found.

### `EQREC-054` — Equation whose sides become the same function after an identity

**Signature:** a complicated side contains a hidden double-angle, half-angle, quotient, or compound-angle expression; the other side is a simpler trig function.

Run a structural scan for shared subexpressions and formula fingerprints before attempting general equation solving. The simplified equation may be `sin 2x=k`, `tan 2x=tan x`, or a graph-ready equation. Simplification must be certificate-checked and domain-preserving.

### `EQREC-055` — Equation embedded in a proof prompt

**Signature:** “Prove that [identity], hence solve [equation]”, “using the result above”, or a multipart question with linked subparts.

Create a dependency graph between question parts. The earlier identity is a premise for the later equation only after the proof obligation is satisfied. The proof target cannot be used to prove itself.

---

# PART E — IDENTITY AND PROOF-PROMPT RECOGNITION

Although SKILL-2 is primarily an equation-recognition database, Form 5 problems often interleave identities and equations. The engine must recognise the proof method likely intended by the structure.

## E1. Fundamental-identity proof patterns

Recognise:

- `sin²x+cos²x`;
- `1+tan²x`, `1+cot²x`;
- reciprocal products such as `sin x csc x`;
- quotient definitions `tan x=sin x/cos x`, `cot x=cos x/sin x`;
- equivalent rearrangements such as `sec²x−tan²x=1`;
- mixed expressions reducible to one common denominator.

Method candidates: convert to sine/cosine, use a Pythagorean identity, factor, take a common denominator, or rationalise. Consult the matching theorem in `SKILL.md` if present, but still check its dependency status.

## E2. Compound-angle proof patterns

Recognise:

- `sin(A+B)`, `sin(A−B)`;
- `cos(A+B)`, `cos(A−B)`;
- `tan(A+B)`, `tan(A−B)`;
- differences such as `cos(x+45°)−cos(x−45°)`;
- sums such as `sin(A+B)−sin(A−B)`;
- expressions with fixed angles such as `15°`, `75°`, `105°`, `135°`.

The engine should match the angle structure, not just exact formula text. For example, `cos(45°+x)` and `cos(x+45°)` are the same argument under commutative addition, but `cos(45°−x)` is a different branch and must retain its sign.

## E3. Double-angle proof patterns

Recognise:

- `sin 2x` against `2sin x cos x`;
- `cos 2x` against `cos²x−sin²x`, `1−2sin²x`, or `2cos²x−1`;
- `tan 2x` against `2tan x/(1−tan²x)`;
- half-angle expressions that reduce to a double-angle expression;
- `cos 2x±1` in a denominator;
- `sin x cos x` products.

When the task says “derive”, do not simply quote the formula being derived. Route to the addition formula or independent geometric construction appropriate to the active foundation profile.

## E4. Rational and conjugate proof patterns

Recognise:

- `sec x±tan x` and `csc x±cot x` conjugate pairs;
- `1±sin x`, `1±cos x`;
- fractions with `cos 2x±1`;
- rational functions with numerator/denominator sharing a trig factor;
- reciprocal expressions that simplify after multiplication by a conjugate.

Candidate methods: common denominator, difference of squares, half-angle formula, quotient conversion, and exact factorisation. All cancellation must be guarded.

## E5. “Hence” proof-to-equation patterns

A proof identity can transform the equation but does not automatically solve it. After using the proven identity:

1. rewrite the equation;
2. record any additional domain conditions;
3. solve all periodic branches;
4. apply the specified interval;
5. check candidates in the original equation.

Examples of recognition patterns:

- `2 tan x cos²x` becomes `sin 2x`;
- `2 cot²x sin²x` becomes `1+cos 2x`;
- `cot(x/2)−tan(x/2)` becomes `2cot x`;
- a rational expression involving `cos 2x` and `sin 2x` becomes a simple tangent expression.

Do not assume the exact identity from the question is already proved simply because it is listed in a database.

---

# PART F — FORMULA FINGERPRINTS FOR RECOGNITION

This section provides compact algebraic fingerprints that may reveal an unfamiliar equation's structure. It supplements, but does not replace, the main formula catalogue in `SKILL.md`.

## F1. Three fundamental relations

- `sin²x+cos²x=1`.
- `1+tan²x=sec²x` where `cos x≠0`.
- `1+cot²x=csc²x` where `sin x≠0`.

Equivalent rearrangements should be recognised structurally, but their domains must remain attached.

## F2. Quotient and reciprocal fingerprints

- `tan x=sin x/cos x`;
- `cot x=cos x/sin x`;
- `sec x=1/cos x`;
- `csc x=1/sin x`;
- `tan x cot x=1` where both exist;
- `sec x−tan x = 1/(sec x+tan x)` where the expressions are defined;
- `csc x−cot x = 1/(csc x+cot x)` where the expressions are defined.

## F3. Double-angle fingerprints

- `sin 2x=2sin x cos x`;
- `cos 2x=cos²x−sin²x`;
- `cos 2x=1−2sin²x`;
- `cos 2x=2cos²x−1`;
- `tan 2x=2tan x/(1−tan²x)` under the exact original domain.

## F4. Half-angle fingerprints

- `sin²(x/2)=(1−cos x)/2`;
- `cos²(x/2)=(1+cos x)/2`;
- `tan(x/2)=sin x/(1+cos x)` when `1+cos x≠0`;
- `tan(x/2)=(1−cos x)/sin x` when `sin x≠0`;
- `cot(x/2)=sin x/(1−cos x)` when `1−cos x≠0`;
- `cot(x/2)=(1+cos x)/sin x` when `sin x≠0`.

The two rational forms for the same half-angle function need not have identical pointwise domains. A proof may use one form only where its denominator is nonzero.

## F5. Compound-angle fingerprints

- `sin(A+B)=sin A cos B+cos A sin B`;
- `sin(A−B)=sin A cos B−cos A sin B`;
- `cos(A+B)=cos A cos B−sin A sin B`;
- `cos(A−B)=cos A cos B+sin A sin B`;
- `tan(A+B)=(tan A+tan B)/(1−tan A tan B)` where defined;
- `tan(A−B)=(tan A−tan B)/(1+tan A tan B)` where defined.

## F6. Triple-angle fingerprints (extension)

- `sin 3x=3sin x−4sin³x`;
- `cos 3x=4cos³x−3cos x`;
- `tan 3x=(3tan x−tan³x)/(1−3tan²x)` where defined.

These may be recognised as extension identities. Do not assume they are an examinable Form 5 learning standard solely from the DSKP Topic 6 list.

## F7. Product/sum fingerprints (extension and support)

- `sin A+sin B=2sin((A+B)/2)cos((A−B)/2)`;
- `sin A−sin B=2cos((A+B)/2)sin((A−B)/2)`;
- `cos A+cos B=2cos((A+B)/2)cos((A−B)/2)`;
- `cos A−cos B=−2sin((A+B)/2)sin((A−B)/2)`;
- `2sin A cos B=sin(A+B)+sin(A−B)`;
- `2cos A cos B=cos(A+B)+cos(A−B)`;
- `2sin A sin B=cos(A−B)−cos(A+B)`.

Use only when it reduces the number of distinct arguments or exposes a factorisation.

---

# PART G — DOMAIN, BRANCH AND SOLUTION-SET SAFEGUARDS

## G1. Original domain ledger

The original domain is permanent and must be computed before transformations.

| Function/expression | Required condition |
|---|---|
| `sin x`, `cos x` | Defined for every real `x`. |
| `tan x`, `sec x`, `1/cos x` | `cos x≠0`. |
| `cot x`, `csc x`, `1/sin x` | `sin x≠0`. |
| `tan x·cot x` | `sin x≠0` and `cos x≠0`. |
| `1/tan x` or `1/cot x` | Both `sin x≠0` and `cos x≠0`. |
| `1−cos x` denominator | `cos x≠1`. |
| `1+cos x` denominator | `cos x≠−1`. |
| `1−sin x` denominator | `sin x≠1`. |
| `1+sin x` denominator | `sin x≠−1`. |
| `sqrt(f(x))` | `f(x)≥0`. |
| `sqrt(f(x))/g(x)` | `f(x)≥0` and `g(x)≠0`. |

For a compound expression, intersect every condition. A later simplification may make an expression appear defined at a point excluded by the original form; that point remains excluded.

## G2. Equivalence versus implication

Every transformation must be tagged as one of:

- **equivalence:** preserves the solution set under the recorded conditions;
- **forward implication:** every original solution is a candidate, but extra candidates may be introduced;
- **reverse implication:** every transformed solution gives an original solution only after extra conditions;
- **case split:** separates zero/nonzero, sign, or branch cases;
- **identity rewrite:** equality of expressions on a specified common domain.

Examples:

- Squaring both sides is generally only a forward implication until sign conditions are checked.
- Multiplying by an expression that may be zero requires a zero/nonzero case split if equivalence is claimed.
- Dividing by `sin x` requires `sin x≠0` or a separate `sin x=0` branch.
- Replacing `sqrt(sin²x)` by `sin x` is invalid without `sin x≥0`; the correct expression is `|sin x|`.
- Cross-multiplication requires all original denominators to be nonzero.

## G3. Solution-set contract

A complete equation solution must establish both:

1. **Necessity:** every original solution is included in the candidate set.
2. **Sufficiency:** every retained candidate satisfies the original equation and all original-domain restrictions.

The final report must state:

- exact solution families or a clearly labelled numerical approximation;
- integer branch parameters and their ranges;
- interval endpoint inclusion;
- excluded points and why they are excluded;
- duplicate branches removed;
- whether the solution set is finite, periodic, an interval union, or all points in a stated interval;
- whether completeness is proved, graphically established, or unresolved.

## G4. Periodicity and interval filtering

Use the fundamental periods:

| Function | Period in radians | Period in degrees |
|---|---:|---:|
| `sin x`, `cos x`, `sec x`, `csc x` | `2π` | `360°` |
| `tan x`, `cot x` | `π` | `180°` |

For `f(bx+c)`, the period is the base period divided by `|b|` when `b≠0`. For `|sin bx|` and `|cos bx|`, the period may halve to `π/|b|`; do not apply this to a vertically shifted expression without checking.

If the interval spans multiple periods, enumerate every branch. If it is negative or extends beyond one full turn, do not truncate it to a principal interval.

## G5. Exact versus numerical answers

If the task asks “in terms of `π`”, “exact value”, or “without calculator”, preserve exact multiples and surds. Use a numerical solver only as a discovery/approximation aid.

A decimal approximation is not a proof that no other roots exist. For graph-based root counts, a rigorous implementation should use certified interval methods, exact monotonicity/critical-point analysis, or an explicit exam-style graphical argument whose limits are disclosed.

---

# PART H — GRAPH RECOGNITION AND ANALYSIS

## H1. Transformations for sine and cosine

For `y=a sin(bx)+c` or `y=a cos(bx)+c` with `b>0`:

- amplitude: `|a|`;
- period: `2π/b` radians or `360°/b` degrees;
- midline: `y=c`;
- range: `[c−|a|, c+|a|]`;
- `a<0`: reflection across the midline;
- `c≠0`: vertical translation;
- `b`: horizontal compression/expansion.

For a general phase-shifted function `a sin(bx+d)+c`, the horizontal shift is `−d/b` when `b≠0`. This is a structural extension of the DSKP's standard form.

## H2. Transformations for tangent

For `y=a tan(bx)+c`:

- period: `π/b` radians or `180°/b` degrees for `b>0`;
- vertical asymptotes: `bx=π/2+nπ`;
- range: all real values when `a≠0`;
- `a<0`: reflection in the midline;
- `c`: vertical translation.

A tangent graph has no global maximum/minimum. Parameter-range reasoning must account for each branch and its asymptotes.

## H3. Absolute-value graphs

Recognise at least these distinct structures:

1. `y=|sin x|`;
2. `y=|cos x|`;
3. `y=|tan x|`;
4. `y=|a sin bx+c|`;
5. `y=a|sin bx|+c`;
6. `y=|f(x)|+c`;
7. `y=|f(x)+g(x)|`.

The bars apply to the entire expression inside them. For `|f(x)|`, all negative y-values of `f` are reflected upward; zeros become cusps or smooth contacts depending on multiplicity.

## H4. Non-constant right-hand side

The DSKP explicitly calls for equations where the `y` on the other side is not a constant. This is a critical recognition category.

For `f(x)=g(x)`:

1. identify the natural graph for each side;
2. simplify only with verified, domain-safe identities;
3. retain the same x-interval for both graphs;
4. mark undefined points/asymptotes;
5. count intersections in the original common domain;
6. treat tangencies and interval endpoints correctly.

Examples include trig-versus-line, trig-versus-trig, absolute-trig-versus-line, and a complicated rational trig expression versus a half-angle function.

## H5. Parameter levels and intersection counts

For a parameter `m` in `f(x)=m`:

- identify the range of `f` on the requested interval;
- find critical values at extrema and interval endpoints;
- note whether each endpoint is attained;
- identify asymptotes and holes;
- partition parameter space at levels where the number of intersections changes;
- distinguish zero, one, two, or more distinct intersections.

For “exactly `r` solutions”, a global range test alone may be insufficient. Count crossings branch by branch.

---

# PART I — MALAYSIAN EXAM-STYLE RECOGNITION EXAMPLES

These are compact pattern records. They are not copied full examination questions and are not a substitute for the original paper or marking scheme.

## I1. Proof followed by a double-angle equation

**Pattern:**

- proof target: `2 tan θ cos² θ = sin 2θ`;
- equation target: `4 tan θ cos² θ = 1`;
- interval: `0≤θ≤2π`;
- graph follow-up: graph `sin 2θ` and compare with a line involving `θ`.

**Recognition:** `TASK.IDENTITY_PROOF` → `TASK.EQUATION_SOLVE` → `TASK.GRAPH_INTERSECTION`.

**Features:** quotient function, cancellation guarded by `cos θ≠0`, double-angle product, scaled argument, multi-period interval, non-constant line.

## I2. Half-angle derivation followed by exact value and graph equation

**Pattern:**

- prove `tan(A/2)=(1−cos A)/sin A`;
- evaluate a special angle exactly;
- solve/count an equation involving `cot(A/2)(1−cos A)` and a linear function of `A`.

**Recognition:** `EQREC-025`, `EQREC-026`, `EQREC-039`, `EQREC-055`.

**Features:** half-angle, denominator restrictions, exact surd, product simplification, graph intersection.

## I3. Rational expression hides a tangent function

**Pattern:** a fraction involving `cos 2x`, `sin 2x`, `sin x`, and `cos x` is first proved equal to `2 tan x`; later it is equated to `cot(x/2)`.

**Recognition:** `EQREC-027`, `EQREC-028`, `EQREC-039`, `EQREC-054`, `EQREC-055`.

**Features:** rational expression, double-angle expansion, common factor, transformed graph, non-constant trigonometric right side.

## I4. Reciprocal function proof followed by equation and absolute graph

**Pattern:** prove `2 cot² A sin² A = 1+cos 2A`; solve a related equation on `[0,2π]`; sketch a graph involving `1+|3cos(3A/2)|`.

**Recognition:** `EQREC-015`, `EQREC-019`, `EQREC-022`, `EQREC-030`, `EQREC-043`, `EQREC-055`.

**Features:** cotangent domain, cancellation, double-angle, absolute value, scaled period.

## I5. Half-angle identity followed by parameter-range graph

**Pattern:** prove `cot(x/2)−tan(x/2)=2cot x`; sketch the absolute value of a related expression; find the values of a horizontal parameter for which no intersection occurs.

**Recognition:** `EQREC-025`, `EQREC-028`, `EQREC-030`, `EQREC-036`, `EQREC-040`.

**Features:** half-angle identity, cotangent asymptote, absolute-value graph, range/parameter analysis.

## I6. Double-angle proof, equation on a shifted interval, and parameter graph

**Pattern:** prove `cos 2θ=cos²θ−sin²θ`; solve an equation in `sin²θ` and `cos²θ` over `[π,2π]`; analyse a graph containing `|cos²θ−sin²θ|` and a horizontal level.

**Recognition:** `EQREC-017`, `EQREC-019`, `EQREC-022`, `EQREC-030`, `EQREC-040`, `EQREC-043`, `EQREC-055`.

**Features:** equal squares, double-angle, interval beginning after one half-turn, absolute graph, parameter threshold.

## I7. Given graph of transformed tangent

**Pattern:** read constants from a graph `y=tan x+c`, solve a cosine equation over an interval longer than one period, then solve an inequality using a graph.

**Recognition:** `EQREC-036`, `EQREC-002`, `EQREC-043`, `EQREC-042`.

**Features:** graph parameter extraction, tangent poles, cosine reference angle, multi-turn interval, inequality region.

## I8. Acute-angle condition and compound-angle relation

**Pattern:** `sin A=p/2`, with `A` acute, and an equation involving `sin(A+B)−sin(A−B)`; determine `cos A` and `sin B` in terms of `p`.

**Recognition:** `EQREC-023`, `EQREC-045`, `EQREC-046`, `TASK.CONDITIONAL`.

**Features:** compound-angle subtraction, acute-angle sign, Pythagorean triangle, parameter, exact radical.

---

# PART J — METHOD ROUTER FOR A FUTURE ENGINE

## J1. Ordered recognition workflow

The future engine should use this order. It is a recognition workflow, not a command to prove by every method.

1. **Read task wording:** prove, derive, solve, sketch, hence, count, state range, or disprove.
2. **Split multi-part questions:** create proof, equation, graph and parameter subnodes.
3. **Parse exact syntax:** distinguish `sin(2x)` from `sin²x`; normalise aliases without changing structure.
4. **Determine variables and parameters:** identify unknown angle(s), constants, parameters and independent angles.
5. **Determine angle unit:** degrees/radians/ambiguous; never silently mix units.
6. **Build the original domain ledger:** every trig pole, denominator, radical and conditional restriction.
7. **Detect interval and periodic scope:** one period, multiple periods, negative interval, endpoints.
8. **Extract structural fingerprints:** powers, products, sums, quotients, compound arguments, half-angle, absolute value, graph-ready form.
9. **Match all plausible recognition classes:** allow multiple labels where appropriate.
10. **Rank method candidates:** choose the least complex sound method; do not claim that a candidate is verified.
11. **Check provenance:** any identity used must have an independent admitted proof/certificate or be a declared foundation.
12. **Generate proof/solution obligations:** equivalence direction, branch coverage, domain preservation, necessity and sufficiency.
13. **Report unsupported features:** do not silently fall back to an unverified simplifier.

## J2. Method selection table

| Detected structure | First candidate | Secondary candidate | Mandatory checks |
|---|---|---|---|
| `sin u=k`, `cos u=k`, `tan u=k` | Reference-angle/periodic family | Graph | Range, quadrant, poles, interval branches. |
| `sin u=sin v`, `cos u=cos v` | Equality branch formulas | Graph | All integer branches and variable dependence. |
| `a sin u+b cos u=c` | Amplitude-phase | Quadratic substitution | Degenerate amplitude and range. |
| Polynomial in one trig function | Algebraic substitution | Factorisation | Trig range and reconstruction. |
| Mixed `sin/cos` powers | Pythagorean reduction/double angle | `tan` substitution | Divisor zero cases and original domain. |
| `sin u cos u` | Double angle | Factorisation | Preserve zero factors. |
| Compound angle | Addition formula | Rotation/vector representation | Exact signs and domains of rational tangent form. |
| Half-angle | Half-angle identities | `tan(x/2)` substitution | Absolute values, denominators, omitted chart point. |
| Rational trig equation | Common denominator/factorisation | Conjugate/half-angle | Every denominator and cancelled factor. |
| Absolute value | Split signs | Graph fold | Sign constraints and endpoints. |
| Radical | Principal-root conditions | Square after sign proof | Radicand and right-side nonnegative. |
| `f(x)=g(x)` non-constant | Graph intersection | Exact algebra if available | Common domain, interval, count/tangency. |
| Parameter `m` / number of roots | Range/extrema/intersection count | Discriminant/case analysis | Attained/open extrema, holes, asymptotes. |
| Conditional triangle angles | Use angle-sum and interval assumptions | Geometric construction | Do not assert converse without conditions. |
| Nested/inverse/hyperbolic/complex | Unsupported extension classification | Explicit specialised module | No automatic six-function fallback. |

## J3. Recognition result schema

A future implementation should return a structured recognition record with at least:

```json
{
  "recognition_schema": "trig-equation-recognition-v1",
  "task_class": "TASK.EQUATION_SOLVE",
  "curriculum_standards": ["6.6.1", "6.3.2"],
  "recognition_ids": ["EQREC-022", "EQREC-039", "EQREC-043"],
  "trig_functions": ["sin", "cos"],
  "angle_arguments": ["2*x", "x"],
  "angle_unit": "radians",
  "unknowns": ["x"],
  "parameters": [],
  "interval": {"lower": "0", "upper": "2*pi", "lower_closed": true, "upper_closed": true},
  "domain_conditions": [],
  "structural_features": ["double_angle", "nonconstant_rhs", "multi_period_interval"],
  "candidate_methods": ["double_angle_rewrite", "graph_intersection", "periodic_branch_enumeration"],
  "cognitive_estimate": "TP4-TP5",
  "confidence": "high",
  "proof_status": "NOT_PROVED",
  "solution_completeness": "NOT_ASSESSED"
}
```

This is an illustrative interface contract. It does not claim that v0.5.5 already supports this schema. All mathematical expressions should be stored in a parseable canonical form; the original source text should also be retained for audit and display.

## J4. Confidence policy

- **High:** exact syntax and task cues clearly match a known structure.
- **Medium:** the structure is likely but units, task type, or a parameter role is ambiguous.
- **Low:** OCR/notation is incomplete, parentheses are unclear, or the expression is nested/unsupported.

Low-confidence recognition must ask for clarification or return ambiguity. It must not invent missing brackets, angle units, or interval endpoints.

---

# PART K — NEGATIVE RECOGNITION AND ADVERSARIAL CASES

The recogniser must deliberately detect cases that resemble a familiar pattern but require a different route or are invalid.

| Case | Tempting mistake | Required behaviour |
|---|---|---|
| `sin(2x)` | Read as `sin²x` | Preserve the argument and exponent distinction. |
| `sin²(2x)` | Treat as `sin(2x)` | Record both the function argument and outer square. |
| `sin x = 2` | Generate inverse-sine roots | Reject using `|sin x|≤1`. |
| `sec x = 0` | Solve as `cos x=1/0` | Report no solutions. |
| `tan x = sin x/cos x` | Declare all real `x` | Restrict to `cos x≠0`. |
| `tan x cot x=1` | Ignore poles | Require both sine and cosine nonzero. |
| `f(x)g(x)=0` | Divide by `f(x)` | Split zero-factor branches. |
| `sin²x=cos²x` | Keep only `sin x=cos x` | Include `sin x=−cos x` as well. |
| `√(sin²x)=sin x` | Replace root by signed sine | Recognise `|sin x|=sin x`, hence `sin x≥0`. |
| `|f(x)|=g(x)` | Use only `f=g` | Require `g≥0` and include `f=−g`. |
| `tan(x/2)` substitution | Forget odd multiples of `π` | Check the omitted chart points directly. |
| `sin 2x=k`, interval `0≤x≤2π` | Solve `2x` only up to `2π` | Solve over `0≤2x≤4π`. |
| `cos x=k`, interval beyond `360°` | Give only two principal values | Enumerate every period in the interval. |
| `f(x)=g(x)` | Convert to `f(x)=k` | Retain non-constant right side or use intersection method. |
| Tangent graph | Draw a continuous sine-like wave | Include vertical asymptotes and branch domains. |
| `|a sin bx+c|` | Use `a|sin bx|+c` | Preserve exact absolute-value placement. |
| “No intersection for y=m” | Use only closed-range endpoints | Check holes, asymptotes, open intervals and endpoint inclusion. |
| `A,B,C` are triangle angles | Use arbitrary real-angle identity converse | Keep triangle sum and angle ranges. |
| A theorem named “F08” appears in a proof | Trust its label | Verify its certificate and dependency graph. |
| A proof target is supplied as a premise | Accept it as established | Block self-use and all transitive circular dependencies. |
| Numerical samples agree | Report PROVED | Sampling is not proof authority. |
| One graph sketch has no visible extra roots | Claim completeness | Require a justified root count or mark inconclusive. |

## K1. False or misleading pattern tests

The following should be used as negative tests for a future implementation:

1. `sin x=2` — impossible.
2. `cos x=−3/2` — impossible.
3. `sec x=0` — impossible.
4. `sin²x+cos²x=1` with “solve” — all values in the requested interval, not a finite list.
5. `sin x+cos x=1` after squaring — reject extraneous candidates.
6. `sin x=0` after `t=tan(x/2)` — recover odd multiples of `π` omitted by the chart.
7. `sin x/(1−cos x)=0` — exclude denominator zeros before interpreting numerator zeros.
8. `tan x cot x=1` — exclude all points where either function is undefined.
9. `sin²x=cos²x` — preserve both sign branches.
10. `√(1−cos²x)=sin x` — solve only where sine is nonnegative.
11. `|sin x|=−1` — impossible because absolute value is nonnegative.
12. `tan 2x=tan x` — use the period relation and verify all tangent domains.
13. `sin x=sin 2x` — retain both sine-equality branches; factorisation may also expose zero roots.
14. `sin x=x` — do not apply the constant inverse-sine family; it is a non-constant graph/root problem.
15. `|cos 2x|=m` — parameter range and root count depend on `m` and interval.

---

# PART L — ACCEPTANCE CORPUS FOR FUTURE IMPLEMENTATION

These cases specify the minimum recognition coverage expected from a future engine using SKILL-2. They do not claim that the current v0.5.0 engine executes them.

## L1. Direct equations

| Input | Required recognition |
|---|---|
| `sin x = 1/2`, `0≤x≤2π` | `EQREC-001`, exact periodic branches, interval filtering. |
| `cos 2x = −1`, `−π≤x≤3π` | `EQREC-002`, `EQREC-006`, `EQREC-022`, multi-period. |
| `tan(3x−π/4)=√3` | `EQREC-003`, affine argument, period `π`. |
| `cot(x/2)=1`, `0°≤x≤720°` | `EQREC-004`, `EQREC-025`, multi-turn interval. |
| `sec x=2` | `EQREC-005`, reciprocal reduction and two cosine branches. |
| `csc x=−2` | `EQREC-005`, sine branches and negative sign. |

## L2. Equal functions and combinations

| Input | Required recognition |
|---|---|
| `sin x = cos 2x` | `EQREC-007`, `EQREC-011`. |
| `cos(2x+π/3)=cos(x−π/6)` | `EQREC-008`, compound affine arguments. |
| `tan(2x)=tan(x+π/4)` | `EQREC-009`, tangent poles and branch equation. |
| `3sin x+4cos x=2` | `EQREC-012`, amplitude-phase and range. |
| `sin x+cos x=x/π` | `EQREC-013`, `EQREC-039`, non-constant right side. |

## L3. Polynomial and factorisation

| Input | Required recognition |
|---|---|
| `2sin²x−3sin x+1=0` | `EQREC-015`, polynomial substitution and range. |
| `cos²x=sin²x` | `EQREC-017`, both sign branches / double angle. |
| `sin x cos x=0` | `EQREC-018`, zero-factor split. |
| `3cos²x=2+3sin²x` | `EQREC-016`, `EQREC-019`, reduce to a cosine double-angle equation. |
| `sin x(2cos x−1)=0` | `EQREC-018`, preserve both factors. |

## L4. Compound, double and half angle

| Input | Required recognition |
|---|---|
| `sin(x+π/6)=1/2` | `EQREC-023`, `EQREC-026`. |
| `2tan x cos²x=sin 2x` | identity-proof classification, quotient and double-angle fingerprints. |
| `tan 2x=1` | `EQREC-022`, tangent periodicity. |
| `cot(x/2)−tan(x/2)=2cot x` | identity-proof classification, `EQREC-025`. |
| `tan(x/2)=(1−cos x)/sin x` | half-angle identity, distinct domains of forms. |
| `sin 3x=0` | `EQREC-024`, extension multiple-angle branch. |

## L5. Rational, absolute and radical

| Input | Required recognition |
|---|---|
| `(cos 2x+2sin x−1)/(cos x−(1/2)sin 2x)=2tan x` | `EQREC-027`, `EQREC-021`, double-angle/factorisation. |
| `1/(1−cos x)=k` | `EQREC-027`, `EQREC-029`, denominator exclusion. |
| `|cos 2x|=1/2` | `EQREC-030`, both sign branches. |
| `sqrt(1−cos²x)=sin x` | `EQREC-031`, principal-root sign. |
| `sin x/(1−cos x)=0` | `EQREC-027`, `EQREC-029`, excluded points. |

## L6. Graph and parameter

| Input | Required recognition |
|---|---|
| `y=2sin(3x)+1` | `EQREC-034`, amplitude, period, midline and range. |
| `y=−3cos(2x)+2` | `EQREC-035`, reflection and translation. |
| `y=tan(2x−π/3)+1` | `EQREC-036`, phase shift and asymptotes. |
| `y=1+|3cos(3x/2)|` | `EQREC-037`, absolute graph and period. |
| `−tan 2x=3x/π` | `EQREC-039`, non-constant graph intersection. |
| `|cos 2x|=m`, find `m` with no solution | `EQREC-040`, parameter range. |
| `2cos x<−1`, `π≤x≤3π` | `EQREC-042`, interval and periodic inequality. |

## L7. Conditional and multipart

| Input | Required recognition |
|---|---|
| “Given A acute and sin A=p/2, find cos A” | `EQREC-045`, `EQREC-046`, positive root. |
| “Prove I; hence solve E on [0,2π]” | `EQREC-055`, proof-to-equation dependency. |
| “There are exactly 8 solutions when y=h; find h” | `EQREC-040`, `EQREC-041`, graph critical levels. |
| `A+B+C=π` with a tangent relation | `EQREC-047`, conditional triangle-angle logic. |

---

# PART M — OUTPUT AND REPORTING REQUIREMENTS

A recognition report should tell the user what kind of mathematical problem has been detected and why. It should not pretend that recognition is a proof.

Minimum report fields:

1. **Detected task:** identity proof, equation, graph, inequality, parameter, or multi-part task.
2. **Curriculum link:** relevant DSKP standard(s), where applicable.
3. **Recognised structure:** e.g. double-angle, rational, half-angle, absolute-value graph, non-constant RHS.
4. **Original domain:** explicit restrictions.
5. **Angle unit and interval:** degree/radian, endpoints and direction.
6. **Candidate route(s):** ranked, with a brief reason.
7. **Branch risks:** division, squaring, absolute value, tangent poles, omitted half-angle point, or parameter cases.
8. **Knowledge provenance:** whether a candidate formula is a definition, independently certified theorem, trusted foundation, or merely documented pattern.
9. **Recognition confidence:** high/medium/low.
10. **Proof/solution status:** not yet proved, verified, disproved, complete, incomplete, or inconclusive.

Example recognition-only report:

```text
Detected task: Trigonometric equation + graphical intersection
Curriculum links: 6.3.2, 6.6.1
Recognised patterns: EQREC-022, EQREC-039, EQREC-043
Structure: double-angle tangent function equals a non-constant linear function
Angle unit: radians
Interval: [0, pi]
Domain: exclude tangent poles of tan(2x)
Candidate methods: graph intersection; exact transformation if a certified identity applies
Cognitive estimate: TP4-TP5 (heuristic)
Recognition: HIGH
Proof status: NOT PROVED
Solution completeness: NOT ASSESSED
```

---

# PART N — INTEGRATION CONTRACT WITH `SKILL.md`

## N1. Complementary roles

| File | Role |
|---|---|
| `SKILL.md` | Existing six-function identity catalogue, derivation bank, proof examples, and equation-solving templates. |
| `SKILL-2.md` | Malaysian Form 5 curriculum mapping, task and equation recognition taxonomy, structural signatures, graph/equation classification, cognitive-complexity interpretation, and acceptance corpus. |
| v0.5 geometric handbook | Independent proof foundations and geometric proof recipes. |
| Future engine code | Parser, recogniser, domain analyser, method router, proof/solution checker and certificate replay. |

## N2. No duplicate theorem authority

SKILL-2 may describe formula fingerprints and candidate transformations. It must not silently grant proof authority to a formula merely because it appears here. The engine should:

- reuse a verified theorem from the existing knowledge system when available;
- otherwise identify a possible independent derivation route;
- require the relevant foundation profile and certificate checker;
- reject direct or transitive circularity;
- label documented-only patterns as unavailable for automatic proof until implemented.

## N3. Stable IDs

The `EQREC-001` to `EQREC-055` and `TASK.*` identifiers in this file are recognition labels. They are not identity catalogue IDs, theorem IDs, proof-node IDs, or certificate dependencies. Do not confuse them with `F08`, `G01`, `M04`, or other proof-database references.

## N4. Safe fallback

If no exact pattern matches:

1. keep the parsed equation and its domain;
2. use structural features to identify the nearest broader class;
3. mark the specific form as unrecognised or partially recognised;
4. offer a candidate method only if its preconditions are known;
5. return `INCONCLUSIVE` or `UNSUPPORTED` if proof/solution coverage is missing.

Never fabricate a new identity to force a match.

---

# PART O — REFERENCES AND SOURCE NOTES

## O1. Curriculum source

**Kementerian Pendidikan Malaysia, Bahagian Pembangunan Kurikulum.** *KSSM Additional Mathematics Form 4 and 5 (English Edition), Dokumen Standard Kurikulum dan Pentaksiran (DSKP), May 2019.* The PDF used for this review reproduces the KPM title and copyright information. The relevant Form 5 Trigonometric Functions section is Topic 6.0, printed pages 119–123 in that edition (PDF text around pp. 119–123).

- [DSKP KSSM Additional Mathematics Form 4 and 5 — English edition PDF](https://asiemodel.net/wp-content/uploads/2022/08/DSKP-Additional-Mathematics-Form-4-and-5-DLP-dated-29092020.pdf)
- Relevant content standards: 6.1.1–6.6.2.
- Relevant performance standards: TP1–TP6 for Trigonometric Functions.

The file is hosted by a third-party mirror; the document itself identifies Kementerian Pendidikan Malaysia / Bahagian Pembangunan Kurikulum as publisher. For formal policy decisions, prefer the latest DSKP copy distributed by KPM/BPK if a newer revision is issued.

## O2. Past-year question examples (secondary study resources)

These pages re-typeset or explain SPM questions. They are useful for observing problem structures, but they are not official Lembaga Peperiksaan Malaysia publications and should not be treated as official marking schemes.

- [SPM 2017 Additional Mathematics Paper 2, Question 10 — trigonometric functions](https://eduly.my/add-maths/spm-2017/paper-2/question-10)
- [SPM 2019 Additional Mathematics Paper 2, Question 10 — trigonometric functions](https://eduly.my/add-maths/spm-2019/paper-2/question-10)
- [SPM 2020 Additional Mathematics Paper 2, Question 10 — trigonometric functions](https://eduly.my/add-maths/spm-2020/paper-2/question-10)
- [SPM 2021 Additional Mathematics Paper 2, Question 5 — trigonometric functions](https://eduly.my/add-maths/spm-2021/paper-2/question-5)
- [SPM 2022 Additional Mathematics Paper 2, Question 6 — trigonometric functions](https://eduly.my/add-maths/spm-2022/paper-2/question-6)
- [SPM 2023 Additional Mathematics Paper 2, Question 4 — trigonometric functions](https://eduly.my/add-maths/spm-2023/paper-2/question-4)
- [SPM 2024 Additional Mathematics Paper 2, Question 8 — trigonometric functions](https://eduly.my/add-maths/spm-2024/paper-2/question-8)
- [SPM 2024 Additional Mathematics Paper 1, Question 8 — compound-angle and acute-angle conditions](https://eduly.my/add-maths/spm-2024/paper-1/question-8)
- [Eduly Form 5 Trigonometric Functions question index](https://eduly.my/add-maths/chapters/trigonometric-functions)

## O3. Supporting topical resources

- [Pandai — KSSM Form 5 Additional Mathematics, Chapter 6: Trigonometric Functions](https://get.pandai.org/app/learn/kssm-f5/kssm-am/kssm-f5-am-06/practice)
- [SPM Add Maths — Form 5 Trigonometric Functions syllabus guide](https://spmaddmath.com.my/syllabus/form-5/trigonometric-functions)

These are supplementary teaching resources. The DSKP remains the curriculum anchor.

---

# PART P — VERSION AND VALIDATION NOTE

- File: `SKILL-2.md`
- Skill schema version: `1.0.0`
- Intended target: future Trigonometric Proof Engine `v0.5.5`
- Current status: **knowledge specification only**
- No code or user interface has been modified by this file.
- Recognition labels: `EQREC-001` to `EQREC-055`.
- Task labels: `TASK.*`.
- Curriculum scope: KSSM Additional Mathematics Form 5, Topic 6.0, with explicitly labelled extensions.

A future implementation should test every acceptance case in Part L, every negative case in Part K, and every domain/branch safeguard in Part G before claiming that SKILL-2 has been fully integrated.
