## Problem Statement

Given

$$
A=\begin{pmatrix}2&-1&3\\0&4&5\end{pmatrix},\qquad
B=\begin{pmatrix}1&0\\-2&3\\4&1\end{pmatrix}.
$$

1. State the sizes of $A$ and $B$.
2. Find $a_{12}$, $a_{23}$, $b_{21}$, and $b_{32}$.
3. Write the second row of $A$ and the first column of $B$ as vectors.

## Theoretical Background and Concepts

The size of a matrix is written as

$$
	ext{number of rows}\times\text{number of columns}.
$$

The entry $a_{ij}$ is the element in row $i$ and column $j$. A row vector is written horizontally, while a column vector is written vertically.

## Detailed Step-by-Step Solution

### 1. Matrix sizes

Matrix $A$ has 2 rows and 3 columns, so

$$
A\text{ is }2\times3.
$$

Matrix $B$ has 3 rows and 2 columns, so

$$
B\text{ is }3\times2.
$$

### 2. Selected entries

Reading the indicated row and column positions gives

$$
a_{12}=-1,\qquad a_{23}=5,
$$

and

$$
b_{21}=-2,\qquad b_{32}=1.
$$

### 3. Row and column vectors

The second row of $A$ is

$$
\begin{pmatrix}0&4&5\end{pmatrix}.
$$

The first column of $B$ is

$$
\begin{pmatrix}1\\-2\\4\end{pmatrix}.
$$

## Verification and Consistency Checks

The listed entry positions are valid because $A$ has 2 rows and 3 columns, while $B$ has 3 rows and 2 columns. In particular, $a_{23}$ uses the last column of $A$, and $b_{32}$ uses the last row of $B$. The second row of $A$ contains three entries, and the first column of $B$ contains three entries, matching their matrix dimensions.
