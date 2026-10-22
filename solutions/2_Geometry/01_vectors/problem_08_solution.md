# Problem 08

## The original problem
Check whether $w=(5,1)$ can be written as
$$w=au+bv,$$
where $u=(1,1)$ and $v=(2,-1)$. If so, find $a,b$, reconstruct $w$ from them, and explain the geometric meaning of the existence of such coefficients.

## What we are looking for
We need to set up the component equations in $\mathbb{R}^2$, solve for scalars $a,b$, reconstruct $w=au+bv$ to verify, and give geometric meaning (basis/ span of $\mathbb{R}^2$, directions form a basis so any vector is a unique linear combination).

## The idea we need
$w = a u + b v$ means
$$
\begin{bmatrix}
w_1\\ w_2
\end{bmatrix}
=
a\begin{bmatrix}
u_1\\ u_2
\end{bmatrix}
+
b\begin{bmatrix}
v_1\\ v_2
\end{bmatrix}
=
\begin{bmatrix}
u_1 & v_1\\ 
u_2 & v_2
\end{bmatrix}
\begin{bmatrix}
a\\ b
\end{bmatrix}.
$$
So componentwise:
$a\cdot 1 + b\cdot 2 = a + 2b = 5$,
$a\cdot 1 + b\cdot (-1) = a - b = 1$.
Geometrically, $u,v$ are directions; if they are linearly independent and span $\mathbb{R}^2$ (form a basis), then every vector $w\in\mathbb{R}^2$ can be written uniquely as $au+bv$ (as a combination of those two directions).

## Step-by-step solution

1. **Set up equations:**
   $w = a u + b v = a(1,1) + b(2,-1) = (a + 2b,\ a - b) = (5,1)$.
   Thus:
   (1) $a + 2b = 5$
   (2) $a - b = 1$

2. **Solve the system:**
   From (2): $a = b + 1$.
   Substitute into (1): $(b+1) + 2b = 5 \implies 3b + 1 = 5 \implies 3b = 4 \implies b = 4/3$.
   Then $a = b + 1 = 4/3 + 1 = 7/3$.

3. **Reconstruct $w$ from $a,b$:**
   $a u + b v = \frac{7}{3}(1,1) + \frac{4}{3}(2,-1) = \left(\frac{7}{3} + \frac{8}{3},\ \frac{7}{3} - \frac{4}{3}\right) = \left(\frac{15}{3},\ \frac{3}{3}\right) = (5,1) = w$.
   (Independent reconstruction matches exactly.)

## Why each step is valid

- **Componentwise equality:** $(x1,x2)=(y1,y2) \iff x1=y1 \land x2=y2$.
- **Linear system solution:** substituting is valid algebra.
- **Reconstruction:** verifies by computing the linear combination with found coefficients (a strong check).

## Final answer (in words)
In plain words: yes, it is possible. The coefficients are $a=7/3, b=4/3$. Geometrically, since $u=(1,1)$ and $v=(2,-1)$ are not scalar multiples of each other in $\mathbb{R}^2$, they form a basis and span the whole plane, so any vector (including $(5,1)$) can be written as a unique combination giving how much to go in direction $u$ and how much in direction $v$.  
In symbols: $a=\frac{7}{3}, b=\frac{4}{3},\ \frac{7}{3}(1,1)+\frac{4}{3}(2,-1)=(5,1)=w$.

## Verification
From equations: (2): $a-b=7/3 - 4/3=3/3=1$ OK. (1): $a+2b=7/3 + 8/3=15/3=5$ OK. Reconstruction gives $(5,1)$ OK. Coeffs are unique for a basis.

## Common mistakes
- **Wrong sign/substitution:** errors solving $a-b=1, a+2b=5$.
- **Not reconstructing:** solving is necessary but the problem says "reconstruct $w$ from them" so verification required.
- **Saying "any two vectors work":** need linear independence (here yes, not multiples).
- **Forgetting geometric meaning:** the question explicitly asks for it.

## How I would explain it in class
We write $(5,1)=a(1,1)+b(2,-1)$ and get two equations: $a+2b=5, a-b=1$. Solving gives $a=7/3, b=4/3$.  
Plugging back gives exactly $(5,1)$, so it works.  
Geometrically, $u$ and $v$ point in different directions and aren't multiples, so together they span $\mathbb{R}^2$ like a new coordinate system — any point in the plane is a unique combination of these two direction vectors.
