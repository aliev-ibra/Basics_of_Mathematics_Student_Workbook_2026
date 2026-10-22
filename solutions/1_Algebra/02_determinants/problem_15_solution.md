# Problem 15

## The original problem

Let $A$ and $B$ be invertible $2\times2$ matrices with
$$
\det A=-2,\qquad \det B=3.
$$
Without finding the entries of the matrices, compute
$$
\det\left(B^{-1}A^TB\right).
$$
State the determinant properties you use in order and explain why the factors involving $B$ eventually cancel.

## What we are looking for

We want one number, the determinant of the product $B^{-1}A^TB$, where $A^T$ is the transpose of $A$ (rows and columns swapped) and $B^{-1}$ is the inverse of $B$. We know only the determinants of $A$ and $B$, so the answer must come from rules, not from entries.

## The idea we need

Three properties of the determinant of square matrices of the same size:

1. **Product rule:** $\det(XY)=\det X\cdot\det Y$.
2. **Transpose rule:** $\det(X^T)=\det X$.
3. **Inverse rule:** $\det(X^{-1})=\dfrac{1}{\det X}$ for an invertible matrix $X$.

The third rule follows from the first: $\det(X)\det(X^{-1})=\det(XX^{-1})=\det I=1$.

## Step-by-step solution

**Step 1: split the product.** By the product rule applied to the three factors,
$$
\det\left(B^{-1}A^TB\right)=\det\left(B^{-1}\right)\cdot\det\left(A^T\right)\cdot\det(B).
$$

**Step 2: inverse rule.** $\det\left(B^{-1}\right)=\dfrac{1}{\det B}=\dfrac13$.

**Step 3: transpose rule.** $\det\left(A^T\right)=\det A=-2$.

**Step 4: substitute the numbers.**
$$
\det\left(B^{-1}A^TB\right)=\frac13\cdot(-2)\cdot3=-2.
$$

**Step 5: why $B$ cancels.** Numbers multiply in any order, so the factors $\det(B^{-1})=\frac{1}{\det B}$ and $\det B$ multiply to $\frac{1}{\det B}\cdot\det B=1$. Only $\det A^T=\det A$ is left.

## Why each step is valid

- The product rule holds for any two square matrices of the same size, and we apply it twice (to a product of three matrices). It does not require the matrices to commute, which matters because $B^{-1}A^TB$ is in general not equal to $A^T$.
- The transpose rule holds because a determinant has the same value when computed along rows or along columns.
- The inverse rule needs $B$ to be invertible, which is given, and it is also why $\det B\neq0$ and the fraction $\frac13$ makes sense.
- The determinants are ordinary numbers, and ordinary numbers commute, so we may bring $\det B^{-1}$ and $\det B$ next to each other even though the matrices themselves cannot be moved.

## Final answer (in words)

The determinant of $B^{-1}A^TB$ equals $-2$. The factor from $B^{-1}$ is $\frac13$ and the factor from $B$ is $3$, so they cancel to $1$, and what remains is $\det A^T=\det A=-2$.

$$
\det\left(B^{-1}A^TB\right)=\det A=-2.
$$

## Verification

I test the result on concrete matrices that are not related to the argument above. Take $A=\begin{pmatrix}1&1\\0&-2\end{pmatrix}$, with $\det A=-2$, and $B=\begin{pmatrix}3&1\\0&1\end{pmatrix}$, with $\det B=3$. Then $A^T=\begin{pmatrix}1&0\\1&-2\end{pmatrix}$, $B^{-1}=\begin{pmatrix}\frac13&-\frac13\\0&1\end{pmatrix}$, and
$$
B^{-1}A^TB=\begin{pmatrix}0&\frac23\\3&-1\end{pmatrix},
$$
whose determinant is $0\cdot(-1)-\frac23\cdot3=-2$. This agrees with the answer. A second pair, $A=\begin{pmatrix}0&1\\2&1\end{pmatrix}$ and $B=\begin{pmatrix}1&2\\1&5\end{pmatrix}$, also has $\det A=-2$ and $\det B=3$ and also gives $-2$ when computed by computer algebra.

## Common mistakes

- Writing $B^{-1}A^TB=A^T$ and cancelling the matrices. Matrices do not commute, so this is false in general, even though the determinants do cancel.
- Using $\det(A^T)=-\det A$ or forgetting the transpose rule and inventing a sign.
- Writing $\det(B^{-1})=-3$ or $\det(B^{-1})=3$ instead of $\frac13$.
- Using the sum rule: the determinant of a sum is not the sum of determinants, and this problem only involves products.

## How I would explain it in class

The determinant of a product is the product of the determinants, so the expression splits into $\det(B^{-1})\cdot\det(A^T)\cdot\det(B)$, which equals $\frac13\cdot(-2)\cdot3$. The two factors coming from $B$ are a number and its reciprocal, so they cancel, and the transpose does not change the determinant, leaving $-2$. I checked this on explicit matrices with the same determinants, and the answer $-2$ came out both times.
