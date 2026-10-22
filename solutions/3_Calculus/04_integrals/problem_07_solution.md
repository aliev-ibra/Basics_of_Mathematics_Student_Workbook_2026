# Problem 7

## The original problem

Compute
$$\int xe^x\,dx.$$
First write the product differentiation rule and, on that basis, explain the meaning of the integration-by-parts formula. Verify the result by differentiation.

> **Why this problem:** it connects a new technique with the familiar product rule.

## What we are looking for

We are asked for an antiderivative of a product in which neither factor can be integrated on its own in a useful way. The product rule gives a way out, so the task is to write that rule down, turn it upside down to obtain the integration-by-parts formula, explain in words what the formula says, and then apply it. The result must still be verified by differentiating back.

## The idea we need

**The product rule (differentiation).** For differentiable functions $u$ and $v$,
$$\frac{d}{dx}\bigl(u(x)v(x)\bigr)=u'(x)v(x)+u(x)v'(x).$$

**Integration by parts (the product rule run backwards).** Integrate both sides of the product rule over $x$:
$$u(x)v(x)=\int u'(x)v(x)\,dx+\int u(x)v'(x)\,dx,$$
because the integral of a derivative is the function itself. Rearranging gives the integration-by-parts formula:
$$\int u(x)v'(x)\,dx=u(x)v(x)-\int u'(x)v(x)\,dx.$$
In words: *the integral of a product equals the product of the factors minus the integral of the same product with the two roles of "differentiate" and "integrate" swapped.*

**How the formula is used.** We split the integrand into two parts and decide which one will be called $u$ (the part we will differentiate) and which one will be called $dv$ (the part we will integrate). Then we compute $du$ and $v$ and put everything into the formula.

**Conditions for use.** The method works when the integrand is a product and at least one of the two factors has an easy antiderivative, so that $v$ can be written down explicitly. The choice of $u$ and $dv$ is a real decision, and Problem 8 is dedicated to it.

**Constant of integration.** A single $C$ is added at the end, because the derivative of a constant is zero.

## Step-by-step solution

**Step 1. Write the product rule.**

$$
\frac{d}{dx}\bigl(u\,v\bigr)=u'v+uv'.
$$
This is the formula we are going to reverse.

**Step 2. Reverse it and write down the integration-by-parts formula.**

Integrating both sides of the product rule and rearranging:
$$
\int u\,v'\,dx=uv-\int u'v\,dx.
$$
For our integral $\int xe^x\,dx$ the product is $u\cdot v'=x\cdot e^x$.

**Step 3. Choose $u$ and $dv$, and justify the choice.**

We take
$$u=x,\qquad dv=e^x\,dx.$$
The justification: differentiating $x$ makes it simpler (it becomes $1$), while integrating $e^x$ does not make it harder (it stays $e^x$). The guiding rule is to put into $u$ the factor that becomes simpler when differentiated, and into $dv$ the factor whose integral you already know. Choosing the other way round, $u=e^x$ and $dv=x\,dx$, would give $du=e^x\,dx$ and $v=\frac{x^2}{2}$, and the remaining integral $\int\frac{x^2}{2}e^x\,dx$ is harder than the one we started with.

**Step 4. Compute $du$ and $v$.**

$$
du=dx,\qquad v=\int e^x\,dx=e^x.$$
The exponential is its own antiderivative, because $\frac{d}{dx}e^x=e^x$.

**Step 5. Substitute into the formula.**

$$
\int xe^x\,dx=uv-\int u'v\,dx=xe^x-\int 1\cdot e^x\,dx=xe^x-e^x+C.
$$

**Step 6. Write the answer in a tidy form.**

$$
\int xe^x\,dx=e^x(x-1)+C,$$
which is the same expression, just factored.

## Why each step is valid

- Step 1 is valid because it is the standard product rule for differentiation.
- Step 2 is valid because integration undoes differentiation on a derivative: $\int \frac{d}{dx}(uv)\,dx=uv+C$, and algebra allows the rearrangement.
- Step 3 is valid because our choice makes both $du$ and $v$ computable and leaves a remaining integral that is strictly simpler than the original one.
- Step 4 is valid because $u=x$ has derivative $1$, and because $e^x$ is its own antiderivative.
- Step 5 is valid because we substituted $u$, $dv$, $du$ and $v$ into a valid formula; the remaining integral $\int e^x\,dx=e^x+C$ is elementary.
- Step 6 is valid because $xe^x-e^x$ and $e^x(x-1)$ are the same number for every $x$.

## Final answer (in words)

The antiderivative of $xe^x$ is $xe^x-e^x$ (equivalently $e^x(x-1)$), plus an arbitrary constant $C$. In words: because the product rule turns the derivative of a product into two sums, reversing it lets us integrate a product by integrating one factor and differentiating the other, then correcting for the extra term that this produces.

## Verification

**Check 1 (the required one): differentiate the answer.** Let $F(x)=xe^x-e^x$. By the product rule,
$$F'(x)=1\cdot e^x+x\cdot e^x-e^x=xe^x,$$
which is exactly the original integrand.

**Check 2: a series check that does not use integration by parts.** Expand $(x-1)e^x$:
$$(x-1)e^x=\left(x-1\right)\left(1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots\right)=-1+\frac{x^2}{2}+\frac{x^3}{3}+\frac{x^4}{8}+\frac{x^5}{30}+\cdots$$
Differentiating this series term by term gives
$$0+x+x^2+\frac{x^3}{2}+\frac{x^4}{6}+\cdots=x\left(1+x+\frac{x^2}{2!}+\cdots\right)=xe^x.$$
So the formula is correct term by term, not only formally.

**Check 3: a numerical check of a definite integral.** The Fundamental Theorem of Calculus gives
$$\int_0^1 xe^x\,dx=\left[xe^x-e^x\right]_0^1=(e-e)-(0-1)=1.$$
Simpson's rule with four subintervals uses the values $0$, $0.321006$, $0.824361$, $1.587750$, $2.718282$ and gives
$$\frac{0.25}{3}\left(0+4\cdot 0.321006+2\cdot 0.824361+4\cdot 1.587750+2.718282\right)\approx 1.000169,$$
which is very close to the exact value $1$.

## Common mistakes

- **Choosing the factors in the wrong order.** Taking $u=e^x$ and $dv=x\,dx$ gives a remaining integral that is harder than the original. The factor that simplifies under differentiation belongs in $u$.
- **Forgetting the second step.** Integration by parts is not finished after the first product: the term $-\int u'v\,dx$ must still be computed, which is why the answer contains both $xe^x$ and $-e^x$.
- **Sign errors.** The formula is $\int u\,v'\,dx=uv-\int u'v\,dx$, with a minus sign in front of the second integral, so the answer must contain $-e^x$ and not $+e^x$.
- **Leaving out the constant $C$.** The indefinite integral is the family $xe^x-e^x+C$.
- **Not explaining the choice.** The problem asks us to justify the choice of $u$ and $dv$ on the basis of the product rule, so the reasoning is part of the answer, not optional decoration.

## How I would explain it in class

The product rule says $(uv)'=u'v+uv'$, and integrating both sides and rearranging gives $\int u\,v'\,dx=uv-\int u'v\,dx$, which is integration by parts. For $\int xe^x\,dx$ I put $u=x$ and $dv=e^x\,dx$, because differentiating $x$ gives the simple number $1$ while integrating $e^x$ keeps it unchanged, whereas the opposite choice makes the problem harder. The formula then gives $xe^x-\int e^x\,dx=xe^x-e^x+C$, and differentiating this returns $xe^x$.
