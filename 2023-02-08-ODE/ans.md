## s

Firstly, if $\tau_p=0$, we get $-(T-T_\infty(t))=0$, which reveals a trivial solution $T=T_\infty(t)=A\exp(t/\tau_w)+B+C\cos(\omega t)$.

If $\tau_p\neq 0$, the equation (1) can be normalized as
$$
\left\{\begin{array}{l}
\dfrac{dT}{dt}+\dfrac{1}{\tau_p}=T_\infty(t),\qquad T_\infty(t)=A\exp(t/\tau_w)+B+C\cos(\omega t)\\
T(0)=T_0
\end{array}\right.
$$


## s

The 2 order ODE that describes a damped spring-mass system with a mass $m$ kg, damping constant $c$ kg/s and spring constant $k$ N/m should be
$$
m \dfrac{d^2y}{dt^2}+c\dfrac{dy}{dt}+ky=f(t)
$$
where $f(t)$ is the external force.

#### a) 

The auxiliary homogenous to the equation above is $m \dfrac{d^2y}{dt^2}+c\dfrac{dy}{dt}+ky=0$

Basic solution form: $y(t)=\exp(\lambda t)$, substitute it back into the equation, we have 
$$
\exp(\lambda t)(m\lambda^2+c\lambda+k)=0\quad \Rightarrow \quad m\lambda^2+c\lambda+k=m(\lambda+\dfrac{c}{2m})^2+k-\dfrac{c^2}{4m}\neq 0\qquad(*)
$$
If the system is critically damped, then $(*)$ has a unique solution, hence $k-\dfrac{c^2}{4m}=0$, i.e. $c=2\sqrt{mk}$. If $k=1/m$, then $c$ should be $2$.

#### b)

The ODE describing a critically damped model without external forcing is $m \dfrac{d^2y}{dt^2}+c\dfrac{dy}{dt}+ky=0$.

Given $k=1/m, c=2\sqrt{mk}$, we'd have $m \dfrac{d^2y}{dt^2}+2\sqrt{mk}\dfrac{dy}{dt}+\dfrac{1}{m}y=0$.

