# Problem 13

## The original problem

Given
$$A=(0,0,0),\qquad B=(1,2,0),\qquad C=(0,1,1),\qquad D=(2,5,1).$$

1. Construct $\overrightarrow{AB}$ and $\overrightarrow{AC}$.
2. Find $n=\overrightarrow{AB}\times\overrightarrow{AC}$.
3. Construct $\overrightarrow{AD}$ and check whether $\overrightarrow{AD}\cdot n=0$.
4. Based on this, decide whether $D$ lies in the plane determined by $A,B,C$, and justify the criterion.

## What we are looking for

The points $A$, $B$, $C$ are three points that determine one flat plane. We must decide whether the fourth point $D$ lies in that same plane. We do it by building a vector $n$ that is perpendicular to the plane and testing whether the arrow from $A$ to $D$ is perpendicular to $n$. We must also explain why this test is correct.

## The idea we need

The cross product $n=\overrightarrow{AB}\times\overrightarrow{AC}$ is a vector perpendicular to both arrows, so it stands straight up from the plane through $A$, $B$, $C$. If $D$ is in the plane, the arrow $\overrightarrow{AD}$ lies flat in the plane and makes a right angle with $n$. If $D$ is above or below the plane, the arrow $\overrightarrow{AD}$ leans out of the plane and has a part along $n$, so its dot product with $n$ is not zero. Therefore:
$$D\text{ lies in the plane}\iff \overrightarrow{AD}\cdot n=0,$$
provided $n\neq0$, which means that $A$, $B$, $C$ are not on one line.

## Step-by-step solution

**Step 1: the two arrows.** Since $A$ is the origin, the arrows have the coordinates of the end points.
$$\overrightarrow{AB}=(1,2,0),\qquad \overrightarrow{AC}=(0,1,1).$$

**Step 2: the normal vector.** Using $p\times q=(p_2q_3-p_3q_2,\;p_3q_1-p_1q_3,\;p_1q_2-p_2q_1)$ with $p=(1,2,0)$ and $q=(0,1,1)$:

- First component: $2\cdot1-0\cdot1=2$.
- Second component: $0\cdot0-1\cdot1=-1$.
- Third component: $1\cdot1-2\cdot0=1$.

So
$$n=(2,-1,1).$$
It is not the zero vector, so $A,B,C$ do span a plane.

**Step 3: the arrow to $D$ and the dot product.**
$$\overrightarrow{AD}=(2,5,1),\qquad \overrightarrow{AD}\cdot n=2\cdot2+5\cdot(-1)+1\cdot1=4-5+1=0.$$

**Step 4: the conclusion.** The dot product is $0$, so $\overrightarrow{AD}$ is perpendicular to $n$. Therefore $D$ lies in the plane determined by $A$, $B$, $C$. The four points are coplanar, which means they lie in one plane.

## Why each step is valid

- The plane through $A$ consists of all points $X$ for which the arrow $\overrightarrow{AX}$ is a combination $s\,\overrightarrow{AB}+t\,\overrightarrow{AC}$. Every such arrow is perpendicular to $n$, because $n\cdot(s\,\overrightarrow{AB}+t\,\overrightarrow{AC})=s\cdot0+t\cdot0=0$. This proves one direction of the criterion.
- For the other direction, suppose $\overrightarrow{AD}\cdot n=0$. In space, the vectors perpendicular to a nonzero $n$ form a flat plane through the origin, and $\overrightarrow{AB}$ and $\overrightarrow{AC}$ are two non-parallel members of it. So they span all of it, and $\overrightarrow{AD}$ is a combination of them. That means $D$ is in the plane.
- This is why the test works in both directions. A zero dot product gives coplanar, and a nonzero dot product gives not coplanar.
- Nonzero $n$ is needed. If $n$ were the zero vector, every dot product with it would be $0$, and the test would say nothing.

## Final answer (in words)

The arrows are $\overrightarrow{AB}=(1,2,0)$, $\overrightarrow{AC}=(0,1,1)$ and $\overrightarrow{AD}=(2,5,1)$, and the normal vector is $n=(2,-1,1)$. Since $\overrightarrow{AD}\cdot n=0$, the point $D$ lies in the plane through $A$, $B$, $C$:
$$\overrightarrow{AD}\cdot n=0\quad\Longrightarrow\quad A,B,C,D\text{ are coplanar.}$$

## Verification

I check this in a different way, by writing $\overrightarrow{AD}$ as a combination of the two arrows. Looking at the third component, $(1,2,0)\cdot s+(0,1,1)\cdot t$ has third component $t$, which must equal $1$. The first component gives $s=2$. Then the second component is $2\cdot2+1=5$, and it matches the second component of $\overrightarrow{AD}$. So
$$\overrightarrow{AD}=2\,\overrightarrow{AB}+\overrightarrow{AC}=(2,4,0)+(0,1,1)=(2,5,1),$$
which shows directly that $D$ is in the plane. As further checks, $n\cdot\overrightarrow{AB}=2-2+0=0$ and $n\cdot\overrightarrow{AC}=0-1+1=0$, so $n$ is correct.

## Common mistakes

- Misreading the zero. The zero dot product means that the arrow $\overrightarrow{AD}$ is perpendicular to the normal $n$, which means that it lies flat in the plane. It does not mean that $D$ itself is perpendicular to anything.
- Using a dot product of the points $D\cdot n$ instead of the arrow $\overrightarrow{AD}\cdot n$. These agree here only because $A$ is the origin.
- Taking a nonzero result to mean the points are close to the plane. It only says that $D$ is not in the plane.
- Making an arithmetic error in the middle component of the cross product, such as writing $+1$ instead of $-1$.

## How I would explain it in class

The cross product $n=\overrightarrow{AB}\times\overrightarrow{AC}=(2,-1,1)$ stands straight up from the plane through $A$, $B$, $C$, so an arrow lies flat in that plane exactly when its dot product with $n$ is zero. For $D$ we get $\overrightarrow{AD}\cdot n=4-5+1=0$, so $D$ lies in the plane and the four points are coplanar. A second check agrees: $\overrightarrow{AD}=2\,\overrightarrow{AB}+\overrightarrow{AC}$.
