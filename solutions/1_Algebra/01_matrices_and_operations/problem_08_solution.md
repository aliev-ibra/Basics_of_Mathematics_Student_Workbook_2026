# Problem 08

## The original problem

For

$$
A=\begin{pmatrix}1&2&-1\\2&4&1\\-1&1&3\end{pmatrix}
$$

perform, in order:
1. $R_2\leftarrow R_2-2R_1$,
2. $R_3\leftarrow R_3+R_1$,
3. interchange $R_2$ and $R_3$.

Write the matrix after each step. Then, for each of the three operations, state an operation that reverses it.

> **Why this exercise:** prepares for elimination by showing that row operations are controlled and reversible transformations of a matrix.

## What we are looking for

We need the matrix obtained after each of the three operations, applied one after another to the result of the previous one, and then for each operation a second operation that undoes it, so that we return to the matrix we had before.

## The idea we need

Here $R_i$ means row $i$ of the current matrix. The notation $R_2\leftarrow R_2-2R_1$ means: replace row $2$ by (row $2$ minus twice row $1$), computed entry by entry, while the other rows stay as they are. Interchanging two rows swaps their positions. Each of these three kinds of operation can be undone by an operation of the same kind: add the same multiple back, or swap again.

## Step-by-step solution

**Step 1: $R_2\leftarrow R_2-2R_1$.** Row 1 is $(1,2,-1)$, so $2R_1=(2,4,-2)$. The new row 2 is $(2-2,\;4-4,\;1-(-2))=(0,0,3)$:

$$
A_1=\begin{pmatrix}1&2&-1\\0&0&3\\-1&1&3\end{pmatrix}.
$$

**Step 2: $R_3\leftarrow R_3+R_1$.** Row 1 is still $(1,2,-1)$. The new row 3 is $(-1+1,\;1+2,\;3+(-1))=(0,3,2)$:

$$
A_2=\begin{pmatrix}1&2&-1\\0&0&3\\0&3&2\end{pmatrix}.
$$

**Step 3: interchange $R_2$ and $R_3$.** Swap $(0,0,3)$ and $(0,3,2)$:

$$
A_3=\begin{pmatrix}1&2&-1\\0&3&2\\0&0&3\end{pmatrix}.
$$

**Step 4: the reversing operations.**

- Operation 1 subtracted $2R_1$ from $R_2$. It is reversed by $R_2\leftarrow R_2+2R_1$.
- Operation 2 added $R_1$ to $R_3$. It is reversed by $R_3\leftarrow R_3-R_1$.
- Operation 3 swapped $R_2$ and $R_3$. It is reversed by swapping $R_2$ and $R_3$ again.

## Why each step is valid

- Each operation uses only the rows named and changes only the row on the left of the arrow, so each matrix can be computed from the previous one with no hidden steps. Order matters: in step 2 the first row is the same as before because step 1 changed only row 2.
- Reversibility: row 1 is untouched by operation 1, so after the operation we still know $R_1$ and can add $2R_1$ back to recover the old row 2: $(R_2-2R_1)+2R_1=R_2$. The same argument works for operation 2. Row 1 stays untouched, which is what makes the undoing possible.
- A swap applied twice puts every row back in its original place, so a swap is its own reverse.
- The undoing operations must be performed in the opposite order (last operation undone first), just as one takes off socks after shoes in the reverse order of putting them on.

## Final answer (in words)

After the three operations the matrices are

$$
A_1=\begin{pmatrix}1&2&-1\\0&0&3\\-1&1&3\end{pmatrix},\quad A_2=\begin{pmatrix}1&2&-1\\0&0&3\\0&3&2\end{pmatrix},\quad A_3=\begin{pmatrix}1&2&-1\\0&3&2\\0&0&3\end{pmatrix}.
$$

The reversing operations are: $R_2\leftarrow R_2+2R_1$ for the first, $R_3\leftarrow R_3-R_1$ for the second, and interchanging $R_2$ and $R_3$ again for the third. The final matrix $A_3$ is upper triangular.

## Verification

I apply the three reversing operations to $A_3$ in the opposite order. First swap rows 2 and 3 of $A_3$ to get $\begin{pmatrix}1&2&-1\\0&0&3\\0&3&2\end{pmatrix}=A_2$. Then $R_3\leftarrow R_3-R_1$ turns the third row $(0,3,2)$ into $(0-1,\;3-2,\;2-(-1))=(-1,1,3)$, giving $A_1$. Finally $R_2\leftarrow R_2+2R_1$ gives $(0+2,\;0+4,\;3-2)=(2,4,1)$, and we are back at the original $A$. This confirms both the matrices and the reverses.

A second, independent check uses the determinant. Expanding along the first row, $\det A=1(12-1)-2(6+1)+(-1)(2+4)=11-14-6=-9$. Operations 1 and 2 do not change the determinant, the swap changes its sign, so $\det A_3$ should be $9$; as $A_3$ is triangular its determinant is $1\cdot3\cdot3=9$.

## Common mistakes

- Changing $R_1$ by accident, or forgetting that $R_1$ stays the same in all of these steps because the operations modify only $R_2$ or $R_3$.
- Sign errors when subtracting $2R_1$, in particular in the third entry: $1-2\cdot(-1)=3$, not $-1$.
- Undoing the operations in the same order instead of the opposite order.
- Writing the reverse of $R_3\leftarrow R_3+R_1$ as $R_1\leftarrow R_1-R_3$, which changes a different row.

## How I would explain it in class

Each row operation rewrites one row using another row, and we simply compute the new row entry by entry: the three steps give $A_1$, $A_2$ and finally the triangular matrix $A_3$. Every operation can be undone: add back what was subtracted, subtract what was added, and swap again to undo a swap, taking the steps in the reverse order. Because nothing is lost, the operations change how the matrix looks but not the information it holds, which is why elimination is safe.
