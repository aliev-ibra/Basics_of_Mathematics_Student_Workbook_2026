# Problem 8

## The original problem

For
$$f(x)=x^4-4x^2$$
find the local extrema, intervals of convexity and concavity, and inflection points. Sketch the graph and mark all the identified features on it.

> **Why this problem:** it introduces the second derivative as a tool for describing the curvature of a graph.

## What we are looking for

We want four things. First, the local extrema: the peaks and valleys of the graph. Second, the intervals where the graph bends upward (convex) and where it bends downward (concave). Third, the inflection points, where the bending changes. Fourth, a sketch that shows all of this.

## The idea we need

A critical point is a point where the first derivative is zero. The first derivative tells us whether the graph goes up or down. If it changes from plus to minus, we have a local maximum. If it changes from minus to plus, we have a local minimum.

The second derivative is the derivative of the first derivative. It tells us how the slope itself changes. If $f''>0$ on an interval, the slope grows, the graph bends upward like a cup, and we call it convex. If $f''<0$, the slope shrinks, the graph bends downward like a cap, and we call it concave. An inflection point is a point where the graph switches between convex and concave, so $f''$ changes sign there.

## Step-by-step solution

1. The function is a polynomial, so it is defined for every real number. It is also even, because $f(-x)=f(x)$ (only even powers appear). So the graph is a mirror image about the $y$-axis.

2. Zeros. Factor: $f(x)=x^2(x^2-4)=x^2(x-2)(x+2)$. The zeros are $x=-2$, $x=0$, $x=2$.

3. First derivative:
$$f'(x)=4x^3-8x=4x(x^2-2)=4x(x-\sqrt2)(x+\sqrt2).$$
It is zero at $x=-\sqrt2$, $x=0$, $x=\sqrt2$. These are the critical points.

4. Sign chart of $f'$. The three critical points cut the line into four intervals. In each we test one point.

| Interval | Test point | Value of $f'$ | Sign | Behavior of $f$ |
|---|---|---|---|---|
| $(-\infty,-\sqrt2)$ | $x=-2$ | $-16$ | $-$ | decreasing |
| $(-\sqrt2,0)$ | $x=-1$ | $4$ | $+$ | increasing |
| $(0,\sqrt2)$ | $x=1$ | $-4$ | $-$ | decreasing |
| $(\sqrt2,\infty)$ | $x=2$ | $16$ | $+$ | increasing |

5. Local extrema. At $x=-\sqrt2$ the sign goes from minus to plus: local minimum. At $x=0$ it goes from plus to minus: local maximum. At $x=\sqrt2$ it goes from minus to plus: local minimum. The values:
$$f(0)=0,\qquad f(\pm\sqrt2)=4-8=-4.$$

6. Second derivative:
$$f''(x)=12x^2-8=4(3x^2-2).$$
It is zero when $x^2=\tfrac23$, that is $x=\pm\sqrt{2/3}=\pm\tfrac{\sqrt6}{3}\approx\pm0.816$.

7. Sign chart of $f''$.

| Interval | Test point | Value of $f''$ | Sign | Shape |
|---|---|---|---|---|
| $(-\infty,-\tfrac{\sqrt6}{3})$ | $x=-1$ | $4$ | $+$ | convex (cup) |
| $(-\tfrac{\sqrt6}{3},\tfrac{\sqrt6}{3})$ | $x=0$ | $-8$ | $-$ | concave (cap) |
| $(\tfrac{\sqrt6}{3},\infty)$ | $x=1$ | $4$ | $+$ | convex (cup) |

8. Inflection points. The second derivative changes sign at both $x=\pm\tfrac{\sqrt6}{3}$, so both are inflection points. The height there: since $x^2=\tfrac23$ and $x^4=\tfrac49$,
$$f=\tfrac49-4\cdot\tfrac23=\tfrac49-\tfrac{24}{9}=-\tfrac{20}{9}\approx-2.22.$$

