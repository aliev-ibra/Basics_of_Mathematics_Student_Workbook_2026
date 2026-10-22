# Problem 01

## The original problem
Compute
$$\lim_{n\to\infty}\frac{4n^2-3n+1}{2n^2+5n-7}.$$
Explain why the highest-degree terms determine the result.

## What we are looking for
We want the value that the sequence approaches as the index $n$ grows without bound. Both the numerator and the denominator are quadratic polynomials, so for very large $n$ the lower-degree terms become small compared with the squared terms. We need to find that limiting value.

## The idea we need
For a quotient of two polynomials of the same degree, the limit as $n\to\infty$ equals the ratio of the leading coefficients. This works because every term of lower degree divided by the highest power tends to zero. Formally, if $P(n)$ and $Q(n)$ are polynomials of the same degree $d$ with leading coefficients $a$ and $b$ ($b\neq 0$), then
$$\lim_{n\to\infty}\frac{P(n)}{Q(n)}=\frac{a}{b}.$$
The condition is that both polynomials have the same degree and the denominator's leading coefficient is not zero.

## Step-by-step solution
1. Write the general term of the sequence:
$$a_n=\frac{4n^2-3n+1}{2n^2+5n-7}.$$
2. Divide both the numerator and the denominator by $n^2$, the highest power of $n$ that appears:
$$a_n=\frac{4-\frac{3}{n}+\frac{1}{n^2}}{2+\frac{5}{n}-\frac{7}{n^2}}.$$
3. As $n\to\infty$, each of the terms $\frac{3}{n}$, $\frac{1}{n^2}$, $\frac{5}{n}$, and $\frac{7}{n^2}$ tends to zero, because a fixed constant divided by a growing number tends to zero.
4. Therefore the numerator tends to $4$ and the denominator tends to $2$. Since the denominator's limit is $2$, which is not zero, the quotient law for limits applies:
$$\lim_{n\to\infty}a_n=\frac{4}{2}=2.$$

## Why each step is valid
Step 1 restates the given sequence so its structure is visible.
Step 2 is valid because dividing both numerator and denominator of a fraction by the same nonzero number ($n^2$) does not change the value of the fraction.
Step 3 uses the rule that $\frac{c}{n^k}\to 0$ as $n\to\infty$ for any constant $c$ and any positive integer $k$.
Step 4 uses the quotient law for limits: if $\lim a_n=A$ and $\lim b_n=B$ with $B\neq 0$, then $\lim\frac{a_n}{b_n}=\frac{A}{B}$. Here $A=4$ and $B=2\neq 0$.

## Final answer (in words)
The sequence approaches the value $2$ as $n$ grows without bound; the limit is determined by the ratio of the leading coefficients $4$ and $2$, because the highest-degree terms dominate for large $n$.

## Verification
Take $n=1000$. Then
$$\frac{4(1000)^2-3(1000)+1}{2(1000)^2+5(1000)-7}=\frac{3997001}{2004993}\approx 1.9935,$$
which is close to $2$. Taking $n=10000$ gives $\frac{399970001}{200049993}\approx 1.99935$, even closer to $2$. This numerical check supports the analytical result.

## Common mistakes
- Forgetting to divide every term by $n^2$, so that some lower-degree terms do not vanish.
- Subtracting the leading coefficients instead of dividing them.
- Assuming the limit does not exist just because both numerator and denominator grow without bound.

## How I would explain it in class
When both the top and bottom grow like $n^2$, the smaller terms get lost in the noise for large $n$, so only the leading coefficients matter. Dividing everything by $n^2$ makes that visible, and the fractions with $n$ in the bottom shrink to zero. That leaves $4$ over $2$, which is $2$.
