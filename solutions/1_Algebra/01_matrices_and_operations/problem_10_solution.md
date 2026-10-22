# Problem 10

## The original problem

Given

$$
A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&2\\-1&0\\3&1\end{pmatrix}.
$$

Denote the columns of $B$ by $b_1,b_2$.

1. Compute $Ab_1$ and $Ab_2$.
2. Compute the matrix $AB$.
3. Compare the results and explain why the columns of $AB$ are exactly the vectors $Ab_1$ and $Ab_2$.

> **Why this exercise:** extends the interpretation of matrix-vector multiplication to a full product of two matrices instead of simply repeating another $Ax$ exercise.

## What we are looking for

We need the two vectors $Ab_1$ and $Ab_2$, the full product $AB$, and a comparison showing that the first column of $AB$ is $Ab_1$ and the second column is $Ab_2$. We also have to explain why this is always so, not only here.

## The idea we need

The columns of $B$ are $b_1=\begin{pmatrix}1\\-1\\3\end{pmatrix}$ and $b_2=\begin{pmatrix}2\\0\\1\end{pmatrix}$. The product $Ab$ of a matrix and a vector is computed row by row: each entry is a row of $A$ multiplied entry by entry with $b$ and added. The product $AB$ is defined entry by entry as (row $i$ of $A$) times (column $j$ of $B$). These two definitions use the same sums, which is the key to part 3.

## Step-by-step solution

**Step 1: $Ab_1$ and $Ab_2$.** $A$ is $2\times3$ and each $b_j$ is $3\times1$, so each result has two entries.

$$
Ab_1=\begin{pmatrix}1\cdot1+2\cdot(-1)+0\cdot3\\0\cdot1+1\cdot(-1)+1\cdot3\end{pmatrix}=\begin{pmatrix}1-2+0\\0-1+3\end{pmatrix}=\begin{pmatrix}-1\\2\end{pmatrix},
$$

$$
Ab_2=\begin{pmatrix}1\cdot2+2\cdot0+0\cdot1\\0\cdot2+1\cdot0+1\cdot1\end{pmatrix}=\begin{pmatrix}2\\1\end{pmatrix}.
$$

**Step 2: the matrix $AB$.** $A$ is $2\times3$ and $B$ is $3\times2$, so $AB$ is $2\times2$. The four entries are:

- row 1, column 1: $1\cdot1+2\cdot(-1)+0\cdot3=-1$;
- row 1, column 2: $1\cdot2+2\cdot0+0\cdot1=2$;
- row 2, column 1: $0\cdot1+1\cdot(-1)+1\cdot3=2$;
- row 2, column 2: $0\cdot2+1\cdot0+1\cdot1=1$.

$$
AB=\begin{pmatrix}-1&2\\2&1\end{pmatrix}.
$$

**Step 3: compare.** The first column of $AB$ is $\begin{pmatrix}-1\\2\end{pmatrix}=Ab_1$ and the second column is $\begin{pmatrix}2\\1\end{pmatrix}=Ab_2$. So

$$
AB=\begin{pmatrix}Ab_1&Ab_2\end{pmatrix}.
$$

**Step 4: why.** Take the entry in row $i$ and column $j$ of $AB$. By the definition of the product it is the sum of (row $i$ of $A$) multiplied entry by entry with (column $j$ of $B$), that is, with $b_j$. But the same sum is the $i$-th entry of the vector $Ab_j$. So column $j$ of $AB$ has, in each row $i$, the same number as the vector $Ab_j$, and therefore column $j$ of $AB$ is $Ab_j$.

## Why each step is valid

- Sizes: a $2\times3$ matrix can multiply a vector with three entries, so $Ab_1$ and $Ab_2$ exist, and each has $2$ entries because $A$ has two rows.
- The entries of $AB$ are computed by the definition of the product, using the same sums as in step 1, which is why we can compare the results line by line.
- The argument in step 4 is general: it never used the particular numbers, so for any matrices $A$ and $B$ for which $AB$ is defined, column $j$ of $AB$ equals $A$ times column $j$ of $B$. This also shows that each column of $AB$ is a linear combination of the columns of $A$, with the entries of $b_j$ as coefficients.

## Final answer (in words)

$Ab_1=\begin{pmatrix}-1\\2\end{pmatrix}$ and $Ab_2=\begin{pmatrix}2\\1\end{pmatrix}$, and the product is $AB=\begin{pmatrix}-1&2\\2&1\end{pmatrix}$. The columns of $AB$ are exactly $Ab_1$ and $Ab_2$, because each entry of the product is the same row-times-column sum that is used to compute the matrix-vector product, so multiplying $A$ by $B$ means multiplying $A$ by each column of $B$ separately.

## Verification

I check with the column-combination point of view, which does not use row-times-column sums. The columns of $A$ are $a_1=\begin{pmatrix}1\\0\end{pmatrix}$, $a_2=\begin{pmatrix}2\\1\end{pmatrix}$, $a_3=\begin{pmatrix}0\\1\end{pmatrix}$. Then $Ab_1=1\cdot a_1+(-1)\cdot a_2+3\cdot a_3=\begin{pmatrix}1\\0\end{pmatrix}-\begin{pmatrix}2\\1\end{pmatrix}+\begin{pmatrix}0\\3\end{pmatrix}=\begin{pmatrix}-1\\2\end{pmatrix}$ and $Ab_2=2a_1+0a_2+1a_3=\begin{pmatrix}2\\0\end{pmatrix}+\begin{pmatrix}0\\1\end{pmatrix}=\begin{pmatrix}2\\1\end{pmatrix}$, both matching.

A second check uses linearity: $b_1+b_2=\begin{pmatrix}3\\-1\\4\end{pmatrix}$, so $A(b_1+b_2)=\begin{pmatrix}3-2+0\\-1+4\end{pmatrix}=\begin{pmatrix}1\\3\end{pmatrix}$, and $Ab_1+Ab_2=\begin{pmatrix}-1+2\\2+1\end{pmatrix}=\begin{pmatrix}1\\3\end{pmatrix}$, as it must be.

## Common mistakes

- Using the rows of $B$ instead of its columns when forming $b_1$ and $b_2$; the columns are $(1,-1,3)$ and $(2,0,1)$.
- Placing $Ab_2$ as the first column of $AB$, which reverses the order of the columns.
- Mixing up the roles of the two factors: here $A$ stands on the left and acts on the columns of $B$; the product $BA$ is a different matrix (of size $3\times3$).
- Believing that the equality of columns is a coincidence of these numbers.

## How I would explain it in class

To multiply $A$ by $B$, we multiply $A$ by each column of $B$ separately and put the results side by side: here $Ab_1=(-1,2)$ and $Ab_2=(2,1)$, so $AB=\begin{pmatrix}-1&2\\2&1\end{pmatrix}$. This is not a coincidence, because the entry of $AB$ in row $i$ and column $j$ is a row of $A$ times column $j$ of $B$, which is exactly the $i$-th entry of $Ab_j$. So a matrix product is just several matrix-vector products at once.
