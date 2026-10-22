# Problem 6

## The original problem

For
$$f(x)=x\sin x+\cos x$$
compute the derivative and simplify the result. Then compute $f'(0)$ and interpret the direction of the tangent line at that point.

> **Why this problem:** it combines the product rule with trigonometric derivatives and geometric interpretation.

## What we are looking for

We need $f'(x)$ in its simplest form. Then we compute the number $f'(0)$ and say what it tells us about the tangent line at $x=0$: does it go up, go down, or stay level?

## The idea we need

The **product rule**: if $f=u\,v$, then $f'=u'v+uv'$. The first term of our function, $x\sin x$, is a product of two different expressions of $x$, namely $x$ and $\sin x$. That is how we recognise that the product rule is needed. The second term, $\cos x$, is a single function, so it needs no rule beyond a known derivative. We also use the **sum rule** and the basic trigonometric derivatives
$$\frac{d}{dx}\sin x=\cos x,\qquad \frac{d}{dx}\cos x=-\sin x.$$
The angle $x$ is measured in radians.

## Step-by-step solution

**Step 1. Split the function.** $f(x)=x\sin x+\cos x$ is a sum of two parts. By the sum rule we differentiate them one at a time.

**Step 2. Differentiate $x\sin x$ by the product rule.** Take $u=x$ and $v=\sin x$. Then $u'=1$ and $v'=\cos x$. So
$$\frac{d}{dx}(x\sin x)=1\cdot\sin x+x\cos x=\sin x+x\cos x.$$

**Step 3. Differentiate $\cos x$.** It is $-\sin x$.

**Step 4. Add.**
$$f'(x)=\sin x+x\cos x-\sin x.$$

**Step 5. Simplify.** The terms $\sin x$ and $-\sin x$ cancel, so
$$f'(x)=x\cos x.$$

**Step 6. Evaluate at $0$.** $f'(0)=0\cdot\cos0=0\cdot1=0$.

**Step 7. The point of tangency.** $f(0)=0\cdot\sin0+\cos0=0+1=1$. The point is $(0,1)$.

**Step 8. Interpret.** The slope of the tangent line at $x=0$ is $0$. A line with slope $0$ is horizontal. So the tangent line at $(0,1)$ is the horizontal line $y=1$. It neither rises nor falls.

**Step 9. What happens next to $0$.** For small $x>0$, $\cos x$ is positive, so $f'(x)=x\cos x>0$. For small $x<0$, $x$ is negative and $\cos x$ is positive, so $f'(x)<0$. The graph goes down before $0$ and up after $0$, so $x=0$ is a local minimum with value $1$.

## Why each step is valid

- Step 2 is valid because the product rule applies to the product of two differentiable functions, and both $x$ and $\sin x$ are differentiable.
- Step 4 is valid by the sum rule.
- Step 5 is valid because a term and its negative add to zero.
- Step 8 is valid because the slope of the tangent line at a point is the value of the derivative there.
- Step 9 is valid because near zero the angle is small, and $\cos x$ is close to $1$, which is positive.

## Final answer (in words)

The derivative is $f'(x)=x\cos x$. At $x=0$ it equals $0$, so the tangent line to the graph at the point $(0,1)$ is horizontal, with equation $y=1$. The graph changes from falling to rising there.

## Verification

**Check 1: difference quotients at $0$.** We have $f(0)=1$. The quotient $\dfrac{f(h)-f(0)}{h}$ equals about $0.0499$ for $h=0.1$, about $0.0050$ for $h=0.01$, and about $0.0005$ for $h=0.001$. The values shrink to $0$, as $f'(0)=0$ says.

**Check 2: another point.** At $x=\pi$ the formula gives $f'(\pi)=\pi\cos\pi=-\pi\approx-3.1416$. The quotients with $h=0.1,\ 0.01,\ 0.001$ are about $-3.1862$, $-3.1465$, $-3.1421$. They approach $-3.1416$. The symmetric quotient with $h=10^{-5}$ gives $-3.14159265$.

**Check 3: a nearby value.** $f(0.1)=0.1\sin0.1+\cos0.1\approx0.00998+0.99500=1.00498$. This is bigger than $f(0)=1$, as a local minimum at $0$ requires.

## Common mistakes

- Differentiating $x\sin x$ as $1\cdot\cos x$, which is the product of the derivatives, instead of the product rule.
- Using $\frac{d}{dx}\cos x=+\sin x$. The sign is minus.
- Not simplifying, and leaving $\sin x+x\cos x-\sin x$, which hides the fact that $f'(0)=0$.
- Saying that $f'(0)=0$ means there is no tangent line. A slope of zero means a horizontal tangent line, not a missing one.

## How I would explain it in class

The first term is a product, so I use the product rule and get $\sin x+x\cos x$, and the derivative of $\cos x$ is $-\sin x$. The two sine terms cancel, which leaves the short formula $f'(x)=x\cos x$. At $x=0$ this equals $0$, so the tangent line at the point $(0,1)$ is the horizontal line $y=1$.
