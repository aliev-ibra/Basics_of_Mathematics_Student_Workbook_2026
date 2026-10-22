# Problem 11

## The original problem

Compare
$$x^2+y^2-z^2=1$$
and
$$x^2+y^2-z^2=-1.$$
For several values $z=c$, check whether the cross-section exists and what its radius is. Based on this, describe qualitatively the difference between the surfaces and make sketches.

## What we are looking for

We cut each surface with horizontal planes $z=c$ for several numbers $c$. For each cut we must decide whether any points exist, and if they do, find the radius of the circle. Then we use this information to say what each surface looks like, and in what way the two surfaces differ.

## The idea we need

Put $z=c$ into the equation and move the number $c^2$ to the right side. Then the left side is $x^2+y^2$, and an equation $x^2+y^2=r^2$ describes a circle of radius $r$ around the $z$-axis. This works only when the right-hand side is positive. If it is zero, there is one point. If it is negative, there is no point, because $x^2+y^2$ is never negative.

## Step-by-step solution

**First surface, $x^2+y^2-z^2=1$.**

Put $z=c$: $x^2+y^2=1+c^2$. The right side is always at least $1$, so it is always positive. A circle exists for every $c$, with radius $\sqrt{1+c^2}$.

| $c$ | $x^2+y^2=$ | radius |
|---|---|---|
| $0$ | $1$ | $1$ |
| $\pm1$ | $2$ | $\sqrt2\approx1.41$ |
| $\pm2$ | $5$ | $\sqrt5\approx2.24$ |
| $\pm3$ | $10$ | $\sqrt{10}\approx3.16$ |

The smallest circle is at $c=0$ with radius $1$. It is the narrowest place of the surface, the waist. Going up or down, the circles grow. So the surface is a single connected piece, shaped like a cooling tower or an hourglass with a hole through the middle. It extends without end both up and down. This surface is called the hyperboloid of one sheet.

**Second surface, $x^2+y^2-z^2=-1$.**

Put $z=c$: $x^2+y^2=c^2-1$. The right side is positive only if $c^2>1$, that is $|c|>1$.

| $c$ | $x^2+y^2=$ | what exists |
|---|---|---|
| $0$ | $-1$ | nothing |
| $\pm\frac12$ | $-\frac34$ | nothing |
| $\pm1$ | $0$ | one point $(0,0,\pm1)$ |
| $\pm2$ | $3$ | circle of radius $\sqrt3\approx1.73$ |
| $\pm3$ | $8$ | circle of radius $\sqrt8=2\sqrt2\approx2.83$ |

For $|c|<1$ the cut is empty, so there is a gap between the heights $-1$ and $1$. At $c=1$ the surface begins at the point $(0,0,1)$, then widens like a bowl facing upward. The same happens below $c=-1$ in mirror image. The surface consists of two separate pieces, one over the other, which do not touch. This is called the hyperboloid of two sheets.

**Vertical cuts, to confirm.** The plane $x=0$ gives $y^2-z^2=1$ for the first surface, a hyperbola crossing the $y$-axis at $(0,\pm1,0)$, whose two branches open to the left and right. For the second surface it gives $y^2-z^2=-1$, that is $z^2-y^2=1$, a hyperbola crossing the $z$-axis at $(0,0,\pm1)$, whose two branches open upward and downward. This explains the two names.

**The difference in one sentence.** Changing the right-hand side from $+1$ to $-1$ changes a connected surface with a waist into two separate bowls.

## Why each step is valid

Putting $z=c$ selects the points of the surface in that plane. Moving $c^2$ to the right side is ordinary algebra. The radius is the square root of the right side, since the circle $x^2+y^2=r^2$ has radius $r$.

The count of pieces follows from the table. For the first surface every height has a circle, so we can walk along the surface from any height to any other without leaving it. For the second surface there is no point of the surface at heights between $-1$ and $1$, so a path from the upper part to the lower part would have to pass through this empty zone, which is impossible. So there are two pieces.

## Final answer (in words)

For $x^2+y^2-z^2=1$ every plane $z=c$ cuts a circle of radius $\sqrt{1+c^2}$, with smallest radius $1$ at $c=0$. The surface is one connected piece with a narrow waist and flaring up and down: the hyperboloid of one sheet.

For $x^2+y^2-z^2=-1$ the plane $z=c$ cuts a circle of radius $\sqrt{c^2-1}$ only when $|c|>1$, one point when $|c|=1$, and nothing when $|c|<1$. The surface has two separate bowl-shaped pieces: the hyperboloid of two sheets.

## Verification

Substitute points into the original equations.

- First surface: $(1,0,0)$ gives $1+0-0=1$. The point $(\sqrt2,0,1)$ gives $2+0-1=1$. The point $(0,\sqrt5,2)$ gives $5-4=1$. All lie on the surface, with radii $1$, $\sqrt2$, $\sqrt5$ at heights $0$, $1$, $2$, matching the table.
- Second surface: $(0,0,1)$ gives $0+0-1=-1$. The point $(\sqrt3,0,2)$ gives $3-4=-1$. The point $(0,2\sqrt2,3)$ gives $8-9=-1$. All lie on the surface.
- A point with $z=0$ would need $x^2+y^2=-1$, which is impossible. So the gap is real.
- The first surface even contains straight lines: the points $(1,t,t)$ give $1+t^2-t^2=1$ for every $t$, which is a quick extra confirmation of the "hourglass" shape.

## Common mistakes

- Thinking the two surfaces differ only by their position. They are different in kind: one piece against two pieces.
- Writing the radius for the second surface as $\sqrt{1-c^2}$ or $\sqrt{c^2+1}$. The correct value is $\sqrt{c^2-1}$.
- Forgetting that at $|c|=1$ the cut is one point.
- Believing that a circle exists for every $c$ in the second case.
- Calling the radius of the first surface $1+c^2$ instead of its square root.

## How I would explain it in class

I put $z=c$ in the equation and read off the right-hand side of $x^2+y^2$. In the first surface it is $1+c^2$, always positive, so there is a circle at every height and the surface is one piece with a waist. In the second it is $c^2-1$, which is negative for $|c|<1$, so there is a gap and the surface falls into two separate bowls.
