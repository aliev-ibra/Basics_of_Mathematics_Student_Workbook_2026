# Problem 13

## The original problem
Using
$$\lim_{x\to0}\frac{\sin x}{x}=1,$$
compute
$$\lim_{x\to0}\frac{\sin5x}{x},\qquad \lim_{x\to0}\frac{\sin2x}{\sin3x}.$$
In each case, show how you reduce the expression to the fundamental limit.

## What we are looking for
We want two numbers: the limit of $\frac{\sin5x}{x}$ as $x\to0$, and the limit of $\frac{\sin2x}{\sin3x}$ as $x\to0$. Here $x$ is measured in radians. Both expressions give $\frac00$ when we put in $x=0$, so we must change them until the fundamental limit $\frac{\sin x}{x}\to1$ can be used.

## The idea we need
The fundamental limit says that $\frac{\sin t}{t}\to1$ when $t\to0$. The letter $t$ can stand for any expression that tends to zero. So $\frac{\sin5x}{5x}\to1$, because $t=5x\to0$ when $x\to0$. The method is to multiply and divide by the right constant, so that the number inside the sine appears in the denominator too.

## Step-by-step solution
**First limit.**

1. Substituting $x=0$ gives $\frac00$, so we transform.
2. Multiply and divide by $5$. This does not change the value:
$$\frac{\sin5x}{x}=5\cdot\frac{\sin5x}{5x}.$$
3. Put $t=5x$. When $x\to0$, also $t\to0$, and $\frac{\sin t}{t}\to1$.
4. So
$$\lim_{x\to0}\frac{\sin5x}{x}=5\cdot1=5.$$

**Second limit.**

5. Substituting $x=0$ again gives $\frac00$.
6. Multiply and divide so that each sine has its own matching denominator:
$$\frac{\sin2x}{\sin3x}=\frac{\sin2x}{2x}\cdot\frac{2x}{3x}\cdot\frac{3x}{\sin3x}.$$
7. The middle factor is $\frac{2x}{3x}=\frac23$ for $x\neq0$.
8. The first factor tends to $1$, with $t=2x$. The last factor is the reciprocal of $\frac{\sin3x}{3x}$, which tends to $1$, so it tends to $\frac11=1$.
9. By the product rule for limits,
$$\lim_{x\to0}\frac{\sin2x}{\sin3x}=1\cdot\frac23\cdot1=\frac23.$$

## Why each step is valid
Step 2 is valid because $5\cdot\frac{1}{5x}=\frac1x$, so we multiplied by $\frac55=1$. Step 3 is valid because the fundamental limit holds for any variable tending to zero; here $5x$ tends to zero exactly when $x$ does. Step 6 is valid because we inserted $\frac{2x}{2x}$ and $\frac{3x}{3x}$, both equal to $1$ for $x\neq0$, and the limit only looks at $x\neq0$. Step 8 uses that the reciprocal of a function that tends to $1$ also tends to $1$. Step 9 uses the rule that the limit of a product is the product of the limits, valid because each of the three limits exists.

## Final answer (in words)
The first limit equals $5$ and the second limit equals $\frac23$. In the first case, the number in front of $x$ inside the sine comes out as a factor. In the second case, it is the ratio of the two numbers, $2$ over $3$.

## Verification
Numerical values:

| $x$ | $\frac{\sin5x}{x}$ | $\frac{\sin2x}{\sin3x}$ |
|---|---|---|
| $0.1$ | $4.79426$ | $0.67227$ |
| $0.01$ | $4.99792$ | $0.66672$ |
| $0.001$ | $4.99998$ | $0.66667$ |
| $-0.01$ | $4.99792$ | $0.66672$ |

The first column approaches $5$, and the second approaches $0.6667=\frac23$. Both expressions are even functions of $x$, so the negative value gives the same number as $0.01$. A different method: for the second limit, divide the top and bottom by $x$ to get $\frac{\sin2x/x}{\sin3x/x}$. By the first limit with $5$ replaced by $2$ and by $3$, this is $\frac{2}{3}$, the same answer.

## Common mistakes
- Answering $1$ for $\frac{\sin5x}{x}$ because "sine over $x$ is $1$". The argument of the sine must match the denominator.
- Cancelling the word "sin" in $\frac{\sin2x}{\sin3x}$ as if it were a common factor. Sine is a function, not a number, and it cannot be cancelled this way.
- Using degrees instead of radians. The fundamental limit holds only in radians.

## How I would explain it in class
The rule says sine of a small thing divided by that same small thing is close to one. For $\frac{\sin5x}{x}$ I multiply and divide by five, so the bottom matches the angle, and the limit is five times one. For $\frac{\sin2x}{\sin3x}$ I match each sine with its own angle, and what remains is the ratio $\frac{2x}{3x}=\frac23$.
