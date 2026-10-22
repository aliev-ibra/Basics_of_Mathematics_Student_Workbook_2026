# Problem 09

## The original problem

Consider
$$\frac{x^2}{9}+\frac{y^2}{4}+\frac{z^2}{16}=1.$$
Give the semiaxis lengths, describe the cross-section $z=0$, and explain how the cross-sections $z=c$ change for $|c|<4$.

## What we are looking for

We need three things. First, the three semiaxis lengths of the surface, that is, how far it reaches from the center along each coordinate axis. Second, the shape of the cross-section by the plane $z=0$. Third, a description of how the cross-section by the plane $z=c$ changes as the number $c$ moves between $-4$ and $4$. A cross-section means the curve we get when we cut the surface with a flat plane.

## The idea we need

An equation of the form
$$\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c_0^2}=1$$
with positive numbers $a,b,c_0$ describes an ellipsoid. It is a closed, egg-like surface, a sphere stretched by different amounts along the three axes. The numbers $a,b,c_0$ are the semiaxes. They are the square roots of the denominators.

The way to understand a surface in space is to cut it with the planes $z=c$. Each plane gives a flat curve, and a family of flat curves tells us the whole shape. To cut, we put $z=c$ into the equation and move the $z$-term to the right side.

## Step-by-step solution

**Step 1: semiaxes.** The denominators are $9$, $4$, $16$. Their square roots are $3$, $2$, $4$. So the semiaxis along the $x$-axis is $3$, along the $y$-axis is $2$, along the $z$-axis is $4$. The surface meets the axes at $(\pm3,0,0)$, $(0,\pm2,0)$ and $(0,0,\pm4)$. The longest direction is $z$, the shortest is $y$.

**Step 2: the cross-section $z=0$.** Put $z=0$. The term $\frac{z^2}{16}$ disappears and we get
$$\frac{x^2}{9}+\frac{y^2}{4}=1.$$
This is a flat ellipse in the plane $z=0$. It is centered at the origin, reaches $\pm3$ along the $x$-axis and $\pm2$ along the $y$-axis. It is the widest cross-section of the surface, its "equator".

**Step 3: the cross-section $z=c$.** Put $z=c$ and move $\frac{c^2}{16}$ to the right side:
$$\frac{x^2}{9}+\frac{y^2}{4}=1-\frac{c^2}{16}=\frac{16-c^2}{16}.$$
If $|c|<4$, then $c^2<16$, so the right side is a positive number. Call it $k=\frac{16-c^2}{16}$. Dividing both sides by $k$ gives
$$\frac{x^2}{9k}+\frac{y^2}{4k}=1.$$
This is again an ellipse, with semiaxes $3\sqrt k$ along $x$ and $2\sqrt k$ along $y$. Since $\sqrt k=\frac{\sqrt{16-c^2}}{4}$, the semiaxes are
$$\frac{3}{4}\sqrt{16-c^2}\quad\text{and}\quad\frac{1}{2}\sqrt{16-c^2}.$$

**Step 4: how the ellipses change.** The ratio of the two semiaxes is always $3:2$, so every cross-section has the same shape and only its size changes. The size is largest at $c=0$ and shrinks as $|c|$ grows. The table shows several levels.

| level $z=c$ | semiaxis along $x$ | semiaxis along $y$ | what we see |
|---|---|---|---|
| $0$ | $3$ | $2$ | the largest ellipse |
| $\pm2$ | $\frac{3\sqrt3}{2}\approx2.60$ | $\sqrt3\approx1.73$ | a smaller ellipse |
| $\pm3$ | $\frac{3\sqrt7}{4}\approx1.98$ | $\frac{\sqrt7}{2}\approx1.32$ | smaller still |
| $\pm4$ | $0$ | $0$ | a single point $(0,0,\pm4)$ |
| $|c|>4$ | none | none | the plane misses the surface |

**Step 5: the picture.** The sketch shows a smooth closed shape, like a rugby ball standing on its tip but with an oval, not round, belt. The belt is the ellipse $z=0$. Going up or down, the ovals shrink and close into the top point $(0,0,4)$ and the bottom point $(0,0,-4)$. Cutting with $x=0$ gives the ellipse $\frac{y^2}{4}+\frac{z^2}{16}=1$, and cutting with $y=0$ gives $\frac{x^2}{9}+\frac{z^2}{16}=1$. Both are tall ovals.

## Why each step is valid

The semiaxes are read from the equation because setting two variables to zero leaves one equation of the form $\frac{x^2}{9}=1$, whose solutions are $x=\pm3$, and the same for the other axes.

Putting $z=c$ is exactly what it means to look at the points of the surface lying in the plane $z=c$. Dividing by $k$ is allowed only when $k\neq0$. If $k>0$ we get an ellipse. If $k=0$, that is $c=\pm4$, the equation $\frac{x^2}{9}+\frac{y^2}{4}=0$ has only the solution $x=y=0$, one point. If $k<0$, the left side is never negative, so no point exists. This is why the condition $|c|<4$ is exactly the condition for a real ellipse.

## Final answer (in words)

The semiaxes are $3$ along $x$, $2$ along $y$ and $4$ along $z$. The cross-section $z=0$ is the ellipse $\frac{x^2}{9}+\frac{y^2}{4}=1$ with semiaxes $3$ and $2$. For $|c|<4$ the cross-section $z=c$ is an ellipse with semiaxes $\frac34\sqrt{16-c^2}$ and $\frac12\sqrt{16-c^2}$. It always has the proportions $3:2$, it is largest at $c=0$, and it shrinks to a point as $|c|$ approaches $4$.

## Verification

I check points directly in the original equation.

- The point $(3,0,0)$: $\frac99+0+0=1$. The point $(0,0,-4)$: $0+0+\frac{16}{16}=1$. Both lie on the surface.
- A point at level $c=2$: the formula gives the vertex $\left(\frac{3\sqrt3}{2},0,2\right)$. Then $x^2=\frac{27}{4}$, so $\frac{x^2}{9}=\frac34$, and $\frac{z^2}{16}=\frac4{16}=\frac14$. The sum is $\frac34+\frac14=1$. Correct.
- The other vertex at that level is $(0,\sqrt3,2)$. Then $\frac{y^2}{4}=\frac34$ and again $\frac{z^2}{16}=\frac14$, sum $1$. Correct.
- A point outside the range: at $c=5$ the right side would be $1-\frac{25}{16}<0$, and the left side cannot be negative, so there is no point, as the table says.

## Common mistakes

- Saying the semiaxes are $9$, $4$, $16$. These are the squares. The semiaxes are $3$, $2$, $4$.
- Thinking the cross-section $z=c$ keeps the size of the ellipse $z=0$. It shrinks.
- Forgetting that the proportions stay the same, so that only the size changes.
- Writing the condition as $|c|<16$ instead of $|c|<4$.
- Forgetting the two end points $c=\pm4$, where the cross-section is one point.

## How I would explain it in class

We read the semiaxes as the square roots of the denominators, which gives $3$, $2$ and $4$. Cutting at height $c$ leaves an ellipse whose right-hand side is $1-\frac{c^2}{16}$, so the ellipse shrinks as we leave the middle and becomes a single point at $c=\pm4$. This is why the surface is a closed oval body, and the cuts at $c=0$ and $c=2$ confirm it when we substitute their points back into the equation.
