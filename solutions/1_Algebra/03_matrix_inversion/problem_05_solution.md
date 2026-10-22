# Problem 05

## The original problem

Use Gauss-Jordan elimination to find the inverse of
$$A=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}.$$
Check the result by multiplication.

## What we are looking for

We want the inverse of the $3\times3$ matrix $A$, found by reducing $[A\mid I]$ to $[I\mid A^{-1}]$.

## The idea we need

Gauss-Jordan elimination works for any square matrix: form $[A\mid I]$, use elementary row operations to make the left block the identity, and the right block becomes $A^{-1}$. The method requires a nonzero pivot at each step.

## Step-by-step solution

Start with
$$[A\mid I]=\left(\begin{array}{ccc|ccc}1&1&0&1&0&0\\0&1&1&0&1&0\\1&0&1&0&0&1\end{array}\right).$$

1. $R_3\leftarrow R_3-R_1$:
$$\left(\begin{array}{ccc|ccc}1&1&0&1&0&0\\0&1&1&0&1&0\\0&-1&1&-1&0&1\end{array}\right).$$

2. $R_3\leftarrow R_3+R_2$:
$$\left(\begin{array}{ccc|ccc}1&1&0&1&0&0\\0&1&1&0&1&0\\0&0&2&-1&1&1\end{array}\right).$$

3. $R_3\leftarrow \tfrac12 R_3$:
$$\left(\begin{array}{ccc|ccc}1&1&0&1&0&0\\0&1&1&0&1&0\\0&0&1&-\tfrac12&\tfrac12&\tfrac12\end{array}\right).$$

4. $R_2\leftarrow R_2-R_3$:
$$\left(\begin{array}{ccc|ccc}1&1&0&1&0&0\\0&1&0&\tfrac12&\tfrac12&-\tfrac12\\0&0&1&-\tfrac12&\tfrac12&\tfrac12\end{array}\right).$$

5. $R_1\leftarrow R_1-R_2$:
$$\left(\begin{array}{ccc|ccc}1&0&0&\tfrac12&-\tfrac12&\tfrac12\\0&1&0&\tfrac12&\tfrac12&-\tfrac12\\0&0&1&-\tfrac12&\tfrac12&\tfrac12\end{array}\right).$$

Thus
$$A^{-1}=\begin{pmatrix}\tfrac12&-\tfrac12&\tfrac12\\ \tfrac12&\tfrac12&-\tfrac12\\ -\tfrac12&\tfrac12&\tfrac12\end{pmatrix}.$$

## Why each step is valid

Each operation is an elementary row operation, reversible and equivalent to left-multiplication by an elementary matrix. The sequence reduces $A$ to $I$, so the same sequence applied to $I$ produces $A^{-1}$.

## Final answer (in words)

The inverse of $A$ is $\begin{pmatrix}\frac12&-\frac12&\frac12\\ \frac12&\frac12&-\frac12\\ -\frac12&\frac12&\frac12\end{pmatrix}$.

## Verification

Compute $A A^{-1}$:
$$\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}
\begin{pmatrix}\tfrac12&-\tfrac12&\tfrac12\\ \tfrac12&\tfrac12&-\tfrac12\\ -\tfrac12&\tfrac12&\tfrac12\end{pmatrix}
=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}=I.$$
Each entry checks out, for example the $(1,1)$ entry is $1\cdot\tfrac12+1\cdot\tfrac12+0=1$.

## Common mistakes

- Arithmetic errors when subtracting fractional rows.
- Forgetting to normalize the pivot row before eliminating above it.
- Checking only one entry of the product instead of all.

## How I would explain it in class

I build the augmented matrix with the identity on the right and reduce the left side to $I$ step by step. Every operation I do on the left I also do on the right, so the right side becomes the inverse. Then I multiply $A$ by my answer to confirm I get the identity.
