# Problem 7

## The original problem

Assume the model
$$
N(t)=N_0e^{kt},\qquad k>0.
$$

1. Verify by differentiation that the model satisfies the relation $N'(t)=kN(t)$.
2. Find the population doubling time.
3. Explain why the doubling time does not depend on $N_0$.

> **Why this problem:** it shows the connection between the exponential function and a growth rate proportional to the current value, without introducing a separate technique for solving differential equations.

## What we are looking for

We have a population. The letter $t$ is time, for example in hours. The letter $N(t)$ is the number of individuals at time $t$. The number $N_0$ is the starting population, and $k$ is a positive growth constant, measured in one over hours. We want to show that the speed of growth is proportional to the current size. Then we want the time needed to double, and the reason why the start size does not matter.

## The idea we need

The derivative $N'(t)$ is the speed of growth: how many individuals are added per hour. We differentiate the model with the chain rule, using the fact that the derivative of $e^{kt}$ is $ke^{kt}$. The doubling time $T$ is the time when $N(T)=2N_0$. To solve for $T$ we take the natural logarithm, which is the inverse of the exponential function.

## Step-by-step solution

1. **Differentiate.** The number $N_0$ is a constant, so
$$
N'(t)=N_0\cdot ke^{kt}=k\,N_0e^{kt}=kN(t).
$$
This is exactly the required relation.

2. **Write the doubling condition.** We look for $T>0$ with
$$
N_0e^{kT}=2N_0.
$$

3. **Divide by $N_0$.** We assume $N_0>0$, so division is allowed:
$$
e^{kT}=2.
$$

4. **Take the natural logarithm** of both sides:
$$
kT=\ln 2,\qquad T=\frac{\ln 2}{k}\approx\frac{0{,}693}{k}.
$$

5. **Why it does not depend on $N_0$.** The number $N_0$ cancelled in step 3, so it does not appear in the formula for $T$.

## Why each step is valid

- The factor $N_0$ stays in front when we differentiate, because the derivative of a constant times a function is the constant times the derivative.
- The chain rule gives $\frac{d}{dt}e^{kt}=e^{kt}\cdot k$, since the inside function $kt$ has derivative $k$.
- Dividing by $N_0$ is legal because a population that starts at zero never grows, so we need $N_0>0$.
- The natural logarithm is the inverse of $e^{x}$, so $\ln e^{kT}=kT$. The value $\ln 2$ is defined because $2>0$.
- The relation $N'=kN$ says that the growth speed is a fixed percentage $k$ of the current size. A bigger population grows faster, but the doubling time stays the same.

## Final answer (in words)

The derivative of $N$ equals $k$ times $N$, so the growth speed is proportional to the current population. The population doubles after the time
$$
T=\frac{\ln 2}{k}\approx\frac{0{,}693}{k}
$$
in the same unit as $t$, for example hours. This time does not depend on $N_0$, because the starting size cancels when we compare $N_0e^{kT}$ with $2N_0$.

## Verification

- **Numerical check.** Take $k=0{,}1$ per hour. Then $T=\ln 2/0{,}1\approx6{,}931$ hours, and $e^{0{,}1\cdot6{,}931}=e^{0{,}6931}\approx2{,}000$.
- **Two different starts.** For $N_0=100$ we get $N(T)\approx200$. For $N_0=5000$ we get $N(T)\approx10\,000$. Both are doubled after the same $T$.
- **Doubling again.** After $2T$ the population is $N_0e^{2kT}=N_0\cdot2^2=4N_0$. So every period of length $T$ doubles it once more.
- **Different method for the derivative.** Take the logarithm: $\ln N=\ln N_0+kt$. Differentiating gives $N'/N=k$, so $N'=kN$.

## Common mistakes

- Writing $\frac{d}{dt}e^{kt}=e^{kt}$ and forgetting the factor $k$.
- Writing $\ln 2/k$ as $\ln(2/k)$.
- Thinking that a bigger starting population doubles faster. It adds more individuals, but it needs the same time.
- Forgetting the unit of $T$: it is the unit of time, not a number of individuals.

## How I would explain it in class

Differentiating $N_0e^{kt}$ gives $kN_0e^{kt}=kN$, so the population grows at a speed proportional to its own size. For doubling we solve $N_0e^{kT}=2N_0$, and after dividing by $N_0$ and taking the logarithm we get $T=\ln 2/k$. The starting size $N_0$ cancelled, so the doubling time is the same whether we begin with one hundred individuals or five thousand.
