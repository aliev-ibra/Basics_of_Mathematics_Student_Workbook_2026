# Problem 13

## The original problem

Let

$$
F=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
$$

Compute $F^2$, $F^3$, $F^4$, and $F^5$. Compare the numbers obtained with the sequence

$$
0,1,1,2,3,5,8,\ldots
$$

and describe the relationship you observe. Then compute

$$
F\begin{pmatrix}a\\b\end{pmatrix}
$$

and explain how this multiplication performs one recurrence step: it creates the sum of two consecutive terms and keeps one of them for the next step.

> **Why this exercise:** shows the connection between matrix powers and a simple numerical recurrence.

## What we are looking for

We need four matrix powers, a description of how their entries relate to the sequence $0,1,1,2,3,5,8,\ldots$ (the Fibonacci numbers, where each term after the first two is the sum of the two previous ones), and the product $F$ times a column vector $(a,b)^T$ with an explanation of why it is one step of the recurrence.

## The idea we need

Label the sequence $F_0=0$, $F_1=1$, $F_2=1$, $F_3=2$, $F_4=3$, $F_5=5$, $F_6=8$, and in general $F_{k+1}=F_k+F_{k-1}$. (The letter $F$ for the numbers and the same letter for the matrix are different objects; to avoid confusion I write the Fibonacci numbers with subscripts.) Powers are repeated products, $F^{k+1}=F^kF$.

## Step-by-step solution

**Step 1: the powers.**

$$
F^2=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}=\begin{pmatrix}1\cdot1+1\cdot1&1\cdot1+1\cdot0\\1\cdot1+0\cdot1&1\cdot1+0\cdot0\end{pmatrix}=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
$$

$$
F^3=F^2F=\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}=\begin{pmatrix}2+1&2+0\\1+1&1+0\end{pmatrix}=\begin{pmatrix}3&2\\2&1\end{pmatrix}.
$$

$$
F^4=F^3F=\begin{pmatrix}3&2\\2&1\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}=\begin{pmatrix}3+2&3+0\\2+1&2+0\end{pmatrix}=\begin{pmatrix}5&3\\3&2\end{pmatrix}.
$$

$$
F^5=F^4F=\begin{pmatrix}5&3\\3&2\end{pmatrix}\begin{pmatrix}1&1\\1&0\end{pmatrix}=\begin{pmatrix}5+3&5+0\\3+2&3+0\end{pmatrix}=\begin{pmatrix}8&5\\5&3\end{pmatrix}.
$$

**Step 2: compare with the sequence.** The entries are Fibonacci numbers. $F^2$ contains $2,1,1,1$, that is $F_3,F_2,F_2,F_1$; $F^3$ contains $3,2,2,1$; $F^4$ contains $5,3,3,2$; $F^5$ contains $8,5,5,3$. The pattern is

$$
F^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}.
$$

For example, $n=5$ gives $F_6=8$, $F_5=5$, $F_4=3$. The first power, $F^1=\begin{pmatrix}1&1\\1&0\end{pmatrix}$, fits the pattern too, with $F_2=1$, $F_1=1$, $F_0=0$. The matrix is symmetric (equal to its transpose), which is why the two off-diagonal entries are always equal.

**Step 3: one recurrence step.**

$$
F\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}1\cdot a+1\cdot b\\1\cdot a+0\cdot b\end{pmatrix}=\begin{pmatrix}a+b\\a\end{pmatrix}.
$$

The first entry of the result is the sum of the two numbers, and the second entry is the first number $a$, copied. If the vector is $\begin{pmatrix}F_{k}\\F_{k-1}\end{pmatrix}$ (two consecutive terms, the newer one on top), the result is $\begin{pmatrix}F_k+F_{k-1}\\F_k\end{pmatrix}=\begin{pmatrix}F_{k+1}\\F_k\end{pmatrix}$. So one multiplication by $F$ creates the next term as the sum of the two consecutive terms and keeps the newer old term as the lower entry, ready for the next step.

