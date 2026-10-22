# Problem 03

## The original problem
For $v=(3,4)$ find a unit vector $e$ with the same direction and orientation. Check that $\|e\|=1$, reconstruct $v$ in the form $v=\|v\|e$, and explain what changes during normalization and what remains unchanged.

## What we are looking for
We need the unit vector in direction of $v$ (in $\mathbb{R}^2$), verification $\|e\|=1$, the reconstruction $v=\|v\|e$, and an explanation distinguishing what changes (length/scaling factor) from what remains unchanged (direction and orientation).

## The idea we need
A unit vector has length 1. To get a unit vector in the same direction and orientation as a nonzero vector $v$, we normalize:
$$
e = \frac{v}{\|v\|}, \qquad \text{provided } v \neq 0.
$$
The Euclidean norm in $\mathbb{R}^2$ is $\|v\|=\sqrt{v_1^2+v_2^2}$. Normalization scales the vector by $1/\|v\|$ so its magnitude becomes 1 but its direction (and orientation along that direction) stays the same; any nonzero $v$ decomposes as $v=\|v\|\, e$ with $\|e\|=1$.

## Step-by-step solution

1. **Compute the length of $v$:**
   $\|v\| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5$.
   (We use the Pythagorean norm in $\mathbb{R}^2$.)

2. **Find the unit vector $e$ in the same direction and orientation:**
   $e = \frac{v}{\|v\|} = \frac{1}{5}(3,4) = \left(\frac{3}{5}, \frac{4}{5}\right)$.
   (Divide each component by the positive scalar $\|v\|$ so orientation is preserved.)

3. **Check that $\|e\|=1$:**
   $\|e\| = \sqrt{(3/5)^2 + (4/5)^2} = \sqrt{\frac{9}{25} + \frac{16}{25}} = \sqrt{\frac{25}{25}} = \sqrt{1} = 1$.
   (Independent check by norm of $e$.)

4. **Reconstruct $v$ in the form $v=\|v\|e$:**
   $\|v\| e = 5 \cdot \left(\frac{3}{5}, \frac{4}{5}\right) = (3,4) = v$.
   (This confirms the decomposition into magnitude and unit direction.)

## Why each step is valid

- **Length first:** we need the scale factor to make magnitude 1.
- **Division by positive scalar:** scaling by a positive number preserves direction and orientation; dividing by $\|v\|>0$ gives magnitude $\|v\|/\|v\|=1$.
- **Norm of $e$:** squaring components gives sum 1, so root is 1.
- **Decomposition:** $e=v/\|v\| \implies v=\|v\|e$ by multiplying both sides by $\|v\|$.

## Final answer (in words)
In plain words: the direction is preserved and orientation unchanged, but the vector becomes length 1. The original vector is just that unit direction scaled by its length 5.  
In symbols: $\|v\|=5,\ e=\left(\frac{3}{5},\frac{4}{5}\right),\ \|e\|=1,\ v=5\cdot \left(\frac{3}{5},\frac{4}{5}\right)$.

## Verification
We checked $\|e\|^2 = 9/25+16/25=1$ independently of step 1 OK. Reconstruction multiplies back to $(3,4)$ exactly OK. All in $\mathbb{R}^2$ as given.

## Common mistakes
- **Forgetting to divide:** giving $v$ itself as unit vector.
- **Sign/orientation errors:** dividing by $-\|v\|$ would reverse direction (bad here since we want same direction/orientation).
- **Arithmetic:** $3^2+4^2=25$ not 7 etc.
- **Confusing direction with vector:** normalization gives direction info encoded in unit vector, magnitude is separate.

## How I would explain it in class
Normalization means we keep the ray direction the same but rescale so the vector has length exactly 1.  
We do this by dividing by the original length, which is 5 here, giving $(3/5,4/5)$.  
What stays is the direction and orientation; what changes is the scale factor from 5 down to 1, and we can always recover the original as length times that unit vector.
