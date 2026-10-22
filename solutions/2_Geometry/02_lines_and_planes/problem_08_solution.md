# Problem 8

## The original problem
Find the intersection point of
$$(x,y,z)=(1,0,2)+t(1,2,-1)$$
with the plane $x+y+z=4$. Check the result by substituting it into both descriptions.

This is a 3D problem (three coordinates per point).

## What we are looking for
We want the single point where a given line in space crosses a given plane. That point must satisfy both the parametric equation of the line and the equation of the plane. We also need to verify the result by plugging it back into both descriptions.

## The idea we need
A line and a plane in space generally intersect at one point when the line is not parallel to the plane. To find it, substitute the parametric coordinates of the line into the plane equation. This gives one equation in the single unknown $t$, which can be solved. Once $t$ is found, substitute it back into the line equation to get the intersection point.

The condition for a unique intersection is that the direction vector $v$ of the line is not perpendicular to the normal vector $n$ of the plane, i.e. $v\cdot n \neq 0$. Here $v=(1,2,-1)$ and $n=(1,1,1)$, so $v\cdot n = 1+2-1 = 2 \neq 0$, confirming a unique intersection point exists.

## Step-by-step solution
1. Identify the line and plane data.
   Line: base point $p=(1,0,2)$, direction $v=(1,2,-1)$.
   Plane: $x+y+z=4$, normal $n=(1,1,1)$.

2. Confirm a unique intersection exists. Compute
   $$v\cdot n = (1)(1) + (2)(1) + (-1)(1) = 1 + 2 - 1 = 2.$$
   Since $v\cdot n \neq 0$, the line is not parallel to the plane, so there is exactly one intersection point.

3. Write a general point on the line using parameter $t$:
   $$(x,y,z) = (1+t,\; 0+2t,\; 2-t) = (1+t,\; 2t,\; 2-t).$$

4. Substitute into the plane equation $x+y+z=4$:
   $$(1+t) + (2t) + (2-t) = 4.$$
   Simplify:
   $$1 + t + 2t + 2 - t = 4,$$
   $$3 + 2t = 4.$$

5. Solve for $t$:
   $$2t = 4 - 3 = 1,$$
   $$t = \frac{1}{2}.$$

6. Substitute $t=\frac{1}{2}$ back into the line equation to get the point:
   $$x = 1 + \frac{1}{2} = \frac{3}{2},$$
   $$y = 2\cdot\frac{1}{2} = 1,$$
   $$z = 2 - \frac{1}{2} = \frac{3}{2}.$$
   So the intersection point is
   $$\left(\frac{3}{2},\; 1,\; \frac{3}{2}\right).$$

## Why each step is valid
- Substituting the line's parametric coordinates into the plane equation is valid because the intersection point lies on both the line and the plane, so its coordinates must satisfy both equations simultaneously.
- The resulting equation is linear in $t$ because the line coordinates are linear in $t$ and the plane equation is linear in $x,y,z$.
- Solving $3+2t=4$ for $t$ is valid because the coefficient of $t$ is nonzero ($2\neq0$), which follows from $v\cdot n\neq0$.
- Substituting the found $t$ back into the line equation gives the actual point on the line at that parameter value, which is the intersection point.
- The condition $v\cdot n\neq0$ guarantees the line crosses the plane rather than running parallel to it, so a unique solution for $t$ is expected.

## Final answer (in words)
The line intersects the plane at exactly one point, namely $\left(\frac{3}{2}, 1, \frac{3}{2}\right)$, reached at parameter value $t=\frac{1}{2}$. This point lies on both the line and the plane.

## Verification
I check the point in both descriptions independently.
- In the plane: $\frac{3}{2} + 1 + \frac{3}{2} = \frac{3}{2} + \frac{2}{2} + \frac{3}{2} = \frac{8}{2} = 4$. ✓
- On the line: at $t=\frac{1}{2}$, $(1,0,2)+\frac{1}{2}(1,2,-1) = (1+\frac{1}{2},\; 0+1,\; 2-\frac{1}{2}) = (\frac{3}{2},\; 1,\; \frac{3}{2})$. ✓
Both descriptions give the same point, confirming the intersection point is correct.

## Common mistakes
- Making an arithmetic error when simplifying $(1+t)+(2t)+(2-t)$, for example mishandling the $-t$ term and getting the wrong coefficient for $t$.
- Solving for $t$ but forgetting to substitute it back into the line equation to get the actual coordinates of the point.
- Not checking that $v\cdot n\neq0$ first, which could lead to missing the case of no intersection or infinitely many intersections.
- Substituting the point into only one description (line or plane) instead of both.

## How I would explain it in class
I would say the line gives us a moving point that depends on a dial called t, and the plane is a flat sheet given by an equation. To find where they meet, I plug the moving point into the sheet's equation and solve for t, which tells me exactly where on the line the crossing happens. Then I turn that t value back into coordinates to name the point, and I double-check by plugging it into both the line and the plane.
