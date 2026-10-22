# Problem 01

## The original problem

For
$$A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$$
check, without using a formula, whether $B=A^{-1}$. Compute $AB$ and $BA$ and relate the result to the definition of the inverse.

## What we are looking for

We need to decide whether $B$ is the inverse of $A$ by multiplying the two matrices in both orders and checking whether both products equal the identity matrix.

## The idea we need

A matrix $B$ is the inverse of $A$ exactly when $AB=I$ and $BA=I$, where $I$ is the identity matrix. No formula is needed: we just perform the two multiplications and compare each result with $I$.

## Step-by-step solution

1. Compute $AB$:
$$AB=\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}.$$
- First row, first column: $2\cdot 1+1\cdot(-1)=2-1=1$.
- First row, second column: $2\cdot(-1)+1\cdot 2=-2+2=0$.
- Second row, first column: $1\cdot 1+1\cdot(-1)=1-1=0$.
- Second row, second column: $1\cdot(-1)+1\cdot 2=-1+2=1$.

So
$$AB=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I.$$

2. Compute $BA$:
$$BA=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\begin{pmatrix}2&1\\1&1\end{pmatrix}.$$
- First row, first column: $1\cdot 2+(-1)\cdot 1=2-1=1$.
- First row, second column: $1\cdot 1+(-1)\cdot 1=1-1=0$.
- Second row, first column: $(-1)\cdot 2+2\cdot 1=-2+2=0$.
- Second row, second column: $(-1)\cdot 1+2\cdot 1=-1+2=1$.

So
$$BA=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I.$$

## Why each step is valid

Both products equal the identity matrix, and the definition of an inverse requires $AB=BA=I$. Since both directions give $I$, $B$ satisfies the definition.

## Final answer (in words)

Yes, $B$ is the inverse of $A$, because multiplying $A$ and $B$ in either order gives the identity matrix.

## Verification

We checked both $AB$ and $BA$ independently and each equals $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$.

## Common mistakes

- Checking only $AB$ and forgetting $BA$.
- Sign errors in matrix multiplication.
- Comparing the product to $A$ instead of to $I$.

## How I would explain it in class

I multiply $A$ by $B$ and $B$ by $A$ and see whether both give the identity matrix. Here both products are $I$, so $B$ is exactly $A^{-1}$. This is the definition of an inverse: it works from both sides.
