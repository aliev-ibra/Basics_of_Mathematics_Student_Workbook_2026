# Problem 10

## The original problem

Find a polynomial $p(x)=ax^2+bx+c$ whose graph passes through $(0,1)$, $(1,3)$, and $(2,9)$. Reduce the problem to a system of equations and check the result by substituting all three points.

## What we are looking for

We need three numbers $a$, $b$, $c$ (the coefficients of the quadratic polynomial) such that the graph of $y=ax^2+bx+c$ contains the three given points.

## The idea we need

A point $(x_0,y_0)$ lies on the graph exactly when $p(x_0)=y_0$. Here the unknowns are the coefficients $a,b,c$, while $x_0$ and $y_0$ are known numbers. Therefore each point gives one equation that is linear in $a,b,c$, and three points give a linear system of three equations in three unknowns, which we solve by elimination.

## Step-by-step solution

1. Point $(0,1)$ means $p(0)=1$: $a\cdot0+b\cdot0+c=1$, so $c=1$.

2. Point $(1,3)$ means $p(1)=3$: $a+b+c=3$.

3. Point $(2,9)$ means $p(2)=9$: $4a+2b+c=9$.

4. The system is
$$\begin{cases}c=1,\\a+b+c=3,\\4a+2b+c=9.\end{cases}$$

5. Substitute $c=1$ into the other two equations: $a+b=2$ and $4a+2b=8$.

6. Eliminate $b$: subtract $2$ times the equation $a+b=2$ from $4a+2b=8$. The left side gives $4a+2b-2a-2b=2a$ and the right side gives $8-4=4$, so $2a=4$ and $a=2$.

7. Then $b=2-a=0$.

8. So $p(x)=2x^2+0\cdot x+1=2x^2+1$.

## Why each step is valid

- Steps 1 to 3 are valid because the graph of $p$ is the set of points $(x,p(x))$; passing through a point means exactly the equation $p(x_0)=y_0$. The value $x_0^2$ is a known number, so the equation really is linear in $a,b,c$.
- Step 5 substitutes an equality ($c$ equals $1$) into other equations, which does not change the solutions.
- Step 6 subtracts equal quantities from both sides, so the solution set is preserved.
- The solution is unique: elimination never needed a division by zero (we divided by $2$), and the three $x$-values $0,1,2$ are distinct, which is what makes the system solvable with exactly one answer.

## Final answer (in words)

The polynomial is $p(x)=2x^2+1$, that is $a=2$, $b=0$, $c=1$. It is the only quadratic of the form $ax^2+bx+c$ passing through the three points.

## Verification

Substitute all three points into $p(x)=2x^2+1$:

- $p(0)=2\cdot0+1=1$, matching $(0,1)$.
- $p(1)=2\cdot1+1=3$, matching $(1,3)$.
- $p(2)=2\cdot4+1=9$, matching $(2,9)$.

As an independent check, compute the second difference of the values at equally spaced points: the values $1,3,9$ have first differences $2,6$ and second difference $6-2=4$, which equals $2a$ for a quadratic with step $1$. This gives $a=2$, as found.

## Common mistakes

- Writing the equation for $(2,9)$ as $2a+2b+c=9$, forgetting that $x^2=4$ multiplies $a$.
- Mixing up which coordinate is substituted: the first coordinate is $x$, the second is the value of $p$.
- Solving only the first two equations and not testing the third point.
- Treating $b=0$ as missing. The answer $2x^2+1$ is correct; the linear term is simply absent.

## How I would explain it in class

A point lies on the graph exactly when its coordinates satisfy $p(x_0)=y_0$, so each point gives one linear equation in the unknown coefficients $a,b,c$. The first point gives $c=1$ at once, and elimination on the remaining two equations gives $a=2$ and $b=0$. The polynomial $2x^2+1$ then reproduces all three given points, which I confirm by substitution.
