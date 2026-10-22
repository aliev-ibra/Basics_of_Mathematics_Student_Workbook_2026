# Problem 14

## The original problem

Given a point $P=(4,1)$ and a line through the origin with direction $v=(1,2)$. Using projection, find the closest point on the line, the distance from $P$ to the line, and verify that the appropriate vector is perpendicular to the direction of the line.

## What we are looking for

The line is the set of all points $t\,v=(t,2t)$ for real numbers $t$. We need three things. First, the point $Q$ on this line that is nearest to $P$. Second, the distance from $P$ to the line, which is the distance from $P$ to $Q$. Third, a proof that the vector from $Q$ to $P$ is perpendicular to $v$.

## The idea we need

Think of $P$ as the tip of an arrow from the origin. The shadow of that arrow on the line, when the light falls at a right angle to the line, ends at the closest point of the line. This shadow is the projection of $P$ onto $v$:
$$Q=\frac{P\cdot v}{v\cdot v}\,v.$$
The dot product $P\cdot v$ is a number, and $v\cdot v=\|v\|^2$ is the squared length of $v$. The segment from $Q$ to $P$ is then perpendicular to the line, and a perpendicular segment is the shortest way from a point to a line. Its length is the distance.

## Step-by-step solution

**Step 1: dot products.**
$$P\cdot v=4\cdot1+1\cdot2=6,\qquad v\cdot v=1+4=5.$$

**Step 2: the closest point.**
$$Q=\frac65(1,2)=\left(\frac65,\frac{12}{5}\right).$$

**Step 3: the vector from the closest point to $P$.**
$$r=P-Q=\left(4-\frac65,\;1-\frac{12}{5}\right)=\left(\frac{14}{5},-\frac75\right).$$

**Step 4: the distance.** The distance from $P$ to the line is the length of $r$.
$$\|r\|=\sqrt{\frac{196}{25}+\frac{49}{25}}=\sqrt{\frac{245}{25}}=\sqrt{\frac{49}{5}}=\frac{7}{\sqrt5}=\frac{7\sqrt5}{5}\approx3.130.$$

**Step 5: perpendicularity.**
$$r\cdot v=\frac{14}{5}\cdot1+\left(-\frac75\right)\cdot2=\frac{14}{5}-\frac{14}{5}=0.$$

## Why each step is valid

- The point $Q$ is the projection because we choose the multiple $t\,v$ for which $P-tv$ is perpendicular to $v$. That needs $(P-tv)\cdot v=0$, so $P\cdot v=t\,(v\cdot v)$, which gives $t=\frac65$.
- Why this point is the closest. Take any other point $X=tv$ of the line. The vector $P-X$ is the sum of $r=P-Q$ and $Q-X$. The vector $Q-X$ lies along the line, so it is perpendicular to $r$. By the Pythagorean theorem, $\|P-X\|^2=\|r\|^2+\|Q-X\|^2$, which is larger than $\|r\|^2$ unless $X=Q$. So $Q$ is strictly the closest point.
- Step 5 shows that $r$ is perpendicular to the direction $v$, as the exercise requires. That perpendicularity is the reason for the Pythagorean argument above.

## Final answer (in words)

The closest point of the line to $P$ is
$$Q=\left(\frac65,\frac{12}{5}\right)=\frac65\,v.$$
The distance from $P$ to the line is
$$\|P-Q\|=\frac{7}{\sqrt5}=\frac{7\sqrt5}{5}\approx3.13.$$
The vector $P-Q=\left(\frac{14}{5},-\frac75\right)$ is perpendicular to the direction $v$, because $(P-Q)\cdot v=0$.

## Verification

First, a method that does not use projection. The squared distance from $P$ to the point $tv=(t,2t)$ is
$$(4-t)^2+(1-2t)^2=5t^2-12t+17.$$
This is a parabola in $t$, and its lowest point is at $t=\frac{12}{10}=\frac65$, which is the same multiplier as before. The lowest value is $5\cdot\frac{36}{25}-\frac{72}{5}+17=\frac{36-72+85}{5}=\frac{49}{5}$, and its square root is $\frac{7}{\sqrt5}$, the same distance.

Second, the line has the equation $2x-y=0$, since $(t,2t)$ satisfies it. The standard distance formula gives
$$\frac{|2\cdot4-1\cdot1|}{\sqrt{2^2+(-1)^2}}=\frac{7}{\sqrt5},$$
the same number again. Finally $Q$ is on the line, because $\frac{12}{5}=2\cdot\frac65$.

## Common mistakes

- Giving the projection length instead of the point, or the point instead of the distance.
- Dividing by $\|v\|$ instead of $v\cdot v=\|v\|^2$ in the formula for $Q$, which gives a point of the wrong length.
- Taking the distance to be $\|Q\|$, the length of the shadow. The distance is $\|P-Q\|$, the length of the leftover perpendicular part.
- Forgetting to square-root when computing the length of $r$.

## How I would explain it in class

The closest point of the line to $P=(4,1)$ is the projection $Q=\frac{6}{5}(1,2)=\left(\frac65,\frac{12}{5}\right)$, and the distance is the length of the leftover vector $P-Q=\left(\frac{14}{5},-\frac75\right)$, which is $\frac{7}{\sqrt5}$. The dot product $(P-Q)\cdot v=0$ shows that the leftover vector is at a right angle to the line, and that is what makes $Q$ the closest point. A different method, minimizing $5t^2-12t+17$, gives the same $t=\frac65$ and the same distance.
