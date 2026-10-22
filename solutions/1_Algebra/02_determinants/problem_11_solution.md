# Problem 11

## The original problem

Compute
$$
\det\begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}
$$
by first performing row operations that create as many zeros as possible. State which operations do not change the determinant.

## What we are looking for

We want the value of a $3\times3$ determinant, obtained by using row operations to create zeros below the first entry (and then below the second), and we must say which of the operations we used leave the determinant unchanged.

## The idea we need

**Row operations and the determinant.** Adding a multiple of one row to a different row does not change the determinant. Swapping two rows changes its sign, and multiplying a row by a number $k$ multiplies the determinant by $k$.

**Triangular matrices.** If all entries below the main diagonal are zero, the determinant is the product of the diagonal entries.

**Plan.** The top-left entry is $1$, a convenient pivot, so we can clear the first column by subtracting the first row from the others, and then clear the second column. Only operations of the first type are needed.

## Step-by-step solution

Let
$$
A=\begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}.
$$

**Step 1: $R_2\leftarrow R_2-R_1$.** The new second row is $(1-1,\,3-2,\,4-3)=(0,1,1)$. This adds a multiple of another row, so the determinant does not change.

**Step 2: $R_3\leftarrow R_3-R_1$.** The new third row is $(1-1,\,4-2,\,6-3)=(0,2,3)$. Again the determinant does not change. The matrix is now
$$
\begin{pmatrix}1&2&3\\0&1&1\\0&2&3\end{pmatrix}.
$$

**Step 3: $R_3\leftarrow R_3-2R_2$.** The new third row is $(0-0,\,2-2\cdot1,\,3-2\cdot1)=(0,0,1)$. This is again an operation that leaves the determinant unchanged. The matrix is
$$
\begin{pmatrix}1&2&3\\0&1&1\\0&0&1\end{pmatrix}.
$$

**Step 4: read off the determinant.** The matrix is upper triangular, so the determinant is the product of the diagonal entries:
$$
\det A=1\cdot1\cdot1=1.
$$

## Why each step is valid

- All three operations have the form $R_i\leftarrow R_i-kR_j$ with $i\neq j$. Such operations do not change the determinant, so every matrix in the chain has the same determinant as $A$.
- In Step 3 we use the new second row $(0,1,1)$, because its leading $1$ sits in the second column and lets us clear the entry $2$ below it.
- The final matrix has zeros below the diagonal, so the triangular rule applies.
- No row was swapped or scaled, so no correction factor or sign is needed.

## Final answer (in words)

The determinant is $1$. All three row operations (subtracting the first row from the second, subtracting the first row from the third, and subtracting twice the second row from the third) leave the determinant unchanged, and they produce a triangular matrix whose diagonal entries are $1,1,1$.

$$
\det\begin{pmatrix}1&2&3\\1&3&4\\1&4&6\end{pmatrix}=1.
$$

## Verification

I expand the original determinant along the first row, without any row operations:
$$
\det A=1\cdot(3\cdot6-4\cdot4)-2\cdot(1\cdot6-4\cdot1)+3\cdot(1\cdot4-3\cdot1).
$$
The three small determinants are $18-16=2$, $6-4=2$ and $4-3=1$, so
$$
\det A=1\cdot2-2\cdot2+3\cdot1=2-4+3=1.
$$
This agrees with the value found by row operations. The determinant is nonzero, so the matrix is also invertible.

## Common mistakes

- Subtracting $R_1$ from $R_3$ but forgetting that the entry $6-3$ equals $3$, not $2$, which produces a wrong third row.
- In Step 3, subtracting $2R_1$ instead of $2R_2$, which would bring back a nonzero entry in the first column.
- Thinking that the operations change the determinant. Adding or subtracting a multiple of a row never changes it.
- Forgetting the signs in the cofactor expansion in the verification (the pattern is plus, minus, plus).

## How I would explain it in class

I subtract the first row from the second and third rows, and then subtract twice the new second row from the third, and none of these operations changes the determinant. This turns the matrix into an upper triangular one with $1,1,1$ on the diagonal, so the determinant is $1\cdot1\cdot1=1$. A direct expansion along the first row gives $2-4+3=1$, which confirms it.
