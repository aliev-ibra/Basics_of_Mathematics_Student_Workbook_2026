# Problem 08

## The original problem
Compute
$$\lim_{x\to4}\frac{\sqrt{x}-2}{x-4}$$
by rationalizing the numerator. Compare the idea with Exercise 3 involving a sequence.

## What we are looking for
We want the value that the function approaches as $x$ gets closer and closer to $4$. Direct substitution gives the indeterminate form $0/0$, so we need to rationalize the numerator. We also need to compare this technique with Exercise 3, which used the same idea for a sequence limit at infinity.

## The idea we need
This is a limit at a point as $x\to4$ (a two-sided limit). Direct substitution gives $\frac{\sqrt{4}-2}{4-4}=\frac{0}{0}$, an indeterminate form. The standard technique is to rationalize the numerator by multiplying by the conjugate expression $\sqrt{x}+2$ over itself. This uses the difference of squares:
$$(\sqrt{x}-2)(\sqrt{x}+2)=x-4,$$
which cancels the factor $x-4$ in the denominator. The cancellation is valid because the limit only concerns $x$ near but not equal to $4$, so $x-4\neq 0$ throughout the relevant neighborhood.

## Step-by-step solution
1. Write the function:
$$f(x)=\frac{\sqrt{x}-2}{x-4}.$$
2. Direct substitution at $x=4$ gives $\frac{0}{0}$, so we cannot substitute directly.
3. Multiply by the conjugate expression $\frac{\sqrt{x}+2}{\sqrt{x}+2}$:
$$f(x)=\frac{\sqrt{x}-2}{x-4}\cdot\frac{\sqrt{x}+2}{\sqrt{x}+2}.$$
4. Apply the difference of squares in the numerator:
$$f(x)=\frac{(\sqrt{x})^2-2^2}{(x-4)(\sqrt{x}+2)}=\frac{x-4}{(x-4)(\sqrt{x}+2)}.$$
5. For $x\neq 4$, cancel the common factor $(x-4)$:
$$f(x)=\frac{1}{\sqrt{x}+2}\qquad (x\neq 4).$$
6. Now compute the limit by substitution, valid because $\sqrt{x}+2$ is continuous at $x=4$:
$$\lim_{x\to4}f(x)=\lim_{x\to4}\frac{1}{\sqrt{x}+2}=\frac{1}{\sqrt{4}+2}=\frac{1}{2+2}=\frac14.$$

## Comparison with Exercise 3
Exercise 3 computed $\lim_{n\to\infty}(\sqrt{n^2+5n}-n)$, a sequence limit at infinity with the indeterminate form $\infty-\infty$. Exercise 8 computes $\lim_{x\to4}\frac{\sqrt{x}-2}{x-4}$, a function limit at a point with the indeterminate form $0/0$. In both cases the key idea is the same: multiply by the conjugate expression to turn a difference involving square roots into a difference of squares, which removes the square roots from the numerator and cancels the troublesome factor. The difference is the setting: Exercise 3 sends $n$ to infinity and divides by $n$ afterward, while Exercise 8 sends $x$ to a finite point $4$ and cancels $x-4$.

## Why each step is valid
Step 3 is valid because multiplying by $\frac{\sqrt{x}+2}{\sqrt{x}+2}$ is multiplying by $1$ (the denominator is nonzero for $x\ge 0$, and near $x=4$ it is certainly nonzero), so the value is unchanged. Step 4 uses the identity $(A-B)(A+B)=A^2-B^2$ with $A=\sqrt{x}$ and $B=2$. Step 5 is valid for $x\neq 4$, which is exactly the domain relevant to the limit $x\to4$. Step 6 uses the continuity of the square root function at $4$ and of rational functions where the denominator is nonzero.

## Final answer (in words)
The function approaches the value $\frac14$ as $x$ approaches $4$ from either side. Rationalizing the numerator removes the indeterminate $0/0$ form and leaves the continuous expression $\frac{1}{\sqrt{x}+2}$, whose value at $x=4$ is $0.25$.

## Verification
Take $x=4.001$: $\frac{\sqrt{4.001}-2}{4.001-4}=\frac{2.00024998-2}{0.001}=\frac{0.00024998}{0.001}=0.24998$. Take $x=3.999$: $\frac{\sqrt{3.999}-2}{3.999-4}=\frac{1.99974998-2}{-0.001}=\frac{-0.00025002}{-0.001}=0.25002$. Both sides approach $0.25=\frac14$, confirming the limit.

## Common mistakes
- Substituting $x=4$ directly and stopping at $0/0$ without rationalizing.
- Forgetting to multiply both numerator and denominator by the conjugate, so the square root remains.
- Cancelling $(x-4)$ and then thinking the original function becomes defined at $x=4$ (it does not; only the simplified expression is defined there).

## How I would explain it in class
Plugging in four gives zero over zero, so we multiply the top and bottom by the conjugate $\sqrt{x}+2$, which is just multiplying by one, and the difference of squares turns the top into $x-4$ which cancels the bottom. We are left with one over $\sqrt{x}+2$, and plugging in four gives one over four. The same conjugation trick that worked for the sequence in Exercise 3 works here too, just at a finite point instead of infinity.
