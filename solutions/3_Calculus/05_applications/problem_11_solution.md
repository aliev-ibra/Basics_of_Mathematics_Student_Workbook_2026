# Problem 11

## The original problem

The region under the graph
$$
y=\sqrt{x},\qquad x\in[0,4],
$$
is rotated about the $x$-axis.

1. Construct the integral describing the volume using the disk method.
2. Compute the volume.
3. Explain where the factor $\pi y^2$ in the integral comes from.

> **Why this problem:** it teaches how to construct an integral from the geometry of cross-sections instead of applying a volume formula without understanding its origin.

## What we are looking for

We have a flat region between the curve $y=\sqrt x$ and the $x$-axis, from $x=0$ to $x=4$. We spin it around the $x$-axis and get a solid, a bit like a bowl or a trumpet. We want its volume, and we want to understand where the integral comes from, so that we do not just memorise a formula.

## The idea we need

We cut the solid into very thin slices, perpendicular to the $x$-axis. Each slice is almost a short cylinder, a disk. We find the volume of one disk and add all disks. Adding infinitely many thin pieces is an integral.

## Step-by-step solution

1. **One slice.** Choose a point $x$ between $0$ and $4$. The slice at $x$ has thickness $dx$, a very small length.

2. **Radius of the disk.** The region reaches up to the curve, so spinning it gives a circle of radius
$$
y=\sqrt x.
$$

3. **Volume of one disk.** Base area times thickness:
$$
\pi y^2\,dx=\pi(\sqrt x)^2\,dx=\pi x\,dx.
$$

4. **Add all disks.**
$$
V=\int_0^4\pi x\,dx.
$$

5. **Compute.** An antiderivative of $\pi x$ is $\frac{\pi x^2}{2}$, so
$$
V=\frac{\pi\cdot4^2}{2}-0=8\pi.
$$

6. **Numerical value.** $8\pi\approx25{,}13$ cubic units.

## Why each step is valid

- The factor $\pi y^2$ is the area of a circle of radius $y$. When the region is spun, the vertical segment of height $y$ at position $x$ turns into a full circle with radius $y$, and the segment's length is the radius.
- Multiplying the area $\pi y^2$ by the small thickness $dx$ gives the volume of a thin cylinder, because volume of a cylinder is base area times height.
- Slices stand perpendicular to the axis of rotation, so every slice is a full disk with no hole. The region touches the $x$-axis, so there is nothing missing inside.
- The sum of all slice volumes becomes the definite integral as the thickness goes to zero.
- Squaring removes the root: $(\sqrt x)^2=x$ for $x\ge0$, which is true on the whole interval $[0,4]$.

## Final answer (in words)

The volume is given by the integral
$$
V=\int_0^4\pi(\sqrt x)^2\,dx=\int_0^4\pi x\,dx=8\pi\approx25{,}13
$$
cubic units. The factor $\pi y^2$ is the area of the circular cross-section: the height $y=\sqrt x$ of the curve becomes the radius of a disk when the region is rotated.

## Verification

- **Another formula, shells.** Slice the solid into thin tubes around the $x$-axis instead. At radius $y$ the tube extends from $x=y^2$ to $x=4$, with height $4-y^2$, and $y$ goes from $0$ to $2$. The volume is
$$
\int_0^2 2\pi y\,(4-y^2)\,dy=2\pi\left[2y^2-\frac{y^4}{4}\right]_0^2=2\pi(8-4)=8\pi.
$$
- **Cone comparison.** The solid fits inside a cylinder of radius $2$ and length $4$, volume $16\pi$, and it is more than the cone with the same radius and length, volume $\frac{16\pi}{3}$. The value $8\pi$ is between them, exactly half of the cylinder.
- **Numerical sum.** Use four disks of thickness $1$ with the radius taken at the middle: $x=0{,}5,1{,}5,2{,}5,3{,}5$ give $\pi(0{,}5+1{,}5+2{,}5+3{,}5)=8\pi$.

## Common mistakes

- Forgetting the factor $\pi$ and integrating $y^2$ only.
- Writing $\pi y$ or $\pi\sqrt{x}$ without squaring the radius.
- Squaring wrongly: $(\sqrt x)^2=x$, so the integrand is $\pi x$, not $\pi\sqrt x$.
- Using the wrong limits, for example $0$ to $2$ for $x$ (the number $2$ is the largest radius, not the largest $x$).

## How I would explain it in class

Cutting the solid into thin slices gives disks, and a disk with radius $y=\sqrt x$ and thickness $dx$ has volume $\pi y^2\,dx$, because the area of a circle is $\pi$ times the radius squared. Adding all disks gives $V=\int_0^4\pi x\,dx=8\pi$. A second method with cylindrical shells gives the same $8\pi\approx25{,}13$, so the result is reliable.
