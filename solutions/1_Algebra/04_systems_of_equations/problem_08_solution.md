# Problem 8

## The original problem

Solve by elimination the two systems
$$\begin{cases}2x+y=5,\\x-y=1,\end{cases}$$
$$\begin{cases}2x+y=1,\\x-y=4.\end{cases}$$
Compare the successive elimination steps. Which part of the calculation is the same in both cases, and why?

## What we are looking for

We must solve both $2\times2$ systems by elimination, then compare the steps to identify which part depends only on the coefficient matrix and is therefore identical in both.

## The idea we need

Elimination on $Ax=b$ acts on the coefficient part $A$ and the right-hand side $b$ together, but the multipliers and pivot positions are determined solely by $A$. Since both systems share the same $A$, the elimination structure (multipliers, row operations on the coefficient columns) is identical; only the right-hand side entries differ.

## Step-by-step solution

### System 1: $2x+y=5$, $x-y=1$

1. Augmented matrix:
$$\left[\begin{array}{cc|c}2&1&5\\1&-1&1\end{array}\right].$$

2. Eliminate: $R_2\leftarrow R_2-\frac12 R_1$:
$$\left[\begin{array}{cc|c}2&1&5\\0&-\frac32&1-\frac52\end{array}\right]
=\left[\begin{array}{cc|c}2&1&5\\0&-\frac32&-\frac32\end{array}\right].$$

3. From row 2: $-\frac32 y=-\frac32$, so $y=1$.

4. From row 1: $2x+1=5$, so $x=2$.

### System 2: $2x+y=1$, $x-y=4$

1. Augmented matrix:
$$\left[\begin{array}{cc|c}2&1&1\\1&-1&4\end{array}\right].$$

2. Same elimination: $R_2\leftarrow R_2-\frac12 R_1$:
$$\left[\begin{array}{cc|c}2&1&1\\0&-\frac32&4-\frac12\end{array}\right]
=\left[\begin{array}{cc|c}2&1&1\\0&-\frac32&\frac72\end{array}\right].$$

3. From row 2: $-\frac32 y=\frac72$, so $y=-\frac73$.

4. From row 1: $2x-\frac73=1$, so $2x=\frac{10}{3}$, giving $x=\frac53$.

### Comparison

The multiplier $\frac12$ and the resulting pivot $-\frac32$ in the coefficient columns are identical in both cases, because they depend only on $A$. The right-hand side updates differ ($1-\frac52$ vs $4-\frac12$) because they depend on $b$.

## Why each step is valid

The row operation $R_2-\frac12R_1$ is elementary and preserves the solution set in both systems. The multiplier $\frac12$ comes from $a_{21}/a_{11}=1/2$, which is a property of $A$ alone. Back substitution is valid because the reduced matrix is upper triangular.

## Final answer (in words)

System 1 has solution $(x,y)=(2,1)$. System 2 has solution $(x,y)=(\frac53,-\frac73)$. The elimination steps on the coefficient matrix are identical in both cases; only the right-hand side updates differ.

## Verification

- System 1: $2(2)+1=5$ and $2-1=1$.
- System 2: $2(\frac53)+(-\frac73)=\frac{10-7}{3}=1$ and $\frac53-(-\frac73)=\frac{12}{3}=4$.
Both check out.

## Common mistakes

- Recomputing the multiplier independently and getting different values.
- Confusing which part is shared (coefficients) with which part differs (right-hand side).
- Sign errors in back substitution.
- Not comparing the steps explicitly.

## How I would explain it in class

Both systems have the same coefficient matrix, so the elimination multipliers and pivots are identical. Only the right-hand side numbers change during elimination. That is why the coefficient-matrix work is reusable and only the right-hand side needs updating.
