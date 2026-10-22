# Problem 02

## The original problem

Find the inverse of
$$A=\begin{pmatrix}3&2\\5&4\end{pmatrix}$$
using the formula for a $2\times2$ matrix. At the end, check the result by computing one product with $A$.

## What we are looking for

We need a $2\times2$ matrix $A^{-1}$ such that $AA^{-1}=A^{-1}A=I$, found with the standard $2\times2$ inverse formula.

## The idea we need

For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$, if $\det A=ad-bc\neq0$, then
$$A^{-1}=\frac1{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$
The determinant must be nonzero; otherwise the matrix has no inverse.

## Step-by-step solution

1. Identify $a=3,\ b=2,\ c=5,\ d=4$.
2. Compute the determinant:
$$\det A=3\cdot4-2\cdot5=12-10=2.$$
Since $2\neq0$, the inverse exists.
3. Apply the formula:
$$A^{-1}=\frac12\begin{pmatrix}4&-2\\-5&3\end{pmatrix}=\begin{pmatrix}2&-1\\-\frac52&\frac32\end{pmatrix}.$$

## Why each step is valid

The formula applies because $A$ is $2\times2$ and its determinant is nonzero. Dividing by the determinant rescales the adjugate matrix so that the product with $A$ gives $I$.

## Final answer (in words)

The inverse of $A$ is $\begin{pmatrix}2&-1\\-\frac52&\frac32\end{pmatrix}$.

## Verification

Multiply $A$ by the computed inverse:
$$A A^{-1}=\begin{pmatrix}3&2\\5&4\end{pmatrix}\begin{pmatrix}2&-1\\-\frac52&\frac32\end{pmatrix}.$$
- First row, first column: $3\cdot2+2\cdot(-\frac52)=6-5=1$.
- First row, second column: $3\cdot(-1)+2\cdot\frac32=-3+3=0$.
- Second row, first column: $5\cdot2+4\cdot(-\frac52)=10-10=0$.
- Second row, second column: $5\cdot(-1)+4\cdot\frac32=-5+6=1$.

The product is $I$, so the inverse is correct.

## Common mistakes

- Forgetting to divide by the determinant.
- Swapping $a$ and $d$ incorrectly.
- Using the formula when the determinant is zero.

## How I would explain it in class

I compute the determinant first; if it is nonzero, I swap the diagonal entries, negate the off-diagonal ones, and divide by the determinant. Then I multiply $A$ by the result to confirm I get the identity. That multiplication is the check that catches arithmetic mistakes.
