# Problem 11

## The original problem

For
$$A(t)=\begin{pmatrix}1&t\\t&1\end{pmatrix}$$
find all $t$ for which the matrix is invertible, and then give a formula for $A(t)^{-1}$. Explain what happens to this formula at the excluded values.

## What we are looking for

The matrix depends on a number $t$. We need the set of values of $t$ for which $A(t)$ has an inverse, an explicit formula for the inverse in terms of $t$, and an explanation of why the formula breaks down at the values of $t$ that were excluded.

## The idea we need

A square matrix is invertible exactly when its determinant is not zero. For $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ the determinant is $ad-bc$, and when it is nonzero the inverse is
$$\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$
The factor $\frac1{ad-bc}$ is the only place where something can go wrong, because it requires dividing by the determinant.

## Step-by-step solution

**Step 1: the determinant.** Here $a=d=1$ and $b=c=t$, so
$$\det A(t)=1\cdot1-t\cdot t=1-t^2=(1-t)(1+t).$$

**Step 2: when is it zero?** A product is zero only if one factor is zero, so $\det A(t)=0$ exactly for $t=1$ and $t=-1$. Hence $A(t)$ is invertible for all real $t$ except $t=1$ and $t=-1$.

**Step 3: the inverse formula.** For $t\neq\pm1$ the $2\times2$ formula gives
$$A(t)^{-1}=\frac{1}{1-t^2}\begin{pmatrix}1&-t\\-t&1\end{pmatrix}.$$

**Step 4: the excluded values.** At $t=1$ the matrix is $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ and at $t=-1$ it is $\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. In both cases the second row is a multiple of the first (equal to it, or equal to $-1$ times it), so the rows are dependent and the matrix squashes the plane onto a line. The formula contains the factor $\frac1{1-t^2}$, which becomes $\frac10$ at these values, so it is not defined there; this is not a flaw of the formula, it reflects the fact that no inverse exists.

## Why each step is valid

- The determinant criterion says that nonzero determinant is equivalent to invertibility, so solving $1-t^2\neq0$ gives exactly the right set of $t$.
- Factoring $1-t^2$ as $(1-t)(1+t)$ is valid for every $t$ and makes the zeros visible at a glance.
- The inverse formula is derived from the identity $A\cdot\mathrm{adj}(A)=\det A\cdot I$, which needs $\det A\neq0$ to divide; this is why Step 3 is stated only for $t\neq\pm1$.
- At the excluded values the matrix has dependent rows, so $A(t)x=0$ has non-zero solutions (for $t=1$, $x=(1,-1)^T$), and an invertible matrix could never send a nonzero vector to zero.

## Final answer (in words)

The matrix $A(t)$ is invertible for every real number $t$ except $t=1$ and $t=-1$. For these allowed values its inverse is
$$A(t)^{-1}=\frac{1}{1-t^2}\begin{pmatrix}1&-t\\-t&1\end{pmatrix}.$$
At $t=1$ and $t=-1$ the determinant is zero, the formula would need division by zero, and the matrix has no inverse.

## Verification

I multiply $A(t)$ by the proposed inverse:
$$\begin{pmatrix}1&t\\t&1\end{pmatrix}\begin{pmatrix}1&-t\\-t&1\end{pmatrix}=\begin{pmatrix}1-t^2&-t+t\\t-t&-t^2+1\end{pmatrix}=(1-t^2)I,$$
so dividing by $1-t^2$ gives exactly $I$.

A numerical check with $t=2$: $\det=1-4=-3$, the formula gives $A(2)^{-1}=-\frac13\begin{pmatrix}1&-2\\-2&1\end{pmatrix}=\begin{pmatrix}-\frac13&\frac23\\ \frac23&-\frac13\end{pmatrix}$, and
$$\begin{pmatrix}1&2\\2&1\end{pmatrix}\begin{pmatrix}-\frac13&\frac23\\ \frac23&-\frac13\end{pmatrix}=\begin{pmatrix}-\frac13+\frac43&\frac23-\frac23\\-\frac23+\frac23&\frac43-\frac13\end{pmatrix}=I.$$
Also $t=0$ gives $A(0)=I$ and the formula gives $I$, as expected.

## Common mistakes

- Giving only $t\neq1$ and forgetting $t=-1$; the equation $t^2=1$ has two solutions.
- Writing the determinant as $1+t^2$ or $t^2-1$ with the wrong sign, which would change the factor in the inverse.
- Leaving out the factor $\frac1{1-t^2}$, or forgetting to change the sign of the off-diagonal entries.
- Saying that at $t=1$ the inverse "is infinite"; the correct statement is that the inverse does not exist.

## How I would explain it in class

I compute the determinant $1-t^2$, which vanishes only at $t=1$ and $t=-1$, so the matrix is invertible for every other $t$. For those values the inverse is $\frac1{1-t^2}\begin{pmatrix}1&-t\\-t&1\end{pmatrix}$, and multiplying back gives $(1-t^2)I$ divided by $1-t^2$, which is $I$. At the two excluded values the rows of the matrix are proportional and the formula would divide by zero, so no inverse exists there.
