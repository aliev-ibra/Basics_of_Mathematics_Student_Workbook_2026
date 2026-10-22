# Problem 1

## The original problem

For

$$f(x)=3x^5-2x^3+7x-4$$

find $f'(x)$. Then compute $f'(0)$ and $f'(1)$, determine the signs of the obtained values, and explain what they say about the slope of the tangent line to the graph at these two points.

> **Why this problem:** it reinforces the power rule and connects the value of the derivative at a point with the geometric meaning of the tangent slope.

## What we are looking for

We need a formula for the derivative $f'(x)$ of the given polynomial. After that we evaluate the derivative at $x=0$ and at $x=1$, decide whether each value is positive, negative, or zero, and say what that tells us about the tangent line. A positive derivative means the tangent line goes upward as we move to the right; a negative one means it goes downward.

## The idea we need

The **power rule**: for any real constant $n$, if $g(x)=x^n$, then $g'(x)=n x^{n-1}$. In LaTeX: $\frac{d}{dx}x^n = n x^{n-1}$. We also use the **sum rule** — the derivative of a sum is the sum of the derivatives — and the **constant multiple rule** — a constant factor passes through the derivative unchanged. The derivative of a constant is $0$. Every term of the polynomial is handled separately with these rules. The domain of a polynomial is all real numbers, and its derivative is also defined for all real numbers, so there is no domain restriction to worry about here.

## Step-by-step solution

1. Write the function term by term: $f(x)=3x^5-2x^3+7x-4$. The four terms are $3x^5$, $-2x^3$, $+7x$, and the constant $-4$.
2. Differentiate the first term. By the power rule and constant multiple rule, the derivative of $3x^5$ is $3 \cdot 5x^4 = 15x^4$.
3. Differentiate the second term. The derivative of $-2x^3$ is $-2 \cdot 3x^2 = -6x^2$.
4. Differentiate the third term. The term $7x = 7x^1$ gives $7 \cdot 1x^0 = 7$.
5. Differentiate the constant term. The derivative of the constant $-4$ is $0$, because a constant function does not change.
6. Put the pieces together using the sum rule: $f'(x)=15x^4-6x^2+7$.
7. Evaluate at $x=0$: substitute $x=0$ to get $f'(0)=15\cdot 0^4-6\cdot 0^2+7=7$. This number is greater than $0$, so it is **positive**.
8. Evaluate at $x=1$: substitute $x=1$ to get $f'(1)=15\cdot 1^4-6\cdot 1^2+7=15-6+7=16$. This number is also greater than $0$, so it is **positive**.
9. Interpret geometrically. At $x=0$ the slope of the tangent line is $7$, and at $x=1$ the slope is $16$. In both cases the slope is positive, so the tangent line rises from left to right. The larger value at $x=1$ means the graph is steeper there than at $x=0$.

## Why each step is valid

- Steps 2–5 are valid because the power rule applies to each power $x^n$ individually, and the constant multiple rule lets us keep the coefficient $3$, $-2$, or $7$ in front.
- Step 6 is valid by the sum rule: the derivative of a sum of functions equals the sum of their derivatives, so we may add the four term-derivatives.
- Step 5 is valid because the derivative of any constant $c$ is $0$; a constant function has zero rate of change.
- Steps 7–8 are valid because evaluating a derivative at a point means substituting the number into the formula for $f'(x)$.
- Step 9 is valid because the derivative $f'(a)$ is exactly the slope of the tangent line to the graph of $f$ at the point $(a,f(a))$.

## Final answer (in words)

The derivative of the polynomial is $f'(x)=15x^4-6x^2+7$. At $x=0$ the derivative equals $7$, which is positive, so the tangent line at $(0,f(0))$ slopes upward from left to right with slope $7$. At $x=1$ the derivative equals $16$, which is also positive, so the tangent line at $(1,f(1))$ slopes upward with slope $16$ and is steeper than the tangent at $x=0$.

## Verification

We can check the power-rule application by re-deriving each term: the exponent drops by one and is multiplied by the old exponent, giving $3\cdot5x^4=15x^4$, $-2\cdot3x^2=-6x^2$, and $7\cdot1x^0=7$, with the constant $-4$ vanishing. To check the point values, note that at $x=0$ only the constant term $7$ survives, so $f'(0)=7$; at $x=1$ every power is $1$, so $f'(1)=15-6+7=16$. Both signs are clearly positive, which is consistent with a polynomial whose leading term $15x^4$ dominates for large $|x|$ and which has no negative contributions at these small points.

## Common mistakes

- Forgetting to multiply by the old exponent: writing $3x^4$ instead of $15x^4$ for the first term.
- Dropping the constant term $-4$ entirely instead of giving it derivative $0$.
- Confusing the sign: claiming $f'(0)$ or $f'(1)$ is negative because of the minus signs in the original expression, when those signs belong to the $x^3$ term, which vanishes at $x=0$ and contributes only $-6$ at $x=1$.
- Saying the tangent line "goes up" without connecting it to the sign of the derivative; the geometric statement must be justified by the computed value.

## How I would explain it in class

I would start by writing the polynomial term by term and reminding you that each power differentiates by the power rule: bring the exponent down and subtract one from the exponent. Then I would evaluate at $x=0$ and $x=1$ and point out that both numbers are positive, which means the tangent line at each of these points climbs as we move to the right, and it climbs faster at $x=1$ because $16$ is larger than $7$.
