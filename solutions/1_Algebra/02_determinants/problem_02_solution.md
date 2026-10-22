# Problem 02

## The original problem

For

$$
A=\begin{pmatrix}1&2&-1\\0&3&4\\2&1&5\end{pmatrix}
$$

compute $\det A$ using Sarrus' rule. Then perform one simple check using a chosen property of the determinant.

## What we are looking for

We need the determinant of the given $3\times3$ matrix, computed with the shortcut called Sarrus' rule, and then an independent confirmation that the number is correct. The check has to use a property of the determinant, so it is genuinely a second opinion rather than a repetition of the same multiplication. Doing this habit now saves time later, when a wrong sign would be hard to spot.

## The idea we need

**Sarrus' rule.** Write the matrix once more with its first two columns repeated on the right:

$$
\begin{pmatrix}1&2&-1&1&2\\0&3&4&0&3\\2&1&5&2&1\end{pmatrix}
$$

The three products of the diagonals that run from top left to bottom right are added, and the three products of the diagonals that run from top right to bottom left are subtracted. Written with the entries $a_{ij}$ of $A$:

$$\det A = \bigl(a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}\bigr)-\bigl(a_{13}a_{22}a_{31}+a_{12}a_{21}a_{33}+a_{11}a_{23}a_{32}\bigr).$$

**Property used for the check.** Transposing a matrix does not change its determinant:

$$\det A^T = \det A.$$

This holds for every square matrix. It is a convenient check, because the transposed matrix has different rows, so the check forces a different sequence of multiplications and a different expansion.

## Step-by-step solution

**Step 1: the three "down-right" products.** Using the extended matrix above, I read the diagonals that start in the first row and move down and to the right:

$$a_{11}a_{22}a_{33}=1\cdot 3\cdot 5=15,$$
$$a_{12}a_{23}a_{31}=2\cdot 4\cdot 2=16,$$
$$a_{13}a_{21}a_{32}=(-1)\cdot 0\cdot 1=0.$$

Their sum is $15+16+0=31$.

**Step 2: the three "down-left" products.** These start in the first row and move down and to the left:

$$a_{13}a_{22}a_{31}=(-1)\cdot 3\cdot 2=-6,$$
$$a_{12}a_{21}a_{33}=2\cdot 0\cdot 5=0,$$
$$a_{11}a_{23}a_{32}=1\cdot 4\cdot 1=4.$$

Their sum is $-6+0+4=-2$.

**Step 3: subtract.** Sarrus' rule says we subtract the second sum from the first:

$$\det A = 31-(-2)=33.$$

**Step 4: the check with a property.** I use the transpose property and compute $\det A^T$ by an ordinary expansion along its first row. The transpose is

$$
A^T=\begin{pmatrix}1&0&2\\2&3&1\\-1&4&5\end{pmatrix},
$$

and expanding along the first row gives

$$\det A^T = 1\cdot\det\begin{pmatrix}3&1\\4&5\end{pmatrix} - 0\cdot\det\begin{pmatrix}2&1\\-1&5\end{pmatrix} + 2\cdot\det\begin{pmatrix}2&3\\-1&4\end{pmatrix}.$$

Now each $2\times2$ determinant is one diagonal product minus the other:

$$\det A^T = 1\cdot(3\cdot5-1\cdot4) - 0 + 2\cdot(2\cdot4-3\cdot(-1)) = 11 + 22 = 33.$$

This matches the Sarrus result, so $\det A=33$ is confirmed.

## Why each step is valid

- Sarrus' rule is a rearrangement of the Leibniz formula for $3\times3$ determinants, so it computes exactly the same number as the general definition; it is not an approximation.
- The repeated columns on the right are only a bookkeeping device: the extra copies allow the three down-left diagonals to be read off in the same visual way as the down-right ones.
- The signs of the six products come directly from the entries, including the negative entry $a_{13}=-1$; in the down-left group the product $a_{13}a_{22}a_{31}$ is therefore $-6$, which is why the second sum is negative and has to be subtracted.
- The property $\det A^T=\det A$ is valid for every square matrix, and the expansion along the first row of $A^T$ uses the cofactor sign pattern $+,-,+$.
- Every $2\times2$ determinant in the check is evaluated with the Leibniz formula $ad-bc$, the same formula used in Problem 1.

## Final answer (in words)

By Sarrus' rule the determinant of $A$ is $33$. The check with the property that a matrix and its transpose have equal determinants gives the same number, so the value is confirmed.

$$\det\begin{pmatrix}1&2&-1\\0&3&4\\2&1&5\end{pmatrix}=33.$$

## Verification

I recompute the determinant a third time, using row operations instead of Sarrus. Adding a multiple of one row to another row does not change the determinant, so the operation $R_3\leftarrow R_3-2R_1$ is allowed:

$$
\det A=\det\begin{pmatrix}1&2&-1\\0&3&4\\0&-3&7\end{pmatrix}.
$$

Expanding this along the first column leaves a single $2\times2$ determinant:

$$
\det A=1\cdot\det\begin{pmatrix}3&4\\-3&7\end{pmatrix}=1\cdot(3\cdot7-4\cdot(-3))=21+12=33.
$$

This is a third independent route to the same number, so the value $33$ is solid. I also check the sign: the matrix has a positive determinant, which is consistent with the orientation of its rows, and the arithmetic of the two Sarrus sums ($31$ and $-2$) is confirmed by the row-operation result $31-(-2)=33$ matching $21+12=33$.

## Common mistakes

- Forgetting that the down-left products are subtracted, or subtracting the down-right products instead.
- Dropping the negative sign of the entry $a_{13}=-1$ when forming the products $a_{13}a_{22}a_{31}$ and $a_{13}a_{21}a_{32}$.
- Mixing up the two middle diagonals, $a_{12}a_{23}a_{31}$ and $a_{12}a_{21}a_{33}$, which give different numbers here ($16$ and $0$).
- Treating the repeated columns on the right as extra real columns, which would change the size of the matrix and the value of the determinant.

## How I would explain it in class

Sarrus' rule means repeating the first two columns on the right, adding the three diagonals that run down to the right and subtracting the three that run down to the left. Here the first sum is $15+16+0=31$ and the second sum is $-6+0+4=-2$, so the determinant is $31-(-2)=33$. To check it I transpose the matrix, use the property that transposing does not change the determinant, and expand along the first row of the transpose, which again gives $33$.
