# Problem 2

## The original problem

Compute
$$\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx.$$
First rewrite the terms as powers, determine the domain of the original expression, and verify the result by differentiation.

> **Why this problem:** it reinforces the power rule and reminds the student to keep track of the domain.

## What we are looking for

We are asked for an antiderivative of a function written in three different ways: a square root, a fraction, and a fractional power. The work has three parts: put everything into power form so that one rule applies to all of it, work out where the original expression is even defined, and differentiate the answer to prove it. The domain matters because a formula can be algebraically correct and still be meaningless at some points.

## The idea we need

**Power rule for antiderivatives.** For any real $n$ with $n\neq -1$,
$$\int x^n\,dx=\frac{x^{n+1}}{n+1}+C.$$
The condition $n\neq -1$ is essential: when $n=-1$ the denominator would be zero, and that case is handled by a logarithm instead (Problem 6).

**Rewriting into power form.** Every term must be written as a coefficient times a single power of $x$:
$$\sqrt{x}=x^{1/2},\qquad \frac{1}{x^{2}}=x^{-2},\qquad x^{1/3}\ \text{is already a power}.$$
Only after this rewriting does the power rule apply to the whole integrand.

**Domain rules.** A square root $\sqrt{x}$ of a real number needs $x\ge 0$. A denominator $x^2$ needs $x\neq 0$. A cube root $x^{1/3}$ is real for every $x$, including negative ones, because an odd root of a negative number is still real.

**Constant of integration.** Every indefinite integral ends with $+C$, since the derivative of a constant is zero and therefore does not change the antiderivative.

## Step-by-step solution

**Step 1. Rewrite every term as a coefficient times a power of $x$.**

$$
2\sqrt{x}=2x^{1/2},\qquad \frac{3}{x^{2}}=3x^{-2},\qquad -x^{1/3}=-1\cdot x^{1/3}.
$$

So the integral becomes
$$\int\left(2x^{1/2}+3x^{-2}-x^{1/3}\right)\,dx.$$

**Step 2. Determine the domain of the original integrand.**

- The term $2\sqrt{x}$ requires $x\ge 0$.
- The term $\dfrac{3}{x^2}$ requires $x\neq 0$.
- The term $-x^{1/3}$ is real for every $x$.

Combining these conditions, the integrand is defined exactly where $x>0$. So the domain is the open interval $(0,\infty)$, and this is the interval on which our antiderivative will be valid.

**Step 3. Integrate the first term.**

Here $n=\frac12$, which is not the forbidden value $-1$, so the power rule applies:
$$\int 2x^{1/2}\,dx=2\cdot\frac{x^{1/2+1}}{1/2+1}=2\cdot\frac{x^{3/2}}{3/2}=\frac{4}{3}x^{3/2}.$$

**Step 4. Integrate the second term.**

Here $n=-2$. The power rule still applies because $-2\neq -1$:
$$\int 3x^{-2}\,dx=3\cdot\frac{x^{-2+1}}{-2+1}=3\cdot\frac{x^{-1}}{-1}=-3x^{-1}=-\frac{3}{x}.$$
Note the sign: the denominator $n+1=-1$ is negative, so this antiderivative is negative.

**Step 5. Integrate the third term.**

Here $n=\frac13$:
$$\int(-x^{1/3})\,dx=-\frac{x^{1/3+1}}{1/3+1}=-\frac{x^{4/3}}{4/3}=-\frac{3}{4}x^{4/3}.$$

**Step 6. Add the three pieces and one constant.**

$$
\int\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)\,dx=\frac{4}{3}x^{3/2}-\frac{3}{x}-\frac{3}{4}x^{4/3}+C,\qquad x>0.
$$

**Step 7. Note where the constant comes from.**

We add a single $C$ because differentiating our answer gives back the integrand regardless of the value of $C$. The constant is the free vertical position of the antiderivative curve.

## Why each step is valid

- Step 1 is valid because $\sqrt{x}=x^{1/2}$ for $x\ge 0$ and $\dfrac{1}{x^2}=x^{-2}$ for $x\neq 0$; the rewriting changes nothing about the values of the function.
- Step 2 is valid because a real square root needs a non-negative argument, a denominator may not be zero, and the cube root of a negative number is real.
- Step 3 is valid because the power rule applies to $n=\frac12$, and the arithmetic $2\cdot\frac{2}{3}=\frac{4}{3}$ checks out.
- Step 4 is valid because the power rule applies to $n=-2$; the minus sign appears automatically because the new denominator $n+1=-1$ is negative.
- Step 5 is valid because the power rule applies to $n=\frac13$, and $1+\frac13=\frac43$, so the reciprocal factor is $\frac34$.
- Step 6 is valid because the derivative of a sum is the sum of the derivatives and the derivative of $C$ is zero.
- Step 7 is valid for the same reason: adding a constant changes no derivative.

