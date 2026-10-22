# Problem 15

## The original problem

For
$$A=\begin{pmatrix}2&1\\1&3\end{pmatrix},\qquad b=\begin{pmatrix}7\\8\end{pmatrix}$$
solve $Ax=b$ in two ways:

1. using $A^{-1}b$,
2. using Gaussian elimination.

Compare both solutions, the number of essential steps, and state which method was simpler in this example.

## What we are looking for

A vector $x=(x_1,x_2)^T$ with $2x_1+x_2=7$ and $x_1+3x_2=8$. We solve it twice, once by multiplying the inverse by $b$ and once by row elimination, then compare the answers and the amount of work.

## The idea we need

If $A$ is invertible, then $Ax=b$ is equivalent to $x=A^{-1}b$ (multiply both sides on the left by $A^{-1}$). Gaussian elimination instead transforms the system, by adding multiples of equations and swapping equations, to a triangular form that is solved from the bottom upwards (back substitution). Both methods give the same unique solution when $\det A\neq0$. For a $2\times2$ matrix the inverse is $\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.

## Step-by-step solution

**Method 1: the inverse.**

1. $\det A=2\cdot3-1\cdot1=5\neq0$, so $A^{-1}$ exists.
2. By the formula,
$$A^{-1}=\frac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}.$$
3. Multiply by $b$:
$$x=A^{-1}b=\frac15\begin{pmatrix}3\cdot7-1\cdot8\\-1\cdot7+2\cdot8\end{pmatrix}=\frac15\begin{pmatrix}13\\9\end{pmatrix}=\begin{pmatrix}\frac{13}5\\ \frac95\end{pmatrix}.$$

**Method 2: Gaussian elimination.** Write the augmented matrix $[A\mid b]$. To avoid fractions, swap the rows first (a swap does not change the solutions):
$$\left(\begin{array}{cc|c}2&1&7\\1&3&8\end{array}\right)\ \xrightarrow{R_1\leftrightarrow R_2}\ \left(\begin{array}{cc|c}1&3&8\\2&1&7\end{array}\right)\ \xrightarrow{R_2\leftarrow R_2-2R_1}\ \left(\begin{array}{cc|c}1&3&8\\0&-5&-9\end{array}\right).$$
Back substitution: the second row says $-5x_2=-9$, so $x_2=\frac95$. The first row says $x_1+3x_2=8$, so $x_1=8-\frac{27}5=\frac{13}5$.

**Comparison.** Both methods give $x=\left(\frac{13}5,\frac95\right)^T$. Method 1 needed the determinant, the four entries of the inverse, and then two row-times-column products (about three stages). Method 2 needed one swap, one row operation, and two short back-substitution lines (also about three to four stages). For this one system the work is similar, but Gaussian elimination is slightly simpler because it never produces the inverse, which we do not need; the inverse would pay off only if we had to solve $Ax=b$ for many different right-hand sides $b$.

## Why each step is valid

- Method 1 relies on $A^{-1}(Ax)=(A^{-1}A)x=Ix=x$, so multiplying by the inverse isolates $x$, which is valid because $\det A\neq0$.
- Method 2 uses only operations that do not change the set of solutions: swapping two equations and subtracting a multiple of one equation from another.
- Back substitution is valid because the last equation involves only $x_2$, and once $x_2$ is known the first equation determines $x_1$.
- Because $\det A\neq0$ the system has exactly one solution, so two correct methods must give the same vector; agreement is a real check.

## Final answer (in words)

Both methods give the same solution: the first component is thirteen fifths and the second is nine fifths,
$$x=\begin{pmatrix}\frac{13}5\\ \frac95\end{pmatrix}.$$
In this example Gaussian elimination is slightly simpler, since it avoids computing the whole inverse, whereas the inverse is worthwhile mainly when the same matrix is used with many right-hand sides.

## Verification

I substitute into the original system:
$$Ax=\begin{pmatrix}2\cdot\frac{13}5+\frac95\\ \frac{13}5+3\cdot\frac95\end{pmatrix}=\begin{pmatrix}\frac{26+9}5\\ \frac{13+27}5\end{pmatrix}=\begin{pmatrix}7\\8\end{pmatrix}=b.$$
Both equations hold: $2x_1+x_2=\frac{35}5=7$ and $x_1+3x_2=\frac{40}5=8$. As a further check, $A\cdot A^{-1}=\frac15\begin{pmatrix}6-1&-2+2\\3-3&-1+6\end{pmatrix}=I$, so the inverse used in Method 1 is correct.

## Common mistakes

- Computing $xA^{-1}$ or $bA^{-1}$ instead of $A^{-1}b$; the inverse must multiply $b$ from the left.
- Forgetting the factor $\frac15$ when multiplying $A^{-1}$ by $b$, which gives $(13,9)^T$.
- Sign errors in the inverse formula, in particular the entries $-1$ off the diagonal.
- Arithmetic slips in back substitution, such as $8-\frac95\cdot3$ computed with the wrong fraction.
- Stopping after finding $x_2$ and not substituting back to get $x_1$.

## How I would explain it in class

With the inverse, I compute $\det A=5$, write $A^{-1}=\frac15\begin{pmatrix}3&-1\\-1&2\end{pmatrix}$ and multiply it by $b$ from the left; with elimination, I swap the rows, subtract twice the first row from the second and use back substitution. Both give $x=\left(\frac{13}5,\frac95\right)^T$, and substituting into $Ax=b$ returns $(7,8)^T$. Elimination was a little simpler here because it does not build the whole inverse, which pays off only when the same matrix is used with many right-hand sides.
