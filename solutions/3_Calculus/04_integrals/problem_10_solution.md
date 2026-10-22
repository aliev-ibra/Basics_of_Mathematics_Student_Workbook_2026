# Problem 10

## The original problem

Before carrying out the exact calculation, estimate the possible range of values of the integral
$$\int_0^2(x^2+1)\,dx,$$
using
$$1\le x^2+1\le5$$
on $[0,2]$. Only then compute the integral exactly, compare the result with the earlier estimate, and explain what type of computational error such a check can detect.

> **Why this problem:** it teaches how to predict the possible range of a result and check the calculation.

## What we are looking for

We want two things. First a range, a lower bound and an upper bound, in which the integral must lie. Second the exact value, which must fall inside that range.

## The idea we need

**Comparison of integrals.** If $m\le f(x)\le M$ on $[a,b]$, then the area under $f$ lies between the area of a rectangle of height $m$ and the area of a rectangle of height $M$. This gives
$$m(b-a)\le\int_a^b f(x)\,dx\le M(b-a).$$

**The exact value** comes from the Fundamental Theorem of Calculus: if $F$ is an antiderivative of $f$, the integral equals $F(b)-F(a)$.

## Step-by-step solution

**Step 1. The estimate.** On $[0,2]$ we are given $1\le x^2+1\le5$. The interval has length $2-0=2$. So the integral is at least $1\cdot2=2$ and at most $5\cdot2=10$:
$$2\le\int_0^2(x^2+1)\,dx\le10.$$

**Step 2. An antiderivative.** By the power rule, an antiderivative of $x^2+1$ is $F(x)=\frac{x^3}{3}+x$.

**Step 3. The exact value.**
$$\int_0^2(x^2+1)\,dx=\left(\frac{8}{3}+2\right)-(0+0)=\frac{14}{3}.$$

**Step 4. Compare.** The number $\frac{14}{3}\approx4.67$ lies between $2$ and $10$, so the result agrees with the estimate.

## Why each step is valid

- Step 1 is valid because the graph lies between the heights $1$ and $5$, so it encloses more area than the low rectangle and less than the tall rectangle.
- Step 2 is valid because the derivative of $\frac{x^3}{3}+x$ is $x^2+1$.
- Step 3 is valid because of the Fundamental Theorem of Calculus. At $x=2$ we get $\frac{2^3}{3}+2=\frac83+2=\frac{14}{3}$, and at $x=0$ we get $0$.
- Step 4 is valid because a correct result cannot leave the proven range.

## Final answer (in words)

The integral must lie between $2$ and $10$, and its exact value is fourteen thirds: $\int_0^2(x^2+1)\,dx=\frac{14}{3}\approx4.67$. This number is inside the predicted range, so the estimate and the calculation agree. Such a check can detect large errors, such as a wrong sign, a missing term, a wrong power, or an arithmetic slip that moves the answer out of range.

## Verification

**Check 1: differentiate the antiderivative.** The derivative of $\frac{x^3}{3}+x$ is $x^2+1$, which is the integrand.

**Check 2: Simpson's rule.** Use the points $0$, $1$, $2$, where the function has the values $1$, $2$, $5$. Simpson's rule gives $\frac{1}{3}(1+4\cdot2+5)=\frac{14}{3}$, the same value.

**Check 3: geometry.** The graph is above $y=1$, and the rectangle under $y=1$ has area $2$. The remaining area is the area under $y=x^2$, which is $\frac{8}{3}$. The sum is $2+\frac83=\frac{14}{3}$.

## Common mistakes

- Using the range of the function instead of multiplying by the length of the interval, which gives $1$ to $5$ instead of $2$ to $10$.
- Forgetting to integrate the constant $1$, so that the term $x$ is missing.
- Computing $F(0)-F(2)$ instead of $F(2)-F(0)$.
- Thinking that the estimate proves the exact value. It only proves that the value is in the range, so a small error inside the range is not detected.

## How I would explain it in class

Because $x^2+1$ is between $1$ and $5$ on an interval of length $2$, the integral must be between $2$ and $10$. The exact calculation gives $\frac{8}{3}+2=\frac{14}{3}$, which is about $4.67$ and lies inside this range. The range check catches big mistakes like a wrong sign or a missing term, but it cannot catch a small error that stays inside the range.
