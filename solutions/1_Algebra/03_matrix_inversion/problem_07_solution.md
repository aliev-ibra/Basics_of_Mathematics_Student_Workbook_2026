# Problem 07

## The original problem

For
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\0&3\end{pmatrix}$$
compute $(AB)^{-1}$ and $B^{-1}A^{-1}$. Check that the results are the same and explain the meaning of the reversed order.

## What we are looking for

We need to compute the inverse of the product $AB$ in two ways and confirm they agree, illustrating that $(AB)^{-1}=B^{-1}A^{-1}$.

## The idea we need

The inverse of a product reverses the order: $(AB)^{-1}=B^{-1}A^{-1}$. This is because $(AB)(B^{-1}A^{-1})=A(BB^{-1})A^{-1}=AIA^{-1}=AA^{-1}=I$.

## Step-by-step solution

1. Compute $AB$:
$$AB=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&3\end{pmatrix}
=\begin{pmatrix}2&3\\0&3\end{pmatrix}.$$

2. Invert $AB$ directly. $\det(AB)=2\cdot3-3\cdot0=6$, so
$$(AB)^{-1}=\frac16\begin{pmatrix}3&-3\\0&2\end{pmatrix}
=\begin{pmatrix}\frac12&-\frac12\\0&\frac13\end{pmatrix}.$$

3. Compute $B^{-1}$ and $A^{-1}$ separately:
$$B^{-1}=\begin{pmatrix}\frac12&0\\0&\frac13\end{pmatrix},\qquad
A^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$

4. Multiply in reversed order:
$$B^{-1}A^{-1}=\begin{pmatrix}\frac12&0\\0&\frac13\end{pmatrix}\begin{pmatrix}1&-1\\0&1\end{pmatrix}
=\begin{pmatrix}\frac12&-\frac12\\0&\frac13\end{pmatrix}.$$

## Why each step is valid

Both computations use the standard $2\times2$ inverse formula and matrix multiplication. The equality of the two results confirms the product-inverse property $(AB)^{-1}=B^{-1}A^{-1}$.

## Final answer (in words)

Both $(AB)^{-1}$ and $B^{-1}A^{-1}$ equal $\begin{pmatrix}\frac12&-\frac12\\0&\frac13\end{pmatrix}$.

## Verification

The two computed matrices are identical, and multiplying either by $AB$ gives $I$, confirming the inverse.

## Common mistakes

- Using the original order $A^{-1}B^{-1}$ instead of $B^{-1}A^{-1}$.
- Forgetting that matrix multiplication is not commutative.
- Arithmetic errors in the determinant.

## How I would explain it in class

To undo the composition $AB$, I undo $B$ first and then $A$, so the inverse is $B^{-1}A^{-1}$ with the order reversed. I compute both $(AB)^{-1}$ and $B^{-1}A^{-1}$ and they match. This shows why the order must be reversed when inverting a product.
