# Problem 14

## The original problem

It is known that
$$f'(x)=(x-1)(x+2).$$
Determine the monotonicity and the locations of the extrema, and sketch a possible qualitative shape of the function. Then, for
$$g(x)=\frac{x^3}{3}+\frac{x^2}{2}-2x$$
verify that $g'(x)=(x-1)(x+2)$, and compare the specific graph with the earlier qualitative sketch.

> **Why this problem:** it teaches how to read the behavior of a function directly from its derivative.

## What we are looking for

In the first part we do not know the function $f$. We only know its derivative. From the derivative alone we must say where $f$ goes up, where it goes down, and where it has peaks and valleys, and we draw a rough picture. In the second part we are given a specific function $g$, we check by differentiating that it has this derivative, and we compare its graph with the rough picture.

## The idea we need

The derivative is the slope of the graph. If $f'>0$ on an interval, the graph goes up there, so $f$ is increasing. If $f'<0$, the graph goes down, so $f$ is decreasing. At a point where $f'$ changes from plus to minus, the graph goes up and then down, which is a local maximum. Where it changes from minus to plus, we have a local minimum. The derivative tells us the shape, but not the height: two functions that differ by a constant have the same derivative.

## Step-by-step solution

1. Zeros of the derivative. $f'(x)=(x-1)(x+2)=0$ when $x=1$ or $x=-2$. These are the only places where the slope is zero, so they are the only candidates for extrema.

2. Sign chart. The derivative is a parabola opening upward (the coefficient of $x^2$ is $1$), so it is positive outside the zeros and negative between them. We confirm with test points:

| Interval | Test point | $f'$ computed | Sign | Behavior of $f$ |
|---|---|---|---|---|
| $(-\infty,-2)$ | $x=-3$ | $(-4)(-1)=4$ | $+$ | increasing |
| $(-2,1)$ | $x=0$ | $(-1)(2)=-2$ | $-$ | decreasing |
| $(1,\infty)$ | $x=2$ | $(1)(4)=4$ | $+$ | increasing |

3. Extrema. At $x=-2$ the sign changes from plus to minus: local maximum. At $x=1$ it changes from minus to plus: local minimum. We cannot say the heights of these points from $f'$ alone.

4. Qualitative sketch. Start in the lower left, climb to a smooth peak above $x=-2$, descend to a smooth valley above $x=1$, and climb again to the upper right. The peak is to the left of the valley, and the peak is higher than the valley, because the function goes down between them. The slope is most negative halfway between the zeros, at $x=-\tfrac12$, where $f'(-\tfrac12)=(-1.5)(1.5)=-2.25$. This is where the graph switches from bending like a cap to bending like a cup.

5. Verify $g'$. Differentiate each term:
$$g'(x)=\frac{3x^2}{3}+\frac{2x}{2}-2=x^2+x-2.$$
Now multiply out the product:
$$(x-1)(x+2)=x^2+2x-x-2=x^2+x-2.$$
The two are equal, so $g'(x)=(x-1)(x+2)$.

6. The specific graph of $g$. Values:
   - $g(-2)=\tfrac{-8}{3}+\tfrac42+4=-\tfrac83+2+4=\tfrac{10}{3}\approx3.33$ (local maximum).
   - $g(1)=\tfrac13+\tfrac12-2=-\tfrac76\approx-1.17$ (local minimum).
   - $g(0)=0$, so the graph passes through the origin.
   - $g''(x)=2x+1$, which changes sign at $x=-\tfrac12$, so there is an inflection point at $(-\tfrac12,\tfrac{13}{12})\approx(-0.5,1.08)$. Concave on $(-\infty,-\tfrac12)$, convex on $(-\tfrac12,\infty)$.
   - Zeros: $g(x)=x\left(\tfrac{x^2}{3}+\tfrac x2-2\right)$, and the bracket is zero at $x=\tfrac{-3\pm\sqrt{105}}{4}$, that is about $-3.31$ and $1.81$.

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|---|---|
| $g(x)$ | $1.5$ | $3.33$ | $2.17$ | $0$ | $-1.17$ | $0.67$ | $7.5$ |

7. Comparison. The specific graph matches the qualitative sketch: it rises up to the peak $(-2,\tfrac{10}{3})$, falls to the valley $(1,-\tfrac76)$, and rises again. What the sketch could not tell us is the height of the peak and valley, the zeros, and the inflection point. Any function $g(x)+C$ has the same derivative and the same shape, only shifted up or down.

## Why each step is valid

- A positive derivative on an interval means the graph goes up there, and a negative one means it goes down. This is the meaning of the derivative as slope.
- The derivative is continuous, so it can change sign only at its zeros. One test point per interval is enough.
- A sign change of $f'$ from plus to minus gives a local maximum, because the function rises and then falls.
- The verification of $g'$ is valid because the derivative of a sum is the sum of derivatives, and the derivative of $x^n$ is $nx^{n-1}$.
- The function is only determined up to an added constant, because the derivative of a constant is zero.

## Final answer (in words)

The function $f$ is increasing on $(-\infty,-2)$ and on $(1,\infty)$, and decreasing on $(-2,1)$. It has a local maximum at $x=-2$ and a local minimum at $x=1$. The qualitative picture is a smooth S-like curve with a peak on the left and a valley on the right. For $g$ we have $g'(x)=x^2+x-2=(x-1)(x+2)$, and its graph has the peak $(-2,\tfrac{10}{3})$ and the valley $(1,-\tfrac76)$, consistent with the sketch.

## Verification

An independent numeric check of the slope of $g$ using secant lines: the slope from $x=0$ to $x=0.01$ is $\tfrac{g(0.01)-g(0)}{0.01}$ with $g(0.01)\approx-0.01995$, giving about $-1.99$, close to $(0-1)(0+2)=-2$. At $x=2$, the secant slope from $2$ to $2.001$ is about $4.0$, close to $(1)(4)=4$. Test values of the table agree with the direction: $g(-3)=1.5<g(-2)=3.33>g(-1)=2.17$ shows a peak at $-2$, and $g(0)=0>g(1)=-1.17<g(2)=0.67$ shows a valley at $1$. A computer algebra check (sympy) gave $g'=(x-1)(x+2)$ and the values $g(-2)=\tfrac{10}{3}$ and $g(1)=-\tfrac76$.

## Common mistakes

- Reversing the signs: calling $x=-2$ a minimum because the parabola $f'$ has its low point in between.
- Confusing the graph of $f'$ with the graph of $f$. The parabola is the slope, not the function.
- Saying the derivative determines the function exactly. It determines it only up to a constant.
- Computing the product $(x-1)(x+2)$ as $x^2-2$, forgetting the middle terms.

## How I would explain it in class

The derivative $(x-1)(x+2)$ is positive left of $-2$, negative between $-2$ and $1$, and positive right of $1$, so the function goes up, then down, then up, with a peak at $-2$ and a valley at $1$. Differentiating $g$ gives $x^2+x-2$, which equals $(x-1)(x+2)$, so $g$ is one specific function with exactly this shape, with peak height $\tfrac{10}{3}$ and valley height $-\tfrac76$. Adding any constant to $g$ gives other functions with the same derivative, so the derivative fixes the shape but not the height.
