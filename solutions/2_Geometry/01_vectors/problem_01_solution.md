# Problem 01

## The original problem
For $u=(2,-1,3)$ and $v=(-1,4,2)$ compute
$$u+v,\qquad u-v,\qquad 3u-2v.$$
Then verify that $(u+v)-v=u$, and explain geometrically what adding two vectors means.

## What we are looking for
We need the three vector results from componentwise operations, an algebraic verification of the identity $(u+v)-v=u$ (showing that subtracting $v$ cancels adding $v$), and a short geometric explanation of vector addition. All answers must be in $\mathbb{R}^3$ since both vectors have three components.

## The idea we need
The idea is componentwise addition/subtraction and scalar multiplication in $\mathbb{R}^n$. For $u=(u_1,u_2,u_3), v=(v_1,v_2,v_3)$, we have $u+v=(u_1+v_1,u_2+v_2,u_3+v_3)$, $u-v=(u_1-v_1,u_2-v_2,u_3-v_3)$, and $\lambda u = (\lambda u_1,\lambda u_2,\lambda u_3)$.  
Geometrically, placing the tail of $v$ at the tip of $u$ gives the tip of $u+v$ (the triangle/ parallelogram rule); adding $v$ then subtracting $v$ brings us back to $u$ (translation by $v$ is invertible by $-v$).

## Step-by-step solution

1. **Compute $u+v$ (componentwise):**  
   $u+v = (2 + (-1),\ -1 + 4,\ 3 + 2) = (1,\ 3,\ 5)$.
   (We add corresponding components.)

2. **Compute $u-v$ (componentwise):**  
   $u-v = (2 - (-1),\ -1 - 4,\ 3 - 2) = (2+1,\ -5,\ 1) = (3,\ -5,\ 1)$.
   (Subtracting $v$ is the same as adding $-v$ componentwise.)

3. **Compute $3u - 2v$ (scalar multiply, then subtract):**  
   First $3u = (3\cdot 2,\ 3\cdot (-1),\ 3\cdot 3) = (6,\ -3,\ 9)$.  
   Then $2v = (2\cdot (-1),\ 2\cdot 4,\ 2\cdot 2) = (-2,\ 8,\ 4)$, so $-2v = - (2v) = (2,\ -8,\ -4)$ (or compute directly).  
   Thus $3u - 2v = (6 - (-2),\ -3 - 8,\ 9 - 4) = (6+2,\ -11,\ 5) = (8,\ -11,\ 5)$.

4. **Verify $(u+v)-v = u$:**  
   From step 1, $u+v = (1,3,5)$. Then $(u+v)-v = (1 - (-1),\ 3 - 4,\ 5 - 2) = (1+1,\ -1,\ 3) = (2,\ -1,\ 3) = u$.  
   (Componentwise subtraction cancels componentwise addition.)

## Why each step is valid

- **Componentwise operations:** in the standard Cartesian coordinates of $\mathbb{R}^3$, vector addition, subtraction, and scalar multiplication are defined componentwise.
- **Scalar multiplication first:** $3u-2v = 3u + (-2)v$ by distributivity of scalar multiplication over addition; we form $-2v$ componentwise.
- **Verification:** associativity/distributivity of these componentwise operations gives $(u+v)-v = u + (v-v)=u+0=u$; doing componentwise confirms it directly.

## Final answer (in words)
In plain words: adding $u$ and $v$ gives a vector whose components are the sums; subtracting gives differences; $3u-2v$ is three times $u$ minus twice $v$. Geometrically, placing $v$ at the tip of $u$ produces $u+v$ (tip-to-tail) — so adding $v$ then removing $v$ returns to the original position.  
In symbols: $u+v=(1,3,5),\ u-v=(3,-5,1),\ 3u-2v=(8,-11,5),\ (u+v)-v=(2,-1,3)=u$.

## Verification
We recomputed each component carefully: for $u+v$ second component $-1+4=3$ OK. For $u-v$ first component $2 - (-1)=3$ OK. For $3u-2v$, $3u=(6,-3,9)$, $2v=(-2,8,4)$, difference $(6 - (-2), -3-8, 9-4)=(8,-11,5)$ OK. The identity check gave back exactly $u=(2,-1,3)$ OK. All in $\mathbb{R}^3$ as given.

## Common mistakes
- **Sign errors:** forgetting that $u-v = (u_1-v_1,\ldots)$ (especially when $v_i$ negative, like $2 - (-1)$).
- **Scalar order:** writing $(3u)- (2v)$ vs confusing coefficients.
- **Thinking geometrically vaguely:** saying "they add up" without mentioning tip-to-tail/parallelogram or the translation interpretation.
- **Dropping components:** treating in 2D by mistake (here all three matter).

## How I would explain it in class
In component form, we just add or subtract corresponding entries and multiply each entry by the scalar.  
Geometrically, adding $v$ to $u$ means placing the tail of $v$ at the tip of $u$ to get the resultant vector $u+v$ (the parallelogram/tip-to-tail rule).  
Finally, subtracting $v$ undoes that translation, which is exactly what $(u+v)-v=u$ shows both algebraically and geometrically.
