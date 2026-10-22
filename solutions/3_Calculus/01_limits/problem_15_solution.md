# Problem 15

## The original problem
Choose one sequence and one function from this set. For the sequence, compute several values for increasingly large $n$. For the function, prepare a table of values with arguments approaching the limit point from the left and right. Sketch the behavior of both objects.

Compare the observation with the analytical result and explain why a finite number of calculations or a sketch does not constitute a proof that the limit exists.

## What we are looking for
We must pick one sequence and one function from the earlier exercises, and produce two tables of real values. We choose the sequence $a_n=\left(1+\frac1n\right)^n$ from Exercise 5 and the function $f(x)=\frac{x^2-4x+3}{x-3}$ from Exercise 7, whose limit point is $x=3$. We then compare what the tables suggest with the exact answers, and explain in words why tables and sketches are not proofs.

## The idea we need
Observation and proof are two different things. A table of values is observation: it shows what happens for the numbers we tried. A proof is an argument that covers all the numbers, including those we never tried. For a sequence, the limit statement is about every large $n$. For a function, the limit statement is about every $x$ close to the point, from both sides. Finite lists cannot cover infinitely many cases.

## Step-by-step solution
**Part A: the sequence $a_n=\left(1+\frac1n\right)^n$.**

1. Compute the terms (rounded to nine decimal places or fewer):

| $n$ | $a_n$ |
|---|---|
| $1$ | $2$ |
| $2$ | $2.25$ |
| $5$ | $2.48832$ |
| $10$ | $2.593742460$ |
| $100$ | $2.704813829$ |
| $1000$ | $2.716923932$ |
| $10000$ | $2.718145927$ |
| $100000$ | $2.718268237$ |
| $1000000$ | $2.718280469$ |

2. The terms increase and slow down. The number $e=2.718281828\ldots$ is above all of them, and the gap shrinks roughly by a factor of $10$ each time $n$ grows by a factor of $10$.
3. The sketch: plot the points $(n,a_n)$. They climb steeply at first, then flatten, and approach the horizontal line $y=e$ from below without touching it.

**Part B: the function $f(x)=\frac{x^2-4x+3}{x-3}$ near $x=3$.**

4. Note that $f(3)$ is not defined, because the denominator is $0$. Compute values on both sides:

| $x$ (left) | $f(x)$ | $x$ (right) | $f(x)$ |
|---|---|---|---|
| $2.9$ | $1.9$ | $3.1$ | $2.1$ |
| $2.99$ | $1.99$ | $3.01$ | $2.01$ |
| $2.999$ | $1.999$ | $3.001$ | $2.001$ |
| $2.9999$ | $1.9999$ | $3.0001$ | $2.0001$ |

5. Both sides approach $2$. The sketch: the graph is the straight line $y=x-1$, with one open circle (a hole) at the point $(3,2)$, because the value at $3$ is missing.

**Part C: comparison with the exact results.**

6. For the function, factor the top: $x^2-4x+3=(x-1)(x-3)$. For $x\neq3$ we cancel $x-3$ and get $f(x)=x-1$. So $\lim_{x\to3}f(x)=3-1=2$. This matches the table.
7. For the sequence, the exact limit is $e\approx2.718281828$, proved in Exercise 5 by an argument that the sequence is increasing and bounded above. This matches the trend in the table.

**Part D: why observation is not proof.**

8. The tables only contain finitely many values. The limit statement speaks about infinitely many values of $n$, or of $x$. A trend that holds for the first million terms can still change later.
9. Here is a real example. Take the sequence $b_n=\frac{n^2}{n^2+10^6}$. Its values are $b_{10}=0.0001$, $b_{100}\approx0.0099$, $b_{1000}=0.5$, $b_{10000}\approx0.9901$, $b_{1000000}\approx0.999999$. If we looked only at $n\le100$, we would guess that the limit is $0$. The true limit is $1$.
10. A sketch has the same weakness. A drawn curve has limited accuracy and a limited window, and a tiny hole or a distant jump cannot be seen. Only an argument with algebra, inequalities, or a theorem covers every case.

## Why each step is valid
Steps 1 to 5 are direct computations, so they are exact or correctly rounded. Step 6 is valid because $\frac{x-3}{x-3}=1$ for $x\neq3$, and the limit only uses $x\neq3$. Step 7 relies on the theorem proved in Exercise 5. Steps 8 to 10 state a logical point: a statement about all numbers cannot be proved by checking some of them, but it can be disproved by a single counterexample, as the example $b_n$ shows that early values can mislead.

## Final answer (in words)
The table for the sequence suggests the limit $e\approx2.71828$, and the proof in Exercise 5 confirms it. The table for the function suggests the limit $2$ at $x=3$, and the algebra $f(x)=x-1$ for $x\neq3$ confirms it. In both cases the tables only suggest the answer, and the proof is the algebraic or theoretical argument that works for all values.

## Verification
Check the function by a second method: since $f(x)=x-1$ for every $x\neq3$, the value $f(3.0001)=2.0001$ and $f(2.9999)=1.9999$ in the table are exactly what the formula gives. Check the sequence by the error column: $e-a_n$ equals $0.718$ at $n=1$, $0.1245$ at $n=10$, $0.01347$ at $n=100$, $0.001358$ at $n=1000$, and $0.000001359$ at $n=1000000$. The error is about $\frac{1.36}{n}$ for large $n$, which is consistent with a limit equal to $e$. The sequence $b_n$ checks the main claim: the early values suggested $0$, but the exact formula gives $\frac{1}{1+10^6/n^2}\to1$.

## Common mistakes
- Treating the table as a proof, or saying that "the pattern is clear" instead of giving an argument.
- Thinking that the missing value $f(3)$ means the limit does not exist. The limit only depends on the nearby values.
- Stating the limit of the sequence as the last value in the table, for example $2.718280469$, instead of the exact number $e$.

## How I would explain it in class
I computed real tables for the sequence $\left(1+\frac1n\right)^n$ and for the function $\frac{x^2-4x+3}{x-3}$ near $3$, and they point to $e$ and to $2$. Then I confirmed both with exact arguments, the theorem from Exercise 5 and the cancellation $f(x)=x-1$. A table can only suggest an answer, because it checks finitely many numbers, and only a proof covers all of them.
