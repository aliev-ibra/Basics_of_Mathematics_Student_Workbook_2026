# Problem 15

## The original problem

For the function
$$f(x)=x^3-3x$$
the derivative was correctly computed as
$$f'(x)=3(x-1)(x+1).$$

However, a student wrote the following conclusion:

> The derivative is positive between its zeros and negative outside them. Therefore, the function is decreasing on $(-\infty,-1)\cup(1,\infty)$, increasing on $(-1,1)$, has a local minimum at $x=-1$, and a local maximum at $x=1$.

1. Without differentiating again, explain why merely identifying the zeros of the derivative does not justify the stated sign chart, and find the error in the student's reasoning.
2. Construct the correct sign chart for $f'(x)$.
3. Give the correct intervals of monotonicity and the character of the extrema.
4. In each of the three intervals, choose one simple test point and show that the sign of the derivative confirms your classification.

> **Why this problem:** it teaches how to diagnose an error in a completed argument and shows that a correct derivative formula is not enough if its sign is interpreted incorrectly.

## What we are looking for

We must find exactly where the student's argument goes wrong, then redo the monotonicity analysis correctly. That means a correct table of signs of $f'$, the correct intervals where $f$ rises and falls, the correct type of each extremum, and one test point in each interval as proof.

## The idea we need

The zeros of the derivative are only the places where the sign can change. They split the number line into pieces. They do not say which piece is positive and which is negative. To know the sign on a piece, we must either compute the derivative at one test point in that piece, or read the sign from the shape of the formula (for example, a parabola opening upward is negative between its zeros and positive outside them). Then: if $f'>0$ the function is increasing, if $f'<0$ it is decreasing. A sign change from plus to minus gives a local maximum, and from minus to plus a local minimum.

## Step-by-step solution

1. Part 1: the error. The student found the zeros $x=-1$ and $x=1$ correctly, and the derivative formula was correct. The error is in the sign chart: the student assumed a sign pattern ("positive between the zeros, negative outside") without testing it. The pattern is reversed. The derivative $3(x-1)(x+1)=3x^2-3$ is a parabola whose leading coefficient $3$ is positive, so it opens upward. An upward parabola is negative between its zeros and positive outside them. So the true pattern is exactly the opposite of the student's claim. A second warning sign: the sign of a product of two factors is plus when both factors have the same sign. For very large $x$, both $(x-1)$ and $(x+1)$ are positive, so $f'$ is positive on the right, not negative. Because the student's sign chart is wrong, all the later conclusions (monotonicity and the type of both extrema) are wrong as well, even though they follow consistently from it.

2. Part 2: the correct sign chart. The zeros $x=-1$ and $x=1$ give three intervals. The factor $3$ is always positive, so we track the signs of $(x-1)$ and $(x+1)$.

| Interval | Test point | $x-1$ | $x+1$ | $3(x-1)(x+1)$ | Sign of $f'$ |
|---|---|---|---|---|---|
| $(-\infty,-1)$ | $x=-2$ | $-3$ | $-1$ | $3\cdot(-3)(-1)=9$ | $+$ |
| $(-1,1)$ | $x=0$ | $-1$ | $1$ | $3\cdot(-1)(1)=-3$ | $-$ |
| $(1,\infty)$ | $x=2$ | $1$ | $3$ | $3\cdot(1)(3)=9$ | $+$ |

3. Part 3: the conclusions.
   - $f'>0$ on $(-\infty,-1)$, so $f$ is increasing there.
   - $f'<0$ on $(-1,1)$, so $f$ is decreasing there.
   - $f'>0$ on $(1,\infty)$, so $f$ is increasing there.
   - At $x=-1$ the sign changes from plus to minus: local maximum, with value $f(-1)=-1+3=2$.
   - At $x=1$ the sign changes from minus to plus: local minimum, with value $f(1)=1-3=-2$.

   Compared to the student: the intervals of increase and decrease are swapped, and so are the maximum and the minimum. The student also wrote one decreasing statement over the union $(-\infty,-1)\cup(1,\infty)$. Even in the wrong chart, monotonicity should be stated on each interval separately. The two pieces are not one interval, and a function cannot be called monotone across the gap between them.

4. Part 4: confirmation with test points. One test point per interval:
   - $x=-2$ in $(-\infty,-1)$: $f'(-2)=3(-3)(-1)=9>0$, so increasing.
   - $x=0$ in $(-1,1)$: $f'(0)=3(-1)(1)=-3<0$, so decreasing.
   - $x=2$ in $(1,\infty)$: $f'(2)=3(1)(3)=9>0$, so increasing.

   A graph description: coming from the lower left, the curve rises through $(-\sqrt3,0)$ to the peak $(-1,2)$, falls through the origin to the valley $(1,-2)$, then rises through $(\sqrt3,0)$ to the upper right.

## Why each step is valid

- A continuous function can change sign only by passing through zero, so the zeros of $f'$ are the only possible boundaries between sign regions.
- Inside each region the sign is constant, so a single test point decides the whole interval. This is the reason the test is valid, and it is also the reason the student could not skip it.
- The rule "positive derivative means increasing" comes from the derivative being the slope of the graph.
- The extremum type follows from the direction of the sign change, not from the zeros alone.

## Final answer (in words)

The student's error is that the sign pattern was assumed instead of tested, and it is backwards: $f'(x)=3(x^2-1)$ is an upward parabola, so it is positive outside the zeros and negative between them. The correct result is: $f'>0$ on $(-\infty,-1)$ and on $(1,\infty)$, and $f'<0$ on $(-1,1)$. So $f$ is increasing on $(-\infty,-1)$, decreasing on $(-1,1)$, and increasing on $(1,\infty)$. There is a local maximum at $x=-1$ with value $2$, and a local minimum at $x=1$ with value $-2$.

## Verification

Directly from the function values, without using the derivative: $f(-2)=-8+6=-2$, $f(-1)=2$, $f(0)=0$, $f(1)=-2$, $f(2)=2$. Going from $x=-2$ to $x=-1$ the value rises from $-2$ to $2$, so the function increases there. From $x=-1$ to $x=1$ the value falls from $2$ to $-2$, so it decreases. From $x=1$ to $x=2$ it rises from $-2$ to $2$. This matches the correct chart and contradicts the student's chart. For example, the student claims $f$ decreases on $(1,\infty)$, but $f(1)=-2<f(2)=2$.

The second derivative gives the same extremum types: $f''(x)=6x$, so $f''(-1)=-6<0$ (local maximum) and $f''(1)=6>0$ (local minimum). A computer algebra check (sympy) gave the same derivative factorization and the same values.

## Common mistakes

- Treating the zeros of the derivative as if they already give the signs.
- Memorizing "positive between the zeros", which is true for a downward parabola but not for an upward one.
- Mixing up the words: the sign of $f'$ is about the slope, not about whether $f$ itself is positive.
- Writing a monotonicity statement over a union of intervals as if it were one interval.

## How I would explain it in class

The student found the right zeros $-1$ and $1$ but then guessed the signs, and the guess was backwards, because $3(x^2-1)$ is an upward parabola that is positive outside the zeros and negative between them. Testing $x=-2$, $x=0$, and $x=2$ gives $9$, $-3$, and $9$, so the function increases, then decreases, then increases. That means the peak is at $x=-1$ with value $2$ and the valley is at $x=1$ with value $-2$, the opposite of what the student wrote.
