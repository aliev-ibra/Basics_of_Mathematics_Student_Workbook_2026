# Problem 02

## The original problem

Reduce

$$x^2+y^2-6x+4y-3=0$$

to canonical form. Find the center and radius, then substitute two simple points from the circle into both forms of the equation.

## What we are looking for

We want the equation in the standard circle form $(x-h)^2+(y-k)^2=r^2$, so we can read the center $(h,k)$ and radius $r$.

## The idea we need

Complete the square for $x$ and $y$ separately. The identity is $x^2+bx=(x+b/2)^2-(b/2)^2$.

## Step-by-step solution

Group terms:

$$x^2-6x+y^2+4y=3.$$

Complete the square:

$$(x-3)^2-9+(y+2)^2-4=3.$$

Move constants to the right:

$$(x-3)^2+(y+2)^2=16.$$

So the center is $(3,-2)$ and the radius is $\sqrt{16}=4$.

Two simple points on the circle are $(7,-2)$ and $(-1,-2)$.

Check $(7,-2)$ in original: $49+4-42-8-3=0$. In canonical: $(7-3)^2+(-2+2)^2=16$.

Check $(-1,-2)$ in original: $1+4+6-8-3=0$. In canonical: $(-1-3)^2+(-2+2)^2=16$.

## Why each step is valid

Completing the square is just adding and subtracting the same square, so equality is preserved. Taking the square root gives the radius because the right-hand side is $r^2$.

## Final answer (in words)

The circle has center $(3,-2)$ and radius $4$. Its canonical equation is $(x-3)^2+(y+2)^2=16$.

## Verification

Expand $(x-3)^2+(y+2)^2=16$: $x^2-6x+9+y^2+4y+4=16$, which simplifies to $x^2+y^2-6x+4y-3=0$. This matches the original equation.

## Common mistakes

- Forgetting to move the constant to the other side.
- Sign errors in the center: $(y+2)^2$ means center $y$-coordinate $-2$.
- Taking $\sqrt{16}=4$ but writing radius squared.

## How I would explain it in class

I complete the square for each variable, then read the center and radius from the standard form. I verify by expanding back to the original equation. The two test points confirm both forms agree.