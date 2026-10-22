# Problem 2

## The original problem

For $f(x)=x^2-4x+1$, find the minimum using the derivative. Compare the result with the vertex form and explain why both approaches lead to the same point.

## What we are looking for

We want to locate the minimum point of a parabola using the derivative, then confirm it matches the vertex obtained by completing the square, and understand why the two methods agree.

## The idea we need

A differentiable function has a local extremum at a point where its derivative is zero, provided the derivative changes sign there. For a parabola opening upward, the derivative is zero at the vertex and changes from negative to positive, so the critical point is a minimum. The vertex form $a(x-h)^2+k$ places the vertex at $(h,k)$. Both methods describe the same geometric point because the vertex is where the tangent is horizontal, which is exactly where the derivative vanishes.

## Step-by-step solution

1. The function is a polynomial, so its domain is all real numbers $\mathbb{R}$ and it is differentiable everywhere.

2. Compute the first derivative:

   $$f'(x)=2x-4.$$

3. Find the critical point by setting the derivative to zero:

   $$2x-4=0 \implies x=2.$$

4. Determine the sign of the derivative around $x=2$:
   - For $x<2$, we have $2x-4<0$, so $f'(x)<0$ and $f$ is decreasing.
   - For $x>2$, we have $2x-4>0$, so $f'(x)>0$ and $f$ is increasing.

   The derivative changes from negative to positive at $x=2$, so by the first-derivative test, $f$ has a local minimum at $x=2$.

5. Compute the function value at the minimum:

   $$f(2)=2^2-4\cdot2+1=4-8+1=-3.$$

   So the minimum point is $(2,-3)$.

6. Now write the function in vertex form by completing the square:

   $$f(x)=x^2-4x+1=(x^2-4x+4)-4+1=(x-2)^2-3.$$

   The vertex form is $(x-2)^2-3$, so the vertex is at $(2,-3)$.

7. Comparison: the derivative method gives the minimum at $(2,-3)$, and the vertex form also gives the vertex at $(2,-3)$. Both approaches lead to the same point.

## Why each step is valid

- Differentiating a polynomial term by term is valid because polynomials are differentiable on all of $\mathbb{R}$.
- Setting $f'(x)=0$ finds the only critical point because a quadratic has a linear derivative with exactly one zero.
- The sign change of $f'$ from negative to positive at $x=2$ proves a local minimum by the first-derivative test.
- Completing the square is an algebraic rewrite that does not change the function, so the vertex read from $(x-2)^2-3$ is the same point as the critical point from the derivative.

## Final answer (in words)

The function has a minimum at $x=2$, with value $f(2)=-3$. The minimum point is $(2,-3)$. The vertex form $(x-2)^2-3$ confirms the same vertex $(2,-3)$, because both methods identify the point where the tangent to the parabola is horizontal.

## Verification

Compute the second derivative:

$$f''(x)=2>0.$$

Since $f''(2)=2>0$, the second-derivative test confirms that $x=2$ is a local minimum. Additionally, $f(1)=1-4+1=-2$ and $f(3)=9-12+1=-2$, both greater than $f(2)=-3$, which is consistent with a minimum at $x=2$.

## Common mistakes

- Forgetting to compute the function value at $x=2$ and reporting only the $x$-coordinate of the minimum.
- Claiming the derivative method and vertex form give different points, when they must agree because both describe the same horizontal tangent.
- Completing the square incorrectly, for example writing $(x-2)^2+1$ instead of $(x-2)^2-3$.

## How I would explain it in class

I take the derivative of the parabola and set it to zero, which gives me $x=2$ as the only critical point. Since the derivative changes from negative to positive there, this is the bottom of the parabola. Completing the square puts the same function into $(x-2)^2-3$, which visibly shows the vertex at $(2,-3)$, so both methods point to the same place.
