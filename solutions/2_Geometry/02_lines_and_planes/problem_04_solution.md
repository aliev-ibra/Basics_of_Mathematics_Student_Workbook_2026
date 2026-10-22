# Problem 4

## The original problem
Find the equation of the plane through
$$A=(1,0,0),\quad B=(0,1,0),\quad C=(0,0,1).$$
First construct two vectors lying in the plane, and then use the cross product. Check the resulting equation on all three points.

This is a 3D problem (three coordinates per point).

## What we are looking for
We want the equation of the single plane that passes through the three given points in space. To write it we need a normal vector to the plane, which we obtain from the cross product of two vectors that lie in the plane, and then we verify that all three given points satisfy the final equation.

## The idea we need
If two vectors $u$ and $v$ lie in a plane, their cross product $n = u \times v$ is a normal vector to that plane, perpendicular to both $u$ and $v$.

Once a normal vector $n=(a,b,c)$ and a point $P=(x_0,y_0,z_0)$ on the plane are known, the point-normal form of the plane is
$$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0,$$
which expands to the general form $ax + by + c = d$.

The cross product is computed as
$$u \times v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{vmatrix}.$$

## Step-by-step solution
1. Construct two vectors lying in the plane using point A as the common origin:
   $$\vec{AB} = B - A = (0-1,\; 1-0,\; 0-0) = (-1,\; 1,\; 0),$$
   $$\vec{AC} = C - A = (0-1,\; 0-0,\; 1-0) = (-1,\; 0,\; 1).$$
   Both $\vec{AB}$ and $\vec{AC}$ connect pairs of points in the plane, so both lie in the plane.

2. Compute the normal vector as the cross product $n = \vec{AB} \times \vec{AC}$:
   $$n = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{vmatrix}.$$
   Expanding:
   - $\mathbf{i}$-component: $(1)(1) - (0)(0) = 1$,
   - $\mathbf{j}$-component: $-\big((-1)(1) - (0)(-1)\big) = -(-1) = 1$,
   - $\mathbf{k}$-component: $(-1)(0) - (1)(-1) = 0 - (-1) = 1$.

   So
   $$n = (1,\; 1,\; 1).$$

3. Write the plane equation in point-normal form using point $A=(1,0,0)$ and normal $n=(1,1,1)$:
   $$1(x-1) + 1(y-0) + 1(z-0) = 0.$$
   Simplifying:
   $$x - 1 + y + z = 0,$$
   $$x + y + z = 1.$$

4. Check the equation on all three points:
   - For $A=(1,0,0)$: $1 + 0 + 0 = 1$. ✓
   - For $B=(0,1,0)$: $0 + 1 + 0 = 1$. ✓
   - For $C=(0,0,1)$: $0 + 0 + 1 = 1$. ✓

## Why each step is valid
- The vectors $\vec{AB}$ and $\vec{AC}$ lie in the plane because they join points that are all in the plane.
- The cross product of two non-parallel vectors in a plane is perpendicular to both, hence normal to the plane. Here $\vec{AB}$ and $\vec{AC}$ are not parallel, so the cross product gives a valid normal.
- The point-normal form is valid because for any point $X=(x,y,z)$ in the plane, the vector $X-A$ lies in the plane and is perpendicular to the normal $n$, so $n\cdot(X-A)=0$.
- Substituting each given point into the equation confirms membership: a point lies in the plane exactly when its coordinates satisfy the equation.

## Final answer (in words)
The plane through A, B, and C has normal vector $(1,1,1)$ and equation $x + y + z = 1$. All three given points satisfy this equation, so it is the correct plane.

## Verification
I recompute the normal using the other pair of vectors as an independent check. $\vec{BA} = (1,-1,0)$ and $\vec{BC} = (0,-1,1)$. Their cross product is $\vec{BA}\times\vec{BC} = ((-1)(1)-(0)(-1),\; (0)(0)-(1)(1),\; (1)(-1)-(-1)(0)) = (-1,\;-1,\;-1) = -(1,1,1)$, which is parallel to $(1,1,1)$, confirming the same normal direction. Also, substituting B and C into $x+y+z=1$ gives 1 in both cases, as shown above.

## Common mistakes
- Using vectors that do not both lie in the plane, for example taking a vector from outside the set of three points.
- Forgetting the minus sign on the $\mathbf{j}$-component when expanding the cross product determinant.
- Using the wrong sign in the point-normal form, writing $a(x-x_0)+b(y-y_0)+c(z-z_0)=d$ with a nonzero $d$ instead of moving the constant correctly.
- Checking only one or two points instead of all three, which could miss an error in the constant term.

## How I would explain it in class
I would draw the three points and connect them to form a triangle, because that triangle sits inside the plane we want. Then I would take two sides of the triangle as vectors lying in the plane and cross them to get an arrow sticking straight out, which is our normal. Finally I would anchor that normal arrow at point A and write down the equation, checking that B and C also land on it.
