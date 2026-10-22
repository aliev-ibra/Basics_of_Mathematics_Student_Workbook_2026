# Problem 3

## The original problem

Solve or show that the system is inconsistent:
$$\begin{cases}x+2y=3,\\2x+4y=7.\end{cases}$$
Show how the contradiction appears in the matrix after elimination and interpret it in terms of equations.

## What we are looking for

We must decide whether there exists a pair $(x,y)$ satisfying both equations. If none exists, we must show the contradiction explicitly and explain what it means geometrically.

## The idea we need

For a linear system, elementary row operations preserve the solution set. A row of the form $0\;0\;\dots\;0\;|\;c$ with $c\neq 0$ represents the equation $0=c$, which is impossible. Such a row proves the system has no solution. Geometrically, two lines with the same slope but different intercepts are parallel and never meet.

## Step-by-step solution

1. Write the augmented matrix:

$$\left[\begin{array}{cc|c}1&2&3\\2&4&7\end{array}\right].$$

2. Eliminate below the first pivot: $R_2\leftarrow R_2-2R_1$:

$$\left[\begin{array}{cc|c}1&2&3\\0&0&1\end{array}\right].$$

3. The second row reads $0\cdot x+0\cdot y=1$, i.e. $0=1$, a contradiction.

4. Therefore no pair $(x,y)$ can satisfy both equations.

## Why each step is valid

The row operation $R_2-2R_1$ is elementary and preserves the solution set, so the contradiction in the new system is a contradiction in the original system. The equation $0=1$ is false for every $(x,y)$, hence the system is inconsistent.

## Final answer (in words)

The system has no solution. The two equations describe parallel lines that never intersect.

## Verification

The first equation gives $x+2y=3$. Multiplying by $2$ gives $2x+4y=6$, but the second equation demands $2x+4y=7$. These two requirements on the same expression cannot both hold, confirming inconsistency.

## Common mistakes

- Concluding "no solution" without showing the zero row.
- Trying to solve for $y$ from $0=1$.
- Confusing inconsistent with dependent (infinitely many solutions).
- Ignoring that the left-hand sides are proportional.

## How I would explain it in class

After elimination the second row becomes $0=1$, which is impossible. That means the two equations ask for different values of the same expression $2x+4y$. Geometrically the lines are parallel, so they never meet.
