# Problem 06

## The original problem

Reduce

$$4x^2+9y^2-16x+18y-11=0$$

to canonical form. Give the center and semiaxis lengths. Check that substituting the coordinates of the center into the left-hand side gives a value consistent with the form you obtained.

## What we are looking for

We want the canonical ellipse equation, its center, and its semi-axis lengths.

## The idea we need

Group and complete the square for both $x$ and $y$, then divide to get $\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=1$.

## Step-by-step solution

Group:

$$4x^2-16x+9y^2+18y=11.$$

Factor:

$$4(x^2-4x)+9(y^2+2y)=11.$$

Complete the square:

$$4((x-2)^2-4)+9((y+1)^2-1)=11.$$

Expand:

$$4(x-2)^2-16+9(y+1)^2-9=11.$$

Move constants:

$$4(x-2)^2+9(y+1)^2=36.$$

Divide by $36$:

$$\frac{(x-2)^2}{9}+\frac{(y+1)^2}{4}=1.$$

Center: $(2,-1)$. Semi-axes: $a=3$, $b=2$.

Substitute the center into the original left-hand side:

$$4(2)^2+9(-1)^2-16(2)+18(-1)-11=16+9-32-18-11=-36.$$

This equals $-36$, which is the negative of the constant moved to the right; it is consistent with the completed-square form.

## Why each step is valid

Factoring before completing the square keeps the leading coefficients correct. Dividing by $36$ normalizes the right-hand side to $1$, matching the canonical ellipse form.

## Final answer (in words)

The ellipse has center $(2,-1)$ and semi-axes $3$ and $2$. Its canonical equation is $\frac{(x-2)^2}{9}+\frac{(y+1)^2}{4}=1$.

## Verification

Expand $\frac{(x-2)^2}{9}+\frac{(y+1)^2}{4}=1$ by multiplying by $36$: $4(x-2)^2+9(y+1)^2=36$, which expands to $4x^2+9y^2-16x+18y-11=0$. This matches the original.

## Common mistakes

- Forgetting to divide the completed square by the leading coefficient.
- Sign error: center is $(2,-1)$, not $(2,1)$.
- Not checking the center substitution.

## How I would explain it in class

I complete the square carefully, keeping the coefficients $4$ and $9$ outside. Then I divide to get the canonical ellipse form and read the center and semi-axes. Expanding back confirms the algebra.