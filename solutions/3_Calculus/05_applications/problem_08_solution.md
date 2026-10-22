# Problem 8

## The original problem

The rate at which requests arrive at a server during the first 5 minutes is described by the function
$$
r(t)=100+20t\quad [\text{requests/min}],\qquad 0\le t\le5.
$$

1. Compute the total number of requests that arrived during this time.
2. Compute the average rate of incoming requests over this interval.
3. Compare the average rate with the values $r(0)$ and $r(5)$.

> **Why this problem:** it shows the integral as summation of a varying rate in an example directly related to computer science.

## What we are looking for

The letter $t$ is time in minutes, counted from the start. The function $r(t)$ says how many requests per minute arrive at the moment $t$. The rate grows, so we cannot just multiply the rate by the time. We want the total number of requests, then the average rate, and then a comparison with the rate at the start and at the end.

## The idea we need

If the rate were constant, the total would be rate times time. A rate that changes is cut into very short pieces of time. In a short piece of length $dt$ about $r(t)\,dt$ requests arrive. Adding all pieces is the definite integral:
$$
\text{total}=\int_0^5 r(t)\,dt.
$$
The average rate is the total divided by the length of the interval, which is $5$ minutes.

## Step-by-step solution

1. **Set up the integral.**
$$
Q=\int_0^5 (100+20t)\,dt.
$$

2. **Find an antiderivative** (a function whose derivative is $100+20t$):
$$
F(t)=100t+10t^2.
$$

3. **Evaluate between $0$ and $5$:**
$$
Q=F(5)-F(0)=(500+250)-0=750.
$$

4. **Average rate.** Divide by the length $5$ min:
$$
r_{\text{avg}}=\frac{750}{5}=150\ \text{requests/min}.
$$

5. **Compare.** At the start $r(0)=100$ and at the end $r(5)=100+100=200$. The average $150$ lies between them. It is exactly their middle: $\frac{100+200}{2}=150$.

## Why each step is valid

- The integral adds up rate times small time, so its unit is requests per minute times minutes, which is requests.
- The Fundamental Theorem of Calculus says that the integral equals $F(5)-F(0)$ for any antiderivative $F$.
- The derivative of $100t+10t^2$ is $100+20t$, so $F$ is a correct antiderivative.
- The average is the total divided by the time, the same as for any quantity: total divided by how long it lasted.
- The average is the middle of the two end values because $r$ is a straight line, so its graph is a trapezoid. The area of a trapezoid is the average of the two parallel sides times the width.

## Final answer (in words)

During the first $5$ minutes $750$ requests arrived. The average rate was $150$ requests per minute. This lies between the starting rate of $100$ requests per minute and the final rate of $200$ requests per minute, exactly in the middle, because the rate grows in a straight line.

## Verification

- **Geometry.** The region under $r$ is a trapezoid with parallel sides $100$ and $200$ and width $5$. Its area is $\frac{100+200}{2}\cdot5=750$.
- **Sum of pieces.** For each minute use the rate in the middle of the minute: $r(0{,}5)=110$, $r(1{,}5)=130$, $r(2{,}5)=150$, $r(3{,}5)=170$, $r(4{,}5)=190$. The sum is $750$.
- **Where is the average reached?** $r(t)=150$ gives $t=2{,}5$ min, the middle of the interval.

## Common mistakes

- Multiplying $r(5)$ by $5$, which gives $1000$ and ignores that the rate was lower earlier.
- Forgetting the lower limit, or forgetting to subtract $F(0)$.
- Dividing by $750$ or by $2$ instead of by the length of time $5$.
- Giving the total in requests per minute instead of in requests.

## How I would explain it in class

The rate changes, so we add up rate times tiny time pieces, and that is the integral of $100+20t$ from $0$ to $5$, which equals $750$ requests. Dividing by five minutes gives the average rate of $150$ requests per minute. It lies between $r(0)=100$ and $r(5)=200$, and it is exactly their middle because the graph of the rate is a straight line.
