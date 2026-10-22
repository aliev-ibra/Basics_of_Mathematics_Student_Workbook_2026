# Problem 13

## The original problem

The matrices
$$S=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad H=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$
describe nonuniform scaling and shear. For $T=HS$, find $T^{-1}$ in two ways:

1. first compute $T$, then its inverse,
2. use $(HS)^{-1}=S^{-1}H^{-1}$.

Compare the results. Additionally compute $H^{-1}S^{-1}$ and verify that the incorrect order gives a different matrix. Explain the rule: “when undoing a composition of operations, we undo them from the end.”

## What we are looking for

The inverse of the composite transformation $T=HS$, computed by two different routes that should agree. Then the product $H^{-1}S^{-1}$ in the wrong order, which must turn out to be a different matrix, and a plain-language explanation of why the order is reversed.

## The idea we need

The matrix $T=HS$ acts on a vector $v$ by first applying $S$ and then $H$: $Tv=H(Sv)$, because the matrix written closest to the vector acts first. To undo this we must first undo the last operation $H$ and then undo $S$, which is the rule
$$(HS)^{-1}=S^{-1}H^{-1}.$$
It holds because $(HS)(S^{-1}H^{-1})=H(SS^{-1})H^{-1}=HH^{-1}=I$. For a $2\times2$ matrix with $\det\neq0$ the inverse is $\frac1{\det}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.

## Step-by-step solution

**Step 1: compute $T$.**
$$T=HS=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}2&0\\0&1\end{pmatrix}=\begin{pmatrix}2&1\\0&1\end{pmatrix}.$$

**Step 2: method 1, invert $T$ directly.** $\det T=2\cdot1-1\cdot0=2\neq0$, so
$$T^{-1}=\frac12\begin{pmatrix}1&-1\\0&2\end{pmatrix}=\begin{pmatrix}\frac12&-\frac12\\0&1\end{pmatrix}.$$

**Step 3: method 2, invert the factors.** The inverse of the diagonal matrix $S$ has reciprocal diagonal entries, and the inverse of the shear $H$ has $-1$ in the corner (it shears back):
$$S^{-1}=\begin{pmatrix}\frac12&0\\0&1\end{pmatrix},\qquad H^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
Then in the reversed order
$$S^{-1}H^{-1}=\begin{pmatrix}\frac12&0\\0&1\end{pmatrix}\begin{pmatrix}1&-1\\0&1\end{pmatrix}=\begin{pmatrix}\frac12&-\frac12\\0&1\end{pmatrix}.$$

**Step 4: compare.** Both routes give the same matrix $\begin{pmatrix}\frac12&-\frac12\\0&1\end{pmatrix}$.

**Step 5: the wrong order.**
$$H^{-1}S^{-1}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}\frac12&0\\0&1\end{pmatrix}=\begin{pmatrix}\frac12&-1\\0&1\end{pmatrix}.$$
The entry in the upper right corner is $-1$ and not $-\frac12$, so this matrix is different from $T^{-1}$.

## Why each step is valid

- Method 1 uses only the $2\times2$ formula, and method 2 uses only the proven rule for the inverse of a product, so they are independent; their agreement is a genuine check.
- Matrix multiplication is not commutative, so $S^{-1}H^{-1}$ and $H^{-1}S^{-1}$ are allowed to differ, and Step 5 shows they do. Only one of them cancels correctly: $(HS)(S^{-1}H^{-1})$ has the inner pair $SS^{-1}$ next to each other, while $(HS)(H^{-1}S^{-1})$ would have $SH^{-1}$ in the middle, which does not cancel.
- The rule in words: $T$ means "first scale with $S$, then shear with $H$". To return to the starting point we must first remove the shear (the last thing done) and only then remove the scaling. This is the same as putting on socks and then shoes: to undo it we take off the shoes first.

## Final answer (in words)

The inverse of $T=HS$ is the inverse of $S$ times the inverse of $H$ in this order, and it equals
$$T^{-1}=S^{-1}H^{-1}=\begin{pmatrix}\frac12&-\frac12\\0&1\end{pmatrix},$$
the same as obtained by inverting $T=\begin{pmatrix}2&1\\0&1\end{pmatrix}$ directly. The wrong order gives $H^{-1}S^{-1}=\begin{pmatrix}\frac12&-1\\0&1\end{pmatrix}\neq T^{-1}$. When we undo a composition, we undo the last operation first.

## Verification

I multiply $T$ by the claimed inverse:
$$T\,T^{-1}=\begin{pmatrix}2&1\\0&1\end{pmatrix}\begin{pmatrix}\frac12&-\frac12\\0&1\end{pmatrix}=\begin{pmatrix}1&-1+1\\0&1\end{pmatrix}=I.$$
I multiply $T$ by the wrong-order matrix:
$$T\,(H^{-1}S^{-1})=\begin{pmatrix}2&1\\0&1\end{pmatrix}\begin{pmatrix}\frac12&-1\\0&1\end{pmatrix}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\neq I,$$
so the wrong order is not an inverse. Finally, an action test on the vector $v=(1,1)^T$: $Sv=(2,1)^T$, $H(Sv)=(3,1)^T$. Applying $T^{-1}$ gives $\left(\frac32-\frac12,\,1\right)^T=(1,1)^T=v$, so we are back at the start, while the wrong matrix gives $\left(\frac32-1,\,1\right)^T=\left(\frac12,1\right)^T\neq v$.

## Common mistakes

- Writing $(HS)^{-1}=H^{-1}S^{-1}$, keeping the original order.
- Inverting the shear as $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ again or forgetting the minus sign in $H^{-1}$.
- Computing $T=SH$ instead of $T=HS$ (the matrices do not commute: $SH=\begin{pmatrix}2&2\\0&1\end{pmatrix}$).
- Concluding that because the two orders look similar they are the same matrix; one entry differs.

## How I would explain it in class

$T=HS$ first scales and then shears, so to go back I must first un-shear and then un-scale, which gives $T^{-1}=S^{-1}H^{-1}$. Both direct inversion of $T=\begin{pmatrix}2&1\\0&1\end{pmatrix}$ and this product give $\begin{pmatrix}\frac12&-\frac12\\0&1\end{pmatrix}$, while the wrong order $H^{-1}S^{-1}$ gives $\begin{pmatrix}\frac12&-1\\0&1\end{pmatrix}$. The vector $(1,1)$ returns to itself under the right inverse and not under the wrong one, just like taking off shoes before socks.
