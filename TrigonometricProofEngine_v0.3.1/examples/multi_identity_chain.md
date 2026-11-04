# Multi-Identity Proof Example (v0.3.1)

## Available established identities

1. **Pythagorean result**

   \[\sin^2 t + \cos^2 t = 1\]

2. **Secant-tangent result**

   \[1 = \sec^2 u - \tan^2 u\]

## Target claim

\[\sin^2 x + \cos^2 x = \sec^2 y - \tan^2 y\]

## Proof chain

\[
\begin{aligned}
\sin^2 x + \cos^2 x
&= 1 && \text{Pythagorean result, with }t=x\\
&= \sec^2 y - \tan^2 y && \text{Secant-tangent result, with }u=y.
\end{aligned}
\]

Therefore,

\[\boxed{\sin^2 x + \cos^2 x = \sec^2 y - \tan^2 y}\]

provided \(\cos y \ne 0\), which is required for the secant and tangent expressions to be defined.

## Enter into the application

**LHS**

```text
sin(x)**2 + cos(x)**2
```

**RHS**

```text
sec(y)**2 - tan(y)**2
```

**Premises**

```text
Pythagorean result: sin(t)**2 + cos(t)**2 = 1
Secant-tangent result: 1 = sec(u)**2 - tan(u)**2
```

Select **Use supplied identities**. The proof report should show both theorem applications as separate steps.
