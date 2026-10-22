# Problem 02

## The original problem

For

$$
A=\begin{pmatrix}1&2\\-1&3\end{pmatrix},\qquad B=\begin{pmatrix}4&-2\\0&5\end{pmatrix},
$$

compute

$$
A+B,\qquad A-B,\qquad 3A-2B.
$$

Explain why matrix addition is possible only for matrices of the same size.

> **Why this exercise:** reinforces entry-by-entry operations and the importance of compatible dimensions.

## What we are looking for

We need three resulting matrices: the sum $A+B$, the difference $A-B$, and the combination $3A-2B$. We also need a short explanation, in words, of why two matrices can be added only when they have the same number of rows and the same number of columns.

## The idea we need

Matrix addition and subtraction are defined entry by entry: for two $m \times n$ matrices $A=(a_{ij})$ and $B=(b_{ij})$, the sum is $A+B=(a_{ij}+b_{ij})$. Scalar multiplication multiplies every entry: $cA=(c\,a_{ij})$. Both operations require the two matrices to have the same size $m \times n$, because each entry of one matrix must pair with exactly one entry of the other at the same position.

## Step-by-step solution

1. **Check sizes.** Both $A$ and $B$ are $2 \times 2$ matrices, so addition and subtraction are defined.
2. **Compute $A+B$.** Add matching entries: $1+4=5$, $2+(-2)=0$, $-1+0=-1$, $3+5=8$. This gives
   $$A+B=\begin{pmatrix}5&0\\-1&8\end{pmatrix}.$$
3. **Compute $A-B$.** Subtract matching entries: $1-4=-3$, $2-(-2)=4$, $-1-0=-1$, $3-5=-2$. This gives
   $$A-B=\begin{pmatrix}-3&4\\-1&-2\end{pmatrix}.$$
4. **Compute $3A$.** Multiply every entry of $A$ by $3$: $3\cdot1=3$, $3\cdot2=6$, $3\cdot(-1)=-3$, $3\cdot3=9$, so $3A=\begin{pmatrix}3&6\\-3&9\end{pmatrix}$.
5. **Compute $2B$.** Multiply every entry of $B$ by $2$: $2\cdot4=8$, $2\cdot(-2)=-4$, $2\cdot0=0$, $2\cdot5=10$, so $2B=\begin{pmatrix}8&-4\\0&10\end{pmatrix}$.
6. **Compute $3A-2B$.** Subtract $2B$ from $3A$ entry by entry: $3-8=-5$, $6-(-4)=10$, $-3-0=-3$, $9-10=-1$. This gives
   $$3A-2B=\begin{pmatrix}-5&10\\-3&-1\end{pmatrix}.$$

## Why each step is valid

- Step 1: the size check is necessary because addition is only defined for matrices of identical dimensions; here both are $2 \times 2$, so the operation is legal.
- Steps 2–3: matrix addition/subtraction pairs entries with the same row and column indices, so the rule $(A\pm B)_{ij}=a_{ij}\pm b_{ij}$ applies directly.
- Steps 4–5: scalar multiplication multiplies each entry by the scalar, which is the definition of $cA$, and it preserves the size of the matrix.
- Step 6: $3A-2B$ is interpreted as $(3A)-(2B)$, and since $3A$ and $2B$ are both $2 \times 2$, their subtraction is again entry by entry.

## Final answer (in words)

The sum is $A+B=\begin{pmatrix}5&0\\-1&8\end{pmatrix}$, the difference is $A-B=\begin{pmatrix}-3&4\\-1&-2\end{pmatrix}$, and the combination is $3A-2B=\begin{pmatrix}-5&10\\-3&-1\end{pmatrix}$. Matrix addition is possible only for matrices of the same size because each entry of one matrix must pair with the entry in the same position of the other matrix, and this pairing exists only when the two matrices have the same number of rows and the same number of columns.

## Verification

I recomputed each result by a different grouping. For $A+B$ I added the columns of $A$ and $B$ separately: column 1 gives $(1+4,\,-1+0)=(5,-1)$ and column 2 gives $(2-2,\,3+5)=(0,8)$, which matches. For $3A-2B$ I checked the equivalent form $A + 2A - 2B$ entrywise and obtained the same numbers. I also verified that every resulting matrix is $2 \times 2$, consistent with the size of $A$ and $B$.

## Common mistakes

- Adding matrices of different sizes, for example treating a $2 \times 2$ matrix and a $2 \times 3$ matrix as addable.
- Subtracting in the wrong order, writing $A-B$ but computing $B-A$.
- Applying the scalar to only one term in $3A-2B$, for example computing $3A-2$ instead of $3A-2B$.
- Multiplying entries by the scalar in only one row or column.

## How I would explain it in class

Matrix addition works entry by entry, like adding two tables of numbers where each cell pairs with the cell in the same position of the other table. Because of this, the two tables must have the same number of rows and the same number of columns, otherwise some cells would have no partner. Scalar multiplication simply scales every cell, and $3A-2B$ means scale $A$ by $3$, scale $B$ by $2$, and then subtract the second scaled table from the first.
