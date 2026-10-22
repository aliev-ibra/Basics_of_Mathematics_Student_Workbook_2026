# Problem 13

## The original problem

Consider the system
$$x_1+x_2=10,\qquad x_2+x_3=8,\qquad x_1-x_3=2.$$
Solve it and check whether all three equations are independently necessary to describe the solution set. If one follows from the others, show this by calculation.

## What we are looking for

We want all triples $(x_1,x_2,x_3)$ satisfying the three equations, and an answer to whether some equation can be removed without changing the solution set.

## The idea we need

An equation is redundant when it can be obtained by adding or subtracting multiples of the other equations. During elimination such an equation turns into $0=0$. A redundant equation does not restrict the solutions further, and so the system has fewer independent conditions than equations.

## Step-by-step solution

1. Subtract equation 2 from equation 1: $(x_1+x_2)-(x_2+x_3)=10-8$, which simplifies to $x_1-x_3=2$.

2. This is exactly equation 3. So equation 3 equals equation 1 minus equation 2. After eliminating, equation 3 minus this result is $0=0$.

3. The independent equations are therefore
$$x_1+x_2=10,\qquad x_2+x_3=8.$$

4. Now $x_3$ is free: put $x_3=s$. From the second equation $x_2=8-s$. From the first $x_1=10-x_2=10-(8-s)=2+s$.

5. Solution set:
$$(x_1,x_2,x_3)=(2+s,\;8-s,\;s),\qquad s\in\mathbb R,$$
which can also be written $(2,8,0)+s(1,-1,1)$.

6. Redundancy: equation 1 is equation 2 plus equation 3, equation 3 is equation 1 minus equation 2, and equation 2 is equation 1 minus equation 3 ($10-2=8$ on the right). So any one of the three can be dropped.

## Why each step is valid

- Step 1 subtracts equal quantities from both sides and uses only the given equations.
- Step 2 shows by calculation that equation 3 is a combination of equations 1 and 2, so any triple satisfying equations 1 and 2 automatically satisfies equation 3. Dropping it keeps the solution set the same.
- Step 4 solves two equations in three unknowns by choosing one unknown freely, which is correct because there are only two independent conditions.
- The statement in step 6 is symmetric: the relation $\text{(eq 1)}-\text{(eq 2)}-\text{(eq 3)}=0$ links all three, so none is more essential than another. Each pair of equations is independent, as no two of them are multiples of each other.

## Final answer (in words)

The system has infinitely many solutions: $x_1=2+s$, $x_2=8-s$, $x_3=s$ for any real number $s$. The three equations are not all independently necessary: the third equals the first minus the second, so only two independent equations remain and the solution set is a line.

## Verification

Substitute $(2+s,8-s,s)$: equation 1 gives $2+s+8-s=10$. Equation 2 gives $8-s+s=8$. Equation 3 gives $2+s-s=2$. All hold for every $s$.

Specific points: $s=0$ gives $(2,8,0)$ with $10$, $8$, $2$; $s=3$ gives $(5,5,3)$ with $10$, $8$, $2$. The determinant of the coefficient matrix $\begin{pmatrix}1&1&0\\0&1&1\\1&0&-1\end{pmatrix}$ is $0$, consistent with a dependent system. Finally, the right-hand sides satisfy the same relation as the left sides, $10-8=2$; had the third equation said $x_1-x_3=3$, the system would be inconsistent.

## Common mistakes

- Thinking that three equations in three unknowns always give one solution.
- Showing only that the three equations look different, without finding the combination that links them.
- Checking the relation on the left sides but not on the right sides: the redundancy needs $10-8=2$ too.
- Writing the answer as a single point instead of a family with a parameter.

## How I would explain it in class

Subtracting the second equation from the first gives $x_1-x_3=2$, which is precisely the third equation, so the third adds no new information. That leaves two independent equations for three unknowns, so one unknown is free and the solutions are $(2+s,8-s,s)$. Any one of the three equations can be removed without changing the solution set.
