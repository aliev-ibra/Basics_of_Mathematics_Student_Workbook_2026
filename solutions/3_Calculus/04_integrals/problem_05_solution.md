# Problem 5

## The original problem

Compute
$$\int xe^{x^2}\,dx.$$
First compare the structure with Problem 4 and explain what is common despite the different appearance of the function.

> **Why this problem:** it shows that the substitution mechanism is recognized by structure, not by the type of function.

## What we are looking for

We are asked for an antiderivative of $x$ times an exponential of $x^2$. Before computing anything we must compare the shape of this integrand with the shape of the one in Problem 4, because the two problems are the same mechanism in different clothes. Then we apply the same substitution, do the easy integral that results, and substitute back.

## The idea we need

**The structural test for substitution.** Do not ask "what kind of function is this?" Ask instead: "is there an inner expression whose derivative appears as a factor next to a function of that inner expression?" If the answer is yes, substitute.

**What is common to Problems 4 and 5.** In Problem 4 the integrand was $2x\,(x^2+1)^4$; here it is $x\,e^{x^2}$. In both cases the integrand has the shape
$$\bigl[\text{something that depends only on }u\bigr]\cdot\bigl[\text{constant multiple of }u'(x)\bigr],$$
where $u$ is an inner expression. In Problem 4, $u=x^2+1$ and the factor is $u'=2x$. Here $u=x^2$ and the factor is $x=\frac12 u'$. The outer functions differ completely (a power versus an exponential), but the mechanism of the substitution is identical.

**Substitution rules.** Set $u=u(x)$ and $du=u'(x)\,dx$, rewrite the whole integral in $u$, integrate, and then substitute back to $x$.

**The basic exponential antiderivative.** $\int e^u\,du=e^u+C$, because $\dfrac{d}{du}e^u=e^u$.

## Step-by-step solution

**Step 1. Compare the structure with Problem 4.**

Problem 4: $\int 2x(x^2+1)^4\,dx$ — the integrand is a function of the inner expression $x^2+1$, multiplied by its derivative $2x$.

Here: $\int xe^{x^2}\,dx$ — the integrand is a function of the inner expression $x^2$, multiplied by the number $x$. The derivative of $x^2$ is $2x$, so $x$ is one half of that derivative. A nonzero constant multiple of the derivative is just as good: the factor $\frac12$ will simply come out of the integral.

**Step 2. Introduce the new variable.**

$$
u=x^2,\qquad du=2x\,dx.$$
From this we also get
$$x\,dx=\frac{1}{2}\,du,$$
because dividing the equation $du=2x\,dx$ by $2$ gives exactly this. The factor $\frac12$ is the price we pay for the fact that the integrand contains $x$ rather than $2x$.

**Step 3. Rewrite the integral in the new variable.**

$$
\int xe^{x^2}\,dx=\int e^{u}\cdot\frac{1}{2}\,du=\frac{1}{2}\int e^{u}\,du.
$$

**Step 4. Integrate.**

The antiderivative of $e^u$ is $e^u$ itself, so
$$\frac{1}{2}\int e^{u}\,du=\frac{1}{2}e^u+C.$$

**Step 5. Substitute back to $x$.**

Since $u=x^2$, we get
$$\int xe^{x^2}\,dx=\frac{1}{2}e^{x^2}+C.$$

**Step 6. State the answer.**

One antiderivative is $F(x)=\dfrac{1}{2}e^{x^2}$, and the whole family is $\dfrac{1}{2}e^{x^2}+C$.

## Why each step is valid

- Step 1 is valid because the chain rule $\dfrac{d}{dx}F(u(x))=F'(u(x))\cdot u'(x)$ produces exactly a product of a function of $u$ with the factor $u'(x)$, and any nonzero constant multiple of $u'(x)$ can be moved out of the integral as a constant.
- Step 2 is valid because $du=2x\,dx$ follows from differentiating $u=x^2$, and dividing by $2$ preserves the equality.
- Step 3 is valid because we only renamed the inner expression and used the equality $x\,dx=\frac12\,du$ from Step 2; the value of the integral is unchanged.
- Step 4 is valid because $\dfrac{d}{du}e^u=e^u$, and constants may be pulled out of an integral.
- Step 5 is valid because back-substitution restores the original variable $x$.
- Step 6 is valid because the derivative of a constant is zero.

## Final answer (in words)

The antiderivative of $xe^{x^2}$ is one half of the exponential of $x^2$, plus an arbitrary constant $C$. In words: the mechanism is exactly the one of Problem 4, because the integrand is a function of the inner expression $x^2$ multiplied by the derivative of that inner expression (up to the factor $\frac12$).

## Verification

**Check 1 (the required one): differentiate the answer.** Let $F(x)=\frac{1}{2}e^{x^2}$. By the chain rule,
$$F'(x)=\frac{1}{2}e^{x^2}\cdot\frac{d}{dx}(x^2)=\frac{1}{2}e^{x^2}\cdot 2x=xe^{x^2}.$$
This is exactly the original integrand.

**Check 2: a series check, using a method that does not use substitution at all.** Expand the exponential into its power series and integrate term by term:
$$xe^{x^2}=x+x^3+\frac{x^5}{2!}+\frac{x^7}{3!}+\cdots$$
So on $[0,1]$,
$$\int_0^1 xe^{x^2}\,dx=\frac12+\frac14+\frac{1}{12}+\frac{1}{48}+\frac{1}{240}+\frac{1}{1440}+\frac{1}{10080}+\cdots\approx 0.8591394.$$
Our formula gives the same number:
$$\left[\frac{1}{2}e^{x^2}\right]_0^1=\frac{e-1}{2}\approx 0.8591409.$$
The two agree to six digits, so the factor $\frac12$ and the exponent are both correct.

**Check 3: a numerical slope check.** Near $x=1$ the integrand equals $1\cdot e^1\approx 2.71828$. Our antiderivative has $F(1)=\frac{e}{2}\approx 1.359141$ and $F(1.001)=\frac12 e^{1.002001}\approx 1.361863$, so the quotient $\frac{F(1.001)-F(1)}{0.001}\approx 2.7224$, which approaches $2.71828$ as the step gets smaller, exactly as a derivative should.

## Common mistakes

- **Losing the factor $\frac12$.** Because $du=2x\,dx$ and the integrand contains only $x$, we must write $x\,dx=\frac12\,du$. Forgetting this gives $e^{x^2}+C$, which is wrong by a factor of two.
- **Choosing $u=x$.** With $u=x$ the integrand becomes $\int u\,e^{u^2}\,du$, which is no easier than before. The candidate must be the inner expression $x^2$.
- **Believing that $\int e^{x^2}\,dx$ can be computed.** On its own, $e^{x^2}$ has no antiderivative that can be written with the usual elementary functions. The factor $x$ is exactly what makes the substitution possible, which is the real lesson of this problem.
- **Forgetting the constant $C$.** The answer is the family $\frac12 e^{x^2}+C$.

## How I would explain it in class

This integral looks different from Problem 4 but has exactly the same shape, because the integrand is a function of the inner expression $x^2$ multiplied by the derivative of that expression, up to the factor $\frac12$. Setting $u=x^2$ gives $du=2x\,dx$, so $x\,dx$ becomes $\frac12\,du$, and the integral turns into $\frac12\int e^u\,du=\frac12 e^u+C$. Substituting back we obtain $\frac12 e^{x^2}+C$, and differentiating it returns $xe^{x^2}$, exactly as required.
