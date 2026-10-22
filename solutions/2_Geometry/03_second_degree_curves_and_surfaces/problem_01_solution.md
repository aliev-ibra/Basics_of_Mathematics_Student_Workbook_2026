# Problem 01

## The original problem

Recognize the curves

$$x^2+y^2=9,$$

$$\frac{x^2}{16}+\frac{y^2}{9}=1,$$

$$y^2=8x,$$

$$\frac{x^2}{9}-\frac{y^2}{4}=1.$$

For each one, identify the most important features and make a sketch. Explain which parts of the equation let you recognize the type of curve.

## What we are looking for

We must name each curve, read its key measurements from the equation, and explain what in the equation gives the type.

## The idea we need

A second-degree curve is recognized by its canonical form. A circle has equal squared terms: $x^2+y^2=r^2$. An ellipse has a sum of squared terms with different positive denominators: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$. A parabola has one squared variable equal to a multiple of the other: $y^2=4px$. A hyperbola has a difference of squared terms: $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$.

## Step-by-step solution

1. $x^2+y^2=9$ matches $x^2+y^2=r^2$ with $r^2=9$, so $r=3$. It is a circle centered at $(0,0)$ with radius $3$.

2. $\frac{x^2}{16}+\frac{y^2}{9}=1$ matches the ellipse form with $a^2=16$ and $b^2=9$. Thus $a=4$ and $b=3$. The intercepts are $(\pm4,0)$ and $(0,\pm3)$.

3. $y^2=8x$ matches $y^2=4px$ with $4p=8$, so $p=2$. The vertex is $(0,0)$, the axis is the $x$-axis, and it opens to the right.

4. $\frac{x^2}{9}-\frac{y^2}{4}=1$ matches the hyperbola form with $a^2=9$ and $b^2=4$. Thus $a=3$, $b=2$, and the vertices are $(\pm3,0)$.

## Why each step is valid

Each equation is already in canonical form, so we only match coefficients with the standard template. The parameters are recovered by taking square roots of the denominators, and for the parabola by solving $4p=8$.

## Final answer (in words)

The first curve is a circle of radius $3$ centered at the origin. The second is an ellipse with semi-axes $4$ and $3$. The third is a parabola with vertex at the origin opening right. The fourth is a hyperbola with vertices $(\pm3,0)$.

## Verification

Check the circle: the point $(3,0)$ satisfies $3^2+0^2=9$. Check the ellipse: $(4,0)$ gives $16/16+0=1$. Check the parabola: for $x=2$, $y^2=16$, so $y=\pm4$, and $4^2=16$. Check the hyperbola: $(3,0)$ gives $9/9-0=1$.

## Common mistakes

- Confusing an ellipse with a circle when the denominators differ.
- Reading $y^2=8x$ as an ellipse instead of a parabola.
- Forgetting that a hyperbola has two branches.
- Mixing up $a$ and $b$ with their squares.

## How I would explain it in class

I look at the structure of the equation first, not the numbers. A sum of equal squares is a circle, a sum of unequal squares is an ellipse, one squared variable equals a linear term is a parabola, and a difference is a hyperbola. Then I read the parameters from the denominators or coefficients.