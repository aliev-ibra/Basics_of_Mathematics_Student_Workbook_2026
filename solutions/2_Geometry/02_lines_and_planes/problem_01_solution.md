# Problem 1

## The original problem
Find the equation of the line through $A=(1,2)$ and $B=(4,-1)$ in parametric and general form. Identify a direction vector and an example of a normal vector. Check that both points satisfy the equation you obtain.

This is a 2D problem (two coordinates per point).

## What we are looking for
We want a description of the straight line that passes through the two given points in the plane. Specifically we need a parametric equation, a general equation, one direction vector, and one normal vector. We also need to confirm that both given points lie on the resulting line.

## The idea we need
A line in the plane can be written as a known point plus a parameter times a direction vector:
$$(x,y) = A + t\cdot v,$$
where $A$ is a point on the line, $v$ is a direction vector parallel to the line, and $t$ is a real number. The direction vector is found as the difference of the two points, $v = B - A$.

The general form of a line is
$$ax + by + c = 0,$$
where the vector $n=(a,b)$ is a normal vector, meaning it is perpendicular to the line. A normal vector is perpendicular to any direction vector of the line, so $n\cdot v = 0$.

## Step-by-step solution
1. Find a direction vector by subtracting the coordinates of A from B:
   $$v = B - A = (4-1,\; -1-2) = (3,\; -3).$$
   The vector $v=(3,-3)$ points from A to B, so it is parallel to the line.

2. Write the parametric form using point A and direction vector v:
   $$(x,y) = (1,2) + t(3,-3),$$
   which means $x = 1+3t$ and $y = 2-3t$ for $t\in\mathbb{R}$.

3. Eliminate the parameter t to get the general form. From $x=1+3t$ we get $t=(x-1)/3$. From $y=2-3t$ we get $t=(2-y)/3$. Setting them equal:
   $$\frac{x-1}{3} = \frac{2-y}{3}.$$
   Multiplying by 3:
   $$x-1 = 2-y.$$
   Rearranging:
   $$x + y - 3 = 0.$$

4. Identify a normal vector. For a line $ax+by+c=0$, the vector $n=(a,b)$ is normal. Here $a=1$, $b=1$, so an example normal vector is
   $$n = (1,1).$$
   Check: $n\cdot v = (1,1)\cdot(3,-3) = 3-3 = 0$, so the normal is perpendicular to the direction, as required.

5. Check that both points satisfy the general equation $x+y-3=0$:
   - For A=(1,2): $1+2-3 = 0$. ✓
   - For B=(4,-1): $4+(-1)-3 = 0$. ✓

## Why each step is valid
- The direction vector $B-A$ is valid because the vector joining two points on a line is parallel to that line.
- The parametric form is the standard point-direction description of a line: starting at A and moving along v by a scalar amount t reaches every point of the line.
- Eliminating t is valid because both expressions equal the same parameter t, so they equal each other; multiplying by the nonzero number 3 preserves equality.
- For $ax+by+c=0$, the coefficients (a,b) form a normal vector because the equation can be read as $(a,b)\cdot(x,y) = -c$, which says every point (x,y) on the line has a fixed dot product with (a,b).
- Substituting a point into the equation checks membership: a point lies on the line exactly when its coordinates make the equation true.

## Final answer (in words)
The line through A and B has direction vector $(3,-3)$, parametric equation $(x,y)=(1,2)+t(3,-3)$, general equation $x+y-3=0$, and an example normal vector is $(1,1)$. Both given points satisfy the equation, confirming they lie on the line.

## Verification
I check the parametric form against the general form. Take the point at $t=1$: $(x,y)=(1,2)+(3,-3)=(4,-1)$, which is B, and B satisfies $4+(-1)-3=0$. Take $t=0$: $(1,2)=A$, and $1+2-3=0$. Both agree. Also the normal $(1,1)$ dotted with direction $(3,-3)$ is zero, confirming perpendicularity.

## Common mistakes
- Using $A-B$ instead of $B-A$ gives $(-3,3)$, which is still a valid direction vector but the opposite sign; either is acceptable as long as it is used consistently.
- Forgetting to check that both points satisfy the final equation, which can hide an algebra error in the constant term.
- Confusing the normal vector with the direction vector; the normal $(1,1)$ is perpendicular to the direction $(3,-3)$, not parallel to it.
- Making a sign error when rearranging $x-1=2-y$ into $x+y-3=0$.

## How I would explain it in class
I would start by drawing the two points and connecting them with an arrow, because that arrow is our direction vector. Then I would say that walking from A in that direction by any amount traces the whole line, which gives the parametric form. Finally I would eliminate the step size t to get the simple equation x plus y minus three equals zero, and check both points lie on it.
