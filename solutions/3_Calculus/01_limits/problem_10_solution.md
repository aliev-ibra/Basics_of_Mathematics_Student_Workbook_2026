# Problem 10

## The original problem
Find $a$ so that
$$f(x)=\begin{cases}ax+1,&x<2,\\x^2-1,&x\ge2\end{cases}$$
is continuous at $x=2$. Explicitly compare the left-hand limit, right-hand limit, and function value.

## What we are looking for
We need the number $a$ that makes the graph of $f$ have no jump or hole at $x=2$. We must also write down three numbers: the left-hand limit at $2$, the right-hand limit at $2$, and the value $f(2)$, and show that they are all equal.

## The idea we need
A function $f$ is continuous at a point $c$ when three things hold. First, $f(c)$ is defined. Second, the limit of $f(x)$ as $x\to c$ exists. Third, that limit is equal to $f(c)$. For a function defined by two formulas that meet at $c$, the limit exists exactly when the left-hand limit and the right-hand limit are equal. So continuity means: left-hand limit $=$ right-hand limit $=$ function value.

## Step-by-step solution
1. Function value. The point $x=2$ belongs to the second line, because that line says $x\ge2$. So
$$f(2)=2^2-1=3.$$
2. Left-hand limit. For $x<2$ the function equals $ax+1$. This is a polynomial, so we may put in $x=2$:
$$\lim_{x\to2^-}f(x)=2a+1.$$
3. Right-hand limit. For $x>2$ the function equals $x^2-1$, again a polynomial:
$$\lim_{x\to2^+}f(x)=2^2-1=3.$$
4. Continuity requires the three numbers to be equal:
$$2a+1=3=3.$$
5. Solve the equation $2a+1=3$. Subtract $1$ from both sides to get $2a=2$, and divide by $2$ to get
$$a=1.$$
6. Final comparison for $a=1$: left-hand limit $=3$, right-hand limit $=3$, and $f(2)=3$. All three agree.

## Why each step is valid
Step 1 is valid because the inequality $x\ge2$ includes $x=2$, so the second formula is used there. Steps 2 and 3 are valid because polynomials are continuous everywhere, so the limit of a polynomial at a point is its value at that point; also the limit as $x\to2^-$ only looks at numbers less than $2$, where the first formula applies, and the limit as $x\to2^+$ only looks at numbers greater than $2$, where the second formula applies. Step 4 is valid by the definition of continuity. Step 5 is a simple linear equation, and it has exactly one solution, so no other value of $a$ works.

## Final answer (in words)
The function is continuous at $x=2$ exactly when $a=1$. For that value the left-hand limit is $3$, the right-hand limit is $3$, and the function value $f(2)$ is $3$, so all three quantities are equal.

## Verification
Take $a=1$, so the left piece is $x+1$. Check values near $2$. On the left: $f(1.9)=2.9$, $f(1.99)=2.99$, $f(1.999)=2.999$. On the right: $f(2.001)=2.001^2-1=3.004001$, $f(2.01)=3.0401$, $f(2.1)=3.41$. Both sides approach $3$, which is also $f(2)$. As a different check, try a wrong value, for example $a=2$. Then the left limit is $2\cdot2+1=5$, while the right limit and the value are $3$. The graph would jump by $2$ at $x=2$, so the function would not be continuous. This confirms that only $a=1$ works.

## Common mistakes
- Comparing only the two one-sided limits and forgetting the function value $f(2)$.
- Using the wrong formula for $f(2)$, that is, substituting $2$ into $ax+1$ instead of $x^2-1$.
- Making an arithmetic error such as $2a+1=3$ leading to $a=2$ instead of $a=1$.

## How I would explain it in class
Continuity at $2$ means the left piece, the right piece, and the actual value at $2$ all land on the same height. The right piece and the value are both $3$, and the left piece reaches the height $2a+1$, so we need $2a+1=3$. This gives $a=1$, and then all three numbers equal $3$.
