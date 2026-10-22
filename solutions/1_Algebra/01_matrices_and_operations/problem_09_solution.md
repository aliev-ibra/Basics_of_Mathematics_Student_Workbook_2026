# Problem 09

## The original problem

Let

$$
S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$

The matrix $S$ describes nonuniform scaling, while $R$ describes a $90^\circ$ counterclockwise rotation.
For

$$
x=\begin{pmatrix}1\\2\end{pmatrix}
$$

compute $RSx$ and $SRx$. Compare the results and explain geometrically why the order of these transformations matters.

> **Why this exercise:** interprets matrix multiplication as composition of transformations.

## What we are looking for

We need two vectors in the plane: $RSx$ (first scale, then rotate) and $SRx$ (first rotate, then scale). Then we must compare them and give a geometric reason why they differ.

## The idea we need

Multiplying a matrix by a vector applies the transformation to the vector. In a product such as $RSx$ the matrix nearest to $x$ acts first: $RSx=R(Sx)$, so $S$ acts first and $R$ acts afterwards. The matrix $S$ stretches the horizontal coordinate by the factor $2$ and leaves the vertical coordinate unchanged. The matrix $R$ turns every vector by $90^\circ$ counterclockwise, sending $(p,q)$ to $(-q,p)$.

## Step-by-step solution

**Step 1: $RSx$.** First scale: $Sx=\begin{pmatrix}2\cdot1+0\cdot2\\0\cdot1+1\cdot2\end{pmatrix}=\begin{pmatrix}2\\2\end{pmatrix}$. Then rotate: $R\begin{pmatrix}2\\2\end{pmatrix}=\begin{pmatrix}0\cdot2-1\cdot2\\1\cdot2+0\cdot2\end{pmatrix}=\begin{pmatrix}-2\\2\end{pmatrix}$.

**Step 2: $SRx$.** First rotate: $Rx=\begin{pmatrix}0\cdot1-1\cdot2\\1\cdot1+0\cdot2\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$. Then scale: $S\begin{pmatrix}-2\\1\end{pmatrix}=\begin{pmatrix}2\cdot(-2)\\1\end{pmatrix}=\begin{pmatrix}-4\\1\end{pmatrix}$.

**Step 3: compare.**

$$
RSx=\begin{pmatrix}-2\\2\end{pmatrix}\neq\begin{pmatrix}-4\\1\end{pmatrix}=SRx.
$$

**Step 4: geometric explanation.** The scaling $S$ stretches only along the horizontal axis. In $RSx$ the vector $(1,2)$ is stretched horizontally while it still points in its original direction, becoming $(2,2)$, and then it is turned to $(-2,2)$. In $SRx$ the vector is first turned to $(-2,1)$, and now the stretch acts on the turned vector: its horizontal part $-2$ is doubled, which gives $(-4,1)$. The same stretch is applied to different parts of the vector, because rotation changes which part of the vector lies along the horizontal axis. As a check on lengths: a rotation never changes length, but the stretch does. The length of $RSx$ is $\sqrt{(-2)^2+2^2}=\sqrt8$ and the length of $SRx$ is $\sqrt{(-4)^2+1^2}=\sqrt{17}$, so the two compositions cannot be the same transformation.

## Why each step is valid

- A product of matrices applied to a vector is evaluated from the right: $RSx=R(Sx)$, by associativity and by the definition of the product as composition. That is why in $RSx$ the scaling happens first.
- Each matrix-vector product is computed with the usual row-times-column rule, and the rotation rule $(p,q)\mapsto(-q,p)$ agrees with the matrix $R$, which sends the first basis vector $(1,0)$ to $(0,1)$ and the second basis vector $(0,1)$ to $(-1,0)$.
- A single example where the results differ is enough to prove that the two orders are not interchangeable in general.

## Final answer (in words)

$RSx=\begin{pmatrix}-2\\2\end{pmatrix}$ and $SRx=\begin{pmatrix}-4\\1\end{pmatrix}$, so the two results are different. The order matters because the nonuniform scaling stretches only the horizontal direction: applied before the rotation it stretches the original vector, and applied after the rotation it stretches the rotated vector, and these are different vectors. Hence $RS\neq SR$.

## Verification

First I compute the two product matrices and apply them directly to $x$. $RS=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix}=\begin{pmatrix}0&-1\\2&0\end{pmatrix}$, and $\begin{pmatrix}0&-1\\2&0\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=\begin{pmatrix}-2\\2\end{pmatrix}$, which matches. Likewise $SR=\begin{pmatrix}2&0\\0&1\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}0&-2\\1&0\end{pmatrix}$, and $\begin{pmatrix}0&-2\\1&0\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=\begin{pmatrix}-4\\1\end{pmatrix}$, which matches. The matrices $RS$ and $SR$ already differ in their entries, so they differ as transformations. Second, the length check above gives $\sqrt8\neq\sqrt{17}$, which is a geometric confirmation independent of the computation of the coordinates.

## Common mistakes

- Reading $RSx$ from left to right and applying $R$ first; the matrix next to $x$ acts first.
- Treating rotation and scaling as commuting operations because they commute for the uniform scaling by the same factor in all directions (which is a special case only).
- Rotating by $90^\circ$ clockwise, giving $(q,-p)$, instead of counterclockwise, giving $(-q,p)$.
- Concluding that the two vectors differ only because of a numerical slip; the product matrices $RS$ and $SR$ show the difference in a structural way.

## How I would explain it in class

Each matrix is a machine acting on a vector, and in $RSx$ the machine nearest to $x$ works first, so we scale $(1,2)$ to $(2,2)$ and then rotate to $(-2,2)$. If we rotate first we get $(-2,1)$, and the scaling then doubles the horizontal part and gives $(-4,1)$. The results differ because the stretch only acts along the horizontal axis, and the rotation changes which part of the vector lies along that axis, so the order of the transformations matters.
