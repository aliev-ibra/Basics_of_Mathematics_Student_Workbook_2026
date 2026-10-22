# Problem 11

## The original problem
Compute
$$\lim_{n\to\infty}\sqrt[n]{5^n+2^n}.$$
Explain which term dominates and why the transformation looks different from the case of a quotient of polynomials.

## What we are looking for
We want the number that the sequence $a_n=\sqrt[n]{5^n+2^n}$ approaches when $n$ becomes very large. The symbol $\sqrt[n]{\ }$ means the $n$-th root. We also need to say which of the two terms, $5^n$ or $2^n$, matters most, and why the method differs from dividing by the highest power of $n$.

## The idea we need
For large $n$, the number $5^n$ is far bigger than $2^n$, because the ratio $\left(\frac25\right)^n$ goes to zero. So $5^n$ is the dominant term. Dominance here is a comparison of exponentials with different bases, not a comparison of powers of $n$. The tool is to factor out the dominant term, so that the remaining sum is $1$ plus something that goes to zero. We also use two facts. First, $\sqrt[n]{5^n}=5$. Second, $\sqrt[n]{c}\to1$ for any fixed positive number $c$.

## Step-by-step solution
1. Factor $5^n$ out of the sum under the root:
$$5^n+2^n=5^n\left(1+\left(\frac25\right)^n\right).$$
2. Take the $n$-th root of a product as the product of $n$-th roots:
$$a_n=\sqrt[n]{5^n}\cdot\sqrt[n]{1+\left(\frac25\right)^n}=5\cdot\left(1+\left(\frac25\right)^n\right)^{1/n}.$$
3. Because $\frac25$ lies between $0$ and $1$, we have $\left(\frac25\right)^n\to0$. So the bracket $b_n=1+\left(\frac25\right)^n$ goes to $1$. In particular, $1\le b_n\le2$ for every $n$.
4. Squeeze the root of the bracket. Since $1\le b_n\le2$, we get $1\le b_n^{1/n}\le2^{1/n}$. As $n\to\infty$, $2^{1/n}\to1$. So $b_n^{1/n}\to1$.
5. Combine: $a_n=5\cdot b_n^{1/n}\to5\cdot1=5$.

An alternative, direct squeeze: $5^n\le5^n+2^n\le2\cdot5^n$. Taking $n$-th roots gives $5\le a_n\le5\cdot2^{1/n}$, and the right side tends to $5$.

## Why each step is valid
Step 1 is an exact algebraic identity: multiplying out the right side returns $5^n+2^n$. Step 2 is valid because $\sqrt[n]{xy}=\sqrt[n]{x}\cdot\sqrt[n]{y}$ for positive $x$ and $y$. Step 3 is valid because a number of absolute value smaller than $1$, raised to higher and higher powers, goes to zero. Step 4 uses the squeeze theorem: a sequence trapped between two sequences with the same limit has that limit, and taking the $n$-th root keeps the order of positive numbers. The fact $2^{1/n}\to1$ holds because the exponent $\frac1n$ goes to $0$ and the function $2^t$ is continuous at $t=0$. Step 5 is the product rule for limits.

## Final answer (in words)
The limit is $5$. The term $5^n$ dominates $2^n$, because the ratio $\left(\frac25\right)^n$ tends to zero, and the $n$-th root of $5^n$ is exactly $5$.

## Verification
Here are real values of $a_n=\sqrt[n]{5^n+2^n}$.

| $n$ | $a_n$ |
|---|---|
| $1$ | $7$ |
| $5$ | $5.0102$ |
| $10$ | $5.0000524$ |
| $20$ | $5.0000000027$ |
| $50$ | $5.0000000000$ (to ten decimal places) |

The values fall toward $5$ very fast and always stay above $5$, which matches the squeeze $5\le a_n\le5\cdot2^{1/n}$. For example, for $n=10$ the upper bound is $5\cdot2^{0.1}\approx5.359$, and $5.0000524$ lies inside the bounds.

## Common mistakes
- Taking the root of each term separately and writing $\sqrt[n]{5^n+2^n}=5+2$. The root of a sum is not the sum of the roots.
- Dividing by $n^2$ or another power of $n$, as in a polynomial quotient. Here the dominance is between exponentials, so we factor out the largest exponential.
- Forgetting to justify that $\left(1+\left(\frac25\right)^n\right)^{1/n}\to1$.

## How I would explain it in class
Inside the root, $5^n$ is much bigger than $2^n$, so I factor out $5^n$, and the root of $5^n$ is exactly $5$. What is left is a number between $1$ and $2$ raised to the power one over $n$, and that goes to $1$ by the squeeze theorem. This differs from a polynomial quotient because we compare exponentials by factoring out the biggest one, not by dividing by a power of $n$.
