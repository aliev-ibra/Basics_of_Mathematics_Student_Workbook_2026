# Problem 5

## The original problem

For the augmented matrix
$$\left[\begin{array}{ccc|c}1&2&-1&3\\0&1&2&1\\0&0&0&0\end{array}\right]$$
determine the number of solutions and write them in parametric form. Explain how you know how many variables may be chosen freely.

## What we are looking for

We must read the solution count and the parametric description directly from the given row echelon form, without performing further elimination.

## The idea we need

In row echelon form, the number of pivots (leading ones) equals the rank of the coefficient matrix. With $n$ unknowns, the number of free variables is $n-\mathrm{rank}$. A zero row $0=0$ means consistency; a zero row $0=c$ with $c\neq0$ would mean inconsistency. Each free variable becomes an independent parameter.

## Step-by-step solution

1. The matrix has pivots in columns 1 and 2, so rank is $2$. There are $3$ unknowns, hence $3-2=1$ free variable.

2. The zero last row is $0=0$, so the system is consistent and has infinitely many solutions (a line).

3. The pivot in row 2 is in column 2 ($y$), so the free variable is $z$. Let $z=t$.

4. From row 2: $y+2z=1$, so $y=1-2t$.

5. From row 1: $x+2y-z=3$. Substitute $y$ and $z$:

$$x+2(1-2t)-t=3 \Rightarrow x+2-4t-t=3 \Rightarrow x=1+5t.$$

6. Parametric solution: $x=1+5t$, $y=1-2t$, $z=t$.

## Why each step is valid

The pivot positions identify which variables are basic (determined) and which are free. Back substitution from the bottom nonzero row upward is valid because each row expresses a basic variable using only variables to its right or constants. The free variable $z$ can take any real value, and each choice determines a unique point.

## Final answer (in words)

The system is consistent with infinitely many solutions forming a line in $\mathbb{R}^3$: $(x,y,z)=(1+5t,\,1-2t,\,t)$ for any real $t$, with exactly one free variable $z$.

## Verification

Take $t=0$: point $(1,1,0)$. Row 1: $1+2(1)-0=3$. Row 2: $1+2(0)=1$. Row 3: $0=0$. All hold, confirming the parametric form.

## Common mistakes

- Declaring a unique solution despite the zero row.
- Choosing a pivot variable as the free parameter.
- Forgetting to substitute back through all rows.
- Miscounting pivots and free variables.

## How I would explain it in class

There are two pivots and three unknowns, so one variable is free. The zero row means consistency, hence infinitely many solutions along a line. I set $z=t$, read $y$ from the second row, then $x$ from the first, and check $t=0$.
