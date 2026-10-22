# Problem 01

## The original problem

Compute

$$
\det\begin{pmatrix}3&-2\\5&4\end{pmatrix},\qquad \det\begin{pmatrix}1&7\\2&14\end{pmatrix}.
$$

Which matrix is invertible? Justify your answer.

## What we are looking for

We need two determinants of $2\times2$ matrices, and then a decision about which of the two matrices can have an inverse. The decision has to be justified, not guessed from the entries. The point of the exercise is the connection between a numerical determinant and the existence of an inverse.

## The idea we need

For a $2\times2$ matrix $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ the determinant is given by the Leibniz formula, which in this size has exactly two terms:

$$\det M = a\cdot d - b\cdot c.$$

In words: multiply the entries of the main diagonal, multiply the entries of the other diagonal, and subtract the second product from the first.

The rule that connects determinants with invertibility is:

$$M \text{ is invertible} \iff \det M \neq 0.$$

A square matrix has an inverse exactly when its rows (equivalently, its columns) are linearly independent, and that is exactly the condition that the determinant is not zero.

## Step-by-step solution

**First matrix.** Let $M_1=\begin{pmatrix}3&-2\\5&4\end{pmatrix}$. Reading off the entries gives $a=3$, $b=-2$, $c=5$, $d=4$, so

$$\det M_1 = 3\cdot 4 - (-2)\cdot 5 = 12 - (-10) = 22.$$

**Second matrix.** Let $M_2=\begin{pmatrix}1&7\\2&14\end{pmatrix}$, so $a=1$, $b=7$, $c=2$, $d=14$, and

$$\det M_2 = 1\cdot 14 - 7\cdot 2 = 14 - 14 = 0.$$

**Invertibility.** Since $\det M_1=22\neq 0$, the matrix $M_1$ is invertible. Since $\det M_2=0$, the matrix $M_2$ is not invertible.

**Extra observation on $M_2$.** Its second row is exactly twice its first row, because $2\cdot(1,7)=(2,14)$. Two proportional rows are linearly dependent, and a matrix with dependent rows has determinant $0$ and therefore no inverse.

## Why each step is valid

- Each determinant uses the Leibniz formula for $2\times2$ matrices; nothing more than reading the four entries off the matrix is needed.
- The sign in $12-(-10)$ comes from two sources: the minus sign that stands in front of $b\cdot c$, and the fact that the entry $b$ is itself negative. Both act in the same direction, so the contribution is $+10$.
- The criterion $M$ invertible $\iff \det M\neq 0$ holds for every square matrix, so applying it here is legitimate for both $2\times2$ matrices.
- The remark about proportional rows uses the same criterion in reverse: linearly dependent rows force $\det M=0$.

## Final answer (in words)

The first matrix has determinant $22$, and the second matrix has determinant $0$. Therefore the matrix $\begin{pmatrix}3&-2\\5&4\end{pmatrix}$ is invertible, while the matrix $\begin{pmatrix}1&7\\2&14\end{pmatrix}$ is not invertible.

$$\det\begin{pmatrix}3&-2\\5&4\end{pmatrix}=22,\qquad \det\begin{pmatrix}1&7\\2&14\end{pmatrix}=0.$$

## Verification

I recompute $M_1$ by a second route that does not use the diagonal formula: I apply the row operation $R_2\leftarrow R_2-\tfrac{5}{3} R_1$, which does not change a determinant and gives the upper triangular matrix $\begin{pmatrix}3&-2\\0&\tfrac{22}{3}\end{pmatrix}$. Its determinant is the product of the diagonal entries, $3\cdot\tfrac{22}{3}=22$, the same value as before.

For $M_2$ I check structurally instead of numerically: the second row is twice the first row, so the rows are dependent and the determinant must be $0$. This matches the computed value.

I also confirm invertibility constructively. The matrix

$$
\frac{1}{22}\begin{pmatrix}4&2\\-5&3\end{pmatrix}
$$

is an inverse of $M_1$, because

$$
\begin{pmatrix}3&-2\\5&4\end{pmatrix}\begin{pmatrix}4&2\\-5&3\end{pmatrix}=\begin{pmatrix}22&0\\0&22\end{pmatrix},
$$

and multiplying that by $1/22$ gives the identity matrix.

## Common mistakes

- Writing $ad+bc$ instead of $ad-bc$.
- Forgetting the minus sign in front of $b\cdot c$, which turns the answer $22$ into $-2$.
- Computing $(-2)\cdot 5=-10$ and then writing $12-(-10)=2$ by mistake.
- Stopping after the two determinants and not answering the second part of the question, which asks which matrix is invertible and why.

## How I would explain it in class

For a $2\times2$ matrix I multiply the main diagonal, multiply the other diagonal, and subtract the second product from the first. That gives $22$ for the first matrix and $0$ for the second one. A matrix is invertible exactly when its determinant is not zero, so the first matrix has an inverse and the second one does not, and indeed the second row of that matrix is just twice its first row.
