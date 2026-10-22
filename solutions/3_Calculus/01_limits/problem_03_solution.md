# Problem 03

## The original problem
Compute
$$\lim_{n\to\infty}\left(\sqrt{n^2+5n}-n\right).$$
Use the conjugate expression and explain why this transformation removes the difficulty.

## What we are looking for
We want the value that the sequence approaches as $n$ grows without bound. The expression is the difference of two quantities that both grow like $n$, so direct substitution gives the indeterminate form $\infty-\infty$. We need to rewrite it to find the actual limiting value.

## The idea we need
The expression is an indeterminate form of type $\infty-\infty$, because both $\sqrt{n^2+5n}$ and $n$ grow without bound. The standard technique is to multiply by the conjugate expression $\sqrt{n^2+5n}+n$ over itself. This uses the difference of squares:
$$(\sqrt{n^2+5n}-n)(\sqrt{n^2+5n}+n)=(n^2+5n)-n^2=5n,$$
which removes the square roots from the numerator and turns the indeterminate difference into a quotient whose limit can be computed. The condition is that we multiply by a factor equal to $1$, so the value of the expression is unchanged.

## Step-by-step solution
1. Write the general term:
$$a_n=\sqrt{n^2+5n}-n.$$
2. Multiply by the conjugate expression over itself:
$$a_n=\left(\sqrt{n^2+5n}-n\right)\cdot\frac{\sqrt{n^2+5n}+n}{\sqrt{n^2+5n}+n}.$$
3. Apply the difference of squares in the numerator:
$$a_n=\frac{(\sqrt{n^2+5n})^2-n^2}{\sqrt{n^2+5n}+n}=\frac{n^2+5n-n^2}{\sqrt{n^2+5n}+n}=\frac{5n}{\sqrt{n^2+5n}+n}.$$
4. Since $n>0$, divide numerator and denominator by $n$. For the square root term, use $\frac{\sqrt{n^2+5n}}{n}=\sqrt{\frac{n^2+5n}{n^2}}=\sqrt{1+\frac{5}{n}}$:
$$a_n=\frac{5}{\sqrt{1+\frac{5}{n}}+1}.$$
5. As $n\to\infty$, $\frac{5}{n}\to 0$, so $\sqrt{1+\frac{5}{n}}\to\sqrt{1}=1$. Therefore the denominator tends to $1+1=2$:
$$\lim_{n\to\infty}a_n=\frac{5}{2}.$$

## Why each step is valid
Step 2 is valid because multiplying by $\frac{\sqrt{n^2+5n}+n}{\sqrt{n^2+5n}+n}$ is multiplying by $1$ (the denominator is nonzero for $n>0$), so the value is unchanged.
Step 3 uses the algebraic identity $(A-B)(A+B)=A^2-B^2$ with $A=\sqrt{n^2+5n}$ and $B=n$.
Step 4 is valid because $n>0$, so $\sqrt{n^2}=n$, allowing $\frac{\sqrt{n^2+5n}}{n}=\sqrt{1+\frac{5}{n}}$.
Step 5 uses the rule $\frac{c}{n}\to 0$ as $n\to\infty$ and the continuity of the square root function at $1$.

## Final answer (in words)
The sequence approaches the value $\frac{5}{2}$ as $n$ grows without bound. Rationalizing with the conjugate removes the indeterminate $\infty-\infty$ form and reveals that the two large terms nearly cancel, leaving a finite limit of $2.5$.

## Verification
Take $n=1000$. Then $\sqrt{1000^2+5(1000)}-1000=\sqrt{1005000}-1000\approx 1002.4975-1000=2.4975$, which is close to $2.5$. Take $n=10000$: $\sqrt{10000^2+5(10000)}-10000=\sqrt{100050000}-10000\approx 10002.4998-10000=2.4998$, even closer to $2.5$. This numerical check supports the result.

## Common mistakes
- Forgetting to multiply by the conjugate and trying to evaluate $\infty-\infty$ directly.
- Dividing $\sqrt{n^2+5n}$ by $n$ without accounting for the sign of $n$ (here $n>0$, so it is fine, but in general one must use $\sqrt{n^2}=|n|$).
- Concluding the limit is $0$ because the two terms "cancel," without computing the remaining finite part.

## How I would explain it in class
We have two big things that both grow like $n$, and we subtract them, which looks like infinity minus infinity. So we multiply by the conjugate, which is just a fancy way of multiplying by one, and the square roots disappear in the numerator. After dividing by $n$, only a constant remains, and that constant divided by two gives us $2.5$.
