# Problem 15

## The original problem
Let
$$L:p+tv,\qquad \Pi:n\cdot x=d.$$
State the conditions distinguishing the three cases: one intersection point, parallel with no common points, and the line contained in the plane. Then illustrate each case with your own simple numerical example.

## What we are looking for
We have a line $L$ given by a point $p$ and a direction vector $v$, and a plane $\Pi$ given by a normal vector $n$ and a number $d$. We want a rule that decides from the numbers $p$, $v$, $n$, $d$ which of the three cases happens. Then we want one simple example for each case.

## The idea we need
A direction vector $v$ is an arrow along the line. A normal vector $n$ is an arrow standing at a right angle to the plane. The dot product $n\cdot v$ is a number that is zero exactly when the two arrows are at a right angle. If $n\cdot v=0$, the line moves along the plane and does not climb away from it. If $n\cdot v\neq0$, the line goes through the plane at an angle.

To find the common points, we put the points $p+tv$ of the line into the plane equation $n\cdot x=d$. Since $n\cdot(p+tv)=n\cdot p+t\,(n\cdot v)$, we get one linear equation
$$n\cdot p+t\,(n\cdot v)=d.$$
All three cases come from looking at this single equation in the unknown $t$.

## Step-by-step solution
**General conditions.**

1. Case A, one intersection point: $n\cdot v\neq0$. Then the equation has exactly one solution
$$t=\frac{d-n\cdot p}{n\cdot v},$$
and the intersection point is $p+tv$ for this $t$.
2. Case B, parallel with no common points: $n\cdot v=0$ and $n\cdot p\neq d$. Then the equation says $n\cdot p=d$, which is false, so no $t$ works.
3. Case C, the line lies in the plane: $n\cdot v=0$ and $n\cdot p=d$. Then the equation says $d=d$, which is true for every $t$, so every point of the line is in the plane.

**Examples.** We use the plane $\Pi:z=0$, so $n=(0,0,1)$ and $d=0$. Then $n\cdot x$ is just the height $z$.

4. Example A. Take $p=(0,0,2)$ and $v=(0,0,1)$. Then $n\cdot v=1\neq0$. The equation is $2+t=0$, so $t=-2$ and the point is $(0,0,2)-2(0,0,1)=(0,0,0)$. The line is vertical and pierces the plane at the origin.
5. Example B. Take $p=(0,0,1)$ and $v=(1,0,0)$. Then $n\cdot v=0$ and $n\cdot p=1\neq0=d$. The line runs horizontally at height $1$ above the plane and never touches it.
6. Example C. Take $p=(0,0,0)$ and $v=(1,1,0)$. Then $n\cdot v=0$ and $n\cdot p=0=d$. The line runs inside the plane through the origin.

## Why each step is valid
- The expansion $n\cdot(p+tv)=n\cdot p+t\,(n\cdot v)$ holds because the dot product respects sums and constant multiples. It turns the geometric question into one linear equation in $t$.
- A linear equation $\alpha+t\beta=d$ has exactly one solution if $\beta\neq0$, no solution if $\beta=0$ and $\alpha\neq d$, and every $t$ as a solution if $\beta=0$ and $\alpha=d$. There are no other possibilities, so the three cases are complete and do not overlap.
- Geometrically, $n\cdot v=0$ means the direction is at a right angle to the normal, hence parallel to the plane. Then the quantity $n\cdot x$ stays constant along the line, equal to $n\cdot p$, and the whole line is either at level $d$ or at another level.
- The check $n\cdot p=d$ only needs one point of the line. This is enough because in the parallel case all points have the same value of $n\cdot x$.

## Final answer (in words)
Look at the number $n\cdot v$. If it is not zero, the line meets the plane in exactly one point, at $t=\dfrac{d-n\cdot p}{n\cdot v}$. If it is zero, the line is parallel to the plane, and then we look at one point: if $n\cdot p\neq d$ there are no common points, and if $n\cdot p=d$ the line lies in the plane. For the plane $z=0$, the line $(0,0,2)+t(0,0,1)$ meets it at the origin, the line $(0,0,1)+t(1,0,0)$ is parallel with no common points, and the line $(0,0,0)+t(1,1,0)$ lies in it.

## Verification
I test each example directly, without the general formula.

Example A: the points are $(0,0,2+t)$. The height is $0$ only for $t=-2$. So there is exactly one common point, $(0,0,0)$.

Example B: the points are $(t,0,1)$. The height is $1$ for every $t$, and it is never $0$. So there are no common points. The dot product is $n\cdot v=(0,0,1)\cdot(1,0,0)=0$, as the rule for parallelism requires.

Example C: the points are $(t,t,0)$. The height is $0$ for every $t$, so every point of the line is in the plane. The dot product is $n\cdot v=(0,0,1)\cdot(1,1,0)=0$, and $n\cdot p=0=d$.

## Common mistakes
- Treating $n\cdot v=0$ as the end of the analysis. It only tells us the line is parallel, and a second test with $n\cdot p$ and $d$ is needed to separate case B from case C.
- Confusing the two vectors and testing $v$ against the plane equation instead of $n$.
- Saying that a line which is parallel to the plane always has no common points. When it lies in the plane, all its points are common.
- Dividing by $n\cdot v$ before checking whether it is zero.

## How I would explain it in class
We put the points of the line into the equation of the plane and get one simple equation for the parameter $t$. If the line goes through the plane at an angle, that equation has exactly one answer, which is the crossing point. If the line runs alongside the plane, the equation either has no answer, when the line floats above or below, or every number is an answer, when the line lies in the plane.
