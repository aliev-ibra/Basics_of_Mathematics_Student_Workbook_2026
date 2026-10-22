# Problem 5

## The original problem

For
$$f(x)=(3x^2-2x+1)^5$$
identify the inner and outer functions, compute their derivatives, and combine the result according to the chain rule. Explain the origin of the additional factor.

> **Why this problem:** it teaches how to recognize the structure of a composition instead of memorizing the rule as a meaningless pattern.

## What we are looking for

We need to split the function into two layers, an inner function and an outer function. We differentiate each layer, combine the results by the chain rule, and explain where the extra factor in the answer comes from.

## The idea we need

The **chain rule**. A composition is a function put inside another function. If $f(x)=F(g(x))$, then
$$f'(x)=F'(g(x))\cdot g'(x).$$
In words: differentiate the outer function and leave the inner one untouched inside it, then multiply by the derivative of the inner function. We recognise a composition when we see a bracket (or root, or sine, and so on) that contains an expression of $x$ rather than just $x$ itself. Here the bracket $3x^2-2x+1$ is raised to the power $5$. The **power rule** is used for each layer: $\frac{d}{dx}t^n=n\,t^{n-1}$.

## Step-by-step solution

**Step 1. Identify the layers.** The inner function is $g(x)=3x^2-2x+1$. The outer function is $F(t)=t^5$, where $t$ stands for whatever is inside the bracket. Then $f(x)=F(g(x))$.

**Step 2. Differentiate the outer function.** By the power rule, $F'(t)=5t^4$. Put the inner function back in place of $t$: $F'(g(x))=5(3x^2-2x+1)^4$.

**Step 3. Differentiate the inner function.** By the power rule term by term, $g'(x)=6x-2$. (The term $3x^2$ gives $6x$, the term $-2x$ gives $-2$, and the constant $1$ gives $0$.)

**Step 4. Multiply.**
$$f'(x)=5(3x^2-2x+1)^4\,(6x-2).$$

**Step 5. Simplify.** Since $6x-2=2(3x-1)$,
$$f'(x)=10\,(3x-1)\,(3x^2-2x+1)^4.$$

**Step 6. The origin of the extra factor.** The factor $(6x-2)$ is the derivative of the inner function. It appears because the bracket itself changes when $x$ changes. If $x$ grows by a small amount, the bracket grows by about $(6x-2)$ times that amount. The outer power then reacts to the change of the bracket. The total rate is the rate of the outer layer times the rate of the inner layer.

**Step 7. A value.** At $x=1$ the bracket equals $3-2+1=2$, so $f(1)=2^5=32$. The derivative is $f'(1)=10\cdot2\cdot2^4=320$. This is positive, so the tangent line at $x=1$ rises steeply.

**Step 8. Where the tangent is horizontal.** The bracket $3x^2-2x+1$ is always positive, because its discriminant $(-2)^2-4\cdot3\cdot1=-8$ is negative and the leading coefficient is positive. So $(3x^2-2x+1)^4$ is never zero, and $f'(x)=0$ only when $3x-1=0$, that is at $x=\frac13$.

## Why each step is valid

- Steps 1 to 4 are valid because the chain rule holds whenever the outer function is differentiable at the inner value and the inner function is differentiable at $x$. Both are polynomials or powers, so this is true everywhere.
- In Step 2 we must keep the inner expression inside the bracket, because the chain rule evaluates $F'$ at $g(x)$, not at $x$.
- Step 5 is valid because factoring $2$ out of $6x-2$ is plain algebra.
- Step 8 is valid because a product is zero only if one of its factors is zero, and the fourth power factor is never zero.

## Final answer (in words)

The inner function is $3x^2-2x+1$ and the outer function is "raise to the fifth power". The derivative is $f'(x)=5(3x^2-2x+1)^4(6x-2)=10(3x-1)(3x^2-2x+1)^4$. The extra factor $6x-2$ is the derivative of the inner function. It appears because the inside of the bracket changes as $x$ changes.

## Verification

**Check 1: difference quotients at $x=1$.** We have $f(1)=32$ and the formula says $f'(1)=320$. The quotient $\dfrac{f(1+h)-f(1)}{h}$ equals about $527.29$ for $h=0.1$, about $335.66$ for $h=0.01$, and about $321.52$ for $h=0.001$. The values approach $320$.

**Check 2: the symmetric quotient.** With $h=10^{-5}$ the quotient $\dfrac{f(1+h)-f(1-h)}{2h}$ equals $320.0000004$, which agrees with $320$.

**Check 3: a different reading of the formula.** The wrong answer without the extra factor would be $5\cdot2^4=80$ at $x=1$. The numerical values above are clearly near $320$, not $80$. The ratio is $320/80=4$, which is exactly the inner derivative $6\cdot1-2=4$.

## Common mistakes

- Writing $5(3x^2-2x+1)^4$ and forgetting the factor $6x-2$.
- Differentiating the inside first and lowering the power inside, for example $(6x-2)^4$.
- Changing the inside while taking the outer derivative, for example $5(6x-2)^4$.
- Writing the exponent as $5$ again, so $5(\dots)^5$. The power drops by one to $4$.
- Making a slip on the middle term of the inner function: the derivative of $-2x$ is $-2$, not $-2x$.

## How I would explain it in class

I see a bracket raised to a power, so this is a composition: the inside is $3x^2-2x+1$ and the outside is the fifth power. I differentiate the outside, which gives $5$ times the bracket to the fourth power, and then I multiply by the derivative of the inside, $6x-2$, because the inside itself changes with $x$. The result is $5(3x^2-2x+1)^4(6x-2)$, and at $x=1$ it equals $320$, which matches the numerical check.
