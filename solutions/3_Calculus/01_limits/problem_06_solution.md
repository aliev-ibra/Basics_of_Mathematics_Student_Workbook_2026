# Problem 06

## The original problem
Compute
$$\lim_{x\to\infty}\frac{3x^2-x+1}{5x^2+4x-2}.$$
Compare the method with Exercise 1. Explain what changes when moving from $n$ to a real variable $x$, and what stays the same.

## What we are looking for
We want the value that the function approaches as the real variable $x$ grows without bound. This is a limit at infinity of a rational function. We also need to compare the method with Exercise 1 and say what changes and what stays the same when the index $n$ is replaced by a continuous real variable $x$.

## The idea we need
For a quotient of two polynomials of the same degree, the limit as $x\to\infty$ is the ratio of the leading coefficients. The method is to divide numerator and denominator by the highest power of $x$ that appears, so that every lower-degree term divided by a power of $x$ tends to zero. The rule is the same as for sequences: if $P(x)$ and $Q(x)$ are polynomials of the same degree $d$ with leading coefficients $a$ and $b$ ($b\neq 0$), then
$$\lim_{x\to\infty}\frac{P(x)}{Q(x)}=\frac{a}{b}.$$
The condition is that both polynomials have the same degree and the denominator's leading coefficient is not zero.

## Step-by-step solution
1. Write the function:
$$f(x)=\frac{3x^2-x+1}{5x^2+4x-2}.$$
2. Divide both numerator and denominator by $x^2$, the highest power of $x$ that appears:
$$f(x)=\frac{3-\frac1x+\frac1{x^2}}{5+\frac4x-\frac2{x^2}}.$$
3. As $x\to\infty$, each of the terms $\frac1x$, $\frac1{x^2}$, $\frac4x$, and $\frac2{x^2}$ tends to zero, because a fixed constant divided by a growing number tends to zero.
4. Therefore the numerator tends to $3$ and the denominator tends to $5$. Since the denominator's limit is $5$, which is not zero, the quotient law for limits applies:
$$\lim_{x\to\infty}f(x)=\frac{3}{5}.$$

## Comparison with Exercise 1
Exercise 1 used the sequence index $n$ (an integer), while this exercise uses a real variable $x$. The computation is identical: divide by the highest power and compare leading coefficients. What changes is the interpretation: $n$ runs through integer values $1,2,3,\dots$, whereas $x$ runs through all real values, so we are now looking at a continuous function rather than a discrete sequence. What stays the same is the dominant-term rule: for large arguments, the highest-degree terms control the behavior, and the limit is the ratio $3/5$ of the leading coefficients.

## Why each step is valid
Step 2 is valid because dividing both numerator and denominator by the same nonzero power of $x$ ($x^2$ for $x\neq 0$, and we consider $x\to\infty$ so $x$ is large and nonzero) does not change the value of the fraction.
Step 3 uses the rule that $\frac{c}{x^k}\to 0$ as $x\to\infty$ for any constant $c$ and any positive integer $k$.
Step 4 uses the quotient law for limits: if $\lim f(x)=A$ and $\lim g(x)=B$ with $B\neq 0$, then $\lim\frac{f(x)}{g(x)}=\frac{A}{B}$. Here $A=3$ and $B=5\neq 0$.

## Final answer (in words)
The function approaches the value $\frac{3}{5}$ as $x$ grows without bound. The limit is $0.6$, determined by the ratio of the leading coefficients $3$ and $5$, exactly as in the sequence case of Exercise 1.

## Verification
Take $x=1000$. Then
$$\frac{3(1000)^2-1000+1}{5(1000)^2+4(1000)-2}=\frac{2999001}{5003998}\approx 0.59933,$$
which is close to $0.6$. Take $x=10000$: $\frac{299990001}{500039998}\approx 0.599933$, even closer to $0.6$. This numerical check supports the analytical result.

## Common mistakes
- Forgetting to divide every term by $x^2$, so that lower-degree terms do not vanish.
- Subtracting the leading coefficients instead of dividing them.
- Thinking the result changes because $x$ is continuous rather than integer; the dominant-term rule is the same.

## How I would explain it in class
This is exactly the same idea as Exercise 1, only now $x$ can be any real number instead of just a whole number. We divide top and bottom by $x^2$, the smaller pieces with $x$ in the bottom shrink to zero, and we are left with the leading coefficients $3$ and $5$. So the function settles at $3/5$, or $0.6$, as $x$ gets larger and larger.
