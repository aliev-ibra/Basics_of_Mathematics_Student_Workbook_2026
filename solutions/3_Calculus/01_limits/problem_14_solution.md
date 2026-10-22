# Problem 14

## The original problem
Compute
$$\lim_{x\to0}\frac{1-\cos x}{x^2}.$$
Justify the result without using l'Hôpital's rule, using a trigonometric identity and the fundamental limit.

## What we are looking for
We want the number that $\frac{1-\cos x}{x^2}$ approaches when $x$ is close to $0$, measured in radians. At $x=0$ the top is $1-\cos0=0$ and the bottom is $0$, so we get $\frac00$. We must remove this by a trigonometric identity, and then use the fundamental limit $\frac{\sin t}{t}\to1$ as $t\to0$.

## The idea we need
There is the half-angle identity
$$1-\cos x=2\sin^2\frac x2.$$
It follows from the double angle formula $\cos x=1-2\sin^2\frac x2$. With it, the top becomes a square of a sine, and we can match the sine with its angle $\frac x2$ in the denominator. Then the fundamental limit applies.

## Step-by-step solution
1. Apply the identity to the top:
$$\frac{1-\cos x}{x^2}=\frac{2\sin^2\frac x2}{x^2}.$$
2. Write the bottom as $x^2=4\left(\frac x2\right)^2$. Then
$$\frac{2\sin^2\frac x2}{4\left(\frac x2\right)^2}=\frac12\cdot\left(\frac{\sin\frac x2}{\frac x2}\right)^2.$$
3. Put $t=\frac x2$. When $x\to0$, also $t\to0$, so $\frac{\sin t}{t}\to1$.
4. The square is a continuous operation, so $\left(\frac{\sin t}{t}\right)^2\to1^2=1$.
5. Therefore
$$\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12\cdot1=\frac12.$$

## Why each step is valid
Step 1 is valid because the half-angle identity holds for every real $x$. It comes from the cosine of a double angle: $\cos x=\cos^2\frac x2-\sin^2\frac x2=1-2\sin^2\frac x2$. Step 2 is only algebra: $\frac{2}{4}=\frac12$. Step 3 is valid because the fundamental limit holds for any variable that tends to zero, and $\frac x2\to0$. Step 4 is valid because if a quantity tends to $1$, its square tends to $1$. The step is allowed because we never used $x=0$, only $x$ near $0$ with $x\neq0$, where all the expressions are defined.

## Final answer (in words)
The limit is $\frac12$. The expression $1-\cos x$ behaves like $\frac12x^2$ for small $x$, so dividing by $x^2$ leaves one half.

## Verification
Numerical values of $\frac{1-\cos x}{x^2}$:

| $x$ | value |
|---|---|
| $0.1$ | $0.499583$ |
| $0.01$ | $0.499996$ |
| $0.001$ | $0.49999996$ |
| $-0.01$ | $0.499996$ |

The values approach $0.5$ from below, on both sides. A different algebraic method: multiply the top and bottom by $1+\cos x$. Then $(1-\cos x)(1+\cos x)=1-\cos^2x=\sin^2x$, so the expression equals $\frac{\sin^2x}{x^2(1+\cos x)}=\left(\frac{\sin x}{x}\right)^2\cdot\frac{1}{1+\cos x}$. As $x\to0$ this tends to $1^2\cdot\frac{1}{1+1}=\frac12$. The two methods agree.

## Common mistakes
- Thinking that $1-\cos x$ is close to $1-1=0$ and so the limit is $0$, ignoring the zero in the denominator.
- Forgetting to square the fundamental limit, or forgetting the factor $\frac12$ that comes from $\frac24$.
- Using the wrong identity, for example writing $1-\cos x=\sin^2x$, which is false.

## How I would explain it in class
I replace $1-\cos x$ by $2\sin^2\frac x2$, which is a correct identity, and then I write $x^2$ as four times $\left(\frac x2\right)^2$. That gives one half times the square of $\frac{\sin(x/2)}{x/2}$, and the fraction tends to one by the fundamental limit. So the answer is one half.
