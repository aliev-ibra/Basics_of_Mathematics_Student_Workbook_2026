# Problem 03

## The original problem

For

$$
A=\begin{pmatrix}1&2&0\\0&3&1\\2&1&1\end{pmatrix}
$$

compute $\det A$. Then form a matrix $B$ by swapping the first and second rows of $A$.

First predict $\det B$ using a determinant property, and then verify your prediction by calculation.

## What we are looking for

Two things: the determinant of $A$, and the determinant of the matrix $B$ that results from swapping the first two rows of $A$. The exercise asks us to predict the second value from a property before computing it, so the property has to be stated clearly and the calculation has to confirm it. The key idea is that one row swap changes the sign of a determinant and nothing else.

## The idea we need

**Expansion along a row.** The determinant of a $3\times3$ matrix can be computed by expanding along one of its rows. If we expand along the first row, the signs of the three terms alternate $+, -, +$:

$$\det A = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13},$$

where $M_{1j}$ is the *minor*: the $2\times2$ matrix left over after deleting row $1$ and column $j$, and $M_{1j}$ is replaced by its own determinant. The alternating signs are the cofactor signs $(-1)^{1+j}$.

**The row-swap property.** Swapping two rows of a square matrix multiplies its determinant by $-1$:

$$\det(\text{matrix with rows } i \text{ and } j \text{ exchanged}) = -\det(\text{original matrix}).$$

The reason is geometric: swapping two rows reverses the orientation of the parallelepiped spanned by the rows, so the signed volume changes sign.

## Step-by-step solution

**Step 1: compute $\det A$ by expanding along the first row.** The minors of the first row are obtained by deleting row $1$ and each column in turn:

$$\det A = 1\cdot\det\begin{pmatrix}3&1\\1&1\end{pmatrix} - 2\cdot\det\begin{pmatrix}0&1\\2&1\end{pmatrix} + 0\cdot\det\begin{pmatrix}0&3\\2&1\end{pmatrix}.$$

**Step 2: evaluate the two $2\times2$ determinants** with the Leibniz formula $ad-bc$:

$$\det\begin{pmatrix}3&1\\1&1\end{pmatrix}=3\cdot1-1\cdot1=2,\qquad \det\begin{pmatrix}0&1\\2&1\end{pmatrix}=0\cdot1-1\cdot2=-2.$$

**Step 3: combine.**

$$\det A = 1\cdot 2 - 2\cdot(-2) + 0\cdot(-6) = 2+4+0 = 6.$$

**Step 4: form $B$.** Swapping the first and second rows of $A$ moves the row $(0,3,1)$ to the top:

$$B=\begin{pmatrix}0&3&1\\1&2&0\\2&1&1\end{pmatrix}.$$

**Step 5: predict.** By the row-swap property, one swap changes the sign and nothing else:

$$\det B = -\det A = -6.$$

**Step 6: verify by calculation.** Expanding $B$ along its first row:

$$\det B = 0\cdot\det\begin{pmatrix}2&0\\1&1\end{pmatrix} - 3\cdot\det\begin{pmatrix}1&0\\2&1\end{pmatrix} + 1\cdot\det\begin{pmatrix}1&2\\2&1\end{pmatrix}.$$

The three small determinants are $2\cdot1-0\cdot1=2$, $1\cdot1-0\cdot2=1$, and $1\cdot1-2\cdot2=-3$, so

$$\det B = 0\cdot 2 - 3\cdot 1 + 1\cdot(-3) = 0-3-3 = -6.$$

The prediction is confirmed.

## Why each step is valid

- Expanding along the first row is legitimate for every square matrix; the minors are the determinants of the remaining submatrices.
- The cofactor signs along the first row are $+,-,+$, which is why the middle term enters with a minus sign.
- The third term vanishes because $a_{13}=0$; there is no need to compute that minor at all.
- The row-swap property is applied to exactly one swap of two rows, so the determinant is multiplied by $-1$ exactly once.
- In the verification, the same Leibniz formula and the same cofactor sign pattern are used, so the two computations are independent in their arithmetic but consistent in their rules.

## Final answer (in words)

The determinant of $A$ is $6$. The matrix $B$ obtained by swapping the first two rows of $A$ has determinant $-6$: a single row swap changes the sign of the determinant and leaves its absolute value unchanged.

$$\det A = 6,\qquad \det B = -6.$$

## Verification

I recompute $\det A$ by a completely different method: elimination. The operation $R_3\leftarrow R_3-2R_1$ does not change the determinant, and it gives

$$
\det A=\det\begin{pmatrix}1&2&0\\0&3&1\\0&-3&1\end{pmatrix}.
$$

Expanding along the first column now gives a single $2\times2$ determinant:

$$
\det A=1\cdot\det\begin{pmatrix}3&1\\-3&1\end{pmatrix}=1\cdot(3\cdot1-1\cdot(-3))=3+3=6,
$$

which agrees with the first computation.

I also check $\det B$ with Sarrus' rule. The three down-right products of $B$ are $0\cdot2\cdot1=0$, $3\cdot0\cdot2=0$ and $1\cdot1\cdot1=1$, giving a sum of $1$. The three down-left products are $1\cdot2\cdot2=4$, $3\cdot1\cdot1=3$ and $0\cdot0\cdot1=0$, giving a sum of $7$. Hence $\det B=1-7=-6$, again as predicted. Finally, the sign makes sense geometrically: the rows of $B$ are the rows of $A$ in the opposite orientation, so the signed volume changes sign while its size stays the same.

## Common mistakes

- Forgetting that the determinant of the swapped matrix is $-6$ and not $+6$, or the other way round.
- Applying the swap property to a matrix where two rows were actually exchanged more than once; two swaps would bring the sign back to $+$.
- Using the cofactor signs $+,-,+$ on the wrong row, for example $+,-,+$ on the second row where it must be $-,+,-$.
- Computing the minors of the first row of $B$ by deleting the wrong column, which silently changes every number in the expansion.

## How I would explain it in class

I expand the determinant of $A$ along its first row, where the signs are plus, minus, plus, and that gives $6$. Swapping two rows of a matrix changes the sign of its determinant and nothing else, because the rows swap orientation, so I predict $-6$ for $B$. Computing $\det B$ directly along its first row gives $0-3-3=-6$, exactly as predicted, and I also confirmed $6$ by elimination.
