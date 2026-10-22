# Problem 9

## The original problem
Compute:
1. the distance from $P=(2,3)$ to the line $3x+4y-10=0$,
2. the distance from $Q=(2,-1,3)$ to the plane $2x-2y+z-4=0$.

Compare the two formulas and explain their common connection with the normal direction.

## What we are looking for
We want two lengths. The first is the length of the shortest segment from the point $P$ in the plane to the given line. The second is the length of the shortest segment from the point $Q$ in space to the given plane. We also want to explain why the two formulas look almost the same.

## The idea we need
A line in the plane, or a plane in space, has a normal vector. The normal vector is an arrow that stands at a right angle to the line or the plane. For the equation $ax+by+c=0$ the normal vector is $n=(a,b)$. For the equation $ax+by+cz+e=0$ it is $n=(a,b,c)$. The length of $n$, written $|n|$, is the square root of the sum of the squares of its entries.

The shortest way from a point to a line or plane is the straight segment that meets it at a right angle. That segment points along the normal direction. So the distance is the part of the journey measured along $n$. This gives the formula
$$\text{distance}=\frac{|\,\text{left side of the equation evaluated at the point}\,|}{|n|}.$$
The top is the number we get by putting the point into the left side. The bottom is the length of the normal. Dividing by $|n|$ turns the raw number into a true length.

## Step-by-step solution
**Part 1.** The line is $3x+4y-10=0$.

1. Read the normal vector: $n=(3,4)$. Its length is
$$|n|=\sqrt{3^2+4^2}=\sqrt{25}=5.$$
2. Put $P=(2,3)$ into the left side:
$$3\cdot 2+4\cdot 3-10=6+12-10=8.$$
3. Divide the absolute value of this number by $|n|$:
$$d_1=\frac{|8|}{5}=\frac{8}{5}.$$

**Part 2.** The plane is $2x-2y+z-4=0$.

1. Read the normal vector: $n=(2,-2,1)$. Its length is
$$|n|=\sqrt{2^2+(-2)^2+1^2}=\sqrt{9}=3.$$
2. Put $Q=(2,-1,3)$ into the left side:
$$2\cdot 2-2\cdot(-1)+3-4=4+2+3-4=5.$$
3. Divide the absolute value of this number by $|n|$:
$$d_2=\frac{|5|}{3}=\frac{5}{3}.$$

**Comparison.** In both cases we put the point into the left side, take the absolute value, and divide by the length of the normal. Only the number of coordinates differs: two in the plane and three in space.

## Why each step is valid
- The normal is read from the coefficients because the equation says that $n$ dotted with the point $(x,y)$ or $(x,y,z)$ has a fixed value. Moving along the line or plane does not change that value, so $n$ is perpendicular to every movement inside it.
- Putting $P$ into the left side gives zero exactly when $P$ is on the line. Otherwise it gives a number that grows in proportion to how far $P$ is from the line, measured along $n$.
- That number is $|n|$ times the distance, because moving a distance $d$ along the unit direction $n/|n|$ changes the left side by $|n|\,d$. So dividing by $|n|$ gives the distance $d$.
- The absolute value is used because distance cannot be negative. The sign only tells us on which side of the line or plane the point lies.

## Final answer (in words)
The distance from $P=(2,3)$ to the line $3x+4y-10=0$ is $\frac{8}{5}=1.6$. The distance from $Q=(2,-1,3)$ to the plane $2x-2y+z-4=0$ is $\frac{5}{3}$. Both formulas are the absolute value of the left side at the point, divided by the length of the normal vector, because the shortest segment runs along the normal direction.

## Verification
I check each answer by finding the foot of the perpendicular and measuring the segment directly.

For the line, walk from $P$ along $n=(3,4)$ by the amount $-\frac{8}{25}$ of $n$ (the value $8$ divided by $|n|^2=25$). The foot is
$$F=(2,3)-\frac{8}{25}(3,4)=\left(\frac{26}{25},\frac{43}{25}\right).$$
Put $F$ into the line: $3\cdot\frac{26}{25}+4\cdot\frac{43}{25}-10=\frac{78+172-250}{25}=0$, so $F$ is on the line. The segment from $F$ to $P$ is $\frac{8}{25}(3,4)$, and its length is $\frac{8}{25}\cdot 5=\frac{8}{5}$. This matches.

For the plane, walk from $Q$ along $n=(2,-2,1)$ by $-\frac{5}{9}$ of $n$ (the value $5$ divided by $|n|^2=9$). The foot is
$$F=(2,-1,3)-\frac{5}{9}(2,-2,1)=\left(\frac{8}{9},\frac{1}{9},\frac{22}{9}\right).$$
Put $F$ into the plane: $\frac{16}{9}-\frac{2}{9}+\frac{22}{9}-4=\frac{36}{9}-4=0$, so $F$ is on the plane. The segment from $F$ to $Q$ is $\frac{5}{9}(2,-2,1)$, with length $\frac{5}{9}\cdot 3=\frac{5}{3}$. This matches as well.

## Common mistakes
- Forgetting to divide by $|n|$ and reporting $8$ or $5$ as the distance.
- Dividing by $|n|^2$ instead of $|n|$.
- Dropping the absolute value, or reading the equation with the wrong sign for the constant. The equation must be in the form with $0$ on the right side first.
- Using the wrong sign for a coordinate, for example $-2y$ with $y=-1$ gives $+2$, not $-2$.

## How I would explain it in class
The normal vector is the arrow that stands straight out of the line or plane, and the shortest path from a point always runs along that arrow. We put the point into the left side of the equation to get a number that measures how far we are in units of the normal, and then we divide by the length of the normal to get a real distance. This is why the plane formula is the line formula with one extra coordinate, and the answers are $\frac{8}{5}$ and $\frac{5}{3}$.
