# Problem 09

## The original problem

For $u=(1,2,0)$ and $v=(0,1,3)$ compute $u\times v$. Use dot products to check perpendicularity to both vectors, compute $v\times u$, and compare the results.

## What we are looking for

We need a new vector $u\times v$ called the cross product. It is a vector in space that is perpendicular to both $u$ and $v$. We must prove the perpendicularity with two dot products, then compute $v\times u$ and say how it differs from $u\times v$.

## The idea we need

The cross product of two vectors in space is a third vector with three properties. It is perpendicular to both of them, so it points straight out of the flat sheet that $u$ and $v$ span. Its length equals the area of the parallelogram built on $u$ and $v$. Its direction is chosen by the right-hand rule: curl the fingers of the right hand from $u$ towards $v$, and the thumb shows the direction.

For $u=(u_1,u_2,u_3)$ and $v=(v_1,v_2,v_3)$ the coordinate formula is
$$u\times v=(u_2v_3-u_3v_2,\;\;u_3v_1-u_1v_3,\;\;u_1v_2-u_2v_1).$$
The dot product $a\cdot b=a_1b_1+a_2b_2+a_3b_3$ is a number. Two nonzero vectors are perpendicular exactly when their dot product is $0$.

## Step-by-step solution

**Step 1: compute $u\times v$.** Here $u_1=1,\ u_2=2,\ u_3=0$ and $v_1=0,\ v_2=1,\ v_3=3$.

- First component: $u_2v_3-u_3v_2=2\cdot3-0\cdot1=6$.
- Second component: $u_3v_1-u_1v_3=0\cdot0-1\cdot3=-3$.
- Third component: $u_1v_2-u_2v_1=1\cdot1-2\cdot0=1$.

So
$$u\times v=(6,-3,1).$$

**Step 2: check perpendicularity to $u$.**
$$(u\times v)\cdot u=6\cdot1+(-3)\cdot2+1\cdot0=6-6+0=0.$$

**Step 3: check perpendicularity to $v$.**
$$(u\times v)\cdot v=6\cdot0+(-3)\cdot1+1\cdot3=0-3+3=0.$$

**Step 4: compute $v\times u$.** Now the first vector is $v$ and the second is $u$, so we swap the roles in the formula.

- First component: $v_2u_3-v_3u_2=1\cdot0-3\cdot2=-6$.
- Second component: $v_3u_1-v_1u_3=3\cdot1-0\cdot0=3$.
- Third component: $v_1u_2-v_2u_1=0\cdot2-1\cdot1=-1$.

So
$$v\times u=(-6,3,-1).$$

**Step 5: compare.** Every component of $v\times u$ is the opposite of the matching component of $u\times v$. Therefore
$$v\times u=-(u\times v).$$

## Why each step is valid

- The formula in Step 1 is the definition of the cross product in coordinates, so we only have to substitute numbers carefully.
- A zero dot product means the angle between the two vectors is $90^\circ$. Steps 2 and 3 therefore prove that $(6,-3,1)$ is perpendicular to $u$ and also to $v$.
- In Step 4 we use the same formula with the two vectors exchanged. Each component of the formula is a difference of two products, and exchanging the vectors exchanges the two products in every difference. That reverses every sign, which is exactly what Step 5 observed.
- Geometrically the sheet spanned by $u$ and $v$ is the same sheet in both cases, so both answers are perpendicular to it. The only choice is which of the two sides of the sheet the arrow points to, and the right-hand rule gives opposite sides when the order is reversed.

## Final answer (in words)

The cross product is $u\times v=(6,-3,1)$. It is perpendicular to both $u$ and $v$, because both dot products are $0$. Reversing the order gives $v\times u=(-6,3,-1)$, which is the same vector pointing the opposite way:
$$u\times v=(6,-3,1),\qquad v\times u=(-6,3,-1)=-(u\times v).$$

## Verification

The dot products above already check the direction. To check the length independently I use the identity
$$\|u\times v\|^2=\|u\|^2\|v\|^2-(u\cdot v)^2.$$
We have $\|u\|^2=1+4+0=5$, $\|v\|^2=0+1+9=10$ and $u\cdot v=0+2+0=2$. So the right side is $5\cdot10-2^2=46$. The left side is $6^2+(-3)^2+1^2=36+9+1=46$. The two numbers agree, so the components are correct.

As a last check, $(v\times u)\cdot u=-6+6+0=0$ and $(v\times u)\cdot v=0+3-3=0$, so the reversed vector is perpendicular to both as well.

## Common mistakes

- Using the wrong sign in the middle component. It is $u_3v_1-u_1v_3$, not $u_1v_3-u_3v_1$.
- Believing that $u\times v=v\times u$. The cross product changes sign when the order changes.
- Confusing the dot product, which is a number, with the cross product, which is a vector.
- Checking perpendicularity against only one of the two vectors.

## How I would explain it in class

The cross product $u\times v=(6,-3,1)$ is a vector that sticks straight out of the sheet containing $u$ and $v$, and the dot products $(u\times v)\cdot u=0$ and $(u\times v)\cdot v=0$ prove it. Swapping the order gives $v\times u=(-6,3,-1)$, the same arrow pointing to the other side of the sheet, so the cross product changes sign when the order changes. The length check $\|u\times v\|^2=46=5\cdot10-2^2$ confirms the numbers independently.
