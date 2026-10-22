# Problem 10

## The original problem

The points $A=(0,0,0)$, $B=(2,1,0)$, and $C=(1,3,2)$ form a triangle. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$, compute the area of the parallelogram using the cross product, and then find the area of the triangle. Explain the factor $\frac12$.

## What we are looking for

We need two edge vectors of the triangle that start at $A$. With them we compute the area of the parallelogram they span, and then the area of the triangle. We must also explain why the triangle has half the area of the parallelogram.

## The idea we need

Two vectors $p$ and $q$ that start at the same point span a parallelogram. The length of their cross product equals the area of that parallelogram:
$$\text{Area of parallelogram}=\|p\times q\|.$$
The reason is that $\|p\times q\|=\|p\|\,\|q\|\sin\theta$, where $\theta$ is the angle between the vectors. The number $\|p\|$ is the base, and $\|q\|\sin\theta$ is the height of the parallelogram, so base times height is the area.

The cross product in coordinates is
$$p\times q=(p_2q_3-p_3q_2,\;\;p_3q_1-p_1q_3,\;\;p_1q_2-p_2q_1).$$
The length of a vector is $\|w\|=\sqrt{w_1^2+w_2^2+w_3^2}$.

## Step-by-step solution

**Step 1: build the edge vectors.** A vector from $A$ to a point is the end point minus $A$. Because $A$ is the origin, the vectors have the same coordinates as the points:
$$\overrightarrow{AB}=B-A=(2,1,0),\qquad \overrightarrow{AC}=C-A=(1,3,2).$$

**Step 2: compute the cross product.** Here $p=\overrightarrow{AB}=(2,1,0)$ and $q=\overrightarrow{AC}=(1,3,2)$.

- First component: $1\cdot2-0\cdot3=2$.
- Second component: $0\cdot1-2\cdot2=-4$.
- Third component: $2\cdot3-1\cdot1=5$.

So
$$\overrightarrow{AB}\times\overrightarrow{AC}=(2,-4,5).$$

**Step 3: the length is the parallelogram area.**
$$\|\overrightarrow{AB}\times\overrightarrow{AC}\|=\sqrt{2^2+(-4)^2+5^2}=\sqrt{4+16+25}=\sqrt{45}=3\sqrt5.$$
So the parallelogram has area $3\sqrt5$.

**Step 4: halve it for the triangle.**
$$\text{Area of triangle }ABC=\frac12\cdot3\sqrt5=\frac{3\sqrt5}{2}.$$
Numerically this is about $3.354$.

## Why each step is valid

- Step 1 is valid because the arrow from $A$ to $B$ moves us from $A$ to $B$, so its coordinates are those of $B$ minus those of $A$.
- Step 3 uses the fact that the cross product length equals base times height, as explained above. The triangle $ABC$ has the same two sides $AB$ and $AC$ as the parallelogram, so this is the right parallelogram.
- The factor $\frac12$ has a clear picture. Draw the parallelogram with vertices $A$, $B$, $C$ and a fourth vertex $D=B+C-A$. The diagonal from $B$ to $C$ cuts the parallelogram into two triangles. These two triangles are congruent, which means one can be turned by a half-turn about the midpoint of the diagonal to lie exactly on the other. So each has half of the total area, and triangle $ABC$ is one of them.

## Final answer (in words)

The edge vectors are $\overrightarrow{AB}=(2,1,0)$ and $\overrightarrow{AC}=(1,3,2)$. Their cross product is $(2,-4,5)$, so the parallelogram has area $3\sqrt5$. The triangle is half of the parallelogram, so its area is
$$\frac{3\sqrt5}{2}\approx3.354.$$

## Verification

I compute the area again without the cross product. Use $\text{Area of parallelogram}=\sqrt{\|p\|^2\|q\|^2-(p\cdot q)^2}$, which comes from $\sin^2\theta=1-\cos^2\theta$. We have $\|p\|^2=4+1+0=5$, $\|q\|^2=1+9+4=14$ and $p\cdot q=2+3+0=5$. Then
$$\sqrt{5\cdot14-5^2}=\sqrt{70-25}=\sqrt{45}=3\sqrt5,$$
which is the same value. Also the vector $(2,-4,5)$ must be perpendicular to both edges: $(2,-4,5)\cdot(2,1,0)=4-4+0=0$ and $(2,-4,5)\cdot(1,3,2)=2-12+10=0$. Both hold.

## Common mistakes

- Forgetting the factor $\frac12$ and giving $3\sqrt5$ as the triangle area.
- Giving the cross product vector $(2,-4,5)$ as the area. The area is a number, namely the length of that vector.
- Forgetting the square root, or computing $\sqrt{2+4+5}$ instead of $\sqrt{4+16+25}$.
- Taking vectors that do not start at the same vertex, for example $\overrightarrow{AB}$ and $\overrightarrow{CB}$.

## How I would explain it in class

The two edges from $A$ are $\overrightarrow{AB}=(2,1,0)$ and $\overrightarrow{AC}=(1,3,2)$, and the length of their cross product $(2,-4,5)$ is $\sqrt{45}=3\sqrt5$, which is the area of the parallelogram they span. The diagonal $BC$ cuts that parallelogram into two equal triangles, so the triangle area is half, $\frac{3\sqrt5}{2}$. I checked it with $\sqrt{5\cdot14-5^2}=\sqrt{45}$, which uses only lengths and a dot product.
