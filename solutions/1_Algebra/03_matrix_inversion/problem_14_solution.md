# Problem 14

## The original problem

Assume that a square matrix $A$ satisfies
$$A^2=I.$$
Show that
$$A^{-1}=A.$$
Then give an example of a $2\times2$ matrix different from $I$ and $-I$ that satisfies this condition, and verify it by multiplication.

## What we are looking for

First a short proof: from the single equation $A^2=I$ we must conclude that $A$ is invertible and that its inverse is $A$ itself. Second, a concrete $2\times2$ matrix with $A^2=I$ that is neither the identity matrix $I$ nor $-I$, checked by direct multiplication.

## The idea we need

By definition, a square matrix $B$ is the inverse of $A$ if $AB=I$ and $BA=I$ (both products give the identity matrix $I$). So to show that $A$ is its own inverse we only need to show that the choice $B=A$ satisfies the definition. The inverse is unique, so once we have found a matrix that works, it is the inverse.

## Step-by-step solution

**Part 1: the proof.**

1. The assumption is $A^2=I$, which by the meaning of a power says $A\cdot A=I$.
2. Take $B=A$ in the definition. We need $AB=I$ and $BA=I$; both products equal $A\cdot A=A^2=I$.
3. Therefore $A$ is invertible and $A$ itself is an inverse of $A$. By uniqueness of the inverse, $A^{-1}=A$.

**Part 2: an example.** Take the matrix that swaps the two coordinates,
$$A=\begin{pmatrix}0&1\\1&0\end{pmatrix}.$$
It is different from $I$ and from $-I$, since its diagonal entries are $0$. Compute
$$A^2=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0\cdot0+1\cdot1&0\cdot1+1\cdot0\\1\cdot0+0\cdot1&1\cdot1+0\cdot0\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I.$$

## Why each step is valid

- The definition of the inverse requires products on both sides to be $I$. For general matrices the two products can be different, but here both are the very same product $A\cdot A$, so no extra work is needed.
- Uniqueness of the inverse: if $B$ and $C$ are both inverses of $A$, then $B=BI=B(AC)=(BA)C=IC=C$. This is why we may write $A^{-1}=A$ and not just "$A$ is an inverse".
- The example is legitimate because it satisfies $A^2=I$ and is visibly not $\pm I$; the condition $A^2=I$ does not force $A$ to be $\pm I$. Geometrically, $A$ reflects the plane in the line $y=x$, and reflecting twice returns every point to where it started.

## Final answer (in words)

If $A^2=I$, then multiplying $A$ by itself gives the identity, so $A$ is invertible and its inverse is $A$ itself: $A^{-1}=A$. An example is the swap matrix $A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which is not $\pm I$ and satisfies $A^2=I$.

## Verification

The multiplication above shows $A^2=I$ for the example. As an independent check use the $2\times2$ inverse formula: $\det A=0\cdot0-1\cdot1=-1$, so
$$A^{-1}=\frac1{-1}\begin{pmatrix}0&-1\\-1&0\end{pmatrix}=\begin{pmatrix}0&1\\1&0\end{pmatrix}=A,$$
which agrees with $A^{-1}=A$. A second example, to show the phenomenon is not special: $C=\begin{pmatrix}1&1\\0&-1\end{pmatrix}$ gives $C^2=\begin{pmatrix}1+0&1-1\\0&1\end{pmatrix}=I$. A quick action test on the vector $(3,5)^T$: the swap matrix gives $(5,3)^T$, and applying it again returns $(3,5)^T$.

## Common mistakes

- Concluding that $A^2=I$ forces $A=I$ or $A=-I$; as in the example, other matrices also work (the real-number intuition $x^2=1\Rightarrow x=\pm1$ fails for matrices).
- Picking a diagonal example such as $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ and arguing it is "different from $I$ and $-I$" but not checking the product; that example does work, but the check must be shown.
- Checking only $A^2=I$ numerically but not stating why this proves $A^{-1}=A$.
- Choosing $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, whose square is $-I$, not $I$.

## How I would explain it in class

The inverse of $A$ is by definition a matrix that gives $I$ when multiplied with $A$ on either side, and the condition $A^2=A\cdot A=I$ says exactly that $A$ itself does the job, so $A^{-1}=A$. A simple example is the swap matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, which is not $I$ or $-I$, and multiplying it by itself gives $I$. Geometrically it is a reflection in the line $y=x$, and doing the same reflection twice brings every point back.
