# Problem 07

## The original problem
Compute
$$\lim_{x\to3}\frac{x^2-4x+3}{x-3}.$$
Explain why the value of the function at $x=3$ is not needed to compute the limit.

## What we are looking for
We want the value that the function approaches as $x$ gets closer and closer to $3$, without necessarily equaling $3$. Direct substitution gives the indeterminate form $0/0$, so we need to factor and cancel. We also need to explain why the function's value at $x=3$ does not matter for the limit.

## The idea we need
This is a limit at a point, specifically a two-sided limit as $x\to 3$. Direct substitution gives $\frac{0}{0}$, an indeterminate form. The standard technique is to factor the numerator and cancel the common factor with the denominator. The cancellation is valid because a limit only concerns values of $x$ near but not equal to $3$, so dividing by $x-3$ (which is nonzero when $x\neq 3$) does not change the limit. Formally, if two functions agree for all $x$ in a neighborhood of $a$ except possibly at $a$ itself, then they have the same limit as $x\to a$.

## Step-by-step solution
1. Write the expression:
$$f(x)=\frac{x^2-4x+3}{x-3}.$$
2. Direct substitution at $x=3$ gives $\frac{3^2-4(3)+3}{3-3}=\frac{0}{0}$, which is indeterminate, so we cannot substitute directly.
3. Factor the numerator:
$$x^2-4x+3=(x-1)(x-3).$$
4. Rewrite the fraction:
$$f(x)=\frac{(x-1)(x-3)}{x-3}.$$
5. For $x\neq 3$, cancel the common factor $(x-3)$:
$$f(x)=x-1\qquad (x\neq 3).$$
6. Now compute the limit by substitution, valid because $x-1$ is continuous everywhere:
$$\lim_{x\to3}f(x)=\lim_{x\to3}(x-1)=3-1=2.$$

## Why the value at $x=3$ is not needed
The original function $f(x)=\frac{x^2-4x+3}{x-3}$ is undefined at $x=3$ because the denominator is zero. However, a limit as $x\to3$ only looks at values of $x$ that are close to $3$ but not equal to $3$. The simplified function $x-1$ agrees with $f(x)$ at every such point, so the two have the same limit as $x\to3$. Whether or not $f(3)$ is defined, and whatever value it might have, does not affect $\lim_{x\to3}f(x)$.

## Why each step is valid
Step 2 confirms that direct substitution fails, motivating the factorization. Step 3 is a standard factorization of a quadratic. Step 5 is valid because we only cancel for $x\neq 3$, which is exactly the domain relevant to the limit $x\to3$. Step 6 uses the continuity of the polynomial $x-1$ and the fact that a continuous function's limit at a point equals its value there.

## Final answer (in words)
The function approaches the value $2$ as $x$ approaches $3$ from either side. Even though the function is undefined at $x=3$, the limit exists and equals $2$ because the factor $(x-3)$ cancels, leaving the continuous expression $x-1$.

## Verification
Take $x=3.001$: $\frac{3.001^2-4(3.001)+3}{3.001-3}=\frac{9.006001-12.004+3}{0.001}=\frac{0.002001}{0.001}=2.001$. Take $x=2.999$: $\frac{2.999^2-4(2.999)+3}{2.999-3}=\frac{8.994001-11.996+3}{-0.001}=\frac{0.001999}{-0.001}=1.999$. Both sides approach $2$, confirming the limit.

## Common mistakes
- Substituting $x=3$ directly and concluding the limit does not exist because of $0/0$, without factoring.
- Cancelling $(x-3)$ and then forgetting that this is valid only for $x\neq 3$, or thinking the function becomes defined at $x=3$.
- Confusing the limit with the function value at $x=3$ (the function is undefined there, but the limit is $2$).

## How I would explain it in class
If you plug in three, you get zero over zero, which tells you nothing, so you factor the top and find an $(x-3)$ that matches the bottom. Since the limit only cares about $x$ close to three but not equal to three, you can cancel that factor and you are left with $x-1$. Plugging in three then gives two, and it does not matter that the original function is not even defined at three.
