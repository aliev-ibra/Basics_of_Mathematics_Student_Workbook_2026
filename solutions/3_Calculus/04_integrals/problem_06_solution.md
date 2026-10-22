# Problem 6

## The original problem

Compute
$$\int\frac{2x}{x^2+5}\,dx.$$
Identify the denominator as a candidate for substitution, compare the numerator with its derivative, and explain the source of the logarithm in the result.

> **Why this problem:** it teaches how to recognize the structure "derivative of the denominator over the denominator."

## What we are looking for

We are asked for an antiderivative of a fraction. The fraction is not to be split into two pieces, and the answer will not be a power function; instead a logarithm appears. We must show why: the denominator is the natural candidate for the new variable, the numerator turns out to be its derivative, and after the substitution we meet the one power that the power rule cannot handle. That is exactly where the logarithm comes from.

## The idea we need

**The structural test.** An integrand of the form
$$\frac{g'(x)}{g(x)}$$
is integrated by substituting $u=g(x)$, which turns it into $\int\frac{du}{u}$. The denominator is the candidate for $u$, and the numerator must be (a constant multiple of) the derivative of the denominator.

**The one case the power rule cannot do.** For $n\neq -1$,
$$\int u^n\,du=\frac{u^{n+1}}{n+1}+C.$$
For $n=-1$ the denominator $n+1$ would be zero, so the power rule fails. This single case is replaced by the logarithm:
$$\int\frac{du}{u}=\ln|u|+C,$$
which holds because the derivative of $\ln|u|$ with respect to $u$ is $\frac1u$. So the logarithm is exactly the antiderivative of the reciprocal function, and it enters our problem because the substitution produces a reciprocal.

**Why the absolute value.** The rule is written $\ln|u|$ because $\frac{du}{u}$ is defined for negative $u$ as well, and $\ln u$ is not real for negative $u$. If we know that $u>0$ on the whole interval, then $|u|=u$ and the absolute value may be dropped.

## Step-by-step solution

**Step 1. Identify the denominator as the candidate for substitution.**

The denominator is $x^2+5$. Write $u=x^2+5$ and ask whether its derivative appears in the numerator.

**Step 2. Compare the numerator with that derivative.**

$$
\frac{d}{dx}(x^2+5)=2x.$$
The numerator of the integrand is exactly $2x$. So the numerator is the derivative of the denominator, with no missing constant factor. This is the structure "derivative of the denominator over the denominator", and substitution applies.

**Step 3. Introduce the new variable.**

$$
u=x^2+5,\qquad du=2x\,dx.$$

**Step 4. Rewrite the integral in the new variable.**

$$
\int\frac{2x}{x^2+5}\,dx=\int\frac{du}{u}.$$

**Step 5. Explain where the logarithm comes from.**

The transformed integral is a power integral with exponent $n=-1$, precisely the case the power rule excludes, because $n+1=0$ would divide by zero. The antiderivative of the reciprocal function $\frac1u$ is the logarithm:
$$\int\frac{du}{u}=\ln|u|+C.$$
So the logarithm is not an arbitrary trick: it is forced by the shape of the integral after the substitution.

**Step 6. Insert the absolute value and then check the sign of $u$.**

The rule gives $\ln|x^2+5|+C$. But $x^2+5\ge 5>0$ for every real $x$, so $|x^2+5|=x^2+5$ and the absolute value can be removed.

**Step 7. State the answer.**

$$
\int\frac{2x}{x^2+5}\,dx=\ln(x^2+5)+C.
$$

**Step 8. Note the role of the constant.**

Any constant may be added, because its derivative is zero. The integrand alone does not determine $C$.

## Why each step is valid

- Step 1 is valid because the denominator is the part of the integrand that is a function of one inner expression; the denominator is always the first candidate to test for this pattern.
- Step 2 is valid because the numerator $2x$ coincides with the derivative of $x^2+5$, which is the exact requirement for the pattern.
- Step 3 is valid by the differential rule $du=u'(x)\,dx$.
- Step 4 is valid because we replaced $x^2+5$ by $u$ and $2x\,dx$ by $du$ simultaneously, using equalities, so the integral keeps its value.
- Step 5 is valid because $\dfrac{d}{du}\ln|u|=\frac1u$ for $u\neq 0$, and the power rule genuinely does not apply at exponent $-1$.
- Step 6 is valid because $x^2\ge 0$ for all real $x$, hence $x^2+5$ is always positive and equals its absolute value.
- Step 8 is valid because the derivative of a constant is zero everywhere.

## Final answer (in words)

The antiderivative of $\frac{2x}{x^2+5}$ is the natural logarithm of $x^2+5$, plus an arbitrary constant $C$. In words: the numerator $2x$ is the derivative of the denominator $x^2+5$, so after the substitution the integral becomes the integral of $1$ divided by $u$, and the antiderivative of the reciprocal function is the logarithm.

## Verification

**Check 1 (the required one): differentiate the answer.** Let $F(x)=\ln(x^2+5)$. Since $x^2+5>0$, we may use the chain rule directly:
$$F'(x)=\frac{1}{x^2+5}\cdot\frac{d}{dx}(x^2+5)=\frac{1}{x^2+5}\cdot 2x=\frac{2x}{x^2+5}.$$
This is exactly the original integrand.

**Check 2: a numerical check of a definite integral.** By the Fundamental Theorem of Calculus,
$$\int_0^1\frac{2x}{x^2+5}\,dx=\ln 6-\ln 5=\ln\frac65\approx 0.182322.$$
Now estimate the same integral numerically. The integrand is increasing on $[0,1]$, so the left-endpoint sum is a lower bound and the right-endpoint sum is an upper bound. With four subintervals of width $0.25$ the function values are
$$f(0)=0,\quad f(0.25)\approx 0.098765,\quad f(0.5)\approx 0.190476,\quad f(0.75)\approx 0.269663,\quad f(1)\approx 0.333333.$$
The lower sum is $0.25(0+0.098765+0.190476+0.269663)\approx 0.139726$ and the upper sum is $0.25(0.098765+0.190476+0.269663+0.333333)\approx 0.223059$. The exact value $0.182322$ lies between them, as it must. Simpson's rule gives $\frac{0.25}{3}(0+4\cdot 0.098765+2\cdot 0.190476+4\cdot 0.269663+0.333333)\approx 0.182333$, which matches the exact value to five decimal places.

**Check 3: a structural sanity check.** If the numerator had been, say, $2x+3$, the substitution would leave the extra constant $3$ behind and produce $\ln(x^2+5)+\frac{3}{\sqrt5}\arctan\left(\frac{x}{\sqrt5}\right)$, not a single logarithm. The fact that our answer is a single logarithm confirms that the numerator really matched the derivative of the denominator, with nothing left over.

## Common mistakes

- **Leaving a factor $2$ in the answer.** Writing $2\ln(x^2+5)$ double-counts: the $2$ is already the derivative of the denominator and is consumed by the substitution.
- **Writing the answer without the logarithm.** For example $\frac{d}{dx}\ln(x^2+5)$ is right, but the answer must be a logarithm of the denominator, not a power of it.
- **Dropping the absolute value without thinking.** Here it is safe because $x^2+5$ is always positive, but for a denominator such as $x^2-5$ the rule $\ln|x^2-5|$ is the correct one and the absolute value cannot be dropped.
- **Splitting the fraction into two separate integrals.** The fraction $\frac{2x}{x^2+5}$ is a single quotient, not a sum; splitting it would destroy the pattern that makes the substitution work.
- **Forgetting the constant $C$.** The indefinite integral is the family $\ln(x^2+5)+C$.

## How I would explain it in class

I start from the denominator $x^2+5$, because it is the part of the integrand that is a function of one inner expression, and I check whether its derivative appears in the numerator: indeed $\frac{d}{dx}(x^2+5)=2x$, so the numerator is exactly the derivative of the denominator. With $u=x^2+5$ and $du=2x\,dx$ the integral becomes $\int\frac{du}{u}$, and this is the single case where the power rule fails, so the antiderivative must be the logarithm. Since $x^2+5$ is always positive I can drop the absolute value and write $\ln(x^2+5)+C$, which differentiates back to $\frac{2x}{x^2+5}$.
