# Problem 03

## The original problem

For
$$A=\begin{pmatrix}2&4\\1&2\end{pmatrix}$$
explain in two ways why $A^{-1}$ does not exist: using the determinant and using dependence between the rows.

## What we are looking for

We need to show that this matrix has no inverse, first by computing its determinant and second by showing its rows are linearly dependent.

## The idea we need

A square matrix is invertible if and only if its determinant is nonzero. Equivalently, its rows must be linearly independent. If the determinant is zero or the rows are dependent, the matrix is singular and has no inverse.

## Step-by-step solution

1. Compute the determinant:
$$\det A=2\cdot2-4\cdot1=4-4=0.$$
Since $\det A=0$, $A$ is singular, so $A^{-1}$ does not exist.

2. Check row dependence. The first row is $(2,4)$ and the second row is $(1,2)$. Notice
$$(2,4)=2\cdot(1,2).$$
So the first row is a scalar multiple of the second row. The rows are linearly dependent, which means the matrix has rank $1$, less than its size $2$.

## Why each step is valid

A zero determinant is an exact criterion for non-invertibility of a square matrix. Dependent rows mean the transformation collapses area to zero, so it cannot be undone by an inverse map.

## Final answer (in words)

$A^{-1}$ does not exist because $\det A=0$ and because the rows of $A$ are linearly dependent (the first row is twice the second).

## Verification

Both arguments agree: the determinant is $0$ and the rows are dependent, two equivalent signs that the matrix is singular.

## Common mistakes

- Saying a matrix has no inverse only because the determinant is zero, without understanding the geometric meaning.
- Confusing row dependence with column dependence in a way that leads to wrong conclusions.
- Attempting Gauss-Jordan and not noticing the zero pivot.

## How I would explain it in class

The determinant is zero, so the matrix is singular and has no inverse. You can also see this directly: the first row is just twice the second row, so the rows do not span the whole plane. Both observations point to the same fact.
