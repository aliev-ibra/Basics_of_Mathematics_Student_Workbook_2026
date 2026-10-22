# Problem 14

## The original problem

Compare
$$x^2+y^2=z^2$$
and
$$x^2+y^2=4.$$
For each surface, describe the cross-sections $z=c$, $x=0$, and $y=0$, make a sketch, and explain why the radius of the cross-section depends on $z$ in the first case but is constant in the second.

## What we are looking for

We have two surfaces in space. For each of them we need the curves cut out by the planes $z=c$ (horizontal), $x=0$ and $y=0$ (the two vertical planes through the $z$-axis). We then describe each surface in words, and explain why the radius of the horizontal circle changes with height in one case and stays fixed in the other.

## The idea we need

In both equations the left side $x^2+y^2$ is the square of the distance of a point from the $z$-axis. So both surfaces are built from circles around the $z$-axis. The only question is what the right side says about the radius: in the first equation it is $z^2$, which depends on the height, and in the second it is the number $4$, which does not.

## Step-by-step solution

### The surface $x^2+y^2=z^2$

**Cut $z=c$.** We get $x^2+y^2=c^2$. This is a circle around the $z$-axis with radius $|c|$. At $c=0$ the radius is $0$, so the cut is one point, the origin. At $c=1$ and $c=-1$ the radius is $1$, at $c=\pm3$ it is $3$.

**Cut $x=0$.** We get $y^2=z^2$, so $z=y$ or $z=-y$. These are two straight lines in the plane $x=0$, crossing at the origin.

**Cut $y=0$.** We get $x^2=z^2$, so $z=x$ or $z=-x$. Again two lines crossing at the origin.

**The shape.** The surface is a double cone: two round cones joined at their tips at the origin, one opening upward and one downward. The slope is $45$ degrees, because the radius equals the height. Both cones continue forever.

### The surface $x^2+y^2=4$

**Cut $z=c$.** The variable $z$ does not appear in the equation, so the equation does not change with $c$. For every $c$ we get the same circle $x^2+y^2=4$ with radius $2$ around the $z$-axis.

**Cut $x=0$.** We get $y^2=4$, so $y=2$ or $y=-2$. In the plane $x=0$ these are two vertical straight lines, parallel to the $z$-axis, at distance $2$ on either side of it.

**Cut $y=0$.** We get $x^2=4$, so $x=\pm2$, again two vertical parallel lines.

**The shape.** The surface is a round tube or pipe of radius $2$ around the $z$-axis, going up and down without end. It is called a circular cylinder.

### Comparison table

| cut | cone $x^2+y^2=z^2$ | cylinder $x^2+y^2=4$ |
|---|---|---|
| $z=c$ | circle of radius $|c|$, point at $c=0$ | circle of radius $2$ for every $c$ |
| $x=0$ | lines $z=y$ and $z=-y$, crossing | lines $y=2$ and $y=-2$, parallel |
| $y=0$ | lines $z=x$ and $z=-x$, crossing | lines $x=2$ and $x=-2$, parallel |

### Why the radius depends on $z$ or not

For the cone, the radius squared is $x^2+y^2$, and the equation says that it must be equal to $z^2$. So the radius is tied to the height: higher means wider. For the cylinder the equation does not contain $z$ at all, so the height has no influence, and the radius is the fixed number $\sqrt4=2$. In short: the variable $z$ appears in one equation and is absent from the other.

## Why each step is valid

Each cut is found by putting a fixed value of one variable into the equation. The step $y^2=z^2\Rightarrow z=\pm y$ is valid because two numbers with equal squares are equal or opposite. The same holds for $x^2=4$.

For the cylinder, the freedom of $z$ is real: if a point $(x,y,z)$ satisfies the equation, then $(x,y,z')$ satisfies it for every $z'$, because $z$ is not used. So the surface is made of whole vertical lines.

## Final answer (in words)

The surface $x^2+y^2=z^2$ is a double cone. Its horizontal cuts are circles of radius $|c|$ (a point at $c=0$), and its cuts $x=0$ and $y=0$ are pairs of crossing lines. The surface $x^2+y^2=4$ is a circular cylinder of radius $2$. Its horizontal cuts are always the circle of radius $2$, and its cuts $x=0$ and $y=0$ are pairs of parallel vertical lines. The radius depends on $z$ in the first equation because $z$ appears on the right side. In the second equation it does not, so the radius stays $2$.

## Verification

Substitute points.

- Cone: $(1,0,1)$ gives $1=1$. The point $(0,3,-3)$ gives $9=9$. The point $(3,4,5)$ gives $25=25$, and its distance from the axis is $5=|z|$, as the radius rule says. The point $(1,0,2)$ gives $1\neq4$, so it is not on the cone.
- Cylinder: $(2,0,5)$ gives $4=4$. The point $(0,-2,7)$ gives $4=4$. The point $(\sqrt2,\sqrt2,-1)$ gives $2+2=4$. The same $(x,y)$ works for all heights, which confirms that the radius does not depend on $z$.
- The point $(1,0,0)$ gives $1\neq4$, so it is inside the tube and not on it.

## Common mistakes

- Saying that the cut $x=0$ of the cone is a parabola or a hyperbola. It is a pair of crossing lines.
- Saying that the cut $x=0$ of the cylinder is a circle. It is two parallel lines.
- Forgetting the lower half of the cone (negative $z$).
- Believing that the equation $x^2+y^2=4$ in space is a circle. In space it is a cylinder, because $z$ is free.
- Forgetting that the cone cut at $c=0$ is a point.

## How I would explain it in class

Both equations say that the distance from the $z$-axis is a fixed rule: for the cone it equals $|z|$, for the cylinder it equals $2$. So the cone cuts are circles that grow with height and the cylinder cuts are the same circle at every height. The vertical cuts show the same difference, crossing lines for the cone and parallel lines for the cylinder.
