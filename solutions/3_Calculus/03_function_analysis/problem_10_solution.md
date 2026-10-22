# Problem 10

## The original problem

Perform a complete analysis of
$$f(x)=\frac{x}{x^2+1}.$$
Include the domain, symmetry, zeros, limits, monotonicity, extrema, and convexity. Finally, produce a sketch based only on this information.

> **Why this problem:** it combines all the basic elements of function analysis into one organized process.

## What we are looking for

We want a full description of the graph in a fixed order: where the function exists, whether it has a mirror-type symmetry, where it crosses the axes, what it does at the far ends, where it rises and falls, where its peaks and valleys are, and where it bends up or down. Then we draw the graph using only these facts.

## The idea we need

We use the standard checklist. The domain says where the formula makes sense. A function is odd if $f(-x)=-f(x)$; its graph is then unchanged by turning it half a turn about the origin. The limits at $\pm\infty$ give horizontal asymptotes. The first derivative gives rising and falling, and the second derivative gives bending: positive means convex (cup), negative means concave (cap). An inflection point is a point where the bending switches.

## Step-by-step solution

1. Domain. The bottom $x^2+1$ is at least $1$, so it is never zero. The domain is all real numbers. There are no vertical asymptotes.

2. Symmetry. Compute $f(-x)=\dfrac{-x}{x^2+1}=-f(x)$. So $f$ is odd. We only need to understand $x\ge0$ and then rotate.

3. Zeros. A fraction is zero when its top is zero and its bottom is not. The top is zero only at $x=0$. So the only zero is $x=0$, and $f(0)=0$ is also the $y$-intercept.

4. Sign. The bottom is positive, so $f$ has the sign of $x$: negative for $x<0$, positive for $x>0$.

5. Limits. For large $|x|$, the bottom $x^2+1$ is much bigger than the top. Dividing top and bottom by $x^2$ gives $\dfrac{1/x}{1+1/x^2}\to\dfrac{0}{1}=0$. So $\lim_{x\to\infty}f=\lim_{x\to-\infty}f=0$, and $y=0$ is a horizontal asymptote on both sides.

6. First derivative, by the quotient rule (top derivative times bottom, minus top times bottom derivative, all over bottom squared):
$$f'(x)=\frac{1\cdot(x^2+1)-x\cdot2x}{(x^2+1)^2}=\frac{1-x^2}{(x^2+1)^2}=\frac{(1-x)(1+x)}{(x^2+1)^2}.$$
The bottom is always positive, so the sign of $f'$ is the sign of $1-x^2$. It is zero at $x=\pm1$.

| Interval | Test point | $f'$ | Behavior |
|---|---|---|---|
| $(-\infty,-1)$ | $x=-2$ | $-\tfrac{3}{25}$ | decreasing |
| $(-1,1)$ | $x=0$ | $1$ | increasing |
| $(1,\infty)$ | $x=2$ | $-\tfrac{3}{25}$ | decreasing |

7. Extrema. At $x=-1$ the sign goes from minus to plus: local minimum, value $f(-1)=-\tfrac12$. At $x=1$ it goes from plus to minus: local maximum, value $f(1)=\tfrac12$.

8. Second derivative. Differentiating $f'$ gives
$$f''(x)=\frac{2x(x^2-3)}{(x^2+1)^3}.$$
The bottom is positive, so the sign comes from $2x(x-\sqrt3)(x+\sqrt3)$, which is zero at $x=-\sqrt3,\ 0,\ \sqrt3$.

| Interval | Test point | $f''$ | Shape |
|---|---|---|---|
| $(-\infty,-\sqrt3)$ | $x=-2$ | $-\tfrac{4}{125}$ | concave (cap) |
| $(-\sqrt3,0)$ | $x=-1$ | $\tfrac12$ | convex (cup) |
| $(0,\sqrt3)$ | $x=1$ | $-\tfrac12$ | concave (cap) |
| $(\sqrt3,\infty)$ | $x=2$ | $\tfrac{4}{125}$ | convex (cup) |

9. Inflection points. The sign of $f''$ changes at all three zeros, so the inflection points are $(-\sqrt3,-\tfrac{\sqrt3}{4})$, $(0,0)$, and $(\sqrt3,\tfrac{\sqrt3}{4})$. Here $\tfrac{\sqrt3}{4}\approx0.433$.

10. What the sketch shows. Coming from the far left, the graph hugs the $x$-axis from below, dips to the valley $(-1,-0.5)$, then climbs through the origin (steepest there, slope $1$) up to the hilltop $(1,0.5)$, then falls back toward the $x$-axis and hugs it from above on the right. The graph lies between the heights $-0.5$ and $0.5$ everywhere, and it is symmetric under a half turn about the origin.

| $x$ | $-3$ | $-\sqrt3$ | $-1$ | $0$ | $1$ | $\sqrt3$ | $3$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $-0.30$ | $-0.43$ | $-0.50$ | $0$ | $0.50$ | $0.43$ | $0.30$ |

## Why each step is valid

- The denominator is never zero, so the function is defined and differentiable everywhere.
- Oddness follows directly from replacing $x$ by $-x$, so the graph for $x<0$ is a rotated copy of the graph for $x>0$.
- Dividing top and bottom by $x^2$ does not change the fraction, and it makes the limit visible.
- Sign charts with one test point per interval are valid because $f'$ and $f''$ are continuous and can change sign only where they are zero.
- Since the denominators of $f'$ and $f''$ are positive, only the numerators decide the signs.

## Final answer (in words)

The domain is all real numbers. The function is odd, with the only zero at the origin. It tends to $0$ at both ends, so $y=0$ is a horizontal asymptote. It decreases on $(-\infty,-1)$, increases on $(-1,1)$ and decreases on $(1,\infty)$, with local minimum $-\tfrac12$ at $x=-1$ and local maximum $\tfrac12$ at $x=1$. It is concave on $(-\infty,-\sqrt3)$ and $(0,\sqrt3)$, and convex on $(-\sqrt3,0)$ and $(\sqrt3,\infty)$, with inflection points at $x=-\sqrt3$, $0$, $\sqrt3$.

## Verification

An independent check that $\tfrac12$ is the highest value, with no calculus: $f(x)\le\tfrac12$ means $2x\le x^2+1$, which is the same as $(x-1)^2\ge0$, always true, with equality only at $x=1$. By oddness the lowest value is $-\tfrac12$ at $x=-1$.

A numeric check: $f(0.5)=0.4$, $f(1)=0.5$, $f(2)=0.4$, and $f(10)\approx0.099$. The values rise to $x=1$ and then fall toward $0$, as the table says. A computer algebra check (sympy) gave critical points $\pm1$ and second-derivative zeros $0,\pm\sqrt3$, the same as above.

## Common mistakes

- Looking for vertical asymptotes. The bottom $x^2+1$ is never zero.
- Thinking the horizontal asymptote $y=0$ means the graph stays near zero everywhere. It only says this about the far ends.
- Forgetting that $x=0$ is also an inflection point.
- Sign slips in the quotient rule, giving $x^2-1$ instead of $1-x^2$, which would reverse the peak and the valley.

## How I would explain it in class

The bottom is never zero, the function is odd, and it tends to zero at both ends, so the graph is a smooth wave around the $x$-axis. The first derivative $\tfrac{1-x^2}{(x^2+1)^2}$ shows a valley at $x=-1$ with height $-\tfrac12$ and a hilltop at $x=1$ with height $\tfrac12$. The second derivative changes sign at $-\sqrt3$, $0$, and $\sqrt3$, so those are the three inflection points that complete the sketch.
