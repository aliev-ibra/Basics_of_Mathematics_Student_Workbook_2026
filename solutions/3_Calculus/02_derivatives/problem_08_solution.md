# Problem 8

## The original problem

For
$$f(x)=e^{2x-3}+5^x$$
compute the derivative. Explain why the factor $2$ appears in the first term and why $\ln5$ appears in the second.

> **Why this problem:** it organizes two different mechanisms that produce additional factors.

## What we are looking for

We need $f'(x)$. For each of the two terms we must explain where the extra factor comes from. In the first term the extra factor is $2$. In the second term it is the number $\ln5$, the natural logarithm of $5$.

## The idea we need

We use the **sum rule** and two exponential derivative facts.

1. The derivative of $e^x$ is $e^x$. For a composition $e^{g(x)}$ we use the **chain rule**: $\frac{d}{dx}e^{g(x)}=e^{g(x)}\cdot g'(x)$. We recognise it because the exponent is an expression of $x$ and not just $x$.
2. For a constant base $a>0$, $\frac{d}{dx}a^x=a^x\ln a$. We recognise it because the base is a fixed number and the variable is in the exponent. This is not the power rule, because the power rule is for a variable base and a fixed exponent.

The second fact comes from the identity $a^x=e^{x\ln a}$, which says that every exponential is $e$ to a multiple of $x$. Here $\ln a$ is the number such that $e^{\ln a}=a$.

## Step-by-step solution

**Step 1. First term.** $e^{2x-3}$ is $e$ raised to an inner expression $g(x)=2x-3$. The outer function is $e^t$, which is its own derivative. The inner derivative is $g'(x)=2$. By the chain rule,
$$\frac{d}{dx}e^{2x-3}=e^{2x-3}\cdot2=2e^{2x-3}.$$

**Step 2. Second term.** Write $5^x=e^{x\ln5}$. Now it is $e$ raised to the inner expression $x\ln5$. Because $\ln5$ is just a fixed number, the inner derivative is $\ln5$. By the chain rule,
$$\frac{d}{dx}5^x=e^{x\ln5}\cdot\ln5=5^x\ln5.$$

**Step 3. Add by the sum rule.**
$$f'(x)=2e^{2x-3}+5^x\ln5.$$

**Step 4. Why the factor $2$.** The exponent $2x-3$ grows twice as fast as $x$. When $x$ increases by a small amount, the exponent increases by twice that amount. So the whole term $e^{2x-3}$ changes twice as fast as $e^{t}$ would change at the same $t$. The constant $-3$ only shifts the exponent and does not change its speed, so it does not appear in the factor.

**Step 5. Why the factor $\ln5$.** The base $5$ is not $e$. Converting $5$ into the base $e$ costs the factor $\ln5$, since $5=e^{\ln5}$. The exponent of $e$ then grows by $\ln5$ for each unit of $x$. Numerically $\ln5\approx1.6094$. This is bigger than $1$ because $5>e\approx2.718$, so $5^x$ grows faster than $e^x$.

**Step 6. Domain and sign.** The function is defined for all real $x$. Both terms of $f'$ are positive, since $e^{\dots}>0$, $5^x>0$ and $\ln5>0$. So $f'(x)>0$ everywhere, and $f$ is increasing on the whole line.

**Step 7. A value.** $f'(0)=2e^{-3}+\ln5\approx0.0996+1.6094=1.7090$.

## Why each step is valid

- Step 1 is valid by the chain rule: outer function $e^t$, inner function $2x-3$.
- Step 2 is valid because $5=e^{\ln5}$, so $5^x=(e^{\ln5})^x=e^{x\ln5}$ by the rule for powers of powers.
- Step 3 is valid by the sum rule.
- The derivative of the inner function $x\ln5$ is $\ln5$ because $\ln5$ is a constant that stays in front, like the number $7$ would in $7x$.
- Step 6 is valid because exponentials are always positive and $\ln5>\ln1=0$.

## Final answer (in words)

The derivative is $f'(x)=2e^{2x-3}+5^x\ln5$. The factor $2$ is the derivative of the exponent $2x-3$, which is the chain rule factor. The factor $\ln5$ appears because $5^x=e^{x\ln5}$, and the derivative of the exponent $x\ln5$ is $\ln5$. The derivative is positive for every $x$.

## Verification

**Check 1: difference quotients at $x=0$.** Here $f(0)=e^{-3}+1\approx1.04979$ and $f'(0)\approx1.70901$. The quotient $\dfrac{f(h)-f(0)}{h}$ equals about $1.8564$ for $h=0.1$, about $1.7230$ for $h=0.01$, and about $1.7104$ for $h=0.001$. The values approach $1.7090$.

**Check 2: another point, $x=1.5$.** The formula gives $f'(1.5)=2e^{0}+5^{1.5}\ln5=2+11.1803\cdot1.6094\approx19.9941$. The quotients for $h=0.1,\ 0.01,\ 0.001$ are about $21.737$, $20.160$, $20.011$. They approach $19.994$. The symmetric quotient with $h=10^{-5}$ gives $19.99406289$.

**Check 3: each factor separately.** Without the factor $2$, the first term at $x=0$ would be $e^{-3}\approx0.0498$ instead of $0.0996$. Without $\ln5$, the second term would be $1$ instead of $1.6094$. The sum of these wrong values, $1.0498$, is far from the numerical values near $1.709$.

## Common mistakes

- Writing $e^{2x-3}$ as the derivative of the first term, without the factor $2$.
- Writing $x\,5^{x-1}$, which uses the power rule. The power rule is for a variable base, and here the variable is in the exponent.
- Writing $\frac{d}{dx}5^x=5^x$, which is true only for the base $e$.
- Writing $\frac{1}{\ln5}$ instead of $\ln5$.
- Including the $-3$ in the factor, for example $2e^{2x-3}\cdot(-3)$.

## How I would explain it in class

The first term is $e$ to an inner expression $2x-3$, so I use the chain rule: the exponential stays the same and I multiply by the derivative of the exponent, which is $2$. The second term has a fixed base $5$ and the variable in the exponent, so I write $5^x=e^{x\ln5}$ and the chain rule gives the factor $\ln5$. The result is $2e^{2x-3}+5^x\ln5$, which is positive for every $x$.
