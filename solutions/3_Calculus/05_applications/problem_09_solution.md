# Problem 9

## The original problem

A closed cylinder has fixed volume $V$.

1. Write the volume constraint.
2. Eliminate one of the variables.
3. Express the surface area as a function of the radius $r$.
4. Find the relation between the height $h$ and the radius $r$ for which the material usage is minimal.

Interpret the obtained relation geometrically.

> **Why this problem:** it requires independent reduction of a problem with two variables to one objective function and control of the geometric constraint.

## What we are looking for

We make a closed can. The letter $r$ is the radius of the base and $h$ is the height, both in centimetres. The volume $V$ is a given fixed number in cubic centimetres. The material used is the whole surface of the can. We want the shape, that is the relation between $h$ and $r$, that needs the least material.

## The idea we need

First the model. The surface has two circles and one side wall. The wall, unrolled, is a rectangle of width $2\pi r$ and height $h$. The volume fixes a link between $r$ and $h$, so one variable can be removed. Then we have a function of one variable, and we use the derivative.

## Step-by-step solution

1. **Volume constraint.** The base area is $\pi r^2$, so
$$
V=\pi r^2h.
$$

2. **Eliminate $h$.**
$$
h=\frac{V}{\pi r^2}.
$$

3. **Surface area.** Two circles give $2\pi r^2$, the wall gives $2\pi rh$:
$$
S=2\pi r^2+2\pi rh.
$$
Put in $h$ from step 2:
$$
S(r)=2\pi r^2+\frac{2V}{r},\qquad r>0.
$$
The domain is $r>0$, and then $h>0$ automatically.

4. **Differentiate.**
$$
S'(r)=4\pi r-\frac{2V}{r^2}.
$$

5. **Solve $S'(r)=0$.** Then $4\pi r^3=2V$, so
$$
r^3=\frac{V}{2\pi},\qquad r_0=\sqrt[3]{\frac{V}{2\pi}}.
$$

6. **Find $h$.** Since $V=2\pi r_0^3$,
$$
h=\frac{V}{\pi r_0^2}=\frac{2\pi r_0^3}{\pi r_0^2}=2r_0.
$$

7. **Type of the point.**
$$
S''(r)=4\pi+\frac{4V}{r^3}>0\quad\text{for all }r>0,
$$
so $S$ is convex and the critical point is a minimum.

8. **Minimal surface.** With $h=2r_0$, $S=2\pi r_0^2+2\pi r_0\cdot2r_0=6\pi r_0^2$.

## Why each step is valid

- The volume of a cylinder is base area times height, so the constraint is correct.
- Solving for $h$ is allowed because $r>0$, so we do not divide by zero.
- The wall is a rectangle after unrolling, with one side equal to the circumference $2\pi r$ of the base.
- Both ends of the domain are bad. For $r\to0^+$ the term $2V/r$ grows without bound, and for $r\to\infty$ the term $2\pi r^2$ grows without bound. So a minimum inside the domain exists.
- Because $S''>0$ everywhere, there is only one critical point and it is the global minimum.

## Final answer (in words)

The surface area as a function of the radius is $S(r)=2\pi r^2+2V/r$ for $r>0$. The material is smallest when
$$
r=\sqrt[3]{\frac{V}{2\pi}},\qquad h=2r.
$$
So the height equals the diameter. Geometrically, the best can is "square" when seen from the side: its side view is a square, and the minimal area is $6\pi r^2$.

## Verification

Take $V=1000\ \mathrm{cm^3}$. Then $r_0=\sqrt[3]{1000/(2\pi)}\approx5{,}419$ cm and $h\approx10{,}839$ cm, which is $2r_0$. Now compare nearby radii, with $h=V/(\pi r^2)$:

| $r$ (cm) | $h$ (cm) | $S$ (cm$^2$) |
|---|---|---|
| 4 | 19,89 | 600,53 |
| 5 | 12,73 | 557,08 |
| 5,419 | 10,84 | 553,58 |
| 6 | 8,84 | 559,53 |
| 7 | 6,50 | 593,59 |

The area falls and then rises, with the lowest value at $r\approx5{,}42$. Also $6\pi r_0^2\approx553{,}58$ agrees with the table. A second method: at the critical point $S'(5{,}419)=4\pi\cdot5{,}419-2000/5{,}419^2\approx68{,}1-68{,}1=0$.

## Common mistakes

- Forgetting one base and counting only $\pi r^2$ instead of $2\pi r^2$ (this is a closed can).
- Differentiating $S$ while it still has two variables $r$ and $h$.
- Solving $r^3=V/(2\pi)$ and then reporting $h=r$ instead of $h=2r$.
- Forgetting to say which kind of point we found.

## How I would explain it in class

The volume $V=\pi r^2h$ lets us replace $h$ by $V/(\pi r^2)$, so the surface becomes $S(r)=2\pi r^2+2V/r$. Setting the derivative to zero gives $r^3=V/(2\pi)$, and then $h=2r$. The second derivative is always positive, so this is the minimum, and the best can has a height equal to its diameter.
