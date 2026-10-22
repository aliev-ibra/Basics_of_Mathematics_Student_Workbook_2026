# Problem 10

## The original problem

Given
$$D=\begin{pmatrix}2&0&0\\0&-3&0\\0&0&5\end{pmatrix},\qquad E=\begin{pmatrix}2&0&0\\0&0&0\\0&0&5\end{pmatrix}.$$
Without using Gauss–Jordan elimination, decide which matrix is invertible. For the invertible matrix, give the inverse and check the result by multiplication.

## What we are looking for

We must decide which of the two diagonal matrices $D$ and $E$ has an inverse, give a reason that does not need a full elimination procedure, write down the inverse of the invertible one, and confirm it by multiplication.

## The idea we need

A diagonal matrix has nonzero entries only on the main diagonal. Its determinant is the product of the diagonal entries, and it is invertible exactly when all diagonal entries are nonzero. In that case the inverse is again diagonal, with each diagonal entry replaced by its reciprocal $1/d_i$. The reason is that multiplying two diagonal matrices just multiplies the matching diagonal entries, so $d_i\cdot\frac1{d_i}=1$ gives the identity on the diagonal.

## Step-by-step solution

**Step 1: look at the diagonal of $D$.** The entries are $2,-3,5$, none of them zero, so $\det D=2\cdot(-3)\cdot5=-30\neq0$ and $D$ is invertible.

**Step 2: look at the diagonal of $E$.** The entries are $2,0,5$. The middle entry is zero, so $\det E=2\cdot0\cdot5=0$ and $E$ is not invertible. Another way to see it: the second row of $E$ consists only of zeros, so the rows are linearly dependent, and every product $EY$ has a zero second row and can never equal $I$ (whose second row is $(0,1,0)$).

**Step 3: write the inverse of $D$.** Replace each diagonal entry by its reciprocal:
$$D^{-1}=\begin{pmatrix}\frac12&0&0\\0&-\frac13&0\\0&0&\frac15\end{pmatrix}.$$

## Why each step is valid

- A nonzero determinant is the criterion for invertibility, and for a diagonal matrix the determinant is simply the product of the diagonal entries, so the test is immediate.
- For $E$ the zero row is a direct obstruction: a matrix with a zero row sends every vector to something with a zero second coordinate, so it cannot be undone.
- For $D$ the candidate $D^{-1}$ works because the product of two diagonal matrices has diagonal entries $d_ie_i$ and zeros elsewhere; the diagonal entries are $2\cdot\frac12$, $(-3)\cdot(-\frac13)$, $5\cdot\frac15$, all equal to $1$.

## Final answer (in words)

The matrix $D$ is invertible and $E$ is not, because $E$ has a zero on its diagonal (determinant $0$). The inverse of $D$ is the diagonal matrix of reciprocals
$$D^{-1}=\begin{pmatrix}\frac12&0&0\\0&-\frac13&0\\0&0&\frac15\end{pmatrix}.$$

## Verification

I multiply $D$ by $D^{-1}$:
$$DD^{-1}=\begin{pmatrix}2&0&0\\0&-3&0\\0&0&5\end{pmatrix}\begin{pmatrix}\frac12&0&0\\0&-\frac13&0\\0&0&\frac15\end{pmatrix}
=\begin{pmatrix}2\cdot\frac12&0&0\\0&(-3)(-\frac13)&0\\0&0&5\cdot\frac15\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}.$$
The product in the other order, $D^{-1}D$, is also $I$ because diagonal matrices commute. As a determinant check, $\det D^{-1}=\frac12\cdot(-\frac13)\cdot\frac15=-\frac1{30}=\frac1{\det D}$, as it must be.

## Common mistakes

- Taking the reciprocal of the zero entry of $E$ and writing "$\frac10$"; division by zero is not allowed, and that is exactly why $E$ has no inverse.
- Forgetting the sign: the inverse of $-3$ is $-\frac13$, not $\frac13$.
- Inverting the matrix as a whole, for example writing $-D$ or $D$ with entries negated, instead of taking reciprocals of the diagonal entries.
- Thinking that a matrix with many zeros is automatically non-invertible; $D$ has six zeros and is still invertible.

## How I would explain it in class

For a diagonal matrix I just read the diagonal: if no entry is zero the matrix is invertible, and the inverse has the reciprocals on the diagonal. So $D$ with $2,-3,5$ is invertible with inverse $\mathrm{diag}\left(\frac12,-\frac13,\frac15\right)$, while $E$ has a zero on the diagonal and therefore a zero row, so it cannot be inverted. Multiplying $D$ by its inverse gives $I$, which confirms the answer.
