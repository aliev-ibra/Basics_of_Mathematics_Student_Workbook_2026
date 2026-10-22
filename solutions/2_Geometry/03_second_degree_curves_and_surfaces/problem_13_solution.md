# Problem 13

## The original problem

Given the sphere
$$x^2+y^2+z^2=25$$
and the plane $z=3$, find the equation of the intersection curve and its radius. Then describe what happens for $z=c$ depending on $c$.

## What we are looking for

We want the curve in which the plane $z=3$ cuts the sphere, written as an equation, and the radius of this curve. Then we want to know, for a general plane $z=c$, what we get depending on the value of $c$.

## The idea we need

The sphere $x^2+y^2+z^2=25$ has its center at the origin and radius $5$. A point is on the intersection when it satisfies both equations at the same time. So we put $z=3$ into the equation of the sphere and see what remains for $x$ and $y$.

## Step-by-step solution

**Step 1: substitute $z=3$.**
$$x^2+y^2+3^2=25.$$
Since $3^2=9$, subtract $9$ from both sides:
$$x^2+y^2=16.$$

**Step 2: read the result.** The equation $x^2+y^2=16$ describes a circle with radius $\sqrt{16}=4$. It lives in the plane $z=3$, and its center is the point $(0,0,3)$, which lies on the $z$-axis. So the intersection curve is
$$x^2+y^2=16,\qquad z=3.$$
Both equations must be written together, because $x^2+y^2=16$ alone would describe a cylinder in space.

**Step 3: the general plane $z=c$.** Substituting $z=c$ gives
$$x^2+y^2=25-c^2.$$
Now we look at the sign of $25-c^2$.

- If $|c|<5$, that is $-5<c<5$, then $25-c^2>0$ and we get a circle with radius $\sqrt{25-c^2}$ and center $(0,0,c)$.
- If $c=\pm5$, then $25-c^2=0$, so $x=y=0$. The plane touches the sphere in the single point $(0,0,5)$ or $(0,0,-5)$. These are the north and south poles.
- If $|c|>5$, then $25-c^2<0$, and since $x^2+y^2$ is never negative, there are no points. The plane misses the sphere.

**Step 4: table.**

| $c$ | $25-c^2$ | cut |
|---|---|---|
| $0$ | $25$ | circle of radius $5$, the equator (largest) |
| $3$ | $16$ | circle of radius $4$ |
| $4$ | $9$ | circle of radius $3$ |
| $\pm5$ | $0$ | one point, a pole |
| $6$ | $-11$ | nothing |

**Step 5: the picture.** The sketch shows a ball of radius $5$ and a horizontal plane through it. If we move the plane from the bottom to the top, it first touches the ball at the south pole, then cuts circles that grow until the equator, then circles that shrink, and finally touches the north pole and leaves.

## Why each step is valid

The intersection of two sets consists of the points that belong to both, so it is described by both equations together. Substituting $z=3$ is allowed because on the plane $z$ always equals $3$.

The radius of a circle $x^2+y^2=r^2$ is $r$, which gives $r=4$. This agrees with geometry: the plane is at distance $3$ from the center, the sphere has radius $5$, and the right triangle with sides $3$, $4$ and hypotenuse $5$ shows that the radius of the circle is $4$.

## Final answer (in words)

The intersection curve is the circle $x^2+y^2=16$ in the plane $z=3$, with center $(0,0,3)$ and radius $4$. For the plane $z=c$ we get the circle $x^2+y^2=25-c^2$ of radius $\sqrt{25-c^2}$ when $|c|<5$, a single point when $c=\pm5$, and no points when $|c|>5$.

## Verification

Check points of the proposed circle in the sphere equation.

- $(4,0,3)$: $16+0+9=25$. Correct.
- $(0,-4,3)$: $0+16+9=25$. Correct.
- $(2,2\sqrt3,3)$: $4+12+9=25$. Correct. It is also on the circle, since $4+12=16$.

A point of the plane that is not on the circle, such as $(1,1,3)$, gives $1+1+9=11\neq25$, so it is not on the sphere, as expected.

Check the general formula with the Pythagorean theorem: radius squared equals $5^2-c^2$. At $c=3$ it is $16$, at $c=4$ it is $9$ (the circle of radius $3$), and at $c=5$ it is $0$.

## Common mistakes

- Writing the answer as $x^2+y^2=25$ and forgetting to subtract $9$.
- Giving $16$ as the radius instead of $4$.
- Writing only $x^2+y^2=16$ without $z=3$, which would be a cylinder.
- Forgetting the two special values $c=\pm5$ where there is one point.
- Saying that for $|c|>5$ the cut is a circle of imaginary radius. In real geometry there is nothing.

## How I would explain it in class

I put $z=3$ into the sphere equation and get $x^2+y^2=16$, a circle of radius $4$ in the plane at height $3$. For a general height $c$ the right-hand side is $25-c^2$, so the circle shrinks as $|c|$ goes toward $5$. At $c=\pm5$ the plane touches the sphere in a point, and above that it misses it.
