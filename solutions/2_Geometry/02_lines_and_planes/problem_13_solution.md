# Problem 13

## The original problem
Find the point on the plane $x+2y+2z=4$ closest to $P=(3,0,0)$. Give the distance and check that the segment joining the two points is perpendicular to the plane.

## What we are looking for
We want the point $Q$ of the plane that is nearest to $P$. We also want the distance from $P$ to $Q$. Finally we must show that the segment from $P$ to $Q$ stands at a right angle to the plane.

## The idea we need
The plane has the normal vector $n=(1,2,2)$, read from the coefficients of $x,y,z$. The normal vector is an arrow that stands at a right angle to the plane. The closest point of a plane to $P$ is found by walking from $P$ straight toward the plane, and the shortest walk is the one at a right angle, which means along $n$. This closest point is called the orthogonal projection of $P$ onto the plane.

So we look for $Q=P+t\,n$ and choose $t$ so that $Q$ is in the plane. The distance is then the length of the walk, which is $|t|\cdot|n|$.

## Step-by-step solution
1. The normal vector is $n=(1,2,2)$. Its length is
$$|n|=\sqrt{1^2+2^2+2^2}=\sqrt 9=3.$$
2. Write the points of the line through $P$ along $n$:
$$P+t\,n=(3+t,\;2t,\;2t).$$
3. Put this into the plane equation $x+2y+2z=4$:
$$(3+t)+2(2t)+2(2t)=4,$$
$$3+9t=4,$$
$$t=\frac19.$$
4. Compute the closest point:
$$Q=\left(3+\frac19,\;\frac29,\;\frac29\right)=\left(\frac{28}{9},\;\frac29,\;\frac29\right).$$
5. Compute the segment from $P$ to $Q$:
$$Q-P=\frac19\,(1,2,2).$$
6. Its length is the distance:
$$|Q-P|=\frac19\cdot 3=\frac13.$$

## Why each step is valid
- Among all segments from $P$ to the plane, the perpendicular one is the shortest. This is the same reason why the straight drop from a ceiling lamp to the floor is shorter than any slanted line.
- The perpendicular to the plane points along the normal $n$, so every candidate has the form $P+t\,n$. This reduces the search to one number $t$.
- The point must lie in the plane, so its coordinates must satisfy the plane equation. The equation is linear in $t$, so it has exactly one solution, because $n\cdot n=9$ is not zero.
- Since the walk is $t\,n$ with $t=\frac19$, the length is $\frac19\cdot|n|=\frac19\cdot3=\frac13$.

## Final answer (in words)
The closest point of the plane $x+2y+2z=4$ to $P=(3,0,0)$ is $Q=\left(\frac{28}{9},\frac29,\frac29\right)$. The distance is $\frac13$. The segment from $P$ to $Q$ is $\frac19(1,2,2)$, a multiple of the normal, so it is perpendicular to the plane.

## Verification
I check three things separately.
- $Q$ is in the plane: $\frac{28}{9}+2\cdot\frac29+2\cdot\frac29=\frac{28+4+4}{9}=\frac{36}{9}=4$.
- The segment is perpendicular to the plane. Take two directions inside the plane, for example $u=(2,-1,0)$ and $w=(0,1,-1)$. Both satisfy $n\cdot u=2-2+0=0$ and $n\cdot w=0+2-2=0$, so they lie along the plane. Then
$$(Q-P)\cdot u=\frac19(2-2+0)=0,\qquad (Q-P)\cdot w=\frac19(0+2-2)=0.$$
The segment is perpendicular to two independent directions of the plane, so it is perpendicular to the whole plane.
- The distance by the standard formula: $\dfrac{|3+0+0-4|}{\sqrt{1+4+4}}=\dfrac{1}{3}$. This matches the length of the segment.

## Common mistakes
- Using the point $(3,0,0)$ as if it were already on the plane. Its value is $3$, not $4$.
- Solving $3+9t=4$ with an arithmetic slip. The coefficient of $t$ is $1+4+4=9$.
- Reporting $t=\frac19$ as the distance. The distance is $t$ times the length of $n$, which is $\frac13$.
- Forgetting to add $P$ and writing the closest point as $\frac19 n$.

## How I would explain it in class
The plane has an arrow standing straight out of it, called the normal, and the shortest way from $P$ to the plane runs along that arrow. We write the points on that line through $P$, put them into the plane equation, and find that we have to walk one ninth of the arrow, which lands us at $\left(\frac{28}{9},\frac29,\frac29\right)$. The walk has length one third, and since it is a multiple of the normal, it is perpendicular to the plane.
