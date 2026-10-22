# Problem 05

## The original problem

For

$$
A=\begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix}
$$

find $\det A$ by simplifying the matrix with row operations. At each step, indicate whether and how the determinant changes.

## What we are looking for

We must compute the determinant using row operations as the main tool, not as an afterthought. That means each elementary operation has to be listed together with its effect on the determinant, so the reader can follow the value of the determinant from the original matrix to the final answer. The intended strategy is to use only operations that leave the determinant unchanged and finish with a triangular matrix.

## The idea we need

**How row operations change a determinant.** For a square matrix $A$:

- Adding a multiple of one row to a different row does not change the determinant: $R_i\leftarrow R_i+kR_j$ with $i\neq j$ gives $\det A'=\det A$.
- Multiplying one row by a number $k$ multiplies the determinant by $k$: $R_i\leftarrow kR_i$ gives $\det A'=k\det A$.
- Swapping two rows multiplies the determinant by $-1$: $R_i\leftrightarrow R_j$ gives $\det A'=-\det A$.

**Strategy.** Use only operations of the first type, so the determinant never changes. Their aim is to create zeros, and once the matrix is upper triangular the determinant is the product of the diagonal entries. So we can read off the answer without ever writing a $3\times3$ expansion.

## Step-by-step solution

Start with

$$
A=\begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix},\qquad \det A=?.
$$

**Step 1: $R_2\leftarrow R_2-2R_1$.** The new second row is $(2-2\cdot1,\;1-2\cdot2,\;0-2\cdot3)=(0,-3,-6)$.

$$
\begin{pmatrix}1&2&3\\0&-3&-6\\-1&4&2\end{pmatrix}
$$

This operation adds a multiple of another row to a row, so **the determinant does not change**: it is still $\det A$.

**Step 2: $R_3\leftarrow R_3+R_1$.** The new third row is $(-1+1,\;4+2,\;2+3)=(0,6,5)$.

$$
\begin{pmatrix}1&2&3\\0&-3&-6\\0&6&5\end{pmatrix}
$$

Again this is of the first type, so **the determinant does not change**.

**Step 3: $R_3\leftarrow R_3+2R_2$.** Here $R_2$ is the already simplified row $(0,-3,-6)$, so the new third row is $(0+2\cdot0,\;6+2\cdot(-3),\;5+2\cdot(-6))=(0,0,-7)$.

$$
\begin{pmatrix}1&2&3\\0&-3&-6\\0&0&-7\end{pmatrix}
$$

This operation also leaves the determinant unchanged, and the matrix is now upper triangular.

**Step 4: read off the answer.** By the triangular rule, the determinant of the final matrix is the product of its diagonal entries:

$$\det A = 1\cdot(-3)\cdot(-7) = 21.$$

## Why each step is valid

- All three operations are of the type $R_i\leftarrow R_i+kR_j$ with $i\neq j$, so each of them leaves the determinant unchanged. The last sentence of the original exercise asks exactly for this: I state after every step that the determinant stays the same.
- In Step 3 the operation must use the *new* second row $(0,-3,-6)$; using the original second row would not create the zero in the third column. Row operations are performed in the order given.
- The final matrix is upper triangular because every entry below the diagonal is $0$, so the product-of-the-diagonal rule applies to it.
- The value found for the final matrix is therefore the value of $\det A$, because all intermediate matrices had the same determinant.

## Final answer (in words)

The determinant of $A$ is $21$. The three row operations used were adding multiples of other rows, and none of them changed the determinant; they only created zeros, after which the triangular matrix $\begin{pmatrix}1&2&3\\0&-3&-6\\0&0&-7\end{pmatrix}$ had determinant equal to the product $1\cdot(-3)\cdot(-7)$ of its diagonal entries.

$$\det\begin{pmatrix}1&2&3\\2&1&0\\-1&4&2\end{pmatrix}=21.$$

## Verification

I recompute the determinant without any row operations, using Sarrus' rule on the original matrix. The three down-right products are $1\cdot1\cdot2=2$, $2\cdot0\cdot(-1)=0$ and $3\cdot2\cdot4=24$, so their sum is $26$. The three down-left products are $3\cdot1\cdot(-1)=-3$, $2\cdot2\cdot2=8$ and $1\cdot0\cdot4=0$, so their sum is $5$. Therefore

$$\det A = 26-5=21,$$

which agrees with the row-operation computation.

A second check is the sign: the final diagonal is $1,-3,-7$, and since it contains two negative entries the determinant must be positive. The value $21$ is indeed positive, so the sign is consistent as well.

## Common mistakes

- Using an operation that scales a row without recording the factor, for example $R_3\leftarrow 2R_3$, and then forgetting that the determinant has been multiplied by $2$.
- Performing a row swap and forgetting that the determinant changes sign; here no swap was needed at all, because the entry $1$ in the top left corner was already a good pivot.
- Writing Step 3 as $R_3\leftarrow R_3+2R_1$ instead of $R_3\leftarrow R_3+2R_2$, which does not produce the triangular matrix.
- Stopping after the row operations without stating, step by step, whether the determinant changed.

## How I would explain it in class

I use only row operations of the form "add a multiple of one row to another", because those leave the determinant unchanged. Subtracting twice the first row from the second and adding the first row to the third clears the first column, and then adding twice the new second row to the third clears the rest. The matrix is now triangular, so the determinant is the product of the diagonal entries, $1\cdot(-3)\cdot(-7)=21$, and I confirmed this with Sarrus' rule on the original matrix.
