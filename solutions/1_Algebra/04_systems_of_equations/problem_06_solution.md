# Problem 6

## The original problem

Analyze, depending on the parameter $a$, the system
$$\begin{cases}x+y=2,\\ax+ay=4.\end{cases}$$
Among the three possibilities — exactly one solution, infinitely many solutions, no solution — determine which actually occur and for which values of $a$. If one type cannot occur, explain why.

## What we are looking for

We must classify the solution set for every real value of $a$: unique, infinite, or none. We also must explain why one of the three types never occurs for this particular system.

## The idea we need

The coefficient matrix is $\begin{pmatrix}1&1\\a&a\end{pmatrix}$, whose determinant is $1\cdot a-1\cdot a=0$ for every $a$. A zero determinant means the rows are always linearly dependent, so a unique solution is impossible. The second equation factors as $a(x+y)=4$; combined with $x+y=2$ this forces $2a=4$.

## Step-by-step solution

1. From the first equation, $x+y=2$.

2. Substitute into the second: $a(x+y)=4$ becomes $2a=4$.

3. Case $a=2$: the condition holds. The second equation is $2(x+y)=4$, identical to the first, so the system reduces to $x+y=2$. There are infinitely many solutions (a line).

4. Case $a\neq 2$ (including $a=0$): the condition $2a=4$ fails. The equations demand $x+y=2$ and $x+y=4/a$ (or $0=4$ when $a=0$), which contradict. No solution.

5. Exactly one solution never occurs because the determinant of the coefficient matrix is $0$ for all $a$.

## Why each step is valid

Substituting the known sum $x+y=2$ into the second equation is valid because any solution must satisfy the first equation. The determinant computation shows the coefficient rows are always proportional, so the two equations can never determine a single point. The case split covers all real $a$.

## Final answer (in words)

For $a=2$ there are infinitely many solutions (the line $x+y=2$). For every $a\neq 2$ there is no solution. Exactly one solution never occurs, because the coefficient matrix is singular for all $a$.

## Verification

- $a=2$: system becomes $x+y=2$ twice, consistent with infinitely many points such as $(0,2)$.
- $a=1$: second equation says $x+y=4$, contradicting $x+y=2$.
- $a=0$: second equation says $0=4$, impossible.
All cases agree with the classification.

## Common mistakes

- Assuming all three cases must occur for some $a$.
- Forgetting $a=0$ as a separate-looking but covered case.
- Claiming a unique solution exists when the determinant is zero.
- Not factoring $a$ out of the second equation.

## How I would explain it in class

The determinant of the coefficient matrix is always zero, so a unique solution is impossible. The second equation becomes $a(x+y)=4$, and since $x+y=2$, we need $2a=4$. Thus only $a=2$ gives infinitely many solutions and all other $a$ give none.
