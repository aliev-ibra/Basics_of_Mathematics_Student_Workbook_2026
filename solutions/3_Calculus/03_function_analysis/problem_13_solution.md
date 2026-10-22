# Problem 13

## The original problem

Perform a complete analysis of
$$f(x)=\frac{\ln x}{x},\qquad x>0.$$
Find the maximum and the behavior at the ends of the domain. Explain which information is necessary for a correct sketch.

> **Why this problem:** it combines the domain, limits, and derivative in a less obvious example.

## What we are looking for

We want a complete description of the graph on $x>0$: the zero, the sign, the limits at the two ends of the domain (when $x$ gets close to $0$ and when $x$ gets very large), where the function rises and falls, the maximum, and the bending. Then we say which of these facts a correct sketch needs.

## The idea we need

The natural logarithm $\ln x$ is defined only for $x>0$, and it is zero at $x=1$, negative for $0<x<1$ and positive for $x>1$. As $x\to0^+$, $\ln x\to-\infty$. As $x\to\infty$, $\ln x\to\infty$, but very slowly, much slower than $x$. So the fraction $\tfrac{\ln x}{x}$ is a fight between a slowly growing top and a fast growing bottom. The derivative tells us the shape, and the limits tell us what the graph does at the edges.

## Step-by-step solution

1. Domain: $x>0$, as given. The function is continuous and differentiable on $(0,\infty)$.

2. Zero and sign. $f(x)=0$ exactly when $\ln x=0$, that is $x=1$. The bottom $x$ is positive, so the sign of $f$ is the sign of $\ln x$: negative on $(0,1)$, positive on $(1,\infty)$.

3. Limit at the left end, $x\to0^+$. The top tends to $-\infty$ and the bottom tends to $0^+$. Dividing a very large negative number by a very small positive number gives a very large negative number. So
$$\lim_{x\to0^+}\frac{\ln x}{x}=-\infty,$$
and $x=0$ is a vertical asymptote (the graph plunges down along the $y$-axis).

4. Limit at the right end, $x\to\infty$. Write $x=e^t$, so $t=\ln x\to\infty$. Then $\tfrac{\ln x}{x}=\tfrac{t}{e^t}$, and the exponential grows faster than any multiple of $t$, so this tends to $0$. (L'Hopital's rule gives the same: the ratio of derivatives is $\tfrac{1/x}{1}=\tfrac1x\to0$.) So
$$\lim_{x\to\infty}\frac{\ln x}{x}=0,$$
and $y=0$ is a horizontal asymptote on the right. Since $f>0$ for $x>1$, the graph approaches the axis from above.

5. First derivative, by the quotient rule:
$$f'(x)=\frac{\frac1x\cdot x-\ln x\cdot1}{x^2}=\frac{1-\ln x}{x^2}.$$
The bottom is positive, so the sign comes from $1-\ln x$. It is zero when $\ln x=1$, that is $x=e\approx2.718$.

| Interval | Test point | $f'$ | Behavior |
|---|---|---|---|
| $(0,e)$ | $x=1$ | $1$ | increasing |
| $(e,\infty)$ | $x=e^2\approx7.39$ | $\tfrac{1-2}{e^4}=-e^{-4}$ | decreasing |

6. Maximum. At $x=e$ the sign goes from plus to minus, so it is a local maximum, and because the function increases on all of $(0,e)$ and decreases on all of $(e,\infty)$ it is the absolute maximum:
$$f(e)=\frac{\ln e}{e}=\frac1e\approx0.368.$$

7. Second derivative. Differentiating $\tfrac{1-\ln x}{x^2}$ gives
$$f''(x)=\frac{2\ln x-3}{x^3}.$$
It is zero when $\ln x=\tfrac32$, that is $x=e^{3/2}\approx4.48$.

| Interval | Test point | $f''$ | Shape |
|---|---|---|---|
| $(0,e^{3/2})$ | $x=2$ | $\tfrac{2\ln2-3}{8}\approx-0.20$ | concave (cap) |
| $(e^{3/2},\infty)$ | $x=5$ | $\tfrac{2\ln5-3}{125}\approx0.0018$ | convex (cup) |

   So there is an inflection point at $x=e^{3/2}$ with value $\tfrac{3/2}{e^{3/2}}=\tfrac32e^{-3/2}\approx0.335$.

