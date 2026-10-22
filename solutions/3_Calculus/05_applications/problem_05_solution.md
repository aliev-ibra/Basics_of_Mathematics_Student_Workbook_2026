# Problem 5

## The original problem

The velocity of a car during the first five seconds is described by the function
$$
v(t)=4t+2\quad [\mathrm{m/s}].
$$

Compute the distance traveled and explain why the integral of velocity gives the change in position.

Then answer what would have to be changed in the reasoning if the velocity also took negative values.

> **Why this problem:** it connects the integral with accumulation and distinguishes displacement from the actual distance traveled.

## What we are looking for

We must add up how far the car travels in five seconds, and we should explain *why* the tool for this is the definite integral. The second part asks us to notice a trap: the integral of velocity always gives the net change of position, and this equals the distance only as long as the car never reverses. We should say exactly what has to change if the car does reverse.

## The idea we need

**Why the integral of velocity gives the change of position.** The Fundamental Theorem of Calculus says: if $s'(t)=v(t)$, then

$$
s(t)-s(0)=\int_{0}^{t}v(u)\,du.
$$

Intuitively, split the five seconds into many tiny intervals of length $\Delta t$. During one such interval the car moves about $v(u)\Delta t$ metres, and the total movement is the sum of all these small pieces:

$$
\text{displacement}\approx\sum v(u_i)\,\Delta t.
$$

As the intervals become infinitely short this sum becomes the definite integral $\int_0^5 v(t)\,dt$. So the definite integral is "the accumulated area under the velocity–time graph", and its units are $\mathrm{m/s}\cdot\mathrm{s}=\mathrm{m}$.

**Distance versus displacement.** The integral always adds the pieces *with their signs*. It therefore measures the **displacement**, the signed difference between the final and the initial position:

$$
\text{displacement}=\int_{0}^{5}v(t)\,dt.
$$

The **distance** travelled adds the absolute values, because going $10$ m backwards still adds $10$ m to the distance:

$$
\text{distance}=\int_{0}^{5}|v(t)|\,dt.
$$

So the two agree only when $v$ has one sign on the whole interval.

**In this problem** $v(t)=4t+2\ge2>0$ on $[0,5]$, so the car never stops and never reverses: distance $=$ displacement.

## Step-by-step solution

1. **Read the data.** The velocity is $v(t)=4t+2$ metres per second for $0\le t\le5$ seconds.

2. **Check the sign of the velocity first**, because this decides whether distance and displacement coincide. The smallest value occurs at $t=0$:

$$
v(0)=2\ \mathrm{m/s}>0,
$$

and $v$ is increasing, so $v(t)>0$ on the whole interval $[0,5]$.

3. **Set up the integral.** The distance is the area under the velocity–time graph:

$$
D=\int_{0}^{5}(4t+2)\,dt.
$$

4. **Compute the antiderivative.**

$$
\int (4t+2)\,dt=2t^2+2t.
$$

5. **Evaluate at the limits.**

$$
D=\left[2t^2+2t\right]_{0}^{5}=(2\cdot25+2\cdot5)-(0+0)=50+10=60.
$$

So the car travels **$60$ m**.

6. **Explain the connection with position.** If $s(t)$ is the position, then $s'(t)=v(t)$, and by the Fundamental Theorem of Calculus

$$
s(5)-s(0)=\int_{0}^{5}v(t)\,dt=60\ \mathrm{m}.
$$

The integral of the velocity *is* the change of position because it adds up the small changes $v(u)\,du$ of the position over small time intervals $du$.

7. **The case of negative velocities.** Suppose the velocity did become negative on some part of $[0,5]$. Then:

   - $\int_0^5 v(t)\,dt$ would still be the **displacement**, i.e. the net change of position, possibly smaller than the distance (or even zero, if the car returned to its starting point);
   - the **distance** would have to be computed as $\int_0^5|v(t)|\,dt$, that is, by splitting the interval at the zeros of $v$ and taking the absolute value of $v$ on each piece:
     $$
     D=\int_{0}^{t_1}|v|\,dt+\int_{t_1}^{t_2}|v|\,dt+\int_{t_2}^{5}|v|\,dt;
     $$
   - concretely, on such a piece $\int |v|\,dt$ equals minus the usual integral, because $v<0$ there.

8. **A small illustration.** Take instead $v(t)=4t-2$ on $[0,5]$. It is negative on $[0,\tfrac12]$ and positive afterwards.

   - Displacement: $\int_0^5(4t-2)\,dt=\left[2t^2-2t\right]_0^5=50-10=40$ m.
   - Distance: $\int_0^{1/2}(2-4t)\,dt+\int_{1/2}^5(4t-2)\,dt=\left[2t-2t^2\right]_0^{1/2}+\left[2t^2-2t\right]_{1/2}^5=0{,}5+40{,}5=41$ m.

   The distance $41$ m is larger than the displacement $40$ m, exactly as it must be, because the first half second was spent going backwards.

