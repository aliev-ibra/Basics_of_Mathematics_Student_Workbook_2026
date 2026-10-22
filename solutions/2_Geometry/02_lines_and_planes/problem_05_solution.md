# Problem 5

## The original problem
Analyze the position of
$$L_1:(x,y,z)=(1,1,0)+t(1,2,1),$$
$$L_2:(x,y,z)=(2,0,1)+s(0,1,-1).$$
If they intersect, give the intersection point. If not, determine whether they are parallel or skew. Justify the classification.

This is a 3D problem (three coordinates per point).

## What we are looking for
We need to decide how the two lines in space are related to each other. Specifically, we must determine whether they intersect at one point, are parallel, or are skew (neither parallel nor intersecting). If they intersect, we must give the coordinates of the intersection point.

## The idea we need
Two lines in space can have three possible relative positions:
1. Parallel: their direction vectors are scalar multiples of each other.
2. Intersecting: there exist parameter values $t$ and $s$ such that the two points coincide, i.e. the same point satisfies both parametric equations.
3. Skew: not parallel and not intersecting.

To test for intersection, set the two parametric expressions equal component by component and solve the resulting system. If the system is consistent, the lines intersect; if inconsistent, they do not.

The direction vector of $L_1$ is $v_1=(1,2,1)$ and of $L_2$ is $v_2=(0,1,-1)$.

## Step-by-step solution
1. Check whether the lines are parallel. The lines are parallel iff $v_1$ is a scalar multiple of $v_2$.
   $$v_1=(1,2,1),\qquad v_2=(0,1,-1).$$
   The first components are $1$ and $0$. For $v_1 = k v_2$ we would need $1 = k\cdot 0 = 0$, which is impossible. So the direction vectors are not proportional, and the lines are not parallel.

2. Test for intersection by setting the two lines equal:
   $$(1+t,\; 1+2t,\; t) = (2,\; s,\; 1-s).$$
   This gives three scalar equations:
   $$1 + t = 2, \tag{1}$$
   $$1 + 2t = s, \tag{2}$$
   $$t = 1 - s. \tag{3}$$

3. Solve equation (1): $t = 2 - 1 = 1$.
   Substitute $t=1$ into equation (2): $s = 1 + 2(1) = 3$.
   So the first two equations give $t=1$ and $s=3$.

4. Check consistency with equation (3). With $t=1$ and $s=3$:
   $$t = 1,\qquad 1 - s = 1 - 3 = -2.$$
   But $1 \neq -2$, so equation (3) is not satisfied.

5. The system is inconsistent: no single pair $(t,s)$ satisfies all three equations simultaneously. Therefore the lines do not intersect.

6. Since the lines are not parallel and do not intersect, they are skew.

## Why each step is valid
- Comparing direction vectors for proportionality is the standard test for parallel lines: parallel lines have the same or opposite direction.
- Setting the two parametric expressions equal is the definition of intersection: a common point means some $t$ on $L_1$ and some $s$ on $L_2$ produce the same coordinates.
- Requiring all three component equations to hold with the same $(t,s)$ is necessary because one parameter pair determines one point in space; satisfying only two coordinates does not guarantee the third matches.
- An inconsistent system means the lines have no common point, so with non-parallel directions they must be skew.

## Final answer (in words)
The two lines are skew: they are not parallel because their direction vectors $(1,2,1)$ and $(0,1,-1)$ are not proportional, and they do not intersect because equating them gives $t=1$ and $s=3$ from two coordinates but a contradiction in the third. There is no intersection point.

## Verification
I independently check the candidate point from the first two equations. With $t=1$ on $L_1$: $(1,1,0)+(1,2,1)=(2,3,1)$. With $s=3$ on $L_2$: $(2,0,1)+3(0,1,-1)=(2,3,-2)$. These differ in the z-coordinate ($1$ vs $-2$), confirming no common point. Also $v_1\times v_2 = (-3,1,1)\neq 0$, confirming the directions are not parallel, so skew is the correct classification.

## Common mistakes
- Concluding the lines intersect after solving only two of the three component equations, without checking the third.
- Declaring the lines parallel just because they look different, without verifying the direction vectors are not proportional.
- Confusing skew lines with parallel lines; skew lines are non-parallel and non-intersecting, which is exactly the situation here.
- Giving an intersection point without substituting it back into both line equations to confirm.

## How I would explain it in class
I would say the two lines point in different directions, so they are definitely not parallel. Then I would try to make them meet by setting their coordinates equal, and I would find that the first two coordinates can match at $t=1$ and $s=3$, but the third coordinate refuses to agree. Since they do not point the same way and they never meet, the lines are skew, meaning they pass each other in space without touching.
