# Problem 10

## The original problem

Compare
$$z=x^2+y^2$$
and
$$z=x^2-y^2.$$
For each surface, describe the cross-sections $x=0$, $y=0$, and $z=c$, then make a qualitative sketch.

## What we are looking for

We have two surfaces. For each one we must find three families of flat curves: the cut by the plane $x=0$ (the plane that contains the $y$-axis and the $z$-axis), the cut by the plane $y=0$, and the cuts by horizontal planes $z=c$. Then we describe what the surface looks like and say how the two surfaces differ.

## The idea we need

To cut a surface, we put the value of one variable into its equation and see which curve remains in the other two variables. Horizontal cuts $z=c$ are also called level curves, because all their points are at the same height.

A parabola is the graph of a square, such as $z=y^2$. It is a U-shaped curve, opening up for $z=y^2$ and opening down for $z=-y^2$. A hyperbola is the curve $x^2-y^2=c$ with $c\neq0$. It has two separate branches.

## Step-by-step solution

### The surface $z=x^2+y^2$

**Cut $x=0$.** The equation becomes $z=y^2$. This is a parabola in the $yz$-plane. Its lowest point is the origin and it opens upward.

**Cut $y=0$.** The equation becomes $z=x^2$, an upward parabola in the $xz$-plane with the same lowest point.

**Cut $z=c$.** The equation becomes $x^2+y^2=c$.

- If $c<0$, a sum of squares cannot be negative, so there are no points.
- If $c=0$, then $x=y=0$, so the cut is the single point at the origin.
- If $c>0$, the cut is a circle with center on the $z$-axis and radius $\sqrt c$.

**The shape.** Circles of growing radius are stacked above a single point. The result is a round bowl or cup, open upward, with its bottom at the origin. The radius grows like the square root of the height, so the bowl is steep near the bottom and gets flatter in profile higher up. This surface is called the circular paraboloid, or paraboloid of revolution.

### The surface $z=x^2-y^2$

**Cut $x=0$.** The equation becomes $z=-y^2$. This is a parabola opening downward, with its top at the origin.

**Cut $y=0$.** The equation becomes $z=x^2$. This is a parabola opening upward, with its bottom at the origin.

So at the origin the surface curves up in one direction and down in the other.

**Cut $z=c$.** The equation becomes $x^2-y^2=c$.

- If $c>0$, this is a hyperbola whose two branches cross the $x$-axis at $x=\pm\sqrt c$ and open left and right.
- If $c<0$, it is a hyperbola whose two branches cross the $y$-axis at $y=\pm\sqrt{-c}$ and open upward and downward in the plane, along the $y$ direction.
- If $c=0$, then $x^2=y^2$, so $y=x$ or $y=-x$. This is a pair of straight lines crossing at the origin.

**The shape.** The surface looks like a horse saddle or a mountain pass. Going along the $x$-axis we climb, going along the $y$-axis we descend. The origin is the saddle point: it is neither a top nor a bottom. This surface is called the hyperbolic paraboloid.

### Comparison table

| cut | $z=x^2+y^2$ | $z=x^2-y^2$ |
|---|---|---|
| $x=0$ | parabola $z=y^2$, opens up | parabola $z=-y^2$, opens down |
| $y=0$ | parabola $z=x^2$, opens up | parabola $z=x^2$, opens up |
| $z=c>0$ | circle of radius $\sqrt c$ | hyperbola, vertices $(\pm\sqrt c,0)$ |
| $z=0$ | one point | two crossing lines $y=\pm x$ |
| $z=c<0$ | no points | hyperbola, vertices $(0,\pm\sqrt{-c})$ |

## Why each step is valid

Each cut is obtained by substituting a fixed value into the equation, which keeps exactly those points of the surface that lie in the chosen plane.

For the first surface, a sum of two squares is never negative, so for $c<0$ no solution exists. A circle $x^2+y^2=r^2$ has radius $r$, here $r=\sqrt c$.

For the second surface, the difference $x^2-y^2$ can be positive, zero or negative, so every value of $c$ is possible. This is the algebraic reason why the saddle exists at all heights, while the bowl exists only above the origin. For $c=0$ we use $x^2-y^2=(x-y)(x+y)=0$, which gives the two lines.

## Final answer (in words)

The surface $z=x^2+y^2$ is a round bowl opening upward. Its vertical cuts through the axes are upward parabolas, and its horizontal cuts are circles of radius $\sqrt c$ for $c>0$, a point for $c=0$, and nothing for $c<0$.

The surface $z=x^2-y^2$ is a saddle. The cut $x=0$ is a downward parabola, the cut $y=0$ is an upward parabola, and the horizontal cuts are hyperbolas, which become two crossing lines at $c=0$.

## Verification

Check points in the equations.

- Bowl: the point $(1,0,1)$ gives $1^2+0^2=1=z$. The point $(0,2,4)$ gives $0+4=4$. The point $(1,1,2)$ gives $2$. All lie on the surface and are consistent with the circles: at height $1$ the radius is $1$, at height $4$ it is $2$, at height $2$ it is $\sqrt2$, which equals the distance of $(1,1)$ from the axis.
- Saddle: the point $(1,0,1)$ gives $1-0=1=z$. The point $(0,1,-1)$ gives $0-1=-1=z$. The point $(2,1,3)$ gives $4-1=3$. The point $(1,2,-3)$ gives $1-4=-3$. The last one lies on the hyperbola $z=-3$ with vertices $(0,\pm\sqrt3)$, and indeed $y=2$ is on the branch.
- The point $(1,1,0)$ lies on the saddle (since $1-1=0$) and on the line $y=x$, as required for $c=0$.

## Common mistakes

- Saying that both surfaces are "bowls" because both contain the parabola $z=x^2$.
- Forgetting that the bowl has no points below the plane $z=0$.
- Saying the cut $z=c$ of the saddle is an ellipse or a circle. It is a hyperbola.
- Mixing up which way the hyperbola opens: for $c>0$ it opens along $x$, for $c<0$ along $y$.
- Forgetting the special case $c=0$ in both surfaces.

## How I would explain it in class

For both surfaces I cut with $x=0$, $y=0$ and $z=c$, which means I substitute one value and look at what remains. In the first surface the horizontal cuts are circles, so it is a bowl with its bottom at the origin. In the second the horizontal cuts are hyperbolas and the two vertical cuts bend in opposite directions, so it is a saddle.
