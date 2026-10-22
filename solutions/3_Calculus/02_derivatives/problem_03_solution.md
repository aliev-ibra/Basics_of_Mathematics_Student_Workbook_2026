# Problem 3

## The original problem

For
$$f(x)=(x^2+1)e^x$$
compute the derivative. Then compare the correct result with the incorrect idea
$$f'(x)\stackrel{?}{=}(2x)e^x$$
and explain which term is missing.

> **Why this problem:** it teaches the product rule by analyzing a common mistake.

## What we are looking for

We need the correct derivative of the function $f(x)=(x^2+1)e^x$. Then we compare it with the tempting wrong answer $2x\,e^x$, which comes from differentiating only the first factor. We must say exactly what the wrong answer leaves out.

## The idea we need

The **product rule**. If $f(x)=u(x)\,v(x)$, then
$$f'(x)=u'(x)\,v(x)+u(x)\,v'(x).$$
In words: differentiate the first factor and keep the second, then keep the first and differentiate the second, and add the two results. We recognise that we need it because the function is two different expressions of $x$ multiplied together: the polynomial $x^2+1$ and the exponential $e^x$. We also use two basic derivatives: $\frac{d}{dx}(x^2+1)=2x$ and $\frac{d}{dx}e^x=e^x$.

## Step-by-step solution

**Step 1. Name the factors.** Let $u(x)=x^2+1$ and $v(x)=e^x$.

**Step 2. Differentiate each factor.** By the power rule and the fact that the constant $1$ has derivative zero, $u'(x)=2x$. The exponential $e^x$ is its own derivative, so $v'(x)=e^x$.

**Step 3. Apply the product rule.**
$$f'(x)=u'v+uv'=2x\,e^x+(x^2+1)e^x.$$

**Step 4. Simplify.** Both terms contain $e^x$, so we factor it out:
$$f'(x)=e^x\bigl(2x+x^2+1\bigr)=e^x\,(x^2+2x+1)=(x+1)^2e^x.$$
The last step uses the identity $x^2+2x+1=(x+1)^2$.

**Step 5. Compare with the wrong idea.** The wrong idea gives $2x\,e^x$. The correct answer is $2x\,e^x+(x^2+1)e^x$. The missing term is
$$(x^2+1)\,e^x=u\cdot v'.$$
It is the part of the product rule where the second factor changes while the first factor stays fixed.

**Step 6. A number that shows the difference.** At $x=0$ the wrong formula gives $2\cdot0\cdot e^0=0$. The correct formula gives $(0+1)^2e^0=1$. At $x=1$ the wrong formula gives $2e\approx5.4366$, while the correct one gives $4e\approx10.8731$.

**Step 7. Sign.** Because $(x+1)^2\ge0$ and $e^x>0$, we have $f'(x)\ge0$ for all $x$, and $f'(x)=0$ only at $x=-1$. So the graph never goes down, and its tangent is horizontal only at $x=-1$.

## Why each step is valid

- Step 3 is valid because the product rule holds for any two functions that have derivatives at the point.
- Step 4 is valid because factoring a common factor and recognising a perfect square are only algebra. They do not change the value.
- The wrong idea fails because the derivative of a product is not the product of the derivatives. Both factors depend on $x$, and when $x$ changes, both change. The product rule counts the effect of each factor changing separately.
- Step 7 is valid because a square is never negative and $e^x$ is always positive, so their product is never negative.

## Final answer (in words)

The derivative is $f'(x)=2x\,e^x+(x^2+1)e^x=(x+1)^2e^x$. The wrong answer $2x\,e^x$ is missing the term $(x^2+1)e^x$, which comes from the change of the factor $e^x$ while $x^2+1$ is held fixed.

## Verification

**Check 1: difference quotients at $x=0$.** Here $f(0)=1$. The quotient $\dfrac{f(h)-f(0)}{h}$ equals about $1.1622$ for $h=0.1$, about $1.0151$ for $h=0.01$, and about $1.0015$ for $h=0.001$. The values approach $1$, which matches the correct $f'(0)=1$ and not the wrong $0$.

**Check 2: difference quotients at $x=1$.** Here $f(1)=2e\approx5.4366$. The quotients for $h=0.1,\ 0.01,\ 0.001$ are about $12.026$, $10.982$, $10.884$. They approach $10.873$, which is $4e$. The wrong formula would give $5.4366$, far away.

**Check 3: the factored form.** Expanding $(x+1)^2e^x$ gives $(x^2+2x+1)e^x$, which equals $2xe^x+(x^2+1)e^x$. Both forms agree.

## Common mistakes

- Differentiating each factor and multiplying: $(x^2+1)'\cdot(e^x)'=2x\,e^x$. This is the mistake the problem shows.
- Using only one of the two terms of the product rule.
- Forgetting that $\frac{d}{dx}e^x=e^x$, and writing $xe^x$ or $e^{x-1}$.
- Making a sign slip when factoring, for example $e^x(x^2+2x-1)$.
- Not noticing that $x^2+2x+1$ is a perfect square, and then missing the sign information.

## How I would explain it in class

The function is a product of two different expressions in $x$, so I use the product rule: derivative of the first times the second, plus the first times the derivative of the second. That gives $2x\,e^x+(x^2+1)e^x$, which simplifies to $(x+1)^2e^x$. The wrong answer $2x\,e^x$ keeps only the first term, and at $x=0$ it says the slope is $0$ while the true slope is $1$.
