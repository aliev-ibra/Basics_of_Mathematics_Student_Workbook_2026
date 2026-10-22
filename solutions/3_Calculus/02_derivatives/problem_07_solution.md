# Problem 7

## The original problem

For
$$f(x)=\sin(x^2+1)$$
compute the derivative. Explicitly identify the outer function, the inner function, and the derivative of the inner function. Finally, determine the sign of $f'(0)$.

> **Why this problem:** it reinforces the chain rule in a different type of composition.

## What we are looking for

We need $f'(x)$. We must name the three pieces: the outer function, the inner function, and the derivative of the inner function. Then we decide whether $f'(0)$ is positive, negative, or zero.

## The idea we need

The **chain rule**: if $f(x)=F(g(x))$, then $f'(x)=F'(g(x))\cdot g'(x)$. In words: differentiate the outer function with the inner function left as it is, then multiply by the derivative of the inner function. We recognise a composition because the sine does not act on $x$ directly. It acts on the expression $x^2+1$. We also need $\frac{d}{dx}\sin t=\cos t$ and the power rule $\frac{d}{dx}x^2=2x$. The angle is measured in radians.

## Step-by-step solution

**Step 1. Outer function.** The outer function is the sine: $F(t)=\sin t$.

**Step 2. Inner function.** The inner function is $g(x)=x^2+1$. Then $f(x)=F(g(x))=\sin(x^2+1)$.

**Step 3. Derivative of the outer function.** $F'(t)=\cos t$. With the inner function put back, $F'(g(x))=\cos(x^2+1)$.

**Step 4. Derivative of the inner function.** $g'(x)=2x$, because the power rule gives $2x$ for $x^2$ and the constant $1$ has derivative $0$.

**Step 5. Multiply.**
$$f'(x)=\cos(x^2+1)\cdot2x=2x\cos(x^2+1).$$

**Step 6. Evaluate at $0$.** The inside is $0^2+1=1$, so $\cos(0^2+1)=\cos1$. Then
$$f'(0)=2\cdot0\cdot\cos1=0.$$

**Step 7. The sign.** The value $f'(0)$ is neither positive nor negative. It is zero, because the factor $2x$ is zero at $x=0$. Note that $\cos1\approx0.5403$ is positive, but this does not matter since it is multiplied by $0$.

**Step 8. The tangent line.** The point of tangency is $(0,f(0))=(0,\sin1)\approx(0,0.8415)$. The slope is $0$, so the tangent line is horizontal, $y=\sin1$.

## Why each step is valid

- Steps 1 to 5 are valid because the chain rule applies when the outer function (sine) and the inner function (a polynomial) are both differentiable, and they are for every $x$.
- In Step 3 the inner expression stays inside the cosine, because $F'$ is evaluated at $g(x)$.
- Step 6 is valid because we only substitute $x=0$ into the formula for $f'$.
- Step 7 is valid because a product with a zero factor equals zero, whatever the other factor is.

## Final answer (in words)

The outer function is $\sin$, the inner function is $x^2+1$, and the derivative of the inner function is $2x$. The derivative is $f'(x)=2x\cos(x^2+1)$. At $x=0$ it equals $0$, so its sign is neither positive nor negative, and the tangent line there is horizontal.

## Verification

**Check 1: difference quotients at $0$.** We have $f(0)=\sin1\approx0.84147$. Since $f(h)=\sin(h^2+1)$, the quotient $\dfrac{f(h)-f(0)}{h}$ is small. For $h=0.1$ it is $\dfrac{\sin1.01-\sin1}{0.1}\approx0.0536$. For $h=0.01$ it is about $0.0054$. It shrinks toward $0$ as $h$ shrinks, in agreement with $f'(0)=0$.

**Check 2: a point where the answer is not zero.** At $x=1$ the formula gives $f'(1)=2\cos2\approx-0.8323$. The quotients with $h=0.1,\ 0.01,\ 0.001$ are about $-1.0673$, $-0.8548$, $-0.8345$. They approach $-0.8323$. The symmetric quotient with $h=10^{-5}$ gives $-0.83229367$, which agrees to seven digits with $2\cos2=-0.83229367$.

**Check 3: symmetry.** The function $f$ is even, because $f(-x)=\sin((-x)^2+1)=f(x)$. The graph of an even function is symmetric about the vertical axis, so its tangent at $x=0$ must be horizontal. This is a reason, independent of the chain rule, for $f'(0)=0$.

## Common mistakes

- Writing $\cos(2x)$ instead of $2x\cos(x^2+1)$: differentiating the inside and putting it in the cosine.
- Forgetting the factor $2x$.
- Differentiating the sine as $-\cos$. The derivative of $\sin$ is $+\cos$.
- Replacing $x^2+1$ by $x$ in the cosine, which loses the inner function.
- Claiming that $f'(0)$ is positive because $\cos1>0$.

## How I would explain it in class

The sine is applied to the expression $x^2+1$, so this is a composition: the outer function is sine and the inner function is $x^2+1$. The chain rule tells me to take cosine of the same inside and multiply by the derivative of the inside, which is $2x$. This gives $2x\cos(x^2+1)$, and at $x=0$ the factor $2x$ is zero, so $f'(0)=0$ and the tangent line is horizontal.
