# Problem 5

## The original problem

Analyze the monotonicity and extrema of

$$f(x)=xe^{-x}.$$

Also examine the behavior as $x\to\infty$ and explain how the limit affects the shape of the graph on the right-hand side.

## What we are looking for

We want to find where the function increases and decreases, locate its local extremum, and describe what happens to the graph as $x$ grows very large in the positive direction.

## The idea we need

The function is a product of $x$ and $e^{-x}$, so we differentiate using the product rule. A critical point occurs where $f'(x)=0$. Since $e^{-x}>0$ for all $x$, the sign of $f'$ is determined by the remaining factor. The limit as $x\to\infty$ tells us the end behavior on the right: if $f(x)\to0$, the graph approaches the x-axis, giving a horizontal asymptote $y=0$ on the right-hand side.

## Step-by-step solution

1. Domain: both $x$ and $e^{-x}$ are defined for all real numbers, so the domain is $\mathbb{R}$.

2. Compute the derivative using the product rule $(uv)'=u'v+uv'$ with $u=x$ and $v=e^{-x}$. Since $u'=1$ and $v'=-e^{-x}$:

   $$f'(x)=1\cdot e^{-x}+x\cdot(-e^{-x})=e^{-x}-xe^{-x}=e^{-x}(1-x).$$

3. Find the critical points by solving $f'(x)=0$:

   $$e^{-x}(1-x)=0.$$

   Since $e^{-x}>0$ for all $x$, we must have $1-x=0$, so

   $$x=1.$$

   This is the only critical point.

4. Sign of the derivative: $e^{-x}>0$ always, so the sign of $f'$ is the sign of $(1-x)$:
   - For $x<1$: $1-x>0$, so $f'(x)>0$, and $f$ is increasing.
   - For $x>1$: $1-x<0$, so $f'(x)<0$, and $f$ is decreasing.

5. Sign table:

   | Interval | Sign of $f'(x)$ | Behavior of $f$ |
   |---|---|---|
   | $(-\infty,1)$ | $+$ | increasing |
   | $(1,\infty)$ | $-$ | decreasing |

6. Extremum: at $x=1$, the derivative changes from positive to negative, so by the first-derivative test there is a local maximum. The value is

   $$f(1)=1\cdot e^{-1}=\frac1e.$$

   So the local maximum is at $(1,\frac1e)$.

7. Behavior as $x\to\infty$: we compute

   $$\lim_{x\to\infty}xe^{-x}=\lim_{x\to\infty}\frac{x}{e^x}.$$

   Both numerator and denominator grow without bound, so this is an $\infty/\infty$ form. Exponential growth dominates polynomial growth, so

   $$\lim_{x\to\infty}\frac{x}{e^x}=0.$$

   Therefore $f(x)\to0$ as $x\to\infty$, meaning the graph approaches the x-axis from above (since $f(x)>0$ for $x>0$) and $y=0$ is a horizontal asymptote on the right-hand side.

8. Effect on the shape on the right-hand side: after the maximum at $x=1$, the function decreases toward $0$ as $x\to\infty$, never crossing the x-axis for $x>0$ and flattening out toward the horizontal asymptote $y=0$.

## Why each step is valid

- The product rule applies because both $x$ and $e^{-x}$ are differentiable everywhere.
- The only critical point is $x=1$ because $e^{-x}$ is never zero, so $f'(x)=0$ exactly when $1-x=0$.
- The sign of $f'$ is the sign of $(1-x)$ because $e^{-x}$ is always positive and does not affect the sign.
- The first-derivative test applies because $f$ is differentiable everywhere and the derivative changes sign at $x=1$.
- The limit $\lim_{x\to\infty}x/e^x=0$ is valid because exponential growth dominates linear growth; this can also be shown by l'Hôpital's rule.
- The horizontal asymptote on the right follows directly from the limit being $0$.

## Final answer (in words)

The function increases on $(-\infty,1)$ and decreases on $(1,\infty)$. It has a local maximum at $(1,\frac1e)$. As $x\to\infty$, $f(x)\to0$, so the graph approaches the horizontal asymptote $y=0$ from above on the right-hand side.

## Verification

Test the derivative at one point in each interval:
- At $x=0$: $f'(0)=e^0(1-0)=1>0$, confirming increase on $(-\infty,1)$.
- At $x=2$: $f'(2)=e^{-2}(1-2)=-e^{-2}<0$, confirming decrease on $(1,\infty)$.

Confirm the extremum type with the second derivative:

$$f''(x)=\frac{d}{dx}\left(e^{-x}(1-x)\right)=-e^{-x}(1-x)+e^{-x}(-1)=e^{-x}(x-2).$$

At $x=1$: $f''(1)=e^{-1}(1-2)=-1/e<0$, confirming a local maximum at $x=1$.

Check the asymptote: $f(10)=10/e^{10}\approx0.000454$, very close to $0$, consistent with $y=0$ as $x$ grows.

## Common mistakes

- Forgetting that $e^{-x}>0$ for all $x$ and incorrectly concluding that $f'(x)=0$ when $e^{-x}=0$, which never happens.
- Claiming the function decreases across all of $\mathbb{R}$ after finding one negative value, ignoring the change of sign at $x=1$.
- Missing the horizontal asymptote and drawing the graph as continuing to drop without bound to the right.

## How I would explain it in class

I use the product rule to get the derivative, which factors as $e^{-x}(1-x)$. Since $e^{-x}$ is always positive, the sign depends only on $1-x$, so the graph goes up until $x=1$ and down afterward, with a peak at $(1,1/e)$. As $x$ gets very large, the exponential in the denominator wins over the linear $x$ on top, so the whole thing shrinks to zero and the graph flattens onto the x-axis.
