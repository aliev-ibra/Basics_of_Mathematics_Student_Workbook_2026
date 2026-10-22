# Problem 9

## The original problem

Analyze the asymptotes of
$$f(x)=\frac{x^2+1}{x-1}.$$
Perform polynomial division and explain why the remainder term vanishes for large $|x|$.

> **Why this problem:** it teaches how to recognize an oblique asymptote and interpret the decomposition of a function.

## What we are looking for

We want every asymptote of the graph. An asymptote is a line that the graph gets closer and closer to. It can be vertical, horizontal, or slanted (we call a slanted one oblique). We also want to divide the polynomials and explain why the leftover piece becomes negligible when $x$ is very large in either direction.

## The idea we need

A fraction of two polynomials can be divided, just like $7\div3=2$ with remainder $1$, so $\tfrac73=2+\tfrac13$. In the same way, when the top has degree one more than the bottom, the division gives a straight line plus a small fraction. The straight line is the oblique asymptote. The small fraction has a constant on top and a growing expression on the bottom, so it goes to zero.

A vertical asymptote appears at a value where the denominator is zero and the numerator is not.

## Step-by-step solution

1. Domain. The denominator is zero at $x=1$, so the domain is all real numbers except $1$.

2. Vertical asymptote. At $x=1$ the numerator is $1^2+1=2$, which is not zero. So the function blows up near $1$. We check each side:
   - Just to the right of $1$ (say $x=1.01$): top $\approx2$, bottom is a small positive number, so $f\to+\infty$.
   - Just to the left of $1$ (say $x=0.99$): top $\approx2$, bottom is a small negative number, so $f\to-\infty$.

   So $x=1$ is a vertical asymptote.

3. Polynomial division. We divide $x^2+1$ by $x-1$. The first term of the answer is $x$, because $x\cdot(x-1)=x^2-x$. Subtract: $(x^2+1)-(x^2-x)=x+1$. The next term is $1$, because $1\cdot(x-1)=x-1$. Subtract: $(x+1)-(x-1)=2$. The remainder is $2$. So
$$\frac{x^2+1}{x-1}=x+1+\frac{2}{x-1}.$$

4. Why the remainder vanishes. The remainder term $\tfrac{2}{x-1}$ has a fixed top $2$ and a bottom that becomes huge when $|x|$ is large. A fixed number divided by a huge number is tiny. So
$$\lim_{x\to\pm\infty}\frac{2}{x-1}=0.$$

5. Oblique asymptote. Because $f(x)-(x+1)=\tfrac{2}{x-1}\to0$ at both ends, the graph approaches the line $y=x+1$ at both ends. This line is the oblique asymptote. There is no horizontal asymptote, because $f(x)$ behaves like $x$ and grows without bound.

6. Which side of the line the graph lies on. The gap $f(x)-(x+1)=\tfrac{2}{x-1}$ is positive when $x>1$ and negative when $x<1$. So on the right the graph lies above the line, and on the left below it.

7. Extra information for the sketch. The derivative is
$$f'(x)=1-\frac{2}{(x-1)^2}=\frac{x^2-2x-1}{(x-1)^2},$$
which is zero at $x=1\pm\sqrt2$. The bottom is always positive, so the sign comes from the top.

| Interval | Test point | $f'$ | Behavior |
|---|---|---|---|
| $(-\infty,1-\sqrt2)$ | $x=-1$ | $\tfrac12$ | increasing |
| $(1-\sqrt2,1)$ | $x=0$ | $-1$ | decreasing |
| $(1,1+\sqrt2)$ | $x=2$ | $-1$ | decreasing |
| $(1+\sqrt2,\infty)$ | $x=3$ | $\tfrac12$ | increasing |

   So there is a local maximum at $x=1-\sqrt2\approx-0.41$ with value $2-2\sqrt2\approx-0.83$, and a local minimum at $x=1+\sqrt2\approx2.41$ with value $2+2\sqrt2\approx4.83$.

8. What the sketch shows. There are two branches. The left branch comes from the lower left along the line $y=x+1$ from below, rises to the local maximum $(-0.41,-0.83)$, then falls steeply to $-\infty$ along the vertical line $x=1$. The right branch starts at $+\infty$ next to $x=1$, falls to the local minimum $(2.41,4.83)$, then climbs and hugs the line $y=x+1$ from above. The graph crosses the $y$-axis at $(0,-1)$ and never touches the $x$-axis.

| $x$ | $-10$ | $-1$ | $0$ | $2$ | $3$ | $10$ |
|---|---|---|---|---|---|---|
| $f(x)$ | $-9.18$ | $-1$ | $-1$ | $5$ | $5$ | $11.22$ |
| line $x+1$ | $-9$ | $0$ | $1$ | $3$ | $4$ | $11$ |

## Why each step is valid

- Division by zero is not allowed, so $x=1$ is excluded and must be examined by one-sided limits.
- Polynomial division is just an exact rewriting: if you multiply $x+1+\tfrac{2}{x-1}$ back by $x-1$ you get $x^2-1+2=x^2+1$.
- The limit of $\tfrac{2}{x-1}$ is zero because a fixed top over an unbounded bottom goes to zero. This is the reason the function and the line get arbitrarily close.
- The oblique asymptote is defined as a line where the vertical gap between graph and line tends to zero. That is exactly what step 4 shows.

## Final answer (in words)

The graph has a vertical asymptote at $x=1$, where it goes to $-\infty$ from the left and $+\infty$ from the right. It has an oblique asymptote $y=x+1$ at both ends, since $f(x)=x+1+\tfrac{2}{x-1}$ and the remainder $\tfrac{2}{x-1}$ tends to $0$ as $|x|\to\infty$. There is no horizontal asymptote.

## Verification

The gap between the function and the line, computed from numbers: at $x=10$, $f=101/9\approx11.222$ and $x+1=11$, so the gap is $2/9\approx0.222$. At $x=100$ the gap is $2/99\approx0.020$. At $x=-10$ the gap is $-2/11\approx-0.182$, and at $x=-100$ it is $-2/101\approx-0.020$. The gaps shrink toward zero on both sides, with the sign predicted in step 6.

The slope check: $f(x)/x\to1$ and $f(x)-x\to1$, which are the two limits that define the line $y=1\cdot x+1$. A computer algebra check (sympy) gave the same division, the same limits, and critical points $1\pm\sqrt2$.

## Common mistakes

- Saying there is a horizontal asymptote because both top and bottom grow. The top has a higher degree, so the function grows like $x$.
- Dropping the remainder and writing the asymptote as $y=x$ instead of $y=x+1$.
- Forgetting to check both sides of $x=1$ separately.
- Believing the graph can never cross an oblique asymptote. Here it does not, but in general it may; only the gap tending to zero is required.

## How I would explain it in class

Dividing $x^2+1$ by $x-1$ gives $x+1$ with remainder $2$, so the function equals $x+1$ plus the small piece $\tfrac{2}{x-1}$. When $x$ is very large in either direction, the bottom $x-1$ is huge, so the small piece goes to zero and the graph hugs the line $y=x+1$. At $x=1$ the bottom is zero but the top is not, so there is also a vertical asymptote there.
