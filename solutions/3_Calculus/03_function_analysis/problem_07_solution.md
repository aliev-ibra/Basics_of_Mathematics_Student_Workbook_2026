# Problem 7

## The original problem

On $[0,2\pi]$, find the intervals of monotonicity and the extrema of

$$f(x)=\sin x+\cos x.$$

Include the endpoints of the interval and compare the function values at the critical points and at the endpoints.

## What we are looking for

We want to find where the function increases and decreases on the closed interval $[0,2\pi]$, locate its local extrema, check the endpoints, and identify the absolute maximum and minimum by comparing all relevant values.

## The idea we need

On a closed interval, extrema can occur at critical points in the interior where $f'(x)=0$, or at the endpoints. The derivative is $f'(x)=\cos x-\sin x$. Setting it to zero gives $\cos x=\sin x$, or $\tan x=1$, whose solutions in $[0,2\pi]$ are $x=\pi/4$ and $x=5\pi/4$. The sign of $f'$ on each subinterval determines monotonicity. We compare values at the critical points and at the endpoints $0$ and $2\pi$ to find the absolute extrema.

## Step-by-step solution

1. Domain: the interval is given as $[0,2\pi]$. Both $\sin x$ and $\cos x$ are defined everywhere, so there are no additional restrictions.

2. Derivative:

   $$f'(x)=\cos x-\sin x.$$

3. Critical points: solve $f'(x)=0$:

   $$\cos x-\sin x=0\implies \cos x=\sin x\implies \tan x=1.$$

   In $[0,2\pi]$, the solutions are

   $$x=\frac{\pi}{4}\quad\text{and}\quad x=\frac{5\pi}{4}.$$

4. Sign of the derivative. We can write $f'(x)=\sqrt{2}\cos(x+\pi/4)$, or simply test points in each subinterval:
   - On $[0,\pi/4)$: test $x=0$: $f'(0)=\cos0-\sin0=1-0=1>0$, so $f$ is increasing.
   - On $(\pi/4,5\pi/4)$: test $x=\pi$: $f'(\pi)=\cos\pi-\sin\pi=-1-0=-1<0$, so $f$ is decreasing.
   - On $(5\pi/4,2\pi]$: test $x=2\pi$: $f'(2\pi)=\cos2\pi-\sin2\pi=1-0=1>0$, so $f$ is increasing.

5. Sign table:

   | Interval | Sign of $f'(x)$ | Behavior of $f$ |
   |---|---|---|
   | $[0,\pi/4)$ | $+$ | increasing |
   | $(\pi/4,5\pi/4)$ | $-$ | decreasing |
   | $(5\pi/4,2\pi]$ | $+$ | increasing |

6. Local extrema:
   - At $x=\pi/4$: $f'$ changes from $+$ to $-$, so a local maximum. Value:

     $$f\left(\frac{\pi}{4}\right)=\sin\frac{\pi}{4}+\cos\frac{\pi}{4}=\frac{\sqrt2}{2}+\frac{\sqrt2}{2}=\sqrt2.$$

   - At $x=5\pi/4$: $f'$ changes from $-$ to $+$, so a local minimum. Value:

     $$f\left(\frac{5\pi}{4}\right)=\sin\frac{5\pi}{4}+\cos\frac{5\pi}{4}=-\frac{\sqrt2}{2}-\frac{\sqrt2}{2}=-\sqrt2.$$

7. Endpoints:
   - At $x=0$: $f(0)=\sin0+\cos0=0+1=1$.
   - At $x=2\pi$: $f(2\pi)=\sin2\pi+\cos2\pi=0+1=1$.

8. Comparison of all values:
   - $f(0)=1$
   - $f(\pi/4)=\sqrt2\approx1.414$ (local maximum)
   - $f(5\pi/4)=-\sqrt2\approx-1.414$ (local minimum)
   - $f(2\pi)=1$

   The absolute maximum on $[0,2\pi]$ is $\sqrt2$ at $x=\pi/4$. The absolute minimum is $-\sqrt2$ at $x=5\pi/4$. The endpoints both give value $1$, which is neither the absolute maximum nor the absolute minimum.

## Why each step is valid

- Differentiating $\sin x$ and $\cos x$ term by term is valid because both are differentiable everywhere.
- Solving $\tan x=1$ gives all critical points in $[0,2\pi]$ because $f'$ is defined everywhere on the interval and the only zeros come from $\cos x=\sin x$.
- Testing one point per subinterval is valid because $f'$ is continuous and can change sign only at its zeros, so the sign is constant on each subinterval between consecutive zeros.
- The endpoints must be checked separately because on a closed interval the absolute extremum can occur at an endpoint even when the derivative is nonzero there.
- Comparing all candidate values identifies the absolute maximum and minimum on the closed interval.

## Final answer (in words)

On $[0,2\pi]$, the function increases on $[0,\pi/4)$ and $(5\pi/4,2\pi]$, and decreases on $(\pi/4,5\pi/4)$. It has a local maximum at $x=\pi/4$ with value $\sqrt2$, and a local minimum at $x=5\pi/4$ with value $-\sqrt2$. The endpoints both have value $1$. The absolute maximum is $\sqrt2$ at $x=\pi/4$, and the absolute minimum is $-\sqrt2$ at $x=5\pi/4$.

## Verification

Check the derivative sign at test points:
- At $x=\pi/2$: $f'(\pi/2)=\cos(\pi/2)-\sin(\pi/2)=0-1=-1<0$, confirming decrease on $(\pi/4,5\pi/4)$.
- At $x=7\pi/4$: $f'(7\pi/4)=\cos(7\pi/4)-\sin(7\pi/4)=\frac{\sqrt2}{2}-(-\frac{\sqrt2}{2})=\sqrt2>0$, confirming increase on $(5\pi/4,2\pi]$.

Confirm extremum types with the second derivative:

$$f''(x)=-\sin x-\cos x=-f(x).$$

At $x=\pi/4$: $f''(\pi/4)=-\sqrt2<0$, confirming a local maximum.
At $x=5\pi/4$: $f''(5\pi/4)=\sqrt2>0$, confirming a local minimum.

## Common mistakes

- Forgetting to check the endpoints $x=0$ and $x=2\pi$, which are candidates for absolute extrema on a closed interval.
- Missing the second solution $x=5\pi/4$ of $\tan x=1$ in $[0,2\pi]$ and only finding $x=\pi/4$.
- Assuming the endpoint values are extrema without comparing them to the critical-point values.

## How I would explain it in class

I take the derivative, which is cosine minus sine, and set it to zero, giving me two angles in the interval: $\pi/4$ and $5\pi/4$. Testing between them shows the graph goes up, then down, then up again, so the first point is a peak and the second is a valley. Finally I check the two ends of the interval, both giving $1$, and see that the peak at $\sqrt2$ and the valley at $-\sqrt2$ beat the endpoints, so those are the absolute highest and lowest points.
