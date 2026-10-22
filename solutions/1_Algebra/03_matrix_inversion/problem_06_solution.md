# Problem 06

## The original problem

Solve
$$Ax=b,$$
where
$$A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}5\\7\end{pmatrix},$$
using $x=A^{-1}b$. Then substitute the resulting vector back into the equation and check the result.

## What we are looking for

We need the vector $x$ that satisfies $Ax=b$, found by first computing $A^{-1}$ and then multiplying it by $b$.

## The idea we need

If $A$ is invertible, the system $Ax=b$ has the unique solution $x=A^{-1}b$. This follows from multiplying both sides of $Ax=b$ on the left by $A^{-1}$: $A^{-1}Ax=A^{-1}b$, so $Ix=A^{-1}b$.

## Step-by-step solution

1. Compute $\det A=2\cdot3-1\cdot1=6-1=5\neq0$, so $A^{-1}$ exists.
2. Use the $2\times2$ formula:
$$A^{-1}=\frac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}
=\begin{pmatrix}\frac35&-\frac15\\-\frac15&\frac25\end{pmatrix}.$$
3. Multiply by $b$:
$$x=A^{-1}b=\begin{pmatrix}\frac35&-\frac15\\-\frac15&\frac25\end{pmatrix}\begin{pmatrix}5\\7\end{pmatrix}
=\begin{pmatrix}\frac35\cdot5-\frac15\cdot7\\-\frac15\cdot5+\frac25\cdot7\end{pmatrix}
=\begin{pmatrix}3-\frac75\\-1+\frac{14}{5}\end{pmatrix}
=\begin{pmatrix}\frac85\\ \frac95\end{pmatrix}.$$

## Why each step is valid

The determinant is nonzero, so the inverse exists and the formula applies. Multiplying $A^{-1}$ on the left of $b$ is valid because matrix multiplication is associative and $A^{-1}A=I$.

## Final answer (in words)

The solution is $x=\begin{pmatrix}\frac85\\ \frac95\end{pmatrix}$.

## Verification

Substitute back into $Ax=b$:
$$Ax=\begin{pmatrix}2&1\\1&3\end{pmatrix}\begin{pmatrix}\frac85\\ \frac95\end{pmatrix}
=\begin{pmatrix}2\cdot\frac85+\frac95\\ \frac85+3\cdot\frac95\end{pmatrix}
=\begin{pmatrix}\frac{16+9}{5}\\ \frac{8+27}{5}\end{pmatrix}
=\begin{pmatrix}5\\7\end{pmatrix}=b.$$
The equation holds.

## Common mistakes

- Multiplying $b$ on the wrong side or using $bA^{-1}$.
- Sign errors in the inverse formula.
- Forgetting to verify by substitution.

## How I would explain it in class

I first find $A^{-1}$, then multiply it by $b$ to get $x$. Because $A^{-1}A=I$, this $x$ solves $Ax=b$. I finish by plugging $x$ back into the original equation to confirm both components match $b$.
