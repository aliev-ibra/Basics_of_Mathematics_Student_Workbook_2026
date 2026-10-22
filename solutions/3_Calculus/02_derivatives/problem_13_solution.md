# Problem 13

## The original problem

For
$$f(x)=e^{\sin(x^2)}$$
compute the derivative. First write the layers
$$x\longrightarrow x^2\longrightarrow \sin(x^2)\longrightarrow e^{\sin(x^2)}$$
and explain why differentiation moves through them in the reverse order.

> **Why this problem:** it develops the chain rule as a method for working with multiple layers.

## What we are looking for

We need $f'(x)$ for a function with three layers placed one inside another. We must also explain a fact about the method: when we compute the value of the function we go from the inside to the outside, but when we differentiate we start from the outside and move to the inside. We need to say why.

## The idea we need

The **chain rule**. For a composition of functions, the derivative is the derivative of the outer function, evaluated at the inner function, times the derivative of the inner function:
$$\frac{d}{dx}F(g(x))=F'(g(x))\cdot g'(x).$$
When there are more layers, we use the rule again and again, and we get one factor for each layer. We recognise the need for it when one function is placed inside another: here the exponential contains a sine, and the sine contains a square.

The basic derivatives we need are: $\frac{d}{dx}e^v=e^v$, $\frac{d}{du}\sin u=\cos u$, and $\frac{d}{dx}x^2=2x$.

## Step-by-step solution

1. Write the layers. Let $u=x^2$. Let $v=\sin u$. Then $f=e^v$. Computing a value goes $x\to u\to v\to f$.
2. Start with the outermost layer, $e^v$. Its derivative is $e^v$. We keep the inside as it is, so this factor is $e^{\sin(x^2)}$.
3. Go one layer inwards, to $v=\sin u$. Its derivative is $\cos u$, and with the inside in place this factor is $\cos(x^2)$.
4. Go to the innermost layer $u=x^2$. Its derivative is $2x$.
5. Multiply the three factors:
$$f'(x)=e^{\sin(x^2)}\cdot\cos(x^2)\cdot 2x=2x\cos(x^2)\,e^{\sin(x^2)}.$$

**Why the order is reversed.** To compute a value of $f$ we must first know $x^2$, then $\sin$ of that number, then $e$ to that power. The inside is computed first, because each outer layer needs the result of the layer inside it as its input.

The derivative of an outer layer is a formula that contains the whole inner layer. For example, the derivative of $e^{v}$ is $e^{v}$ with the entire $\sin(x^2)$ sitting in the place of $v$. So we can write the outer derivative at once, and we leave the inside untouched. Only after that do we differentiate the inside, which is the next layer, and again we leave its own inside untouched. In this way we peel the function like an onion, from the skin to the centre, and every layer gives one factor. We cannot start from the centre. The derivative of $x^2$ alone says nothing about how the sine and the exponential react to it. They react through their own derivatives, evaluated at the values they receive. This is why the order of differentiation is the reverse of the order of computing.

## Why each step is valid

- Step 2 is valid because the derivative of $e^v$ with respect to $v$ is $e^v$, and the chain rule tells us to keep the inner expression unchanged inside the outer derivative.
- Step 3 is valid because the middle layer is $\sin$ of the inner layer, and $\frac{d}{du}\sin u=\cos u$.
- Step 4 is valid by the power rule: $\frac{d}{dx}x^2=2x$.
- Step 5 is valid because the chain rule applied twice gives a product of three factors, one for each layer.
- The outside-first order is valid because the derivative of an outer layer is written in terms of the whole inner expression, so that expression is kept in place and differentiated afterwards.

## Final answer (in words)

The derivative is
$$f'(x)=2x\cos(x^2)\,e^{\sin(x^2)}.$$
It is the product of three factors: $e^{\sin(x^2)}$ from the exponential, $\cos(x^2)$ from the sine, and $2x$ from the square. Values are computed from the inside out, and the derivative is written by peeling the layers from the outside in.

## Verification

**Check 1: a special value.** At $x=0$ the formula gives $2\cdot0\cdot\cos0\cdot e^{0}=0$. The function near $0$ behaves like $e^{x^2}\approx 1+x^2$, because $\sin(x^2)\approx x^2$. This has a horizontal tangent at $0$. The values agree.

**Check 2: a numerical difference quotient.** At $x=1$ the formula gives $2\cos(1)\,e^{\sin 1}\approx2.50676$. A central difference quotient with $h=0.0001$ is $\frac{f(1.0001)-f(0.9999)}{0.0002}\approx2.50676$. The two numbers agree.

**Check 3: symmetry.** The function is even, because $(-x)^2=x^2$. So the derivative must be odd. In our formula the factor $2x$ is odd and the other two factors are even, so the product is odd. This is consistent.

## Common mistakes

- Forgetting a layer. The answer $\cos(x^2)e^{\sin(x^2)}$ lacks the factor $2x$.
- Changing the inside while differentiating the outside, for example writing $e^{\cos(x^2)}$ for the first factor. The inside must stay the same.
- Putting the $2x$ inside the cosine. The correct factor is $\cos(x^2)$, and the $2x$ stands outside it as a separate multiplier.

## How I would explain it in class

The function has three layers, a square inside a sine inside an exponential, and the value is computed from the inside outwards. For the derivative I use the chain rule and peel from the outside: the exponential gives $e^{\sin(x^2)}$, the sine gives $\cos(x^2)$, and the square gives $2x$, with each inside left unchanged until its own turn. Multiplying the three factors gives $2x\cos(x^2)e^{\sin(x^2)}$.
