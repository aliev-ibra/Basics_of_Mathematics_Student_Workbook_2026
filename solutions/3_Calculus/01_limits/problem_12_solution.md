# Problem 12

## The original problem
Compute
$$\lim_{x\to0}(1+3x)^{1/x}.$$
Connect the result with the limit from Exercise 5 and show the appropriate transformation.

## What we are looking for
We want the number that $(1+3x)^{1/x}$ approaches when $x$ comes close to $0$ from both sides. The base $1+3x$ tends to $1$ and the exponent $\frac1x$ becomes very large in absolute value, so direct substitution is not possible. We must relate this expression to the classical limit $\left(1+\frac1n\right)^n\to e$ from Exercise 5.

## The idea we need
The classical limit says that $\left(1+\frac1m\right)^m$ tends to the number $e\approx2.71828$ when $m$ becomes very large. It remains true when $m$ becomes very large and negative. The plan is to rename the small quantity $3x$ so that the base takes the form $1+\frac1m$ and the exponent becomes a multiple of $m$. Then the expression is a power of the classical expression.

## Step-by-step solution
1. The form is $1^\infty$: the base goes to $1$ and the exponent goes to infinity in absolute value. This is an indeterminate form, so we transform.
2. Introduce a new variable $m=\dfrac{1}{3x}$. Then $3x=\dfrac1m$ and $x=\dfrac{1}{3m}$. As $x\to0$, $|m|\to\infty$.
3. Rewrite the exponent: $\dfrac1x=3m$.
4. Rewrite the whole expression:
$$(1+3x)^{1/x}=\left(1+\frac1m\right)^{3m}.$$
5. Use the rule $(A^{p})^{q}=A^{pq}$ in reverse:
$$\left(1+\frac1m\right)^{3m}=\left[\left(1+\frac1m\right)^{m}\right]^{3}.$$
6. The bracket tends to $e$ as $|m|\to\infty$, from the classical limit. The cube is continuous, so
$$\lim_{x\to0}(1+3x)^{1/x}=e^3.$$
7. In decimals, $e^3\approx20.0855$.

## Why each step is valid
Step 2 is valid because $x\neq0$ near the limit point, so $m$ is well defined, and $x\to0$ exactly when $|m|\to\infty$. Step 4 is an exact rewriting: $1+3x=1+\frac1m$ and $\frac1x=3m$. Step 5 is the power rule for exponents. Step 6 uses two facts: the limit $\left(1+\frac1m\right)^m\to e$ holds for $m\to+\infty$ and also for $m\to-\infty$ (the second is a standard extension of Exercise 5), and a limit can be moved inside the continuous function $t\mapsto t^3$.

## Final answer (in words)
The limit is $e^3$, which is approximately $20.0855$. The expression is the cube of the classical expression for $e$, after renaming $m=\frac{1}{3x}$.

## Verification
Numerical check with real values of $(1+3x)^{1/x}$:

| $x$ | value | $x$ | value |
|---|---|---|---|
| $0.1$ | $13.7858$ | $-0.1$ | $35.4013$ |
| $0.01$ | $19.2186$ | $-0.01$ | $21.0294$ |
| $0.001$ | $19.9955$ | $-0.001$ | $20.1763$ |

From both sides the values close in on $e^3\approx20.0855$. A different method uses logarithms. We have $\ln\left((1+3x)^{1/x}\right)=\dfrac{\ln(1+3x)}{x}=3\cdot\dfrac{\ln(1+3x)}{3x}$. Since $\dfrac{\ln(1+u)}{u}\to1$ as $u\to0$, this tends to $3$. So the original expression tends to $e^3$, the same answer.

## Common mistakes
- Saying the limit is $1$ because the base tends to $1$. The exponent is also changing, and $1^\infty$ is indeterminate.
- Substituting $m=\frac1x$ and forgetting the factor $3$, which gives the wrong answer $e$ instead of $e^3$.
- Writing $e\cdot3$ instead of $e^3$. The factor $3$ becomes a power.

## How I would explain it in class
The base is one plus a small number $3x$ and the exponent is one over $x$, which is almost the pattern for $e$, except that the small number and the exponent do not match. I rename $m=\frac{1}{3x}$, so the base is $1+\frac1m$ and the exponent becomes $3m$. That is the classical expression raised to the third power, so the answer is $e^3$.
