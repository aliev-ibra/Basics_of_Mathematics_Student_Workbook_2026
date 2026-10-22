# Problem 6

## The original problem

Compute the average value of the function
$$
f(x)=x^2
$$
on the interval $[0,3]$.

Find a point $c\in[0,3]$ for which $f(c)$ is equal to this average value, and interpret the result geometrically.

> **Why this problem:** it gives the integral the interpretation of an average value and connects the numerical result with a level of the function on the graph.

## What we are looking for

We want a single number that represents the function $f(x)=x^2$ over the whole interval $[0,3]$, in the same way that a single number can represent the height of a rectangle standing on that interval. Then we look for a point of the graph at exactly that height, and we explain what the number means when we draw it. The tool is the definite integral, because the integral measures accumulated area and an average is a total divided by a length.

## The idea we need

**Average value of a function.** If $f$ is continuous on $[a,b]$, its average value there is

$$
f_{\text{avg}}=\frac{1}{b-a}\int_a^b f(x)\,dx.
$$

The reason for the factor $\frac{1}{b-a}$ is dimensional: $\int_a^b f(x)\,dx$ is an *area* (function units times length units), and dividing by the length $b-a$ returns the function units. Formally, this is the area under the graph divided by the width of the interval, i.e. the height of the rectangle with the same area.

**A point where the function takes its average value.** The Mean Value Theorem for Integrals says that for a continuous $f$ there is a $c\in[a,b]$ with

$$
f(c)=\frac{1}{b-a}\int_a^b f(x)\,dx=f_{\text{avg}}.
$$

Intuitively: a continuous curve that starts low and ends high must pass through every level in between, so it must pass through the average level.

**The definite integral as accumulated area.** Here

$$
\int_0^3 x^2\,dx=\left[\frac{x^3}{3}\right]_0^3=9,
$$

so the region under the parabola $y=x^2$ between $0$ and $3$ has area $9$, and the average value is $9/3=3$.

## Step-by-step solution

1. **Identify the data.** $f(x)=x^2$ on the interval $[a,b]=[0,3]$, so $b-a=3$.

2. **Write the average-value formula.**

$$
f_{\text{avg}}=\frac{1}{3}\int_0^3 x^2\,dx.
$$

3. **Compute the integral.** The antiderivative of $x^2$ is $\frac{x^3}{3}$, so by the Fundamental Theorem of Calculus

$$
\int_0^3 x^2\,dx=\left[\frac{x^3}{3}\right]_0^3=\frac{27}{3}-\frac{0}{3}=9.
$$

4. **Divide by the length of the interval.**

$$
f_{\text{avg}}=\frac{9}{3}=3.
$$

5. **Find the point $c$.** We need $f(c)=c^2$ to equal $3$:

$$
c^2=3 \;\Longrightarrow\; c=\sqrt{3}\ \text{ or }\ c=-\sqrt{3}.
$$

Only $c=\sqrt{3}\approx1{,}732$ lies in $[0,3]$, so

$$
c=\sqrt{3}.
$$

6. **Check that such a point exists and is unique.** The function $x^2$ is continuous on $[0,3]$ and increasing there, so the equation $x^2=3$ has exactly one solution in $[0,3]$. The Mean Value Theorem for Integrals guarantees its existence in general.

7. **Geometric interpretation: the equal-area rectangle.** The area under $y=x^2$ on $[0,3]$ is $9$, so the rectangle with base $3$ (from $x=0$ to $x=3$) and height $3$ has the same area $3\cdot3=9$. The horizontal line $y=3$ therefore "replaces" the region under the parabola by an equal-area rectangle — that is the geometric meaning of the average value.

8. **Geometric interpretation: the two equal wings.** The line $y=3$ meets the parabola at $x=\sqrt{3}$, and together the line and the curve enclose two "wings", one on each side of $c$. Their areas are

$$
\text{left wing}=\int_0^{\sqrt{3}}(3-x^2)\,dx
=\left[3x-\frac{x^3}{3}\right]_0^{\sqrt{3}}=3\sqrt{3}-\sqrt{3}=2\sqrt{3},
$$

$$
\text{right wing}=\int_{\sqrt{3}}^{3}(x^2-3)\,dx
=\left[\frac{x^3}{3}-3x\right]_{\sqrt{3}}^{3}=(9-9)-(\sqrt{3}-3\sqrt{3})=2\sqrt{3}.
$$

The two wings have exactly the same area, $2\sqrt{3}\approx3{,}46$. This is the picture behind the Mean Value Theorem: the average level is the level at which the curve sits "balanced" with respect to the area above and below it.

## Why each step is valid

