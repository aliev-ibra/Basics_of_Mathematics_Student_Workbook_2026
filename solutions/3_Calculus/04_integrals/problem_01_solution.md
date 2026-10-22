# Problem 1

## The original problem

For
$$f(x)=3x^2-4x+5$$
find one antiderivative $F(x)$. Write the entire family of antiderivatives, verify the result by differentiation, and explain the meaning of the constant $C$.

> **Why this problem:** it introduces integration as the inverse operation to differentiation.

## What we are looking for

We are asked to undo differentiation. An antiderivative of a function $f$ is a function $F$ whose derivative is $f$. We need one such function, then all of them, and then a check that differentiates our answer back to the original function. We also need to say in words what the letter $C$ means, because it is not decoration: it is the free vertical position of the graph.

## The idea we need

**Power rule for antiderivatives.** For any real number $n$ with $n\neq -1$,
$$\int x^n\,dx=\frac{x^{n+1}}{n+1}+C.$$
The condition $n\neq -1$ is needed because the denominator $n+1$ would be zero. The excluded case $n=-1$ is not a disaster: it produces a logarithm, which is exactly what happens in Problem 6.

**Integration is the inverse operation of differentiation.** If $F'(x)=f(x)$ on an interval, then
$$\int f(x)\,dx=F(x)+C.$$
This is why the constant of integration must appear. The derivative of a constant is zero, so adding $C$ never changes the value of the derivative.

**Why the family is complete.** Suppose $F$ and $G$ are two antiderivatives of $f$. Then $(F-G)'=f-f=0$ on the interval, and a function with zero derivative is a constant there. So $F-G$ is a constant, which means every antiderivative differs from every other one by a constant, and the indefinite integral is a whole family of functions rather than one function.

## Step-by-step solution

**Step 1. Split the integral into three separate integrals.**

We integrate term by term because the derivative of a sum is the sum of the derivatives, so an antiderivative of $f_1+f_2$ is the sum of antiderivatives of $f_1$ and $f_2$.

$$
\int(3x^2-4x+5)\,dx=\int 3x^2\,dx+\int(-4x)\,dx+\int 5\,dx.
$$

**Step 2. Integrate the first term with the power rule.**

The power of $x$ here is $2$, so we raise it to $3$ and divide by $3$:

$$
\int 3x^2\,dx=3\cdot\frac{x^{3}}{3}=x^3.
$$

**Step 3. Integrate the second term.**

The power is $1$, so we raise it to $2$ and divide by $2$, keeping the sign:

$$
\int(-4x)\,dx=-4\cdot\frac{x^{2}}{2}=-2x^2.
$$

**Step 4. Integrate the third term.**

The number $5$ is $5x^0$, so the power rule gives $5x^{1}/1=5x$. This is the same as saying that the derivative of $5x$ equals $5$.

$$
\int 5\,dx=5x.
$$

**Step 5. Put the pieces together and add one constant.**

$$
\int(3x^2-4x+5)\,dx=x^3-2x^2+5x+C.
$$

**Step 6. Write down one antiderivative.**

The family is an infinite list, so "one antiderivative" means one member of it. The simplest choice is the member with $C=0$:

$$
F(x)=x^3-2x^2+5x.
$$

**Step 7. Read the meaning of $C$.**

Every function of the form
$$F_C(x)=x^3-2x^2+5x+C$$
has the same derivative, because the derivative of the added constant $C$ is zero. Graphically, $C$ shifts the curve up or down along the vertical axis. The integrand $f$ alone can never tell us the value of $C$; only an extra piece of information, such as the value of $F$ at one point, can fix it. (In a definite integral the constant disappears on its own, because the Fundamental Theorem of Calculus evaluates the antiderivative as $F(b)-F(a)$ and the two copies of $C$ cancel.)

## Why each step is valid

- Step 1 is valid because differentiation is linear: $(f_1+f_2)'=f_1'+f_2'$, so an antiderivative of a sum is a sum of antiderivatives.
- Steps 2 to 4 are valid applications of the power rule $\int x^n\,dx=\frac{x^{n+1}}{n+1}+C$, and none of the powers $2$, $1$, $0$ equals the forbidden value $-1$.
- Step 5 is valid because a single constant $C$ may be added to a sum; the constant $C$ is the same symbol in every place because the integral of a sum has one arbitrary constant, not one per term.
- Step 6 is valid because $C=0$ is allowed in the family, and $0$ is just one of infinitely many choices.
- Step 7 is valid because $C'=0$ for every constant $C$, so the derivative of $F_C$ does not depend on $C$ at all.

## Final answer (in words)

One antiderivative of $f(x)=3x^2-4x+5$ is the cubic polynomial $x^3-2x^2+5x$. The entire family of antiderivatives is that same polynomial plus an arbitrary constant $C$, and the role of $C$ is purely vertical: it slides the graph up or down without changing the slope of the curve at any point, because the derivative of a constant is zero.

## Verification

**Check 1 (the required one): differentiate the answer.** Taking $F(x)=x^3-2x^2+5x$ and differentiating term by term gives
$$F'(x)=3x^2-4x+5,$$
which is exactly the original integrand. So $F$ is indeed an antiderivative.

**Check 2: test that $C$ really is free.** Take the family member with $C=7$, that is $G(x)=x^3-2x^2+5x+7$. Then $G'(x)=3x^2-4x+5$ as well, since the derivative of $7$ is zero. Also $G(x)-F(x)=7$, a constant, which confirms the claim that any two antiderivatives of the same function differ by a constant.

**Check 3: a numerical slope check, independent of the symbolic rule.** A derivative should be approximated by a small quotient of differences. We have $F(1)=1-2+5=4$ and $F(1.001)=1.003003001-2.004002+5.005=4.004001001$, so
$$\frac{F(1.001)-F(1)}{0.001}=\frac{0.004001001}{0.001}\approx 4.001,$$
while $f(1)=3-4+5=4$. The numerical slope is close to $4$, so the formula behaves the way the derivative says it should.

## Common mistakes

- **Omitting the constant.** Writing $\int(3x^2-4x+5)\,dx=x^3-2x^2+5x$ is incomplete: the indefinite integral is the family $x^3-2x^2+5x+C$.
- **Putting a separate constant in every term.** The answer is $x^3-2x^2+5x+C$, not $x^3+C-2x^2+C+5x+C$. Several different constants would mean the constant part depends on $x$, which is a contradiction.
- **Sign errors.** $\int(-4x)\,dx=-2x^2$, not $+2x^2$; a wrong sign here is caught immediately by differentiating back.
- **Thinking the integrand determines $C$.** The function $f$ alone leaves $C$ free. A number for $C$ requires an extra condition, for example $F(0)=5$ would force $C=5$.

## How I would explain it in class

I integrate each term of $f(x)=3x^2-4x+5$ with the power rule and get $x^3-2x^2+5x+C$. The constant $C$ appears because the derivative of any constant is zero, so every vertical shift of that graph is also an antiderivative. Differentiating $x^3-2x^2+5x$ gives back exactly $3x^2-4x+5$, which proves that the answer is right and that the whole family is complete.
