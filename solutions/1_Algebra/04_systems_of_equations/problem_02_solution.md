# Problem 2

## The original problem

Solve using Gaussian elimination:
$$\begin{cases}x+y+z=6,\\2x-y+z=3,\\x+2y-z=2.\end{cases}$$
After solving, substitute the result into all equations and check consistency.

## What we are looking for

We need the single triple $(x,y,z)$ that satisfies all three equations. Gaussian elimination will reduce the system to an upper-triangular form, after which back substitution gives the values.

## The idea we need

Gaussian elimination uses elementary row operations on the augmented matrix. These operations do not change the solution set. Once the matrix is in row echelon form, the last nonzero row gives one variable, and we substitute upward. The operations are: swapping rows, multiplying a row by a nonzero scalar, and adding a multiple of one row to another.

## Step-by-step solution

1. Write the augmented matrix:

$$\left[\begin{array}{ccc|c}1&1&1&6\\2&-1&1&3\\1&2&-1&2\end{array}\right].$$

2. Eliminate below the first pivot: $R_2\leftarrow R_2-2R_1$, $R_3\leftarrow R_3-R_1$:

$$\left[\begin{array}{ccc|c}1&1&1&6\\0&-3&-1&-9\\0&1&-2&-4\end{array}\right].$$

3. Swap $R_2$ and $R_3$ to get a simpler pivot:

$$\left[\begin{array}{ccc|c}1&1&1&6\\0&1&-2&-4\\0&-3&-1&-9\end{array}\right].$$

4. Eliminate below the second pivot: $R_3\leftarrow R_3+3R_2$:

$$\left[\begin{array}{ccc|c}1&1&1&6\\0&1&-2&-4\\0&0&-7&-21\end{array}\right].$$

5. Back substitute. From the last row: $-7z=-21$, so $z=3$.

6. Second row: $y-2z=-4$, so $y-6=-4$, giving $y=2$.

7. First row: $x+y+z=6$, so $x+2+3=6$, giving $x=1$.

## Why each step is valid

Elementary row operations produce a system with the same solution set, so the reduced system is equivalent to the original. Back substitution is valid because each row expresses one variable in terms of already known values. The final values satisfy all three original equations by direct substitution.

## Final answer (in words)

The system has exactly one solution: the point $(x,y,z)=(1,2,3)$ in $\mathbb{R}^3$.

## Verification

Substitute into the equations:
- $1+2+3=6$,
- $2(1)-2+3=3$,
- $1+2(2)-3=2$.
All three hold, so the solution is consistent.

## Common mistakes

- Forgetting to apply the row operation to the right-hand side.
- Sign errors when subtracting rows.
- Stopping at row echelon form without back substituting.
- Not checking the result in all original equations.

## How I would explain it in class

I reduce the augmented matrix with row operations until it is upper triangular. Then I read off $z$, substitute into the row above for $y$, and into the top row for $x$. Finally I plug $(1,2,3)$ into all three equations to confirm.
