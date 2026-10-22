# Problem 12

## The original problem
Find a parametric equation of the line that is the intersection of
$$x+y+z=3,\qquad x-y+z=1.$$
Find its direction vector in two ways: from the system of equations and from the cross product of the normal vectors. Compare the results.

## What we are looking for
Two planes that are not parallel meet along a line. We want a parametric equation of that line, which means one point on it and one direction vector. A direction vector is an arrow that points along the line. We want to find this direction in two different ways and see whether the two answers agree.

## The idea we need
Every point of the intersection line must satisfy both plane equations at the same time. So we solve the two equations together. Two equations in three unknowns leave one free choice, and that free choice becomes the parameter $t$.

The geometric way uses the normal vectors. A normal vector is an arrow standing at a right angle to a plane. The line lies in both planes, so it is perpendicular to both normals. The cross product of two vectors is a vector perpendicular to both of them. So the cross product of the two normals points along the line.

## Step-by-step solution
**Method 1: from the system.**

1. Add the two equations. The $y$ terms cancel:
$$(x+y+z)+(x-y+z)=3+1,\qquad 2x+2z=4,\qquad x+z=2.$$
2. Subtract the second equation from the first. The $x$ and $z$ terms cancel:
$$(x+y+z)-(x-y+z)=3-1,\qquad 2y=2,\qquad y=1.$$
3. So every point on the line has $y=1$ and $z=2-x$. Choose $x=t$ as the free parameter:
$$(x,y,z)=(t,\;1,\;2-t)=(0,1,2)+t(1,0,-1).$$
4. The point is $(0,1,2)$ and the direction vector is $d_1=(1,0,-1)$.

**Method 2: from the cross product.**

1. The normal vectors are $n_1=(1,1,1)$ and $n_2=(1,-1,1)$.
2. Compute
$$n_1\times n_2=\big(1\cdot1-1\cdot(-1),\;\;1\cdot1-1\cdot1,\;\;1\cdot(-1)-1\cdot1\big)=(2,\;0,\;-2).$$
3. This direction is $d_2=(2,0,-2)$.

**Comparison.** We see $d_2=2\,d_1$. The two vectors are parallel, so they give the same direction of the line. They differ only by the length, which does not matter for a direction.

## Why each step is valid
- Adding or subtracting two true equations gives a new true equation, so every point on both planes satisfies the new equations. Conversely, the pair $x+z=2$ and $y=1$ gives back both original equations: adding $y=1$ to $x+z=2$ gives the first, and $x+z-y=1$ gives the second.
- Setting $x=t$ is allowed because $x$ is free: for every $x$ there is exactly one $z=2-x$. That is why we get a whole line and one parameter.
- The cross product is perpendicular to both normals. A direction perpendicular to $n_1$ stays inside the first plane, and a direction perpendicular to $n_2$ stays inside the second. A direction doing both is along the intersection.
- The two methods agree up to a factor because the line has only one direction, and any nonzero multiple of a direction vector is a direction vector of the same line.

## Final answer (in words)
The intersection line is
$$(x,y,z)=(0,1,2)+t(1,0,-1).$$
Its direction vector from the system is $(1,0,-1)$, and from the cross product it is $(2,0,-2)$, which is exactly twice as long and points the same way. So both methods give the same line direction.

## Verification
I check that the line lies in both planes by putting a general point $(t,\,1,\,2-t)$ into each equation.

First plane: $t+1+(2-t)=3$. This holds for every $t$.

Second plane: $t-1+(2-t)=1$. This holds for every $t$.

I also check the direction with the dot product. The direction $(1,0,-1)$ is perpendicular to $n_1$: $1+0-1=0$. It is perpendicular to $n_2$: $1-0-1=0$. Both are zero, which is what a direction along both planes requires.

## Common mistakes
- Solving only one of the equations, or making a sign error in the subtraction and getting $y=2$ or a wrong relation between $x$ and $z$.
- Saying the two direction vectors differ and so the methods disagree. Parallel vectors are equally good directions.
- Computing the cross product with a sign error. The check that the result is perpendicular to both normals catches this.
- Using a point that satisfies only one plane equation as the base point.

## How I would explain it in class
Each plane is a flat sheet, and where two sheets cross we get a straight line. If we solve the two equations together, one coordinate stays free, and letting it run gives the line $(0,1,2)+t(1,0,-1)$. The cross product of the two normal arrows gives the same direction, only twice as long, because the line must be perpendicular to both arrows.
