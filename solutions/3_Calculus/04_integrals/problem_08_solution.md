# Problem 8

## The original problem

Compute
$$\int x\cos x\,dx.$$
Before calculating, justify why it is convenient to differentiate $x$ and integrate $\cos x$, rather than the other way around.

> **Why this problem:** it teaches that integration by parts requires a deliberate choice of factors.

## What we are looking for

We are asked for an antiderivative of a polynomial factor times a trigonometric factor. Such a product cannot be handled by the power rule, so integration by parts is needed, and integration by parts always begins with a decision. The problem therefore asks us to make that decision and to defend it before doing any calculation. Only then do we carry out the computation and check the result.

## The idea we need

**Integration by parts.** The formula obtained by reversing the product rule is
$$\int u\,v'\,dx=uv-\int u'v\,dx,$$
where $u$ is the part we differentiate and $dv$ is the part we integrate.

**The rule for the choice.** Two guidelines are used in practice:

1. *Differentiate the factor that becomes simpler.* A polynomial becomes a simpler polynomial, while $\cos x$ does not become simpler when differentiated (it becomes $-\sin x$).
2. *Integrate the factor whose antiderivative you know.* Here $\int\cos x\,dx=\sin x$ is a standard fact, whereas integrating $x$ is also standard, so both candidates are integrable and we must use guideline 1 to decide.

Equivalently, in the usual ordering rule (logarithmic, inverse trigonometric, algebraic, trigonometric, exponential), the factor that comes earlier is the one we differentiate. Here the algebraic factor $x$ comes earlier than the trigonometric factor $\cos x$, so $x$ is differentiated.

**Conditions for the method to work.** After the choice, the remaining integral $\int u'v\,dx$ must be easier than the original one, ideally integrable in one step. This is the real test of a good choice.

**Constant of integration.** A single $C$ is added at the end, since the derivative of a constant is zero.

## Step-by-step solution

**Step 1. State the method and its formula.**

The integrand $x\cos x$ is a product of a polynomial and a trigonometric function, and neither factor can be integrated to give the other factor back. This is exactly the situation of integration by parts:
$$\int u\,v'\,dx=uv-\int u'v\,dx.$$

**Step 2. Make the choice and justify it before calculating.**

We choose
$$u=x,\qquad dv=\cos x\,dx.$$
The justification has two parts.

- *Differentiating $x$ simplifies it.* $u'=1$, a constant. Differentiating $\cos x$ instead would give $-\sin x$, which is no simpler, so on this side the polynomial is clearly the better candidate for $u$.
- *The other way round fails.* If we took $u=\cos x$ and $dv=x\,dx$, then $du=-\sin x\,dx$ and $v=\frac{x^2}{2}$, and the formula would give
$$\int x\cos x\,dx=x\cos x-\int\frac{x^2}{2}\cdot(-\sin x)\,dx=x\cos x+\frac{1}{2}\int x^2\sin x\,dx.$$
The new integral contains a polynomial of higher degree, so it is harder than the original and would require integration by parts again. Our choice, by contrast, leaves the trivial integral $\int \sin x\,dx$.

**Step 3. Compute $du$ and $v$.**

$$
du=dx,\qquad v=\int\cos x\,dx=\sin x.
$$
Both are immediate: the derivative of $x$ is $1$, and the derivative of $\sin x$ is $\cos x$.

**Step 4. Apply the formula.**

$$
\int x\cos x\,dx=uv-\int u'v\,dx=x\sin x-\int 1\cdot\sin x\,dx=x\sin x-\left(-\cos x\right)+C=x\sin x+\cos x+C.
$$

**Step 5. Watch the sign in the last step.**

Since $\int\sin x\,dx=-\cos x$, the term $-\int\sin x\,dx$ becomes $+\cos x$. Two minus signs cancel here, and forgetting this is the most common slip in the problem.

**Step 6. State the answer.**

One antiderivative is $F(x)=x\sin x+\cos x$; the whole family is $x\sin x+\cos x+C$.

