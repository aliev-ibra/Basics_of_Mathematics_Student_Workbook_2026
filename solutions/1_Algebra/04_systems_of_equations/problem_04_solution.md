# Problem 4

## The original problem

Solve
$$\begin{cases}x+y+z=2,\\2x+2y+2z=4,\\x-y+z=0.\end{cases}$$
Give the solution in parametric form, identify a free variable, and for one chosen parameter value check that the resulting point really satisfies the system.

## What we are looking for

We need all triples $(x,y,z)$ satisfying the three equations. Because one equation is a multiple of another, we expect infinitely many solutions forming a line; we will describe them with one free parameter.

## The idea we need

A system has infinitely many solutions when elimination produces a row of zeros $0=0$, leaving fewer independent equations than unknowns. The variables not tied to pivots are free and can be set to a parameter. Each free variable adds one degree of freedom to the solution set.

## Step-by-step solution

1. Write the augmented matrix:

$$\left[\begin{array}{ccc|c}1&1&1&2\\2&2&2&4\\1&-1&1&0\end{array}\right].$$

2. Notice $R_2=2R_1$, so $R_2\leftarrow R_2-2R_1$ gives a zero row:

$$\left[\begin{array}{ccc|c}1&1&1&2\\0&0&0&0\\1&-1&1&0\end{array}\right].$$

3. Eliminate below the first pivot: $R_3\leftarrow R_3-R_1$:

$$\left[\begin{array}{ccc|c}1&1&1&2\\0&0&0&0\\0&-2&0&-2\end{array}\right].$$

4. Swap $R_2$ and $R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&2\\0&-2&0&-2\\0&0&0&0\end{array}\right].$$

5. Simplify $R_2$: divide by $-2$: $y=1$.

6. From $R_1$: $x+1+z=2$, so $x+z=1$, hence $x=1-z$.

7. Let the free variable $z=t$. Then $x=1-t$, $y=1$, $z=t$.

## Why each step is valid

The zero row $0=0$ confirms the second equation adds no new information. The remaining two independent equations determine $y$ and the relation $x+z=1$, leaving $z$ free. Setting $z=t$ parameterizes the whole solution line.

## Final answer (in words)

The system has infinitely many solutions forming a line: $(x,y,z)=(1-t,\,1,\,t)$ for any real $t$, with $z$ (equivalently $t$) as the free variable.

## Verification

Take $t=0$, giving $(0,1,1)$. Check: $0+1+1=2$, $2(0)+2(1)+2(1)=4$, and $0-1+1=0$. All three hold, so the parametric form is correct.

## Common mistakes

- Treating the redundant equation as independent and forcing a unique solution.
- Choosing a non-free variable as the parameter.
- Forgetting to express all variables in terms of the parameter.
- Not verifying with a concrete parameter value.

## How I would explain it in class

The second equation is just twice the first, so it gives no new information. After elimination we have two equations for three unknowns, leaving $z$ free. Setting $z=t$ gives the line $(1-t,1,t)$, and checking $t=0$ confirms it.
