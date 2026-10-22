# Problem 6

## The original problem
Given
$$\Pi_1:x+y+z=1,\qquad \Pi_2:x-y=2.$$
First use the normal vectors to decide whether the planes are parallel. If not, compute the angle between them and explain why the normal vectors alone are enough for this calculation.

This is a 3D problem (three coordinates per point).

## What we are looking for
We want to analyze two planes in space. Specifically we need to decide whether they are parallel using their normal vectors, and if they are not parallel, compute the angle between them. We also need to explain why knowing the normal vectors is sufficient to determine the angle.

## The idea we need
A plane with equation $ax+by+cz=d$ has normal vector $n=(a,b,c)$, which is perpendicular to the plane. Two planes are parallel iff their normal vectors are parallel (scalar multiples of each other).

If two planes are not parallel, they intersect in a line, and the angle between the planes equals the angle between their normal vectors (or its supplement; we take the acute angle). The angle $\theta$ between two normals $n_1$ and $n_2$ is given by
$$\cos\theta = \frac{|n_1\cdot n_2|}{|n_1|\,|n_2|},$$
where $n_1\cdot n_2$ is the dot product and $|n|$ is the length of $n$. The absolute value ensures we get the acute angle between $0$ and $90$ degrees.

The normal vectors alone are enough because tilting a plane is exactly tilting its normal: the angle between two planes is defined as the angle between their normals, since both the plane and its normal rotate together.

## Step-by-step solution
1. Identify the normal vectors from the plane equations.
   For $\Pi_1:x+y+z=1$, the coefficients of $x,y,z$ give
   $$n_1=(1,1,1).$$
   For $\Pi_2:x-y=2$, we write it as $x-y+0z=2$, so
   $$n_2=(1,-1,0).$$

2. Decide whether the planes are parallel. The planes are parallel iff $n_1$ and $n_2$ are scalar multiples.
   Is there a number $k$ such that $(1,1,1)=k(1,-1,0)$? Comparing components:
   - first: $1=k\cdot1$, so $k=1$;
   - second: $1=k\cdot(-1)$, so $k=-1$;
   - third: $1=k\cdot0=0$, impossible.
   Since no single $k$ works, the normals are not proportional, so the planes are not parallel.

3. Compute the angle between the planes using the normals.
   Dot product:
   $$n_1\cdot n_2 = (1)(1) + (1)(-1) + (1)(0) = 1 - 1 + 0 = 0.$$
   Lengths:
   $$|n_1| = \sqrt{1^2+1^2+1^2} = \sqrt{3},$$
   $$|n_2| = \sqrt{1^2+(-1)^2+0^2} = \sqrt{2}.$$
   Therefore
   $$\cos\theta = \frac{|0|}{\sqrt{3}\sqrt{2}} = 0.$$
   So $\theta = 90^\circ$ (or $\pi/2$ radians).

4. The planes are perpendicular to each other.

## Why each step is valid
- The normal vector is read directly from the coefficients of $x,y,z$ because the plane equation can be written as $n\cdot(x,y,z)=d$, which says every point in the plane has the same dot product with $n$.
- Parallel planes have parallel normals because both planes have the same orientation in space; checking proportionality of normals is therefore the correct test.
- The angle between two planes equals the angle between their normals because the normal measures the tilt of the plane; if two normals make angle $\theta$, the planes make the same angle (or $180^\circ-\theta$, and we take the acute value).
- The dot-product formula for $\cos\theta$ is the standard formula for the angle between two vectors, valid for any nonzero vectors in space.

## Final answer (in words)
The planes are not parallel because their normals $(1,1,1)$ and $(1,-1,0)$ are not proportional. They are perpendicular: the angle between them is $90^\circ$, since the dot product of the normals is zero. The normal vectors alone determine the angle because the angle between two planes equals the angle between their normals.

## Verification
I recompute the dot product independently: $n_1\cdot n_2 = 1\cdot1 + 1\cdot(-1) + 1\cdot0 = 0$, confirming perpendicularity. I also check parallelism another way: $\Pi_1$ has normal with all nonzero components, while $\Pi_2$ has normal with zero z-component, so they cannot point in the same direction. The angle computation gives $\cos\theta=0$, so $\theta=90^\circ$, consistent with the dot product being zero.

## Common mistakes
- Forgetting to write $x-y=2$ as $x-y+0z=2$ and missing the zero z-component in the normal vector.
- Omitting the absolute value in the cosine formula, which could give a negative cosine and an obtuse angle instead of the acute angle between planes.
- Concluding the planes are parallel just because the dot product is zero; a zero dot product actually means perpendicular, not parallel.
- Giving the angle between normals as obtuse instead of taking the acute angle between planes.

## How I would explain it in class
I would say each plane comes with an arrow sticking straight out of it, called the normal, and we can read that arrow right off the equation. Two planes are parallel exactly when those arrows point the same way, which they do not here. To find the angle between the planes, we just measure the angle between the two arrows, and here the arrows are perpendicular, so the planes meet at a right angle.
