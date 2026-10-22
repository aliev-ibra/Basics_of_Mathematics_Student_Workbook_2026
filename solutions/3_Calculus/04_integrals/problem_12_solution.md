# Problem 12

## The original problem

Compare
$$\int_{-2}^{2}x\,dx$$
and
$$\int_{-2}^{2}|x|\,dx.$$
Before calculating, predict the results from symmetry and a sketch, then carry out the calculation and explain the difference.

> **Why this problem:** it teaches how to use symmetry and geometry before applying a computational procedure.

## What we are looking for

We want two numbers, one for $x$ and one for $|x|$, both on the interval from $-2$ to $2$. We first guess them from symmetry and a picture. Then we compute them and explain why they differ.

## The idea we need

**Symmetry.** The interval $[-2,2]$ is symmetric around $0$. A function is *odd* if $f(-x)=-f(x)$, and its graph is symmetric about the origin. A function is *even* if $f(-x)=f(x)$, and its graph is a mirror image across the $y$-axis.

**Signed area.** For an odd function the left part cancels the right part, so the integral over a symmetric interval is $0$. For an even function the two halves are equal, so the integral is twice the integral over $[0,2]$.

**Absolute value.** The symbol $|x|$ means the distance of $x$ from $0$. It equals $x$ when $x\ge0$ and $-x$ when $x<0$.

## Step-by-step solution

**Step 1. Prediction for $x$.** The function $x$ is odd, because its value at $-x$ is the negative of its value at $x$. The graph is a line through the origin. The triangle on the left lies below the axis and the triangle on the right lies above it, and they are mirror copies of each other. So we predict $0$.

**Step 2. Prediction for $|x|$.** The graph of $|x|$ is a V shape with its corner at the origin. It never goes below the axis, so nothing can cancel. The function is even, so we predict a positive number, twice the area of the right half.

**Step 3. Compute the first integral.** An antiderivative of $x$ is $\frac{x^2}{2}$, so
$$\int_{-2}^{2}x\,dx=\frac{2^2}{2}-\frac{(-2)^2}{2}=2-2=0.$$

**Step 4. Split the second integral.** Because $|x|=-x$ on $[-2,0]$ and $|x|=x$ on $[0,2]$, we write
$$\int_{-2}^{2}|x|\,dx=\int_{-2}^{0}(-x)\,dx+\int_{0}^{2}x\,dx.$$

**Step 5. Compute both pieces.** The first piece is $\left[-\frac{x^2}{2}\right]_{-2}^{0}=0-\left(-2\right)=2$. The second piece is $\left[\frac{x^2}{2}\right]_0^2=2$. The sum is $4$.

## Why each step is valid

- Steps 1 and 2 are valid because the shape and the symmetry of the graph decide the signs of the pieces before any formula is used.
- Step 3 is valid because of the Fundamental Theorem of Calculus.
- Step 4 is valid because the integral can be split at a point inside the interval, and $|x|$ has a different formula on each side of $0$. Without the split we cannot integrate $|x|$ directly.
- Step 5 is valid because on $[-2,0]$ the function $-x$ has antiderivative $-\frac{x^2}{2}$, and each piece is the area of a triangle with base $2$ and height $2$, which is $2$.

## Final answer (in words)

The first integral is zero: $\int_{-2}^{2}x\,dx=0$. The second integral is four: $\int_{-2}^{2}|x|\,dx=4$. They differ because $x$ is negative on the left, so its two triangles cancel, while $|x|$ is never negative, so its two triangles add.

## Verification

**Check 1: geometry.** Each triangle has base $2$ and height $2$, so its area is $\frac12\cdot2\cdot2=2$. For $x$ the signed total is $-2+2=0$. For $|x|$ it is $2+2=4$.

**Check 2: differentiate.** The derivative of $\frac{x^2}{2}$ is $x$, and the derivative of $-\frac{x^2}{2}$ is $-x$, which is $|x|$ on $x<0$.

**Check 3: the predictions.** Both predictions from symmetry, zero and a positive number, agree with the calculation.

## Common mistakes

- Treating $\int|x|\,dx$ as $\int x\,dx$, which gives $0$ instead of $4$.
- Writing $\int_{-2}^{2}|x|\,dx=\frac{x^2}{2}$ without splitting at $0$.
- Using the symmetry argument for an even function and writing $0$.
- Forgetting that the first piece, $\int_{-2}^{0}(-x)\,dx$, is positive, because $-x$ is positive there.

## How I would explain it in class

The function $x$ is odd, so its graph has equal triangles below and above the axis, and the integral is $0$. The function $|x|$ is even and never negative, so its two triangles of area $2$ add up to $4$. The integral of $x$ is signed, and the integral of $|x|$ is the ordinary area.
