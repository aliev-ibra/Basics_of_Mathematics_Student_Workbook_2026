# Problem 05

## The original problem
Given $u=(1,1,0)$ and $v=(1,0,1)$:

1. Use the sign of $u\cdot v$ to predict the type of angle.
2. Compute the angle.
3. Compare the result with the prediction.

## What we are looking for
We need the sign-based prediction (acute/right/obtuse) using the dot product, the actual angle $\theta=\arccos\frac{u\cdot v}{\|u\|\|v\|}$ (in a standard form, probably degrees or just the exact value in terms of inverse trig), and comparison.

## The idea we need
For nonzero vectors, $u\cdot v = \|u\|\|v\|\cos\theta$ with $\theta \in (0,\pi]$ (the angle between vectors taken as the smaller one usually, $0<\theta\le \pi$). Therefore:
- $u\cdot v > 0 \implies \cos\theta > 0 \implies \theta$ acute ($0<\theta<\pi/2$)
- $u\cdot v = 0 \implies \theta = \pi/2$ (perpendicular)
- $u\cdot v < 0 \implies \cos\theta < 0 \implies \theta$ obtuse ($\pi/2 < \theta < \pi$)

Conditions: Euclidean dot product and Euclidean norms in Cartesian coordinates; angle between vectors as defined above.

## Step-by-step solution

1. **Use sign of $u\cdot v$ to predict angle type:**
   Compute $u\cdot v = 1\cdot 1 + 1\cdot 0 + 0\cdot 1 = 1 + 0 + 0 = 1$.
   Since $u\cdot v = 1 > 0$, we predict the angle between $u$ and $v$ is acute ($0 < \theta < \pi/2$).

2. **Compute the angle:**
   Compute norms:
   $\|u\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$.
   $\|v\| = \sqrt{1^2 + 0^2 + 1^2} = \sqrt{2}$.
   Then
   $$\cos\theta = \frac{u\cdot v}{\|u\|\|v\|} = \frac{1}{\sqrt{2}\cdot \sqrt{2}} = \frac{1}{2}.$$
   Thus $\theta = \arccos(1/2) = \frac{\pi}{3}$ radians (60 degrees).

3. **Compare with prediction:**
   $\pi/3$ radians = 60° is acute, which matches the prediction from $u\cdot v > 0$.

## Why each step is valid

- **Sign rule:** follows directly from $u\cdot v=\|u\|\|v\|\cos\theta$ and $\|u\|\|v\|>0$ for nonzero vectors.
- **Norms:** Euclidean lengths via Pythagorean theorem.
- **Angle formula:** the standard formula relating dot product, norms, and the angle between vectors (defined in the plane/space spanned by them).
- **Arccos:** gives the unique angle in $(0,\pi]$ with that cosine.

## Final answer (in words)
In plain words: since the dot product is positive (1), the angle between the vectors is acute; computing gives $\cos\theta=1/2$ so the angle is 60 degrees ($\pi/3$ radians), which matches.  
In symbols: $u\cdot v=1>0 \implies \theta$ acute, $\cos\theta=\frac{1}{\sqrt{2}\sqrt{2}}=\frac{1}{2},\ \theta=\frac{\pi}{3}$.

## Verification
Recomputed $u\cdot v$: $1*1 + 1*0 + 0*1 = 1$ OK. Norms $\sqrt{1+1}=\sqrt{2}, \sqrt{1+1}=\sqrt{2}$ OK. Product denominator 2 OK. $\arccos(1/2)=\pi/3$ is a standard value OK.

## Common mistakes
- **Forgetting absolute value/sign logic:** confusing the sign.
- **Using degrees/radians inconsistently:** either form is fine if stated; better give exact in terms of inverse trig or standard angle.
- **Computing norms wrong:** missing a square.
- **Assuming the acute angle without computing:** the problem says "Use the sign..." first (prediction) then compute (exact) then compare.

## How I would explain it in class
Before calculating, the dot product tells us the sign of $\cos\theta$: here it's positive, so the angle must be less than 90 degrees.  
Then we compute norms and get $\cos\theta = 1/2$, so the angle is exactly 60 degrees.  
This matches perfectly — the sign gave us a quick qualitative prediction, and the formula gave the precise angle.
