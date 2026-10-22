# Problem 3

## The original problem

From a $30\text{ cm}\times40\text{ cm}$ sheet, squares of side length $x$ are cut from the corners and the edges are folded up to form an open box.

Write the volume as a function of $x$, determine the physically meaningful domain, and find the value of $x$ for which the volume is greatest.

> **Why this problem:** it develops optimization modeling in a situation where the objective function is not given and must be built independently from the geometry.

## What we are looking for

Here nobody hands us a formula; we must build the model ourselves out of the picture of the sheet of cardboard. We have to work out the three dimensions of the box in terms of the cut size $x$, write the volume as a function of that single variable, restrict $x$ to the values for which a real box exists, and then find the cut that gives the biggest box. The whole point is the modelling step: geometry first, calculus second.

## The idea we need

**Step 1 — the geometry.** Cutting squares of side $x$ from the four corners shortens each of the two edges of the sheet by $2x$ (one cut of size $x$ at each end). The sheet is $30$ cm by $40$ cm, so the base of the box is $(30-2x)$ cm by $(40-2x)$ cm, and the height of the box is $x$ cm, because the walls are the folded-up squares.

**Step 2 — the objective function.** Volume $=$ base area $\times$ height:

$$
V(x)=x(30-2x)(40-2x)=4x^3-140x^2+1200x \quad [\mathrm{cm^3}].
$$

**Step 3 — the domain from the physics.** All three dimensions must be positive:

$$
x>0,\qquad 30-2x>0\Rightarrow x<15,\qquad 40-2x>0\Rightarrow x<20.
$$

The binding condition is $x<15$, so the physically meaningful domain is $x\in(0,15)$ cm.

**Step 4 — the calculus.** A maximum of a differentiable function on the interior of an interval must occur at a critical point, where the derivative vanishes:

$$
V'(x)=12x^2-280x+1200=4(3x^2-70x+300)=0.
$$

Solving the quadratic gives two candidates, and only one of them lies in the domain. The second derivative test then confirms the type:

$$
V''(x)=24x-280,\qquad V''(5{,}657)\approx-144{,}2<0,
$$

so the surviving critical point is a maximum; the endpoints $x=0$ and $x=15$ both give volume $0$, which makes it a global maximum.

## Step-by-step solution

1. **Model the geometry.** Let $x$ be the side of the cut-out square in centimetres. After the cuts and the folding:

   - length of the base: $30-2x$ cm,
   - width of the base: $40-2x$ cm,
   - height: $x$ cm.

2. **Write the volume.**

$$
V(x)=x(30-2x)(40-2x).
$$

Expanding for the differentiation step:

$$
V(x)=x(1200-60x-80x+4x^2)=x(1200-140x+4x^2)=4x^3-140x^2+1200x.
$$

3. **Fix the domain.** We need $x>0$, $30-2x>0$ and $40-2x>0$, that is $0<x<15$. Outside this range the sheet is either untouched ($x\le0$) or too narrow to fold ($x\ge15$).

4. **Differentiate.**

$$
V'(x)=12x^2-280x+1200.
$$

5. **Solve the critical equation.** Dividing by $4$ (which does not change the roots),

$$
3x^2-70x+300=0.
$$

With the quadratic formula, $\Delta=70^2-4\cdot3\cdot300=4900-3600=1300$, so

$$
x=\frac{70\pm\sqrt{1300}}{6}=\frac{70\pm10\sqrt{13}}{6}=\frac{35\pm5\sqrt{13}}{3}.
$$

6. **Keep only the admissible root.**

$$
x_1=\frac{35-5\sqrt{13}}{3}\approx5{,}6574\ \mathrm{cm},\qquad
x_2=\frac{35+5\sqrt{13}}{3}\approx17{,}6759\ \mathrm{cm}.
$$

The second value $x_2\approx17{,}68$ cm is larger than $15$ cm and therefore outside the domain (the $30$ cm side would give $30-2x<0$). Only $x_1$ is a physical cut.

7. **Check the type of the extremum.**

$$
V''(x)=24x-280,\qquad V''(x_1)=24\cdot5{,}6574-280\approx-144{,}22<0.
$$

So $x_1$ is a local maximum.

8. **Check the endpoints.** At the ends of the domain the box degenerates to nothing:

$$
V(0)=0,\qquad V(15)=15\cdot0\cdot10=0.
$$

Both are smaller than $V(x_1)$, so $x_1$ is the global maximum on $(0,15)$.

9. **Compute the maximum volume.** Using the exact root,

$$
V(x_1)=\frac{35000+13000\sqrt{13}}{27}\approx3032{,}30\ \mathrm{cm^3}.
$$

