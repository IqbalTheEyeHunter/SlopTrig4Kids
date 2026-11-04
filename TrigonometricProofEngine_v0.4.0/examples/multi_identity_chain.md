# Multi-Identity Catalogue Proof (v0.4.0)

This example uses only identities from the bundled `SKILL.md` catalogue. No user-supplied premises are required.

## Claim

\[1+\tan^2 x = \frac{1}{\cos^2 x}\]

## Search result

The catalogue search can derive the RHS from the LHS using two established identities:

1. **F09 — Pythagorean identity for tangent and secant**
   \[1+\tan^2x=\sec^2x\]
2. **F03 — Reciprocal identity for secant**
   \[\sec x=\frac{1}{\cos x}\]

## Proof chain

\[\begin{aligned}
1+\tan^2x & = \sec^2x && \text{F09}\\
& = \left(\frac{1}{\cos x}\right)^2 && \text{F03}\\
& = \frac{1}{\cos^2x}. && \text{Algebra}
\end{aligned}\]

Therefore, the identity is established for \(\cos x\ne0\), which is the common domain of the original expressions.

## Enter into the application

**LHS**: `1 + tan(x)**2`

**RHS**: `1/cos(x)**2`

Select **Use full identity catalogue**. The report should show two separate identity-application steps, their substitutions, and the sequence `F09 → F03`.
