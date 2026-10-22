# Problem 11

## The original problem

For each integral, first write which method you choose and how you recognize it, and then compute:
1. $\int\sin(3x)\,dx$,
2. $\int x\ln x\,dx$,
3. $\int\frac{x}{\sqrt{x^2+1}}\,dx$.

> **Why this problem:** it tests the choice of method based on the structure of the problem.

## What we are looking for

For each of three integrals we want an antiderivative. Before any calculation we must name the method and say what in the integrand tells us to use it.

## The idea we need

**Substitution.** This reverses the chain rule. We look for an inner function $u(x)$ whose derivative also appears in the integrand, up to a constant factor. Then $\int f(u(x))\,u'(x)\,dx=\int f(u)\,du$.

**Integration by parts.** This reverses the product rule: $\int u\,v'\,dx=uv-\int u'v\,dx$. We use it for a product of two unrelated kinds of functions. We differentiate the factor that becomes simpler.

## Step-by-step solution

**Integral 1: $\int\sin(3x)\,dx$.**

- *Method:* substitution. We recognize it because $\sin$ is applied to an inner function $3x$, and the derivative of the inner function is the constant $3$.
- Let $u=3x$. Then $du=3\,dx$, so $dx=\frac{du}{3}$.
- The integral becomes $\frac13\int\sin u\,du=-\frac13\cos u+C$.
- Return to $x$:
$$\int\sin(3x)\,dx=-\frac13\cos(3x)+C.$$

**Integral 2: $\int x\ln x\,dx$.**

- *Method:* integration by parts. We recognize it because the integrand is a product of $x$ and $\ln x$. No inner function has its derivative sitting next to it, so substitution does not apply.
- Choose $u=\ln x$, because its derivative $\frac1x$ is simpler, and $dv=x\,dx$. Then $du=\frac{1}{x}dx$ and $v=\frac{x^2}{2}$.
- The formula gives
$$\int x\ln x\,dx=\frac{x^2}{2}\ln x-\int\frac{x^2}{2}\cdot\frac1x\,dx=\frac{x^2}{2}\ln x-\frac12\int x\,dx.$$
- Since $\frac12\int x\,dx=\frac{x^2}{4}$, we get
$$\int x\ln x\,dx=\frac{x^2}{2}\ln x-\frac{x^2}{4}+C.$$
This holds for $x>0$, where $\ln x$ is defined.

**Integral 3: $\int\frac{x}{\sqrt{x^2+1}}\,dx$.**

- *Method:* substitution. We recognize it because the inner function $x^2+1$ sits under the root, and its derivative $2x$ appears in the numerator, up to the constant factor $2$.
- Let $u=x^2+1$. Then $du=2x\,dx$, so $x\,dx=\frac{du}{2}$.
- The integral becomes $\frac12\int u^{-1/2}\,du=\frac12\cdot2u^{1/2}=\sqrt u$.
- Return to $x$:
$$\int\frac{x}{\sqrt{x^2+1}}\,dx=\sqrt{x^2+1}+C.$$

## Why each step is valid

- Integral 1: the substitution is valid because the derivative of $3x$ is $3$, so $dx=\frac{du}{3}$ exactly. The antiderivative of $\sin u$ is $-\cos u$.
- Integral 2: parts is valid because it is the product rule reversed. The choice of $u=\ln x$ is good because the remaining integral $\int x\,dx$ is easy. The opposite choice would require an antiderivative of $\ln x$, which is not a basic one.
- Integral 3: the substitution is valid because $x\,dx$ equals $\frac{du}{2}$ exactly, and the power rule gives $\int u^{-1/2}du=2u^{1/2}$.

## Final answer (in words)

1. Substitution gives $-\frac13\cos(3x)+C$.
2. Parts gives $\frac{x^2}{2}\ln x-\frac{x^2}{4}+C$, for $x>0$.
3. Substitution gives $\sqrt{x^2+1}+C$.

## Verification

**Check 1: differentiate each answer.**

- The derivative of $-\frac13\cos(3x)$ is $-\frac13\cdot(-\sin(3x))\cdot3=\sin(3x)$.
- The derivative of $\frac{x^2}{2}\ln x-\frac{x^2}{4}$ is $x\ln x+\frac{x^2}{2}\cdot\frac1x-\frac{x}{2}=x\ln x+\frac x2-\frac x2=x\ln x$.
- The derivative of $\sqrt{x^2+1}$ is $\frac{1}{2\sqrt{x^2+1}}\cdot2x=\frac{x}{\sqrt{x^2+1}}$.

**Check 2: numerical values of definite integrals from $0$ to $1$, $1$ to $2$ and $0$ to $1$.** A numerical computation gives $\int_0^1\sin(3x)\,dx\approx0.66333$, which equals $\frac{1-\cos3}{3}$. It gives $\int_1^2x\ln x\,dx\approx0.63629$, which equals $2\ln2-\frac34$. It gives $\int_0^1\frac{x}{\sqrt{x^2+1}}\,dx\approx0.41421$, which equals $\sqrt2-1$.

**Check 3: sanity of the structure.** In the third integral the answer $\sqrt{x^2+1}$ is increasing for $x>0$, as it should be, because the integrand is positive there.

## Common mistakes

- Forgetting the factor $\frac13$ in the first integral and writing $-\cos(3x)$.
- Choosing $u=x$ in the second integral. Then $v$ would be an antiderivative of $\ln x$, which is harder.
- Writing the second answer without the term $-\frac{x^2}{4}$, or with a wrong sign.
- Leaving the answer in terms of $u$ instead of returning to $x$.
- Forgetting the constant $C$.

## How I would explain it in class

In the first and third integrals I see an inner function whose derivative is present, namely $3x$ with derivative $3$, and $x^2+1$ with derivative $2x$, so I use substitution and get $-\frac13\cos(3x)+C$ and $\sqrt{x^2+1}+C$. In the second integral I see a product of $x$ and $\ln x$ with no such inner function, so I use parts with $u=\ln x$ and $dv=x\,dx$, which gives $\frac{x^2}{2}\ln x-\frac{x^2}{4}+C$. In all three cases differentiating the answer gives back the original integrand.
