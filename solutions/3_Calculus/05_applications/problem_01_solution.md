# Problem 1

## The original problem

The position of a point is described by
$$
s(t)=t^3-6t^2+9t+2,\qquad t\ge0.
$$

1. Determine the velocity and acceleration.
2. Find the times at which the point stops.
3. Determine on which intervals the point moves in the positive direction of the axis and on which intervals it moves in the negative direction.

> **Why this problem:** it shows the derivative as a real rate of change and requires interpretation of the sign of the derivative in the context of motion.

## What we are looking for

We are given a position function of time and we want three things: how fast the point moves, how fast that speed changes, and when and in which direction the point actually travels. The whole problem is solved with the derivative, because the derivative of a position function is the velocity and the derivative of a velocity function is the acceleration. The sign of the velocity then tells us the direction of motion.

## The idea we need

Two definitions from mechanics do all the work:

- velocity is the rate of change of position, $v(t)=s'(t)$;
- acceleration is the rate of change of velocity, $a(t)=v'(t)=s''(t)$.

In formulas, with $s(t)=t^3-6t^2+9t+2$:

$$
v(t)=s'(t)=3t^2-12t+9,\qquad a(t)=s''(t)=6t-12.
$$

The point stops exactly when its velocity is zero, because "stopped" means "not moving", i.e. $v(t)=0$. To factor the velocity we write

$$
v(t)=3t^2-12t+9=3(t^2-4t+3)=3(t-1)(t-3),
$$

so the zeros are $t=1$ and $t=3$, and both lie in the domain $t\ge0$.

For the direction of motion we use the sign rule: on an interval where $v(t)>0$ the position increases, so the point moves in the positive direction of the axis; on an interval where $v(t)<0$ the position decreases, so it moves in the negative direction. The sign is read off the two linear factors $t-1$ and $t-3$, because a product of two real numbers is positive when both factors have the same sign.

Units: the formula for $s$ carries no units, so we use the standard reading of the exercise — $t$ in seconds and $s$ in metres. Then $v$ is in $\mathrm{m/s}$ and $a$ is in $\mathrm{m/s^2}$.

## Step-by-step solution

1. **Position function.** The point is at $s(t)=t^3-6t^2+9t+2$ metres at time $t\ge0$ seconds.

2. **Velocity.** Differentiate term by term, using $(t^n)'=nt^{n-1}$:

$$
v(t)=s'(t)=3t^2-12t+9\quad [\mathrm{m/s}].
$$

3. **Factor the velocity**, because a factored form makes the zeros and the sign easy to read:

$$
v(t)=3(t^2-4t+3)=3(t-1)(t-3).
$$

4. **Acceleration.** Differentiate the velocity once more:

$$
a(t)=v'(t)=6t-12=6(t-2)\quad [\mathrm{m/s^2}].
$$

5. **Times when the point stops.** Solve $v(t)=0$:

$$
3(t-1)(t-3)=0 \;\Longrightarrow\; t=1 \;\text{ or }\; t=3.
$$

Both values satisfy $t\ge0$, so both are admissible and there are no other stopping times.

6. **Sign of the velocity on $[0,\infty)$.** The two critical numbers $1$ and $3$ split the domain into three intervals. We test one point in each:

| Interval | Test point | $t-1$ | $t-3$ | $v(t)=3(t-1)(t-3)$ | Sign |
|---|---|---|---|---|---|
| $[0,1)$ | $t=0$ | $-$ | $-$ | $v(0)=9$ | positive |
| $(1,3)$ | $t=2$ | $+$ | $-$ | $v(2)=-3$ | negative |
| $(3,\infty)$ | $t=4$ | $+$ | $+$ | $v(4)=9$ | positive |

7. **Read off the direction of motion.** Where $v>0$ the position increases, so the point moves in the positive direction; where $v<0$ the position decreases, so the point moves in the negative direction.

8. **Extra picture of the motion.** The acceleration changes sign at $t=2$: it is negative for $t<2$ (the point slows down) and positive for $t>2$ (it speeds up again). The positions at the critical times are

$$
s(0)=2,\qquad s(1)=1-6+9+2=6,\qquad s(3)=27-54+27+2=2.
$$

So the point moves forward from $2$ m to $6$ m, then backward from $6$ m to $2$ m, then forward again.

