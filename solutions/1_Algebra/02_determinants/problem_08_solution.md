# Problem 08

## The original problem

Let $A,B$ be square matrices such that $\det A=3$ and $\det B=-5$. Compute

$$
\det(AB),\qquad \det(BA)
$$

and, if it exists, $\det(A^{-1}B)$. Explain why the first two results are equal even though usually $AB\neq BA$.

## What we are looking for

Three determinants, all built from the two known numbers $\det A=3$ and $\det B=-5$. The interesting part is the last question: the matrix $A^{-1}B$ only exists when $A$ can be inverted, so we must check that first and then use the determinant rules for products and inverses. Finally we have to explain the apparently paradoxical fact that $\det(AB)=\det(BA)$ although the matrices $AB$ and $BA$ themselves are usually different.

## The idea we need

**Product rule.** For square matrices of the same size,

$$\det(AB)=\det A\cdot\det B.$$

**Inverse rule.** A square matrix is invertible exactly when its determinant is not zero, and then

$$\det(A^{-1})=\frac{1}{\det A}.$$

This follows from the product rule applied to $A\cdot A^{-1}=I$: $\det A\cdot\det(A^{-1})=\det I=1$.

**Assumption of the exercise.** Since both products $AB$ and $BA$ appear, $A$ and $B$ must be square matrices of the *same* size; only then are the products defined at all.

## Step-by-step solution

**Step 1: $\det(AB)$.** By the product rule,

$$\det(AB)=\det A\cdot\det B=3\cdot(-5)=-15.$$

**Step 2: $\det(BA)$.** Again by the product rule, with the factors in the other order,

$$\det(BA)=\det B\cdot\det A=(-5)\cdot 3=-15.$$

**Step 3: does $A^{-1}B$ exist?** Yes. Since $\det A=3\neq 0$, the criterion for invertibility gives that $A$ has an inverse, so the product $A^{-1}B$ is a well-defined square matrix of the same size.

**Step 4: $\det(A^{-1}B)$.** First the determinant of the inverse, then the product rule:

$$\det(A^{-1}B)=\det(A^{-1})\cdot\det B=\frac{1}{\det A}\cdot\det B=\frac{1}{3}\cdot(-5)=-\frac{5}{3}.$$

**Step 5: why $\det(AB)=\det(BA)$ although $AB\neq BA$.** The determinant turns matrix multiplication into multiplication of ordinary numbers, and multiplication of real numbers is commutative. So

$$\det(AB)=\det A\cdot\det B=\det B\cdot\det A=\det(BA).$$

The determinant therefore "forgets" the order of the factors. The matrices $AB$ and $BA$ keep that order and can be different, but their determinants are always equal.

## Why each step is valid

- The product rule requires both matrices to be square of the same size, which is exactly the assumption made in the exercise.
- The invertibility of $A$ is not an extra hypothesis but a consequence of $\det A=3\neq 0$, so $A^{-1}B$ exists; this is why the exercise says "if it exists".
- The formula $\det(A^{-1})=1/\det A$ is obtained by applying the product rule to $A\cdot A^{-1}=I$ and using $\det I=1$, so no separate proof of the inverse formula is needed.
- The equality of the two products is an equality of real numbers, and real multiplication is commutative; this has nothing to do with matrix multiplication, which is *not* commutative.

## Final answer (in words)

The determinant of the product $AB$ is $-15$, and the determinant of the product $BA$ is $-15$ as well. The matrix $A^{-1}B$ does exist, because $A$ is invertible, and its determinant is $-\frac{5}{3}$. The two first values are equal because the determinant of a product is the product of the determinants, and products of ordinary numbers do not depend on the order of the factors.

$$\det(AB)=-15,\qquad \det(BA)=-15,\qquad \det(A^{-1}B)=-\frac{5}{3}.$$

## Verification

I check the third answer by multiplying back. Multiplying the known value by $\det A$ must give $\det B$ again:

$$\det A\cdot\det(A^{-1}B)=\det(A\cdot A^{-1}\cdot B)=\det(IB)=\det B=-5,$$

and indeed $3\cdot\left(-\tfrac{5}{3}\right)=-5$, so $\det(A^{-1}B)=-\tfrac{5}{3}$ is consistent.

I check the equality $\det(AB)=\det(BA)$ on an explicit pair for which the matrices really are different. Take

$$
A=\begin{pmatrix}3&0\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}-5&1\\0&1\end{pmatrix},
$$

which have $\det A=3$ and $\det B=-5$. Then

$$
AB=\begin{pmatrix}-15&3\\0&1\end{pmatrix},\qquad BA=\begin{pmatrix}-15&1\\0&1\end{pmatrix},
$$

so $AB\neq BA$, yet both determinants are $-15\cdot1-0= -15$, exactly the values predicted by the rules. In the same example $A^{-1}B=\begin{pmatrix}-\tfrac53&\tfrac13\\0&1\end{pmatrix}$ has determinant $-\tfrac{5}{3}$, again as predicted.

As a final consistency check, the signs agree: $\det B=-5$ is negative and $1/\det A=1/3$ is positive, so $\det(A^{-1}B)$ must be negative, which it is.

## Common mistakes

- Writing $\det(A^{-1})=-\det A$ or $\det(A^{-1})=1-\det A$ instead of $1/\det A$.
- Believing that $\det(AB)=\det(BA)$ implies $AB=BA$; the equality of determinants is much weaker than the equality of matrices.
- Forgetting to check that $A^{-1}$ exists at all; here it does, because $\det A=3\neq 0$.
- Applying the product rule to matrices of different sizes, for which the product is not even defined.

## How I would explain it in class

The determinant of a product is the product of the determinants, so $\det(AB)=\det(BA)=3\cdot(-5)=-15$, and this works although the matrices $AB$ and $BA$ are different because ordinary numbers can be multiplied in any order. Since $\det A=3$ is not zero, $A$ is invertible, so $A^{-1}B$ exists and its determinant is $\det(A^{-1})\det B=\tfrac13\cdot(-5)=-\tfrac53$. I verified the last value by multiplying back, since $3\cdot(-\tfrac53)=-5=\det B$.
