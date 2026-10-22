# Problem 08

## The original problem

Reduce

$$x^2+y^2+z^2-4x+2y-6z-2=0$$

to canonical form. Find the center and radius. Give two points on the sphere and check them in the equation.

## What we are looking for

We want the sphere's canonical equation, center, radius, and two verified points.

## The idea we need

Complete the square in three variables. A sphere has canonical form $(x-a)^2+(y-b)^2+(z-c)^2=r^2$.

## Step-by-step solution

Group:

$$x^2-4x+y^2+2y+z^2-6z=2.$$

Complete the square:

$$(x-2)^2-4+(y+1)^2-1+(z-3)^2-9=2.$$

Move constants:

$$(x-2)^2+(y+1)^2+(z-3)^2=16.$$

Center: $(2,-1,3)$. Radius: $\sqrt{16}=4$.

Two points on the sphere: $(6,-1,3)$ and $(2,-1,7)$.

Check $(6,-1,3)$ in original: $36+1+9-24-2-18-2=0$. In canonical: $(6-2)^2+(-1+1)^2+(3-3)^2=16$.

Check $(2,-1,7)$ in original: $4+1+49-8-2-42-2=0$. In canonical: $(2-2)^2+(-1+1)^2+(7-3)^2=16$.

## Why each step is valid

Completing the square preserves equality. The right-hand side after moving constants is $r^2$, so the radius is its square root. Points are obtained by moving the radius along a coordinate axis from the center.

## Final answer (in words)

The sphere has center $(2,-1,3)$ and radius $4$. Its canonical equation is $(x-2)^2+(y+1)^2+(z-3)^2=16$.

## Verification

Expand $(x-2)^2+(y+1)^2+(z-3)^2=16$: $x^2-4x+4+y^2+2y+1+z^2-6z+9=16$, which simplifies to $x^2+y^2+z^2-4x+2y-6z-2=0$. This matches the original.

## Common mistakes

- Sign error in the center $z$-coordinate.
- Forgetting to move all three constants.
- Using radius $16$ instead of $4$.

## How I would explain it in class

I complete the square in all three variables, then read the center and radius. Expanding back confirms the algebra. The two test points are found by moving the radius from the center.