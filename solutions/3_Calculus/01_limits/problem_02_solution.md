# Problem 02

## The original problem
Compute
$$\lim_{n\to\infty}\frac{3n+1}{n^2+4},\qquad \lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}.$$
Compare the two cases and formulate a general observation about the degrees of the polynomials in the numerator and denominator.

## What we are looking for
We want the limiting value of two different sequences as $n$ grows without bound. In the first sequence the numerator grows more slowly than the denominator, while in the second the numerator grows faster. We need to find each limit and then state a general rule that covers both cases.

## The idea we need
For a quotient of two polynomials, the limit as $n\to\infty$ is decided by comparing the degrees of the numerator and the denominator. If the numerator's degree is smaller, the limit is $0$. If the degrees are equal, the limit is the ratio of the leading coefficients. If the numerator's degree is larger, the absolute value of the quotient grows without bound, so the limit is infinite (with a sign determined by the leading coefficients). This works because dividing every term by the highest power of $n$ in the denominator makes all lower-degree terms vanish.

## Step-by-step solution
First limit:
$$\lim_{n\to\infty}\frac{3n+1}{n^2+4}.$$
1. Divide numerator and denominator by $n^2$, the highest power in the denominator:
$$\frac{3n+1}{n^2+4}=\frac{\frac{3}{n}+\frac{1}{n^2}}{1+\frac{4}{n^2}}.$$
2. As $n\to\infty$, $\frac{3}{n}\to 0$, $\frac{1}{n^2}\to 0$, and $\frac{4}{n^2}\to 0$. So the numerator tends to $0$ and the denominator tends to $1$.
3. Therefore
$$\lim_{n\to\infty}\frac{3n+1}{n^2+4}=\frac{0}{1}=0.$$

Second limit:
$$\lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}.$$
4. Divide numerator and denominator by $n^2$, the highest power in the denominator:
$$\frac{2n^3-n}{5n^2+1}=\frac{2n-\frac{1}{n}}{5+\frac{1}{n^2}}.$$
5. As $n\to\infty$, the numerator $2n-\frac{1}{n}$ grows without bound (it behaves like $2n$), while the denominator tends to $5$. So the quotient grows without bound in the positive direction:
$$\lim_{n\to\infty}\frac{2n^3-n}{5n^2+1}=+\infty.$$

## Comparison and general observation
The first case has numerator degree $1$ and denominator degree $2$, so the numerator's degree is smaller and the limit is $0$. The second case has numerator degree $3$ and denominator degree $2$, so the numerator's degree is larger and the limit is $+\infty$. The general observation is: compare the degrees. If $\deg(\text{numerator})<\deg(\text{denominator})$, the limit is $0$. If the degrees are equal, the limit is the ratio of the leading coefficients. If $\deg(\text{numerator})>\deg(\text{denominator})$, the limit is infinite, with the sign given by the ratio of the leading coefficients.

## Why each step is valid
Step 1 and step 4 are valid because dividing both numerator and denominator by the same nonzero power of $n$ does not change the fraction's value.
Steps 2 and 5 use the rule $\frac{c}{n^k}\to 0$ as $n\to\infty$ for constant $c$ and positive integer $k$, and the fact that $2n\to+\infty$.
The conclusion for each limit uses the quotient law or the fact that a quantity growing without bound divided by a nonzero constant still grows without bound.

## Final answer (in words)
The first sequence approaches $0$ because its numerator grows more slowly than its denominator. The second sequence grows without bound toward $+\infty$ because its numerator grows faster than its denominator. In general, the relative degrees of the numerator and denominator decide the limit: lower numerator degree gives $0$, equal degrees give the ratio of leading coefficients, and higher numerator degree gives an infinite limit.

## Verification
For the first limit, take $n=1000$: $\frac{3(1000)+1}{1000^2+4}=\frac{3001}{1000004}\approx 0.003001$, close to $0$. For the second limit, take $n=1000$: $\frac{2(1000)^3-1000}{5(1000)^2+1}=\frac{1999999000}{5000001}\approx 399.9998$, which is large and positive, consistent with growth toward $+\infty$.

## Common mistakes
- Comparing only the leading terms without checking the degrees first.
- Saying the second limit is a finite number instead of recognizing it diverges to $+\infty$.
- Forgetting that "limit is $+\infty$" means the sequence does not converge to a finite value.

## How I would explain it in class
Look at the powers on top and bottom. If the bottom power is bigger, everything shrinks to zero; if they are equal, you divide the leading numbers; if the top power is bigger, the whole thing blows up. Here one over $n^2$ goes to zero, and the other one has an extra $n$ on top so it shoots off to infinity.
