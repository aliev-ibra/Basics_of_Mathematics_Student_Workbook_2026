# Problem 3

## The original problem
Find the equation of the plane through $P=(1,-2,3)$ and perpendicular to $n=(2,1,-1)$. Check the result by substituting the point P and explain the role of the normal vector.

This is a 3D problem (three coordinates per point).

## What we are looking for
We need the equation of a single plane in three-dimensional space. We know one point that the plane passes through and a vector perpendicular to the plane, and we must produce the plane's equation, verify the given point satisfies it, and explain what the normal vector means geometrically.

## The idea we need
The point-normal form of a plane is
$$n\cdot(X-P) = 0,$$
where P is a known point on the plane, n is a nonzero normal vector perpendicular to the plane, and $X=(x,y,z)$ is any point on the plane. This works because $X-P$ is a vector lying in the plane, and the dot product with the normal is zero exactly when two vectors are perpendicular. Expanding gives
$$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$
for $n=(a,b,c)$ and $P=(x_0,y_0,z_0)$.

## Step-by-step solution
1. Identify the data: point $P=(1,-2,3)$ so $(x_0,y_0,z_0)=(1,-2,3)$, and normal $n=(2,1,-1)$ so $(a,b,c)=(2,1,-1)$.

2. Apply the point-normal form:
   $$(2,1,-1)\cdot\big((x,y,z)-(1,-2,3)\big) = 0.$$

3. Form the difference vector:
   $$(x,y,z)-(1,-2,3) = (x-1,\; y-(-2),\; z-3) = (x-1,\; y+2,\; z-3).$$

4. Compute the dot product:
   $$2(x-1) + 1(y+2) + (-1)(z-3) = 0.$$

5. Expand and simplify:
   $$2x-2 + y+2 - z + 3 = 0,$$
   $$2x + y - z + 3 = 0.$$

   So the plane equation is $2x+y-z+3=0$.

6. Check by substituting P=(1,-2,3):
   $$2(1) + (-2) - (3) + 3 = 2 - 2 - 3 + 3 = 0.$$
   The point satisfies the equation.

## Why each step is valid
- The point-normal form is valid because any vector from P to another point X in the plane lies in the plane, and by definition the normal n is perpendicular to every such vector, so their dot product is zero.
- Forming $X-P$ gives the vector from P to X, which is a direction lying in the plane when X is in the plane.
- Expanding the dot product uses bilinearity of the dot product and distributes the scalar coefficients over each coordinate.
- Substituting P checks correctness: P must satisfy its own plane equation since P is on the plane, and $n\cdot(P-P)=n\cdot(0)=0$ always holds.

## Final answer (in words)
The plane passing through P=(1,-2,3) and perpendicular to n=(2,1,-1) has equation $2x+y-z+3=0$. Substituting P gives zero, confirming P lies on the plane. The normal vector n is perpendicular to the plane and to every vector lying in it.

## Verification
I verify independently by expanding $n\cdot(X-P)$ once more: $(2,1,-1)\cdot(x-1,y+2,z-3) = 2(x-1)+(y+2)-(z-3) = 2x-2+y+2-z+3 = 2x+y-z+3$, which matches. Also, the constant term can be checked as $-n\cdot P = -(2\cdot1 + 1\cdot(-2) + (-1)\cdot3) = -(2-2-3) = -(-3) = 3$, agreeing with the +3 in the equation.

## Common mistakes
- Writing $y-2$ instead of $y+2$ when forming $y-(-2)$; the double minus becomes a plus.
- Using the point coordinates as the normal or the normal coordinates as the point; the normal defines orientation, the point defines position.
- Forgetting that the plane equation can be multiplied by any nonzero constant, so equivalent forms like $4x+2y-2z+6=0$ describe the same plane.
- Omitting the verification step, which would leave an undetected sign error in the constant term.

## How I would explain it in class
I would say that a plane is determined when we know one point on it and one arrow sticking straight out of it, which is the normal. Then every other point X in the plane must make the arrow from P to X perpendicular to that normal arrow, which is exactly what the dot product equaling zero says. Substituting P back in is just a sanity check that our starting point really is on the plane we built.
