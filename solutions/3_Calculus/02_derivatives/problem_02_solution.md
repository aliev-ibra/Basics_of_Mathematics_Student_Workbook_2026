# Problem 2

## The original problem

For
$$f(x)=2\sqrt{x}-\frac{3}{x^2}+x^{3/2}$$
1. rewrite the function using powers,
2. determine the domain,
3. compute the derivative,
4. compare the domain of the function with the domain of its derivative.

> **Why this problem:** it teaches how to rewrite different forms so that the power rule can be applied and how to keep track of the domain.

## What we are looking for

We want four things. First, the same function written only with powers of $x$. Second, the set of $x$ for which the formula makes sense; this set is called the domain. Third, the derivative $f'(x)$. Fourth, a comparison: is the set where $f'$ makes sense the same set as the domain of $f$, or is it smaller?

## The idea we need

The **power rule** says: if $g(x)=x^n$ for a fixed number $n$, then $g'(x)=n\,x^{n-1}$. The number $n$ may be negative or a fraction. The rule only works when the function is written as a plain power of $x$. A root or a fraction does not look like a power, so we first rewrite it with these two facts:
$$\sqrt{x}=x^{1/2},\qquad \frac{1}{x^2}=x^{-2}.$$
We recognise that we need this rewriting because the formula contains a square root and a fraction with $x$ in the denominator. We also use the **sum rule** (the derivative of a sum is the sum of the derivatives) and the **constant multiple rule** (a number in front stays in front).

## Step-by-step solution

**Step 1. Rewrite with powers.** The root becomes $\sqrt{x}=x^{1/2}$. The fraction becomes $\dfrac{3}{x^2}=3x^{-2}$. The last term is already a power. So
$$f(x)=2x^{1/2}-3x^{-2}+x^{3/2}.$$

**Step 2. Find the domain.** We check each term.
- The term $x^{1/2}=\sqrt{x}$ needs $x\ge 0$, because a square root of a negative number is not a real number.
- The term $x^{-2}=\dfrac1{x^2}$ needs $x\neq 0$, because we cannot divide by zero.
- The term $x^{3/2}=\sqrt{x}^{\,3}$ needs $x\ge 0$ for the same reason as the root.

All three conditions must hold together. So $x\ge0$ and $x\ne0$, which means $x>0$. The domain is $(0,\infty)$.

**Step 3. Differentiate term by term.**
- For $2x^{1/2}$: the power rule gives $2\cdot\frac12\,x^{-1/2}=x^{-1/2}$.
- For $-3x^{-2}$: the power rule gives $-3\cdot(-2)\,x^{-3}=6x^{-3}$.
- For $x^{3/2}$: the power rule gives $\frac32\,x^{1/2}$.

By the sum rule,
$$f'(x)=x^{-1/2}+6x^{-3}+\frac32 x^{1/2}.$$
Written with roots and fractions this is
$$f'(x)=\frac{1}{\sqrt{x}}+\frac{6}{x^3}+\frac32\sqrt{x}.$$

**Step 4. Domain of the derivative.** Look at the three terms of $f'$.
- $\dfrac1{\sqrt{x}}$ needs $x>0$, because the root must be real and the denominator must not be zero.
- $\dfrac{6}{x^3}$ needs $x\ne0$.
- $\dfrac32\sqrt{x}$ needs $x\ge0$.

Together they give $x>0$. The domain of $f'$ is $(0,\infty)$, which is exactly the domain of $f$.

**Step 5. Compare.** The two domains are equal. Note that $f'$ does not become defined at $x=0$, even though the term $\frac32\sqrt{x}$ alone would allow it.

## Why each step is valid

- Step 1 is valid because $\sqrt{x}=x^{1/2}$ and $\frac1{x^2}=x^{-2}$ are the definitions of fractional and negative exponents. We only changed the way we write the same number.
- Step 2 is valid because the formula for $f$ is a sum, and a sum is defined only where every term is defined.
- Step 3 is valid because the power rule holds for every real exponent, and the sum rule and constant multiple rule allow us to treat each term on its own.
- In the second term, the minus sign in front and the exponent $-2$ multiply to a plus: $(-3)(-2)=+6$. The exponent goes down by one, from $-2$ to $-3$.
- Step 4 is valid for the same reason as Step 2: the derivative is again a sum, so each term must be defined.

## Final answer (in words)

In power form, $f(x)=2x^{1/2}-3x^{-2}+x^{3/2}$. The domain is all $x$ greater than zero, written $(0,\infty)$. The derivative is $f'(x)=x^{-1/2}+6x^{-3}+\frac32x^{1/2}$, which is the same as $\frac1{\sqrt{x}}+\frac6{x^3}+\frac32\sqrt{x}$. The derivative is defined on the same set as the function, the positive numbers.

## Verification

**Check 1: a number from the formula.** At $x=1$ we get $f(1)=2-3+1=0$ and $f'(1)=1+6+\frac32=8.5$.

**Check 2: difference quotients.** The difference quotient is $\dfrac{f(1+h)-f(1)}{h}$. It is the slope of a line through two points of the graph. For $h=0.1$ it equals about $7.7197$. For $h=0.01$ it equals about $8.4124$. For $h=0.001$ it equals about $8.4911$. The values move toward $8.5$. The symmetric quotient $\dfrac{f(1+h)-f(1-h)}{2h}$ with $h=10^{-5}$ gives $8.5000000$ to seven digits. This check does not use the power rule at all, so it is independent.

**Check 3: sign.** Every term of $f'$ is positive for $x>0$, so $f'(x)>0$ on the whole domain. The value $8.5$ is consistent with that.

## Common mistakes

- Differentiating $\sqrt{x}$ or $\frac1{x^2}$ without rewriting first, or using the quotient rule where a power is enough.
- Writing $-3x^{-3}$ instead of $+6x^{-3}$: forgetting to multiply by the exponent $-2$.
- Subtracting one the wrong way, for example turning $x^{-2}$ into $x^{-1}$. Subtracting one from $-2$ gives $-3$.
- Giving the domain as $x\ge0$ because of the roots, and forgetting that $\frac1{x^2}$ forbids $x=0$.
- Checking only one term of $f'$ for the domain. A sum is defined only where every term is defined, so all three terms must be checked.

## How I would explain it in class

First I rewrite the root and the fraction as powers, $x^{1/2}$ and $x^{-2}$, because the power rule only works on powers. Then I differentiate each term by bringing the exponent down and lowering it by one, which gives $x^{-1/2}+6x^{-3}+\frac32x^{1/2}$. The function and its derivative are both defined exactly for $x>0$, since the root and the division by $x^2$ together exclude zero and all negative numbers.
