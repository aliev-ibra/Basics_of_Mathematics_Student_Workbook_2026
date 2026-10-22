# Problem 14

## The original problem

Let
$$f(x)=\begin{cases}x+1,&-1\le x<1,\\2,&1\le x\le3.\end{cases}$$
Sketch the graph, decide where to split the integral, compute
$$\int_{-1}^{3}f(x)\,dx$$
and verify the result geometrically.

> **Why this problem:** it requires understanding the definition of the function before carrying out the calculation.

## What we are looking for

We want the area under a graph that is made of two pieces with different formulas. The sketch tells us the shape. The split point tells us where one formula ends and the other begins. Then we compute and check with simple areas.

## The idea we need

**Additivity.** An integral over $[a,c]$ can be split at a point $b$ in the middle: $\int_a^c f\,dx=\int_a^b f\,dx+\int_b^c f\,dx$. For a piecewise function we split exactly where the formula changes, and we use the correct formula on each piece.

## Step-by-step solution

**Step 1. Sketch the graph in words.** For $x$ from $-1$ to $1$ the graph is the line $y=x+1$. It starts at the point $(-1,0)$ on the axis and rises to the point $(1,2)$. For $x$ from $1$ to $3$ the graph is the horizontal line $y=2$. The two pieces meet at $(1,2)$, so there is no jump.

**Step 2. Choose the split point.** The formula changes at $x=1$, so we split there:
$$\int_{-1}^{3}f(x)\,dx=\int_{-1}^{1}(x+1)\,dx+\int_{1}^{3}2\,dx.$$

**Step 3. The first piece.** An antiderivative of $x+1$ is $\frac{x^2}{2}+x$, so
$$\int_{-1}^{1}(x+1)\,dx=\left(\frac12+1\right)-\left(\frac12-1\right)=\frac32+\frac12=2.$$

**Step 4. The second piece.** An antiderivative of $2$ is $2x$, so
$$\int_{1}^{3}2\,dx=2\cdot3-2\cdot1=4.$$

**Step 5. Add.** The total is $2+4=6$.

## Why each step is valid

- Step 1 is valid because each formula is used only on its own interval, and at $x=1$ both formulas give the value $2$.
- Step 2 is valid because of additivity, and a single value at the point $x=1$ does not change the area.
- Steps 3 and 4 are valid because of the Fundamental Theorem of Calculus, and the derivatives of $\frac{x^2}{2}+x$ and $2x$ are $x+1$ and $2$.
- Step 5 is valid because the two pieces together cover $[-1,3]$ exactly once.

## Final answer (in words)

The integral is six: $\int_{-1}^{3}f(x)\,dx=6$. It is the sum of $2$ from the rising part and $4$ from the flat part. We split at $x=1$, because that is where the formula changes.

## Verification

**Check 1: geometry.** On $[-1,1]$ the region under the line is a right triangle with base $2$ and height $2$, so its area is $\frac12\cdot2\cdot2=2$. On $[1,3]$ the region is a rectangle with width $2$ and height $2$, so its area is $4$. The sum is $6$.

**Check 2: differentiate.** The derivative of $\frac{x^2}{2}+x$ is $x+1$ and the derivative of $2x$ is $2$, so both antiderivatives are correct.

**Check 3: the average height.** The function rises from $0$ to $2$ on the first piece, with average height $1$, and stays at $2$ on the second piece. The total is $1\cdot2+2\cdot2=6$.

## Common mistakes

- Using one formula on the whole interval. Both $x+1$ and $2$ would give the wrong total $8$ here.
- Splitting at the wrong place, for example at $0$.
- Forgetting that on $[1,3]$ the antiderivative of the constant $2$ is $2x$, not $2$.

## How I would explain it in class

The graph is a rising line from $(-1,0)$ to $(1,2)$ followed by a flat line at height $2$ up to $x=3$, so I split the integral at $x=1$. The first piece is $\int_{-1}^{1}(x+1)\,dx=2$ and the second is $\int_{1}^{3}2\,dx=4$, so the total is $6$. The same numbers appear as the area of a triangle, $\frac12\cdot2\cdot2=2$, and the area of a rectangle, $2\cdot2=4$.
