# Problem 05

## The original problem
Compute
$$\lim_{n\to\infty}\left(1+\frac1n\right)^n.$$
Calculate several values for increasing $n$ and compare the observed behavior with the value of the limit. Explain why a few values do not constitute a proof.

## What we are looking for
We want the limiting value of the sequence $\left(1+\frac1n\right)^n$ as $n$ grows without bound. This is a classical limit that defines the number $e$. We also need to list some numerical values and explain why observing a pattern in finitely many terms is not the same as proving the limit exists.

## The idea we need
The limit
$$\lim_{n\to\infty}\left(1+\frac1n\right)^n=e$$
is the classical definition of Euler's number $e$, approximately $2.71828$. It is not obtained by substituting $n=\infty$ directly (that would give the indeterminate form $1^\infty$). One standard justification uses the binomial theorem: expanding $\left(1+\frac1n\right)^n$ shows the sequence is increasing and bounded above, so it converges, and its limit is defined to be $e$. The key point is that this is a definition backed by a theorem, not something we can read off from a few sample values.

## Step-by-step solution
1. The expression $\left(1+\frac1n\right)^n$ as $n\to\infty$ has the indeterminate form $1^\infty$, because the base tends to $1$ and the exponent tends to infinity. We cannot evaluate it by direct substitution.
2. The classical result, provable using the binomial theorem and the monotone convergence theorem, is
$$\lim_{n\to\infty}\left(1+\frac1n\right)^n=e,\qquad e\approx 2.718281828.$$
The number $e$ is defined as this limit.

## Numerical values
3. For $n=1$: $\left(1+\frac11\right)^1=2$.
4. For $n=2$: $\left(1+\frac12\right)^2=\left(\frac32\right)^2=2.25$.
5. For $n=10$: $\left(1+\frac1{10}\right)^{10}\approx 2.59374$.
6. For $n=100$: $\left(1+\frac1{100}\right)^{100}\approx 2.70481$.
7. For $n=1000$: $\left(1+\frac1{1000}\right)^{1000}\approx 2.71692$.
8. For $n=10000$: $\left(1+\frac1{10000}\right)^{10000}\approx 2.71815$.
These values increase and get closer to $e\approx 2.71828$, consistent with the analytical result.

## Why a few values do not constitute a proof
9. Observing finitely many values can suggest a pattern, but it cannot establish that the sequence converges or identify its limit. A sequence could follow a pattern for many terms and then behave differently later, or it could grow so slowly that it eventually exceeds any proposed limit. A proof requires an analytical argument (for example, showing the sequence is increasing and bounded above) that covers all $n$, not just the ones we have computed.

## Why each step is valid
Steps 3 through 8 are direct substitutions into the formula and are exact or correctly rounded approximations. Step 2 relies on the standard theorem defining $e$ as this limit, which is established by the binomial expansion and monotone convergence. Step 9 states a general logical point: finite observation never proves a universal statement about all natural numbers.

## Final answer (in words)
The sequence approaches Euler's number $e$, approximately $2.71828$, as $n$ grows without bound. Numerical values for increasing $n$ confirm that the terms rise toward $e$, but only an analytical argument proves the limit.

## Verification
The numerical checks above give $2.59374$ at $n=10$, $2.70481$ at $n=100$, $2.71692$ at $n=1000$, and $2.71815$ at $n=10000$, all approaching $e\approx 2.71828$ from below. The values are increasing and closing in on $e$, which independently supports the analytical result.

## Common mistakes
- Substituting $n=\infty$ directly and claiming the limit is $1^\infty=1$, which is invalid because $1^\infty$ is an indeterminate form.
- Concluding the limit is exactly one of the computed values (for example $2.71815$) rather than recognizing $e$ as the limiting value.
- Believing that a long table of values is a proof of convergence.

## How I would explain it in class
As $n$ gets bigger, the base $1+1/n$ gets closer and closer to $1$, while the exponent $n$ gets bigger and bigger, and these two effects balance out at a special number called $e$. If you plug in bigger and bigger values of $n$, you see the results creeping up toward $2.71828$. But just calculating a few values isn't a proof—you need a real argument to know the sequence settles on $e$ for all $n$.
