# Problem 13

## The original problem

Compute the determinant
$$
A=\begin{pmatrix}1&2&3\\2&5&7\\1&0&2\end{pmatrix}
$$
using elimination. Record the effect of every row operation used on the value of the determinant.

## What we are looking for

We need the number $\det A$, computed by transforming the matrix into a triangular one with row operations, and for each operation we must state whether it changes the determinant and by what factor.

## The idea we need

**Row operations.** Adding a multiple of one row to a different row leaves the determinant unchanged. Swapping two rows multiplies it by $-1$. Multiplying a row by $k$ multiplies it by $k$.

**Triangular matrices.** If all entries below the diagonal are zero, the determinant is the product of the diagonal entries.

**Plan.** The top-left entry is $1$, so we can use it to clear the first column with operations of the first type. Then we clear the second column. No swaps or scalings are needed, so the determinant stays equal to $\det A$ throughout.

## Step-by-step solution

**Step 1: $R_2\leftarrow R_2-2R_1$.** The new second row is $(2-2,\;5-4,\;7-6)=(0,1,1)$. Effect on the determinant: none (factor $1$).

**Step 2: $R_3\leftarrow R_3-R_1$.** The new third row is $(1-1,\;0-2,\;2-3)=(0,-2,-1)$. Effect on the determinant: none. The matrix is
$$
\begin{pmatrix}1&2&3\\0&1&1\\0&-2&-1\end{pmatrix}.
$$

**Step 3: $R_3\leftarrow R_3+2R_2$.** The new third row is $(0,\;-2+2\cdot1,\;-1+2\cdot1)=(0,0,1)$. Effect on the determinant: none. The matrix is
$$
\begin{pmatrix}1&2&3\\0&1&1\\0&0&1\end{pmatrix}.
$$

**Step 4: triangular rule.** The matrix is upper triangular with diagonal entries $1,1,1$, so its determinant is $1\cdot1\cdot1=1$. Since no operation changed the determinant, $\det A=1$.

Summary of the effect of each operation: Step 1 factor $1$, Step 2 factor $1$, Step 3 factor $1$. The total factor is $1\cdot1\cdot1=1$.

## Why each step is valid

- All three operations are of the form $R_i\leftarrow R_i+kR_j$ with $i\neq j$, which never changes the determinant. This is why the determinant of the final matrix equals $\det A$ exactly, with no correction.
- In Step 3, we use the updated second row $(0,1,1)$, whose leading $1$ in the second column cancels the $-2$ below it.
- The final matrix has zeros below the diagonal, so the triangular rule applies.

## Final answer (in words)

The determinant of $A$ is $1$. Every row operation used was an addition of a multiple of another row, so each had factor $1$ and the determinant stayed equal to that of $A$ until we reached the triangular matrix with diagonal $1,1,1$.

$$
\det\begin{pmatrix}1&2&3\\2&5&7\\1&0&2\end{pmatrix}=1.
$$

## Verification

I recompute by expanding along the first row, without any row operations:
$$
\det A=1\cdot(5\cdot2-7\cdot0)-2\cdot(2\cdot2-7\cdot1)+3\cdot(2\cdot0-5\cdot1)=1\cdot10-2\cdot(-3)+3\cdot(-5)=10+6-15=1.
$$
This agrees with the elimination result. The determinant is nonzero, so $A$ is invertible.

## Common mistakes

- Writing the third row after Step 2 as $(0,2,1)$ by dropping the signs; the correct row is $(0,-2,-1)$.
- In Step 3 subtracting $2R_2$ instead of adding it, which would give $(0,-4,-3)$ and not clear the entry.
- Believing that a row operation always changes the determinant. Only swaps and scalings do.
- Forgetting to record the effect of each operation, which is part of the task.

## How I would explain it in class

I clear the first column by subtracting twice the first row from the second and the first row from the third, and then I add twice the new second row to the third. Each of these three operations adds a multiple of another row, so it leaves the determinant unchanged, and the result is a triangular matrix with diagonal $1,1,1$. Therefore the determinant is $1$, and expanding along the first row gives $10+6-15=1$ as a check.
