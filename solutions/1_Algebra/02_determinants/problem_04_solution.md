# Problem 04

## The original problem

Without expanding the determinant, compute

$$
\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}.
$$

State the rule for an arbitrary triangular matrix and explain it using this example.

## What we are looking for

The determinant of the given matrix, but computed without expanding it along a row or a column. On top of that we must state the general rule for any triangular matrix and show how the example illustrates that rule. The rule is the standard shortcut, and the explanation has to say why it works.

## The idea we need

**Triangular matrix.** A matrix is *upper triangular* if all entries below the main diagonal are zero, and *lower triangular* if all entries above the main diagonal are zero.

**The rule.** For any triangular matrix $T$ of size $n\times n$, with diagonal entries $t_{11},t_{22},\dots,t_{nn}$:

$$\det T = t_{11}\,t_{22}\cdots t_{nn}.$$

That is: the determinant of a triangular matrix is the product of its diagonal entries. This holds for upper and lower triangular matrices, in any size.

**Why the rule works.** Expand the determinant along the first column of an upper triangular matrix. All entries of that column except the first one are zero, so only one term survives, and the minor that remains is again triangular. Repeating this argument peels off one diagonal entry at a time, and the last $1\times1$ determinant is the last diagonal entry.

## Step-by-step solution

**Step 1: recognise the shape of the matrix.** The matrix

$$
\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}
$$

has zeros in the positions $(2,1)$, $(3,1)$ and $(3,2)$, i.e. in every position strictly below the main diagonal. So it is upper triangular.

**Step 2: read the diagonal.** The diagonal entries, from top left to bottom right, are $2$, $-3$ and $7$.

**Step 3: multiply them.**

$$\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}=2\cdot(-3)\cdot 7=-42.$$

**Step 4: explain the rule with this example.** Expanding along the first column of this matrix leaves only the entry $2$:

$$
\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}
=2\cdot\det\begin{pmatrix}-3&5\\0&7\end{pmatrix}
=2\cdot(-3)\cdot 7,
$$

because the $2\times2$ minor is triangular as well, and so on. Each expansion along the first column removes exactly one diagonal entry and leaves the rest of the matrix triangular, which is why the final answer is the product of all diagonal entries.

## Why each step is valid

- To identify a triangular matrix one only has to check the entries below (or above) the diagonal; here all three of them are $0$.
- The rule itself is valid for every triangular matrix of every size, so applying it to this $3\times3$ example needs no further conditions.
- In the illustrative expansion, the zeros in the first column remove all terms except one, and the cofactor sign of the entry $(1,1)$ is $+1$, so no sign change occurs.
- The sign of the final answer is forced: exactly one diagonal entry, namely $-3$, is negative, so the product is negative.

## Final answer (in words)

The determinant of the given upper triangular matrix is $-42$, obtained without expanding: it is the product $2\cdot(-3)\cdot 7$ of the diagonal entries. The general rule is that the determinant of any triangular matrix equals the product of its diagonal entries, and the example illustrates it because each expansion along the first column removes one diagonal entry and leaves a smaller triangular matrix.

$$\det\begin{pmatrix}2&4&1\\0&-3&5\\0&0&7\end{pmatrix}=2\cdot(-3)\cdot 7=-42.$$

## Verification

I expand the determinant in two different ways and compare with the rule.

Expansion along the first column gives

$$2\cdot\det\begin{pmatrix}-3&5\\0&7\end{pmatrix}=2\cdot\bigl((-3)\cdot7-5\cdot0\bigr)=2\cdot(-21)=-42.$$

Expansion along the third row gives

$$0\cdot(\ldots)+0\cdot(\ldots)+7\cdot\det\begin{pmatrix}2&4\\0&-3\end{pmatrix}=7\cdot\bigl(2\cdot(-3)-4\cdot0\bigr)=7\cdot(-6)=-42.$$

Both expansions agree with the product rule. As a further consistency check, the product $2\cdot(-3)\cdot7$ has one negative factor, so the determinant must be negative, and $-42$ is indeed negative; the magnitude $42$ also equals $2\cdot3\cdot7$, the product of the absolute values of the diagonal entries.

## Common mistakes

- Forgetting that one diagonal entry is negative and reporting $42$ instead of $-42$.
- Believing that "without expanding" forbids any reasoning, so the note contains no explanation of why the rule holds.
- Applying the rule to a matrix that is not triangular; for instance $\begin{pmatrix}2&4&1\\0&-3&5\\1&0&7\end{pmatrix}$ has the same diagonal but a different determinant, because the entry $1$ below the diagonal is not zero.
- Reading the "diagonal" as the anti-diagonal (from top right to bottom left), which is wrong.

## How I would explain it in class

A triangular matrix has zeros on one side of the main diagonal, and its determinant is simply the product of its diagonal entries, so here I get $2\cdot(-3)\cdot7=-42$. The reason is that expanding along the first column leaves only one nonzero term and a smaller triangular matrix, and I keep doing this until only the diagonal entries are left. That is why we can multiply them without writing out any long expansion.
