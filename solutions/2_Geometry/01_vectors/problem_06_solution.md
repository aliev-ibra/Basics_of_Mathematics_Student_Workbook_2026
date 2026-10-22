# Problem 06

## The original problem
Find the projection of $u=(4,2)$ onto the direction $v=(1,1)$. Then compute
$$r=u-\operatorname{proj}_v u$$
and verify that $r\cdot v=0$. Explain this result geometrically.

## What we are looking for
We need the scalar projection factor and/or the vector projection $\operatorname{proj}_v u$, $r = u - \operatorname{proj}_v u$, verification $r\cdot v=0$, and geometric explanation (decomposition into parallel and perpendicular components).

## The idea we need
The vector projection of $u$ onto a nonzero direction $v$ is
$$
\operatorname{proj}_v u = \frac{u\cdot v}{v\cdot v} v.
$$
(Equivalently $\frac{u\cdot v}{\|v\|^2}v$; note $v\cdot v=\|v\|^2$.)  
This gives the component of $u$ parallel to $v$. The remainder
$$
r = u - \operatorname{proj}_v u
$$
is perpendicular to $v$ (the perpendicular component). This is an orthogonal decomposition $u = u_\parallel + u_\perp$ with $u_\parallel \parallel v$, $u_\perp \perp v$. Conditions: $v \neq 0$, Euclidean dot product.

## Step-by-step solution

1. **Compute needed dot products:**
   $u\cdot v = 4\cdot 1 + 2\cdot 1 = 4 + 2 = 6$.
   $v\cdot v = 1^2 + 1^2 = 1 + 1 = 2$ (which is $\|v\|^2$).

2. **Find the projection $\operatorname{proj}_v u$:**
   $\operatorname{proj}_v u = \frac{u\cdot v}{v\cdot v} v = \frac{6}{2} (1,1) = 3 (1,1) = (3,3)$.
   (This is in the direction of $v=(1,1)$.)

3. **Compute $r = u - \operatorname{proj}_v u$:**
   $r = (4,2) - (3,3) = (4-3,\ 2-3) = (1,\ -1)$.

4. **Verify $r\cdot v = 0$:**
   $r\cdot v = 1\cdot 1 + (-1)\cdot 1 = 1 - 1 = 0$.
   (Independent check confirms perpendicularity.)

## Why each step is valid

- **Formula for projection:** derived from minimizing $\|u - t v\|^2$ or from requiring $u-t v \perp v \implies (u-t v)\cdot v=0 \implies t=\frac{u\cdot v}{v\cdot v}$.
- **Dot products:** Euclidean in $\mathbb{R}^2$.
- **Orthogonality of remainder:** algebraically $(u - t v)\cdot v = u\cdot v - t (v\cdot v)=0$ when $t$ is chosen as above.
- **Check:** direct computation confirms.

## Final answer (in words)
In plain words: we decompose $u$ into a part along $v$ (the projection) and a part perpendicular to $v$ (the remainder). The projection is $(3,3)$ in the direction of $(1,1)$; subtracting gives $(1,-1)$ which is at right angles to $v$. Geometrically this is the orthogonal projection dropping a perpendicular onto the line along $v$.  
In symbols: $\operatorname{proj}_v u = \frac{6}{2}(1,1)=(3,3),\ r=(4,2)-(3,3)=(1,-1),\ r\cdot v=0$.

## Verification
Recomputed $u\cdot v=6, v\cdot v=2$ OK. Projection scaled $(1,1)$ by 3 OK. $r=(1,-1)$ dot with $(1,1)$ gives 0 OK. Independent check passes.

## Common mistakes
- **Using $\|v\|$ in denominator without square:** formula is $u\cdot v/(v\cdot v)$ not $u\cdot v/\|v\|$.
- **Projecting onto $u$ instead of $v$:** order matters.
- **Forgetting to subtract:** $r$ must be $u - \operatorname{proj}_v u$.
- **Assuming perpendicular without check:** the problem requires verification.

## How I would explain it in class
To get the closest component of $u$ along direction $v$, we project: the coefficient is $(u\cdot v)/(v\cdot v)$ giving $(3,3)$.  
The leftover is $u$ minus that projection, which turns out to be perpendicular to $v$ — we can check the dot product is zero.  
This gives a clean split into parallel and perpendicular parts, which is exactly what the orthogonal decomposition does.
