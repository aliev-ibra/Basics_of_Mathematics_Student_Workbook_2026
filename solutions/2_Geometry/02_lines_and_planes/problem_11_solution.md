# Problem 11

## The original problem
Find the equation of the plane containing
$$(x,y,z)=(1,0,2)+t(1,1,-1)$$
and the point $P=(0,2,1)$. Check that both the entire line and the point lie in the plane you obtain.

## What we are looking for
We want one plane that contains the whole given line and also the point $P$. We want its equation in the form $ax+by+cz=d$. Then we must check that every point of the line, and the point $P$, satisfies this equation.

## The idea we need
A plane is fixed by one point and two different directions lying in it. A direction vector is an arrow that points along a line. If two direction vectors do not point the same way or opposite ways, they are called independent.

Here the line gives one point $A=(1,0,2)$ and one direction $v=(1,1,-1)$. A second direction comes from joining $A$ to the extra point $P$. The cross product of two vectors is a new vector that stands at a right angle to both of them. So the cross product of the two directions is a normal vector of the plane, the arrow standing straight out of it. With a normal vector and a point, we can write the equation of the plane.

## Step-by-step solution
1. Take the point $A=(1,0,2)$ on the line and the direction $v=(1,1,-1)$.
2. Build the second direction by subtracting $A$ from $P$:
$$w=P-A=(0-1,\;2-0,\;1-2)=(-1,2,-1).$$
3. Check that $v$ and $w$ are independent. The entries of $w$ are not a constant multiple of the entries of $v$: the first entries $1$ and $-1$ would force the multiple $-1$, but then the second entries would give $-1$ and not $2$. So the vectors point in different directions, and $P$ is not on the line.
4. Compute the normal vector by the cross product $n=v\times w$:
$$n=\big(1\cdot(-1)-(-1)\cdot 2,\;\;(-1)\cdot(-1)-1\cdot(-1),\;\;1\cdot 2-1\cdot(-1)\big)=(1,\;2,\;3).$$
5. Write the plane through $A$ with normal $n=(1,2,3)$:
$$x+2y+3z=d.$$
6. Find $d$ by putting in $A=(1,0,2)$:
$$d=1+0+6=7.$$
7. The plane is
$$x+2y+3z=7.$$

## Why each step is valid
- A plane containing a line must contain the point $A$ of that line and the direction $v$. A plane containing $P$ as well must contain the arrow from $A$ to $P$, which is $w$.
- The vectors $v$ and $w$ both lie in the plane, so a vector perpendicular to both is perpendicular to the plane. This is what the cross product gives us.
- Independence in step 3 matters. If $v$ and $w$ were parallel, the cross product would be the zero vector and would give no plane.
- The equation $n\cdot(x,y,z)=d$ describes all points whose dot product with $n$ equals the value at $A$. Moving inside the plane does not change this value, because the movement is perpendicular to $n$.

## Final answer (in words)
The plane containing the given line and the point $P=(0,2,1)$ has the equation $x+2y+3z=7$. Its normal vector is $(1,2,3)$.

## Verification
I check the point and then the whole line, by substituting into the equation $x+2y+3z=7$.

The point $P=(0,2,1)$: $0+2\cdot 2+3\cdot 1=0+4+3=7$. It is in the plane.

The whole line: a general point is $(1+t,\;t,\;2-t)$. Then
$$(1+t)+2t+3(2-t)=1+t+2t+6-3t=7.$$
The terms with $t$ cancel: $t+2t-3t=0$. So the result is $7$ for every value of $t$, and the entire line lies in the plane.

A second independent check: the normal $n=(1,2,3)$ must be perpendicular to both directions. We get $n\cdot v=1+2-3=0$ and $n\cdot w=-1+4-3=0$. Both are zero.

## Common mistakes
- Using $P$ itself as a direction vector. A direction must be a difference of two points, here $P-A$.
- Making a sign error in the cross product, so that the normal is not perpendicular to $v$ and $w$. The dot product check catches this.
- Checking only one point of the line, such as $A$. The point of the exercise is to check that the whole line is in the plane, which needs a general point with $t$.
- Not noticing that $P$ must not be on the line, otherwise the plane is not unique.

## How I would explain it in class
The line gives us a point and a direction, and the extra point $P$ gives us a second direction by joining it to the line. Two different directions fix a tilted flat sheet, and the cross product gives the arrow standing straight out of that sheet. With that arrow and one point we write $x+2y+3z=7$, and putting in a general point of the line, the $t$ terms cancel, which proves the whole line is inside.
