# Problem 3

## The original problem

Analyze the domain, zeros, asymptotes, and monotonicity of

$$f(x)=\frac{x+1}{x-2}.$$

Finally, sketch a graph consistent with all the information obtained.

## What we are looking for

We want to find where the function is defined, where it equals zero, what its asymptotes are, and on which intervals it increases or decreases, then use all of this to sketch the graph.

## The idea we need

For a rational function, the domain excludes values that make the denominator zero. A vertical asymptote occurs at a point excluded from the domain where the function blows up. A horizontal asymptote is found from the limit as $x\to\pm\infty$. The derivative sign determines monotonicity: if $f'(x)>0$ on an interval, the function increases; if $f'(x)<0$, it decreases. Since the domain is split by the vertical asymptote, we analyze each side separately.

## Step-by-step solution

1. Domain: the denominator $x-2$ is zero when $x=2$, so the domain is

   $$\{x\in\mathbb{R}:x\ne2\}=(-\infty,2)\cup(2,\infty).$$

2. Zero of the function: $f(x)=0$ when the numerator is zero and the denominator is not:

   $$x+1=0\implies x=-1.$$

   At $x=-1$, the denominator is $-1-2=-3\ne0$, so $x=-1$ is a zero. The zero point is $(-1,0)$.

3. Vertical asymptote: at $x=2$ the denominator is zero while the numerator is $2+1=3\ne0$. We check the one-sided limits:

   $$\lim_{x\to2^-}\frac{x+1}{x-2}=-\infty,\qquad
   \lim_{x\to2^+}\frac{x+1}{x-2}=+\infty.$$

   So $x=2$ is a vertical asymptote.

4. Horizontal asymptote: divide numerator and denominator by $x$:

   $$f(x)=\frac{x+1}{x-2}=\frac{1+1/x}{1-2/x}.$$

   As $x\to\pm\infty$, the terms $1/x$ and $2/x$ go to zero, so

   $$\lim_{x\to\pm\infty}f(x)=\frac{1}{1}=1.$$

   Hence $y=1$ is a horizontal asymptote.

5. Derivative: using the quotient rule $\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$ with $u=x+1$ and $v=x-2$:

   $$f'(x)=\frac{(1)(x-2)-(x+1)(1)}{(x-2)^2}
   =\frac{x-2-x-1}{(x-2)^2}
   =\frac{-3}{(x-2)^2}.$$

6. Sign of the derivative: the numerator $-3$ is always negative, and the denominator $(x-2)^2$ is positive for all $x\ne2$. Therefore

   $$f'(x)<0\quad\text{for all }x\ne2.$$

7. Monotonicity: since $f'(x)<0$ on each interval of the domain, $f$ is decreasing on $(-\infty,2)$ and decreasing on $(2,\infty)$. These are two separate intervals because the domain is disconnected by the vertical asymptote at $x=2$.

8. Sketch: the graph passes through $(-1,0)$, approaches $-\infty$ as $x\to2^-$, approaches $+\infty$ as $x\to2^+$, and approaches $y=1$ from below on both sides as $x\to\pm\infty$.

## Why each step is valid

- The domain excludes $x=2$ because division by zero is undefined.
- The zero is found from the numerator because a fraction equals zero exactly when its numerator is zero and its denominator is nonzero.
- The vertical asymptote at $x=2$ follows from the one-sided limits tending to $\mp\infty$ with a nonzero numerator.
- The horizontal asymptote follows from the limit at infinity, since the degrees of numerator and denominator are equal and the ratio of leading coefficients is $1$.
- The quotient rule applies because both numerator and denominator are differentiable and the denominator is nonzero on the domain.
- The derivative is negative everywhere on the domain, so the function decreases on each connected interval of the domain separately.

## Final answer (in words)

The domain is all real numbers except $x=2$. The only zero is at $x=-1$. There is a vertical asymptote at $x=2$ and a horizontal asymptote at $y=1$. The function is decreasing on $(-\infty,2)$ and on $(2,\infty)$, analyzed separately.

## Verification

We check the derivative sign at one test point in each interval:
- At $x=0$: $f'(0)=\frac{-3}{(-2)^2}=-\frac{3}{4}<0$, confirming decrease on $(-\infty,2)$.
- At $x=3$: $f'(3)=\frac{-3}{(1)^2}=-3<0$, confirming decrease on $(2,\infty)$.

We check the asymptote: $f(100)=\frac{101}{98}\approx1.03$, close to $1$, consistent with $y=1$ as $x$ grows large.

## Common mistakes

- Treating $(-\infty,2)\cup(2,\infty)$ as one interval and claiming the function decreases across the asymptote, which is false because the function is not defined at $x=2$.
- Forgetting that the numerator must be nonzero at the vertical asymptote; here $x+1=3\ne0$ at $x=2$, so it is a genuine asymptote and not a removable hole.
- Confusing the horizontal asymptote value by not dividing leading coefficients correctly.

## How I would explain it in class

This is a rational function, so first I note that $x=2$ is forbidden because it makes the denominator zero, giving a vertical asymptote there. The graph crosses the x-axis at $x=-1$ and levels off at height $1$ far to the left and right. The derivative is always negative, so the curve goes down on each side of the asymptote separately, never crossing from one side to the other.
