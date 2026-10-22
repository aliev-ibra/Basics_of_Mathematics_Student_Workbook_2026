# Problem 07

## The original problem
Given
$$u=(1,2,3),\qquad v=(2,4,6),\qquad w=(0,1,1).$$
Identify a specific relation between $u$ and $v$, decide whether the three vectors can be linearly independent, and explain why no long calculation is needed.

## What we are looking for
We need to spot the relation between $u,v$ (scalar multiple), the conclusion about linear independence of the triple, and the reasoning (structure/recognition before computation).

## The idea we need
Vectors are linearly dependent if there exist scalars not all zero with $\alpha_1 x_1 + \alpha_2 x_2 + \alpha_3 x_3 = 0$. A sufficient obvious case: one vector is a scalar multiple of another (and both nonzero) => the pair is linearly dependent => any larger set containing that pair is linearly dependent. Also in $\mathbb{R}^3$ you cannot have 4 independent vectors etc, but more directly here the relation is visible.  
Conditions: real scalars (usual), Euclidean space.

## Step by step solution

1. **Identify relation between $u$ and $v$:**
   Notice $v = (2,4,6) = 2\cdot (1,2,3) = 2u$.
   So $v$ is exactly 2 times $u$ (same direction, different length; $u \neq 0$).

2. **Decide about linear independence of all three:**
   Since $v = 2u$, we have $2u + (-1)v + 0\cdot w = (0,0,0)$ and the coefficients $(2, -1, 0)$ are not all zero. Therefore the three vectors $u,v,w$ are linearly dependent.

3. **Explain why no long calculation is needed:**
   Linear dependence of a set is already established if any nontrivial linear combination gives zero. Spotting $v=2u$ gives such a combination immediately without setting up and solving a full system for all three.

## Why each step is valid

- **Scalar multiple:** componentwise equality is easy to check.
- **Dependence criterion:** if some $x_i = \sum_{j\neq i}\beta_j x_j$ (or simply a multiple) then $\sum \alpha_k x_k=0$ nontrivially.
- **Set containing dependent pair:** if a subset is linearly dependent, the whole set is linearly dependent.

## Final answer (in words)
In plain words: $v$ is twice $u$, so $u$ and $v$ point in the same direction (linearly dependent as a pair). Adding any third vector $w$ cannot make the triple independent — having a dependent pair already means there is a nontrivial combination giving zero. No system of equations is needed because the structure is obvious.  
In symbols: $v = 2u \implies 2u - 1v + 0w = 0$, coefficients not all zero => $\{u,v,w\}$ linearly dependent.

## Verification
Check components: $2*1=2, 2*2=4, 2*3=6$ matches $v$ exactly OK. The combination gives zero vector OK.

## Common mistakes
- **Saying independent because $w$ different:** adding another vector doesn't remove dependence if a pair is dependent.
- **Thinking only triples can be independent in $\mathbb{R}^3$:** independence is a property of the set; but having a dependent pair forces dependence regardless of dimension count except trivial edge cases.
- **Missing the coefficient zero:** we must include all three vectors in the combination (with coefficient 0 for $w$).

## How I would explain it in class
I notice right away that $v = 2u$, so one is a scalar multiple of the other — that already means the pair is linearly dependent.  
A set containing a linearly dependent subset is itself linearly dependent, so adding $w$ doesn't help.  
Because of that structure, I don't need to solve equations; the relation $2u - v = 0$ is enough to show dependence.
