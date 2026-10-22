# Problem 4

## The original problem

Find the area of the region bounded by the graphs
$$
y=x
$$
and
$$
y=x^2.
$$

First find the intersection points and justify which function is greater on the relevant interval.

> **Why this problem:** it teaches that before integrating, one must first determine the geometry of the region and the correct order of the functions.

## What we are looking for

Two curves cut each other at certain points, and between those points they enclose a region whose area we must compute. Before touching the integral we have to describe the region: find the intersection points, and decide on each piece which curve is the upper one. Only then can we write the area integral with the correct order of subtraction. Getting the order wrong is the most common mistake in this type of problem.

## The idea we need

**Step 1 — the intersection points.** The curves meet where $x=x^2$, i.e. where

$$
x^2-x=0 \;\Longrightarrow\; x(x-1)=0 \;\Longrightarrow\; x=0 \ \text{or}\ x=1.
$$

So the curves cross at the points $(0,0)$ and $(1,1)$.

**Step 2 — which curve is on top.** On the interval $[0,1]$ the difference between the line and the parabola is

$$
x-x^2=x(1-x),
$$

which is positive for $0<x<1$. So on the whole relevant interval the line $y=x$ lies above the parabola $y=x^2$.

**Step 3 — the area as an integral.** The area between two curves is the definite integral of "upper minus lower" over the interval where they enclose a region:

$$
A=\int_{0}^{1}\bigl(\underbrace{x}_{\text{upper}}-\underbrace{x^2}_{\text{lower}}\bigr)\,dx.
$$

The definite integral $\int_a^b f(x)\,dx$ is the accumulated area between the graph of $f$ and the $x$-axis; when the integrand is the difference of two curves it is exactly the area of the region between them.

**Step 4 — the antiderivative.**

$$
\int (x-x^2)\,dx=\frac{x^2}{2}-\frac{x^3}{3},
$$

evaluated at the two intersection abscissas $1$ and $0$.

## Step-by-step solution

1. **Find the intersection points.** Set the two expressions for $y$ equal:

$$
x=x^2 \;\Longrightarrow\; x(x-1)=0 \;\Longrightarrow\; x_1=0,\ x_2=1.
$$

Substituting back, $y=0$ and $y=1$, so the crossing points are $(0,0)$ and $(1,1)$.

2. **Note where the region is bounded.** For $x>1$ we have $x^2>x$, but that part of the plane between the curves is unbounded, so it does not enclose a finite region. The region bounded by the two graphs is the one over $[0,1]$.

3. **Justify the order of the curves.** On $[0,1]$,

$$
x-x^2=x(1-x)>0 \quad\text{for } 0<x<1,
$$

so the line is the upper curve and the parabola is the lower one everywhere on the interval.

4. **Write the area integral.**

$$
A=\int_{0}^{1}(x-x^2)\,dx.
$$

5. **Compute it.** Antiderivatives: $\int x\,dx=\frac{x^2}{2}$ and $\int x^2\,dx=\frac{x^3}{3}$.

$$
A=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_{0}^{1}
=\left(\frac{1}{2}-\frac{1}{3}\right)-\left(0-0\right)
=\frac{3-2}{6}=\frac{1}{6}.
$$

6. **Describe the region.** It is a curved "cap" inside the unit square $0\le x\le1$, $0\le y\le1$: the parabola bends down from $(0,0)$ to $(1,1)$ and the straight line closes it off from above. Its area is $1/6\approx0{,}167$ of a unit square, which is visibly less than the triangle under the line, whose area is $1/2$.

## Why each step is valid

- Intersection points are found by equating the two formulas for $y$, because a point belongs to both graphs exactly when both give the same $y$ for the same $x$.
- The equation $x(x-1)=0$ has exactly the two solutions $x=0$ and $x=1$, so the region between the curves over $[0,1]$ is the only bounded one.
- The sign test $x(1-x)>0$ on $(0,1)$ is valid because both factors are positive there, and it shows rigorously which curve is on top; a picture alone would not be a proof.
- The formula $\int_a^b(\text{upper}-\text{lower})\,dx$ holds because the area under the upper curve equals the area under the lower curve plus the area between them, so subtracting the two integrals leaves exactly the region between them.
- The Fundamental Theorem of Calculus (part 2) says that the definite integral equals the antiderivative evaluated at the endpoints, which is what we use in the last computation.

## Final answer (in words)

The two curves meet at the points $(0,0)$ and $(1,1)$, and on the interval from $0$ to $1$ the line $y=x$ lies above the parabola $y=x^2$.

The area of the bounded region is

$$
\boxed{\frac{1}{6}\ \text{square units}\;\approx\;0{,}1667}.
$$

## Verification

- **Independent split of the integral.** The area under the line $y=x$ on $[0,1]$ is $\frac12$ (it is a triangle of base $1$ and height $1$), and the area under the parabola $y=x^2$ on $[0,1]$ is $\frac13$ (standard, $\int_0^1x^2dx=\frac13$). Their difference is $\frac12-\frac13=\frac16$, the same value as the direct computation.
- **Numerical check by Simpson's rule** with the midpoint $x=0.5$: $A\approx\frac{1}{6}\left[f(0)+4f(0.5)+f(1)\right]$ where $f(x)=x-x^2$, so $A\approx\frac16\left(0+4\cdot0.25+0\right)=\frac16$. ✓
- **Magnitude sanity check.** The region lies inside the unit square, so its area must be less than $1$; and it lies below the line, so it must be less than the triangle's area $\frac12$. The value $\frac16\approx0.167$ satisfies both.
- **Shape sanity check.** The region is a thin cap: at $x=0.5$ the gap between the curves is $0.5-0.25=0.25$, i.e. about a quarter of the unit width, and the gap vanishes at both ends. A cap of that shape over a base of length $1$ with average height about $1/6$ is exactly what we computed.
- **Boundary check.** At $x=0$ and $x=1$ the integrand $x-x^2$ is $0$, which is correct: the region has zero height at both intersection points.

## Common mistakes

- Integrating in the wrong order, $\int_0^1(x^2-x)\,dx$, which gives $-\frac16$; the integral of a negative quantity cannot be an area, and the sign error is the signal that the order is wrong.
- Forgetting to find the intersection points and integrating from $0$ to $10$ or from $0$ to $2$, which describes a different (or no) region.
- Assuming "the parabola is above the line" without checking; the answer reverses outside $[0,1]$.
- Reporting $\frac{1}{3}$ (the area under the parabola) or $\frac{1}{2}$ (the area under the line) instead of the difference.
- Forgetting to evaluate the antiderivative at the lower limit $0$, writing $\frac12-\frac13$ and stopping, or dropping the $\left[\,\right]_0^1$ notation and so not showing the limits.

## How I would explain it in class

Before integrating I always draw the picture and find the intersection points, here $x=0$ and $x=1$, because outside that interval the region is not bounded. The test $x-x^2=x(1-x)>0$ tells me the line is the upper curve on $[0,1]$, so the area is $\int_0^1(x-x^2)\,dx$. Evaluating the antiderivative $\frac{x^2}{2}-\frac{x^3}{3}$ at $0$ and $1$ gives $\frac12-\frac13=\frac16$, and indeed the area under the line minus the area under the parabola gives the same number.
