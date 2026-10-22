# Problem 15

## The original problem

Given
$$a=(1,2,1),\qquad b=(2,4,2),\qquad c=(2,0,3).$$
For each pair, compute
$$\frac{u\cdot v}{\|u\|\,\|v\|}.$$
Order the pairs by increasing angle between the vectors. Explain why for $a$ and $b$ the value is $1$ even though the vectors have different lengths.

## What we are looking for

There are three pairs of vectors: $(a,b)$, $(a,c)$ and $(b,c)$. For each pair we need the number $\frac{u\cdot v}{\|u\|\,\|v\|}$, which is the cosine of the angle between the two vectors. Then we must list the pairs from the smallest angle to the largest. Finally we must explain why $a$ and $b$ give exactly $1$.

## The idea we need

For two nonzero vectors $u$ and $v$ the dot product satisfies $u\cdot v=\|u\|\,\|v\|\cos\theta$, where $\theta$ is the angle between them. So
$$\cos\theta=\frac{u\cdot v}{\|u\|\,\|v\|}.$$
The length of a vector is $\|w\|=\sqrt{w_1^2+w_2^2+w_3^2}$. Dividing by both lengths turns each vector into an arrow of length $1$, so only the direction is left. For angles between $0^\circ$ and $180^\circ$ the cosine goes down when the angle goes up. Therefore the larger the cosine, the smaller the angle.

## Step-by-step solution

**Step 1: the lengths.**
$$\|a\|=\sqrt{1+4+1}=\sqrt6,\qquad \|b\|=\sqrt{4+16+4}=\sqrt{24}=2\sqrt6,\qquad \|c\|=\sqrt{4+0+9}=\sqrt{13}.$$

**Step 2: the dot products.**
$$a\cdot b=2+8+2=12,\qquad a\cdot c=2+0+3=5,\qquad b\cdot c=4+0+6=10.$$

**Step 3: the three cosines.**

- Pair $(a,b)$: $\dfrac{12}{\sqrt6\cdot2\sqrt6}=\dfrac{12}{12}=1$.
- Pair $(a,c)$: $\dfrac{5}{\sqrt6\cdot\sqrt{13}}=\dfrac{5}{\sqrt{78}}\approx0.566$.
- Pair $(b,c)$: $\dfrac{10}{2\sqrt6\cdot\sqrt{13}}=\dfrac{10}{2\sqrt{78}}=\dfrac{5}{\sqrt{78}}\approx0.566$.

**Step 4: the angles.**

- Pair $(a,b)$: $\cos\theta=1$, so $\theta=0^\circ$.
- Pairs $(a,c)$ and $(b,c)$: $\cos\theta=\frac{5}{\sqrt{78}}$, so $\theta=\arccos\frac{5}{\sqrt{78}}\approx55.5^\circ$.

**Step 5: the order.** Since $1>\frac{5}{\sqrt{78}}$, the angle for $(a,b)$ is the smallest. The other two pairs have equal cosines, so their angles are equal. The order by increasing angle is
$$(a,b)\;<\;(a,c)=(b,c).$$

## Why each step is valid

- Each cosine is the dot product divided by both lengths, exactly as the exercise says.
- The pairs $(a,c)$ and $(b,c)$ give the same value because $b=2a$. Then $b\cdot c=2(a\cdot c)$ and $\|b\|=2\|a\|$, so the factor $2$ cancels between the top and the bottom. The vectors $a$ and $b$ point in the same direction, so each makes the same angle with $c$. A tie is not a mistake, it is what we expect.
- The cosine of an angle decreases from $1$ to $-1$ as the angle grows from $0^\circ$ to $180^\circ$. So comparing cosines compares angles in the opposite order, and the largest cosine means the smallest angle.
- Why the value for $a$ and $b$ is $1$ although the lengths differ. We have $b=2a$, so $b$ is a longer arrow pointing in exactly the same direction as $a$. The formula divides by $\|a\|\,\|b\|$, which removes the lengths completely. What is left is the cosine of the angle, and the angle between two arrows in the same direction is $0^\circ$, whose cosine is $1$. Lengths change the dot product, but the division cancels them. Only the direction matters.

## Final answer (in words)

The three values are
$$\cos(a,b)=1,\qquad \cos(a,c)=\frac{5}{\sqrt{78}}\approx0.566,\qquad \cos(b,c)=\frac{5}{\sqrt{78}}\approx0.566.$$
Ordered by increasing angle, the pair $(a,b)$ comes first with angle $0^\circ$, and then the pairs $(a,c)$ and $(b,c)$ tie with angle about $55.5^\circ$. The value for $a$ and $b$ is $1$ because $b=2a$ has the same direction as $a$, and the formula ignores lengths.

## Verification

First, I check $b=2a$ directly: $2(1,2,1)=(2,4,2)$. Then $a\cdot b=2\|a\|^2=2\cdot6=12$, and $\|a\|\,\|b\|=\sqrt6\cdot2\sqrt6=12$, so the cosine is exactly $1$.

Second, I check the other cosines with a different grouping. Because $b=2a$, the unit vector $\frac{b}{\|b\|}$ equals $\frac{a}{\|a\|}$, so the pairs $(a,c)$ and $(b,c)$ must have the same cosine. They do. The value is $\frac{a}{\|a\|}\cdot\frac{c}{\|c\|}=\frac{5}{\sqrt6\sqrt{13}}$.

Third, the sign of the dot products is positive, $5>0$ and $10>0$, so the angles are sharp, below $90^\circ$. A cosine of $0.566$ lies between $0$ and $1$, which fits an angle between $0^\circ$ and $90^\circ$. A numerical computation gives $\arccos(0.566)\approx55.5^\circ$.

## Common mistakes

- Forgetting to divide by one of the lengths, or dividing by $\|u\|+\|v\|$ instead of the product $\|u\|\,\|v\|$.
- Ordering the pairs by the cosine instead of by the angle. A larger cosine means a smaller angle.
- Expecting the answer for $a$ and $b$ to depend on how long the vectors are.
- Claiming that $(a,c)$ is closer in direction than $(b,c)$, or the other way round, because the dot product $10$ is bigger than $5$. The bigger dot product comes only from the longer vector $b$.

## How I would explain it in class

The cosine $\frac{u\cdot v}{\|u\|\,\|v\|}$ divides out both lengths, so it measures only the angle, and the three values are $1$ for $(a,b)$ and $\frac{5}{\sqrt{78}}\approx0.566$ for both $(a,c)$ and $(b,c)$. A larger cosine means a smaller angle, so the order from smallest angle is $(a,b)$ at $0^\circ$ and then the tie $(a,c)=(b,c)$ at about $55.5^\circ$. The value is $1$ for $a$ and $b$ because $b=2a$ is just a longer arrow in the same direction, and the lengths cancel in the division.
