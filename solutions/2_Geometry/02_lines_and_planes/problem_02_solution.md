# Problem 2

## The original problem
Given
$$L:(x,y,z)=(2,-1,3)+t(1,2,-2).$$
State a point on the line and its direction vector, check whether $P=(4,3,-1)$ lies on $L$, and find the point corresponding to $t=-1$.

This is a 3D problem (three coordinates per point).

## What we are looking for
We need to read off geometric information from the parametric equation of a line in space. Specifically we need one point that lies on the line, the line's direction vector, a yes-or-no answer about whether a given point is on the line, and the coordinates of the point reached when the parameter equals -1.

## The idea we need
The parametric form of a line in space is
$$(x,y,z) = p + t\cdot v,$$
where $p$ is a fixed point on the line (the position vector at $t=0$), $v$ is the direction vector, and $t$ is a real parameter. A point X lies on the line exactly when the equation $X = p + t v$ has a solution for t, meaning the same t works in all three coordinate equations.

## Step-by-step solution
1. Read the point and direction from the equation. Comparing with $p+t v$:
   $$p = (2,-1,3),\qquad v = (1,2,-2).$$
   So $(2,-1,3)$ is a point on the line (the point at $t=0$), and $(1,2,-2)$ is the direction vector.

2. Check whether $P=(4,3,-1)$ lies on L. Set
   $$(4,3,-1) = (2,-1,3) + t(1,2,-2) = (2+t,\; -1+2t,\; 3-2t).$$
   This gives three equations:
   $$4 = 2+t,\qquad 3 = -1+2t,\qquad -1 = 3-2t.$$

3. Solve each for t:
   - From the first: $t = 4-2 = 2$.
   - From the second: $2t = 3+1 = 4$, so $t = 2$.
   - From the third: $-2t = -1-3 = -4$, so $t = 2$.

4. All three equations give the same value $t=2$. Therefore P lies on L, and it is the point reached at parameter value $t=2$.

5. Find the point at $t=-1$:
   $$(x,y,z) = (2,-1,3) + (-1)(1,2,-2) = (2-1,\; -1-2,\; 3-(-2)) = (1,\; -3,\; 5).$$
   So the point corresponding to $t=-1$ is $(1,-3,5)$.

## Why each step is valid
- Reading off p and v is valid because the parametric form explicitly writes the line as a base point plus a scalar multiple of a direction vector.
- Setting P equal to $p+t v$ is the definition of membership: P is on the line iff such a t exists.
- Requiring the same t in all three coordinates is necessary because a single parameter value determines one point; different t values in different coordinates would describe no single point on the line.
- Substitution into $p+t v$ at a specific t gives a point on the line by construction of the parametric form.

## Final answer (in words)
A point on the line is $(2,-1,3)$ and its direction vector is $(1,2,-2)$. The point $P=(4,3,-1)$ lies on the line because it is reached at $t=2$. The point corresponding to $t=-1$ is $(1,-3,5)$.

## Verification
I verify P by plugging $t=2$ back into the line equation: $(2,-1,3)+2(1,2,-2) = (2+2,\; -1+4,\; 3-4) = (4,\; 3,\; -1)$, which is exactly P. I verify the $t=-1$ point directly: $(2,-1,3)-(1,2,-2) = (1,\; -3,\; 5)$. Both substitutions match, so the results are consistent.

## Common mistakes
- Reading the constant triple $(2,-1,3)$ as the direction vector instead of the base point; the base point is at $t=0$ and the direction is the vector multiplied by t.
- Solving each coordinate equation for t separately and not checking that all three give the same value; inconsistent t values mean the point is not on the line.
- Making an arithmetic sign error at $t=-1$, especially in the z-coordinate where $3-(-2)=5$ rather than $3-2=1$.
- Concluding a point is not on the line just because one coordinate looks different, without solving for t.

## How I would explain it in class
I would point out that the numbers standing alone, $(2,-1,3)$, are where the line starts when t is zero, and the numbers attached to t tell us which way the line goes. To test the point P, I would ask whether one single value of t can hit all three coordinates at once, and here t equals two everywhere, so P is on the line. For t equals minus one, I just walk one step backward along the direction and land on $(1,-3,5)$.
