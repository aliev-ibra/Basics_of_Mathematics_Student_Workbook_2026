# Problem 14

## The original problem

Compare the systems
$$\begin{cases}x+y=2,\\2x-y=1,\\3x=3\end{cases}$$
and
$$\begin{cases}x+y=2,\\2x-y=1,\\3x=3.1.\end{cases}$$
Check the consistency of each system and explain why a small change in one number can change the type of the system.

## What we are looking for

For each system we must decide whether it is consistent (has at least one solution) or inconsistent (has none), and explain why changing $3$ to $3.1$ matters so much.

## The idea we need

There are three equations but only two unknowns, so the equations must agree with each other. We solve the first two equations, which determine $x$ and $y$, and then test whether the third equation is also satisfied. Adding the first two equations produces $3x$ on the left, which links the third equation to the others.

## Step-by-step solution

1. Add equations 1 and 2: $(x+y)+(2x-y)=2+1$, giving $3x=3$, so $x=1$.

2. From $x+y=2$ we get $y=1$. So the first two equations have the unique solution $(1,1)$.

3. System A: the third equation is $3x=3$. At $x=1$ it reads $3=3$, true. So $(1,1)$ satisfies all three equations. Also the third equation is exactly the sum of the first two, so in elimination it becomes $0=0$.

4. System B: the third equation is $3x=3.1$. The first two equations force $x=1$, which gives $3x=3$. Subtracting the sum of the first two equations from the third gives $0=3.1-3$, that is $0=0.1$, a contradiction.

5. So System A is consistent with exactly one solution $(1,1)$, and System B is inconsistent with no solution.

## Why each step is valid

- Step 1 adds equal quantities to both sides and keeps the solution set.
- In System B, any solution would have to satisfy the first two equations, which allow only $x=1$, and the third equation would then require $x=\frac{3.1}{3}=\frac{31}{30}\neq1$. One number cannot be both, so no solution exists.
- A small change in a number matters because each extra equation is a new line, and three lines have a common point only if the third passes exactly through the intersection of the other two. Line $3x=3$ is the vertical line $x=1$ which passes through $(1,1)$; line $3x=3.1$ is the vertical line $x=\frac{31}{30}$, which misses that point by $\frac{1}{30}$. Consistency is an exact condition: it holds or it does not, with no partial credit for being close.

## Final answer (in words)

The first system is consistent and has the single solution $x=1$, $y=1$. The second system is inconsistent and has no solution, because its first two equations force $x=1$ while its third demands $x=\frac{31}{30}$. The type changes from one solution to none because consistency of an overdetermined system requires an exact match.

## Verification

System A at $(1,1)$: $1+1=2$, $2-1=1$, $3\cdot1=3$. All three hold. System B at $(1,1)$: the first two hold, but $3\cdot1=3\neq3.1$. To make sure no other point works, note that the first two equations have only $(1,1)$ as a solution, since their determinant is $1\cdot(-1)-1\cdot2=-3\neq0$. Hence no point satisfies all three equations of System B.

## Common mistakes

- Saying that $3.1$ is close to $3$, so the system is basically consistent. Exact equations are either satisfied or not.
- Checking the third equation at a rounded value or an unrelated point instead of at the solution of the first two.
- Concluding from three equations and two unknowns that the system must have no solution. System A shows it can have one.
- Declaring System B to have infinitely many solutions because $0=0.1$ looks small. A false statement such as $0=0.1$ means no solution.

## How I would explain it in class

The first two equations meet at a single point, $(1,1)$, and adding them gives $3x=3$, which is exactly the third equation of the first system. In the second system the third equation is $3x=3.1$, and subtracting gives the false statement $0=0.1$, so no point satisfies all three. A tiny change breaks consistency because three lines share a point only when the third passes exactly through the crossing of the first two.
