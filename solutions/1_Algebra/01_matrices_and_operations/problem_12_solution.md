# Problem 12

## The original problem

Let

$$
A=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
$$

Compute $A^2$, $A^3$, and $A^4$, and use them to formulate a conjecture for $A^n$. Then do not stop after checking one more case: assume the formula is true for $n$, multiply by $A$, and explain why you obtain exactly the formula for $n+1$.

> **Why this exercise:** teaches how to recognize a pattern and formulate a generalization from several computations.

## What we are looking for

We need the matrices $A^2$, $A^3$, $A^4$, then a general formula for $A^n$ (a conjecture, that is, an educated guess based on the pattern), and finally a proof by induction step: if the formula holds for $n$, it also holds for $n+1$.

## The idea we need

Powers are repeated products: $A^{k+1}=A^kA$. To prove a formula for every positive integer $n$ we use induction. We check the formula for the first case $n=1$ (the base case), and we show that whenever it is true for some $n$, it is also true for $n+1$ (the induction step). Then it is true for $n=1$, hence for $n=2$, hence for $n=3$, and so on for every $n$.

## Step-by-step solution

**Step 1: the powers.**

$$
A^2=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}1\cdot1+1\cdot0&1\cdot1+1\cdot1\\0&1\end{pmatrix}=\begin{pmatrix}1&2\\0&1\end{pmatrix}.
$$

$$
A^3=A^2A=\begin{pmatrix}1&2\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}1&1+2\\0&1\end{pmatrix}=\begin{pmatrix}1&3\\0&1\end{pmatrix}.
$$

$$
A^4=A^3A=\begin{pmatrix}1&3\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}1&1+3\\0&1\end{pmatrix}=\begin{pmatrix}1&4\\0&1\end{pmatrix}.
$$

**Step 2: the conjecture.** In every power the diagonal entries are $1$, the lower left entry is $0$, and the upper right entry equals the exponent: $1,2,3,4$. We conjecture

$$
A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}\qquad\text{for every positive integer }n.
$$

**Step 3: base case.** For $n=1$ the formula gives $\begin{pmatrix}1&1\\0&1\end{pmatrix}=A$, which is true.

**Step 4: induction step.** Assume that for some $n$ we have $A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$. Then

$$
A^{n+1}=A^nA=\begin{pmatrix}1&n\\0&1\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}=\begin{pmatrix}1\cdot1+n\cdot0&1\cdot1+n\cdot1\\0\cdot1+1\cdot0&0\cdot1+1\cdot1\end{pmatrix}=\begin{pmatrix}1&n+1\\0&1\end{pmatrix}.
$$

This is exactly the formula with $n$ replaced by $n+1$.

**Step 5: conclusion.** The base case holds and each case implies the next, so the formula $A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$ holds for every positive integer $n$.

## Why each step is valid

- Computing the powers directly is allowed because each is a matrix product of known matrices, and writing $A^{k+1}=A^kA$ uses only the definition of a power.
- A pattern seen in three cases is not a proof, since a different rule could produce the same first three values. This is why the induction step is needed: it works with an arbitrary $n$, not with one particular number.
- In step 4 the assumption (the induction hypothesis) is used exactly once, to replace $A^n$ by the matrix with $n$ in the corner. After that only the ordinary rule for multiplying matrices is used.
- The two parts together make a complete proof: the base case starts the chain and the induction step keeps it going without a gap.

## Final answer (in words)

$A^2=\begin{pmatrix}1&2\\0&1\end{pmatrix}$, $A^3=\begin{pmatrix}1&3\\0&1\end{pmatrix}$, $A^4=\begin{pmatrix}1&4\\0&1\end{pmatrix}$, and in general

$$
A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}.
$$

Multiplying the formula for $n$ by $A$ gives the same formula with $n+1$ in the corner, because multiplying by $A$ adds $1$ to the upper right entry and changes nothing else; therefore the formula is true for every positive integer $n$.

## Verification

An independent check avoids induction: write $A=I+N$ with $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$. Then $N^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}$, and because $I$ commutes with $N$ the binomial expansion gives $A^n=I+nN+(\text{terms with }N^2\text{ or higher})=I+nN=\begin{pmatrix}1&n\\0&1\end{pmatrix}$, the same formula. A numerical test with a larger exponent: sympy gives $A^{10}=\begin{pmatrix}1&10\\0&1\end{pmatrix}$, in agreement. Also, the determinant of every power should equal $(\det A)^n=1$, and $\det\begin{pmatrix}1&n\\0&1\end{pmatrix}=1$.

## Common mistakes

- Raising each entry to the power $n$, which would give $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ again and is not matrix powering.
- Accepting the conjecture after checking only one more case, for example $A^5$.
- Making an arithmetic slip in the induction step, such as computing the upper right entry as $1\cdot1+n\cdot0$ instead of $1\cdot1+n\cdot1$, which loses the added $1$.
- Forgetting the base case and proving only the step.

## How I would explain it in class

Computing $A^2$, $A^3$, $A^4$ gives upper right entries $2,3,4$ with the rest unchanged, so we guess $A^n=\begin{pmatrix}1&n\\0&1\end{pmatrix}$. To prove it, assume it holds for $n$ and multiply by $A$: the product is $\begin{pmatrix}1&n+1\\0&1\end{pmatrix}$, which is the formula for $n+1$. Since the formula holds for $n=1$ and each case leads to the next, it holds for all $n$, and the splitting $A=I+N$ with $N^2=0$ gives the same result by a different route.
