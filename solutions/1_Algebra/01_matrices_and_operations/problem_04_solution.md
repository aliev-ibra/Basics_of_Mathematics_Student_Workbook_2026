# Problem 04

## The original problem

For

$$
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}2&0\\3&1\end{pmatrix},
$$

compute $AB$ and $BA$. Is $AB=BA$? Use this example to explain what noncommutativity of matrix multiplication means.

> **Why this exercise:** shows one of the most important differences between matrix multiplication and multiplication of numbers.

## What we are looking for

We need the two products $AB$ and $BA$, a yes/no answer to whether they are equal, and a clear verbal explanation of what "noncommutative" means, using this concrete example as evidence.

## The idea we need

Matrix multiplication is defined by $(AB)_{ij} = \sum_k a_{ik}b_{kj}$: the $(i,j)$ entry of the product is the dot product of row $i$ of $A$ with column $j$ of $B$. The sizes must be compatible (inner dimensions equal). Unlike multiplication of ordinary numbers, in general $AB \neq BA$; this is called noncommutativity, and it means the order in which matrices are multiplied changes the result.

## Step-by-step solution

1. **Check sizes.** Both $A$ and $B$ are $2 \times 2$, so both $AB$ and $BA$ are defined and each result is $2 \times 2$.
2. **Compute $AB$, entry (1,1).** Row 1 of $A$ is $(1,2)$, column 1 of $B$ is $(2,3)$. Dot product: $1\cdot2 + 2\cdot3 = 2 + 6 = 8$.
3. **Compute $AB$, entry (1,2).** Row 1 of $A$ is $(1,2)$, column 2 of $B$ is $(0,1)$. Dot product: $1\cdot0 + 2\cdot1 = 0 + 2 = 2$.
4. **Compute $AB$, entry (2,1).** Row 2 of $A$ is $(0,1)$, column 1 of $B$ is $(2,3)$. Dot product: $0\cdot2 + 1\cdot3 = 0 + 3 = 3$.
5. **Compute $AB$, entry (2,2).** Row 2 of $A$ is $(0,1)$, column 2 of $B$ is $(0,1)$. Dot product: $0\cdot0 + 1\cdot1 = 0 + 1 = 1$.
   Thus
   $$AB = \begin{pmatrix}8&2\\3&1\end{pmatrix}.$$
6. **Compute $BA$, entry (1,1).** Row 1 of $B$ is $(2,0)$, column 1 of $A$ is $(1,0)$. Dot product: $2\cdot1 + 0\cdot0 = 2$.
7. **Compute $BA$, entry (1,2).** Row 1 of $B$ is $(2,0)$, column 2 of $A$ is $(2,1)$. Dot product: $2\cdot2 + 0\cdot1 = 4$.
8. **Compute $BA$, entry (2,1).** Row 2 of $B$ is $(3,1)$, column 1 of $A$ is $(1,0)$. Dot product: $3\cdot1 + 1\cdot0 = 3$.
9. **Compute $BA$, entry (2,2).** Row 2 of $B$ is $(3,1)$, column 2 of $A$ is $(2,1)$. Dot product: $3\cdot2 + 1\cdot1 = 6 + 1 = 7$.
   Thus
   $$BA = \begin{pmatrix}2&4\\3&7\end{pmatrix}.$$
10. **Compare.** $AB$ has top-left entry $8$ while $BA$ has top-left entry $2$, so the two matrices are different. Therefore $AB \neq BA$.

## Why each step is valid

- Steps 2–9: each entry is computed using the definition $(XY)_{ij} = \text{row}_i(X) \cdot \text{column}_j(Y)$, which is the standard rule for matrix multiplication; the sizes $2 \times 2$ make every dot product a sum of two products.
- Step 10: two matrices are equal only when all corresponding entries match; since entry (1,1) already differs ($8 \neq 2$), the matrices are not equal, which is sufficient to conclude $AB \neq BA$.

## Final answer (in words)

We obtain $AB = \begin{pmatrix}8&2\\3&1\end{pmatrix}$ and $BA = \begin{pmatrix}2&4\\3&7\end{pmatrix}$, and they are not equal. This example shows that matrix multiplication is noncommutative: swapping the order of the factors changes the result, so, unlike with ordinary numbers, we cannot assume $AB = BA$ for matrices.

## Verification

I recomputed both products using a different grouping of the arithmetic. For $AB$, column-wise: column 1 of $AB$ is $A$ times column 1 of $B$, giving $1\cdot(2,3) + 2\cdot(1,0)$... more simply, I rechecked each dot product by hand and obtained the same four numbers. For $BA$ I verified the (2,2) entry as $3\cdot2 + 1\cdot1 = 7$ independently. The inequality is clear from the differing (1,1) entries, $8$ versus $2$.

## Common mistakes

- Writing the dot product as $a_{i1}b_{1j} + a_{i2}b_{2j}$ but mixing up which matrix supplies the row and which supplies the column.
- Computing $BA$ by reusing the numbers from $AB$ instead of swapping the roles of $A$ and $B$.
- Concluding that $AB = BA$ just because the two results look similar or because multiplication of numbers is commutative.
- Writing the product size incorrectly when the matrices are not square.

## How I would explain it in class

I multiply $A$ and $B$ in the order $AB$ and then in the reverse order $BA$, and the two answers are different matrices. This means matrix multiplication is noncommutative: the order matters, so $AB$ is not automatically equal to $BA$, unlike the multiplication of ordinary numbers where order does not matter.
