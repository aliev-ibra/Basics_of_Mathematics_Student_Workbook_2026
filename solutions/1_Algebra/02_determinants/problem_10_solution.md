# Problem 10

## The original problem

Without carrying out a full determinant calculation, explain why
$$
\det\begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix}=0.
$$
Identify a specific dependence between the rows and connect it with noninvertibility of the matrix.

## What we are looking for

We must show that the determinant is zero by looking at the structure of the matrix instead of expanding it. We must name an explicit relation between the rows, and we must explain why such a relation means the matrix has no inverse.

## The idea we need

**Rows that are multiples of each other force a zero determinant.** If one row of a square matrix is a multiple of another row, then subtracting that multiple from the row produces a row of zeros without changing the determinant. A matrix with a row of zeros has determinant $0$, because the determinant is linear in that row, and multiplying the zero row by any number changes nothing while multiplying the determinant by that number.

**Link with invertibility.** A square matrix is invertible exactly when its determinant is not zero. So a zero determinant means the matrix is not invertible.

## Step-by-step solution

Call the rows $R_1=(1,2,3)$, $R_2=(2,4,6)$ and $R_3=(0,1,5)$.

**Step 1: spot the relation.** Multiplying $R_1$ by $2$ gives $(2\cdot1,\,2\cdot2,\,2\cdot3)=(2,4,6)=R_2$. So
$$
R_2=2R_1,\qquad\text{equivalently}\qquad 2R_1-R_2=(0,0,0).
$$

**Step 2: apply a row operation.** Replace $R_2$ by $R_2-2R_1$. This adds a multiple of another row to a row, so the determinant does not change. The new matrix is
$$
\begin{pmatrix}1&2&3\\0&0&0\\0&1&5\end{pmatrix}.
$$

**Step 3: conclude.** A matrix with a row of zeros has determinant $0$. The determinant did not change in Step 2, so the original matrix also has determinant $0$.

**Step 4: connect with invertibility.** A nonzero relation among the rows, here $2R_1-R_2+0\cdot R_3=0$, means the rows are linearly dependent. A square matrix with dependent rows is not invertible, which agrees with $\det=0$.

## Why each step is valid

- The operation $R_2\leftarrow R_2-2R_1$ is of the type "add a multiple of one row to a different row", and this type never changes the determinant.
- A zero row gives determinant $0$: if we expand the determinant along that row, every term contains a factor $0$.
- Invertibility and a nonzero determinant are equivalent, because the inverse formula divides by the determinant, and conversely a matrix with $\det=0$ cannot satisfy $\det(A)\det(A^{-1})=\det I=1$.
- The third row $(0,1,5)$ plays no role, so we did not need to look at it.

## Final answer (in words)

The determinant is $0$ because the second row is exactly twice the first row, $R_2=2R_1$. Subtracting twice the first row from the second row gives a zero row without changing the determinant, and a matrix with a zero row has determinant zero. Because the rows are linearly dependent and the determinant is zero, the matrix is not invertible.

$$
\det\begin{pmatrix}1&2&3\\2&4&6\\0&1&5\end{pmatrix}=0.
$$

## Verification

I now compute the determinant fully, by expanding along the first column. Only the entries $1$ (top) and $2$ (middle) matter, because the bottom entry is $0$:
$$
\det=1\cdot\det\begin{pmatrix}4&6\\1&5\end{pmatrix}-2\cdot\det\begin{pmatrix}2&3\\1&5\end{pmatrix}+0
=1\cdot(20-6)-2\cdot(10-3)=14-14=0.
$$
The full calculation agrees with the structural argument. As a second check, if the matrix had an inverse we could multiply the relation $2R_1-R_2=0$ out and get a contradiction: the row vector $(2,-1,0)$ multiplied by the matrix gives $(0,0,0)$, so $(2,-1,0)\,A=0$, and multiplying by $A^{-1}$ on the right would force $(2,-1,0)=0$, which is false.

## Common mistakes

- Thinking the determinant is zero only when two rows are equal. A row that is a multiple of another row is enough, and in general any dependence among the rows is enough.
- Believing that the third row must also be related to the others. Here it is not, and one relation is already sufficient.
- Forgetting that the problem asks about invertibility as well; the answer must state that the matrix is not invertible.
- Checking only that $R_2$ looks bigger than $R_1$ instead of multiplying every entry: $2\cdot3=6$ matches the last entry too.

## How I would explain it in class

The second row $(2,4,6)$ is exactly twice the first row $(1,2,3)$, so subtracting twice the first row from the second leaves a row of zeros without changing the determinant. A matrix with a row of zeros has determinant $0$, and a square matrix with determinant $0$ has no inverse because its rows are linearly dependent. Expanding along the first column gives $14-14=0$, which confirms it.
