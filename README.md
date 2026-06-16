Rational domain implementation of the lambda function defined as:

$$\lambda(x) = \text{sgn}(x) \cdot \sum{k=0}^{\lfloor \log{10}(|x|) \rfloor} \left( \lfloor |x| \cdot 10^{-k} \rfloor \pmod{10} \right) \cdot 10^{\lfloor \log{10}(|x|) \rfloor - k}$$

That is, for a number x, the value of lambda(x) is a number with reverse digit order (i.e lambda(23)=32).
A problem arises when x is a rational number with infinite decimal expansion.
(i.e. lambda(1/3)=lambda(0.333...)=...333.0?)
The problem can be solved by shifting the domain to the g-adic number system.

In it, lambda(1/3) can be calculated as a geometric series 3+30+300+...
That is (using the geometric series formula) 3/(1-10) or -1/3.

Treating the result this way even preserves involution, i.e. lmabda(lambda(1/3))=lambda(-1/3)=1/3.
Altough lambda is not an involution, since lambda(lambda(10))=lambda(1)=1, not 10 -- unless the domain of x is either defined for strings, or $10^x$ to $10^-x$.

The second option seems better compared to the original function. However, lambda(12) becomes 2.1 instead of 21, but stays involution:

$$\lambda(x) = \text{sgn}(x) \cdot \sum_{k=-\infty}^{\infty} \left( \lfloor |x| \cdot 10^{-k} \rfloor \pmod{10} \right) \cdot 10^{-k}$$
