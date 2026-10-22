# Problem 09

## The original problem
Analyze the left-hand and right-hand limits of
$$f(x)=\frac1{x-2}$$
as $x\to2$. Does the two-sided limit exist? Interpret the result on a sketch of the graph and identify the vertical asymptote.

## What we are looking for
We want to know what happens to the function $f(x)=\frac{1}{x-2}$ when $x$ comes close to the number $2$. We look at two cases separately: $x$ approaching $2$ from the left (with $x<2$) and from the right (with $x>2$). Then we decide whether one single two-sided limit exists, and we name the vertical line that the graph hugs.

## The idea we need
A limit describes where the values of $f$ go while $x$ gets close to a point, without ever being equal to it. The left-hand limit, written $\lim_{x\to2^-}f(x)$, uses only numbers $x$ smaller than $2$. The right-hand limit, written $\lim_{x\to2^+}f(x)$, uses only numbers $x$ larger than $2$. The two-sided limit exists only when both one-sided limits exist and are equal to the same value. A vertical asymptote is a vertical line $x=a$ such that the function grows without bound, in absolute value, near $a$.

## Step-by-step solution
1. At $x=2$ the denominator $x-2$ is zero, so $f(2)$ is not defined. The numerator is $1$, which is not zero. So we expect the values to become very large, not to settle near a finite number.
2. Left side: let $x$ be slightly less than $2$. Then $x-2$ is a small negative number. The number $1$ divided by a small negative number is a large negative number. The smaller $|x-2|$ is, the larger $|f(x)|$ is. So
$$\lim_{x\to2^-}\frac{1}{x-2}=-\infty.$$
3. Right side: let $x$ be slightly more than $2$. Then $x-2$ is a small positive number. The number $1$ divided by a small positive number is a large positive number. So
$$\lim_{x\to2^+}\frac{1}{x-2}=+\infty.$$
4. The two one-sided limits are different: one goes to minus infinity and the other to plus infinity. Neither is a finite number, and they do not agree. Therefore the two-sided limit $\lim_{x\to2}\frac1{x-2}$ does not exist.
5. The sketch. The graph has two separate branches. The right branch lies above the $x$-axis for $x>2$ and shoots up along the line $x=2$ as $x$ comes down to $2$. The left branch lies below the $x$-axis for $x<2$ and plunges down along the same line as $x$ rises to $2$. Far away, both branches come close to the $x$-axis, so the line $y=0$ is a horizontal asymptote.
6. The vertical asymptote is the line $x=2$.

## Why each step is valid
Step 1 is valid because division by zero is not defined, so $2$ is not in the domain. Step 2 and step 3 are valid because the sign of a quotient is the sign of the numerator times the sign of the denominator, and because $\frac{1}{t}$ becomes larger than any number we choose once $|t|$ is small enough: for example $\frac1t>1000$ whenever $0<t<0.001$. Step 4 is valid because the definition of a two-sided limit requires the same behavior from both sides. Step 6 is valid because the definition of a vertical asymptote asks exactly that the one-sided values become unboundedly large near the line.

## Final answer (in words)
As $x$ approaches $2$ from the left, $f(x)$ decreases without bound, so the left-hand limit is $-\infty$. As $x$ approaches $2$ from the right, $f(x)$ increases without bound, so the right-hand limit is $+\infty$. The two sides disagree, so the two-sided limit does not exist, and the graph has the vertical asymptote $x=2$.

## Verification
Here is a table of real values of $f(x)=\frac1{x-2}$.

| $x$ (left) | $f(x)$ | $x$ (right) | $f(x)$ |
|---|---|---|---|
| $1.9$ | $-10$ | $2.1$ | $10$ |
| $1.99$ | $-100$ | $2.01$ | $100$ |
| $1.999$ | $-1000$ | $2.001$ | $1000$ |

Moving closer to $2$ makes the left values more and more negative, and the right values more and more positive. This matches the analytic answer. A second check uses the symmetry of the function: $f(2+h)=\frac1h$ and $f(2-h)=-\frac1h$, so the two sides are exact opposites of each other, and they can never agree.

## Common mistakes
- Writing that the limit is $\infty$ without saying from which side, or claiming that the two-sided limit equals $\infty$.
- Saying that the limit does not exist because the function is not defined at $2$. The real reason is that the one-sided limits are different.
- Forgetting the sign: the left side gives minus infinity, not plus infinity.

## How I would explain it in class
If I stand slightly to the left of $2$, the denominator is a tiny negative number, so the fraction is a huge negative number, and if I stand slightly to the right, it is a huge positive number. Since the two sides go in opposite directions, there is no single value they agree on, so the two-sided limit does not exist. The graph climbs and falls along the vertical line $x=2$, which is the vertical asymptote.
