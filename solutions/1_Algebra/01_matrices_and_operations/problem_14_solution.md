# Problem 14

## The original problem

The matrix for a rotation through an angle $\theta$ is

$$
R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}.
$$

Compute $R(\alpha)R(\beta)$ and, using the angle-sum formulas for sine and cosine, show that

$$
R(\alpha)R(\beta)=R(\alpha+\beta).
$$

Explain the result geometrically.

> **Why this exercise:** shows the consistency between matrix algebra and the geometry of composing rotations.

## What we are looking for

We need the product of two rotation matrices with angles $\alpha$ and $\beta$ written out entry by entry, then a proof that each entry equals the corresponding entry of $R(\alpha+\beta)$, and finally a geometric reading: what the equality says about turning a plane twice.

## The idea we need

The angle-sum formulas are

$$
\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,\qquad \sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta.
$$

The matrix $R(\theta)$ turns every vector in the plane by the angle $\theta$ counterclockwise about the origin; for example, it sends the vector $(1,0)$ to $(\cos\theta,\sin\theta)$. A product of matrices applied to a vector means: apply the right factor first, then the left factor.

## Step-by-step solution

**Step 1: write the product.**

$$
R(\alpha)R(\beta)=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}\begin{pmatrix}\cos\beta&-\sin\beta\\\sin\beta&\cos\beta\end{pmatrix}.
$$

**Step 2: compute the four entries (row times column).**

- Position $(1,1)$: $\cos\alpha\cos\beta+(-\sin\alpha)\sin\beta=\cos\alpha\cos\beta-\sin\alpha\sin\beta$.
- Position $(1,2)$: $\cos\alpha(-\sin\beta)+(-\sin\alpha)\cos\beta=-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)$.
- Position $(2,1)$: $\sin\alpha\cos\beta+\cos\alpha\sin\beta$.
- Position $(2,2)$: $\sin\alpha(-\sin\beta)+\cos\alpha\cos\beta=\cos\alpha\cos\beta-\sin\alpha\sin\beta$.

**Step 3: apply the angle-sum formulas.** The expression in positions $(1,1)$ and $(2,2)$ is $\cos(\alpha+\beta)$. The expression $\sin\alpha\cos\beta+\cos\alpha\sin\beta$ in position $(2,1)$ is $\sin(\alpha+\beta)$, and position $(1,2)$ is its negative. Therefore

$$
R(\alpha)R(\beta)=\begin{pmatrix}\cos(\alpha+\beta)&-\sin(\alpha+\beta)\\\sin(\alpha+\beta)&\cos(\alpha+\beta)\end{pmatrix}=R(\alpha+\beta).
$$

**Step 4: geometric meaning.** Apply $R(\alpha)R(\beta)$ to a vector $v$. First $R(\beta)$ turns $v$ by $\beta$, and then $R(\alpha)$ turns the result by a further $\alpha$, so in total the vector has been turned by $\alpha+\beta$. The equality says that the single matrix $R(\alpha+\beta)$ does the same job as the two rotations one after the other: composing rotations about the same point adds their angles. Since $\alpha+\beta=\beta+\alpha$, the order does not matter here, so $R(\alpha)R(\beta)=R(\beta)R(\alpha)$; rotations of the plane about the origin commute, unlike scalings and rotations combined (compare Problem 09).

## Why each step is valid

- Each entry in step 2 is computed by the row-times-column rule, with the minus signs carried carefully from the matrices.
- The angle-sum formulas are standard identities of trigonometry, valid for all real angles, so the equality of matrices holds for every $\alpha$ and $\beta$, not only for special values.
- Two matrices are equal exactly when all four entries agree; entries $(1,1)$ and $(2,2)$ agree by the cosine formula, and entries $(1,2)$ and $(2,1)$ by the sine formula.
- The geometric reading follows because the matrix $R(\theta)$ was defined as the rotation by $\theta$ and the product represents composition of transformations; the algebra confirms that this reading is consistent.

## Final answer (in words)

The product is $R(\alpha)R(\beta)=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\sin\alpha\cos\beta+\cos\alpha\sin\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}$, and by the angle-sum formulas this is $R(\alpha+\beta)$. Geometrically, rotating by $\beta$ and then by $\alpha$ is the same as rotating once by the sum $\alpha+\beta$, because angles of rotations about the same point add.

## Verification

A numerical check with $\alpha=\beta=45^\circ$: here $\cos45^\circ=\sin45^\circ=\frac{\sqrt2}{2}$, so the entries of $R(45^\circ)R(45^\circ)$ are $\frac12-\frac12=0$ in positions $(1,1)$ and $(2,2)$, $-(\frac12+\frac12)=-1$ in position $(1,2)$ and $1$ in position $(2,1)$. The result is $\begin{pmatrix}0&-1\\1&0\end{pmatrix}$, which is $R(90^\circ)$, as predicted. A second, independent check is to track one vector: $R(\beta)$ sends $(1,0)$ to $(\cos\beta,\sin\beta)$, and applying $R(\alpha)$ gives $(\cos\alpha\cos\beta-\sin\alpha\sin\beta,\;\sin\alpha\cos\beta+\cos\alpha\sin\beta)$, which is the first column of $R(\alpha+\beta)$, the point at angle $\alpha+\beta$ on the unit circle. Sympy confirmed that the difference $R(\alpha+\beta)-R(\alpha)R(\beta)$ is the zero matrix after expanding the trigonometric sums.

## Common mistakes

- Dropping the minus sign in position $(1,2)$, which leads to $\sin\alpha\cos\beta-\cos\alpha\sin\beta$ and the angle difference instead of the sum.
- Mixing up the sine formula and writing $\sin(\alpha+\beta)=\sin\alpha\sin\beta+\cos\alpha\cos\beta$.
- Adding the matrices entry by entry instead of multiplying them.
- Concluding that all transformations commute because rotations do; this is true for rotations about the same point, not in general.

## How I would explain it in class

Multiplying the two rotation matrices gives a matrix whose entries are $\cos\alpha\cos\beta-\sin\alpha\sin\beta$ and $\sin\alpha\cos\beta+\cos\alpha\sin\beta$, and these are exactly $\cos(\alpha+\beta)$ and $\sin(\alpha+\beta)$ by the angle-sum formulas, so the product is $R(\alpha+\beta)$. Geometrically, turning the plane by $\beta$ and then by $\alpha$ is the same as turning it once by $\alpha+\beta$. So the trigonometric identities are the algebraic way of saying that angles of rotations add.
