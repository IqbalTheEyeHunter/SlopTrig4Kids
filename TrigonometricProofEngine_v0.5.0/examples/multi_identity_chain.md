# Trigonometric Proof Report

- **Engine version:** 0.4.1
- **Status:** PROVED
- **Selected route:** LHS using identity catalogue

## Claim

\[ \sin^{2}{\left(x \right)} + \cos^{2}{\left(x \right)} = - \tan^{2}{\left(y \right)} + \sec^{2}{\left(y \right)} \]

## Original common-domain conditions

- `cos(y) ≠ 0`

## Derivation chain

- **Identity sequence:** F08 → F11
- **Identity applications:** 2
- Each identity is applied as a separate, recorded substitution below.

## Proof / analysis steps

1. **Start with the LHS** — LHS
   - To: `sin(x)**2 + cos(x)**2`
   - Reason: Original expression in the requested identity.
2. **Apply identity F08: sin²x + cos²x = 1** — LHS (Identity IDs: F08)
   - From: `sin(x)**2 + cos(x)**2`
   - To: `1`
   - Reason: Apply established identity F08 in the forward direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Previously established result: **F08 — sin²x + cos²x = 1**
   - Variable substitution: x → x
3. **Apply identity F11: sec²x − tan²x = 1** — LHS (Identity IDs: F11)
   - From: `1`
   - To: `-tan(y)**2 + sec(y)**2`
   - Reason: Apply established identity F11 in the reverse direction to the matched subexpression. The instantiated identity is checked against the recorded step.
   - Previously established result: **F11 — sec²x − tan²x = 1**
   - Variable substitution: x → y
   - Conditions for this use: cos(y) ≠ 0
4. **Match the target side** — LHS
   - From: `-tan(y)**2 + sec(y)**2`
   - To: `-tan(y)**2 + sec(y)**2`
   - Reason: The displayed identity substitutions establish the requested target form.

## Identities / theorems used

- **F08 — sin²x + cos²x = 1**: `sin(x)**2 + cos(x)**2 = 1` (Bundled SKILL.md identity catalogue)
- **F11 — sec²x − tan²x = 1**: `-tan(x)**2 + sec(x)**2 = 1` (Bundled SKILL.md identity catalogue)

## Conclusion

The identity search found a derivation using 2 explicit established identity application(s). Each substitution and algebraic transformation is recorded separately on the original common domain.

> Numerical sampling is used only to find counterexamples; it is never used to certify an identity.