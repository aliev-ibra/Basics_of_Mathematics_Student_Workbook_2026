# Problem 05

## The original problem

For

$$\frac{x^2}{16}-\frac{y^2}{9}=1,$$

find the intercepts with the $x$-axis, the asymptotes, and make a sketch. Explain why the asymptotes describe the behavior of the curve far from the center.

## What we are looking for

We need the $x$-intercepts, the asymptote equations, and an explanation of their role.

## The idea we need

A hyperbola $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ has vertices $(\pm a,0)$ and asymptotes $y=\pm\frac{b}{a}x$. Far from the center the hyperbola approaches these lines.

## Step-by-step solution

Here $a^2=16$, so $a=4$, and $b^2=9$, so $b=3$.

$x$-intercepts: set $y=0$: $\frac{x^2}{16}=1$, so $x=\pm4$. Points: $(4,0)$ and $(-4,0)$.

Asymptotes: $y=\pm\frac{b}{a}x=\pm\frac{3}{4}x$.

Far from the center, the constant $1$ becomes negligible compared with the squared terms, so $\frac{x^2}{16}-\frac{y^2}{9}\approx0$, giving $y\approx\pm\frac{3}{4}x$.

## Why each step is valid

The vertices come from the standard hyperbola form. The asymptotes are found by replacing the right-hand side $1$ with $0$. The approximation is valid for large $|x|$ and $|y|$.

## Final answer (in words)

The hyperbola has $x$-intercepts $(\pm4,0)$ and asymptotes $y=\pm\frac34 x$.

## Verification

Check $(4,0)$: $16/16-0=1$. For large $x$, take $x=100$: then $y\approx\pm75$, and $\frac{10000}{16}-\frac{5625}{9}=625-625=0$ plus $1$, consistent with the asymptote.

## Common mistakes

- Writing asymptotes as $y=\pm\frac{a}{b}x$ instead of $\frac{b}{a}x$.
- Forgetting the hyperbola has no $y$-intercepts.
- Mixing the roles of $a$ and $b$.

## How I would explain it in class

I read $a$ and $b$ from the denominators, then the vertices and asymptotes follow. The asymptotes come from setting the equation to zero, which describes the curve far away. This explains the global shape.