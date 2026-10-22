# Problem 7

## The original problem
For
$$L:(x,y,z)=(1,1,0)+t(1,-1,0),\qquad \Pi:x+y+z=2,$$
determine whether the line intersects the plane at one point, is parallel to it, or lies in it. Explain the role of the dot product of the direction vector and the normal vector.

This is a 3D problem (three coordinates per point).

## What we are looking for
We need to determine the relative position of a line and a plane in space. There are three possibilities: the line crosses the plane at exactly one point, the line is parallel to the plane and never touches it, or the line lies entirely inside the plane. We also need to explain how the dot product of the line's direction vector and the plane's normal vector helps decide among these cases.

## The idea we need
The line has direction vector $v=(1,-1,0)$. The plane $x+y+z=2$ has normal vector $n=(1,1,1)$.

The dot product $v\cdot n$ tells us whether the line is parallel to the plane:
- If $v\cdot n \neq 0$, the line is not parallel to the plane, so it intersects the plane at exactly one point.
- If $v\cdot n = 0$, the direction vector is perpendicular to the normal, meaning the line is parallel to the plane. In this case there are two subcases: the line either lies entirely in the plane, or it is parallel to the plane with no common points. To distinguish, check whether one point of the line satisfies the plane equation.

The point-direction form of the line lets us pick any point on it, for example the point at $t=0$.

## Step-by-step solution
1. Identify the direction vector of the line and the normal vector of the plane:
   $$v=(1,-1,0),\qquad n=(1,1,1).$$

2. Compute the dot product:
   $$v\cdot n = (1)(1) + (-1)(1) + (0)(1) = 1 - 1 + 0 = 0.$$

3. Interpret the dot product. Since $v\cdot n=0$, the direction vector is perpendicular to the normal vector. Therefore the line is parallel to the plane (it never crosses through the plane). It either lies in the plane or is strictly parallel with no intersection.

4. Distinguish the two subcases by testing a point on the line. Take the point at $t=0$:
   $$P=(1,1,0).$$
   Substitute into the plane equation $x+y+z=2$:
   $$1 + 1 + 0 = 2.$$
   The point satisfies the equation, so $P$ lies in the plane.

5. Since the line is parallel to the plane and one of its points lies in the plane, the entire line lies in the plane.

## Why each step is valid
- The direction vector $v$ and normal vector $n$ are read directly from the parametric line equation and the plane equation coefficients.
- The dot product $v\cdot n=0$ means $v$ is perpendicular to $n$, which is exactly the condition for the line's direction to be parallel to the plane (the plane consists of all directions perpendicular to $n$).
- When $v\cdot n=0$, the line cannot cross the plane; it either stays inside or stays outside at a constant distance. Testing one point decides which: if one point of the line is in the plane, every point is, because moving along $v$ keeps the dot product with $n$ unchanged.
- Substituting the point into the plane equation checks membership, since a point lies in the plane exactly when its coordinates satisfy the equation.

## Final answer (in words)
The line lies in the plane. The direction vector $(1,-1,0)$ and the plane normal $(1,1,1)$ have dot product zero, so the line is parallel to the plane, and the point $(1,1,0)$ on the line satisfies $x+y+z=2$, so the whole line is contained in the plane.

## Verification
I verify by substituting the full parametric line into the plane equation. A general point on the line is $(1+t,\;1-t,\;0)$. Plugging into $x+y+z$:
$$(1+t) + (1-t) + 0 = 1 + t + 1 - t = 2.$$
This equals 2 for every value of $t$, confirming that every point on the line satisfies the plane equation. So the line lies entirely in the plane, independently confirming the dot-product test.

## Common mistakes
- Concluding the line is parallel with no intersection just because $v\cdot n=0$, without checking whether a point of the line lies in the plane.
- Computing the dot product incorrectly, for example getting a nonzero value and wrongly concluding the line intersects at one point.
- Testing a point that is not actually on the line when distinguishing the two subcases.
- Confusing the normal vector with the direction vector and dotting the wrong two vectors.

## How I would explain it in class
I would say the normal arrow points straight out of the plane, and the direction arrow shows which way the line travels. If those two arrows are perpendicular, meaning their dot product is zero, the line can never poke through the plane; it just skims alongside it. Then I would check one point on the line, see that it already sits on the plane, and conclude the whole line lives inside the plane.
