# Problem 3

## The original problem

Compute
$$\int\left(2e^x+3\cos x-4\sin x\right)\,dx.$$
Match each term with a known derivative and verify the entire result with one differentiation.

> **Why this problem:** it builds a catalogue of basic antiderivatives from known derivatives.

## What we are looking for

We are asked for an antiderivative of a sum of three standard functions: an exponential, a cosine and a sine. No clever technique is needed. What we must show is the reasoning: for each term we look up which derivative it came from, and the sign is decided by that derivative, not by guesswork. Finally we differentiate the whole answer once and check that all three terms come back correctly.

## The idea we need

**Integration is the inverse of differentiation.** Every antiderivative is found by asking the question "which known function has derivative equal to this?".

**The catalogue we need.** These four derivative pairs are the ones we use here:
$$\frac{d}{dx}e^x=e^x,\qquad \frac{d}{dx}\sin x=\cos x,\qquad \frac{d}{dx}(-\cos x)=\sin x,\qquad \frac{d}{dx}\cos x=-\sin x.$$
Reading them backwards gives the antiderivatives:
$$\int e^x\,dx=e^x+C,\qquad \int\cos x\,dx=\sin x+C,\qquad \int\sin x\,dx=-\cos x+C.$$

**Linearity of the integral.** Since the derivative of a sum is the sum of the derivatives, an antiderivative of a sum is the sum of antiderivatives, and constants may be pulled out:
$$\int(a\,g+b\,h)\,dx=a\int g\,dx+b\int h\,dx.$$

**The constant of integration.** One arbitrary constant $C$ is added at the end, because the derivative of a constant is zero.

## Step-by-step solution

**Step 1. Match each term of the integrand with a known derivative.**

- The term $2e^x$ is a multiple of $e^x$, and $\dfrac{d}{dx}e^x=e^x$.
- The term $3\cos x$ is a multiple of $\cos x$, and $\dfrac{d}{dx}\sin x=\cos x$.
- The term $-4\sin x$ is a multiple of $\sin x$, and $\dfrac{d}{dx}(-\cos x)=\sin x$.

So the antiderivatives we need are $e^x$, $\sin x$ and $-\cos x$ respectively.

**Step 2. Integrate the first term.**

$$
\int 2e^x\,dx=2e^x.
$$

**Step 3. Integrate the second term.**

Since the derivative of $\sin x$ is $\cos x$, the antiderivative of $\cos x$ is $\sin x$:
$$\int 3\cos x\,dx=3\sin x.$$
This term is positive, because the sign of the antiderivative follows the sign of the derivative we matched, and $\dfrac{d}{dx}\sin x=+\cos x$.

**Step 4. Integrate the third term.**

Here we must be careful with the sign. We know $\dfrac{d}{dx}\cos x=-\sin x$, so the function whose derivative is $-\sin x$ is $+\cos x$:
$$\int(-4\sin x)\,dx=-4\cdot(-\cos x)=4\cos x.$$
The minus sign of the integrand cancels the minus sign that comes out of the matching, and the result is positive.

**Step 5. Add the pieces and one constant.**

$$
\int\left(2e^x+3\cos x-4\sin x\right)\,dx=2e^x+3\sin x+4\cos x+C.
$$

**Step 6. Verify the entire result with one differentiation.**

Take $F(x)=2e^x+3\sin x+4\cos x$. Differentiating the whole expression at once gives
$$F'(x)=2e^x+3\cos x+4(-\sin x)=2e^x+3\cos x-4\sin x=f(x).$$
All three terms come back exactly, so the answer is confirmed.

**Step 7. What the constant means here.**

Every function $2e^x+3\sin x+4\cos x+C$ is an antiderivative of $f$, because the added constant has derivative zero. The integrand alone cannot determine $C$.

## Why each step is valid

- Step 1 is valid because an antiderivative of a function is, by definition, a function whose derivative is that function; each pairing above satisfies this definition.
- Step 2 is valid because the derivative of $2e^x$ is $2e^x$, which is the first term of the integrand.
- Step 3 is valid because $\dfrac{d}{dx}(3\sin x)=3\cos x$, matching the second term of the integrand.
- Step 4 is valid because $\dfrac{d}{dx}(4\cos x)=-4\sin x$, matching the third term of the integrand exactly.
- Step 5 is valid because the derivative of a sum is the sum of the derivatives, and the derivative of $C$ is zero.
- Step 6 is valid as a complete check: a single differentiation of the final formula reproduces the whole integrand, term by term.
- Step 7 is valid because a constant has derivative zero everywhere.

## Final answer (in words)

The antiderivative is $2e^x+3\sin x+4\cos x$ plus an arbitrary constant $C$. In words: the exponential term integrates to itself, the cosine term integrates to a sine with a plus sign, and the sine term with a minus sign integrates to a cosine with a plus sign, because the derivative of $\cos x$ is $-\sin x$.

## Verification

**Check 1 (the required one): one differentiation of the whole answer.** As shown in Step 6,
$$\frac{d}{dx}\left(2e^x+3\sin x+4\cos x\right)=2e^x+3\cos x-4\sin x,$$
which coincides with the integrand term by term.

**Check 2: a numerical slope check at a single point.** At $x=0$ our antiderivative has the value
$$F(0)=2\cdot 1+3\cdot 0+4\cdot 1=6,$$
and its derivative at $0$ is
$$F'(0)=2\cdot 1+3\cdot 1-4\cdot 0=5.$$
The integrand at $0$ is $2e^0+3\cos 0-4\sin 0=2+3-0=5$. The two agree, so the formula is right at this point, not only formally.

**Check 3: numerical value of a definite integral.** Using the Fundamental Theorem of Calculus,
$$\int_0^1\left(2e^x+3\cos x-4\sin x\right)dx=F(1)-F(0)=2e+3\sin 1+4\cos 1-6\approx 4.122186.$$
Simpson's rule with four subintervals gives $\frac{0.25}{3}\left(f(0)+4f(0.25)+2f(0.5)+4f(0.75)+f(1)\right)\approx 4.122275$, which agrees with the exact value to about four decimal places.

## Common mistakes

- **Wrong sign for the sine term.** The derivative of $\cos x$ is $-\sin x$, so the term $-4\sin x$ integrates to $+4\cos x$, not to $-4\cos x$.
- **Confusing the two trigonometric antiderivatives.** It is $\int\cos x\,dx=\sin x$ and $\int\sin x\,dx=-\cos x$; mixing them up is the most common error in this problem.
- **Writing $\int e^x\,dx=xe^x$.** The exponential is its own antiderivative, so $\int e^x\,dx=e^x+C$; the factor $x$ would come from integration by parts.
- **Dropping the constant $C$.** The indefinite integral is the family $2e^x+3\sin x+4\cos x+C$, not a single function.

## How I would explain it in class

For each term I ask which known function has exactly that derivative, so $2e^x$ comes from $e^x$, $3\cos x$ comes from $3\sin x$, and $-4\sin x$ comes from $4\cos x$ because the derivative of a cosine is a minus sine. Adding the three pieces gives $2e^x+3\sin x+4\cos x+C$. Differentiating that whole expression once brings back $2e^x+3\cos x-4\sin x$, which proves the answer in one step.
