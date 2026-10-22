# Problem 9

## The original problem

For
$$f(x)=\ln(x^2+1)$$
compute the derivative. Then determine the sign of $f'(x)$ for $x<0$, $x=0$, and $x>0$, and describe qualitatively how the function behaves around zero.

> **Why this problem:** it connects differentiation with sign analysis and the behavior of a function.

## What we are looking for

We need two things. First, a formula for the derivative $f'(x)$. The derivative tells us the slope of the graph at each point. Second, we need to decide where this slope is negative, zero, or positive. Then we use these signs to describe the shape of the graph near $x=0$. A negative slope means the graph goes down as we move right. A positive slope means it goes up.

## The idea we need

The **chain rule**. It is for a function made of two layers, an outer function applied to an inner function. We write it as $\frac{d}{dx}F(g(x))=F'(g(x))\cdot g'(x)$. In words: differentiate the outer layer, keep the inner layer inside it unchanged, then multiply by the derivative of the inner layer.

We recognise it here because $\ln$ is applied not to $x$ but to the whole expression $x^2+1$. The outer layer is $\ln(u)$. The inner layer is $u=x^2+1$.

We also use two basic facts. The derivative of $\ln u$ with respect to $u$ is $\frac{1}{u}$. The derivative of $x^2+1$ is $2x$.

The domain is all real numbers. The reason is that $x^2+1\ge 1$, so it is always positive, and the logarithm is defined for positive numbers only.

## Step-by-step solution

1. Name the layers. The inner layer is $u=x^2+1$. The outer layer is $\ln(u)$.
2. Differentiate the outer layer. The derivative of $\ln(u)$ is $\frac1u$. We keep $u=x^2+1$ inside, so we get $\frac{1}{x^2+1}$.
3. Differentiate the inner layer. The derivative of $x^2+1$ is $2x$. The constant $1$ contributes nothing.
4. Multiply the two results, as the chain rule says:
$$f'(x)=\frac{1}{x^2+1}\cdot 2x=\frac{2x}{x^2+1}.$$
5. Study the denominator. Since $x^2\ge 0$, we have $x^2+1\ge 1>0$. The denominator is always positive. So the sign of $f'(x)$ is the sign of the numerator $2x$, which is the sign of $x$.
6. Case $x<0$. Then $2x<0$ and the denominator is positive, so $f'(x)<0$. The slope is negative.
7. Case $x=0$. Then $f'(0)=\frac{0}{1}=0$. The slope is zero.
8. Case $x>0$. Then $2x>0$, so $f'(x)>0$. The slope is positive.
9. Describe the behaviour. To the left of $0$ the function decreases. At $0$ the tangent line is horizontal. To the right of $0$ the function increases. Also $f(0)=\ln 1=0$, and for every $x$ we have $x^2+1\ge1$, so $f(x)\ge\ln 1=0$. So the point $(0,0)$ is the lowest point of the graph. It is a minimum.

## Why each step is valid

- Step 2 is valid because the rule $\frac{d}{du}\ln u=\frac1u$ holds for every $u>0$, and our $u=x^2+1$ is always positive.
- Step 4 is valid because the chain rule says to multiply the derivative of the outer layer, evaluated at the inner layer, by the derivative of the inner layer.
- Step 5 is valid because a fraction with a positive denominator has the same sign as its numerator.
- Steps 6 to 8 are valid because the sign of the derivative tells the direction of the function. If $f'$ is negative on an interval, the function decreases there. If $f'$ is positive, it increases there.
- Step 9 is valid because the function goes down up to $0$ and up after $0$, and its value at $0$ is the smallest value it ever takes.

## Final answer (in words)

The derivative is $f'(x)=\dfrac{2x}{x^2+1}$. For $x<0$ it is negative, so the function decreases. At $x=0$ it equals $0$, so the tangent line is horizontal. For $x>0$ it is positive, so the function increases. Around zero the graph has a smooth lowest point at $(0,0)$, with value $f(0)=0$, and it is symmetric about the vertical axis.

## Verification

**Check 1: symmetry.** Since $(-x)^2=x^2$, we have $f(-x)=f(x)$. The graph is mirror-symmetric about the vertical axis. A mirror image turns a rising slope into a falling slope of the same size. So $f'$ must change sign when $x$ changes sign. Our formula gives $f'(-x)=\frac{-2x}{x^2+1}=-f'(x)$. This agrees. For example $f'(-1)=-1$ and $f'(1)=1$.

**Check 2: numbers from the definition.** We use the difference quotient at $x=1$ with $h=0.01$:
$$\frac{\ln(1.01^2+1)-\ln 2}{0.01}=\frac{\ln 2.0201-\ln 2}{0.01}\approx 0.99998.$$
The formula gives $f'(1)=\frac{2}{2}=1$. The two numbers agree. This is evidence from a computation that does not use the chain rule.

**Check 3: values.** $f(-1)=f(1)=\ln 2\approx0.693$, which is larger than $f(0)=0$. This matches the picture: down to zero, then up.

## Common mistakes

- Writing $f'(x)=\frac1{x^2+1}$ and forgetting the factor $2x$ from the inner layer.
- Writing $f'(x)=\frac{1}{2x}$, which means differentiating the inside instead of the outside.
- Saying the sign depends on the denominator. The denominator is always positive, so only the numerator matters.
- Thinking that $f'(0)=0$ means the function is constant. It only means the tangent line is horizontal at that one point.

## How I would explain it in class

I see $\ln$ applied to the whole expression $x^2+1$, so I use the chain rule: the outside gives $\frac{1}{x^2+1}$ and the inside gives $2x$, which multiply to $\frac{2x}{x^2+1}$. The denominator is always positive, so the sign of the derivative is the sign of $x$: negative to the left of zero, zero at zero, positive to the right. So the graph falls, flattens at the point $(0,0)$, and then rises, which means $0$ is the lowest point.
