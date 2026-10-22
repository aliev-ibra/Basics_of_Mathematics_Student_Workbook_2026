# Problem 10

## The original problem
Find the orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$, and then find the reflection of $P$ across this plane. Check that the midpoint of the segment joining the point and its reflection lies on the plane.

## What we are looking for
We want two points. The first is the orthogonal projection of $P$: the point of the plane that is closest to $P$, where the straight drop from $P$ meets the plane at a right angle. The second is the reflection of $P$: the mirror image of $P$ when the plane is a mirror. We also want to show that the middle of the segment from $P$ to its reflection lies on the plane.

## The idea we need
The plane $x+y+z=3$ has the normal vector $n=(1,1,1)$. The normal vector is an arrow that stands at a right angle to the plane. If we drop a perpendicular from $P$ to the plane, it runs along $n$. So the projection has the form
$$F=P+t\,n$$
for some number $t$. We find $t$ by asking that $F$ lies on the plane.

The reflection is found by going twice as far along the same line. If the foot is $F$ and the point is $P$, the mirror image is $P'=P+2t\,n$, so that $F$ is exactly in the middle between $P$ and $P'$.

## Step-by-step solution
1. Write the normal vector: $n=(1,1,1)$.
2. Write the line through $P$ along $n$:
$$P+t\,n=(2+t,\;1+t,\;3+t).$$
3. Put this point into the plane equation $x+y+z=3$:
$$(2+t)+(1+t)+(3+t)=3,$$
$$6+3t=3,$$
$$t=-1.$$
4. Put $t=-1$ back to get the projection:
$$F=(2-1,\;1-1,\;3-1)=(1,0,2).$$
5. Get the reflection by using $2t=-2$:
$$P'=(2-2,\;1-2,\;3-2)=(0,-1,1).$$
6. Find the midpoint of $P$ and $P'$ by averaging each coordinate:
$$M=\left(\frac{2+0}{2},\;\frac{1+(-1)}{2},\;\frac{3+1}{2}\right)=(1,0,2).$$
7. Check that $M$ is in the plane: $1+0+2=3$. It is, and in fact $M=F$.

## Why each step is valid
- The perpendicular from $P$ to the plane is parallel to the normal $n$, so every point of that perpendicular has the form $P+t\,n$.
- The projection is the one point of that line which also lies in the plane. So its coordinates must satisfy the plane equation, and this gives one equation for $t$.
- The value $t=-1$ is negative because $P$ lies on the side of the plane where $x+y+z=6$ is bigger than $3$. We have to walk backwards along $n$ to reach the plane.
- The reflection is at the same distance from the plane as $P$ but on the other side, on the same perpendicular line. Doubling the step from $t=-1$ to $2t=-2$ does exactly this.
- The midpoint of a segment is the average of its two ends, so the midpoint of $PP'$ must be the foot $F$. The check in step 7 confirms this by an independent computation.

## Final answer (in words)
The orthogonal projection of $P=(2,1,3)$ onto the plane $x+y+z=3$ is the point $(1,0,2)$. The reflection of $P$ across the plane is the point $(0,-1,1)$. The midpoint of $P$ and its reflection is $(1,0,2)$, and since $1+0+2=3$ it lies on the plane.

## Verification
I check four things, each separately.
- The projection is in the plane: $1+0+2=3$.
- The reflection is on the other side at the same level: for $P$ the sum of the coordinates is $6$, which is $3$ above the plane value $3$. For $P'=(0,-1,1)$ the sum is $0$, which is $3$ below. So the two points are on opposite sides at the same distance.
- The segment from $P$ to $P'$ is perpendicular to the plane. Its direction is $P'-P=(-2,-2,-2)$, and this is $-2$ times $n=(1,1,1)$, so it is parallel to the normal.
- The distance from $P$ to the plane by the standard formula is $\frac{|2+1+3-3|}{\sqrt 3}=\frac{3}{\sqrt 3}=\sqrt 3$. The length of $F-P=(-1,-1,-1)$ is $\sqrt 3$ as well.

## Common mistakes
- Using the point $P$ itself, or the plane constant $3$, as the normal vector. The normal is $(1,1,1)$, the coefficients of $x,y,z$.
- Making a sign error in solving $6+3t=3$ and getting $t=1$, which would send the point further away from the plane.
- Reflecting with $t$ instead of $2t$, which gives the projection again and not the mirror image.
- Computing the midpoint by adding the coordinates and forgetting to divide by $2$.

## How I would explain it in class
Imagine the plane as a mirror and the normal vector as an arrow standing straight out of it. We drop a straight line from the point along that arrow until it touches the mirror, and the touching point is the projection, which is $(1,0,2)$. If we keep going the same distance past the mirror, we land on the reflection $(0,-1,1)$, and the touching point is exactly halfway between the two, so the midpoint lies on the plane.
