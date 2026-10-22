# Problem 03

## The original problem

The matrix sizes are

$$
A_{2\times3},\qquad B_{3\times4},\qquad C_{4\times2},\qquad D_{2\times2}.
$$

For the products

$$
AB,\ BA,\ BC,\ CB,\ AC,\ CA,\ AD,\ DA
$$

determine whether they are defined. If so, state the size of the result. Justify each decision using the dimension compatibility condition.

> **Why this exercise:** forces an understanding of dimension compatibility before carrying out any calculation.

## What we are looking for

We need a yes/no decision for each of the eight products, and for the ones that are defined we need the size of the resulting matrix. Every decision must be justified by comparing the number of columns of the left matrix with the number of rows of the right matrix.

## The idea we need

The product of an $m \times n$ matrix and a $p \times q$ matrix is defined only when $n = p$, that is, when the number of columns of the first matrix equals the number of rows of the second. When it is defined, the result is an $m \times q$ matrix. This is the dimension compatibility condition, and it is the first check one must always perform before multiplying.

## Step-by-step solution

1. **$AB$.** $A$ is $2 \times 3$ and $B$ is $3 \times 4$. The inner dimensions are $3$ (columns of $A$) and $3$ (rows of $B$), which match, so $AB$ is defined and has size $2 \times 4$.
2. **$BA$.** $B$ is $3 \times 4$ and $A$ is $2 \times 3$. The inner dimensions are $4$ (columns of $B$) and $2$ (rows of $A$), and $4 \neq 2$, so $BA$ is **not defined**.
3. **$BC$.** $B$ is $3 \times 4$ and $C$ is $4 \times 2$. The inner dimensions are $4$ and $4$, which match, so $BC$ is defined and has size $3 \times 2$.
4. **$CB$.** $C$ is $4 \times 2$ and $B$ is $3 \times 4$. The inner dimensions are $2$ (columns of $C$) and $3$ (rows of $B$), and $2 \neq 3$, so $CB$ is **not defined**.
5. **$AC$.** $A$ is $2 \times 3$ and $C$ is $4 \times 2$. The inner dimensions are $3$ (columns of $A$) and $4$ (rows of $C$), and $3 \neq 4$, so $AC$ is **not defined**.
6. **$CA$.** $C$ is $4 \times 2$ and $A$ is $2 \times 3$. The inner dimensions are $2$ and $2$, which match, so $CA$ is defined and has size $4 \times 3$.
7. **$AD$.** $A$ is $2 \times 3$ and $D$ is $2 \times 2$. The inner dimensions are $3$ (columns of $A$) and $2$ (rows of $D$), and $3 \neq 2$, so $AD$ is **not defined**.
8. **$DA$.** $D$ is $2 \times 2$ and $A$ is $2 \times 3$. The inner dimensions are $2$ and $2$, which match, so $DA$ is defined and has size $2 \times 3$.

## Why each step is valid

- Each decision uses the dimension compatibility condition: the product of an $m \times n$ matrix and a $p \times q$ matrix exists exactly when $n = p$, and then the result is $m \times q$.
- For $AB$, $BC$, $CA$, and $DA$ the inner dimensions coincide ($3=3$, $4=4$, $2=2$, $2=2$), so the products exist and their sizes come from the outer dimensions.
- For $BA$, $CB$, $AC$, and $AD$ the inner dimensions differ ($4\neq2$, $2\neq3$, $3\neq4$, $3\neq2$), so the products are undefined; no computation is possible because the dot products required by the definition cannot be formed.

## Final answer (in words)

The defined products are $AB$ (size $2 \times 4$), $BC$ (size $3 \times 2$), $CA$ (size $4 \times 3$), and $DA$ (size $2 \times 3$). The products $BA$, $CB$, $AC$, and $AD$ are not defined because in each case the number of columns of the first matrix does not equal the number of rows of the second matrix.

## Verification

I rechecked each pair by writing the sizes side by side: for $AB$, $(2\times3)(3\times4)$ gives inner $3=3$ and outer $2\times4$; for $DA$, $(2\times2)(2\times3)$ gives inner $2=2$ and outer $2\times3$. The four undefined products were re-examined and in every case the two inner numbers are different, confirming that the dot product of a row of the left matrix with a column of the right matrix cannot be formed. The count of defined products (four) and undefined products (four) is consistent with the eight products asked for.

## Common mistakes

- Checking the outer dimensions instead of the inner dimensions when deciding whether a product is defined.
- Writing the size of a defined product as $n \times p$ (inner dimensions) instead of $m \times q$ (outer dimensions).
- Assuming that because $AB$ is defined, $BA$ must also be defined.
- Declaring a product defined when the inner dimensions match only after swapping the two matrices.

## How I would explain it in class

To multiply two matrices, the number of columns of the first must equal the number of rows of the second; if this inner pair matches, the product exists and the outer pair gives the size of the answer. When the inner numbers disagree, the product is simply not defined, because the dot products at the heart of the multiplication cannot be formed. This is why $AB$ can exist while $BA$ may not, and it is the first check you must always make before doing any calculation.
