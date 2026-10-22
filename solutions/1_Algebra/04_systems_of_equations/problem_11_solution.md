# Problem 11

## The original problem

Analyze the number of solutions depending on $t$:
$$\begin{cases}x+y+z=1,\\x+ty+z=2,\\x+y+tz=3.\end{cases}$$
Use elimination and separately analyze the parameter values for which a standard calculation step ceases to be valid.

## What we are looking for

For every real number $t$ we must say whether the system has exactly one solution, infinitely many solutions, or none, and give the solution whenever it exists. The letter $t$ is a fixed but unknown number, so the answer depends on its value.

## The idea we need

We use elimination: subtract the first equation from the others so that $x$ disappears. This will leave equations containing $t$ as a coefficient. To solve for $y$ we would divide by that coefficient, which is allowed only when it is not zero. So we split into the generic case and the value of $t$ where the coefficient vanishes, and treat that value separately by looking at the equation that results.

## Step-by-step solution

1. Subtract equation 1 from equation 2: $(x+ty+z)-(x+y+z)=2-1$, which simplifies to $(t-1)y=1$.

2. Subtract equation 1 from equation 3: $(x+y+tz)-(x+y+z)=3-1$, which simplifies to $(t-1)z=2$.

3. The system is now equivalent to
$$\begin{cases}x+y+z=1,\\(t-1)y=1,\\(t-1)z=2.\end{cases}$$

4. Case $t\neq1$. The number $t-1$ is not zero, so we may divide: $y=\dfrac{1}{t-1}$ and $z=\dfrac{2}{t-1}$. Then
$$x=1-y-z=1-\frac{3}{t-1}=\frac{t-4}{t-1}.$$

5. Case $t=1$. Then $t-1=0$ and the second reduced equation reads $0\cdot y=1$, that is $0=1$. This is impossible for every $y$, so there is no solution. (The third gives $0=2$, also impossible.)

## Why each step is valid

- Steps 1 and 2 subtract one equation from another, which keeps the solution set the same because the first equation is kept and the operation can be undone.
- Division in step 4 is valid only when $t-1\neq0$. This is exactly the standard step that ceases to be valid at $t=1$, and that is why $t=1$ is handled separately.
- At $t=1$ the original system has equations $x+y+z=1$, $x+y+z=2$, $x+y+z=3$: the same left side set equal to three different numbers, so no triple can work. This agrees with the contradiction $0=1$.
- Infinitely many solutions cannot occur: for $t\neq1$ every unknown is determined, and for $t=1$ nothing works.

## Final answer (in words)

For every $t$ different from $1$ the system has exactly one solution,
$$(x,y,z)=\left(\frac{t-4}{t-1},\;\frac{1}{t-1},\;\frac{2}{t-1}\right).$$
For $t=1$ the system has no solution. There is no value of $t$ giving infinitely many solutions.

## Verification

Check the general formula in all three original equations. Equation 1: $\frac{t-4+1+2}{t-1}=\frac{t-1}{t-1}=1$. Equation 2: $x+ty+z=\frac{t-4+t+2}{t-1}=\frac{2t-2}{t-1}=2$. Equation 3: $x+y+tz=\frac{t-4+1+2t}{t-1}=\frac{3t-3}{t-1}=3$. All hold for every $t\neq1$.

Numerical spot checks: $t=2$ gives $(-2,1,2)$ and $-2+1+2=1$, $-2+2+2=2$, $-2+1+4=3$. For $t=0$ the formula gives $(4,-1,-2)$ and $4-1-2=1$, $4+0-2=2$, $4-1+0=3$. As an independent confirmation, the determinant of the coefficient matrix is $(t-1)^2$, which is zero only at $t=1$, matching the case split.

## Common mistakes

- Dividing by $t-1$ without noting that it may be zero, and so missing the case $t=1$.
- Concluding that $t=1$ gives infinitely many solutions because the determinant is zero. A zero determinant only rules out a unique solution; here the right-hand sides $1,2,3$ are different, so there are none.
- Algebra slips in $x=1-y-z$, for example forgetting that the two fractions add to $\frac{3}{t-1}$.
- Not checking the final formulas in the equations that were not used to derive them.

## How I would explain it in class

Subtracting the first equation from the other two gives $(t-1)y=1$ and $(t-1)z=2$, and then dividing by $t-1$ is the only delicate step. If $t$ is not $1$ we divide and get exactly one solution, $x=\frac{t-4}{t-1}$, $y=\frac1{t-1}$, $z=\frac2{t-1}$. If $t=1$ all three equations have the same left side $x+y+z$ with different right sides, so there is no solution.