## Why each step is valid

- The distance travelled equals $\int_0^5 v(t)\,dt$ here only because $v>0$ everywhere on the interval; this is checked first, so the reasoning is valid rather than assumed.
- $v(t)=4t+2$ is increasing on $[0,5]$ because its derivative $4$ is positive, so its minimum on the interval is at $t=0$; hence $v(t)\ge v(0)=2>0$.
- The antiderivative $2t^2+2t$ is correct because its derivative is $4t+2$, and the Fundamental Theorem of Calculus lets us compute the definite integral by evaluating it at the limits.
- The identity $s(t)-s(0)=\int_0^t v(u)\,du$ is a direct instance of the Fundamental Theorem of Calculus applied to $s$, because $s'=v$.
- The units are consistent: $\mathrm{m/s}$ integrated over $\mathrm{s}$ gives $\mathrm{m}$.
- When $v$ changes sign, $\int v\,dt$ still gives the change of position because the Fundamental Theorem does not care about the sign of $v$; only the *interpretation* as "distance" breaks down, and the fix is the absolute value.
- Splitting the integral at the zeros of $v$ is legitimate because $|v|$ is continuous and piecewise smooth there, so the integral over the whole interval is the sum of the integrals over the pieces.

## Final answer (in words)

In the first five seconds the car travels **$60$ metres**, and this is also its displacement, because the velocity is positive on the whole interval.

The integral of velocity gives the change of position because it accumulates the small changes of position $v(u)\,du$ over small time intervals $du$, which is exactly the Fundamental Theorem of Calculus: $s(t)-s(0)=\int_0^t v(u)\,du$.

If the velocity took negative values, then $\int_0^5 v(t)\,dt$ would measure only the **net change of position** (the displacement), while the **distance** would have to be computed as $\int_0^5|v(t)|\,dt$, splitting the integral at the times where $v=0$ and reversing the sign on the pieces where $v<0$.

$$
\boxed{D=\int_{0}^{5}(4t+2)\,dt=60\ \mathrm{m},\qquad
D_{\text{general}}=\int_{0}^{5}|v(t)|\,dt}
$$

## Verification

- **Geometric check.** The graph of $v$ on $[0,5]$ is a straight line from $(0,2)$ to $(5,22)$. The area under it is a trapezoid with parallel sides $2$ and $22$ and height $5$, so

$$
D=\frac{2+22}{2}\cdot5=60\ \mathrm{m},
$$

the same value as the antiderivative computation. ✓

- **Consistency with the position function.** Integrating $v$ gives a position $s(t)=2t^2+2t+C$. Then $s(5)-s(0)=(50+10+C)-(0+C)=60$ m, so the change of position and the distance coincide, as they must when the car never reverses.
- **Magnitude check.** An average speed of $\frac{60}{5}=12\ \mathrm{m/s}$ sits between the minimum speed $2$ and the maximum speed $22$, as it must for a speed that increases steadily.
- **Units check.** $\int (4t+2)\,dt$ has units $\mathrm{m/s}\cdot\mathrm{s}=\mathrm{m}$, and the answer $60$ m is a distance. ✓
- **Sign check on the second part.** In the illustration, the distance $41$ m is strictly larger than the displacement $40$ m; the extra $1$ m is exactly twice the $0{,}5$ m the car rolled backwards in the first half second, which is the expected correction.
- **Consistency with Problem 1.** In Problem 1 the velocity changed sign and the distance ($12$ m over $[0,4]$) differed from the displacement ($4$ m), which confirms the rule stated here.

## Common mistakes

- Integrating $|4t+2|$ without checking the sign first; the absolute value must be applied only where the velocity is actually negative.
- Writing the distance as $s(5)-s(0)$ without ever finding $s$, or conversely assuming $s(5)-s(0)$ is the distance in a situation where the car reverses.
- Computing the displacement $\int v\,dt$ and calling it the distance when the velocity changes sign.
- Forgetting to split the integral at the zeros of $v$ when the velocity changes sign, or taking the absolute value of the whole integral instead of of each piece.
- Getting the units wrong (writing $\mathrm{m/s}$ or $\mathrm{m^2}$) — an integral of velocity over time is a length.

## How I would explain it in class

The distance is the area under the velocity graph, so I integrate $4t+2$ from $0$ to $5$ and get $60$ metres, and because the velocity never becomes negative the distance and the displacement are the same number here. The integral of the velocity gives the change of position because it adds up the tiny pieces of movement $v\,dt$, which is the Fundamental Theorem of Calculus in the form $s(t)-s(0)=\int_0^t v\,dt$. If the velocity went negative, that integral would only give the net displacement, and for the real distance I would have to integrate the absolute value and split the interval where the velocity changes sign.
