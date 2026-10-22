# Problem 9

## The original problem

Compute
$$\int_{-1}^{2}x\,dx.$$
Then separately compute the areas of the parts of the graph below and above the $x$-axis and explain the difference between the definite integral and geometric area.

> **Why this problem:** it clarifies the difference between signed accumulation and area.

## What we are looking for

We want one number, the definite integral of $x$ from $-1$ to $2$. We also want two other numbers: the area of the piece of the graph under the $x$-axis and the area of the piece above it. Then we explain why the integral and the total area are different numbers.

## The idea we need

A **definite integral** $\int_a^b f(x)\,dx$ is the signed accumulation of $f$ from $a$ to $b$. Signed means that the part of the graph above the $x$-axis counts as positive and the part below the $x$-axis counts as negative.

**Geometric area** is different. It is always positive, so every piece counts as a positive amount.

To compute the integral we use the Fundamental Theorem of Calculus. If $F$ is an antiderivative of $f$, then $\int_a^b f(x)\,dx=F(b)-F(a)$.

## Step-by-step solution

**Step 1. Find an antiderivative.** An antiderivative of $x$ is $F(x)=\frac{x^2}{2}$, because its derivative is $x$.

**Step 2. Subtract the values at the ends.**
$$\int_{-1}^{2}x\,dx=\frac{2^2}{2}-\frac{(-1)^2}{2}=2-\frac12=\frac32.$$

**Step 3. Describe the graph.** The graph of $y=x$ is a straight line through the origin. It crosses the $x$-axis at $x=0$. On $[-1,0]$ the line is below the axis, and on $[0,2]$ it is above the axis.

**Step 4. Area below the axis.** On $[-1,0]$ the graph and the axis form a right triangle with base $1$ and height $1$. Its area is $\frac12\cdot1\cdot1=\frac12$.

**Step 5. Area above the axis.** On $[0,2]$ the graph and the axis form a right triangle with base $2$ and height $2$. Its area is $\frac12\cdot2\cdot2=2$.

**Step 6. Compare.** The total geometric area is $\frac12+2=\frac52$. The integral counts the lower piece with a minus sign, so it equals $2-\frac12=\frac32$.

## Why each step is valid

- Step 1 is valid because the derivative of $\frac{x^2}{2}$ is $x$.
- Step 2 is valid because the Fundamental Theorem of Calculus says that the definite integral equals $F(b)-F(a)$.
- Steps 3 to 5 are valid because the area of a right triangle is half of base times height, and the line $y=x$ has height equal to the distance from the axis.
- Step 6 is valid because the integral adds signed pieces, while area adds only positive pieces.

## Final answer (in words)

The definite integral is three halves: $\int_{-1}^{2}x\,dx=\frac32$. The part below the axis has area one half, and the part above the axis has area two. The integral is the upper area minus the lower area, $2-\frac12=\frac32$, but the geometric area is their sum, $\frac52$.

## Verification

**Check 1: the geometry.** The signed total from the triangles is $2-\frac12=\frac32$, which agrees with the formula.

**Check 2: differentiate the antiderivative.** The derivative of $\frac{x^2}{2}$ is $x$, so $F$ is a correct antiderivative.

**Check 3: the average value.** The line $y=x$ has height $-1$ at the left end and $2$ at the right end, so its average height on the interval is $\frac{-1+2}{2}=\frac12$. The interval has length $3$, and $\frac12\cdot3=\frac32$.

## Common mistakes

- Saying that the integral is the area. It is the area only when the graph is not below the axis.
- Subtracting in the wrong order, $F(a)-F(b)$, which gives $-\frac32$.
- Using $-1$ in the formula without brackets, so that $(-1)^2$ becomes $-1$ by mistake.
- Computing the whole area as $\frac32$ and forgetting that the lower piece must be added as a positive number.

## How I would explain it in class

The integral $\int_{-1}^{2}x\,dx$ equals $\frac{2^2}{2}-\frac{(-1)^2}{2}=\frac32$, and this number is a signed total. The graph has a small triangle of area $\frac12$ below the axis and a larger triangle of area $2$ above it, so the integral is $2-\frac12=\frac32$ while the geometric area is $2+\frac12=\frac52$. The integral subtracts what lies below the axis, and the area adds it.