## Final answer (in words)

The antiderivative is the expression $\frac{4}{3}x^{3/2}-\frac{3}{x}-\frac{3}{4}x^{4/3}$ plus an arbitrary constant $C$, and this formula is valid on the interval $x>0$. In words: the integrand is the sum of a square-root term, a reciprocal-square term and a cube-root term, and the original expression is defined only for positive $x$, because the square root needs $x\ge 0$ while the denominator $x^2$ forbids $x=0$.

## Verification

**Check 1 (the required one): differentiate the answer.** Let
$$F(x)=\frac{4}{3}x^{3/2}-\frac{3}{x}-\frac{3}{4}x^{4/3}.$$
Differentiating each piece:
$$\frac{d}{dx}\left(\frac{4}{3}x^{3/2}\right)=\frac{4}{3}\cdot\frac{3}{2}x^{1/2}=2x^{1/2}=2\sqrt{x},$$
$$\frac{d}{dx}\left(-\frac{3}{x}\right)=-3\cdot(-x^{-2})=3x^{-2}=\frac{3}{x^{2}},$$
$$\frac{d}{dx}\left(-\frac{3}{4}x^{4/3}\right)=-\frac{3}{4}\cdot\frac{4}{3}x^{1/3}=-x^{1/3}.$$
The three pieces give back exactly the three terms of the original integrand, so $F'=f$ on $(0,\infty)$.

**Check 2: a numerical check of a definite integral.** The antiderivative evaluated at the endpoints gives the definite integral by the Fundamental Theorem of Calculus:
$$\int_1^2\left(2\sqrt{x}+\frac{3}{x^2}-x^{1/3}\right)dx=F(2)-F(1).$$
Here $F(2)=\frac43\cdot 2^{3/2}-\frac32-\frac34\cdot 2^{4/3}\approx 3.771236-1.5-1.889882=0.381355$ and $F(1)=\frac43-3-\frac34=-2.416667$, so the integral should be about $2.798022$.

On the other hand, Simpson's rule with step $h=0.25$ on $[1,2]$ uses the values
$$f(1)\approx 4.000000,\quad f(1.25)\approx 3.078851,\quad f(1.5)\approx 2.638109,\quad f(1.75)\approx 2.420272,\quad f(2)\approx 2.318506,$$
and gives
$$\frac{0.25}{3}\bigl(f(1)+4f(1.25)+2f(1.5)+4f(1.75)+f(2)\bigr)\approx 2.799268.$$
The numerical estimate $2.7993$ is close to the exact value $2.7980$, so the formula behaves correctly.

## Common mistakes

- **Writing $\int\frac{3}{x^2}\,dx=3\ln x$.** That is the antiderivative of $\frac{3}{x}$, not of $\frac{3}{x^{2}}$. The correct piece is $-\frac{3}{x}$.
- **Forgetting to raise the exponent by one.** For example, $\int x^{1/3}\,dx$ is $\frac{3}{4}x^{4/3}$, not $x^{2/3}$ and not $\frac{3}{4}x^{1/3}$.
- **Losing the sign when the new denominator is negative.** Since $n+1=-1$ for $n=-2$, the term comes out negative: $-3/x$, and not $+3/x$.
- **Ignoring the domain.** The original expression is not defined at $x=0$ and is not real for $x<0$, so the answer must be stated for $x>0$ and must not be evaluated at $0$.
- **Forgetting the constant $C$.** The indefinite integral is the family, not a single function.

## How I would explain it in class

First I rewrite everything as powers: $\sqrt{x}=x^{1/2}$ and $\frac{1}{x^{2}}=x^{-2}$, so one rule handles all three terms. The square root needs $x\ge 0$ and the denominator needs $x\neq 0$, so the integrand lives only on $x>0$. Applying the power rule term by term gives $\frac{4}{3}x^{3/2}-\frac{3}{x}-\frac{3}{4}x^{4/3}+C$, and differentiating that expression returns $2\sqrt{x}+\frac{3}{x^2}-x^{1/3}$, exactly as required.
