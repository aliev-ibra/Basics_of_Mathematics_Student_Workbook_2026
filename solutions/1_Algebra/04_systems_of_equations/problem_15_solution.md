# Problem 15

## The original problem

For each of the following systems, perform only as much elimination as necessary to recognize its type:

1. $\begin{cases}x+y=2,\\x-y=0,\end{cases}$
2. $\begin{cases}x+y=2,\\2x+2y=4,\end{cases}$
3. $\begin{cases}x+y=2,\\2x+2y=5.\end{cases}$

For each, justify the classification: one solution, infinitely many solutions, or no solution.

## What we are looking for

For each of the three systems we must decide which of the three possible types it is, with a reason read off from the elimination, and also give the solution where one exists.

## The idea we need

After eliminating $x$ from the second equation, the second equation has the form $(\text{number})\cdot y=(\text{number})$. If the coefficient of $y$ is not zero, we can solve for $y$ and the solution is unique. If both numbers are zero, the equation is $0=0$ and $y$ remains free, giving infinitely many solutions. If the coefficient is zero and the right side is not, we get a false statement such as $0=1$, and there is no solution.

## Step-by-step solution

**System 1.** Subtract equation 1 from equation 2: $(x-y)-(x+y)=0-2$, giving $-2y=-2$. The coefficient $-2$ is not zero, so $y=1$, and $x+1=2$ gives $x=1$. Type: exactly one solution, $(1,1)$.

**System 2.** Subtract $2$ times equation 1 from equation 2: $(2x+2y)-2(x+y)=4-2\cdot2$, giving $0=0$. The second equation is a repeat of the first. Only $x+y=2$ remains, so $y=s$ is free and $x=2-s$. Type: infinitely many solutions, $(2-s,s)$.

**System 3.** Subtract $2$ times equation 1 from equation 2: $(2x+2y)-2(x+y)=5-4$, giving $0=1$. This is false for every $x,y$. Type: no solution.

## Why each step is valid

- Each subtraction is an elementary operation: it subtracts equal quantities from both sides and can be reversed, so it does not change the solution set.
- In System 1 dividing by $-2$ is valid because it is not zero.
- In System 2 the statement $0=0$ is always true, so the second equation puts no restriction on $x$ and $y$; only the first equation counts.
- In System 3 the statement $0=1$ is never true, so no pair $(x,y)$ can satisfy the second equation together with the first. A system with a contradictory equation has no solution.
- Geometrically: System 1 has lines with different slopes ($-1$ and $1$) which cross once; System 2 has the same line twice; System 3 has two parallel lines, $x+y=2$ and $x+y=\frac52$, which never meet.

## Final answer (in words)

System 1 has exactly one solution, $x=1$ and $y=1$. System 2 has infinitely many solutions, namely $(x,y)=(2-s,s)$ for any real $s$. System 3 has no solution because elimination gives the false statement $0=1$. All three types occur.

## Verification

System 1: $1+1=2$ and $1-1=0$. System 2: for $s=0$ the point $(2,0)$ gives $2+0=2$ and $4+0=4$; for $s=3$ the point $(-1,3)$ gives $-1+3=2$ and $-2+6=4$; in general $(2-s)+s=2$ and $2(2-s)+2s=4$. System 3: if some pair satisfied $x+y=2$, then $2x+2y=2(x+y)=4$, which cannot be $5$, so no pair satisfies both. The determinants of the coefficient matrices are $-2$, $0$, $0$, which agrees: nonzero for System 1 and zero for Systems 2 and 3, which then differ in their right-hand sides.

## Common mistakes

- Deciding the type from the coefficients alone. Systems 2 and 3 have identical left sides and differ only in the right side, yet one has infinitely many solutions and the other none.
- Treating $0=1$ as acceptable, or $0=0$ as a contradiction.
- Forgetting to multiply the right side by $2$ when subtracting twice the first equation.
- Stopping at one solution found by guessing, such as $(1,1)$ in System 2, and claiming it is the only one.

## How I would explain it in class

I subtract a suitable multiple of the first equation from the second and look at what is left. A nonzero coefficient of $y$ gives one solution, the statement $0=0$ gives infinitely many solutions, and the statement $0=1$ gives none. So $x+y=2$ with $x-y=0$ has the single solution $(1,1)$, with $2x+2y=4$ it has the whole line $(2-s,s)$, and with $2x+2y=5$ it has no solution.
