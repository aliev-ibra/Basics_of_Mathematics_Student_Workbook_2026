# Problem 02

## The original problem
The points are $A=(1,2,3)$ and $B=(4,-2,6)$.

1. Construct $\overrightarrow{AB}$.
2. Compute its length.
3. Compute the distance between the points using the coordinate formula.
4. Explain why both calculations give the same result.

## What we are looking for
We need $\overrightarrow{AB}$ as the vector from $A$ to $B$, its Euclidean length $\|\overrightarrow{AB}\|$, the point-to-point distance via the coordinate distance formula in $\mathbb{R}^3$, and the explanation of why these coincide (they are the same quantity: length of the difference vector).

## The idea we need
For two points in $\mathbb{R}^n$, $\overrightarrow{AB} = B - A = (B_1-A_1,\ldots,B_n-A_n)$. The Euclidean length (norm) is
$$
\|x\| = \sqrt{x_1^2 + x_2^2 + x_3^2}, \qquad x\in\mathbb{R}^3.
$$
The distance between points $A,B$ is defined as $d(A,B)=\|B-A\|=\|\overrightarrow{AB}\|$. This holds in any dimension with the Euclidean norm (a consequence of the Pythagorean theorem / definition of length in Cartesian coordinates).

## Step-by-step solution

1. **Construct $\overrightarrow{AB}$:**  
   $\overrightarrow{AB} = B - A = (4-1,\ -2-2,\ 6-3) = (3,\ -4,\ 3)$.
   (We subtract coordinates of the tail $A$ from the head $B$.)

2. **Compute its length:**  
   $\|\overrightarrow{AB}\| = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9 + 16 + 9} = \sqrt{34}$.
   (Square each component, sum, take non-negative square root.)

3. **Compute distance using the coordinate formula:**  
   $d(A,B)=\sqrt{(4-1)^2 + (-2-2)^2 + (6-3)^2} = \sqrt{3^2 + (-4)^2 + 3^2} = \sqrt{9+16+9}=\sqrt{34}$.
   (The coordinate distance formula is exactly the same expression.)

4. **Explanation:**  
   Both give the same result because the coordinate distance formula is defined as the Euclidean length of the displacement vector $\overrightarrow{AB}=B-A$. The Pythagorean theorem gives the length of a straight segment as that square root; in Cartesian coordinates we write the segment's vector components as differences of coordinates and take the same norm.

## Why each step is valid

- **Vector from $A$ to $B$:** in position-vector terms, moving from point $A$ (with position vector $A$) to $B$ gives displacement $B-A$.
- **Norm definition:** $\|x\|^2 = x\cdot x = \sum x_i^2$ is the squared Euclidean length.
- **Distance formula identity:** $d(A,B)=\sqrt{\sum (B_i-A_i)^2}=\|B-A\|=\|\overrightarrow{AB}\|$ by definition of both the formula and the norm.

## Final answer (in words)
In plain words: the vector from $A$ to $B$ is $(3,-4,3)$, its length is $\sqrt{34}$, and the straight-line distance between $A$ and $B$ is also $\sqrt{34}$. Geometrically, distance between points is the length of the shortest (straight) path, which is exactly the magnitude of the displacement vector.  
In symbols: $\overrightarrow{AB}=(3,-4,3),\ \|\overrightarrow{AB}\|=\sqrt{34},\ d(A,B)=\sqrt{34}$.

## Verification
We recomputed squares: $3^2=9, (-4)^2=16, 3^2=9$, sum $34$ OK. Both formulas used identical differences $(3,-4,3)$ under sqrt OK. Length is positive and matches point distance OK.

## Common mistakes
- **Direction confusion:** writing $\overrightarrow{BA}=A-B$ instead of $\overrightarrow{AB}=B-A$ (length same but vector reversed).
- **Forgetting squares:** dropping squares or square root.
- **Sign inside:** $(-4)^2$ must be positive.
- **Thinking of different norms:** in Euclidean (standard) geometry this identity holds; the problem states coordinates so Euclidean norm is intended.

## How I would explain it in class
The displacement from $A$ to $B$ is just $B$ minus $A$, so $\overrightarrow{AB}=(3,-4,3)$.  
By the Pythagorean theorem, the straight-line distance is the square root of the sum of squares of those components, which is the same formula as the coordinate distance.  
Thus, the point distance and the length of the difference vector are identical because they are both measuring the same Euclidean length.
