# Problem 12

## The original problem

A museum wants to create a rectangular exhibition room next to an existing straight wall. The side along the wall does not need to be built. The remaining three sides are to be constructed to two different standards: the two sides perpendicular to the wall cost $300\ \mathrm{PLN/m}$ each, while the side parallel to the wall costs $500\ \mathrm{PLN/m}$. The budget is $30\,000\ \mathrm{PLN}$.

Build a model that maximizes the area of the room and prepare a complete analysis containing:

- definition of variables and units,
- mathematical model,
- domain resulting from the problem statement,
- computation of the derivative,
- determination and verification of the optimum,
- interpretation of the result,
- graph of the objective function,
- numerical verification of several values near the optimum found.

Finally, indicate which part of the solution required modeling the problem and which part was only the execution of the calculation. Produce the graph and computer calculations only after completing the mathematical solution, and treat them as verification.

> **Why this problem:** it checks full transfer to a new problem with unequal side costs and integrates the process from model construction to independent verification.

## What we are looking for

We build three walls of a rectangular room, and the fourth side is the old wall. The two walls that meet the old wall at a right angle cost less per metre than the wall parallel to it. We have a fixed budget. We want the dimensions that give the largest floor area, and then a check of the result with a table and a graph.

## The idea we need

This is a problem with a budget. First we name the unknown lengths and write the cost. The budget links the two lengths, so we can remove one and get a function of a single variable. Only then do we use the derivative. The computer comes last, as a check.

## Step-by-step solution

**Part A. Modelling.**

1. **Variables and units.** Let $x$ be the length of one wall perpendicular to the old wall, in metres. Let $y$ be the length of the wall parallel to the old wall, in metres. The area is $A$, in square metres.

2. **Area.** The room is a rectangle, so
$$
A=xy.
$$

3. **Cost.** Two walls of length $x$ cost $300$ PLN per metre, and one wall of length $y$ costs $500$ PLN per metre:
$$
600x+500y\ \text{PLN}.
$$

4. **Budget.** We spend the whole budget:
$$
600x+500y=30\,000,\qquad\text{so}\qquad y=60-1{,}2x.
$$

5. **Objective function.** Put $y$ into the area:
$$
A(x)=x(60-1{,}2x)=60x-1{,}2x^2\quad[\mathrm{m^2}].
$$

6. **Domain.** Both lengths must be positive: $x>0$ and $y>0$. The second gives $60-1{,}2x>0$, so $x<50$. The domain is
$$
0<x<50\ \mathrm m.
$$

**Part B. Calculation.**

7. **Derivative.**
$$
A'(x)=60-2{,}4x.
$$

8. **Critical point.** $A'(x)=0$ gives $x=25$.

9. **Type of the point.** $A''(x)=-2{,}4<0$, so the graph is a parabola opening downwards and $x=25$ is a maximum. Near the ends of the domain $A\to0$.

10. **The other side and the area.**
$$
y=60-1{,}2\cdot25=30,\qquad A=25\cdot30=750.
$$

## Why each step is valid

- The whole budget is spent in the best solution. If some money were left, we could lengthen a wall and get more area, so the optimum cannot be strictly below the budget. This is why we use an equation and not an inequality.
- Cost equals price per metre times metres for each wall, and there are two walls of length $x$. Forgetting the second wall is the typical modelling error.
- The domain comes from geometry. A wall of zero or negative length is not a room. The length $x=50$ would use the whole budget on the two short walls and leave $y=0$.
- On the open interval $(0,50)$ the function $A$ is a downward parabola, so its only critical point is the global maximum. Here this is also clear because $A$ rises while $A'>0$ and falls after it.
- Since $A(0)=A(50)=0$, the ends of the interval give no room at all, so nothing beats $x=25$.

## Final answer (in words)

The room has area $A(x)=60x-1{,}2x^2$ square metres, for $0<x<50$ metres. The area is largest when each wall perpendicular to the old wall is $25$ m long and the wall parallel to the old wall is $30$ m long. The maximal area is $750\ \mathrm{m^2}$. The cost check: $2\cdot25\cdot300+30\cdot500=15\,000+15\,000=30\,000$ PLN, so the whole budget is used. In the best room, half of the money goes to the two short walls and half to the long wall.

## Verification

**Table of values near the optimum**, with $y=60-1{,}2x$:

| $x$ (m) | $y$ (m) | cost (PLN) | $A$ ($\mathrm{m^2}$) |
|---|---|---|---|
| 15 | 42 | 30 000 | 630 |
| 20 | 36 | 30 000 | 720 |
| 24 | 31,2 | 30 000 | 748,8 |
| 25 | 30 | 30 000 | 750 |
| 26 | 28,8 | 30 000 | 748,8 |
| 30 | 24 | 30 000 | 720 |
| 35 | 18 | 30 000 | 630 |

The values on the two sides of $25$ are equal in pairs ($24$ and $26$, $20$ and $30$, $15$ and $35$), which shows the symmetry of a parabola with the top at $25$.

**Different method, no derivative.** With $u=600x$ and $v=500y$ we have $u+v=30\,000$. The area is $xy=\frac{uv}{300\,000}$. For a fixed sum, a product is largest when the two numbers are equal, so $u=v=15\,000$, which gives $x=25$ and $y=30$. The same answer.

**Description of the graph.** The graph of $A(x)$ is a parabola opening downwards. It starts at $0$ for $x=0$, rises more and more slowly, reaches its top at the point $(25;\,750)$, and falls symmetrically to $0$ at $x=50$.

**Short Python code to draw it** (run only after the solution above, as a check):

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 50, 501)
A = 60 * x - 1.2 * x**2

plt.plot(x, A)
plt.plot(25, 750, "o")
plt.xlabel("x [m]")
plt.ylabel("A [m^2]")
plt.title("Area of the room")
plt.grid(True)
plt.show()
```

## Which part was modelling and which was calculation

- **Modelling** (needs thinking about the situation): choosing the variables $x$ and $y$, noticing that the old wall costs nothing, counting two walls of length $x$, writing the cost $600x+500y$, deciding that the whole budget is used, eliminating $y$, and finding the domain $0<x<50$.
- **Calculation** (only execution): the derivative $60-2{,}4x$, solving for $x=25$, the second derivative, the value $750$, the table, and the graph.
- **Interpretation** is a third part: saying that the room is $25\times30$ m and the budget is split in half.

## Common mistakes

- Counting only one perpendicular wall, or charging the old wall.
- Using the price $300$ for the long wall and $500$ for the short ones.
- Writing the cost as $300x+500y$, which gives a wrong room of $50\times30$ m.
- Leaving the domain out, or taking $x$ up to $100$ or beyond $50$, where $y<0$.
- Forgetting the units, or giving only $x$ and not $y$ and the area.
- Trusting the graph and the computer without the mathematical solution first.

## How I would explain it in class

Let $x$ be the length of each wall perpendicular to the old wall and $y$ the wall parallel to it, so the cost is $600x+500y=30\,000$, which gives $y=60-1{,}2x$ and the area $A(x)=60x-1{,}2x^2$ on $0<x<50$. The derivative $60-2{,}4x$ is zero at $x=25$, and the downward parabola shows a maximum, so the room is $25$ m by $30$ m with area $750\ \mathrm{m^2}$. The table and the graph show the area falling on both sides of $25$, and the modelling was the cost equation and the domain, while the rest was calculation.