## Why each step is valid

- Differentiating term by term is allowed because $s$ is a polynomial and polynomials are differentiable everywhere; the rule $(t^n)'=nt^{n-1}$ applies to each power separately.
- "The point stops" is exactly the statement $v(t)=0$: velocity measures the instantaneous rate of change of position, so zero velocity means the position is momentarily constant.
- Both roots $1$ and $3$ belong to the domain $t\ge0$, and a product $3(t-1)(t-3)$ vanishes only when at least one factor is zero, so there is no third stopping time.
- The sign of $v$ can be constant on each interval between consecutive zeros of $v$, because $v$ is continuous and cannot change sign without passing through zero.
- Testing one point per interval is enough because of that continuity argument, not a guess.
- The acceleration is negative before $t=2$ and positive after $t=2$ because $a(t)=6(t-2)$ is a product of a positive constant and a linear factor that changes sign at $t=2$.

## Final answer (in words)

The velocity is $v(t)=3t^2-12t+9$ metres per second and the acceleration is $a(t)=6t-12$ metres per second squared.

The point stops at exactly two moments: at $t=1$ s and at $t=3$ s.

The point moves in the **positive** direction of the axis on $[0,1)$ and on $(3,\infty)$, and in the **negative** direction of the axis on $(1,3)$. At $t=1$ s the position $s=6$ m is a local high point of the path (a turning point), and at $t=3$ s the position $s=2$ m is a local low point; after $t=3$ s the point keeps moving in the positive direction.

$$
\boxed{v(t)=3t^2-12t+9,\quad a(t)=6t-12,\quad \text{stops at } t=1\ \text{s and } t=3\ \text{s}}
$$

## Verification

- **Differentiate back.** If $v(t)=s'(t)$ then $s(t)$ must be the antiderivative of $v$: $\int (3t^2-12t+9)\,dt=t^3-6t^2+9t+C$, and $C=2$ reproduces the given $s$. The velocity is correct.
- **Check the zeros numerically.** $v(1)=3-12+9=0$ and $v(3)=27-36+9=0$. ✓
- **Check the signs numerically.** $v(0)=9>0$, $v(2)=12-24+9=-3<0$, $v(4)=48-48+9=9>0$. These match the sign table.
- **Check the direction with positions instead of derivatives.** On $[0,1]$ the positions are $s(0)=2$, $s(0{,}5)=5{,}125$, $s(1)=6$: they increase, so the motion was positive. On $[1,3]$ we get $s(1)=6$, $s(2)=4$, $s(3)=2$: they decrease, so the motion was negative. On $[3,4]$ we get $s(3)=2$, $s(4)=6$: they increase again. The derivative-based answer agrees with the raw positions.
- **Units.** $s$ in metres and $t$ in seconds give $v$ in $\mathrm{m/s}$ and $a$ in $\mathrm{m/s^2}$; these are the correct units for a derivative of a position function and its derivative.
- **Displacement versus distance.** On $[0,4]$ the displacement is $s(4)-s(0)=6-2=4$ m, while the distance travelled is $4+4+4=12$ m. The two differ, which is exactly what the sign analysis predicts (the point goes backwards on $(1,3)$).

## Common mistakes

- Differentiating the velocity to get the acceleration but forgetting the power rule on the $9t$ term (writing $9$ instead of $0$ for its derivative).
- Solving $v(t)=0$ and forgetting to reject roots outside the domain; here both roots are admissible, but the habit matters.
- Reading the direction of motion from the sign of the *acceleration* instead of the sign of the *velocity*.
- Claiming that the point stops "at $t=2$" because $a(2)=0$; $a(2)=0$ only means the acceleration vanishes, so the velocity is most negative there ($v(2)=-3$), i.e. the point is moving fastest backwards, not standing still.
- Writing the sign table without testing a point in each interval, or claiming the sign is the same on $(0,1)$ and $(1,3)$ without checking.

## How I would explain it in class

The velocity is just the derivative of the position function, and the acceleration is the derivative of the velocity, so both come from one routine differentiation. The point stops exactly where the velocity is zero, and after factoring the velocity those zeros are $t=1$ and $t=3$. Looking at the sign of the velocity on the three intervals they cut out, the point moves forward, then backward, then forward again.
