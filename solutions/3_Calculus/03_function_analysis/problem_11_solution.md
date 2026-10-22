# Problem 11

## The original problem

For
$$f_a(x)=x^3-3ax$$
depending on $a$, determine the number of critical points and their character. Separate the parameter cases and justify why the structure of the graph changes.

> **Why this problem:** it teaches how to analyze an entire family of functions instead of a single example.

## What we are looking for

The letter $a$ is a parameter: a fixed number that we have not chosen yet. Each value of $a$ gives a different function. We want to know, for every possible $a$, how many critical points there are (points where the derivative is zero) and whether each is a peak, a valley, or neither. Then we explain why the picture changes when $a$ crosses a certain value.

## The idea we need

Critical points are the solutions of $f'(x)=0$. Whether a solution exists depends on the sign of $a$, so we split into cases. At a critical point, if the derivative changes sign from plus to minus, it is a local maximum; from minus to plus, a local minimum; if the derivative does not change sign, it is neither. We use the sign of the derivative, because it works also in the case where the second derivative test fails.

## Step-by-step solution

1. The function is a polynomial, so it is differentiable everywhere. Its derivative is
$$f_a'(x)=3x^2-3a=3(x^2-a).$$

2. Critical points: solve $x^2=a$. The number of solutions depends on $a$.

**Case 1: $a<0$.** Then $x^2=a$ has no real solution, because a square is never negative. So there are no critical points. Moreover $x^2-a=x^2+|a|>0$ for every $x$, so $f_a'>0$ everywhere. The function is increasing on the whole line and has no extrema.
Example, $a=-1$: $f(x)=x^3+3x$, $f'(x)=3x^2+3\ge3$.

**Case 2: $a=0$.** Then $f_0(x)=x^3$ and $f_0'(x)=3x^2$, zero only at $x=0$. There is exactly one critical point. But $3x^2\ge0$ on both sides, so the derivative does not change sign. The function is increasing on the whole line, and $x=0$ is neither a maximum nor a minimum. The graph is flat for an instant at the origin (horizontal tangent), then keeps rising.

**Case 3: $a>0$.** Then $x^2=a$ has two solutions, $x=-\sqrt a$ and $x=\sqrt a$. We have $f_a'(x)=3(x-\sqrt a)(x+\sqrt a)$. Sign chart:

| Interval | Test point | $f_a'$ | Behavior |
|---|---|---|---|
| $(-\infty,-\sqrt a)$ | $x=-\sqrt a-1$ | $+$ | increasing |
| $(-\sqrt a,\sqrt a)$ | $x=0$ | $-3a<0$ | decreasing |
| $(\sqrt a,\infty)$ | $x=\sqrt a+1$ | $+$ | increasing |

(For the outer intervals, $x^2>a$, so $3(x^2-a)>0$.) So $x=-\sqrt a$ is a local maximum and $x=\sqrt a$ is a local minimum. The values:
$$f_a(-\sqrt a)=-a\sqrt a+3a\sqrt a=2a^{3/2},\qquad f_a(\sqrt a)=a\sqrt a-3a\sqrt a=-2a^{3/2}.$$

3. Extra information valid for all $a$. The second derivative is $f_a''(x)=6x$, which changes sign at $x=0$ for every $a$. So the origin is always an inflection point. Also $f_a(0)=0$.

4. Summary of the three cases:

| Case | Critical points | Character | Shape |
|---|---|---|---|
| $a<0$ | none | no extrema | strictly increasing S-curve |
| $a=0$ | one: $x=0$ | neither max nor min | increasing, flat tangent at origin |
| $a>0$ | two: $x=\pm\sqrt a$ | max at $-\sqrt a$, min at $\sqrt a$ | rises, falls, rises again |

5. Why the structure changes. The derivative is a parabola $3(x^2-a)$ whose vertex is at height $-3a$. When $a<0$ the vertex is above the $x$-axis, so the parabola never touches the axis. When $a=0$ the vertex touches the axis at one point. When $a>0$ the vertex is below the axis, so the parabola crosses it twice. The graph of $f_a$ changes at $a=0$ because the number of zeros of $f_a'$ changes from $0$ to $1$ to $2$. At $a=0$ the peak and the valley merge into one flat point and disappear.

6. Sketch description for $a>0$. The graph passes through the origin, rises to the peak $(-\sqrt a,2a^{3/2})$, falls through the origin to the valley $(\sqrt a,-2a^{3/2})$, then rises. It crosses the $x$-axis at $0$ and $\pm\sqrt{3a}$. For example, $a=1$: peak $(-1,2)$, valley $(1,-2)$, zeros $0,\pm\sqrt3\approx\pm1.73$.

## Why each step is valid

- A polynomial is differentiable everywhere, so extrema occur only where $f'=0$.
- A real number squared is never negative, so $x^2=a$ has no real solution when $a<0$.
- When $a=0$ we cannot rely on the usual test with the second derivative, since $f_0''(0)=0$; instead we look at the sign of $f_0'=3x^2$, which stays nonnegative, so there is no extremum.
- In case 3 the sign of the product $3(x-\sqrt a)(x+\sqrt a)$ is plus outside the roots because the leading coefficient $3$ is positive.
- The inflection claim is valid because $6x$ changes sign at $0$ for any value of $a$.

## Final answer (in words)

If $a<0$, there are no critical points and the function is increasing everywhere. If $a=0$, there is exactly one critical point, $x=0$, and it is neither a maximum nor a minimum. If $a>0$, there are two critical points: a local maximum at $x=-\sqrt a$ with value $2a^{3/2}$ and a local minimum at $x=\sqrt a$ with value $-2a^{3/2}$. The structure changes at $a=0$ because the derivative $3(x^2-a)$ has no, one, or two real zeros.

## Verification

Test values of $a$:

| $a$ | $f_a'(x)$ | zeros of $f_a'$ | Result |
|---|---|---|---|
| $-1$ | $3x^2+3$ | none | increasing, no extrema |
| $0$ | $3x^2$ | $0$ | no extremum |
| $4$ | $3x^2-12$ | $\pm2$ | max $f(-2)=-8+24=16$, min $f(2)=8-24=-16$ |

The last row agrees with the formula $2a^{3/2}=2\cdot8=16$. A direct numeric look for $a=4$: $f(-3)=-27+36=9$, $f(-2)=16$, $f(-1)=-1+12=11$, so $-2$ is higher than its neighbors. And $f(1)=-11$, $f(2)=-16$, $f(3)=-9$, so $2$ is lower than its neighbors. A computer algebra check (sympy) gave critical points $\pm\sqrt a$ and the values $\mp2a^{3/2}$.

## Common mistakes

- Solving $x^2=a$ as $x=\sqrt a$ only and forgetting the negative root.
- Taking square roots of a negative $a$ and writing complex or meaningless critical points.
- Claiming that a critical point is always an extremum. For $a=0$ it is not.
- Ignoring the case $a=0$ because it looks like a boundary.

## How I would explain it in class

The derivative is $3(x^2-a)$, so the critical points are the solutions of $x^2=a$, and the number of solutions depends on the sign of $a$. If $a$ is negative there are none, if $a$ is zero there is one flat point that is neither a peak nor a valley, and if $a$ is positive there are two, a peak at $-\sqrt a$ and a valley at $\sqrt a$. The graph changes at $a=0$ because the peak and the valley slide together, merge into a flat point, and then disappear.
