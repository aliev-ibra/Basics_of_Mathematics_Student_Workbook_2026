# Problem 12

## The original problem

Given $A=(1,0,2)$, $B=(2,1,0)$, and $C=(0,3,1)$. Construct two vectors lying in the plane, find a vector perpendicular to both, and check the perpendicularity using dot products.

## What we are looking for

Three points that are not on one line determine exactly one plane. We need two arrows that lie inside this plane. Then we need a vector $n$ that is perpendicular to both arrows. Such a vector is perpendicular to the whole plane, and it is called a normal vector of the plane.

## The idea we need

An arrow drawn from one of the three points to another lies in the plane. The cross product $p\times q$ of two arrows $p$ and $q$ is a vector perpendicular to both of them. If $p$ and $q$ are not parallel, they span the plane, so their cross product sticks straight out of the plane. The coordinate formula is
$$p\times q=(p_2q_3-p_3q_2,\;\;p_3q_1-p_1q_3,\;\;p_1q_2-p_2q_1).$$
Two vectors are perpendicular exactly when their dot product is $0$.

## Step-by-step solution

**Step 1: two vectors in the plane.** An arrow from $A$ to another point is the end point minus $A$.
$$\overrightarrow{AB}=B-A=(2-1,\;1-0,\;0-2)=(1,1,-2),$$
$$\overrightarrow{AC}=C-A=(0-1,\;3-0,\;1-2)=(-1,3,-1).$$

**Step 2: the normal vector.** Take $p=\overrightarrow{AB}=(1,1,-2)$ and $q=\overrightarrow{AC}=(-1,3,-1)$.

- First component: $p_2q_3-p_3q_2=1\cdot(-1)-(-2)\cdot3=-1+6=5$.
- Second component: $p_3q_1-p_1q_3=(-2)\cdot(-1)-1\cdot(-1)=2+1=3$.
- Third component: $p_1q_2-p_2q_1=1\cdot3-1\cdot(-1)=3+1=4$.

So
$$n=\overrightarrow{AB}\times\overrightarrow{AC}=(5,3,4).$$

**Step 3: check perpendicularity to the first arrow.**
$$n\cdot\overrightarrow{AB}=5\cdot1+3\cdot1+4\cdot(-2)=5+3-8=0.$$

**Step 4: check perpendicularity to the second arrow.**
$$n\cdot\overrightarrow{AC}=5\cdot(-1)+3\cdot3+4\cdot(-1)=-5+9-4=0.$$

## Why each step is valid

- The arrows $\overrightarrow{AB}$ and $\overrightarrow{AC}$ join points of the plane, so they lie in it. They are not parallel, because no number $k$ satisfies $(1,1,-2)=k(-1,3,-1)$: the first components force $k=-1$ and the second components force $k=\frac13$. So they span the plane and are not just two arrows on one line.
- The cross product is perpendicular to both of its factors. Steps 3 and 4 prove this for our numbers, since a zero dot product means a right angle.
- A vector perpendicular to two arrows that span the plane is perpendicular to every arrow in the plane, because every such arrow is a combination $s\,\overrightarrow{AB}+t\,\overrightarrow{AC}$, and $n\cdot(s\,\overrightarrow{AB}+t\,\overrightarrow{AC})=s\cdot0+t\cdot0=0$. So $n$ is a normal vector of the plane.
- The vector $n\neq(0,0,0)$, which confirms that the three points are not on one line.

## Final answer (in words)

Two vectors in the plane are $\overrightarrow{AB}=(1,1,-2)$ and $\overrightarrow{AC}=(-1,3,-1)$. A vector perpendicular to both, and therefore to the whole plane, is
$$n=(5,3,4).$$
Any nonzero multiple of $n$ also works, for example $-n=(-5,-3,-4)$.

## Verification

The two dot products in Steps 3 and 4 are the check requested. I add two more checks that use a third arrow, $\overrightarrow{BC}=C-B=(-2,2,1)$. It also lies in the plane, so it must be perpendicular to $n$:
$$n\cdot\overrightarrow{BC}=5\cdot(-2)+3\cdot2+4\cdot1=-10+6+4=0.$$
The length of $n$ must be twice the triangle area, which equals the parallelogram area. We get $\|n\|=\sqrt{25+9+16}=\sqrt{50}$. Using lengths and the dot product instead, $\|\overrightarrow{AB}\|^2=6$, $\|\overrightarrow{AC}\|^2=11$ and $\overrightarrow{AB}\cdot\overrightarrow{AC}=-1+3+2=4$, so $\sqrt{6\cdot11-4^2}=\sqrt{50}$. The two values agree.

## Common mistakes

- Making a sign error with the negative entries, for example in $1\cdot(-1)-(-2)\cdot3$, where minus times minus is plus.
- Subtracting in the wrong direction, so that an arrow is $A-B$ instead of $B-A$. The arrow still lies in the plane, but the normal vector changes its sign, so the numbers differ from the ones above.
- Checking perpendicularity against only one arrow.
- Thinking that the normal vector is unique. Every nonzero multiple of $n$ is also a normal vector.

## How I would explain it in class

The arrows $\overrightarrow{AB}=(1,1,-2)$ and $\overrightarrow{AC}=(-1,3,-1)$ lie in the plane, and their cross product $n=(5,3,4)$ points straight out of the plane. The dot products $n\cdot\overrightarrow{AB}=0$ and $n\cdot\overrightarrow{AC}=0$ prove that it is perpendicular to both arrows, hence to every arrow in the plane. The third arrow $\overrightarrow{BC}$ is also perpendicular to $n$, which is a check that I did not use when I built $n$.
