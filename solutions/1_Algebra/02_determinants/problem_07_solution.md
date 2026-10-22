# Problem 07

## The original problem

Suppose that for a $3\times3$ matrix, $\det A=-4$. Compute

$$
\det(2A),\qquad \det(A^T),\qquad \det(A^2),\qquad \det(-A).
$$

Justify each answer using the appropriate property.

## What we are looking for

Four determinants, all of them built from the single known number $\det A=-4$. The point of the exercise is not to compute anything by brute force but to use the four properties of the determinant that turn matrix operations into ordinary multiplication of numbers. Each answer must name the property that produces it, and the size $3\times3$ matters in two of them.

## The idea we need

Let $A$ be an $n\times n$ matrix, here $n=3$. We use four standard properties.

**1. Scaling the whole matrix.** Multiplying every entry of an $n\times n$ matrix by a number $c$ multiplies the determinant by $c^n$:

$$\det(cA)=c^n\det A.$$

The exponent $n$ appears because the determinant is multilinear in the rows: every term of the Leibniz sum contains one entry from each of the $n$ rows.

**2. Transpose.** A matrix and its transpose have the same determinant:

$$\det A^T=\det A.$$

**3. Product.** The determinant of a product is the product of the determinants:

$$\det(AB)=\det A\cdot\det B.$$

**4. Sign.** Multiplying the whole matrix by $-1$ is the same as scaling with $c=-1$:

$$\det(-A)=(-1)^n\det A.$$

For $n=3$ the odd exponent gives $\det(-A)=-\det A$.

## Step-by-step solution

**First: $\det(2A)$.** Here $c=2$ and $n=3$, so the scaling property gives

$$\det(2A)=2^3\det A=8\cdot(-4)=-32.$$

**Second: $\det(A^T)$.** The transpose property gives

$$\det(A^T)=\det A=-4.$$

**Third: $\det(A^2)$.** Note that $A^2$ means the matrix product $A\cdot A$. Applying the product property twice,

$$\det(A^2)=\det(A\cdot A)=\det A\cdot\det A=(-4)\cdot(-4)=16.$$

**Fourth: $\det(-A)$.** Using the scaling property with $c=-1$ and $n=3$,

$$\det(-A)=(-1)^3\det A=-1\cdot(-4)=4.$$

## Why each step is valid

- The scaling property requires the size of the matrix, and the exercise states that $A$ is $3\times3$, so the factor is $2^3=8$ and not $2$.
- The transpose property holds for every square matrix, so no additional hypothesis is needed here.
- The product property requires both matrices to be square of the same size; $A$ and $A$ satisfy this, so $\det(A^2)=\det A\cdot\det A$ is legitimate.
- The exponent in $(-1)^3$ comes from the same multilinearity as in the first part, so for an odd size the sign flips and for an even size it does not; here $3$ is odd, so $-\det A=4$ is correct.
- All four computations use only the known number $\det A=-4$; no entries of $A$ are needed, which is exactly what the exercise asks for.

## Final answer (in words)

The determinant of $2A$ is $-32$, the determinant of the transpose $A^T$ is $-4$, the determinant of the square $A^2$ is $16$, and the determinant of $-A$ is $4$. These come from the scaling property with the third power, the transpose property, the product property and the sign change for odd size, respectively.

$$\det(2A)=-32,\qquad \det(A^T)=-4,\qquad \det(A^2)=16,\qquad \det(-A)=4.$$

## Verification

I check all four answers on a concrete $3\times3$ matrix that really has determinant $-4$, namely

$$
A_0=\begin{pmatrix}-4&0&0\\0&1&0\\0&0&1\end{pmatrix},
$$

whose determinant is the product of the diagonal, $-4\cdot1\cdot1=-4$.

- $2A_0=\begin{pmatrix}-8&0&0\\0&2&0\\0&0&2\end{pmatrix}$ has determinant $-8\cdot2\cdot2=-32$, as claimed.
- $A_0^T=A_0$, so $\det A_0^T=-4$, as claimed.
- $A_0^2=\begin{pmatrix}16&0&0\\0&1&0\\0&0&1\end{pmatrix}$ has determinant $16$, as claimed.
- $-A_0=\begin{pmatrix}4&0&0\\0&-1&0\\0&0&-1\end{pmatrix}$ has determinant $4\cdot(-1)\cdot(-1)=4$, as claimed.

I also check the scaling factor directly from the Leibniz formula: each term of the determinant of a $3\times3$ matrix contains exactly three entries, so multiplying all entries by $2$ multiplies every term by $2^3=8$, and $-4\cdot8=-32$. Finally, $\det(A^2)=16>0$ is exactly what the rule $\det(A^2)=(\det A)^2$ predicts, and it is consistent with $A^2$ being invertible, whose determinant therefore cannot be zero.

## Common mistakes

- Using $\det(2A)=2\det A$ instead of $2^3\det A$, which would give $-8$ instead of $-32$.
- Forgetting that $A^2$ means the matrix product $A\cdot A$, and not the square of the number $-4$.
- Applying the rule $\det(-A)=-\det A$ without checking the size: for a $2\times2$ matrix the sign would *not* change.
- Believing that $\det(A^T)$ needs a minus sign or that it equals $-\det A$; the transpose keeps the value unchanged.

## How I would explain it in class

For an $n\times n$ matrix the determinant reacts to these four operations by simple rules, and since our matrix is $3\times3$ the powers matter. Scaling by $2$ multiplies the determinant by $2^3$, transposing leaves it unchanged, a product multiplies determinants, and multiplying by $-1$ flips the sign because $3$ is odd. Starting from $\det A=-4$ this gives $-32$, $-4$, $16$ and $4$, and I verified each one on an explicit diagonal matrix with determinant $-4$.
