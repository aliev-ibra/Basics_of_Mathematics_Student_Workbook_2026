# Problem 4

## The original problem

Analyze

$$f(x)=\frac1{x^2-1}.$$

Determine the domain, asymptotes, sign, and monotonicity on the intervals of the domain. Explain why each interval must be analyzed separately.

## What we are looking for

We want to find the domain of the function, locate its asymptotes, determine where it is positive or negative, find where it increases or decreases, and explain why the separate pieces of the domain need separate treatment.

## The idea we need

The domain of a rational function excludes values that make the denominator zero. Vertical asymptotes occur at those excluded values when the one-sided limits are infinite. The sign of the function follows from the sign of the denominator since the numerator is constant and positive. The derivative sign determines monotonicity on each connected interval of the domain. Each interval must be analyzed separately because the domain is disconnected: the function is not defined at the points splitting the intervals, so monotonicity cannot jump across them.

## Step-by-step solution

1. Domain: the denominator $x^2-1=(x-1)(x+1)$ is zero when $x=1$ or $x=-1$. Hence

   $$\text{Domain}=(-\infty,-1)\cup(-1,1)\cup(1,\infty).$$

2. Vertical asymptotes: at $x=-1$ and $x=1$, the denominator is zero while the numerator is $1\ne0$. We check the one-sided limits:

   - As $x\to-1^-$: $x^2-1\to0^+$ (since $x^2>1$), so $f(x)\to+\infty$.
   - As $x\to-1^+$: $x^2-1\to0^-$ (since $x^2<1$), so $f(x)\to-\infty$.
   - As $x\to1^-$: $x^2-1\to0^-$, so $f(x)\to-\infty$.
   - As $x\to1^+$: $x^2-1\to0^+$, so $f(x)\to+\infty$.

   Thus $x=-1$ and $x=1$ are both vertical asymptotes.

3. Horizontal asymptote: as $x\to\pm\infty$, the denominator $x^2-1\to\infty$, so

   $$\lim_{x\to\pm\infty}\frac1{x^2-1}=0.$$

   Hence $y=0$ is a horizontal asymptote.

4. Sign of $f$: the numerator is $1>0$, so the sign of $f$ equals the sign of $x^2-1$:
   - $x^2-1>0$ when $|x|>1$, i.e., on $(-\infty,-1)\cup(1,\infty)$, so $f>0$ there.
   - $x^2-1<0$ when $|x|<1$, i.e., on $(-1,1)$, so $f<0$ there.

5. Derivative: using the chain rule or quotient rule with $u=1$ and $v=x^2-1$:

   $$f'(x)=\frac{0\cdot(x^2-1)-1\cdot(2x)}{(x^2-1)^2}=\frac{-2x}{(x^2-1)^2}.$$

6. Sign of the derivative: the denominator $(x^2-1)^2$ is positive for all $x$ in the domain. The numerator $-2x$ determines the sign:
   - $f'(x)>0$ when $-2x>0$, i.e., $x<0$. On the domain, this means $(-\infty,-1)$ and $(-1,0)$.
   - $f'(x)<0$ when $-2x<0$, i.e., $x>0$. On the domain, this means $(0,1)$ and $(1,\infty)$.
   - $f'(x)=0$ when $x=0$, which is in the domain.

7. Monotonicity on each interval:
   - $(-\infty,-1)$: $f'>0$, increasing.
   - $(-1,0)$: $f'>0$, increasing.
   - $(0,1)$: $f'<0$, decreasing.
   - $(1,\infty)$: $f'<0$, decreasing.

   At $x=0$, the derivative changes from positive to negative, so there is a local maximum at $(0,f(0))=(0,-1)$.

8. Why each interval separately: the domain has three connected components separated by $x=-1$ and $x=1$, where the function is undefined. Monotonicity is a property on an interval, and we cannot say the function "increases from $(-\infty,-1)$ to $(-1,0)$" because there is no connection across the asymptote. The sign table of the derivative must be built on each component independently.

## Why each step is valid

- The domain excludes $\pm1$ because division by zero is undefined.
- The vertical asymptotes follow from the one-sided limits tending to $\pm\infty$ with a nonzero numerator.
- The horizontal asymptote $y=0$ follows from the limit at infinity since the denominator grows without bound.
- The sign of $f$ matches the sign of $x^2-1$ because the numerator $1$ is positive.
- The quotient rule applies because both $1$ and $x^2-1$ are differentiable and the denominator is nonzero on the domain.
- Monotonicity is concluded separately on each connected component because the domain is disconnected at the asymptotes.

## Final answer (in words)

The domain is $(-\infty,-1)\cup(-1,1)\cup(1,\infty)$. There are vertical asymptotes at $x=-1$ and $x=1$, and a horizontal asymptote at $y=0$. The function is positive on $(-\infty,-1)\cup(1,\infty)$ and negative on $(-1,1)$. It increases on $(-\infty,-1)$ and $(-1,0)$, and decreases on $(0,1)$ and $(1,\infty)$. There is a local maximum at $(0,-1)$. Each interval is analyzed separately because the domain is disconnected by the vertical asymptotes.

## Verification

We check the derivative at test points:
- At $x=-2$: $f'(-2)=\frac{-2(-2)}{((-2)^2-1)^2}=\frac{4}{9}>0$, confirming increase on $(-\infty,-1)$.
- At $x=-0.5$: $f'(-0.5)=\frac{-2(-0.5)}{((-0.5)^2-1)^2}=\frac{1}{(-0.75)^2}>0$, confirming increase on $(-1,0)$.
- At $x=0.5$: $f'(0.5)=\frac{-2(0.5)}{(0.25-1)^2}=\frac{-1}{(-0.75)^2}<0$, confirming decrease on $(0,1)$.
- At $x=2$: $f'(2)=\frac{-4}{(4-1)^2}=\frac{-4}{9}<0$, confirming decrease on $(1,\infty)$.

The second derivative test at $x=0$: $f''(x)=\frac{-2(x^2-1)^2+8x^2(x^2-1)}{(x^2-1)^4}$, at $x=0$ gives $f''(0)=\frac{-2(1)}{1}=-2<0$, confirming a local maximum at $x=0$.

## Common mistakes

- Combining $(-\infty,-1)$ and $(-1,0)$ into a single increasing interval, ignoring that $x=-1$ breaks the domain.
- Forgetting that $f$ is negative on $(-1,1)$, since $x^2-1<0$ there.
- Missing the local maximum at $x=0$ because $f'(0)=0$ lies between two asymptotes.

## How I would explain it in class

The function blows up at $x=-1$ and $x=1$, so those are vertical asymptotes and they chop the number line into three separate pieces. On each piece I check whether the derivative is positive or negative, which tells me the graph goes up on the two left-of-zero pieces and down on the two right-of-zero pieces, with a peak at $x=0$ where the value is $-1$.
