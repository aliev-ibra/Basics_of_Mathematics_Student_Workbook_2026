# Problem 15

## The original problem

Given

$$
A=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix},\quad B=\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix},\quad C=\begin{pmatrix}2&1\\0&-1\end{pmatrix}.
$$

Compute $(AB)C$ and $A(BC)$. Compare the results and the number of intermediate operations. Explain what associativity of matrix multiplication means in this example.

> **Why this exercise:** reinforces associativity by comparing two mathematically equivalent calculation paths.

## What we are looking for

We need the matrix $(AB)C$ (multiply $A$ and $B$ first, then multiply by $C$) and the matrix $A(BC)$ (multiply $B$ and $C$ first, then multiply $A$ by the result). Then we compare the two final matrices and count how many multiplications of numbers each path needed, and say what associativity means here.

## The idea we need

Matrix multiplication is associative: $(AB)C=A(BC)$ whenever the sizes allow the products. It does not say that the intermediate matrices are equal, only that the final results are. The size of the matrices determines the work: an $m\times n$ matrix times an $n\times p$ matrix needs $m\cdot n\cdot p$ multiplications of numbers (each of the $m\cdot p$ entries needs $n$ products).

Sizes here: $A$ is $2\times3$, $B$ is $3\times2$, $C$ is $2\times2$.

## Step-by-step solution

**Step 1: path one, $AB$.** The result is $2\times2$:

- row 1, column 1: $1\cdot1+2\cdot2+0\cdot(-1)=5$;
- row 1, column 2: $1\cdot0+2\cdot1+0\cdot3=2$;
- row 2, column 1: $0\cdot1+1\cdot2+1\cdot(-1)=1$;
- row 2, column 2: $0\cdot0+1\cdot1+1\cdot3=4$.

$$
AB=\begin{pmatrix}5&2\\1&4\end{pmatrix}.
$$

**Step 2: path one, $(AB)C$.**

$$
(AB)C=\begin{pmatrix}5&2\\1&4\end{pmatrix}\begin{pmatrix}2&1\\0&-1\end{pmatrix}=\begin{pmatrix}5\cdot2+2\cdot0&5\cdot1+2\cdot(-1)\\1\cdot2+4\cdot0&1\cdot1+4\cdot(-1)\end{pmatrix}=\begin{pmatrix}10&3\\2&-3\end{pmatrix}.
$$

**Step 3: path two, $BC$.** $B$ is $3\times2$ and $C$ is $2\times2$, so $BC$ is $3\times2$:

- row 1 $(1,0)$: $1\cdot2+0\cdot0=2$ and $1\cdot1+0\cdot(-1)=1$;
- row 2 $(2,1)$: $2\cdot2+1\cdot0=4$ and $2\cdot1+1\cdot(-1)=1$;
- row 3 $(-1,3)$: $-1\cdot2+3\cdot0=-2$ and $-1\cdot1+3\cdot(-1)=-4$.

$$
BC=\begin{pmatrix}2&1\\4&1\\-2&-4\end{pmatrix}.
$$

**Step 4: path two, $A(BC)$.**

$$
A(BC)=\begin{pmatrix}1&2&0\\0&1&1\end{pmatrix}\begin{pmatrix}2&1\\4&1\\-2&-4\end{pmatrix}=\begin{pmatrix}2+8+0&1+2+0\\0+4-2&0+1-4\end{pmatrix}=\begin{pmatrix}10&3\\2&-3\end{pmatrix}.
$$

**Step 5: compare the results.** Both paths give

$$
(AB)C=A(BC)=\begin{pmatrix}10&3\\2&-3\end{pmatrix}.
$$

**Step 6: count the multiplications of numbers.**

- Path one: $AB$ is $(2\times3)(3\times2)$, so $2\cdot3\cdot2=12$ products; then $(AB)C$ is $(2\times2)(2\times2)$, so $2\cdot2\cdot2=8$ products. Total $20$.
- Path two: $BC$ is $(3\times2)(2\times2)$, so $3\cdot2\cdot2=12$ products; then $A(BC)$ is $(2\times3)(3\times2)$, so $2\cdot3\cdot2=12$ products. Total $24$.

The additions are counted similarly, and path one is also the cheaper one in additions.

**Step 7: what associativity means.** The two calculation paths have different intermediate matrices ($AB$ is $2\times2$, $BC$ is $3\times2$) and different amounts of work ($20$ against $24$ multiplications), but the final matrix is the same. Associativity means that we may place the brackets wherever we like, so the product $ABC$ without brackets is meaningful and we can choose the cheaper order.

## Why each step is valid

- The sizes are compatible in both orders: $AB$ is defined because $A$ has three columns and $B$ has three rows, and $(AB)C$ because $AB$ has two columns and $C$ has two rows; similarly $BC$ and $A(BC)$.
- Every entry was computed with the row-times-column rule, so each of the four matrices is determined by the definition and nothing else is assumed.
- The equality of the final answers is guaranteed by the general theorem on associativity: the entry of either product is $\sum_{j,k}a_{ij}b_{jk}c_{kl}$, the sum over all index chains, which does not depend on how the products are grouped. Our numbers confirm the theorem in this case; they do not replace it.
- The operation count follows from the size rule: each of the $m\cdot p$ entries of the product needs $n$ multiplications.

## Final answer (in words)

Both orders of calculation give the same matrix:

$$
(AB)C=A(BC)=\begin{pmatrix}10&3\\2&-3\end{pmatrix}.
$$

The first path needs $20$ multiplications of numbers and the second needs $24$, so the intermediate steps differ but the result is the same; this is what associativity means: the brackets can be placed freely without changing the product, and one may choose the cheaper grouping.

## Verification

I test the result with the vector $v=(1,1)^T$ without using the matrices $AB$ or $BC$. First $Cv=(2+1,\;0-1)^T=(3,-1)^T$. Then $B(3,-1)^T=(3,\;6-1,\;-3-3)^T=(3,5,-6)^T$. Then $A(3,5,-6)^T=(3+10+0,\;0+5-6)^T=(13,-1)^T$. Using the answer, $\begin{pmatrix}10&3\\2&-3\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}13\\-1\end{pmatrix}$, which matches. A second check uses determinants of the square matrices: $\det(AB)=5\cdot4-2\cdot1=18$ and $\det C=2\cdot(-1)-0=-2$, so the determinant of the product must be $18\cdot(-2)=-36$; the computed matrix has determinant $10\cdot(-3)-3\cdot2=-36$.

## Common mistakes

- Multiplying in the wrong order, for example computing $CB$, which is not defined ($C$ has two columns, $B$ has three rows).
- Expecting the intermediate matrices $AB$ and $BC$ to be equal or to have the same size; only the final results are guaranteed to agree.
- Confusing associativity with commutativity; the order of the factors $A,B,C$ is never changed, only the brackets.
- Counting only the number of matrix products (two in each path) and concluding that the work is identical.

## How I would explain it in class

We calculated the product in two ways, $(AB)C$ and $A(BC)$, and both gave $\begin{pmatrix}10&3\\2&-3\end{pmatrix}$, although the intermediate matrices $AB$ and $BC$ were different and had different sizes. Associativity means that the brackets can be put anywhere without changing the final answer, as long as the order of the factors stays the same. In this example the first path needed $20$ multiplications of numbers and the second $24$, so we may choose the cheaper grouping.