8. What the sketch shows. On the left the graph starts at $-\infty$ next to the $y$-axis, rises steeply, crosses the $x$-axis at $(1,0)$, and keeps rising until the peak $(e,\tfrac1e)\approx(2.72,0.368)$. After the peak it falls slowly. It bends from cap to cup at about $(4.48,0.335)$ and then flattens, approaching the $x$-axis from above without touching it.

| $x$ | $0.1$ | $0.5$ | $1$ | $2$ | $e\approx2.72$ | $4$ | $10$ | $100$ |
|---|---|---|---|---|---|---|---|---|
| $f(x)$ | $-23.03$ | $-1.39$ | $0$ | $0.347$ | $0.368$ | $0.347$ | $0.230$ | $0.046$ |

9. Which information a correct sketch needs. We need: the domain (nothing exists for $x\le0$), the vertical asymptote at $x=0$ with the direction $-\infty$, the zero at $x=1$, the maximum point $(e,1/e)$, the horizontal asymptote $y=0$ on the right with the graph staying above it, and the change of bending. Without the limit at $\infty$ one might think the graph keeps falling below the axis; without the limit at $0^+$ one would miss the plunge.

## Why each step is valid

- The sign of $\ln x$ is known from its graph: it is increasing and equals zero at $1$.
- The limit at $0^+$ is of the form "negative large over small positive", which has no cancellation, so the result is $-\infty$.
- The limit at $\infty$ is an indeterminate form (large over large), so we need an argument: either the substitution $x=e^t$ or L'Hopital's rule. Both give $0$.
- The quotient rule applies because $\ln x$ and $x$ are differentiable on $x>0$ and the bottom is nonzero.
- The maximum is absolute because the function is strictly increasing before $e$ and strictly decreasing after $e$.

## Final answer (in words)

The function is defined for $x>0$. It is zero only at $x=1$, negative before it and positive after it. As $x\to0^+$ it tends to $-\infty$ (vertical asymptote $x=0$), and as $x\to\infty$ it tends to $0$ from above (horizontal asymptote $y=0$). It increases on $(0,e)$ and decreases on $(e,\infty)$, so the absolute maximum is $\tfrac1e$ at $x=e$. It is concave on $(0,e^{3/2})$ and convex on $(e^{3/2},\infty)$, with an inflection point at $x=e^{3/2}$.

## Verification

Numeric check around the maximum: $f(2)\approx0.3466$, $f(e)\approx0.3679$, $f(3)\approx0.3662$, $f(4)\approx0.3466$. The value at $e$ is the largest of these, as predicted. The limit table shows $f(100)=0.046$, and $f(10^6)=\tfrac{13.8}{10^6}\approx0.0000138$, which tends to $0$. At the left, $f(0.01)\approx-460.5$, which keeps growing negative. A computer algebra check (sympy) confirmed $f'=\tfrac{1-\ln x}{x^2}$, the single critical point $x=e$, the limits $-\infty$ and $0$, and the second-derivative zero $e^{3/2}$.

## Common mistakes

- Saying the limit at infinity is infinite because $\ln x\to\infty$. The bottom grows faster.
- Saying the limit at $0^+$ is $0$ or does not exist, instead of $-\infty$.
- Sketching the graph for negative $x$. The domain is only $x>0$.
- Forgetting that the horizontal asymptote is approached from above, since $f>0$ for $x>1$.
- Writing $\ln e=e$ instead of $\ln e=1$ when computing the maximum value.

## How I would explain it in class

The logarithm grows very slowly, so for large $x$ the fraction $\tfrac{\ln x}{x}$ is pulled down toward zero, while near $x=0$ it plunges to minus infinity. The derivative $\tfrac{1-\ln x}{x^2}$ is positive until $x=e$ and negative after it, so the highest point of the graph is $(e,\tfrac1e)$. For a correct sketch I must show the vertical asymptote at $x=0$, the zero at $x=1$, the peak at $x=e$, and the flattening toward the axis on the right.
