# Problem 10

## The original problem

For
$$f(x)=x^2-3x+1$$
find the equation of the tangent line at the point with $x=2$. Give the point of tangency, the value $f'(2)$, the equation of the line, and verify that the point lies on the obtained tangent line.

> **Why this problem:** it combines the derivative and the equation of a line into a complete geometric problem.

## What we are looking for

We want the straight line that touches the parabola $y=x^2-3x+1$ at the place where $x=2$. A line needs two things: a point on it and a slope. The point is the point of tangency, which has coordinates $(2,f(2))$. The slope is the derivative $f'(2)$. We must report the point, the slope, the equation, and a check.

## The idea we need

The **geometric meaning of the derivative**. The number $f'(a)$ is the slope of the tangent line to the graph at the point $(a,f(a))$.

The **point-slope form** of a line: the line through the point $(x_0,y_0)$ with slope $m$ is $y-y_0=m(x-x_0)$.

For the derivative itself we use the power rule, which says $\frac{d}{dx}x^n=nx^{n-1}$. We also use the sum rule and the constant multiple rule. They say that we differentiate term by term and constant factors stay in front. The derivative of a constant is $0$.

## Step-by-step solution

1. Find the point of tangency. Its first coordinate is $x_0=2$. Its second coordinate is
$$f(2)=2^2-3\cdot2+1=4-6+1=-1.$$
So the point is $(2,-1)$.
2. Differentiate term by term. The derivative of $x^2$ is $2x$. The derivative of $-3x$ is $-3$. The derivative of the constant $1$ is $0$. Therefore
$$f'(x)=2x-3.$$
3. Evaluate at $x=2$: $f'(2)=2\cdot2-3=1$. So the slope of the tangent line is $m=1$.
4. Write the point-slope equation with $(x_0,y_0)=(2,-1)$ and $m=1$:
$$y-(-1)=1\cdot(x-2),\qquad\text{that is}\qquad y+1=x-2.$$
5. Solve for $y$:
$$y=x-3.$$
6. Check the point. Put $x=2$ into $y=x-3$. We get $y=-1$. This is the second coordinate of the point $(2,-1)$, so the point lies on the line.

## Why each step is valid

- Step 1 is valid because the tangent line touches the graph, so it must pass through the point of the graph with $x=2$, and that point has height $f(2)$.
- Step 2 is valid because the power rule, the sum rule and the constant multiple rule apply to every polynomial term.
- Step 3 is valid because the slope of the tangent line at $x=2$ is by definition the value $f'(2)$ of the derivative at that point.
- Step 4 is valid because a non-vertical line is fully determined by one of its points and its slope, and the point-slope form says exactly this.
- Step 6 is valid because a point lies on a line exactly when its coordinates satisfy the equation of the line.

## Final answer (in words)

The point of tangency is $(2,-1)$. The derivative is $f'(x)=2x-3$, so the slope is $f'(2)=1$. The tangent line is $y=x-3$. The point $(2,-1)$ lies on it, because $2-3=-1$.

## Verification

**Check 1: the point.** Substituting $x=2$ in $y=x-3$ gives $-1$, which equals $f(2)=-1$. So the line and the parabola meet at $x=2$.

**Check 2: a different method.** A tangent line to a parabola meets it in exactly one point. Set the parabola equal to the line:
$$x^2-3x+1=x-3\quad\Longrightarrow\quad x^2-4x+4=0\quad\Longrightarrow\quad (x-2)^2=0.$$
There is one solution only, $x=2$, and it is a double root. This is the algebraic sign of tangency, and it did not use the derivative. So the line $y=x-3$ is indeed the tangent.

**Check 3: a nearby number.** At $x=2.1$ the parabola gives $f(2.1)=4.41-6.3+1=-0.89$. The line gives $-0.9$. They differ by only $0.01$, which is $(0.1)^2$. Close to the point of tangency the line is very close to the curve.

## Common mistakes

- Using $f(2)$ as the slope, or $f'(2)$ as the height of the point. The value $f(2)$ is a height, and $f'(2)$ is a slope.
- Writing $y=1\cdot(x-2)$ and forgetting to add the height $-1$ of the point.
- Making a sign error with the point $(2,-1)$: $y-(-1)$ is $y+1$, not $y-1$.
- Forgetting to check that the point lies on the line.

## How I would explain it in class

A tangent line needs a point and a slope, so I first find the point $(2,f(2))=(2,-1)$ and then the slope $f'(2)=1$ from the derivative $2x-3$. The point-slope form $y+1=1\cdot(x-2)$ gives the line $y=x-3$. As a check, $x=2$ gives $y=-1$ on the line, and the equation $x^2-3x+1=x-3$ has only the double root $x=2$, which shows the line really touches the parabola.
