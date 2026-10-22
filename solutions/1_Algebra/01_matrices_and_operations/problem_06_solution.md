# Problem 06

## The original problem

For

$$
A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix},\qquad B=\begin{pmatrix}1&0\\2&1\\-1&3\end{pmatrix}
$$

compute $A^T$, $B^T$, and $AB$. Then verify in this example that

$$
(AB)^T=B^TA^T.
$$

> **Why this exercise:** teaches transposition and an important property that reverses the order of factors.

## What we are looking for

We need three matrices: the transpose of $A$, the transpose of $B$, and the product $AB$. After that we must compute both $(AB)^T$ and $B^TA^T$ and see that they are the same matrix, which confirms the rule in this particular example.

## The idea we need

**Transpose.** The transpose $M^T$ of a matrix $M$ is obtained by turning every row of $M$ into a column (equivalently, every column into a row). The entry in row $i$ and column $j$ of $M^T$ is the entry in row $j$ and column $i$ of $M$. A $2\times3$ matrix therefore becomes a $3\times2$ matrix.

**Product.** The entry in row $i$ and column $j$ of $AB$ is the dot product of row $i$ of $A$ with column $j$ of $B$: multiply matching entries and add the results.

**The rule to test.** $(AB)^T=B^TA^T$. The order of the factors is reversed. Notice that the sizes force this: $AB$ is $2\times2$, while $B^T$ is $2\times3$ and $A^T$ is $3\times2$, so $B^TA^T$ is defined and is $2\times2$.

## Step-by-step solution

**Step 1: the transposes.** The rows of $A$ are $(1,2,3)$ and $(4,5,6)$; writing them as columns gives

$$
A^T=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.
$$

The rows of $B$ are $(1,0)$, $(2,1)$, $(-1,3)$; writing them as columns gives

$$
B^T=\begin{pmatrix}1&2&-1\\0&1&3\end{pmatrix}.
$$

**Step 2: the product $AB$.** $A$ is $2\times3$ and $B$ is $3\times2$, so $AB$ is defined and is $2\times2$. Entry by entry:

- row 1 of $A$ with column 1 of $B$: $1\cdot1+2\cdot2+3\cdot(-1)=1+4-3=2$;
- row 1 of $A$ with column 2 of $B$: $1\cdot0+2\cdot1+3\cdot3=0+2+9=11$;
- row 2 of $A$ with column 1 of $B$: $4\cdot1+5\cdot2+6\cdot(-1)=4+10-6=8$;
- row 2 of $A$ with column 2 of $B$: $4\cdot0+5\cdot1+6\cdot3=0+5+18=23$.

$$
AB=\begin{pmatrix}2&11\\8&23\end{pmatrix}.
$$

**Step 3: the left side $(AB)^T$.** Turn the rows of $AB$ into columns:

$$
(AB)^T=\begin{pmatrix}2&8\\11&23\end{pmatrix}.
$$

**Step 4: the right side $B^TA^T$.** Here $B^T$ is $2\times3$ and $A^T$ is $3\times2$:

- row 1 of $B^T$ with column 1 of $A^T$: $1\cdot1+2\cdot2+(-1)\cdot3=1+4-3=2$;
- row 1 of $B^T$ with column 2 of $A^T$: $1\cdot4+2\cdot5+(-1)\cdot6=4+10-6=8$;
- row 2 of $B^T$ with column 1 of $A^T$: $0\cdot1+1\cdot2+3\cdot3=0+2+9=11$;
- row 2 of $B^T$ with column 2 of $A^T$: $0\cdot4+1\cdot5+3\cdot6=0+5+18=23$.

$$
B^TA^T=\begin{pmatrix}2&8\\11&23\end{pmatrix}.
$$

**Step 5: compare.** Both matrices equal $\begin{pmatrix}2&8\\11&23\end{pmatrix}$, so $(AB)^T=B^TA^T$ holds here.

## Why each step is valid

- Transposing is only a relabelling of positions, so each row of the original must appear, in the same order, as a column of the transpose.
- The product is defined because the number of columns of $A$ (three) equals the number of rows of $B$ (three); the result takes the number of rows of $A$ and the number of columns of $B$, giving $2\times2$.
- The reason for the reversed order is visible in the entries. The entry in row $i$, column $j$ of $(AB)^T$ is the entry in row $j$, column $i$ of $AB$, which is row $j$ of $A$ dotted with column $i$ of $B$. In $B^TA^T$, row $i$ of $B^T$ is column $i$ of $B$ and column $j$ of $A^T$ is row $j$ of $A$, so the same numbers are multiplied and added. This is why the two sides agree, and it is also why one cannot keep the order: $A^TB^T$ would be a $3\times3$ matrix and could not equal a $2\times2$ matrix.

## Final answer (in words)

The transpose of $A$ is the $3\times2$ matrix with columns $(1,2,3)$ and $(4,5,6)$; the transpose of $B$ is the $2\times3$ matrix with rows $(1,2,-1)$ and $(0,1,3)$; the product is $AB=\begin{pmatrix}2&11\\8&23\end{pmatrix}$. In symbols,

$$
(AB)^T=B^TA^T=\begin{pmatrix}2&8\\11&23\end{pmatrix},
$$

so the transpose of the product equals the product of the transposes in reversed order.

## Verification

I check the numbers in a way that does not repeat the dot products above. Multiply $AB$ by the vector $(1,1)^T$ in two ways. First, $B(1,1)^T=(1,3,2)^T$ (sum of the entries in each row of $B$), and then $A(1,3,2)^T=(1+6+6,\;4+15+12)^T=(13,31)^T$. Second, using the matrix found, $\begin{pmatrix}2&11\\8&23\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=(13,31)^T$. The two results agree, so $AB$ is correct. For the transposes, the entry in row 2, column 1 of $(AB)^T$ must be the entry in row 1, column 2 of $AB$, which is $11$; the table above has $11$ there. Finally, a computer algebra check with sympy gave the same matrices.

## Common mistakes

- Writing $(AB)^T=A^TB^T$ without reversing the order; here that product is $3\times3$ and has the wrong size.
- Transposing by reading columns in the wrong order, for example putting row 2 of $A$ in the first column of $A^T$.
- Multiplying $A$ and $B$ in the wrong order: $BA$ is $3\times3$, not the matrix that is asked for.
- Believing that checking one example proves the rule; it only confirms it here, and the entry argument above explains why it holds always.

## How I would explain it in class

Transposing turns every row into a column, so $A^T$ is $3\times2$ and $B^T$ is $2\times3$, and we found $AB=\begin{pmatrix}2&11\\8&23\end{pmatrix}$. Transposing the product gives $\begin{pmatrix}2&8\\11&23\end{pmatrix}$, and multiplying $B^T$ by $A^T$ gives exactly the same matrix. The order must be reversed because the entry of the transposed product is the same row-times-column sum, just read from the other side, and the sizes of $A^TB^T$ would not even match.
