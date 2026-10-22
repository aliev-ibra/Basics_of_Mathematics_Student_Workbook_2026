# Problem 09

## The original problem

Given
$$A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}3&1\\2&4\end{pmatrix}.$$
Solve the equation $AX=B$ for $X$. Before calculating, decide on which side of the equation $A^{-1}$ must be used. Then check the result by computing $AX$.

## What we are looking for

We want a $2\times2$ matrix $X$ such that when $A$ multiplies it from the left, the product is $B$. We must also say, before any arithmetic, whether $A^{-1}$ is placed to the left or to the right of $B$, and then confirm the answer by multiplying $A$ by $X$.

## The idea we need

Matrix multiplication is not commutative: in general $PQ\neq QP$. So when we "divide" by $A$, we must multiply both sides of the equation by $A^{-1}$ on the same side where $A$ stands. In $AX=B$ the matrix $A$ stands on the left of $X$, so we multiply from the left:
$$A^{-1}(AX)=A^{-1}B \quad\Longrightarrow\quad (A^{-1}A)X=A^{-1}B \quad\Longrightarrow\quad X=A^{-1}B.$$
Here $I$ is the identity matrix, $A^{-1}A=I$ by the definition of the inverse, and $IX=X$. The inverse of a $2\times2$ matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $ad-bc\neq0$ is $\dfrac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.

## Step-by-step solution

**Decision.** $A$ is on the left of $X$, so $A^{-1}$ must be used on the left: $X=A^{-1}B$, not $X=BA^{-1}$.

**Step 1: check that $A^{-1}$ exists.** $\det A=1\cdot1-2\cdot0=1\neq0$, so $A$ is invertible.

**Step 2: find $A^{-1}$.** By the $2\times2$ formula, with $ad-bc=1$,
$$A^{-1}=\begin{pmatrix}1&-2\\0&1\end{pmatrix}.$$

**Step 3: multiply $A^{-1}$ by $B$ from the left.** Each entry is a row of $A^{-1}$ times a column of $B$:
$$X=A^{-1}B=\begin{pmatrix}1&-2\\0&1\end{pmatrix}\begin{pmatrix}3&1\\2&4\end{pmatrix}
=\begin{pmatrix}1\cdot3-2\cdot2&1\cdot1-2\cdot4\\0\cdot3+1\cdot2&0\cdot1+1\cdot4\end{pmatrix}
=\begin{pmatrix}-1&-7\\2&4\end{pmatrix}.$$

## Why each step is valid

- Multiplying both sides of an equation by the same matrix on the same side gives a true equation again, so $AX=B$ implies $A^{-1}AX=A^{-1}B$. The side matters because $A^{-1}$ can cancel $A$ only when it is directly next to it.
- Matrix multiplication is associative, so $A^{-1}(AX)=(A^{-1}A)X$, and then $A^{-1}A=I$ and $IX=X$. This is why the left side becomes exactly $X$.
- The inverse exists because $\det A\neq0$; without that we could not multiply by $A^{-1}$ at all.
- The answer is unique: any solution must equal $A^{-1}B$ by the argument above.

## Final answer (in words)

The unknown matrix is the inverse of $A$ multiplied by $B$ from the left, and it equals
$$X=\begin{pmatrix}-1&-7\\2&4\end{pmatrix}.$$

## Verification

I multiply $A$ by $X$ and compare with $B$:
$$AX=\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}-1&-7\\2&4\end{pmatrix}
=\begin{pmatrix}-1+4&-7+8\\2&4\end{pmatrix}=\begin{pmatrix}3&1\\2&4\end{pmatrix}=B.$$

As an independent check of the side decision, compute the wrong candidate $BA^{-1}$:
$$BA^{-1}=\begin{pmatrix}3&1\\2&4\end{pmatrix}\begin{pmatrix}1&-2\\0&1\end{pmatrix}=\begin{pmatrix}3&-5\\2&0\end{pmatrix}.$$
Multiplying it by $A$ gives $A(BA^{-1})=\begin{pmatrix}7&-5\\2&0\end{pmatrix}\neq B$, so the wrong side really does fail.

## Common mistakes

- Writing $X=BA^{-1}$, which uses the inverse on the wrong side and gives a different matrix, $\begin{pmatrix}3&-5\\2&0\end{pmatrix}$, that does not solve $AX=B$.
- Multiplying only one side of the equation by $A^{-1}$ (for example, left on the left side and right on the right side).
- Dividing entries of $B$ by entries of $A$; there is no entrywise division of matrices.
- Sign error in the inverse formula: the off-diagonal entries change sign, giving $-2$ and not $2$.

## How I would explain it in class

Since $A$ stands on the left of $X$, I multiply both sides by $A^{-1}$ on the left, which cancels $A$ and gives $X=A^{-1}B$. With $A^{-1}=\begin{pmatrix}1&-2\\0&1\end{pmatrix}$ I get $X=\begin{pmatrix}-1&-7\\2&4\end{pmatrix}$. Multiplying $A$ by this $X$ returns $B$, while the other order $BA^{-1}$ does not, which shows that the side really matters.
