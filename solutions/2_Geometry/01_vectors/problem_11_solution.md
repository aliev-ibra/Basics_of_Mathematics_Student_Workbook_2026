# Problem 11

## The original problem

Decompose $u=(3,4)$ into components parallel and perpendicular to $v=(1,2)$. Check
$$u=u_{\parallel}+u_{\perp},\qquad u_{\perp}\cdot v=0.$$
Explain why these are two independent checks of correctness.

## What we are looking for

We need to split $u$ into two pieces. One piece, $u_\parallel$, lies along the direction of $v$. The other piece, $u_\perp$, makes a right angle with $v$. The two pieces must add up to $u$. We must also explain why the two checks catch different kinds of mistakes.

## The idea we need

Think of $v$ as a line through the origin and of $u$ as an arrow. The shadow that $u$ casts on this line, when the light falls at a right angle to the line, is the parallel part $u_\parallel$. It is called the projection of $u$ onto $v$. It is a multiple of $v$:
$$u_\parallel=\frac{u\cdot v}{v\cdot v}\,v.$$
The number $u\cdot v$ is the dot product, and $v\cdot v=\|v\|^2$ is the squared length of $v$. The rest of the arrow, $u_\perp=u-u_\parallel$, joins the tip of the shadow to the tip of $u$, and it meets the line at a right angle.

## Step-by-step solution

**Step 1: dot products.**
$$u\cdot v=3\cdot1+4\cdot2=11,\qquad v\cdot v=1\cdot1+2\cdot2=5.$$

**Step 2: the multiplier.** The projection is the number $\frac{11}{5}$ times $v$.

**Step 3: the parallel part.**
$$u_\parallel=\frac{11}{5}(1,2)=\left(\frac{11}{5},\frac{22}{5}\right).$$

**Step 4: the perpendicular part.** We subtract the shadow from $u$.
$$u_\perp=u-u_\parallel=\left(3-\frac{11}{5},\;4-\frac{22}{5}\right)=\left(\frac45,-\frac25\right).$$

**Step 5: check 1, the sum.**
$$u_\parallel+u_\perp=\left(\frac{11}{5}+\frac45,\;\frac{22}{5}-\frac25\right)=(3,4)=u.$$

**Step 6: check 2, perpendicularity.**
$$u_\perp\cdot v=\frac45\cdot1+\left(-\frac25\right)\cdot2=\frac45-\frac45=0.$$

## Why each step is valid

- The formula in Step 3 comes from asking for the multiple $t\,v$ such that $u-tv$ is perpendicular to $v$. That requires $(u-tv)\cdot v=0$, so $u\cdot v=t\,(v\cdot v)$, which gives $t=\frac{u\cdot v}{v\cdot v}$.
- In Step 4 we define $u_\perp$ as what is left over, so $u=u_\parallel+u_\perp$ is true by construction.
- The two checks are independent in the following sense. The sum in Step 5 is a statement about adding. The perpendicularity in Step 6 is a statement about angles. Suppose I had used a wrong multiplier, say $2$ instead of $\frac{11}{5}$. Then $u_\perp=u-2v=(1,0)$ would still satisfy $u_\parallel+u_\perp=u$, but $u_\perp\cdot v=1\neq0$. So the sum check alone cannot find that error, and the dot product check does.
- In the other direction, perpendicularity alone does not tell us that the pieces add back to $u$. The zero vector is perpendicular to $v$, but it is certainly not the leftover piece of $u$. Only both conditions together say that the two pieces are the correct ones. The decomposition is also unique, because the multiplier $t$ is forced by the perpendicularity condition.

## Final answer (in words)

The part of $u$ along $v$ is $u_\parallel=\left(\frac{11}{5},\frac{22}{5}\right)$, which equals $\frac{11}{5}v$. The part of $u$ at a right angle to $v$ is $u_\perp=\left(\frac45,-\frac25\right)$. Together
$$u=\left(\frac{11}{5},\frac{22}{5}\right)+\left(\frac45,-\frac25\right),\qquad u_\perp\cdot v=0.$$

## Verification

The two checks of the exercise are done in Steps 5 and 6. Here is a third check that does not reuse the projection formula. The vector $(2,-1)$ is perpendicular to $v=(1,2)$, because $2\cdot1+(-1)\cdot2=0$. In the plane, the perpendicular part must be a multiple of $(2,-1)$, and the multiplier is $\frac{u\cdot(2,-1)}{(2,-1)\cdot(2,-1)}=\frac{6-4}{5}=\frac25$. So $u_\perp=\frac25(2,-1)=\left(\frac45,-\frac25\right)$, which matches. Finally, the Pythagorean theorem must hold, because the two pieces are at a right angle. We compute $\|u_\parallel\|^2=\frac{121}{25}+\frac{484}{25}=\frac{605}{25}=\frac{121}{5}$ and $\|u_\perp\|^2=\frac{16}{25}+\frac{4}{25}=\frac45$. The sum is $\frac{125}{5}=25=\|u\|^2$.

## Common mistakes

- Dividing by $\|v\|$ instead of $v\cdot v=\|v\|^2$ in the projection formula.
- Computing only the parallel part and forgetting to subtract it from $u$.
- Checking only the sum $u_\parallel+u_\perp=u$, which is automatic, and skipping the dot product check.
- Mixing up the order and projecting $v$ onto $u$ instead of $u$ onto $v$.

## How I would explain it in class

The parallel part is the shadow of $u$ on the line of $v$, which is $\frac{u\cdot v}{v\cdot v}v=\frac{11}{5}(1,2)=\left(\frac{11}{5},\frac{22}{5}\right)$, and the perpendicular part is what is left, $\left(\frac45,-\frac25\right)$. The sum check shows that nothing was lost, and the dot product $u_\perp\cdot v=0$ shows that the leftover really is at a right angle. They are independent because a wrong multiplier would still pass the sum check but would fail the perpendicularity check.
