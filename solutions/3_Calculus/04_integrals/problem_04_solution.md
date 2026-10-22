# Problem 4

## The original problem

Compute
$$\int 2x(x^2+1)^4\,dx.$$
Before calculating, identify a candidate for the new variable $u$ and show that its derivative appears in the integral. Finally, verify the result by differentiation.

> **Why this problem:** it teaches how to recognize substitution as reversing the chain rule.

## What we are looking for

We are asked for an antiderivative of a product in which a complicated power of a polynomial is multiplied by a factor that looks exactly like the derivative of that polynomial. The point of the problem is not the arithmetic but the recognition: before computing, we must find the right candidate for the new variable and show why it works. Then we replace that candidate by a letter, integrate something easy, and substitute back.

## The idea we need

**Substitution as the chain rule run backwards.** The chain rule says
$$\frac{d}{dx}F(g(x))=F'(g(x))\cdot g'(x).$$
Integration wants the opposite: we are given a product of a function of $g(x)$ and the factor $g'(x)$, and we want to recover $F$. The rule of the substitution method is:

> If an integrand contains a function of an inner expression together with the derivative of that inner expression, replace the inner expression by a new variable $u$ and integrate.

**The conditions for using it.** The pattern must appear as a *product*. We need one factor to be a function of some inner expression $u=u(x)$, and the other factor to be a constant multiple of $du=u'(x)\,dx$. If no factor looks like the derivative of the other part's inner expression, substitution will not help.

**The power rule, applied after the substitution.** Once $u$ is in place, the integral usually becomes a plain power integral $\int u^n\,du=\frac{u^{n+1}}{n+1}+C$, which is the easy part.

**Back-substitution.** The result must be written in the original variable $x$, and the constant $C$ must be restored at the end.

## Step-by-step solution

**Step 1. Look for an inner expression and its derivative.**

The integrand is $2x\,(x^2+1)^4$. The part in parentheses, $x^2+1$, is the natural inner expression: the integrand is a function of $x^2+1$ multiplied by something else. We therefore check whether the derivative of $x^2+1$ shows up.

The derivative of the inner expression is
$$\frac{d}{dx}(x^2+1)=2x.$$
And indeed the integrand is $2x\cdot(x^2+1)^4$, so the factor $2x$ is exactly the derivative of the inner expression $x^2+1$. This is the pattern the substitution method needs, so substitution is the right method here.

**Step 2. Introduce the new variable.**

We set
$$u=x^2+1,\qquad du=2x\,dx.$$
The equality $du=2x\,dx$ is the crucial piece of bookkeeping: it converts the leftover factor $2x\,dx$ in the integral into the differential $du$.

**Step 3. Rewrite the integral in the new variable.**

$$
\int 2x(x^2+1)^4\,dx=\int u^4\,du.
$$

**Step 4. Integrate with the power rule.**

Here the power is $4$, and $4\neq -1$, so the power rule applies:
$$\int u^4\,du=\frac{u^{5}}{5}+C.$$

**Step 5. Substitute back to $x$.**

We replace $u$ by the expression it stood for, $x^2+1$:
$$\int 2x(x^2+1)^4\,dx=\frac{(x^2+1)^5}{5}+C.$$

**Step 6. State the answer.**

One antiderivative is $F(x)=\dfrac{(x^2+1)^5}{5}$; the whole family is obtained by adding an arbitrary constant $C$.

## Why each step is valid

- Step 1 is valid because the chain rule tells us that a derivative of the form $\dfrac{d}{dx}F(x^2+1)=F'(x^2+1)\cdot 2x$ contains exactly the factor $2x$ we see in the integrand.
- Step 2 is valid because $u=x^2+1$ gives $du=2x\,dx$ by the differential rule $du=u'(x)\,dx$, and this turns the factor $2x\,dx$ into $du$ exactly, with nothing lost.
- Step 3 is valid because we only renamed the inner expression and used the equality $du=2x\,dx$, which leaves the value of the integral unchanged.
- Step 4 is valid because the power rule $\int u^n\,du=\frac{u^{n+1}}{n+1}+C$ holds for $n\neq -1$, and here $n=4$.
- Step 5 is valid because back-substitution restores the original variable; a result written in $u$ alone would not be an answer to the original question.
- Step 6 is valid because the derivative of the constant $C$ is zero, so it may be added freely.

## Final answer (in words)

The antiderivative of $2x(x^2+1)^4$ is the fifth power of $x^2+1$, divided by five, plus an arbitrary constant $C$. In words: because the factor $2x$ is the derivative of the inner expression $x^2+1$, the whole integrand becomes the plain power integral $\int u^4\,du$ once we rename $x^2+1$ as $u$.

## Verification

**Check 1 (the required one): differentiate the answer.** Let $F(x)=\dfrac{(x^2+1)^5}{5}$. Using the chain rule,
$$F'(x)=\frac{1}{5}\cdot 5(x^2+1)^4\cdot\frac{d}{dx}(x^2+1)=\frac{1}{5}\cdot 5(x^2+1)^4\cdot 2x=2x(x^2+1)^4.$$
This is exactly the original integrand, so $F$ is an antiderivative.

**Check 2: a completely different method on a definite integral.** Expand the fourth power by the binomial formula:
$$(x^2+1)^4=x^8+4x^6+6x^4+4x^2+1.$$
Then the integrand becomes $2x^9+8x^7+12x^5+8x^3+2x$, and the power rule alone gives
$$\int_0^1 2x(x^2+1)^4\,dx=\left[\frac{x^{10}}{5}+x^8+2x^6+2x^4+x^2\right]_0^1=\frac15+1+2+2+1=\frac{31}{5}=6.2.$$
Our formula gives the same number: $\left[\dfrac{(x^2+1)^5}{5}\right]_0^1=\dfrac{2^5-1^5}{5}=\dfrac{31}{5}=6.2$. Two independent methods agree exactly.

**Check 3: numerical comparison.** Simpson's rule with four subintervals on $[0,1]$ gives about $6.27$, which is the correct size for a function that rises from $2$ to $32$ over that interval and matches the exact value $6.2$ to within the expected error of the rule.

## Common mistakes

- **Forgetting that $du=2x\,dx$.** If you set $u=x^2+1$ and then integrate $\int u^4\cdot 2x\,du$, you have changed the problem. The whole point is that the leftover factor $2x$ is exactly $du$.
- **Choosing the wrong candidate, for example $u=x$.** With $u=x$ the integral becomes $\int 2x(x^2+1)^4\,dx$ again, and nothing is simplified. A good candidate is an inner expression whose derivative appears as a factor.
- **Forgetting the factor $\frac{1}{5}$.** $\int u^4\,du=\frac{u^5}{5}$, not $u^5$.
- **Leaving the answer in $u$.** The final formula must contain only $x$.
- **Dropping the constant of integration $C$.** The indefinite integral is the family of all antiderivatives.

## How I would explain it in class

I look at the integrand $2x(x^2+1)^4$ and notice that the inner expression $x^2+1$ has derivative $2x$, which sits in the integrand as a separate factor, so this is exactly the situation where substitution works. Setting $u=x^2+1$ and $du=2x\,dx$ turns the integral into the easy $\int u^4\,du$, which is $\frac{u^5}{5}+C$. Substituting back gives $\frac{(x^2+1)^5}{5}+C$, and differentiating it returns $2x(x^2+1)^4$.
