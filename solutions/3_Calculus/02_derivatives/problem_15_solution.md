# Problem 15

## The original problem

Choose one function from the problem set and a point $x_0$ at which the derivative exists. Compute $f'(x_0)$ exactly, and then calculate
$$\frac{f(x_0+h)-f(x_0)}h$$
for $h=1$, $0.1$, and $0.01$. Compare the values with $f'(x_0)$ and explain why the difference quotient approaching a single number is consistent with the definition of the derivative, while a few computations do not replace a limit argument.

> **Why this problem:** it connects the definition of the derivative with concrete calculations and teaches the distinction between observation and proof.

## What we are looking for

We choose a function and a point. We find the derivative at that point exactly, by a rule. Then we compute the difference quotient for three step sizes, $h=1$, $h=0.1$ and $h=0.01$, and we put the results in a table. The question is whether the numbers get closer to the exact derivative. Then we explain what this does show and what it does not show.

**Our choice.** We take the function from Problem 9,
$$f(x)=\ln(x^2+1),\qquad x_0=1.$$
The derivative exists at this point, because the function is smooth everywhere.

## The idea we need

The **difference quotient** $\dfrac{f(x_0+h)-f(x_0)}{h}$ is the slope of the secant line, that is, the line through the two points $(x_0,f(x_0))$ and $(x_0+h,f(x_0+h))$. The **derivative** is defined as the limit of this quotient as $h$ tends to $0$. A limit is a statement about all small $h$, not about a few chosen ones.

For the exact value we use the chain rule: the derivative of $\ln(u)$ is $\frac1u$ times the derivative of the inside $u=x^2+1$, which is $2x$.

## Step-by-step solution

1. Exact derivative. By the chain rule, $f'(x)=\dfrac{2x}{x^2+1}$. At $x_0=1$:
$$f'(1)=\frac{2}{1+1}=1.$$
2. The value of the function at $x_0$: $f(1)=\ln2\approx0.693147$.
3. Quotient for $h=1$. Here $f(2)=\ln5\approx1.609438$, so
$$\frac{f(2)-f(1)}{1}=\ln5-\ln2=\ln2.5\approx0.916291.$$
4. Quotient for $h=0.1$. Here $f(1.1)=\ln(1.21+1)=\ln2.21\approx0.792993$, so
$$\frac{\ln2.21-\ln2}{0.1}=\frac{\ln1.105}{0.1}\approx0.998453.$$
5. Quotient for $h=0.01$. Here $f(1.01)=\ln(1.0201+1)=\ln2.0201$, so
$$\frac{\ln2.0201-\ln2}{0.01}=\frac{\ln1.01005}{0.01}\approx0.999983.$$
6. Put the results in a table. The last column is the quotient minus the exact value $1$.

| $h$ | difference quotient | quotient $-\,f'(1)$ |
|---|---|---|
| $1$ | $0.916291$ | $-0.083709$ |
| $0.1$ | $0.998453$ | $-0.001547$ |
| $0.01$ | $0.999983$ | $-0.0000165$ |

7. Observe. When $h$ is divided by $10$, the quotient comes much closer to $1$. The gap goes from about $0.084$, to $0.0015$, to $0.000017$. The numbers are heading towards $1$, which is exactly $f'(1)$.

## Why each step is valid

- Step 1 is valid because the chain rule applies to the composition $\ln(x^2+1)$, and the inside is positive everywhere.
- Steps 3 to 5 are valid because the quotient is just arithmetic with the definition, and each value uses the correct point $x_0+h$.
- Step 7 is consistent with the definition. The derivative is the number that the quotient approaches as $h\to0$. If the derivative is $1$, quotients for small $h$ must be near $1$, and they are. So the table is what the definition predicts.

## Final answer (in words)

The exact derivative is $f'(1)=1$. The difference quotients are about $0.9163$ for $h=1$, $0.9985$ for $h=0.1$, and $0.99998$ for $h=0.01$. They approach $1$, the exact derivative, as $h$ shrinks, which is what the definition of the derivative predicts. But three numbers are only an observation and not a proof. A proof needs a limit argument that covers every small $h$.

**Observation versus proof.** The table makes it believable that the limit is $1$, and it catches errors: if our formula had given $2$, the table would show that something is wrong. But it does not prove the limit, for three reasons. First, we tested only three values of $h$, while the limit speaks about all values. Second, the same table could be produced by a function whose quotient does something strange between our chosen values. Third, the quotient can look convergent from one side and still fail to have a derivative. For example, for $f(x)=|x|$ at $x_0=0$, every quotient with positive $h$ equals $1$, but the quotients with negative $h$ equal $-1$, and there is no derivative. A proof, such as the algebraic simplification in Problem 11, shows the result for all small $h$ at once.

## Verification

**Check 1: the exact value in another way.** At $x_0=1$ the formula $\frac{2x}{x^2+1}$ gives $\frac22=1$. The tangent line there is $y=\ln2+(x-1)$.

**Check 2: from the left.** Take $h=-0.01$. Then $\frac{\ln(0.9801+1)-\ln2}{-0.01}=\frac{\ln1.9801-\ln2}{-0.01}\approx0.999983$. This is also near $1$, and almost the same as the quotient for $h=0.01$. So the quotients from both sides approach the same number, as they must if the derivative exists.

**Check 3: a computed value of the function.** From the table of values, $f(1.01)=\ln2.0201\approx0.703147$ and $f(1)=\ln 2\approx0.693147$. Their difference is $0.01$ to six digits, so dividing by $0.01$ gives a number very close to $1$, as the table says.

## Common mistakes

- Saying the table proves that $f'(1)=1$. It supports the claim only.
- Computing $f(x_0+h)$ with the wrong point, for example using $f(1)+0.1$ instead of $f(1.1)$.
- Forgetting to divide by $h$. The numerator alone tends to $0$.
- Using degrees or a rounded value too early, so that the last digits of the small gaps are lost. With small $h$ keep many digits.

## How I would explain it in class

I take $f(x)=\ln(x^2+1)$ at $x_0=1$, where the chain rule gives the exact derivative $f'(1)=1$, and then I compute the secant slopes for $h=1$, $0.1$ and $0.01$, which are $0.9163$, $0.9985$ and $0.99998$. They get closer to $1$, which is what the definition of the derivative as a limit of the difference quotient predicts. But three numbers only show a pattern, and a proof must show that the quotient approaches the number for all small $h$, which is why we also use rules and limit arguments.
