# Problem 7

## The original problem

Do not solve all of the following systems completely. For each situation, choose the method that best uses its structure and justify your choice:

1. one system with a triangular coefficient matrix
   $$\begin{cases}2x-y=3,\\4y=8;\end{cases}$$
2. three systems $Ax=b_i$ with the same invertible matrix $A$, when $A^{-1}$ is already known;
3. one $3\times3$ system for which the inverse matrix is not given and the goal is only to find one solution vector.

For case 1, carry out the chosen method completely. For cases 2 and 3, describe the plan and indicate which part of the computation would be reusable or unnecessary. Do not judge a method by its name alone — refer to the number of right-hand sides and the structure of the matrix.

## What we are looking for

We must match each situation to the most efficient method, justify the choice by structure and by number of right-hand sides, fully solve case 1, and outline reusable or unnecessary work for cases 2 and 3.

## The idea we need

A triangular system is solved by back substitution from the last equation upward, which is cheaper than general elimination. When $A^{-1}$ is known and several right-hand sides $b_i$ are given, each solution is $x_i=A^{-1}b_i$, reusing the inverse. When only one solution is needed and no inverse is given, Gaussian elimination is preferred because computing an inverse costs more than solving one system.

## Step-by-step solution

### Case 1 — triangular system: back substitution

1. From $4y=8$, we get $y=2$.

2. Substitute into $2x-y=3$: $2x-2=3$, so $2x=5$, giving $x=\frac52$.

### Case 2 — three systems, $A^{-1}$ known

Plan: compute $x_i=A^{-1}b_i$ for $i=1,2,3$. The inverse is computed (or given) once and reused for all three right-hand sides; no elimination is repeated.

### Case 3 — one $3\times3$ system, no inverse given, one solution needed

Plan: use Gaussian elimination on the augmented matrix $[A|b]$ and back substitute. Computing $A^{-1}$ would be unnecessary extra work because only one solution vector is required.

## Why each step is valid

Back substitution is valid for triangular systems because each equation introduces exactly one new variable. Reusing $A^{-1}$ is valid because $Ax=b$ implies $x=A^{-1}b$ when $A$ is invertible. Gaussian elimination is valid because row operations preserve the solution set.

## Final answer (in words)

Case 1 gives $(x,y)=(\frac52,2)$. Case 2 should reuse the known inverse for all three right-hand sides. Case 3 should use Gaussian elimination without computing an inverse.

## Verification

Check case 1: $4(2)=8$ and $2(\frac52)-2=5-2=3$. Both original equations hold.

## Common mistakes

- Solving a triangular system by full elimination instead of back substitution.
- Recomputing $A^{-1}$ for each right-hand side.
- Computing an inverse when only one solution is needed.
- Choosing a method by name rather than by structure.

## How I would explain it in class

For the triangular system I use back substitution: $y=2$, then $x=\frac52$. When the inverse is already known and there are multiple right-hand sides, I multiply each by $A^{-1}$. For a single system without an inverse, Gaussian elimination is enough and avoids extra work.
