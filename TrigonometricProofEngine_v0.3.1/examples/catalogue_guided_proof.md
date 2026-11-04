# Catalogue-Guided Proof Example — v0.3.1

## Target identity

\[
\frac{\sin^2 x}{1-\cos x}=1+\cos x
\]

## Original domain

\[
1-\cos x\ne 0
\]

## Step-by-step proof

**Step 1 — Start with the LHS**

\[
\frac{\sin^2 x}{1-\cos x}
\]

**Step 2 — Apply identity F18**

Use \(\sin^2x=1-\cos^2x\):

\[
\frac{1-\cos^2 x}{1-\cos x}
\]

**Step 3 — Factor the numerator**

\[
\frac{-(\cos x-1)(\cos x+1)}{1-\cos x}
\]

**Step 4 — Cancel the common factor**

\[
\cos x+1
\]

The cancellation is valid because the original domain requires \(1-\cos x\ne0\).

**Step 5 — Match the RHS**

\[
\boxed{\frac{\sin^2 x}{1-\cos x}=1+\cos x}
\]

The proof uses identity **F18** and two explicit algebraic transformations. The original domain restriction is retained in the report.

## Application input

```text
LHS: sin(x)**2/(1-cos(x))
RHS: 1+cos(x)
Proof strategy: Use full identity catalogue
```
