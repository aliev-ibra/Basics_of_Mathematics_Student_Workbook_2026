# Problem 01

## The original problem

Given

$$
A=\begin{pmatrix}2&-1&3\\0&4&5\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\-2&3\\4&1\end{pmatrix}.
$$

1. State the sizes of matrices $A$ and $B$.
2. Read off the entries $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

> **Why this exercise:** builds basic fluency with matrix notation, indices, rows, and columns.

## What we are looking for

We need to describe how big each matrix is, pull out four specific numbered entries, and write one whole row of $A$ and one whole column of $B$ as vectors. The answers are just readings from the given arrays, but they must be stated with correct notation and correct dimensions.

## The idea we need

A matrix size is written as $m \times n$, where $m$ is the number of rows and $n$ is the number of columns. The notation $a_{ij}$ means the entry sitting in row $i$ and column $j$ (row index first, column index second). A row is written horizontally as a $1 \times n$ vector, and a column is written vertically as an $m \times 1$ vector. These rules apply to every matrix, regardless of its entries.

## Step-by-step solution

1. **Size of $A$.** Matrix $A$ has $2$ rows and $3$ columns, so we write $A$ is $2 \times 3$.
2. **Size of $B$.** Matrix $B$ has $3$ rows and $2$ columns, so we write $B$ is $3 \times 2$.
3. **Entry $a_{12}$.** In $A$, row 1 is $(2,-1,3)$ and column 2 is $(-1,4)$; their intersection is $-1$. Hence $a_{12} = -1$.
4. **Entry $a_{23}$.** Row 2 of $A$ is $(0,4,5)$ and column 3 is $(3,5)$; their intersection is $5$. Hence $a_{23} = 5$.
5. **Entry $b_{21}$.** In $B$, row 2 is $(-2,3)$ and column 1 is $(1,-2,4)$; their intersection is $-2$. Hence $b_{21} = -2$.
6. **Entry $b_{32}$.** Row 3 of $B$ is $(4,1)$ and column 2 is $(0,3,1)$; their intersection is $1$. Hence $b_{32} = 1$.
7. **Second row of $A$.** Take row 2 of $A$ as a horizontal vector: $\begin{pmatrix}0&4&5\end{pmatrix}$.
8. **First column of $B$.** Take column 1 of $B$ as a vertical vector: $\begin{pmatrix}1\\-2\\4\end{pmatrix}$.

## Why each step is valid

- Steps 1–2: the size $m \times n$ is defined by counting rows first, then columns; this is the standard convention and it tells us which indices are legal for each matrix.
- Steps 3–6: the definition $a_{ij} =$ entry in row $i$, column $j$ lets us locate each requested number directly; for example $a_{23}$ exists because $A$ has at least $2$ rows and $3$ columns, and $b_{32}$ exists because $B$ has at least $3$ rows and $2$ columns.
- Steps 7–8: a row of an $m \times n$ matrix is a $1 \times n$ vector and a column is an $m \times 1$ vector, so the second row of $A$ has $3$ entries and the first column of $B$ has $3$ entries, matching their dimensions.

## Final answer (in words)

$A$ is a $2 \times 3$ matrix and $B$ is a $3 \times 2$ matrix. The requested entries are $a_{12} = -1$, $a_{23} = 5$, $b_{21} = -2$, and $b_{32} = 1$. The second row of $A$ is the row vector $(0,4,5)$, and the first column of $B$ is the column vector $(1,-2,4)^T$.

## Verification

I re-read each entry from the printed arrays: in $A$, position (1,2) is $-1$ and position (2,3) is $5$; in $B$, position (2,1) is $-2$ and position (3,2) is $1$. The row count and column count were checked independently by counting the rows of each matrix (2 for $A$, 3 for $B$) and the entries in the first row of each (3 for $A$, 2 for $B$). The second row of $A$ contains three entries and the first column of $B$ contains three entries, which agrees with the sizes $2 \times 3$ and $3 \times 2$.

## Common mistakes

- Writing the size as $n \times m$ (columns first, rows second) instead of $m \times n$.
- Interpreting $a_{ij}$ as column $i$, row $j$ instead of row $i$, column $j$.
- Asking for an entry that does not exist, for example $a_{31}$ in a $2 \times 3$ matrix.
- Writing a row vertically or a column horizontally, which changes the dimension of the vector.

## How I would explain it in class

I identify a matrix size by counting rows first and columns second, so $A$ is $2 \times 3$ and $B$ is $3 \times 2$. The notation $a_{ij}$ means row $i$, column $j$, so I can read off each requested entry directly from the correct position. Finally, the second row of $A$ is written horizontally with three entries and the first column of $B$ is written vertically with three entries, which matches their dimensions.
