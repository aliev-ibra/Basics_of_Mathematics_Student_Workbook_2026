# Problem 12

## The original problem

Solve
$$\begin{cases}x+2y-z=0,\\2x+4y-2z=0,\\x-y+2z=0.\end{cases}$$
Give all solutions in parametric form and explain why $(0,0,0)$ always satisfies a homogeneous system.

## What we are looking for

We want every triple $(x,y,z)$ that makes all three equations true, written with a free parameter, and a reason why the zero triple is always a solution of a system whose right-hand sides are all zero.

## The idea we need

Elimination changes a system into a simpler one with the same solutions. If an equation turns into $0=0$, it carried no new information and a variable stays free. We can then describe all solutions by letting that variable be any number $s$ (a parameter) and expressing the other variables through it.

## Step-by-step solution

1. Equation 2 is $2$ times equation 1: $2x+4y-2z=2(x+2y-z)$. Subtract $2$ times equation 1 from equation 2: the row becomes $0x+0y+0z=0$, that is $0=0$. It adds nothing.

2. What remains is
$$\begin{cases}x+2y-z=0,\\x-y+2z=0.\end{cases}$$

3. Subtract equation 2 from equation 1: $(x+2y-z)-(x-y+2z)=0$, which gives $3y-3z=0$, so $y=z$.

4. Put $y=z$ into $x-y+2z=0$: $x-z+2z=x+z=0$, so $x=-z$.

5. The variable $z$ is free. Write $z=s$ for any real number $s$. Then $x=-s$, $y=s$, $z=s$:
$$(x,y,z)=s\,(-1,\,1,\,1),\qquad s\in\mathbb R.$$

6. Why $(0,0,0)$ is always a solution: in every equation each term is a coefficient times an unknown. Putting all unknowns equal to $0$ makes each term $0$, so every left side is $0$, which equals the right side $0$. This is the case $s=0$ above.

## Why each step is valid

- Step 1 is an elementary row operation, which does not change the solution set. The result $0=0$ is always true, so deleting that equation loses nothing.
- Step 3 subtracts two equations whose right sides are both $0$, so the right side stays $0$. Dividing by $3$ is fine because $3\neq0$.
- Step 4 is substitution of an equal quantity.
- There are $3$ unknowns and only $2$ independent equations, so exactly one free parameter is expected; one free variable describes a line through the origin in space.

## Final answer (in words)

The solutions are all triples that are multiples of $(-1,1,1)$: $(x,y,z)=(-s,s,s)$ for any real number $s$. So there are infinitely many solutions, and they form a line through the origin. The zero triple $(0,0,0)$ is the solution with $s=0$ and is always a solution of a homogeneous system because every term of every equation becomes $0$.

## Verification

Substitute $(-s,s,s)$ into the original equations. Equation 1: $-s+2s-s=0$. Equation 2: $-2s+4s-2s=0$. Equation 3: $-s-s+2s=0$. All hold for every $s$.

Specific check with $s=1$: $(-1,1,1)$ gives $-1+2-1=0$, $-2+4-2=0$, $-1-1+2=0$. An independent check: the determinant of the coefficient matrix is $0$ (row 2 is twice row 1), consistent with a nonzero solution existing, and the rank is $2$, so $3-2=1$ parameter, as found.

## Common mistakes

- Keeping all three equations and concluding that only $(0,0,0)$ works. Equation 2 is a repeat of equation 1, so it does not count as an extra condition.
- Reading $0=0$ as a contradiction. It is a true statement and signals a free variable.
- Writing the solution as a single vector $(-1,1,1)$ instead of all its multiples $s(-1,1,1)$.
- Sign error in step 4 and getting $x=z$ instead of $x=-z$.

## How I would explain it in class

The second equation is just twice the first, so elimination turns it into $0=0$ and only two real conditions remain for three unknowns. Subtracting the remaining equations gives $y=z$ and then $x=-z$, so $z$ is free and the solutions are $s(-1,1,1)$. The zero triple always works in a homogeneous system because every term is a coefficient times $0$, and here it is the case $s=0$.