## Why each step is valid

- Step 1 is valid because the power rule cannot handle a product of unrelated functions, so a different method is needed, and integration by parts is the standard method for a product with one easily integrable factor.
- Step 2 is valid because the choice is judged by the remaining integral: our choice leaves $\int\sin x\,dx$, while the opposite choice leaves $\int x^2\sin x\,dx$, which is strictly harder.
- Step 3 is valid because $\frac{d}{dx}x=1$ and $\frac{d}{dx}\sin x=\cos x$.
- Step 4 is valid because it is the integration-by-parts formula with $u$, $v$, $du$, $v'$ substituted correctly.
- Step 5 is valid because $\int\sin x\,dx=-\cos x$ follows from $\frac{d}{dx}\cos x=-\sin x$.
- Step 6 is valid because the derivative of a constant is zero, so every value of $C$ gives an antiderivative.

## Final answer (in words)

The antiderivative of $x\cos x$ is $x\sin x+\cos x$, plus an arbitrary constant $C$. In words: we differentiate the polynomial factor $x$ and integrate the trigonometric factor $\cos x$, because differentiating a polynomial makes it simpler while differentiating a cosine does not, and the opposite choice would leave behind an integral that is harder than the one we began with.

## Verification

**Check 1 (the required one): differentiate the answer.** Let $F(x)=x\sin x+\cos x$. By the product rule and the chain rule for the sine,
$$F'(x)=1\cdot\sin x+x\cos x+(-\sin x)=x\cos x.$$
The two extra terms $\sin x$ and $-\sin x$ cancel, and exactly the original integrand remains.

**Check 2: a numerical check of a definite integral.** The Fundamental Theorem of Calculus gives
$$\int_0^1 x\cos x\,dx=\left[x\sin x+\cos x\right]_0^1=(\sin 1+\cos 1)-(0+1)\approx 0.381773.$$
Simpson's rule with four subintervals uses the values $0$, $0.242228$, $0.438791$, $0.548767$, $0.540302$ and gives
$$\frac{0.25}{3}\left(0+4\cdot 0.242228+2\cdot 0.438791+4\cdot 0.548767+0.540302\right)\approx 0.381822,$$
in good agreement with the exact value $0.381773$.

**Check 3: a symmetry check of the structure.** The answer is a sum of a term with $x$ and a term without $x$. That is exactly what the formula must produce: the product $uv=x\sin x$ keeps the factor $x$, and the correction term $v=\sin x$ does not. A wrong choice of $u$ and $dv$ would have produced terms of the wrong shape (here a square $x^2$), which is a quick way to notice a mistake.

## Common mistakes

- **Choosing $u=\cos x$.** Then $v=\frac{x^2}{2}$ and the remaining integral $\int x^2\sin x\,dx$ is harder than the original, so the method does not simplify anything.
- **Losing the sign on the correction term.** Since $\int\sin x\,dx=-\cos x$, the term $-\int\sin x\,dx$ is $+\cos x$. Writing $-\cos x$ instead is the classic error here.
- **Stopping halfway.** After writing $x\sin x-\int\sin x\,dx$ the work is not finished: the remaining integral still has to be evaluated.
- **Forgetting the constant $C$.** The indefinite integral is the family $x\sin x+\cos x+C$.
- **Choosing without justifying.** The problem explicitly asks why this choice of factors is convenient, so the reasoning must be written down, not just the final numbers.

## How I would explain it in class

Integration by parts needs a decision, and here I decide to differentiate $x$ and integrate $\cos x$, because differentiating a polynomial makes it simpler while differentiating a cosine does not, and the opposite choice would leave the harder integral $\int x^2\sin x\,dx$. With $u=x$, $dv=\cos x\,dx$, $du=dx$ and $v=\sin x$, the formula gives $x\sin x-\int\sin x\,dx=x\sin x+\cos x+C$. Differentiating this answer reproduces $x\cos x$, because the extra $\sin x$ and $-\sin x$ terms cancel.
