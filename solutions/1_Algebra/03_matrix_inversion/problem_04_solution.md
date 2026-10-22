# Problem 04

## The original problem

Find $A^{-1}$ using the Gauss-Jordan method for
$$A=\begin{pmatrix}1&2\\3&5\end{pmatrix}.$$
Show the augmented matrix $[A\mid I]$ after successive operations and explain why obtaining $I$ on the left gives the inverse on the right.

## What we are looking for

We want the inverse of the $2\times2$ matrix $A$, obtained by transforming the augmented matrix $[A\mid I]$ until the left block becomes $I$.

## The idea we need

Gauss-Jordan elimination applies elementary row operations to $[A\mid I]$. The same operations that reduce $A$ to $I$ transform $I$ into $A^{-1}$, because each row operation is left-multiplication by an elementary matrix, and the product of those elementary matrices is $A^{-1}$.

## Step-by-step solution

Start with
$$[A\mid I]=\left(\begin{array}{cc|cc}1&2&1&0\\3&5&0&1\end{array}\right).$$

1. $R_2\leftarrow R_2-3R_1$:
$$\left(\begin{array}{cc|cc}1&2&1&0\\0&-1&-3&1\end{array}\right).$$

2. $R_2\leftarrow -R_2$:
$$\left(\begin{array}{cc|cc}1&2&1&0\\0&1&3&-1\end{array}\right).$$

3. $R_1\leftarrow R_1-2R_2$:
$$\left(\begin{array}{cc|cc}1&0&1-6&0+2\\0&1&3&-1\end{array}\right)
=\left(\begin{array}{cc|cc}1&0&-5&2\\0&1&3&-1\end{array}\right).$$

The left block is now $I$, so
$$A^{-1}=\begin{pmatrix}-5&2\\3&-1\end{pmatrix}.$$

## Why each step is valid

Each row operation is reversible and corresponds to left-multiplication by an elementary matrix. Reducing $A$ to $I$ means the product of these elementary matrices equals $A^{-1}$, so applying them to $I$ yields $A^{-1}$ on the right.

## Final answer (in words)

The inverse of $A$ is $\begin{pmatrix}-5&2\\3&-1\end{pmatrix}$.

## Verification

$$A A^{-1}=\begin{pmatrix}1&2\\3&5\end{pmatrix}\begin{pmatrix}-5&2\\3&-1\end{pmatrix}
=\begin{pmatrix}-5+6&2-2\\-15+15&6-5\end{pmatrix}
=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I.$$

## Common mistakes

- Applying an operation to only one side of the augmented matrix.
- Sign errors when subtracting rows.
- Stopping before the left block is fully reduced to $I$.

## How I would explain it in class

I attach the identity to $A$ and perform row operations until the left side becomes $I$. Because every operation is also applied to the right side, that side becomes $A^{-1}$. Finally I multiply $A$ by the result to confirm I get $I$.