**Step 4: link to the powers.** Starting from $\begin{pmatrix}F_1\\F_0\end{pmatrix}=\begin{pmatrix}1\\0\end{pmatrix}$ and applying $F$ repeatedly gives $F^n\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}F_{n+1}\\F_n\end{pmatrix}$, which is exactly the first column of $F^n$. This is why the powers contain the Fibonacci numbers.

## Why each step is valid

- Each power is obtained by one more multiplication by $F$, using the row-times-column rule; the entries come out as sums of two earlier entries, because multiplying by $F$ on the right replaces a row $(p,q)$ by $(p+q,\,p)$.
- That same fact is the reason for the Fibonacci pattern: the row $(p,q)$ becomes $(p+q,p)$, so the first entry of each row is the sum of both entries of the earlier row, and the second entry is the earlier first entry. This is the recurrence $F_{k+1}=F_k+F_{k-1}$ written for matrices.
- The vector computation in step 3 is the matrix-vector rule, and its interpretation as a recurrence step depends only on the two entries being consecutive terms.
- The identification $F^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$ was observed for $n=1,\dots,5$; it holds for all $n$ by induction, since multiplying the matrix by $F$ turns a row $(F_{n+1},F_n)$ into $(F_{n+1}+F_n,F_{n+1})=(F_{n+2},F_{n+1})$ and a row $(F_n,F_{n-1})$ into $(F_{n+1},F_n)$.

## Final answer (in words)

The powers are $F^2=\begin{pmatrix}2&1\\1&1\end{pmatrix}$, $F^3=\begin{pmatrix}3&2\\2&1\end{pmatrix}$, $F^4=\begin{pmatrix}5&3\\3&2\end{pmatrix}$, $F^5=\begin{pmatrix}8&5\\5&3\end{pmatrix}$. Their entries are consecutive Fibonacci numbers: $F^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$. Multiplying by $F$ gives $F\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}a+b\\a\end{pmatrix}$, which creates the sum of the two numbers in the top entry and keeps the first number in the bottom entry, so each multiplication is one step of the recurrence.

## Verification

The relation $F^5=F^2F^3$ is a check that does not use the one-step-at-a-time products: $\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}3&2\\2&1\end{pmatrix}=\begin{pmatrix}6+2&4+1\\3+2&2+1\end{pmatrix}=\begin{pmatrix}8&5\\5&3\end{pmatrix}$, equal to the computed $F^5$. The determinants give another check: $\det F=1\cdot0-1\cdot1=-1$, so $\det F^n=(-1)^n$, and for $F^5$ we get $8\cdot3-5\cdot5=24-25=-1$, as required (for $F^4$: $5\cdot2-9=1$). Finally, sympy confirmed the four matrices, and also $F^6=\begin{pmatrix}13&8\\8&5\end{pmatrix}$, which fits the pattern with $F_7=13$, $F_6=8$, $F_5=5$.

## Common mistakes

- Squaring the entries, for example writing $F^2=\begin{pmatrix}1&1\\1&0\end{pmatrix}$ again.
- Shifting the indices by one, such as claiming the top left entry of $F^n$ is $F_n$ instead of $F_{n+1}$.
- Writing the vector in the order $(b,a)^T$ and getting $(a+b,b)^T$ or other nonsense; the newer term must be on top.
- Believing that matching five powers proves the pattern, without the row argument (or induction) that explains why the pattern continues.

## How I would explain it in class

Multiplying by $F$ turns a pair $(a,b)$ into $(a+b,a)$, which is exactly one step of the Fibonacci rule: the sum becomes the new top term and the old top term moves down. Repeating this step $n$ times is multiplying by $F^n$, and that is why $F^2,\ldots,F^5$ are $\begin{pmatrix}2&1\\1&1\end{pmatrix}$, $\begin{pmatrix}3&2\\2&1\end{pmatrix}$, $\begin{pmatrix}5&3\\3&2\end{pmatrix}$, $\begin{pmatrix}8&5\\5&3\end{pmatrix}$, all filled with Fibonacci numbers. In general $F^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$.
