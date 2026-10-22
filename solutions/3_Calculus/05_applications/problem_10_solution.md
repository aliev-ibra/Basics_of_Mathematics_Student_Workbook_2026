# Problem 10

## The original problem

Point $A$ lies on one bank of a river of width $100$ m, and point $B$ lies on the other bank, $500$ m along the bank from the point directly opposite $A$.

The cost per meter of cable underwater is twice the cost per meter of cable on land.

Build a cost function depending on the point where the cable comes out of the water, determine the domain, and find the solution that minimizes the cost.

> **Why this problem:** it checks whether the student can independently translate a spatial description and two different costs into a single function to be optimized.

## What we are looking for

We lay a cable from $A$ to $B$. First it goes under the water across the river, then on land along the bank. We choose the landing point. If we land close to the opposite point, the water part is short but the land part is long. If we land near $B$, the land part is short but the water part is long. We want the landing point with the lowest total cost.

## The idea we need

First the model. Let $O$ be the point on the far bank directly opposite $A$. Let $x$ be the distance from $O$ to the landing point $P$, measured in metres along the bank towards $B$. Let $c$ be the cost of one metre of cable on land, so one metre under water costs $2c$. Then the cost is a function of $x$ only, and we use the derivative.

## Step-by-step solution

1. **Underwater part.** The segment $AP$ is the hypotenuse of a right triangle with legs $100$ and $x$:
$$
|AP|=\sqrt{100^2+x^2}=\sqrt{10\,000+x^2}.
$$

2. **Land part.** The distance from $P$ to $B$ along the bank is $500-x$.

3. **Cost function.**
$$
C(x)=2c\sqrt{10\,000+x^2}+c\,(500-x)=c\left(2\sqrt{10\,000+x^2}+500-x\right).
$$

4. **Domain.** The landing point lies between $O$ and $B$, so
$$
0\le x\le500.
$$

5. **Differentiate.** Since $c>0$ is a constant factor, we study
$$
f(x)=2\sqrt{10\,000+x^2}+500-x,\qquad f'(x)=\frac{2x}{\sqrt{10\,000+x^2}}-1.
$$

6. **Solve $f'(x)=0$.** Then $2x=\sqrt{10\,000+x^2}$. Both sides are non-negative, so we square: $4x^2=10\,000+x^2$, hence $3x^2=10\,000$ and
$$
x_0=\frac{100}{\sqrt3}=\frac{100\sqrt3}{3}\approx57{,}74\ \mathrm{m}.
$$
This is in the domain.

7. **Type of the point.**
$$
f''(x)=\frac{2\cdot10\,000}{(10\,000+x^2)^{3/2}}>0,
$$
so $f$ is convex and $x_0$ is the minimum.

8. **Endpoints.**
$$
f(0)=200+500=700,\qquad f(500)=2\sqrt{260\,000}\approx1019{,}80.
$$

9. **Minimal cost.** At $x_0$ the underwater length is $\sqrt{10\,000+10\,000/3}\approx115{,}47$ m, and
$$
f(x_0)=500+100\sqrt3\approx673{,}21.
$$

## Why each step is valid

- The river bank and the line from $A$ to $O$ are perpendicular, so the Pythagorean theorem is correct for $AP$.
- The cheapest path under water between two points is a straight segment, and on land it is the bank itself.
- The cost is a sum of length times price for each part, so the model has the right units: price times metres.
- The factor $c$ does not change where the minimum is, so we can drop it and later put it back.
- Squaring is safe in step 6 because both sides were non-negative, and the root found is positive.
- The derivative test finds the candidate only inside the domain. The endpoints must be checked separately, and here they are both higher. Convexity also shows that the single critical point is the global minimum.

## Final answer (in words)

The cost is
$$
C(x)=c\left(2\sqrt{10\,000+x^2}+500-x\right),\qquad 0\le x\le500\ \mathrm m,
$$
where $x$ is the distance of the landing point from the point opposite $A$. The cheapest solution is to land $x=\dfrac{100}{\sqrt3}\approx57{,}7$ m from the opposite point, with about $115{,}5$ m of cable under water and about $442{,}3$ m on land. The cost is then $(500+100\sqrt3)\,c\approx673{,}2\,c$, which is the cost of about $673$ m of land cable. At this point the underwater cable makes an angle of $30^\circ$ with the straight crossing $AO$, because $\sin\varphi=x_0/\sqrt{10\,000+x_0^2}=\tfrac12$.

## Verification

Costs in units of $c$:

| $x$ (m) | $f(x)$ |
|---|---|
| 0 | 700,00 |
| 30 | 678,81 |
| 50 | 673,61 |
| 57,74 | 673,21 |
| 65 | 673,54 |
| 100 | 682,84 |
| 200 | 747,21 |
| 500 | 1019,80 |

The values fall until about $57{,}7$ and then rise, and both endpoints are worse. The numbers were also checked by computer algebra (sympy), which gave the same critical point and the same values. Second method, a geometric check: let $\varphi$ be the angle between the underwater cable and the straight crossing $AO$. Then $\sin\varphi=x/\sqrt{10\,000+x^2}$, and the equation $f'(x)=0$ says exactly $2\sin\varphi=1$, so $\varphi=30^\circ$. Indeed $\tan30^\circ=57{,}74/100$.

## Common mistakes

- Using the distance $500$ for the water part, or forgetting that the land part is $500-x$.
- Putting the factor $2$ on the land part instead of the water part.
- Taking the domain as all real numbers and not checking the endpoints.
- Giving only $x$ and not saying what it measures.
- Landing at $B$ directly (straight line across) because it is the shortest path. It is shortest but not cheapest.

## How I would explain it in class

Let $x$ be the landing distance from the point opposite $A$; the water part is $\sqrt{10\,000+x^2}$ and the land part is $500-x$, so with land price $c$ the cost is $c(2\sqrt{10\,000+x^2}+500-x)$ for $0\le x\le500$. The derivative is zero when $2x=\sqrt{10\,000+x^2}$, which gives $x=100/\sqrt3\approx57{,}7$ m. The endpoints cost $700c$ and about $1020c$, while the optimum costs about $673{,}2c$, so it is the cheapest solution.
