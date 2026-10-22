# Problem 9

## The original problem

Find numbers $x,y$ satisfying
$$x+y=10,\qquad 2x+5y=32.$$
Solve the system and explain geometrically why the solution is unique.

## What we are looking for

We want the pair of numbers $(x,y)$ that makes both equations true at the same time. We also want to explain, with a picture of two lines, why there cannot be a second pair.

## The idea we need

Each equation of the form $px+qy=r$ describes a straight line in the plane: its points are exactly the pairs $(x,y)$ that satisfy it. A pair satisfying both equations lies on both lines, so it is an intersection point. Two different lines that are not parallel meet in exactly one point. To find that point we use elimination: we add a multiple of one equation to another so that one unknown disappears.

## Step-by-step solution

1. Write the system as an augmented matrix, where each row is one equation and the last column holds the right-hand sides:
$$\left[\begin{array}{cc|c}1&1&10\\2&5&32\end{array}\right].$$

2. Remove $x$ from the second equation. Replace row 2 by row 2 minus $2$ times row 1. The new second row is $(2-2\cdot1,\;5-2\cdot1,\;32-2\cdot10)=(0,3,12)$:
$$\left[\begin{array}{cc|c}1&1&10\\0&3&12\end{array}\right].$$

3. The second row now says $3y=12$, so $y=4$.

4. Put $y=4$ into the first row $x+y=10$. This gives $x+4=10$, so $x=6$.

5. Geometric reading. The first line $x+y=10$ can be written $y=10-x$ and has slope $-1$. The second line $2x+5y=32$ can be written $y=\frac{32-2x}{5}$ and has slope $-\frac25$. The slopes $-1$ and $-\frac25$ are different.

## Why each step is valid

- Step 2 subtracts equal quantities from both sides of the second equation (the left side $2x+5y$ minus $2(x+y)$, and the right side $32$ minus $2\cdot10$). Any pair that solved both original equations still solves the new pair, and the operation can be undone by adding $2$ times row 1 back, so no solutions are gained or lost.
- Step 3 divides by $3$, which is allowed because $3\neq0$.
- Step 4 uses the first equation, which was never changed, so back substitution is legitimate.
- Step 5: two lines in the plane with different slopes are not parallel, so they cross, and they cross only once. The same fact appears in the elimination: the number $3=5-2$ left in front of $y$ is not zero. If it had been zero, the lines would have the same slope and elimination would have produced either $0=0$ or a contradiction.

## Final answer (in words)

The only pair that satisfies both conditions is $x=6$ and $y=4$, that is $(x,y)=(6,4)$. It is unique because the two lines have different slopes, so they intersect in exactly one point, namely $(6,4)$.

## Verification

Substitute into the original equations, not the reduced ones. First equation: $6+4=10$. Second equation: $2\cdot6+5\cdot4=12+20=32$. Both hold.

An independent check uses the substitution method: from $x+y=10$ we get $x=10-y$; then $2(10-y)+5y=20+3y=32$, so $3y=12$ and $y=4$, $x=6$, the same answer. The determinant of the coefficient matrix is $1\cdot5-1\cdot2=3\neq0$, which agrees with the geometric claim that the solution is unique.

## Common mistakes

- Computing $32-2\cdot10$ as $32-10$, that is, forgetting to multiply the right-hand side by $2$ together with the left side.
- Subtracting $2$ times row 1 from the $x$ coefficient but forgetting the $y$ coefficient, getting $5$ instead of $5-2=3$.
- Checking the answer in only one equation. The pair $(10,0)$ fits the first equation but gives $20\neq32$ in the second.
- Claiming uniqueness because a solution was found. Uniqueness comes from the different slopes, not from finding one point.

## How I would explain it in class

Each equation is a straight line, and a solution is a point lying on both lines. Subtracting twice the first equation from the second leaves $3y=12$, so $y=4$ and then $x=6$. The slopes $-1$ and $-\frac25$ differ, so the lines cross exactly once and the point $(6,4)$ is the only solution.
