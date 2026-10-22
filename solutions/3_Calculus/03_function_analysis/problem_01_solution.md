# Problem 1

## The original problem

Analyze the monotonicity and extrema of

$$f(x)=x^3-3x^2+2.$$

Sketch the graph based on the results and mark the critical points.

## What we are looking for

We want to find where the function is increasing and where it is decreasing, locate its local maximum and minimum points, and mark them on a sketch of the graph.

## The idea we need

The first derivative tells us the direction of change of a function. If $f'(x)>0$ on an interval, the function is increasing there; if $f'(x)<0$, it is decreasing. A point where $f'(x)=0$ is a critical point, and it may be a local extremum. We use the sign table of the derivative: find the zeros of $f'$, split the domain at those zeros, check the sign on each interval, and apply the first-derivative test. The conditions are that $f$ is differentiable on the intervals considered.

## Step-by-step solution

1. The function is a polynomial, so its domain is all real numbers $\mathbb{R}$ and it is differentiable everywhere.

2. Compute the first derivative:

   $$f'(x)=3x^2-6x=3x(x-2).$$

3. Find the zeros of the derivative. We solve $3x(x-2)=0$, which gives

   $$x=0 \quad \text{or} \quad x=2.$$

   These are the two critical points.

4. The critical points split $\mathbb{R}$ into three intervals: $(-\infty,0)$, $(0,2)$, and $(2,\infty)$. We check the sign of $f'(x)=3x(x-2)$ on each:

   - On $(-\infty,0)$: both factors $x$ and $(x-2)$ are negative, so their product is positive. Hence $f'(x)>0$.
   - On $(0,2)$: $x$ is positive and $(x-2)$ is negative, so their product is negative. Hence $f'(x)<0$.
   - On $(2,\infty)$: both factors are positive, so their product is positive. Hence $f'(x)>0$.

5. The sign table of the derivative is:

   | Interval | Sign of $f'(x)$ | Behavior of $f$ |
   |---|---|---|
   | $(-\infty,0)$ | $+$ | increasing |
   | $(0,2)$ | $-$ | decreasing |
   | $(2,\infty)$ | $+$ | increasing |

6. Apply the first-derivative test at each critical point:
   - At $x=0$: the derivative changes from positive to negative, so there is a local maximum. The value is $f(0)=0^3-3\cdot0^2+2=2$.
   - At $x=2$: the derivative changes from negative to positive, so there is a local minimum. The value is $f(2)=2^3-3\cdot2^2+2=8-12+2=-2$.

7. For the sketch: the graph rises on $(-\infty,0)$, reaches a peak at $(0,2)$, falls to a valley at $(2,-2)$, and rises again afterward. Mark the points $(0,2)$ and $(2,-2)$ as the critical points.

## Why each step is valid

- Differentiating a polynomial term by term is valid because polynomials are differentiable on all of $\mathbb{R}$.
- The zeros of $f'$ are the only candidates for local extrema because $f$ is differentiable everywhere (no other points where the derivative is undefined).
- The sign of $f'$ determines monotonicity by the increasing-decreasing theorem: positive derivative means increasing, negative means decreasing.
- The first-derivative test classifies a critical point as a local maximum when $f'$ changes from $+$ to $-$, and as a local minimum when $f'$ changes from $-$ to $+$.

## Final answer (in words)

The function increases on the intervals $(-\infty,0)$ and $(2,\infty)$, and decreases on the interval $(0,2)$. It has a local maximum at the point $(0,2)$ with value $2$, and a local minimum at the point $(2,-2)$ with value $-2$.

## Verification

We test the derivative at one point in each interval:
- At $x=-1$: $f'(-1)=3(-1)(-3)=9>0$, confirming increase on $(-\infty,0)$.
- At $x=1$: $f'(1)=3(1)(-1)=-3<0$, confirming decrease on $(0,2)$.
- At $x=3$: $f'(3)=3(3)(1)=9>0$, confirming increase on $(2,\infty)$.

The sign pattern matches the table above, so the monotonicity conclusions are correct.

## Common mistakes

- Forgetting that the derivative is negative between the two zeros $0$ and $2$, and assuming the sign stays the same on both sides of zero.
- Confusing the order of the critical points and assigning the maximum to $x=2$ instead of $x=0$.
- Sketching the graph without marking the critical points, which the problem explicitly requires.

## How I would explain it in class

First I take the derivative of the cubic and find where it equals zero, which gives me two critical points at zero and two. Then I check whether the derivative is positive or negative between those points to see where the graph goes up or down, and that tells me which point is the peak and which is the valley.
