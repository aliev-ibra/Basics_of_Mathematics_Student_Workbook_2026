# Problem 12

## The original problem

Analyze
$$f(x)=|x^2-4|.$$
First sketch $x^2-4$, then explain the effect of the absolute value. Indicate the points where the derivative does not exist and justify the reason geometrically.

> **Why this problem:** it shows the limits of mechanical application of calculus and the importance of the geometry of the graph.

## What we are looking for

We want to understand the graph of $|x^2-4|$ starting from the graph of $x^2-4$. We want to know where the function rises and falls, where its extrema are, where it bends, and at which points the derivative does not exist. For those points we need a reason that can be seen in the picture.

## The idea we need

The absolute value $|u|$ equals $u$ when $u\ge0$ and $-u$ when $u<0$. On the graph this means: the part of the graph that lies above the $x$-axis stays as it is, and the part below the $x$-axis is flipped upward, like a mirror in the $x$-axis. Wherever the original graph crosses the axis with a nonzero slope, the flip creates a sharp corner. At a sharp corner there is no single tangent line, because the slope from the left and the slope from the right are different. Then the derivative does not exist.

## Step-by-step solution

1. The graph of $g(x)=x^2-4$. It is a parabola opening upward, with vertex $(0,-4)$, crossing the $x$-axis at $x=-2$ and $x=2$. It lies below the axis exactly on $(-2,2)$, because there $x^2<4$.

2. Apply the absolute value. Writing $f$ as separate pieces:
$$f(x)=\begin{cases}x^2-4,& x\le-2\text{ or }x\ge2,\\ 4-x^2,& -2<x<2.\end{cases}$$
So the pieces outside $[-2,2]$ stay the same, and the middle piece is flipped upward. The vertex $(0,-4)$ moves to $(0,4)$, and the middle becomes an upside-down parabola (a cap) of height $4$.

3. Derivative on each piece.
   - For $x<-2$ or $x>2$: $f'(x)=2x$.
   - For $-2<x<2$: $f'(x)=-2x$.

4. The points $x=\pm2$. We compare one-sided slopes.

| Point | Slope from the left | Slope from the right |
|---|---|---|
| $x=-2$ | $2(-2)=-4$ | $-2(-2)=4$ |
| $x=2$ | $-2(2)=-4$ | $2(2)=4$ |

   At each point the two slopes differ ($-4$ and $4$), so the derivative does not exist at $x=-2$ and $x=2$. The function itself is continuous there, with value $0$. Geometrically, the original parabola crosses the axis going steeply, and the flip turns that crossing into a V-shaped corner.

5. The point $x=0$. Here $f(x)=4-x^2$ near $0$, so $f'(0)=0$ and the derivative exists. It is a smooth hilltop.

6. Sign chart of $f'$.

| Interval | Test point | $f'$ | Behavior |
|---|---|---|---|
| $(-\infty,-2)$ | $x=-3$ | $-6$ | decreasing |
| $(-2,0)$ | $x=-1$ | $2$ | increasing |
| $(0,2)$ | $x=1$ | $-2$ | decreasing |
| $(2,\infty)$ | $x=3$ | $6$ | increasing |

7. Extrema.
   - $x=\pm2$: the function goes from decreasing to increasing, so local minima, value $0$. Since $f\ge0$ everywhere, these are also absolute minima. They occur at the corner points, where $f'$ does not exist, so they are found only by looking at the graph.
   - $x=0$: from increasing to decreasing, a local maximum with value $4$. It is only local, because $f\to\infty$ at the ends.

8. Bending. $f''=2$ on $(-\infty,-2)$ and $(2,\infty)$, so these are convex (cup). $f''=-2$ on $(-2,2)$, so that part is concave (cap). The bending changes at $\pm2$, but we do not call these inflection points, because there is no tangent line at a corner.

9. Ends: $f(x)\to+\infty$ as $x\to\pm\infty$. There is no asymptote.

10. What the sketch shows. A "W" with sharp bottom points: from the upper left the graph comes down along the parabola to the corner $(-2,0)$ on the axis, goes up along a cap to the smooth peak $(0,4)$, comes down to the corner $(2,0)$, and rises again along the original parabola. The graph is symmetric about the $y$-axis and never goes below the axis.

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $x^2-4$ | $5$ | $0$ | $-3$ | $-4$ | $-3$ | $0$ | $5$ |
| $f(x)=\lvert x^2-4\rvert$ | $5$ | $0$ | $3$ | $4$ | $3$ | $0$ | $5$ |

## Why each step is valid

- The piecewise form follows from the definition of the absolute value, using the sign of $x^2-4$.
- Each piece is a polynomial, so the derivative on its open interval is found by the ordinary rules.
- The derivative at a point exists only if the left and right slopes are equal. At $\pm2$ they are $-4$ and $4$, so it fails there.
- Absolute minima are found from the graph and the fact $|u|\ge0$, since mechanical use of $f'=0$ would miss the corner points.

## Final answer (in words)

The function is $x^2-4$ for $|x|\ge2$ and $4-x^2$ for $|x|<2$. It is decreasing on $(-\infty,-2)$ and $(0,2)$, and increasing on $(-2,0)$ and $(2,\infty)$. It has a local maximum $4$ at $x=0$ and absolute minima $0$ at $x=-2$ and $x=2$. The derivative does not exist at $x=\pm2$, because the graph has a corner there with slopes $-4$ on one side and $4$ on the other. It is convex outside $[-2,2]$ and concave inside.

## Verification

Test values: $f(-2.1)=|4.41-4|=0.41$, $f(-2)=0$, $f(-1.9)=|3.61-4|=0.39$. Both neighbors are higher than $0$, so $x=-2$ is a minimum. The slopes of the secant lines near $x=2$ show the corner: from $x=2$ to $x=2.01$, the rise is $f(2.01)-f(2)=0.0401$, slope $\approx4.01$. From $x=1.99$ to $x=2$, the rise is $0-f(1.99)=-0.0399$, slope $\approx-3.99$. The slopes are near $-4$ and $+4$, which confirms the corner. A computer algebra check (sympy) gave the same pieces and the same one-sided slopes $\pm4$.

## Common mistakes

- Writing $f'(x)=2x$ everywhere, forgetting that the middle piece has the opposite sign.
- Saying $f'(\pm2)=0$ because the function has a minimum there. A minimum at a corner does not need a zero derivative.
- Calling $x=\pm2$ inflection points. There is no tangent at a corner.
- Saying the minimum at $x=0$ instead of the maximum, because of the original parabola.

## How I would explain it in class

The absolute value keeps the parts of the graph above the axis and flips the part below the axis upward, so the parabola $x^2-4$ turns into a W with a smooth peak $(0,4)$ in the middle. At $x=-2$ and $x=2$ the graph has sharp corners where the slope jumps from $-4$ to $4$, so the derivative does not exist there even though these are the lowest points. This is why we must look at the picture and not only at the formula for the derivative.
