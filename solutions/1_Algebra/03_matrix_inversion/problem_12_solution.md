# Problem 12

## The original problem

It is known that
$$A^{-1}=\begin{pmatrix}2&-1\\-3&2\end{pmatrix}.$$
Without finding $A$, compute $(3A)^{-1}$, $(A^T)^{-1}$, and $(A^2)^{-1}$. Justify each result using the appropriate property.

## What we are looking for

Three inverses, each of which is built from the single known matrix $A^{-1}$ by a rule, without ever computing $A$ itself. For each we must name the property of the inverse that we use.

## The idea we need

Three rules, valid whenever $A$ is an invertible square matrix:

- Scalar rule: for a number $k\neq0$, $(kA)^{-1}=\dfrac1k A^{-1}$, because $(kA)\left(\frac1kA^{-1}\right)=\left(k\cdot\frac1k\right)AA^{-1}=I$.
- Transpose rule: $(A^T)^{-1}=(A^{-1})^T$, because $A^T(A^{-1})^T=(A^{-1}A)^T=I^T=I$.
- Product (power) rule: $(A^2)^{-1}=(AA)^{-1}=A^{-1}A^{-1}=(A^{-1})^2$, because the inverse of a product reverses the order of the factors and here both factors are the same.

Here $A^T$ is the transpose of $A$ (rows and columns exchanged), and $I$ is the identity matrix. Note that $A^{-1}$ is given, so $A$ exists and is invertible.

## Step-by-step solution

Write $C=A^{-1}=\begin{pmatrix}2&-1\\-3&2\end{pmatrix}$.

**Step 1: $(3A)^{-1}$.** By the scalar rule with $k=3$ we multiply $C$ by $\frac13$:
$$(3A)^{-1}=\frac13C=\begin{pmatrix}\frac23&-\frac13\\-1&\frac23\end{pmatrix}.$$

**Step 2: $(A^T)^{-1}$.** By the transpose rule we transpose $C$, that is, swap the off-diagonal entries $-1$ and $-3$:
$$(A^T)^{-1}=C^T=\begin{pmatrix}2&-3\\-1&2\end{pmatrix}.$$

**Step 3: $(A^2)^{-1}$.** By the product rule we square $C$:
$$(A^2)^{-1}=C^2=\begin{pmatrix}2&-1\\-3&2\end{pmatrix}\begin{pmatrix}2&-1\\-3&2\end{pmatrix}
=\begin{pmatrix}4+3&-2-2\\-6-6&3+4\end{pmatrix}=\begin{pmatrix}7&-4\\-12&7\end{pmatrix}.$$

## Why each step is valid

- Scalar rule: scaling $A$ by $3$ scales every output by $3$, so to undo it we must also scale by $\frac13$; the displayed one-line proof shows $(3A)\cdot\frac13A^{-1}=I$, and the inverse is unique, so this is the inverse.
- Transpose rule: transposing reverses the order of a product, $(PQ)^T=Q^TP^T$, so $A^T(A^{-1})^T=(A^{-1}A)^T=I$; again uniqueness of the inverse finishes the argument. The inverse of the transpose is the transpose of the inverse, so the two operations can be swapped.
- Power rule: $(A^2)(A^{-1})^2=A\,(AA^{-1})\,A^{-1}=AA^{-1}=I$, which uses associativity of multiplication only.
- In all three cases we exhibit a matrix that multiplies to $I$ and rely on the fact that an inverse is unique.

## Final answer (in words)

The inverse of $3A$ is one third of $A^{-1}$, the inverse of $A^T$ is the transpose of $A^{-1}$, and the inverse of $A^2$ is the square of $A^{-1}$:
$$(3A)^{-1}=\begin{pmatrix}\frac23&-\frac13\\-1&\frac23\end{pmatrix},\qquad
(A^T)^{-1}=\begin{pmatrix}2&-3\\-1&2\end{pmatrix},\qquad
(A^2)^{-1}=\begin{pmatrix}7&-4\\-12&7\end{pmatrix}.$$

## Verification

As an independent check I recover $A$ from the given inverse: $\det A^{-1}=2\cdot2-(-1)(-3)=1$, so $A=\begin{pmatrix}2&1\\3&2\end{pmatrix}$ (swap the diagonal, change the signs of the off-diagonal entries, divide by $1$). Now multiply directly:
$$(3A)\,(3A)^{-1}=\begin{pmatrix}6&3\\9&6\end{pmatrix}\begin{pmatrix}\frac23&-\frac13\\-1&\frac23\end{pmatrix}=\begin{pmatrix}4-3&-2+2\\6-6&-3+4\end{pmatrix}=I,$$
$$A^T(A^T)^{-1}=\begin{pmatrix}2&3\\1&2\end{pmatrix}\begin{pmatrix}2&-3\\-1&2\end{pmatrix}=\begin{pmatrix}4-3&-6+6\\2-2&-3+4\end{pmatrix}=I,$$
$$A^2=\begin{pmatrix}2&1\\3&2\end{pmatrix}^2=\begin{pmatrix}7&4\\12&7\end{pmatrix},\qquad A^2(A^2)^{-1}=\begin{pmatrix}7&4\\12&7\end{pmatrix}\begin{pmatrix}7&-4\\-12&7\end{pmatrix}=\begin{pmatrix}49-48&-28+28\\84-84&-48+49\end{pmatrix}=I.$$

## Common mistakes

- Writing $(3A)^{-1}=3A^{-1}$; the factor must be inverted too, giving $\frac13$.
- Forgetting to transpose in the second part, or transposing and also inverting again.
- Computing $(A^2)^{-1}$ as $2A^{-1}$ or as $A^{-1}$ with entries squared; it is the matrix product $A^{-1}A^{-1}$.
- Doing a full inversion of $3A$ or $A^2$ from scratch; that is correct but wastes the information given.

## How I would explain it in class

Each of the three inverses can be read off from $A^{-1}$ by one rule: scaling by $3$ is undone by scaling by $\frac13$, the inverse of a transpose is the transpose of the inverse, and the inverse of $A^2$ is $A^{-1}A^{-1}$. This gives $\begin{pmatrix}\frac23&-\frac13\\-1&\frac23\end{pmatrix}$, $\begin{pmatrix}2&-3\\-1&2\end{pmatrix}$ and $\begin{pmatrix}7&-4\\-12&7\end{pmatrix}$. I checked all three by recovering $A=\begin{pmatrix}2&1\\3&2\end{pmatrix}$ and multiplying each matrix by its claimed inverse to get $I$.
