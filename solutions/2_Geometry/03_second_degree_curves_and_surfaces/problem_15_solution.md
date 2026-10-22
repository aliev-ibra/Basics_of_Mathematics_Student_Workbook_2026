# Problem 15

## The original problem

Consider the two equations:

$$4x^2+9y^2-8x+36y+4=0,$$

$$4x^2+y^2=z^2.$$

For the first equation, reduce it to canonical form, recognize the curve, give its most important features, and make a sketch.

For the second equation, do not begin by using a ready-made name for the surface. First describe the cross-sections $z=c$ and the cross-sections by the planes $x=0$ and $y=0$, paying attention to the different scales along the axes. Only then identify the surface and make a sketch.

## What we are looking for

Part one: we must rewrite the first equation in canonical form, which is a standard form from which the type of curve can be read, say which curve it is, and list its center, semiaxes and special points.

Part two: we must study the surface $4x^2+y^2=z^2$ by cutting it with the planes $z=c$, $x=0$ and $y=0$, describe what we see, and only after that give the surface its name.

## The idea we need

For part one we use completing the square. An expression $4x^2-8x$ is rewritten as $4(x-1)^2-4$. This shifts the picture so that the center sits at a convenient point. After dividing so that the right side is $1$, an equation $\frac{(x-p)^2}{a^2}+\frac{(y-q)^2}{b^2}=1$ is an ellipse with center $(p,q)$ and semiaxes $a$ and $b$.

For part two we use cross-sections. A cross-section is the curve in which a plane cuts the surface. We substitute the value of one variable and look at the remaining equation in two variables.

## Step-by-step solution

### Part one: the curve

**Step 1: group the terms.**
$$4x^2-8x+9y^2+36y+4=0.$$

**Step 2: complete the square in $x$.** Take out the factor $4$: $4x^2-8x=4(x^2-2x)=4\big((x-1)^2-1\big)=4(x-1)^2-4$.

**Step 3: complete the square in $y$.** Take out the factor $9$: $9y^2+36y=9(y^2+4y)=9\big((y+2)^2-4\big)=9(y+2)^2-36$.

**Step 4: put back and collect numbers.**
$$4(x-1)^2-4+9(y+2)^2-36+4=0,$$
and $-4-36+4=-36$, so
$$4(x-1)^2+9(y+2)^2=36.$$

**Step 5: divide by $36$.**
$$\frac{(x-1)^2}{9}+\frac{(y+2)^2}{4}=1.$$

**Step 6: read the curve.** This is an ellipse. Its center is $(1,-2)$. The semiaxis in the $x$ direction is $\sqrt9=3$, and in the $y$ direction is $\sqrt4=2$. So the ellipse is wider than it is tall.

**Important points.**

- The ends of the horizontal axis: $(1\pm3,-2)$, that is $(4,-2)$ and $(-2,-2)$.
- The ends of the vertical axis: $(1,-2\pm2)$, that is $(1,0)$ and $(1,-4)$.
- Intersection with the $x$-axis ($y=0$): the original equation becomes $4x^2-8x+4=0$, so $4(x-1)^2=0$ and $x=1$. The ellipse touches the $x$-axis at the single point $(1,0)$.
- Intersection with the $y$-axis ($x=0$): $9y^2+36y+4=0$, giving $y=-2\pm\frac{4\sqrt2}{3}$, about $-0.11$ and $-3.89$.

**Sketch.** The picture shows an oval centered at $(1,-2)$, below the $x$-axis. It spans from $x=-2$ to $x=4$ and from $y=-4$ to $y=0$. Its top touches the $x$-axis exactly at $(1,0)$. It crosses the $y$-axis at two points, near $(0,-0.11)$ and $(0,-3.89)$.

### Part two: the surface $4x^2+y^2=z^2$

**Cut $z=c$.** We get $4x^2+y^2=c^2$.

- For $c=0$: $4x^2+y^2=0$ forces $x=y=0$, so the cut is the origin.
- For $c\neq0$: divide by $c^2$ to get $\frac{x^2}{(c/2)^2}+\frac{y^2}{c^2}=1$. This is an ellipse centered on the $z$-axis, with semiaxis $\frac{|c|}{2}$ along $x$ and $|c|$ along $y$.

The scales differ: the ellipse is twice as long in the $y$ direction as in the $x$ direction. The reason is that $x$ is multiplied by $2$ in the equation, so $x$ needs to be half as large to give the same contribution. The shape of the ellipse is the same at each height, and its size grows in proportion to $|c|$.

