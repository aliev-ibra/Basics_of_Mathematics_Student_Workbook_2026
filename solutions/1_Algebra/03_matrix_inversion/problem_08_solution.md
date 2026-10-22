# Problem 08

## The original problem

The matrix
$$S=\begin{pmatrix}2&0\\0&\frac12\end{pmatrix}$$
describes a scaling of the plane. Find $S^{-1}$ and explain geometrically what the inverse transformation does. Check the action of the pair $S,S^{-1}$ on one simple vector.

## What we are looking for

We need the inverse of the diagonal scaling matrix $S$, a geometric description of what it does, and a check on a chosen vector.

## The idea we need

For a diagonal matrix, the inverse is obtained by inverting each diagonal entry: if $D=\mathrm{diag}(d_1,\dots,d_n)$ with all $d_i\neq0$, then $D^{-1}=\mathrm{diag}(1/d_1,\dots,1/d_n)$. Geometrically, the inverse undoing a scaling by factors $2$ and $\frac12$ scales by the reciprocals $\frac12$ and $2$.

## Step-by-step solution

1. $S$ is diagonal with entries $2$ and $\frac12$, both nonzero, so it is invertible.
2. Invert each diagonal entry:
$$S^{-1}=\begin{pmatrix}\frac12&0\\0&2\end{pmatrix}.$$

3. Geometric meaning: $S$ stretches the $x$-coordinate by $2$ and shrinks the $y$-coordinate by $\frac12$. Its inverse $S^{-1}$ shrinks the $x$-coordinate by $\frac12$ and stretches the $y$-coordinate by $2$, exactly undoing $S$.

4. Check on the vector $v=\begin{pmatrix}1\\1\end{pmatrix}$:
$$Sv=\begin{pmatrix}2\\ \frac12\end{pmatrix},\qquad
S^{-1}(Sv)=\begin{pmatrix}\frac12&0\\0&2\end{pmatrix}\begin{pmatrix}2\\ \frac12\end{pmatrix}
=\begin{pmatrix}1\\1\end{pmatrix}=v.$$

## Why each step is valid

A diagonal matrix is invertible exactly when all diagonal entries are nonzero, and its inverse is diagonal with reciprocal entries. Composing $S^{-1}$ after $S$ gives the identity, which is the defining property of an inverse transformation.

## Final answer (in words)

$S^{-1}=\begin{pmatrix}\frac12&0\\0&2\end{pmatrix}$; geometrically it undoes the scaling by scaling $x$ by $\frac12$ and $y$ by $2$.

## Verification

On $v=(1,1)$, applying $S$ gives $(2,\frac12)$ and applying $S^{-1}$ returns $(1,1)$, so the pair acts as the identity.

## Common mistakes

- Inverting the matrix by negating instead of taking reciprocals.
- Forgetting that a zero diagonal entry would make the matrix singular.
- Confusing which coordinate gets which scale factor.

## How I would explain it in class

The matrix scales $x$ by $2$ and $y$ by $\frac12$, so the inverse must scale $x$ by $\frac12$ and $y$ by $2$. I write the inverse by taking reciprocals on the diagonal. Then I test it on the vector $(1,1)$: after $S$ and $S^{-1}$ I get $(1,1)$ back, so the inverse truly undoes the transformation.
