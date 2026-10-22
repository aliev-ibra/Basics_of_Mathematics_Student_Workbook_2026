# Problem 12

## The original problem

A certain surface has the following properties:
- the cross-section $z=0$ is a point,
- for $z>0$, the cross-sections $z=\text{const}$ are circles with increasing radius,
- vertical cross-sections through the $Oz$ axis are parabolas.

Propose a simple equation for such a surface and justify your choice.

## What we are looking for

We must invent an equation, and then show that it really has all three properties. A good answer has two parts: a choice, and a check that the choice works. We also explain why a tempting alternative does not fit.

## The idea we need

Surfaces whose horizontal cuts are circles around the $z$-axis depend on $x$ and $y$ only through the combination $x^2+y^2$, which is the squared distance from the $z$-axis. So we look for an equation $z=f(x^2+y^2)$, or the other way round.

The third property says the vertical cut is a parabola. A parabola is the graph of a square, for example $z=t^2$. So the height must be equal to the square of the horizontal distance. That suggests $z=x^2+y^2$.

## Step-by-step solution

**Proposal.**
$$z=x^2+y^2.$$

**Property 1: the cut $z=0$.** Put $z=0$: $x^2+y^2=0$. A sum of two squares is zero only when both are zero, so $x=0$ and $y=0$. The cut is the single point $(0,0,0)$, the origin. Correct.

**Property 2: the cuts $z=c$ with $c>0$.** Put $z=c$: $x^2+y^2=c$. This is a circle around the $z$-axis with radius $\sqrt c$. When $c$ grows, $\sqrt c$ grows. For example, at height $1$ the radius is $1$, at height $4$ it is $2$, at height $9$ it is $3$. So the circles have increasing radius. Correct.

**Property 3: vertical cuts through the $Oz$ axis.** A vertical plane through the $z$-axis is the set of points where $y=mx$ for some number $m$ (or the plane $x=0$). Take $y=mx$. Then
$$z=x^2+m^2x^2=(1+m^2)x^2.$$
On this plane, the horizontal distance from the $z$-axis is $t=x\sqrt{1+m^2}$ (measured along the line in the plane), and the equation becomes $z=t^2$. This is a parabola with its vertex at the origin, opening upward. For the plane $x=0$ we get directly $z=y^2$, again a parabola. Correct.

**The shape.** The surface is a round bowl with its bottom at the origin, opening upward, like a satellite dish or a wine glass. It is called the circular paraboloid.

**Why not another surface.** The cone $z^2=x^2+y^2$ also has a point at $z=0$ and circles of growing radius. But its vertical cuts through the axis are the two lines $z=\pm|x|$, not parabolas. So the cone fails the third property. The ellipsoid has circles that first grow and then shrink, so it fails the second.

**What is not fixed.** The three properties do not fix the scale. Any equation $z=k(x^2+y^2)$ with $k>0$ works as well. We took $k=1$ because it is the simplest. For $z<0$ the surface has no points, and the problem says nothing about this region, so this is allowed.

## Why each step is valid

The proposal is justified by checking each property directly, using only substitution. This is the correct logic for an inverse problem: we are not asked to prove that the surface is the only possible one (it is not, because of the scale $k$), only to give one equation and show that it meets all the requirements.

The step about the plane $y=mx$ is valid because every vertical plane that contains the $z$-axis has this form, apart from $x=0$, which we checked separately. The substitution of $y=mx$ keeps exactly the points of the surface lying in that plane.

## Final answer (in words)

One equation that works is $z=x^2+y^2$, a circular paraboloid. At height $0$ it touches the plane at the origin only. At height $c>0$ its cut is a circle of radius $\sqrt c$, which grows with the height. Every vertical plane through the $z$-axis cuts it along the parabola $z=(1+m^2)x^2$. Any $z=k(x^2+y^2)$ with $k>0$ would also fit.

## Verification

Test points independently from the derivation.

- The point $(0,0,0)$ satisfies $0=0+0$, and no other point has $z=0$, since $x^2+y^2=0$ forces $x=y=0$.
- At height $4$ the point $(2,0,4)$ satisfies $4=4+0$, and so does $(0,-2,4)$ and $(\sqrt2,\sqrt2,4)$, because $2+2=4$. All three are at distance $2$ from the axis, so they are on one circle of radius $2$.
- In the plane $y=x$, the point $(1,1,2)$ satisfies $2=1+1$. The formula gives $z=(1+1)x^2=2$. The parameter $t=x\sqrt2=\sqrt2$ gives $t^2=2$. Consistent.
- The point $(0,0,-1)$ would need $-1=0$, which is false, so nothing lies below the plane $z=0$.

## Common mistakes

- Proposing the cone $z^2=x^2+y^2$ because the first two properties fit. The vertical cuts are lines, not parabolas.
- Writing $z=x^2-y^2$, which has no circles at all.
- Writing $z=\sqrt{x^2+y^2}$, which is the upper half of the cone.
- Only checking one property and calling the proposal justified.
- Claiming that the answer is unique, although $z=k(x^2+y^2)$ also works.

## How I would explain it in class

Circles around the $z$-axis tell me the equation uses $x^2+y^2$, and a parabola tells me the height is a square of the distance, so I propose $z=x^2+y^2$. Then I check each property: at $z=0$ only the origin remains, at height $c$ I get a circle of radius $\sqrt c$, and in the plane $y=mx$ I get $z=(1+m^2)x^2$, a parabola. The cone is not suitable, because its vertical cuts are straight lines.
