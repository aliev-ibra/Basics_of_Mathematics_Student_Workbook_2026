# Problem 09

## The original problem

The vectors
$$
u=\begin{pmatrix}3\\1\end{pmatrix},\qquad v=\begin{pmatrix}1\\4\end{pmatrix}
$$
span a parallelogram. Compute its area using a determinant. Then reverse the order of the vectors and explain what changes in the determinant and what does not change in the area.

## What we are looking for

We want the area of the parallelogram whose two sides are the arrows $u$ and $v$ drawn from the same starting point. We must obtain it from a determinant. We must also compute the determinant with the vectors in the opposite order and say what is different (the sign) and what is the same (the area).

## The idea we need

**Area as a determinant.** If two vectors in the plane are written as the columns of a $2\times2$ matrix, then the absolute value of the determinant of that matrix is the area of the parallelogram they span:
$$
\text{area}=\left|\det\begin{pmatrix}u_1&v_1\\u_2&v_2\end{pmatrix}\right|=|u_1v_2-v_1u_2|.
$$
Here $u_1,u_2$ are the two entries of $u$ and $v_1,v_2$ are the two entries of $v$. The determinant itself can be negative, but an area is never negative, which is why we take the absolute value. A negative determinant only records that going from the first vector to the second turns clockwise instead of counterclockwise.

## Step-by-step solution

**Step 1: build the matrix.** Put $u$ in the first column and $v$ in the second column:
$$
M=\begin{pmatrix}3&1\\1&4\end{pmatrix}.
$$

**Step 2: compute the determinant.** For a $2\times2$ matrix, the determinant is the product of the main diagonal minus the product of the other diagonal:
$$
\det M=3\cdot4-1\cdot1=12-1=11.
$$

**Step 3: take the area.** Since $11>0$, the area is $|11|=11$ square units.

**Step 4: reverse the order.** Now put $v$ first and $u$ second:
$$
M'=\begin{pmatrix}1&3\\4&1\end{pmatrix},\qquad \det M'=1\cdot1-3\cdot4=1-12=-11.
$$
The matrix $M'$ is $M$ with its two columns swapped, so we expected the determinant to change sign, and it did. The area is $|-11|=11$, the same as before.

## Why each step is valid

- Using columns (rather than rows) is a convention; the determinant of a matrix equals the determinant of its transpose, so rows would give the same number.
- The determinant formula $ad-bc$ for $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ is the standard $2\times2$ rule.
- Swapping two columns multiplies the determinant by $-1$, exactly like swapping two rows. That explains why $11$ became $-11$.
- The parallelogram spanned by $v,u$ is the same set of points as the one spanned by $u,v$, because the sides are the same two segments. So its area cannot change, and the absolute value removes the sign.

## Final answer (in words)

The parallelogram has area $11$ square units. With the order $(u,v)$ the determinant is $11$; with the order $(v,u)$ the determinant is $-11$. The sign of the determinant changes because swapping two columns flips it, while the area stays $11$ because it is the absolute value and the shape is the same.

$$
\det\begin{pmatrix}3&1\\1&4\end{pmatrix}=11,\qquad \det\begin{pmatrix}1&3\\4&1\end{pmatrix}=-11,\qquad \text{area}=11.
$$

## Verification

I compute the area without any determinant, using lengths and the dot product. The squared lengths are $|u|^2=3^2+1^2=10$ and $|v|^2=1^2+4^2=17$, and the dot product is $u\cdot v=3\cdot1+1\cdot4=7$. The area of a parallelogram is $|u||v|\sin\theta$, where $\theta$ is the angle between the vectors, and $\cos\theta=\dfrac{u\cdot v}{|u||v|}$. Hence
$$
\text{area}^2=|u|^2|v|^2\sin^2\theta=|u|^2|v|^2-(u\cdot v)^2=10\cdot17-49=170-49=121,
$$
so the area is $\sqrt{121}=11$. This agrees with the determinant.

## Common mistakes

- Reporting the area as $-11$. An area cannot be negative, so always take the absolute value.
- Computing $3\cdot1-1\cdot4=-1$ by mixing up which entries lie on which diagonal. The diagonal product is $3\cdot4$, using the first entry of $u$ and the second entry of $v$.
- Saying that reversing the vectors changes the area. It changes only the sign of the determinant.
- Forgetting the units: the answer is $11$ square units, not $11$ units of length.

## How I would explain it in class

Put the two vectors side by side as columns of a $2\times2$ matrix and compute $3\cdot4-1\cdot1=11$, which is the area of the parallelogram because an area is the absolute value of that determinant. If I swap the vectors I swap two columns, so the determinant becomes $-11$, but the parallelogram is the same shape, so the area is still $11$. As a separate check, the formula $\sqrt{10\cdot17-7^2}=\sqrt{121}=11$ gives the same area without any determinant.
