# Problem 13

## The original problem

Let
$$F(x)=\int_0^x(t^2+1)\,dt.$$
Determine $F(x)$, compute $F'(x)$, and compare the result with the integrand. Explain in your own words why the height of the function describes the local rate of increase of the accumulated area.

> **Why this problem:** it connects differentiation and integration through the idea of accumulation.

## What we are looking for

The function $F(x)$ is the area under the graph of $t^2+1$ from $0$ up to the moving point $x$. We want a formula for $F(x)$, then its derivative $F'(x)$, and then a comparison with $t^2+1$. We also want a plain explanation of why they are linked.

## The idea we need

**Accumulation function.** The letter $t$ is a dummy variable that runs from $0$ to $x$. The upper limit $x$ is the variable of $F$. The number $F(x)$ is the signed area from $0$ to $x$.

**Fundamental Theorem of Calculus.** If $F(x)=\int_0^x f(t)\,dt$ and $f$ is continuous, then $F'(x)=f(x)$. We will also compute the formula directly and see that this holds.

## Step-by-step solution

**Step 1. Find an antiderivative of the integrand.** An antiderivative of $t^2+1$ is $G(t)=\frac{t^3}{3}+t$.

**Step 2. Evaluate between $0$ and $x$.**
$$F(x)=G(x)-G(0)=\frac{x^3}{3}+x-0=\frac{x^3}{3}+x.$$

**Step 3. Differentiate.** By the power rule,
$$F'(x)=\frac{3x^2}{3}+1=x^2+1.$$

**Step 4. Compare.** The derivative $x^2+1$ is exactly the integrand $t^2+1$, with $t$ replaced by $x$.

**Step 5. The explanation.** Move the upper limit from $x$ to $x+h$, where $h$ is a small positive number. The area grows by a thin strip. The strip has width $h$ and height almost equal to $f(x)=x^2+1$, so its area is about $f(x)\cdot h$. The growth per unit of width is therefore about $f(x)$. When $h$ shrinks to $0$, this becomes exactly $f(x)$.

## Why each step is valid

- Step 1 is valid because the derivative of $\frac{t^3}{3}+t$ is $t^2+1$.
- Step 2 is valid because of the Fundamental Theorem of Calculus, and $G(0)=0$.
- Step 3 is valid because the derivative of $\frac{x^3}{3}$ is $x^2$ and the derivative of $x$ is $1$.
- Step 4 is valid because the two expressions are equal as functions.
- Step 5 is valid because the new strip is almost a rectangle when $h$ is small, since the function barely changes over a tiny width.

## Final answer (in words)

The accumulated area is $F(x)=\frac{x^3}{3}+x$. Its derivative is $F'(x)=x^2+1$, which is the integrand evaluated at $x$. The height of the graph tells how fast the area grows: a taller graph adds more area for each small step to the right, and a lower graph adds less.

## Verification

**Check 1: the derivative.** Differentiating $\frac{x^3}{3}+x$ gives $x^2+1$, which matches the integrand.

**Check 2: a numerical value.** At $x=2$ the formula gives $F(2)=\frac83+2=\frac{14}{3}\approx4.667$. Simpson's rule with the heights $1$, $2$, $5$ at $t=0,1,2$ gives $\frac13(1+8+5)=\frac{14}{3}$.

**Check 3: the rate of growth.** From $x=2$ to $x=2.01$ the formula gives $F(2.01)-F(2)\approx0.05020$. Dividing by $0.01$ gives about $5.02$, which is close to $f(2)=5$.

## Common mistakes

- Writing $F'(x)=\int_0^x2t\,dt$, which means differentiating inside the integral.
- Forgetting that $F(0)=0$, which shows that no constant is added here.
- Mixing up $t$ and $x$. The variable $t$ runs inside the integral, and the final formula depends only on $x$.
- Thinking that $F'$ is the area. It is the height of the graph.

## How I would explain it in class

The function $F(x)$ is the area under $t^2+1$ from $0$ to $x$, and the calculation gives $F(x)=\frac{x^3}{3}+x$. Differentiating gives $F'(x)=x^2+1$, which is the height of the graph at $x$. This is natural, because a small step to the right adds a thin strip whose area is about height times width, so the rate of growth of the area is the height.
