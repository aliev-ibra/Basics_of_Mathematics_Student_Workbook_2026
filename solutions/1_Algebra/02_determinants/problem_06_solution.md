# Problem 06

## The original problem

For

$$
A(t)=\begin{pmatrix}t&1\\2&t\end{pmatrix}
$$

find all values of $t$ for which the matrix is not invertible. Explain how your answer is related to the determinant being zero.

## What we are looking for

The determinant here depends on a parameter $t$, so the answer must be a list of parameter values, not a single number. We need all values of $t$ for which the matrix cannot be inverted, and we must explain the connection between that question and the vanishing of the determinant. The typical trap is to solve the quadratic only halfway.

## The idea we need

**The determinant as a function of $t$.** For a $2\times2$ matrix the Leibniz formula gives, with $a=t$, $b=1$, $c=2$, $d=t$:

$$\det A(t) = a\cdot d-b\cdot c = t\cdot t-1\cdot 2 = t^2-2.$$

**The invertibility criterion.** For a square matrix of any size,

$$A \text{ is invertible} \iff \det A \neq 0.$$

The word *not invertible* therefore means exactly $\det A(t)=0$, so the problem is reduced to solving the quadratic equation $t^2-2=0$.

**The solutions.** $t^2=2$ gives $t=\sqrt2$ or $t=-\sqrt2$. Equivalently, using the factorisation $t^2-2=(t-\sqrt2)(t+\sqrt2)$, the determinant vanishes exactly at those two values.

## Step-by-step solution

**Step 1: compute the determinant.**

$$\det A(t)=t\cdot t-1\cdot 2=t^2-2.$$

**Step 2: impose the condition.** The matrix is not invertible exactly when the determinant is zero:

$$t^2-2=0 \iff t^2=2 \iff t=\pm\sqrt2.$$

So the two exceptional values are $t=\sqrt2$ and $t=-\sqrt2$.

**Step 3: say what happens for all other values.** For every real $t$ different from $\sqrt2$ and $-\sqrt2$ we have $t^2-2\neq 0$, so $\det A(t)\neq 0$ and $A(t)$ is invertible.

**Step 4: explain the link with the rows.** At the two exceptional values the rows of $A(t)$ become proportional, and that is exactly why the determinant vanishes. The first row is $(t,1)$ and the second is $(2,t)$. The second row equals $\tfrac{2}{t}$ times the first row whenever $t\cdot t=2$:

$$t=\sqrt2:\quad \sqrt2\cdot(\sqrt2,1)=(2,\sqrt2),$$
$$t=-\sqrt2:\quad (-\sqrt2)\cdot(-\sqrt2,1)=(2,-\sqrt2).$$

In both cases the rows are dependent, so the matrix cannot be inverted, which is the same statement as $\det A(t)=0$.

## Why each step is valid

- The Leibniz formula applies to every $2\times2$ matrix, and it applies here to the matrix whose entries are numbers involving the parameter $t$; the result is a polynomial in $t$.
- The criterion "invertible if and only if the determinant is not zero" is valid for every square matrix, so it is legitimate to replace the question about the inverse by the equation $\det A(t)=0$.
- The equation $t^2=2$ has exactly two real solutions, because a positive number has two square roots, one positive and one negative. Both must be listed.
- For $t\neq 0$ the factor $\tfrac{2}{t}$ is well defined, and it is at the two solutions that $\tfrac{2}{t}=t$, which is precisely the condition $t^2=2$.

## Final answer (in words)

The matrix $A(t)$ is not invertible for exactly two values of the parameter, namely $t=\sqrt2$ and $t=-\sqrt2$. For every other value of $t$ the matrix is invertible. The two conditions are the same statement: the matrix fails to be invertible exactly when its determinant $t^2-2$ is zero.

$$\det A(t)=t^2-2,\qquad A(t)\text{ is not invertible} \iff t=\sqrt2 \text{ or } t=-\sqrt2.$$

## Verification

I check the answer by substitution. For $t=\sqrt2$ the determinant is $(\sqrt2)^2-2=2-2=0$; for $t=-\sqrt2$ it is $(-\sqrt2)^2-2=2-2=0$. Both give a singular matrix, as required.

I also check a value that is *not* in the answer. At $t=0$ the matrix is $\begin{pmatrix}0&1\\2&0\end{pmatrix}$ with determinant $0\cdot0-1\cdot2=-2\neq 0$, so it is invertible — consistent with $0\notin\{\pm\sqrt2\}$.

Finally, the factorisation $t^2-2=(t-\sqrt2)(t+\sqrt2)$ shows that the determinant has exactly two real zeros and no others, so no further exceptional values were missed. As a structural check, the rows $(t,1)$ and $(2,t)$ are dependent exactly when their $2\times2$ determinant $t^2-2$ vanishes, which confirms the answer from a second direction.

## Common mistakes

- Writing $t=2$ instead of $t=\pm\sqrt2$, i.e. forgetting to take the square root at all.
- Solving $t^2=2$ and reporting only the positive root $t=\sqrt2$, thereby missing $t=-\sqrt2$.
- Claiming that the matrix is never invertible, or that it is invertible only for positive $t$.
- Solving the quadratic and then describing the answer as "the determinant is $t^2-2$" without ever saying which values of $t$ make it zero.

## How I would explain it in class

The determinant of this matrix is $t^2-2$, and a matrix is invertible exactly when its determinant is not zero, so the matrix fails to be invertible exactly when $t^2=2$. That gives two values, $t=\sqrt2$ and $t=-\sqrt2$, and for every other $t$ the matrix has an inverse. At those two values the second row is $\tfrac{2}{t}$ times the first row, so the rows are dependent, which is the geometric reason the determinant vanishes.
