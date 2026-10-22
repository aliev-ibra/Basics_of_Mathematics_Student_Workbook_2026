# Problem 12

## The original problem

For
$$
A(t)=\begin{pmatrix}1&2&3\\2&4&t\\0&1&1\end{pmatrix}
$$
find the values of $t$ for which the matrix is not invertible.

Before computing the determinant, perform the operation
$$
R_2\leftarrow R_2-2R_1
$$
and use the resulting structure. At the end, explain what special thing happens to the rows for the value of the parameter you found.

## What we are looking for

The symbol $t$ is an unknown number placed in the matrix. We want every value of $t$ for which $A(t)$ has no inverse, which happens exactly when $\det A(t)=0$. We must reach this by the row operation named in the problem, and we must describe what the rows look like for the special value.

## The idea we need

**Invertibility and the determinant.** A square matrix is not invertible exactly when its determinant is $0$.

**Row operation.** Replacing a row by itself minus a multiple of another row does not change the determinant. Here it will leave a row with only one possibly nonzero entry, which makes the determinant very easy to compute.

## Step-by-step solution

**Step 1: perform $R_2\leftarrow R_2-2R_1$.** The new second row is $(2-2\cdot1,\;4-2\cdot2,\;t-2\cdot3)=(0,0,t-6)$. The determinant is unchanged, so
$$
\det A(t)=\det\begin{pmatrix}1&2&3\\0&0&t-6\\0&1&1\end{pmatrix}.
$$

**Step 2: swap rows 2 and 3 to reach a triangular form.** Swapping two rows multiplies the determinant by $-1$:
$$
\det A(t)=-\det\begin{pmatrix}1&2&3\\0&1&1\\0&0&t-6\end{pmatrix}.
$$

**Step 3: use the triangular rule.** The matrix on the right is upper triangular, so its determinant is the product of the diagonal entries $1\cdot1\cdot(t-6)$. Therefore
$$
\det A(t)=-(t-6)=6-t.
$$

**Step 4: solve $\det A(t)=0$.** The equation $6-t=0$ gives $t=6$. For every other value of $t$ the determinant is nonzero, so the matrix is invertible.

**Step 5: look at the rows for $t=6$.** For $t=6$ the second row of the original matrix is $(2,4,6)=2\cdot(1,2,3)$, so the second row is exactly twice the first row. Equivalently, the row operation of Step 1 produces a row of zeros.

## Why each step is valid

- The operation in Step 1 adds a multiple of a different row to a row, so it does not change the determinant.
- The swap in Step 2 changes the sign of the determinant, which is why we put a minus sign in front.
- The matrix after the swap has zeros below the diagonal, so the triangular rule applies.
- A nonzero determinant means invertible and a zero determinant means not invertible, so $t=6$ is the only bad value.
- For $t=6$ the dependence $R_2-2R_1=0$ among the rows shows directly that the rows are linearly dependent, which is the geometric reason for the lack of an inverse.

## Final answer (in words)

The matrix $A(t)$ is not invertible only for $t=6$, because its determinant is $6-t$. For $t=6$ the second row $(2,4,6)$ is exactly twice the first row $(1,2,3)$, so after the operation $R_2\leftarrow R_2-2R_1$ the second row becomes entirely zero. For every other value of $t$ the matrix is invertible.

$$
\det A(t)=6-t,\qquad \det A(t)=0\iff t=6.
$$

## Verification

I compute the determinant of the original matrix directly, expanding along the first column, without any row operation:
$$
\det A(t)=1\cdot\det\begin{pmatrix}4&t\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}2&3\\1&1\end{pmatrix}+0=(4-t)-2(2-3)=4-t+2=6-t.
$$
This equals the formula found through row operations. As a numerical spot check, for $t=7$ the formula gives $-1\neq0$, and for $t=6$ the rows $(1,2,3)$ and $(2,4,6)$ are visibly proportional.

## Common mistakes

- Forgetting the minus sign created by the row swap, which would give $t-6$ instead of $6-t$. The solution $t=6$ is the same either way, but the formula would be wrong.
- Computing the new second row as $(0,0,t-3)$ by subtracting only $3$ instead of $2\cdot3=6$.
- Claiming the answer is "all $t$ except $6$". The question asks for the values where the matrix is not invertible.
- Forgetting to describe the rows for $t=6$, which the exercise explicitly requires.

## How I would explain it in class

Subtracting twice the first row from the second leaves the row $(0,0,t-6)$ and does not change the determinant. After one swap the matrix is triangular with diagonal $1,1,t-6$, so the determinant is $6-t$ and it vanishes only at $t=6$. At that value the second row is exactly twice the first, which is why the matrix has no inverse.
