# Problem 11

## The original problem

Given

$$
A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
$$

Find the conditions on $a,b,c,d$ under which $AB=BA$. Describe the general form of all such matrices $B$.

> **Why this exercise:** deepens the idea of noncommutativity by finding the conditions under which commutativity does hold.

## What we are looking for

We want all $2\times2$ matrices $B$ with unknown entries $a,b,c,d$ (any real numbers) for which multiplying by $A$ on the left gives the same matrix as multiplying by $A$ on the right. The answer is a set of equations on $a,b,c,d$, and then a description of the matrices that satisfy them.

## The idea we need

Two matrices are equal exactly when all four corresponding entries are equal. So we compute $AB$ and $BA$ with the unknown entries, set the four entries equal, and solve the resulting equations. The product is computed by the usual rule: the entry in row $i$, column $j$ is row $i$ of the left factor times column $j$ of the right factor.

## Step-by-step solution

**Step 1: $AB$.**

$$
AB=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}a&b\\c&d\end{pmatrix}=\begin{pmatrix}1\cdot a+1\cdot c&1\cdot b+1\cdot d\\0\cdot a+1\cdot c&0\cdot b+1\cdot d\end{pmatrix}=\begin{pmatrix}a+c&b+d\\c&d\end{pmatrix}.
$$

**Step 2: $BA$.**

$$
BA=\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}a\cdot1+b\cdot0&a\cdot1+b\cdot1\\c\cdot1+d\cdot0&c\cdot1+d\cdot1\end{pmatrix}=\begin{pmatrix}a&a+b\\c&c+d\end{pmatrix}.
$$

**Step 3: equate the entries.**

- Position $(1,1)$: $a+c=a$, which gives $c=0$.
- Position $(1,2)$: $b+d=a+b$, which gives $d=a$.
- Position $(2,1)$: $c=c$, which is always true.
- Position $(2,2)$: $d=c+d$, which gives $c=0$.

**Step 4: the conditions.** The only restrictions are $c=0$ and $d=a$; the numbers $a$ and $b$ are free. Therefore

$$
B=\begin{pmatrix}a&b\\0&a\end{pmatrix},\qquad a,b\ \text{arbitrary}.
$$

**Step 5: another description.** Since $A=I+N$ with $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$, we can write $B=aI+bN=(a-b)I+bA$. So the matrices commuting with $A$ are exactly the combinations $pI+qA$ of the identity matrix and $A$ itself (with $p=a-b$ and $q=b$).

## Why each step is valid

- Equality of matrices means equality of all entries, so the four entry equations are necessary and sufficient for $AB=BA$; nothing is lost or added in step 3.
- Each equation was solved by cancelling the same term from both sides ($a$ in the first, $b$ in the second, $d$ in the fourth), which is legitimate because we are working with ordinary numbers.
- The equation in position $(2,1)$ gives no condition, so $b$ is completely unrestricted, and the conditions $c=0$, $d=a$ do not involve $b$.
- The decomposition in step 5 is only a rewriting: $(a-b)I+bA=(a-b)I+bI+bN=aI+bN$.

## Final answer (in words)

The equality $AB=BA$ holds exactly when $c=0$ and $d=a$, with $a$ and $b$ arbitrary. So the matrices that commute with $A$ are precisely the upper triangular matrices with equal diagonal entries,

$$
B=\begin{pmatrix}a&b\\0&a\end{pmatrix},
$$

which can also be written as $B=pI+qA$ for numbers $p,q$.

## Verification

I substitute the answer back. For $B=\begin{pmatrix}a&b\\0&a\end{pmatrix}$ we get $AB=\begin{pmatrix}a&b+a\\0&a\end{pmatrix}$ and $BA=\begin{pmatrix}a&a+b\\0&a\end{pmatrix}$, which are equal. A numerical example: $a=2$, $b=5$ gives $AB=\begin{pmatrix}2&7\\0&2\end{pmatrix}=BA$.

To see that the conditions are really needed, take a matrix violating them, for example $B=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ (so $c=1$). Then $AB=\begin{pmatrix}1&0\\1&0\end{pmatrix}$ and $BA=\begin{pmatrix}0&0\\1&1\end{pmatrix}$, which differ. The second example, with $d\neq a$, namely $B=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, gives $AB=\begin{pmatrix}1&2\\0&2\end{pmatrix}$ and $BA=\begin{pmatrix}1&1\\0&2\end{pmatrix}$, again different.

## Common mistakes

- Concluding that $B$ must be a multiple of $I$, which loses the free parameter $b$.
- Writing only the equation $a+c=a$ and forgetting to use the remaining entries, so that $d=a$ is missed.
- Computing $BA$ by copying the entries of $AB$ with a sign change instead of multiplying again.
- Treating the equation $c=c$ as a mistake instead of recognising that it gives no restriction.

## How I would explain it in class

We multiply $A$ and $B$ in both orders with unknown entries and get $AB=\begin{pmatrix}a+c&b+d\\c&d\end{pmatrix}$ and $BA=\begin{pmatrix}a&a+b\\c&c+d\end{pmatrix}$, and then we ask that the four entries agree. This forces $c=0$ and $d=a$ while $a$ and $b$ stay free, so $B=\begin{pmatrix}a&b\\0&a\end{pmatrix}$. In other words, only the matrices of the form $pI+qA$ commute with $A$, and a generic matrix does not.
