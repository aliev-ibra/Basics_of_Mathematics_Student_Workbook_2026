# Problem 07

## The original problem

For

$$
A=\begin{pmatrix}2&1\\0&2\end{pmatrix}
$$

compute

$$
AI,\qquad IA,\qquad A+0,\qquad A^2,\qquad A^3.
$$

Explain the roles of the matrices $I$ and $0$, and describe the pattern you observe in successive powers of $A$.

> **Why this exercise:** organizes the roles of neutral elements and reveals regularity in successive powers of a matrix.

## What we are looking for

We need five matrices: $AI$, $IA$, $A+0$, $A^2$ and $A^3$, where $I$ is the $2\times2$ identity matrix and $0$ is the $2\times2$ zero matrix. We also need to say in words what $I$ and $0$ do, and to describe how the entries of $A^n$ change as $n$ grows.

## The idea we need

**Identity matrix.** $I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ has ones on the diagonal and zeros elsewhere. It plays the role of the number $1$ in multiplication: multiplying by it, on either side, changes nothing.

**Zero matrix.** $0=\begin{pmatrix}0&0\\0&0\end{pmatrix}$ has all entries zero. It plays the role of the number $0$ in addition: adding it changes nothing.

**Powers.** $A^2=A\cdot A$ and $A^3=A^2\cdot A$. Each power is obtained by multiplying by $A$ once more.

## Step-by-step solution

**Step 1: $AI$ and $IA$.** Row by column:

$$
AI=\begin{pmatrix}2\cdot1+1\cdot0&2\cdot0+1\cdot1\\0\cdot1+2\cdot0&0\cdot0+2\cdot1\end{pmatrix}=\begin{pmatrix}2&1\\0&2\end{pmatrix},
$$

$$
IA=\begin{pmatrix}1\cdot2+0\cdot0&1\cdot1+0\cdot2\\0\cdot2+1\cdot0&0\cdot1+1\cdot2\end{pmatrix}=\begin{pmatrix}2&1\\0&2\end{pmatrix}.
$$

Both equal $A$.

**Step 2: $A+0$.** Adding entry by entry gives $\begin{pmatrix}2+0&1+0\\0+0&2+0\end{pmatrix}=\begin{pmatrix}2&1\\0&2\end{pmatrix}=A$.

**Step 3: $A^2$.**

$$
A^2=\begin{pmatrix}2&1\\0&2\end{pmatrix}\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}2\cdot2+1\cdot0&2\cdot1+1\cdot2\\0\cdot2+2\cdot0&0\cdot1+2\cdot2\end{pmatrix}=\begin{pmatrix}4&4\\0&4\end{pmatrix}.
$$

**Step 4: $A^3$.** Multiply $A^2$ by $A$:

$$
A^3=\begin{pmatrix}4&4\\0&4\end{pmatrix}\begin{pmatrix}2&1\\0&2\end{pmatrix}=\begin{pmatrix}4\cdot2+4\cdot0&4\cdot1+4\cdot2\\0\cdot2+4\cdot0&0\cdot1+4\cdot2\end{pmatrix}=\begin{pmatrix}8&12\\0&8\end{pmatrix}.
$$

**Step 5: the pattern.** Collect the powers:

$$
A^1=\begin{pmatrix}2&1\\0&2\end{pmatrix},\quad A^2=\begin{pmatrix}4&4\\0&4\end{pmatrix},\quad A^3=\begin{pmatrix}8&12\\0&8\end{pmatrix}.
$$

The diagonal entries are $2,4,8$, that is $2^n$. The lower left entry stays $0$. The upper right entries are $1,4,12$, which equal $n\cdot2^{n-1}$ (for $n=1$: $1\cdot1$; for $n=2$: $2\cdot2$; for $n=3$: $3\cdot4$). This suggests

$$
A^n=\begin{pmatrix}2^n&n\,2^{n-1}\\0&2^n\end{pmatrix}.
$$

This is a pattern seen in three cases, so it is a conjecture; the verification below explains why it is true.

## Why each step is valid

- $AI=A$ and $IA=A$ because each entry of the product is a row-column sum in which the identity contributes a single $1$ and zeros, so the matching entry of $A$ is copied. Because it works on the left and on the right, $I$ is a two-sided neutral element for multiplication.
- $A+0=A$ because addition is entry by entry and adding the number $0$ to an entry leaves it unchanged. So $0$ is the neutral element for addition.
- $A^2$ and $A^3$ are by definition repeated products; writing $A^3=A^2A$ is allowed because multiplication is associative, so it does not matter how the three factors are grouped.
- The pattern is read off from the entries; it is a guess supported by the three computed cases, and it is justified in the next section.

## Final answer (in words)

$AI=IA=A$ and $A+0=A$: the identity matrix is the neutral element of multiplication and the zero matrix is the neutral element of addition. The powers are $A^2=\begin{pmatrix}4&4\\0&4\end{pmatrix}$ and $A^3=\begin{pmatrix}8&12\\0&8\end{pmatrix}$. In successive powers the diagonal entries double each time (they are $2^n$), the lower left entry stays zero, and the upper right entry equals $n\cdot2^{n-1}$, so $A^n=\begin{pmatrix}2^n&n2^{n-1}\\0&2^n\end{pmatrix}$.

## Verification

An independent explanation of the pattern: write $A=2I+N$ with $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Then $N^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}$ (the single $1$ of $N$ is multiplied by a zero). Since $2I$ and $N$ commute, the binomial expansion applies, and every term containing $N^2$ or a higher power vanishes, leaving $A^n=(2I)^n+n(2I)^{n-1}N=2^nI+n2^{n-1}N$, which is exactly the matrix in the conjecture. As a numerical test of the formula, $A^4$ from the formula is $\begin{pmatrix}16&32\\0&16\end{pmatrix}$, and multiplying $A^3$ by $A$ gives $\begin{pmatrix}8\cdot2&8\cdot1+12\cdot2\\0&16\end{pmatrix}=\begin{pmatrix}16&32\\0&16\end{pmatrix}$, the same. A further check is the determinant: $\det A=4$, so $\det A^3$ must be $4^3=64$, and the computed $A^3$ has determinant $8\cdot8-12\cdot0=64$.

## Common mistakes

- Squaring entry by entry and writing $A^2=\begin{pmatrix}4&1\\0&4\end{pmatrix}$; matrix powers use matrix multiplication.
- Using the zero matrix as a neutral element for multiplication; $A\cdot0=0$, not $A$.
- Using a matrix of all ones instead of the identity matrix.
- Stating the pattern for the upper right entry as $2^{n-1}$ or $n+1$ after seeing only the first power.

## How I would explain it in class

The identity matrix $I$ leaves a matrix unchanged under multiplication, like the number $1$, and the zero matrix leaves it unchanged under addition, like the number $0$; so $AI=IA=A+0=A$. Multiplying out gives $A^2=\begin{pmatrix}4&4\\0&4\end{pmatrix}$ and $A^3=\begin{pmatrix}8&12\\0&8\end{pmatrix}$, where the diagonal doubles each time and the corner entry grows as $n\cdot2^{n-1}$. The reason is that $A=2I+N$ with $N^2=0$, so only the first two terms of the binomial expansion survive.
