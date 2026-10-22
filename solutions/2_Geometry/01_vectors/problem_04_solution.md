# Problem 04

## The original problem
For $u=(1,2,-1)$ and $v=(2,-1,3)$ compute $u\cdot v$ and determine whether the vectors are perpendicular. Then find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$, and check the result.

## What we are looking for
We need the dot product $u\cdot v$ in $\mathbb{R}^3$, the perpendicularity test (dot product zero), the value of $a$ making $w\perp u$, and an independent check of that condition.

## The idea we need
The standard dot product in $\mathbb{R}^n$ is
$$
u\cdot v = \sum_{i=1}^{n} u_i v_i = u_1 v_1 + u_2 v_2 + u_3 v_3 \quad (n=3).
$$
A key geometric fact (Euclidean): for nonzero vectors, $u\perp v \iff u\cdot v = 0$. Also equivalently $u\cdot v = \|u\|\|v\|\cos\theta$. So the dot product is both a computational tool and a test for perpendicularity.  
Conditions: this is the standard Euclidean dot product in Cartesian coordinates.

## Step-by-step solution

1. **Compute $u\cdot v$:**
   $u\cdot v = 1\cdot 2 + 2\cdot (-1) + (-1)\cdot 3 = 2 - 2 - 3 = -3$.
   (Multiply corresponding components and sum.)

2. **Determine perpendicularity:**
   Since $u\cdot v = -3 \neq 0$, the vectors $u$ and $v$ are not perpendicular.
   (Perpendicularity in the Euclidean sense requires dot product exactly 0 for the direction test.)

3. **Find $a$ so that $w=(2,-1,a)$ is perpendicular to $u$:**
   Perpendicular to $u=(1,2,-1)$ means $w\cdot u = 0$.
   Compute $w\cdot u = 2\cdot 1 + (-1)\cdot 2 + a\cdot (-1) = 2 - 2 - a = -a$.
   Set to zero: $-a = 0 \implies a = 0$.
   Thus $w=(2,-1,0)$ when perpendicular to $u$.

4. **Check the result:**
   With $a=0$, $w=(2,-1,0)$, $w\cdot u = 2 - 2 + 0 = 0$. OK, exactly zero.

## Why each step is valid

- **Dot product formula:** defined componentwise in Cartesian $\mathbb{R}^3$.
- **Perp test:** in Euclidean geometry, two nonzero vectors are orthogonal iff their dot product is 0 (this follows from the law of cosines: $u\cdot v=\|u\|\|v\|\cos\theta$).
- **Condition:** $w\perp u \iff w\cdot u=0$; we treat this as an equation in $a$.
- **Check:** recomputing the dot product with the found $a$ is an independent verification.

## Final answer (in words)
In plain words: $u\cdot v = -3 \neq 0$, so $u$ and $v$ are not perpendicular. To have $w=(2,-1,a)$ perpendicular to $u$, the combination gives $-a=0$ so $a$ must be 0, making $w=(2,-1,0)$ and their dot product zero.  
In symbols: $u\cdot v = -3$, not perpendicular; $w\cdot u = -a = 0 \implies a=0,\ w=(2,-1,0),\ w\cdot u=0$.

## Verification
Recomputed $u\cdot v$: $1*2=2, 2*(-1)=-2, (-1)*3=-3$, sum $2-2-3=-3$ OK. For $w$: $2*1 + (-1)*2 + a*(-1)=2-2-a=-a$ OK. Setting to 0 gives $a=0$, check gives 0 OK.

## Common mistakes
- **Arithmetic sign errors:** especially the last term $(-1)\cdot 3 = -3$.
- **Assuming perpendicular by eye:** must use dot product.
- **Solving equation:** writing $w\cdot u = -a = 0 \implies a=0$ (not $a=- ?$).
- **Forgetting the check:** the problem says "and check the result", so verification is required.

## How I would explain it in class
The dot product gives a single number we can test for perpendicularity: zero means orthogonal in the Euclidean sense.  
Here $u\cdot v = -3$, so they are not at right angles.  
To force perpendicularity between $w$ and $u$, we set $w\cdot u = -a = 0$ and get $a=0$, and we quickly verify that the dot product is indeed zero.