- The average-value formula is the area under the curve divided by the width of the interval, so it is the height of the rectangle with the same area; the division by $b-a=3$ is what makes the units right.
- $f(x)=x^2$ is a polynomial, hence continuous on $[0,3]$, so the integral exists and the Mean Value Theorem for Integrals applies.
- $\frac{x^3}{3}$ is an antiderivative of $x^2$ because $\left(\frac{x^3}{3}\right)'=x^2$, so the Fundamental Theorem of Calculus justifies evaluating it at $0$ and $3$.
- The equation $c^2=3$ has two real roots, but only $\sqrt{3}\approx1{,}73$ belongs to $[0,3]$; a candidate outside the interval is not admissible.
- The two wings are computed with the upper curve minus the lower curve in each case, so both integrals come out positive and represent genuine areas.
- The equality of the two wings is not a coincidence: it is exactly the statement $\int_0^3(3-x^2)\,dx=9-9=0$, i.e. the signed area between the line and the curve cancels over the whole interval.
- Uniqueness of $c$ on $[0,3]$ follows from $x^2$ being strictly increasing on $[0,3]$ (its derivative $2x>0$ for $x>0$).

## Final answer (in words)

The average value of $f(x)=x^2$ on the interval $[0,3]$ is **$3$**.

There is a point $c=\sqrt{3}\approx1{,}732$ in $[0,3]$ at which the function takes exactly this value, since $f(\sqrt{3})=(\sqrt{3})^2=3$.

Geometrically, the area under the parabola on $[0,3]$ is $9$, so the rectangle of base $3$ and height $3$ has exactly the same area; and the horizontal line $y=3$ together with the parabola encloses two equal "wings", one on each side of $x=\sqrt{3}$, each of area $2\sqrt{3}\approx3{,}46$.

$$
\boxed{f_{\text{avg}}=\frac{1}{3}\int_0^3x^2\,dx=3,\qquad c=\sqrt{3}}
$$

## Verification

- **Recompute the integral.** $\int_0^3x^2\,dx=\left[\frac{x^3}{3}\right]_0^3=27/3=9$, and $9/3=3$. ✓
- **Check the function value.** $f(\sqrt{3})=(\sqrt{3})^2=3=f_{\text{avg}}$, and $c=\sqrt{3}\in[0,3]$. ✓
- **Check the equal-area claim numerically.** Left wing $\int_0^{\sqrt3}(3-x^2)\,dx=2\sqrt3\approx3{,}4641$; right wing $\int_{\sqrt3}^3(x^2-3)\,dx=2\sqrt3\approx3{,}4641$. They agree, as they must because $\int_0^3(3-x^2)\,dx=0$.
- **Check the total area.** The region under the parabola splits into the part below the line, $9-2\sqrt{3}\approx5{,}536$, and the right wing, $2\sqrt{3}\approx3{,}464$; their sum is $9$, the independently computed area under the curve. ✓
- **Bounds check.** A continuous function on a closed interval has its minimum and maximum inside it, so the average must lie between them: $f_{\min}=f(0)=0$ and $f_{\max}=f(3)=9$, and indeed $0<3<9$. ✓
- **Units check.** The integral has units of "function units × length", dividing by the length $3$ gives "function units", so the answer $3$ is in the units of $f$. ✓
- **Location check.** Sampling $f$ at $x=0,0{,}75,1{,}5,2{,}25,3$ gives $0,\ 0{,}5625,\ 2{,}25,\ 5{,}0625,\ 9$; the level $3$ is crossed between $x=1{,}5$ and $x=2{,}25$, consistent with $c=\sqrt3\approx1{,}73$.

## Common mistakes

- Forgetting the factor $\frac{1}{b-a}$ and answering $9$ (the area) instead of $3$ (the average value).
- Computing the average of the endpoint values $\frac{f(0)+f(3)}{2}=\frac{9}{2}$, which is a trapezoid approximation and is wrong here because $f$ is not linear.
- Choosing $c=-\sqrt{3}$ because it solves $c^2=3$, forgetting that $c$ must lie in $[0,3]$.
- Dividing by $2$ instead of by $3$ because the interval $[0,3]$ "has length $2$" — the length is $3-0=3$.
- Claiming that the line $y=3$ cuts the region under the parabola into two equal halves; what is equal are the two wings between the line and the curve (on the left and on the right of $c$), not the two parts of the region under the curve.
- Not explaining the geometric meaning, so the number $3$ is left as a result with no interpretation.

## How I would explain it in class

The average value of a function on an interval is the area under its graph divided by the width of the interval, so here it is $\frac{1}{3}\int_0^3x^2dx=\frac{1}{3}\cdot9=3$. Since the parabola is continuous and increases from $0$ to $9$, it must cross the level $3$, and indeed $f(\sqrt3)=3$, so $c=\sqrt3$. Geometrically, the rectangle of base $3$ and height $3$ has the same area $9$ as the region under the parabola, and the line $y=3$ forms with the curve two equal wings of area $2\sqrt3$ on either side of that point.
