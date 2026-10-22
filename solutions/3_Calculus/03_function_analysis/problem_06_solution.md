# Problem 6

## The original problem

Analyze the domain, zero, and monotonicity of

$$f(x)=\ln x-x+1.$$

Explain why the analysis must begin with the domain.

## What we are looking for

We want to find where the function is defined, where it equals zero, and on which intervals it increases or decreases, with an explanation of why the domain comes first.

## The idea we need

The natural logarithm $\ln x$ is defined only for $x>0$, so the domain is the starting point of the analysis: no derivative or sign can be considered outside the domain. Once the domain is known, the derivative $f'(x)=1/x-1$ is computed, its zero found, and the sign table built on the intervals of the domain. The monotonicity follows from the sign of the derivative on each subinterval.

## Step-by-step solution

1. Domain: $\ln x$ requires $x>0$. The terms $-x+1$ are defined everywhere, so the domain is determined solely by the logarithm:

   $$\text{Domain}=(0,\infty)=\{x\in\mathbb{R}:x>0\}.$$

   This is why the analysis must begin with the domain: we cannot differentiate, find zeros, or discuss monotonicity at any $x\le0$ because the function itself is not defined there.

2. Zero of the function: solve $\ln x-x+1=0$. Try $x=1$:

   $$\ln 1-1+1=0-1+1=0.$$

   So $x=1$ is a zero. To check uniqueness, we use monotonicity (computed below): $f$ increases on $(0,1)$ and decreases on $(1,\infty)$, with maximum value $f(1)=0$. Since the maximum value is $0$ and it is attained only at $x=1$, the zero $x=1$ is unique.

3. Derivative: $\ln x$ differentiates to $1/x$, and $-x+1$ differentiates to $-1$:

   $$f'(x)=\frac1x-1=\frac{1-x}{x}.$$

4. Critical point: solve $f'(x)=0$:

   $$\frac{1-x}{x}=0\implies 1-x=0\implies x=1.$$

   The derivative is undefined at $x=0$, but $x=0$ is not in the domain anyway.

5. Sign of the derivative on $(0,\infty)$: the denominator $x$ is positive for all $x$ in the domain, so the sign of $f'$ is the sign of $1-x$:
   - For $0<x<1$: $1-x>0$, so $f'(x)>0$, and $f$ is increasing.
   - For $x>1$: $1-x<0$, so $f'(x)<0$, and $f$ is decreasing.

6. Sign table:

   | Interval | Sign of $f'(x)$ | Behavior of $f$ |
   |---|---|---|
   | $(0,1)$ | $+$ | increasing |
   | $(1,\infty)$ | $-$ | decreasing |

7. Extremum: at $x=1$, the derivative changes from positive to negative, so there is a local maximum. The value is

   $$f(1)=\ln 1-1+1=0.$$

   So the local maximum is at $(1,0)$, which is also the unique zero of the function.

## Why each step is valid

- The domain is $(0,\infty)$ because $\ln x$ is undefined for $x\le0$; this is the necessary starting point.
- The derivative $1/x-1$ is valid by the sum rule and the derivative of $\ln x$, which holds for $x>0$.
- The only critical point in the domain is $x=1$; $x=0$ is excluded from the domain so it is not a critical point.
- The sign of $f'$ is determined by $1-x$ because $x>0$ on the domain, so the denominator never changes sign.
- The first-derivative test applies because $f$ is differentiable on $(0,\infty)$ and $f'$ changes from $+$ to $-$ at $x=1$.

## Final answer (in words)

The domain is $(0,\infty)$, and the analysis must start there because $\ln x$ is undefined for $x\le0$. The unique zero is at $x=1$. The function increases on $(0,1)$ and decreases on $(1,\infty)$, with a local maximum at $(1,0)$.

## Verification

Test the derivative at one point in each interval:
- At $x=0.5$: $f'(0.5)=1/0.5-1=2-1=1>0$, confirming increase on $(0,1)$.
- At $x=2$: $f'(2)=1/2-1=-0.5<0$, confirming decrease on $(1,\infty)$.

Confirm the maximum with the second derivative:

$$f''(x)=-\frac1{x^2}.$$

At $x=1$: $f''(1)=-1<0$, confirming a local maximum at $x=1$.

Check the zero: $f(1)=0$, and since $f(0.5)=\ln0.5-0.5+1\approx-0.693+0.5= -0.193<0$ and $f(2)=\ln2-2+1\approx0.693-1=-0.307<0$, the value $0$ at $x=1$ is indeed the peak and the only zero.

## Common mistakes

- Starting the analysis with the derivative before stating the domain, which could lead to considering $x\le0$ where $\ln x$ is undefined.
- Claiming there are zeros other than $x=1$ without checking that the maximum value is $0$ and is attained only once.
- Treating $(0,\infty)$ as one interval for monotonicity and missing the change at $x=1$.

## How I would explain it in class

First I point out that the natural log only works for positive numbers, so the whole conversation starts with $x>0$. Then I differentiate and find the derivative changes sign at $x=1$, meaning the graph climbs up to $x=1$ and goes down after that, hitting exactly zero at the top. Since the highest point is zero and it only touches zero there, $x=1$ is the only place the graph meets the x-axis.