10. **Give the resulting box.** With $x=x_1\approx5{,}6574$ cm the box measures

$$
18{,}685\ \mathrm{cm}\times28{,}685\ \mathrm{cm}\times5{,}657\ \mathrm{cm}.
$$

## Why each step is valid

- Cutting a square of side $x$ from each corner removes $x$ centimetres from both ends of each edge, so each edge loses $2x$ in total; this is the only change in the base dimensions.
- The height of the box is exactly $x$, because the walls are the cut squares folded up along the fold lines.
- The volume of a cuboid is base area times height, so $V(x)=x(30-2x)(40-2x)$; expanding the product gives the polynomial used for differentiation.
- The domain comes from lengths, not from taste: a negative base length is meaningless, so $x<15$ (the narrower of the two sheets) is required.
- Fermat's theorem says an interior maximum of a differentiable function satisfies $V'(x)=0$, so the critical equation is the right one to solve; dividing by the nonzero constant $4$ preserves the solution set.
- The quadratic formula gives both roots, and the second root is rejected because it lies outside the domain, not because it "looks wrong" — this check must be made explicitly.
- $V''(x_1)<0$ means the function bends downwards at $x_1$, which by the second-derivative test makes the critical point a local maximum.
- Comparing with the endpoints and using continuity of $V$ on $[0,15]$ (Extreme Value Theorem) turns the local maximum into a global one.

## Final answer (in words)

The volume is the function

$$
V(x)=x(30-2x)(40-2x)\ \mathrm{cm^3},\qquad 0<x<15,
$$

with the physically meaningful domain $x\in(0,15)$ cm coming from the requirement that all three dimensions stay positive.

The volume is greatest when the cut squares have side

$$
x=\frac{35-5\sqrt{13}}{3}\approx5{,}66\ \mathrm{cm},
$$

and then the box has base $18{,}69\ \mathrm{cm}\times28{,}69\ \mathrm{cm}$ and height $5{,}66\ \mathrm{cm}$, with maximum volume

$$
V_{\max}=\frac{35000+13000\sqrt{13}}{27}\approx3032{,}30\ \mathrm{cm^3}.
$$

## Verification

- **Check the critical equation numerically.** $V'(5{,}6574)=12\cdot32{,}006-280\cdot5{,}6574+1200\approx384{,}07-1584{,}07+1200=0$. ✓
- **Check the second derivative.** $V''(5{,}6574)\approx-144{,}22<0$, so the critical point is a maximum.
- **Check the endpoints.** $V(0)=0$ and $V(15)=0$, so no endpoint beats the critical point; the maximum is global.
- **Check neighbouring values.** $V(5)=3000$, $V(6)=3024$, $V(7)=2912$, while $V(5{,}6574)\approx3032{,}30$. The values rise towards $5{,}6574$ and fall after it, exactly as the maximum requires.
- **Brute-force check.** Scanning $x$ in steps of $0{,}001$ cm over the whole domain, the largest value found is $3032{,}3025\ \mathrm{cm^3}$ at $x=5{,}657$ cm, which matches the analytic answer.
- **Check the geometry physically.** $30-2\cdot5{,}6574=18{,}685>0$ and $40-2\cdot5{,}6574=28{,}685>0$, so the cuts do fit into the sheet and the box really exists.
- **Check the units.** $x$ is in cm, so the volume is in $\mathrm{cm^3}$; the number $3032$ is a volume of about $3$ litres, which is a sensible size for a box cut from a $30\times40$ cm sheet.

## Common mistakes

- Forgetting that the base loses $2x$ on each side and using $30-x$ and $40-x$ instead of $30-2x$ and $40-2x$.
- Setting the domain to $0<x<20$ (forgetting the narrower $30$ cm side) or to all of $\mathbb{R}$.
- Accepting both quadratic roots, when $x\approx17{,}68$ cm makes the $30$ cm side negative and is not a physical box.
- Stopping after the derivative test and never comparing with the endpoints.
- Confusing the height of the box with $2x$ or with $x/2$.
- Reporting only the cut size and forgetting to give the resulting three dimensions of the box.

## How I would explain it in class

The geometry gives the model: after cutting out squares of side $x$ the base is $(30-2x)$ by $(40-2x)$ and the height is $x$, so the volume is $V(x)=x(30-2x)(40-2x)$ with the domain $0<x<15$. Differentiating gives a quadratic equation whose only admissible root is $x\approx5{,}66$ cm, because the second root would need more cardboard than the narrow side has. The second derivative is negative there and both endpoints give volume zero, so this is the global maximum, a box of about $18{,}7\times28{,}7\times5{,}7$ cm with volume $3032\ \mathrm{cm^3}$.
