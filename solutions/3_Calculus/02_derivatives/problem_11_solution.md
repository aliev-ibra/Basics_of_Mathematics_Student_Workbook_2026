# Problem 11

## The original problem

Using only
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h,$$
find the derivative of $f(x)=x^2$. Compare the result with the power rule and indicate where the limit is used in the calculation.

> **Why this problem:** it shows the origin of the power rule and the direct connection between the derivative and a limit.

## What we are looking for

We must find $f'(x)$ for $f(x)=x^2$ without any differentiation rules. We may use only the definition. The definition says: take a small step $h$ from $x$, compute the average slope between the two points, and see which number this average slope approaches when $h$ gets closer and closer to $0$. We must also compare with the power rule and say exactly where the limit was used.

## The idea we need

The **definition of the derivative**. The fraction
$$\frac{f(x+h)-f(x)}{h}$$
is called the **difference quotient**. It is the slope of the straight line through the points $(x,f(x))$ and $(x+h,f(x+h))$. This line is called a secant line. The symbol $\lim_{h\to0}$ means: look at what number the quotient gets close to when $h$ is very small but not equal to $0$. This number, if it exists, is the derivative.

The important point is that $h$ is never $0$ in the quotient, because we cannot divide by $0$. So we can cancel $h$ in the numerator and the denominator before taking the limit. This is the standard algebraic trick for this kind of problem.

We also need the expansion $(x+h)^2=x^2+2xh+h^2$.

## Step-by-step solution

1. Write down the difference quotient for $f(x)=x^2$:
$$\frac{f(x+h)-f(x)}{h}=\frac{(x+h)^2-x^2}{h}.$$
2. Expand the square in the numerator: $(x+h)^2=x^2+2xh+h^2$.
3. Subtract $x^2$. The terms $x^2$ cancel, and what is left is $2xh+h^2$. So the quotient is
$$\frac{2xh+h^2}{h}.$$
4. Factor $h$ out of the numerator: $2xh+h^2=h(2x+h)$.
5. Cancel $h$. This is allowed because $h\ne0$ inside the limit. We get
$$\frac{h(2x+h)}{h}=2x+h\qquad (h\neq0).$$
6. **Now we use the limit.** We let $h$ go to $0$ in the simplified expression:
$$f'(x)=\lim_{h\to0}(2x+h)=2x.$$
As $h$ becomes very small, the term $h$ disappears and only $2x$ remains. This is the only step where the limit is taken.
7. Compare with the power rule. The power rule says $\frac{d}{dx}x^n=nx^{n-1}$. For $n=2$ it gives $2x^{1}=2x$. The two answers are the same.

## Why each step is valid

- Step 1 is valid because it is the definition of the derivative with $f(x)=x^2$ inserted, so $f(x+h)=(x+h)^2$.
- Steps 2 and 3 are valid because they are ordinary algebra: the square of a sum is the first square, plus twice the product, plus the second square.
- Step 5 is valid because in a limit as $h\to0$ we look at values of $h$ close to $0$ but different from $0$. For those values dividing by $h$ is allowed. Before this step, putting $h=0$ would give the meaningless $\frac00$.
- Step 6 is valid because $2x+h$ is a simple expression: when $h$ gets close to $0$, the value $2x+h$ gets close to $2x$. The limit exists and equals $2x$.
- Step 7 shows that the power rule is not a separate fact. It is a shortcut that comes from this same limit calculation.

## Final answer (in words)

Using only the definition, the derivative of $x^2$ is $2x$. The limit appears in one place only, at the end: the difference quotient simplifies to $2x+h$ for every $h\neq0$, and when $h$ tends to $0$ this tends to $2x$. This is the same result as the power rule gives for $x^2$.

## Verification

**Check 1: numbers.** Take $x=3$. The formula says $f'(3)=6$. The difference quotient for $h=0.001$ is
$$\frac{3.001^2-3^2}{0.001}=\frac{9.006001-9}{0.001}=6.001.$$
For $h=-0.001$ it is $\frac{2.999^2-9}{-0.001}=5.999$. The values from both sides are close to $6$.

**Check 2: the simplified quotient.** The quotient equals $2x+h$ exactly, so at $x=3$ it equals $6+h$. For $h=0.001$ this is $6.001$, the same as the direct computation. So the cancellation in Step 5 was correct.

**Check 3: a special point.** At $x=0$ the formula gives $f'(0)=0$. The quotient is $\frac{h^2}{h}=h$, which tends to $0$. The graph of $x^2$ has a horizontal tangent at its lowest point, as it should.

## Common mistakes

- Writing $(x+h)^2=x^2+h^2$ and forgetting the middle term $2xh$. Then the answer would wrongly be $0+h\to0$.
- Putting $h=0$ at the start. This gives $\frac00$, which has no meaning.
- Taking the limit too early, before cancelling $h$.
- Writing $\lim$ in every line. The limit symbol belongs only in front of the expressions where the limit is still to be taken.

## How I would explain it in class

The derivative is the number that the slope of a secant line approaches as the second point comes closer, so I write the quotient $\frac{(x+h)^2-x^2}{h}$ and expand the square. After the cancellation the quotient is $2x+h$, and only then I let $h$ go to $0$, which is the one place where the limit is used. The answer $2x$ is the same as the power rule gives, which shows that the power rule comes from the definition.
