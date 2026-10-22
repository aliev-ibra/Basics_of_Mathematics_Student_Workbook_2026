# Problem 04

## The original problem
Analyze
$$\left(\frac23\right)^n,\qquad \left(\frac32\right)^n,\qquad (-1)^n,\qquad \frac{(-1)^n}{n}.$$
For each sequence, describe the type of behavior and justify your answer.

## What we are looking for
For each of the four sequences, we need to say what happens as $n$ grows without bound: does it converge to a finite number, diverge to infinity, or oscillate without settling down? We also need to justify each answer.

## The idea we need
A geometric sequence $r^n$ behaves according to the size of the base $r$: if $|r|<1$, then $r^n\to 0$; if $r>1$, then $r^n\to+\infty$; if $r=-1$, the sequence alternates between $1$ and $-1$ and does not converge. For a sequence of the form $\frac{(-1)^n}{n}$, the numerator stays bounded (it is always $1$ or $-1$) while the denominator grows without bound, so the whole fraction tends to $0$ by the squeeze idea: an oscillating but bounded numerator divided by a growing denominator still goes to $0$.

## Step-by-step solution
Sequence 1: $\left(\frac23\right)^n$.
1. The base is $r=\frac23$, and $|r|=\frac23<1$.
2. A geometric sequence with base whose absolute value is less than $1$ tends to $0$. Therefore
$$\lim_{n\to\infty}\left(\frac23\right)^n=0.$$
The sequence converges to $0$.

Sequence 2: $\left(\frac32\right)^n$.
3. The base is $r=\frac32$, and $r>1$.
4. A geometric sequence with base greater than $1$ grows without bound. Therefore
$$\lim_{n\to\infty}\left(\frac32\right)^n=+\infty.$$
The sequence diverges to $+\infty$.

Sequence 3: $(-1)^n$.
5. The terms alternate: for even $n$ the term is $1$, and for odd $n$ the term is $-1$.
6. The sequence does not approach any single value, because it keeps jumping between $1$ and $-1$. Therefore the limit does not exist; the sequence diverges by oscillation.

Sequence 4: $\frac{(-1)^n}{n}$.
7. The numerator $(-1)^n$ is bounded: it is always either $1$ or $-1$, so $|(-1)^n|\le 1$.
8. The denominator $n$ grows without bound. Hence
$$0\le \left|\frac{(-1)^n}{n}\right|=\frac{1}{n}\to 0\quad\text{as }n\to\infty.$$
9. Since the absolute value tends to $0$, the sequence itself tends to $0$:
$$\lim_{n\to\infty}\frac{(-1)^n}{n}=0.$$
The sequence converges to $0$, even though its terms alternate in sign.

## Why each step is valid
Steps 2 and 4 use the standard behavior of geometric sequences: powers of a number with absolute value less than $1$ shrink to $0$, while powers of a number greater than $1$ grow without bound.
Step 6 is justified by the definition of convergence: a convergent sequence must eventually stay arbitrarily close to one number, which $(-1)^n$ does not.
Step 8 uses the fact that $\frac{1}{n}\to 0$ as $n\to\infty$, and step 9 uses the rule that if $|a_n|\to 0$ then $a_n\to 0$.

## Final answer (in words)
The sequence $(2/3)^n$ converges to $0$ because its base is smaller than $1$ in absolute value. The sequence $(3/2)^n$ diverges to $+\infty$ because its base is greater than $1$. The sequence $(-1)^n$ diverges by oscillation between $1$ and $-1$ and has no limit. The sequence $(-1)^n/n$ converges to $0$ because a bounded oscillating numerator divided by a growing denominator still shrinks to zero.

## Verification
For $(2/3)^n$ at $n=20$: $(2/3)^{20}\approx 0.0003$, close to $0$. For $(3/2)^n$ at $n=20$: $(3/2)^{20}\approx 3325$, large and positive, consistent with divergence to $+\infty$. For $(-1)^n$: at $n=10$ the value is $1$ and at $n=11$ it is $-1$, confirming oscillation with no limit. For $(-1)^n/n$ at $n=1000$: the value is $\frac{1}{1000}=0.001$ (even $n$) or $-\frac{1}{1000}=-0.001$ (odd $n$), both close to $0$. These numerical checks support the conclusions.

## Common mistakes
- Saying $(-1)^n$ converges to $0$ or to $1$ just because the terms are bounded.
- Treating $(-1)^n/n$ as divergent because the numerator oscillates, ignoring that the denominator damps the oscillation.
- Forgetting that a geometric sequence with base greater than $1$ diverges rather than approaching a finite limit.

## How I would explain it in class
If the base is smaller than one in absolute value, multiplying it over and over makes the terms shrink to zero. If the base is bigger than one, the terms explode; if the base is exactly minus one, the sequence just bounces back and forth forever and never settles. And if you have that bouncing divided by a growing number, the bounce gets smaller and smaller until it disappears at zero.
