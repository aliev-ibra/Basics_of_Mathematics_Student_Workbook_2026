# Problem 14

## The original problem

Investigate the behavior at $x=0$ of
$$f(x)=\begin{cases}x^2,&x\ge0,\\ax,&x<0.\end{cases}$$
For which values of $a$ is the function continuous? For which values do the one-sided derivatives exist and agree? For which value of $a$ is the function differentiable? Explain why continuity alone is not sufficient.

> **Why this problem:** it requires an organized argument and a clear distinction between two concepts.

## What we are looking for

The function has two formulas. For $x\ge0$ we use $x^2$. For $x<0$ we use $ax$, where $a$ is a constant number that we can choose. We must study the point $x=0$, where the formulas meet, and answer three questions. For which $a$ do the two pieces join without a jump? For which $a$ do the slopes from the left and from the right exist and agree? For which $a$ is the function differentiable at $0$? Finally we must explain why joining without a jump is not enough for a derivative.

## The idea we need

**Continuity at a point $0$.** A function is continuous at $0$ if three numbers are equal: the value $f(0)$, the limit from the left, and the limit from the right. Informally, the graph can be drawn through that point without lifting the pencil.

**One-sided derivatives.** The derivative from the right is
$$f'_+(0)=\lim_{h\to0^+}\frac{f(0+h)-f(0)}{h},$$
where $h\to0^+$ means $h$ is positive and tends to $0$. The derivative from the left is the same limit with $h\to0^-$, that is, $h$ negative and tending to $0$. The quotient is the slope of the line through the points $(0,f(0))$ and $(h,f(h))$.

**Differentiability.** The function is differentiable at $0$ if and only if both one-sided derivatives exist and are equal. The common value is $f'(0)$.

We use this because the function has different formulas on the two sides, so we must test each side separately.

## Step-by-step solution

1. The value at zero. Since $0\ge0$, we use the first formula: $f(0)=0^2=0$.
2. The limit from the right. For $x>0$ we have $f(x)=x^2$, which tends to $0$. So the right limit is $0$.
3. The limit from the left. For $x<0$ we have $f(x)=ax$, which tends to $a\cdot0=0$. So the left limit is $0$ for every value of $a$.
4. Continuity. The value, the left limit and the right limit are all $0$, whatever $a$ is. So $f$ is continuous at $0$ for **every real number $a$**.
5. Right derivative. For $h>0$ we have $f(h)=h^2$, so
$$\frac{f(h)-f(0)}{h}=\frac{h^2-0}{h}=h\longrightarrow0\quad(h\to0^+).$$
So $f'_+(0)=0$. It exists for every $a$.
6. Left derivative. For $h<0$ we have $f(h)=ah$, so
$$\frac{f(h)-f(0)}{h}=\frac{ah-0}{h}=a\longrightarrow a\quad(h\to0^-).$$
So $f'_-(0)=a$. It exists for every $a$.
7. Agreement. The two one-sided derivatives are equal when $a=0$, and only then.
8. Conclusion. The function is differentiable at $0$ exactly for $a=0$, and then $f'(0)=0$. For $a\neq0$ the graph has a corner at the origin: the right piece leaves the origin horizontally, and the left piece leaves it with slope $a$.
9. Why continuity is not enough. Take $a=1$. The function is continuous at $0$ by Step 4. But the left slope is $1$ and the right slope is $0$. These are different, so the derivative does not exist. Continuity says only that the two pieces meet at one point. Differentiability asks for more: they must also meet with the same direction.

## Why each step is valid

- Steps 1 to 4 are valid because continuity is defined by the equality of $f(0)$ with the left and right limits.
- Steps 5 and 6 are valid because, for $h>0$ the point $h$ lies in the part where $f=x^2$, and for $h<0$ it lies in the part where $f=ax$. We use the correct formula for each side. After cancelling $h$ (allowed because $h\neq0$) we have simple expressions whose limits are obvious.
- Step 7 is valid because a two-sided limit exists exactly when both one-sided limits exist and are equal.
- Step 9 is valid because differentiability at a point means that the single two-sided limit of the quotient exists, and here the two sides give different numbers.

## Final answer (in words)

The function is continuous at $0$ for every real $a$. The right derivative at $0$ is $0$ and the left derivative is $a$, so both exist for every $a$, and they agree only when $a=0$. So the function is differentiable at $0$ only for $a=0$, and then $f'(0)=0$. Continuity is not sufficient: for $a=1$ the function is continuous at $0$ but has a corner there, with different slopes on the two sides.

## Verification

**Check 1: numbers for $a=2$.** Take $h=0.01$ and $h=-0.01$. We have $f(0.01)=0.0001$, so the quotient is $0.01$, near $0$. We have $f(-0.01)=-0.02$, so the quotient is $\frac{-0.02}{-0.01}=2$, which equals $a$. The two sides differ, so there is no derivative.

**Check 2: the case $a=0$.** Then $f(x)=0$ for $x<0$ and $f(x)=x^2$ for $x\ge0$. The quotient from the left is exactly $0$, and from the right it is $h$, which tends to $0$. Both sides give $0$, so $f'(0)=0$. This matches Step 8.

**Check 3: a familiar example.** The function $|x|$ is continuous at $0$, with slope $-1$ on the left and $1$ on the right, and it is not differentiable there. Our function with $a\neq0$ is a corner of the same kind, so the conclusion agrees with this known example.

## Common mistakes

- Thinking that continuity forces $a=0$. The pieces already meet at height $0$ for every $a$.
- Using the formula $x^2$ for negative $h$, or $ax$ for positive $h$.
- Differentiating each piece and glueing the formulas, writing $f'(0)=2\cdot0=0$ from the right only. The left side must also be checked.
- Believing that continuous implies differentiable. It is true in the other direction: a differentiable function is always continuous.

## How I would explain it in class

At $x=0$ both pieces give height $0$, so the function is continuous for every value of $a$. Then I compute the slopes on each side from the definition: from the right the quotient is $h$ and tends to $0$, and from the left the quotient is $a$, so the two slopes agree only for $a=0$. This is why differentiability is stronger than continuity: for $a=1$ the graph is unbroken but has a corner at the origin, and a corner has no single tangent line.