| height $c$ | semiaxis along $x$ | semiaxis along $y$ |
|---|---|---|
| $0$ | $0$ | $0$ |
| $\pm1$ | $\frac12$ | $1$ |
| $\pm2$ | $1$ | $2$ |
| $\pm4$ | $2$ | $4$ |

**Cut $x=0$.** We get $y^2=z^2$, so $z=y$ or $z=-y$: two straight lines crossing at the origin.

**Cut $y=0$.** We get $4x^2=z^2$, so $z=2x$ or $z=-2x$: two straight lines crossing at the origin. They are steeper than the previous ones, because along the $x$ direction the surface widens more slowly.

**Identify and sketch.** Elliptical cuts growing in proportion to the height, together with straight-line cuts through the axis, describe a cone whose cross-section is an ellipse instead of a circle. It is the elliptic cone, a double cone with tip at the origin, one part opening upward and one downward. The sketch shows two oval funnels meeting at their tips. They are wider in the $y$ direction than in the $x$ direction.

## Why each step is valid

Completing the square is an exact rewriting. Expanding $4(x-1)^2+9(y+2)^2-36$ gives $4x^2-8x+4+9y^2+36y+36-36$, which equals the original left side minus $0$, so no information is lost. Dividing by $36$ is allowed because $36\neq0$.

An equation of the form $\frac{X^2}{a^2}+\frac{Y^2}{b^2}=1$ with $X=x-1$ and $Y=y+2$ is the ellipse centered at the origin of the $(X,Y)$ system, which is the point $(1,-2)$ of the original system.

For the surface, each cut keeps exactly the points in the chosen plane. The conclusion that the surface is a cone follows from the fact that all the cuts $z=c$ are similar ellipses with size proportional to $|c|$, and the surface is made of straight lines through the origin.

## Final answer (in words)

The curve $4x^2+9y^2-8x+36y+4=0$ is the ellipse
$$\frac{(x-1)^2}{9}+\frac{(y+2)^2}{4}=1$$
with center $(1,-2)$, semiaxes $3$ along $x$ and $2$ along $y$, and touching the $x$-axis at $(1,0)$.

The surface $4x^2+y^2=z^2$ has elliptical cuts $z=c$ with semiaxes $\frac{|c|}{2}$ and $|c|$ (only the origin at $c=0$), and line-pair cuts $z=\pm y$ for $x=0$ and $z=\pm2x$ for $y=0$. It is an elliptic cone with its tip at the origin.

## Verification

Curve. Substitute special points of the ellipse into the original equation.

- $(4,-2)$: $4\cdot16+9\cdot4-32-72+4=64+36-32-72+4=0$. Correct.
- $(-2,-2)$: $16+36+16-72+4=0$. Correct.
- $(1,0)$: $4+0-8+0+4=0$. Correct.
- $(1,-4)$: $4+144-8-144+4=0$. Correct.
- The center $(1,-2)$ is inside, and the left side gives $4+36-8-72+4=-36$, which equals $4\cdot0+9\cdot0-36$, consistent with the form $4(x-1)^2+9(y+2)^2-36$.

Surface. Substitute points.

- $(1,0,2)$ gives $4+0=4=z^2$. Correct.
- $(0,2,2)$ gives $0+4=4$. Correct. At height $2$, these are the ends of the semiaxes $1$ and $2$.
- $(0,3,3)$ gives $9=9$ and $(1,0,-2)$ gives $4=4$. Correct.
- $\left(\frac12,1,\sqrt2\right)$ gives $1+1=2=z^2$. It lies on the ellipse at height $\sqrt2$, which confirms the cut.

## Common mistakes

- Dividing by the wrong number, for example dividing the whole equation by $4$ and keeping the number $9$ in a denominator.
- Forgetting to subtract the numbers $4$ and $36$ that appear when completing the square.
- Writing the center as $(-1,2)$, the opposite signs. The factors $x-1$ and $y+2$ give $(1,-2)$.
- Swapping the semiaxes, so that the ellipse is made taller instead of wider.
- Calling the second surface a circular cone because the cuts are called "circles". The coefficient $4$ makes the cuts ellipses.
- Forgetting that the lines in the cut $y=0$ are $z=\pm2x$ and not $z=\pm x$.

## How I would explain it in class

For the first equation I complete the square in $x$ and in $y$, move the numbers to the right side and divide by $36$, which gives an ellipse centered at $(1,-2)$ with semiaxes $3$ and $2$. For the second equation I look at the cuts first: horizontal cuts are ellipses twice as long in $y$ as in $x$ and growing with the height, and the vertical cuts through the axes are pairs of crossing lines. This is why I call the surface an elliptic cone.
