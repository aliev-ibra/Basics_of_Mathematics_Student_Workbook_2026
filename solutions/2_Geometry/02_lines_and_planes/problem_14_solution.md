# Problem 14

## The original problem
From the point $P=(0,0,1)$, two lines are drawn with direction vectors
$$v_1=(2,1,-1),\qquad v_2=(2,1,0).$$
For each line, analyze its position relative to the plane $z=0$.

For the line that intersects the plane, find the intersection point. For the other line, explain how you can recognize parallelism without solving an equation.

## What we are looking for
We have two lines that both start at $P=(0,0,1)$. The plane $z=0$ is the flat floor of the coordinate system. For each line we must say whether it crosses the floor in one point, runs parallel to it, or lies in it. For the crossing line we must give the point. For the other we must explain, without solving anything, why it is parallel.

## The idea we need
A direction vector is an arrow that points along a line. The plane $z=0$ has the normal vector $n=(0,0,1)$, an arrow standing straight up from the floor. The dot product of $v$ and $n$ is the sum of the products of the matching entries. If the dot product is zero, then $v$ is at a right angle to the normal, which means $v$ runs along the floor and never climbs or falls. Then the line is parallel to the plane. If the dot product is not zero, the line climbs or falls, so it must cross the floor.

If a line is parallel to the plane, we then look at the starting point. If $P$ is in the plane, the line lies in it. If not, the line never touches it.

## Step-by-step solution
1. The normal vector of the plane $z=0$ is $n=(0,0,1)$.
2. For the first line, compute
$$v_1\cdot n=2\cdot0+1\cdot0+(-1)\cdot1=-1.$$
This is not zero, so the first line crosses the plane at exactly one point.
3. For the second line, compute
$$v_2\cdot n=2\cdot0+1\cdot0+0\cdot1=0.$$
This is zero, so the second line is parallel to the plane.
4. Find the crossing point of the first line. Its points are
$$P+t\,v_1=(2t,\;t,\;1-t).$$
The plane requires $z=0$, so $1-t=0$ and $t=1$. The point is
$$(2,\;1,\;0).$$
5. Decide for the second line. Its points are $(2s,\;s,\;1)$. The third coordinate is always $1$, and the plane needs $0$. The starting point $P$ has $z=1$, so it is not in the plane. Hence the second line is parallel to the plane and has no common point with it.

## Why each step is valid
- The plane $z=0$ consists of all points whose third coordinate is zero. Only the third entry of a direction vector tells how fast the height changes, and the normal $(0,0,1)$ picks out exactly that entry. This is why the dot product with $n$ is the height change per step.
- For $v_2$, the height change is zero. Moving along it never changes the height $1$, so the line stays at the same height above the floor. This is the recognition of parallelism without solving any equation.
- For $v_1$, the height changes by $-1$ for each step of $t$, so the line must reach height $0$ after $t=1$. This is the only solution, since the equation is linear.
- A parallel line with starting point outside the plane cannot lie in it, so it has no common point. The value $1\neq0$ shows that $P$ is outside.

## Final answer (in words)
The first line, with direction $(2,1,-1)$, crosses the plane $z=0$ in exactly one point, which is $(2,1,0)$. The second line, with direction $(2,1,0)$, is parallel to the plane because its direction has no vertical part, which is the same as saying its dot product with the normal $(0,0,1)$ is zero. It stays at height $1$ forever, so it never meets the plane.

## Verification
For the crossing point: on the first line, at $t=1$ we get $(0,0,1)+1\cdot(2,1,-1)=(2,1,0)$. Its third coordinate is $0$, so it is in the plane. No other $t$ works, since $1-t=0$ only for $t=1$.

For the parallel line: take a few parameter values, for example $s=0,1,-3$. We get the points $(0,0,1)$, $(2,1,1)$ and $(-6,-3,1)$. All have height $1$, so none is in the plane. The distance from any of these points to the plane is $1$, the same for all, which is the sign of a parallel line.

## Common mistakes
- Looking only at the first two entries of the direction vector, which look the same ($2$ and $1$ in both), and concluding that the lines behave alike. The third entry decides.
- Saying that the second line lies in the plane. It would do so only if $P$ were in the plane, but $P$ has height $1$.
- Computing the dot product with the wrong normal. For the plane $z=0$ the normal is $(0,0,1)$, not $(1,1,1)$.
- Concluding that a line with $v\cdot n=0$ is perpendicular to the plane. That would be the case of a direction parallel to $n$. A zero dot product means perpendicular to the normal, so parallel to the plane.

## How I would explain it in class
The floor is the plane $z=0$, and both lines start one unit above it, at the same point. The first line goes downward by one unit for each step, so it reaches the floor after one step at the point $(2,1,0)$. The second line has a zero in its last entry, so it never goes up or down, and it flies at height one above the floor without ever touching it.
