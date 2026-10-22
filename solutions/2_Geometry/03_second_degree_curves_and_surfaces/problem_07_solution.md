# Problem 07

## The original problem

Determine the type of object described by:

1. $4x^2+9y^2=36$,
2. $x^2-y^2=1$,
3. $x^2-4y=0$,
4. $x^2+y^2+1=0$.

In the last case, explain why there are no real points.

## What we are looking for

We must classify each equation and explain the empty case.

## The idea we need

Divide to canonical form and look at signs. Sum of two positive squares equals positive gives an ellipse (or circle). Difference equals positive gives a hyperbola. One squared variable equals a linear term gives a parabola. Sum of squares equals a negative number has no real solutions.

## Step-by-step solution

1. Divide by $36$: $\frac{x^2}{9}+\frac{y^2}{4}=1$. This is an ellipse with semi-axes $3$ and $2$.

2. $x^2-y^2=1$ is already $\frac{x^2}{1}-\frac{y^2}{1}=1$, a hyperbola.

3. Solve for $y$: $y=\frac{x^2}{4}$. This is a parabola opening upward with vertex $(0,0)$.

4. $x^2+y^2=-1$. For real $x,y$, we have $x^2\ge0$ and $y^2\ge0$, so $x^2+y^2\ge0$. It cannot equal $-1$. No real points.

## Why each step is valid

Dividing an equation by a nonzero constant preserves the solution set. The classification follows from the canonical forms. The nonexistence argument uses that squares of real numbers are nonnegative.

## Final answer (in words)

The four objects are: an ellipse, a hyperbola, a parabola, and an empty set with no real points.

## Verification

For case 4, test $(0,0)$: $0+0+1=1\neq0$. Since $x^2+y^2\ge0$, $x^2+y^2+1\ge1>0$ for all real $x,y$.

## Common mistakes

- Calling case 1 a circle.
- Missing that case 3 is a parabola, not an ellipse.
- Thinking case 4 is a circle of imaginary radius without explaining nonexistence.

## How I would explain it in class

I normalize each equation and compare with the canonical forms. For the last one I use that squares are nonnegative, so the left side is at least $1$. That shows there are no real points.