# Problem 2

## The original problem

A rectangle has perimeter $40$.

1. Write its area as a function of the length of one side.
2. Determine the domain of this function resulting from the geometry of the problem.
3. Find the dimensions that give the maximum area.
4. Justify that the point found actually gives a maximum.

> **Why this problem:** it teaches the complete optimization scheme: model → domain → derivative → verification and interpretation of the maximum.

## What we are looking for

We must find the rectangle with the largest possible area among all rectangles whose perimeter is $40$. The work splits into four parts: first we write the area as a function of one side only, then we say which values of that side are physically possible, then we locate the best value with a derivative, and finally we prove that the best value really is the largest one and not just a local bump. The perimeter condition is what ties the two sides together.

## The idea we need

A rectangle has two side lengths; call them $x$ and $y$. The perimeter condition is a constraint on both variables:

$$
2x+2y=40 \quad\Longleftrightarrow\quad y=20-x.
$$

Only one variable is free, so we solve the constraint for $y$ and substitute it into the area $A=xy$. The result is the objective function

$$
A(x)=x(20-x)=20x-x^2,
$$

and the geometry of the rectangle (both sides must be positive) gives the domain

$$
0<x<20.
$$

The maximum of a continuous function on a closed interval is found at a **critical point** (where the derivative vanishes) or at an **endpoint**. That is Fermat's theorem for interior points together with the Extreme Value Theorem for the endpoints. So we solve

$$
A'(x)=20-2x=0 \quad\Longrightarrow\quad x=10,
$$

and then check the endpoints $x=0$ and $x=20$. The second derivative

$$
A''(x)=-2<0
$$

tells us the graph bends downwards everywhere, so the critical point is a maximum.

Units: the perimeter is given as the bare number $40$. We use it as $40$ length units; if the perimeter is meant to be $40\ \mathrm{m}$, then the area answer is $100\ \mathrm{m^2}$.

## Step-by-step solution

1. **Introduce the variables.** Let $x$ be the length of one side (in length units) and $y$ the length of the other side. Both must be positive.

2. **Write the constraint.** The perimeter of a rectangle is $2x+2y$, so the condition "perimeter $40$" is

$$
2x+2y=40 \quad\Longrightarrow\quad y=20-x.
$$

3. **Write the objective function.** The area is $A=xy$. Substituting the constraint,

$$
A(x)=x(20-x)=20x-x^2.
$$

4. **Determine the domain.** A side length must be positive: $x>0$, and also $y=20-x>0$, which means $x<20$. Hence

$$
x\in(0,20).
$$

(If we prefer a closed interval for the extreme value theorem, we may extend $A$ to $[0,20]$; the added endpoints correspond to a degenerate rectangle of area $0$.)

5. **Differentiate.** The rate of change of area with respect to $x$ is

$$
A'(x)=20-2x.
$$

6. **Solve the critical equation.**

$$
A'(x)=0 \quad\Longrightarrow\quad 20-2x=0 \quad\Longrightarrow\quad x=10.
$$

Then $y=20-10=10$.

7. **Check the type of the extremum with the second derivative.**

$$
A''(x)=-2.
$$

Since $A''(10)=-2<0$ for every $x$, the function is concave down on the whole domain and the critical point is a local maximum.

8. **Check the endpoints.** The area of a degenerate rectangle is $0$:

$$
A(0)=0,\qquad A(20)=20\cdot0=0.
$$

Both endpoint values are far below $A(10)$.

9. **Evaluate the maximum area.**

$$
A(10)=10\cdot(20-10)=100.
$$

10. **Interpretation.** The rectangle must be a square: equal sides. The perimeter $40$ splits into four equal sides of $10$, which is exactly the square.

## Why each step is valid

- The perimeter of a rectangle with sides $x,y$ is $2x+2y$, because the opposite sides have equal lengths and each side is counted twice when walking around the figure.
- Solving the constraint for $y$ is legitimate because the constraint is a line, so for every admissible $x$ there is exactly one $y$; the geometry becomes a one-variable problem.
- The domain comes from the geometry: a rectangle with a side of length $0$ does not exist, and if $x\ge20$ then $y\le0$, which is not a length. This is why the domain is not "all real numbers".
- A maximum of a differentiable function on the interior of an interval must satisfy $A'(x)=0$ (Fermat's theorem), so the only candidates are the critical point and, at the ends of the interval, the endpoints themselves.
- $A''(x)=-2<0$ everywhere means the graph is concave down; equivalently, $A$ is increasing before $x=10$ and decreasing after it, so $x=10$ is a maximum and not a minimum.
- Comparing with the endpoints (or invoking the Extreme Value Theorem on the continuous function $A$ on the closed interval $[0,20]$) turns the local maximum into a global one.

## Final answer (in words)

The area as a function of one side $x$ is $A(x)=x(20-x)=20x-x^2$, defined for $0<x<20$.

The largest area is **$100$ square units** (i.e. $100\ \mathrm{m^2}$ if the perimeter is $40$ metres), and it is attained by the rectangle with sides

$$
x=10,\qquad y=10,
$$

that is, by a **square of side $10$**.

$$
\boxed{A(x)=x(20-x),\quad x\in(0,20),\quad A_{\max}=100\ \text{at}\ x=y=10}
$$

## Verification

- **Evaluate the objective at all candidates.** $A(10)=10\cdot10=100$, $A(0)=0$, $A(20)=0$. The critical point beats both endpoints by a wide margin.
- **Check the second derivative.** $A''(10)=-2<0$, confirming a maximum.
- **Independent algebraic check.** Completing the square gives

$$
A(x)=20x-x^2=100-(x-10)^2.
$$

Since $(x-10)^2\ge0$ for every real $x$, we immediately get $A(x)\le100$, with equality only at $x=10$. This proves the maximum globally without any calculus, and it confirms the derivative answer.
- **Check the constraint.** With $x=y=10$ the perimeter is $2\cdot10+2\cdot10=40$, exactly as required.
- **Check the units.** Lengths in length units give area in squared length units, so $10\times10=100$ is consistent.
- **Sanity check against a neighbouring rectangle.** $x=8$ gives $A=8\cdot12=96$ and $x=12$ gives $A=12\cdot8=96$: both are smaller than $100$, as the maximum requires.

## Common mistakes

- Forgetting the factor $2$ in the perimeter and writing $x+y=40$ instead of $2x+2y=40$; this changes the answer to $x=y=20$ and $A=400$.
- Using the whole real line as the domain, which ignores that a side length cannot be $0$ or negative.
- Finding the critical point and stopping there, without comparing the endpoints — for a closed interval the maximum may sit at an endpoint.
- Dividing the perimeter between the two sides as $x+y=40$ in the area formula as well, mixing up the half-perimeter with the perimeter.
- Forgetting to report the second side $y=20-x$, so the answer gives only half of the dimensions.

## How I would explain it in class

I call the two sides $x$ and $y$, and the perimeter condition $2x+2y=40$ lets me write $y=20-x$, so the area becomes the one-variable function $A(x)=x(20-x)$ on the domain $0<x<20$. Differentiating gives $A'(x)=20-2x$, which vanishes only at $x=10$, and since $A''=-2$ and the endpoints give area $0$, this critical point is the global maximum. The winning rectangle is a square with side $10$, and its area is $100$.
