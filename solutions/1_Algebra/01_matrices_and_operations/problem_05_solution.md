# Problem 05

## The original problem

Let

$$
A=\begin{pmatrix}2&-1\\1&3\end{pmatrix},\qquad x=\begin{pmatrix}4\\2\end{pmatrix}.
$$

Compute $Ax$. Then express $Ax$ as a linear combination of the columns of $A$, with coefficients coming from the vector $x$.

> **Why this exercise:** shows that multiplying a matrix by a vector can be understood as a linear combination of the matrix columns.

## What we are looking for

We need the product $Ax$, computed entry by entry, and then we need to rewrite that same vector as a combination of the two columns of $A$ where the coefficients are exactly the entries of $x$. Both forms must give the same numerical vector, which confirms the column interpretation.

## The idea we need

For an $m \times n$ matrix $A$ with columns $a_1, a_2, \dots, a_n$ and a vector $x = (x_1, \dots, x_n)^T$, the product satisfies
$$Ax = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n.$$
This is the column rule: matrix-vector multiplication is a linear combination of the columns of the matrix, weighted by the entries of the vector. The sizes must match: $A$ is $m \times n$ and $x$ must be $n \times 1$.

## Step-by-step solution

1. **Check sizes.** $A$ is $2 \times 2$ and $x$ is $2 \times 1$; the inner dimension $2$ matches, so $Ax$ is defined and will be a $2 \times 1$ vector.
2. **Compute the first entry of $Ax$.** Row 1 of $A$ is $(2,-1)$; dot it with $x$: $2\cdot4 + (-1)\cdot2 = 8 - 2 = 6$.
3. **Compute the second entry of $Ax$.** Row 2 of $A$ is $(1,3)$; dot it with $x$: $1\cdot4 + 3\cdot2 = 4 + 6 = 10$.
   Thus
   $$Ax = \begin{pmatrix}6\\10\end{pmatrix}.$$
4. **Identify the columns of $A$.** Column 1 is $a_1 = \begin{pmatrix}2\\1\end{pmatrix}$ and column 2 is $a_2 = \begin{pmatrix}-1\\3\end{pmatrix}$.
5. **Form the linear combination.** Using the entries of $x$ as coefficients, $x_1 = 4$ and $x_2 = 2$, we compute
   $$4a_1 + 2a_2 = 4\begin{pmatrix}2\\1\end{pmatrix} + 2\begin{pmatrix}-1\\3\end{pmatrix}.$$
6. **Evaluate the combination.** $4a_1 = \begin{pmatrix}8\\4\end{pmatrix}$ and $2a_2 = \begin{pmatrix}-2\\6\end{pmatrix}$; adding them gives $\begin{pmatrix}8-2\\4+6\end{pmatrix} = \begin{pmatrix}6\\10\end{pmatrix}$.

## Why each step is valid

- Steps 2–3: the entry-by-entry rule $(Ax)_i = \sum_j a_{ij}x_j$ is the definition of the matrix-vector product, and it applies because the number of columns of $A$ equals the number of rows of $x$.
- Steps 4–6: the column rule $Ax = x_1 a_1 + \cdots + x_n a_n$ is an equivalent restatement of the same definition; expanding the sum reproduces exactly the two dot products computed above, so the two computations must agree.

## Final answer (in words)

The product is $Ax = \begin{pmatrix}6\\10\end{pmatrix}$, and it can be written as the linear combination $4\begin{pmatrix}2\\1\end{pmatrix} + 2\begin{pmatrix}-1\\3\end{pmatrix}$, where the coefficients $4$ and $2$ are the entries of $x$. This shows that multiplying a matrix by a vector is the same as taking a weighted combination of the matrix's columns.

## Verification

I checked the column combination independently of the entry-by-entry computation: $4\cdot(2,1) = (8,4)$ and $2\cdot(-1,3) = (-2,6)$, and $(8,4) + (-2,6) = (6,10)$, which matches $Ax$ exactly. I also recomputed the two dot products once more: $2\cdot4 + (-1)\cdot2 = 6$ and $1\cdot4 + 3\cdot2 = 10$, confirming the same result.

## Common mistakes

- Multiplying the vector on the left, writing $xA$ instead of $Ax$, which is not defined for a $2 \times 2$ matrix and a $2 \times 1$ vector in that order.
- Using the rows of $A$ as coefficients instead of the columns.
- Taking the coefficients from the matrix entries rather than from the vector $x$.
- Writing the combination as $x_1 a_1 + x_2 a_2$ but computing $a_1$ and $a_2$ from the wrong matrix.

## How I would explain it in class

I first compute $Ax$ entry by entry, which gives the vector $(6,10)$. Then I notice that the same vector is obtained by taking $4$ times the first column of $A$ plus $2$ times the second column, where $4$ and $2$ are exactly the entries of $x$. This means multiplying a matrix by a vector is just a weighted sum of the matrix's columns, with the vector supplying the weights.
