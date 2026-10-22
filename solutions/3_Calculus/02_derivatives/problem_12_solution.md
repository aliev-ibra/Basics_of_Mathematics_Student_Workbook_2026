# Problem 12

## The original problem

For
$$f(x)=(x^2+1)^3e^x$$
compute the derivative. Before calculating, write down a plan: which rule applies to the whole expression and which rule applies to one of its factors. Finally, organize the result by factoring out common factors.

> **Why this problem:** it practices the order of decisions when combining familiar differentiation rules.

## What we are looking for

We need the derivative $f'(x)$, and we need to show how we decided which rules to use and in which order. The function looks complicated, but it is built from simple pieces. The task is to see the structure first and calculate second. At the end the answer must be written in a short factored form.

## The idea we need

**The plan, written before any calculation.**

1. Look at the whole expression. It is two factors multiplied: $(x^2+1)^3$ times $e^x$. A product means the **product rule** applies to the whole expression.
2. The product rule says: if $f=u\cdot v$, then $f'=u'v+uv'$. In words: derivative of the first times the second, plus the first times the derivative of the second.
3. Now look at each factor. The factor $v=e^x$ is simple. Its derivative is $e^x$.
4. The factor $u=(x^2+1)^3$ is a power of an expression, so it has two layers: the inside $x^2+1$ and the outside "cube". A function inside a function means the **chain rule** applies to this factor. The chain rule says to differentiate the outside, keep the inside, and multiply by the derivative of the inside.
5. At the end, both terms contain the common factors $(x^2+1)^2$ and $e^x$, so we factor them out.

We recognise the product rule by the multiplication sign between two functions of $x$. We recognise the chain rule by a bracket raised to a power.

## Step-by-step solution

1. Name the factors: $u(x)=(x^2+1)^3$ and $v(x)=e^x$. Then $f=u\cdot v$.
2. Differentiate $v$: $v'(x)=e^x$.
3. Differentiate $u$ with the chain rule. The outside is $w^3$ with $w=x^2+1$. Its derivative is $3w^2=3(x^2+1)^2$. The derivative of the inside $x^2+1$ is $2x$. Multiply:
$$u'(x)=3(x^2+1)^2\cdot 2x=6x(x^2+1)^2.$$
4. Apply the product rule:
$$f'(x)=u'v+uv'=6x(x^2+1)^2e^x+(x^2+1)^3e^x.$$
5. Find the common factor. Both terms contain $(x^2+1)^2$ and $e^x$. The first term has nothing else except $6x$. The second term has one more factor $(x^2+1)$. Factor out:
$$f'(x)=(x^2+1)^2e^x\big[6x+(x^2+1)\big].$$
6. Simplify the bracket: $6x+x^2+1=x^2+6x+1$. So
$$f'(x)=(x^2+1)^2\,e^x\,(x^2+6x+1).$$

## Why each step is valid

- Step 3 is valid because $u$ is a composition: first we compute $x^2+1$, then we cube it. The chain rule is the correct rule for a composition.
- Step 4 is valid because $f$ is a product of two differentiable functions, and the product rule gives the derivative of such a product. We cannot just multiply $u'$ and $v'$.
- Step 5 is valid because factoring out a common factor is the reverse of the distributive law. Nothing is lost.
- The factor $e^x$ is never zero and $(x^2+1)^2$ is never zero, so the sign of $f'$ is decided by $x^2+6x+1$ alone. This is a useful reason for factoring.

## Final answer (in words)

The derivative is
$$f'(x)=(x^2+1)^2\,e^x\,(x^2+6x+1).$$
We got it by the product rule for the whole expression, and the chain rule for the factor $(x^2+1)^3$. The result is the product of $(x^2+1)^2$, $e^x$, and the quadratic $x^2+6x+1$.

## Verification

**Check 1: a different method.** Take the natural logarithm: $\ln f=3\ln(x^2+1)+x$. Differentiate both sides: $\frac{f'}{f}=\frac{6x}{x^2+1}+1$. Multiply by $f=(x^2+1)^3e^x$:
$$f'=(x^2+1)^3e^x\cdot\frac{6x}{x^2+1}+(x^2+1)^3e^x=6x(x^2+1)^2e^x+(x^2+1)^3e^x.$$
This is the same as Step 4. This method did not use the product rule.

**Check 2: a number at $x=0$.** Our formula gives $f'(0)=1\cdot1\cdot1=1$. The difference quotient with $h=0.001$ is $\frac{(1.000001)^3e^{0.001}-1}{0.001}\approx1.001$, which is near $1$.

**Check 3: a number at $x=1$.** The formula gives $f'(1)=2^2\cdot e\cdot(1+6+1)=32e\approx86.985$. A central difference quotient with $h=0.0001$ gives about $86.985$, the same to five digits.

## Common mistakes

- Writing $f'=u'v'$, which is multiplying the derivatives. This is not the product rule.
- Forgetting the factor $2x$ from the inside layer when differentiating $(x^2+1)^3$. The result $3(x^2+1)^2$ alone is incomplete.
- Differentiating $e^x$ and getting $xe^{x-1}$. That is the power rule, and it applies only when the variable is in the base, not in the exponent.
- Factoring wrongly, for example forgetting that the second term has an extra factor $(x^2+1)$, which gives the $+1$ in $x^2+6x+1$.

## How I would explain it in class

Before computing, I note that the expression is a product, so the product rule applies to the whole thing, and that the first factor is a bracket to a power, so the chain rule applies inside it. The chain rule gives $6x(x^2+1)^2$ for the first factor, the exponential stays $e^x$, and the product rule adds two terms. Then I factor out $(x^2+1)^2e^x$ and the answer is $(x^2+1)^2e^x(x^2+6x+1)$.
