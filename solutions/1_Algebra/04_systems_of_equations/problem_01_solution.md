# Problem 1

## The original problem

Write the system
$$\begin{cases}2x-y+z=4,\\x+3y-2z=1,\\3x+y+z=7.\end{cases}$$
in the form $Ax=b$.
Identify the coefficient matrix, the vector of unknowns, and the right-hand side vector. Explain how each row of the matrix corresponds to one equation.

## What we are looking for

We must translate a system of three linear equations in three unknowns into a single matrix equation $Ax=b$. The answer names the matrix $A$, the vector $x$ of unknowns, and the vector $b$ of constants, and explains the row-by-row correspondence.

## The idea we need

A system $a_{i1}x_1+\dots+a_{in}x_n=b_i$ for $i=1,\dots,m$ is written as $Ax=b$, where $A$ is the $m\times n$ matrix of coefficients $a_{ij}$, $x$ is the column vector of unknowns, and $b$ is the column vector of right-hand sides. Row $i$ of $A$ contains exactly the coefficients of equation $i$.

## Step-by-step solution

1. Read the coefficients of $x$, $y$, $z$ from each equation in order:

$$A=\begin{pmatrix}2&-1&1\\1&3&-2\\3&1&1\end{pmatrix}.$$

2. Collect the unknowns into a column vector:

$$x=\begin{pmatrix}x\\y\\z\end{pmatrix}.$$

3. Collect the constants on the right-hand sides:

$$b=\begin{pmatrix}4\\1\\7\end{pmatrix}.$$

4. The matrix equation is therefore

$$\begin{pmatrix}2&-1&1\\1&3&-2\\3&1&1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}4\\1\\7\end{pmatrix}.$$

5. Row correspondence: the first row $(2,-1,1)$ dotted with $(x,y,z)^T$ gives $2x-y+z$, which equals $4$, the first equation. The second row gives $x+3y-2z=1$, and the third gives $3x+y+z=7$.

## Why each step is valid

Each row of $A$ is built directly from the coefficients of the corresponding equation, so matrix-vector multiplication reproduces that equation. The vector $x$ lists the unknowns in the same order used for the columns of $A$, and $b$ lists the constants in the same order as the equations.

## Final answer (in words)

The system is $Ax=b$ with coefficient matrix $A$ the $3\times3$ matrix above, unknown vector $x=(x,y,z)^T$, and right-hand side $b=(4,1,7)^T$. Each row of $A$ is the coefficient triple of the matching equation.

## Verification

Multiplying $A$ by $x$ gives three expressions $2x-y+z$, $x+3y-2z$, $3x+y+z$, which are exactly the left-hand sides of the three original equations. Setting these equal to $4,1,7$ recovers the original system, so the translation is correct.

## Common mistakes

- Writing the unknown vector as a row instead of a column.
- Mixing the order of unknowns between $A$ and $x$.
- Forgetting the minus signs on negative coefficients.
- Putting the constants inside the matrix instead of in $b$.

## How I would explain it in class

The matrix $A$ holds the coefficients, $x$ holds the unknowns, and $b$ holds the constants. Multiplying row $i$ of $A$ by $x$ rebuilds equation $i$. So the whole system becomes one matrix equation $Ax=b$.
