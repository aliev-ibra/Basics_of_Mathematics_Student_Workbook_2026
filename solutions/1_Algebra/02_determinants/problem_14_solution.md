# Problem 14

## The original problem

Consider the system $Ax=b$, where
$$
A=\begin{pmatrix}1&2\\k&4\end{pmatrix}.
$$
For which values of $k$ does the system have exactly one solution for every $b$? For the remaining value, give an example of a right-hand side $b$ for which the system has infinitely many solutions, and an example for which it has no solution.

## What we are looking for

Here $x=\begin{pmatrix}x_1\\x_2\end{pmatrix}$ is the unknown vector, $b=\begin{pmatrix}b_1\\b_2\end{pmatrix}$ is any given right-hand side, and $k$ is a parameter (a number we are free to choose). We want the values of $k$ for which the system has one and only one solution no matter which $b$ is chosen. For the one remaining value of $k$ we must exhibit two concrete vectors $b$: one giving infinitely many solutions and one giving none.

## The idea we need

**Determinant and solvability.** For a square matrix $A$, the system $Ax=b$ has exactly one solution for every $b$ if and only if $\det A\neq0$, because then $A$ is invertible and $x=A^{-1}b$. If $\det A=0$, then $A$ is not invertible, and the system has, depending on $b$, either no solution or infinitely many solutions.

## Step-by-step solution

**Step 1: compute the determinant.**
$$
\det A=1\cdot4-2\cdot k=4-2k.
$$

**Step 2: find where it is zero.** The equation $4-2k=0$ gives $k=2$.

**Step 3: conclude for $k\neq2$.** For every $k\neq2$ the determinant is nonzero, so the system has exactly one solution for every $b$.

**Step 4: study $k=2$.** Then the system is
$$
\begin{aligned}
x_1+2x_2&=b_1,\\
2x_1+4x_2&=b_2.
\end{aligned}
$$
The left side of the second equation is exactly twice the left side of the first. So a solution can exist only when $b_2=2b_1$.

**Step 5: an example with infinitely many solutions.** Take $b=\begin{pmatrix}1\\2\end{pmatrix}$, so $b_2=2b_1$. Both equations say the same thing, $x_1+2x_2=1$. Choose $x_2=s$ freely; then $x_1=1-2s$. So every vector $\begin{pmatrix}1-2s\\s\end{pmatrix}$ with $s$ any real number is a solution, giving infinitely many solutions.

**Step 6: an example with no solution.** Take $b=\begin{pmatrix}1\\3\end{pmatrix}$, so $b_2\neq2b_1$. The first equation says $x_1+2x_2=1$, so the left side of the second equation is $2(x_1+2x_2)=2$, but the second equation demands $3$. This is a contradiction, so there is no solution.

## Why each step is valid

- A nonzero determinant gives an inverse $A^{-1}$, and then $x=A^{-1}b$ is a solution, and it is the only one because any solution must equal $A^{-1}b$.
- For $k=2$ the rows of $A$ are proportional, so the equations are not independent. This is why the right-hand sides must satisfy the same proportion for a solution to exist.
- In Step 5 the two equations coincide, so only one condition remains for two unknowns, which leaves one free variable.
- In Step 6 the two equations contradict each other, so no pair $(x_1,x_2)$ can satisfy both.

## Final answer (in words)

The system has exactly one solution for every $b$ for all values $k\neq2$, because $\det A=4-2k$ is nonzero exactly then. For the remaining value $k=2$, the right-hand side $b=\begin{pmatrix}1\\2\end{pmatrix}$ gives infinitely many solutions, namely $\begin{pmatrix}1-2s\\s\end{pmatrix}$ for any real $s$, and the right-hand side $b=\begin{pmatrix}1\\3\end{pmatrix}$ gives no solution.

$$
\det A=4-2k,\qquad k\neq2\ \Rightarrow\ \text{unique solution for every }b.
$$

## Verification

I check the two examples by substitution, independently of the determinant. For $b=(1,2)$ and the solution $(1-2s,\,s)$: the first equation gives $(1-2s)+2s=1$ and the second gives $2(1-2s)+4s=2-4s+4s=2$, so both hold for every $s$. For $b=(1,3)$, adding $-2$ times the first equation to the second gives $0=3-2=1$, which is false, so no solution exists. For the case $k\neq2$, take for instance $k=0$: then $\det A=4$, and solving $x_1+2x_2=b_1$, $4x_2=b_2$ gives $x_2=b_2/4$ and $x_1=b_1-b_2/2$, a unique solution for any $b$.

## Common mistakes

- Saying that for $k=2$ there is always no solution or always infinitely many; it depends on $b$.
- Choosing $b=(1,2)$ for the "no solution" case, or $b=(1,3)$ for the "infinitely many" case, which is the wrong way around. A solution exists only when $b_2=2b_1$.
- Concluding that $k=2$ is the answer to the first question. It is the exceptional value, and the first question asks for all other values.
- Thinking that a zero determinant always means no solution.

## How I would explain it in class

The determinant is $4-2k$, so unless $k=2$ the matrix is invertible and the system has exactly one solution for every right-hand side. When $k=2$ the second equation has the left side of the first one doubled, so the system is solvable only if $b_2=2b_1$, for example $b=(1,2)$ gives infinitely many solutions. A choice such as $b=(1,3)$ breaks the proportion and the system has no solution.