9. Ends of the graph. For large $|x|$ the term $x^4$ dominates, so $f(x)\to+\infty$ as $x\to\pm\infty$.

10. What the sketch shows. The graph is a "W". It comes down from the upper left, passes through $(-2,0)$, reaches a valley at $(-\sqrt2,-4)$, climbs to a hilltop at the origin $(0,0)$, falls to a second valley at $(\sqrt2,-4)$, then rises through $(2,0)$ to the upper right. The graph is a cup far out, a cap near the middle, and a cup again; the bending changes at $(\pm0.816,-2.22)$.

| $x$ | $-2$ | $-\sqrt2\approx-1.41$ | $-0.82$ | $0$ | $0.82$ | $1.41$ | $2$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $0$ | $-4$ | $-2.22$ | $0$ | $-2.22$ | $-4$ | $0$ |
| Feature | zero | local min | inflection | local max | inflection | local min | zero |

## Why each step is valid

- A polynomial is differentiable everywhere, so every extremum happens where $f'=0$.
- Testing one point per interval is enough because $f'$ is continuous and can change sign only at its zeros.
- A sign change of $f'$ from plus to minus means the function rises and then falls, which is the definition of a local maximum. The other direction gives a minimum.
- The second derivative measures the change of the slope, so its sign gives the bending. Inflection requires a real sign change, not only $f''=0$.
- The symmetry check is valid because $f(-x)=f(x)$, which is why the values at $-x$ and $x$ in the table agree.

## Final answer (in words)

The function has local minima at $x=-\sqrt2$ and $x=\sqrt2$, both with value $-4$, and a local maximum at $x=0$ with value $0$. It is convex on $(-\infty,-\tfrac{\sqrt6}{3})$ and on $(\tfrac{\sqrt6}{3},\infty)$, and concave on $(-\tfrac{\sqrt6}{3},\tfrac{\sqrt6}{3})$. The inflection points are $\left(\pm\tfrac{\sqrt6}{3},-\tfrac{20}{9}\right)$. The graph is a "W" shape symmetric about the $y$-axis.

## Verification

The second-derivative test is a different route to the same types. $f''(0)=-8<0$, so a cap and a maximum. $f''(\pm\sqrt2)=4(6-2)=16>0$, so a cup and a minimum. This agrees with the sign chart of $f'$.

A numeric table of function values around the critical points:

| $x$ | $-1.6$ | $-1.41$ | $-1.2$ | $-0.5$ | $0$ | $0.5$ | $1.2$ | $1.41$ | $1.6$ |
|---|---|---|---|---|---|---|---|---|---|
| $f(x)$ | $-3.69$ | $-4.00$ | $-3.69$ | $-0.94$ | $0$ | $-0.94$ | $-3.69$ | $-4.00$ | $-3.69$ |

The value $-4$ is lower than its neighbors on both sides, and $0$ is higher than its neighbors. Also, a computer algebra check (sympy) gave critical points $0,\pm\sqrt2$ and inflection points $\pm\sqrt6/3$, with $f=-20/9$ there.

## Common mistakes

- Thinking that $f''=0$ alone proves an inflection point. The sign of $f''$ must change.
- Mixing up the words: convex means cup (second derivative positive), concave means cap (second derivative negative).
- Forgetting the symmetry and computing only one side, or putting the inflection points at $\pm\sqrt2$ by confusing them with the critical points.
- Forgetting to compute the height of the inflection points.

## How I would explain it in class

First I set the first derivative $4x(x^2-2)$ to zero, which gives a hilltop at $x=0$ and two valleys at $x=\pm\sqrt2$ with height $-4$. Then I use the second derivative $12x^2-8$: it is positive far from the middle, so the graph is a cup there, and negative near the middle, so the graph is a cap there. The bending changes at $x=\pm\tfrac{\sqrt6}{3}$, which are the inflection points, and together these facts draw a W-shaped graph.
