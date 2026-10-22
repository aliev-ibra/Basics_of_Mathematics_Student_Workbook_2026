# Problem 15

## The original problem

The function $F$ satisfies
$$F'(x)=2xe^{x^2}$$
and
$$F(0)=3.$$

1. Recognize the method needed to find the function $F$.
2. Determine the entire family of functions with the given derivative.
3. Use the condition $F(0)=3$ to determine the correct constant.
4. Verify the final result by differentiation and substitution of $x=0$.

> **Why this problem:** it combines recognition of substitution, the meaning of the constant of integration, and an initial condition in one problem, using only mechanisms introduced earlier.

## What we are looking for

We know the derivative of an unknown function $F$, and we know one value of $F$. We must find the formula for $F$. The derivative alone gives a whole family of functions, and the value $F(0)=3$ picks one function from it.

## The idea we need

**Substitution.** This reverses the chain rule. We look for an inner function whose derivative also appears in the integrand.

**Constant of integration.** Two functions with the same derivative differ by a constant. So the antiderivative is a family with a letter $C$.

**Initial condition.** A known value of $F$ at one point fixes $C$.

## Step-by-step solution

**Step 1. Recognize the method (part 1).** The integrand $2xe^{x^2}$ contains the exponential of an inner function, $x^2$. The derivative of $x^2$ is $2x$, and $2x$ is also present as a factor. This is the pattern for substitution.

**Step 2. Substitute.** Let $u=x^2$. Then $du=2x\,dx$. The integral becomes
$$\int e^{u}\,du=e^{u}+C.$$

**Step 3. Return to $x$ (part 2).** Replacing $u$ by $x^2$ gives the family
$$F(x)=e^{x^2}+C.$$

**Step 4. Use the condition (part 3).** Put $x=0$: $F(0)=e^{0}+C=1+C$. We need $F(0)=3$, so $1+C=3$ and $C=2$.

**Step 5. The answer.**
$$F(x)=e^{x^2}+2.$$

## Why each step is valid

- Step 1 is valid because the factor $2x$ is exactly the derivative of the inner function $x^2$, so nothing is left over.
- Step 2 is valid because $du=2x\,dx$ matches the integrand with no extra factor, and the antiderivative of $e^u$ is $e^u$.
- Step 3 is valid because we return to the original variable. The constant stays, since the derivative of a constant is $0$.
- Step 4 is valid because $e^{0}=1$ and the condition must hold for the chosen function.
- Step 5 is valid because only one value of $C$ satisfies the condition.

## Final answer (in words)

The function with the derivative $2xe^{x^2}$ is $F(x)=e^{x^2}+C$ for some constant $C$. The condition $F(0)=3$ gives $C=2$. So the answer is $F(x)=e^{x^2}+2$.

## Verification

**Check 1: differentiate.** By the chain rule, the derivative of $e^{x^2}$ is $e^{x^2}\cdot2x$, and the derivative of $2$ is $0$. So $F'(x)=2xe^{x^2}$, as required.

**Check 2: substitute $x=0$.** $F(0)=e^{0}+2=1+2=3$, as required.

**Check 3: a numerical value.** The growth from $0$ to $1$ is $F(1)-F(0)=(e+2)-3=e-1\approx1.718$. Numerically integrating $2xe^{x^2}$ from $0$ to $1$ gives the same value.

## Common mistakes

- Writing $F(x)=\frac{e^{x^2}}{2x}$, which wrongly treats $x^2$ like $x$.
- Dropping the constant and getting $e^{x^2}$, which gives $F(0)=1$ instead of $3$.
- Finding $C$ by substituting into $F'$ instead of $F$.
- Writing $C=3$ instead of $C=2$, forgetting that $e^0=1$.

## How I would explain it in class

The derivative $2xe^{x^2}$ is an exponential of $x^2$ times the derivative of $x^2$, so I use substitution with $u=x^2$ and get the family $F(x)=e^{x^2}+C$. The condition $F(0)=3$ gives $1+C=3$, so $C=2$ and $F(x)=e^{x^2}+2$. Differentiating gives back $2xe^{x^2}$, and putting $x=0$ gives $3$.
