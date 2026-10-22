# Problem 4

## The original problem

For
$$f(x)=\frac{x^2+1}{x-1}$$
determine the domain, compute the derivative, simplify the result, and explain why the restriction $x\neq1$ remains important.

> **Why this problem:** it practices the quotient rule together with domain control.

## What we are looking for

We need three things: the set of numbers where the fraction makes sense, a simplified formula for $f'(x)$, and an explanation of why $x=1$ stays forbidden even after we simplify.

## The idea we need

The **quotient rule**. If $f(x)=\dfrac{u(x)}{v(x)}$ and $v(x)\ne0$, then
$$f'(x)=\frac{u'(x)\,v(x)-u(x)\,v'(x)}{\bigl(v(x)\bigr)^2}.$$
In words: bottom times the derivative of the top, minus top times the derivative of the bottom, all divided by the bottom squared. We recognise that we need it because the function is one expression of $x$ divided by another expression of $x$. The rule itself requires that the bottom is not zero, so the domain matters from the start.

## Step-by-step solution

**Step 1. Domain.** A fraction is defined only when its denominator is not zero. The denominator $x-1$ is zero exactly when $x=1$. So the domain is all real numbers except $1$, that is $(-\infty,1)\cup(1,\infty)$.

**Step 2. Name the parts.** Let $u(x)=x^2+1$ (the top) and $v(x)=x-1$ (the bottom). Then $u'(x)=2x$ and $v'(x)=1$.

**Step 3. Apply the quotient rule.**
$$f'(x)=\frac{2x\,(x-1)-(x^2+1)\cdot1}{(x-1)^2}.$$

**Step 4. Expand the numerator.** First $2x(x-1)=2x^2-2x$. Then subtract $x^2+1$:
$$2x^2-2x-x^2-1=x^2-2x-1.$$
So
$$f'(x)=\frac{x^2-2x-1}{(x-1)^2},\qquad x\neq1.$$

**Step 5. Check whether anything cancels.** At $x=1$ the numerator equals $1-2-1=-2$, which is not zero. So the numerator does not contain the factor $x-1$, and nothing cancels. The formula is already in simplest form.

**Step 6. Why $x\ne1$ stays.** The denominator $(x-1)^2$ is zero at $x=1$, and the numerator is $-2$ there. A fraction with a nonzero top and a zero bottom is not defined. Also, the original function $f$ is not defined at $x=1$, so it has no graph point there and no tangent line there. The derivative can exist only where the function exists.

**Step 7. Sign of the derivative.** The bottom $(x-1)^2$ is positive for every $x\ne1$. So the sign of $f'$ is the sign of $x^2-2x-1$. This quadratic has roots $x=1\pm\sqrt2$, about $-0.414$ and $2.414$. It is positive outside these roots and negative between them. So $f$ rises for $x<1-\sqrt2$ and for $x>1+\sqrt2$, and falls on the two pieces between them, except that $x=1$ is excluded.

## Why each step is valid

- Step 1 is valid because division by zero has no meaning.
- Step 3 is valid because the quotient rule holds wherever $v(x)\ne0$, and we are working on the domain.
- Step 4 is valid by ordinary expansion; the minus sign applies to the whole bracket $x^2+1$.
- Step 5 is valid because a factor cancels only if it appears in both the top and the bottom, and a number that makes the top nonzero cannot be a root.
- Step 6 is valid because a derivative is the slope of a tangent line, and a point that is not on the graph has no tangent line.

## Final answer (in words)

The domain is every real number except $1$. The derivative is $f'(x)=\dfrac{x^2-2x-1}{(x-1)^2}$ for $x\ne1$. The restriction stays because the function is undefined at $1$, the denominator of $f'$ is also zero there, and the numerator does not cancel it.

## Verification

**Check 1: a different method.** Divide the top by the bottom first: $\dfrac{x^2+1}{x-1}=x+1+\dfrac{2}{x-1}$. Check by multiplying: $(x+1)(x-1)+2=x^2-1+2=x^2+1$. Now differentiate with the power rule: $\frac{d}{dx}\bigl(x+1+2(x-1)^{-1}\bigr)=1-\dfrac{2}{(x-1)^2}$. Put this over a common denominator: $\dfrac{(x-1)^2-2}{(x-1)^2}=\dfrac{x^2-2x-1}{(x-1)^2}$. This is the same result, found without the quotient rule.

**Check 2: difference quotients at $x=2$.** Here $f(2)=5$ and the formula gives $f'(2)=\dfrac{4-4-1}{1}=-1$. The quotients $\dfrac{f(2+h)-f(2)}{h}$ for $h=0.1,\ 0.01,\ 0.001$ are about $-0.8182$, $-0.9802$, $-0.9980$. They approach $-1$.

## Common mistakes

- Reversing the order in the numerator and getting $u\,v'-u'v$. The sign of the whole answer flips.
- Forgetting to subtract the whole product $(x^2+1)\cdot1$, and subtracting only $x^2$.
- Writing the denominator as $x-1$ instead of $(x-1)^2$.
- Dropping the restriction $x\ne1$ because the final formula looks simple.
- Claiming that $(x-1)$ cancels with the numerator. It does not, because the numerator is $-2$ at $x=1$.

## How I would explain it in class

The function is one expression divided by another, so first I note that the bottom $x-1$ must not be zero, which excludes $x=1$. The quotient rule gives bottom times derivative of top, minus top times derivative of bottom, over bottom squared, and this simplifies to $\dfrac{x^2-2x-1}{(x-1)^2}$. The number $1$ stays forbidden because the function has no point there, so it cannot have a tangent, and the simplified formula still has a zero denominator.
