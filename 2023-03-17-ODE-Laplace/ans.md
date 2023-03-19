## Question 1

Given ODE:
$$
\tau_p\dfrac{dT}{dt}=-(T-T_{\infty}(t)),\qquad T_{\infty}(t)=T_\infty(t)=A\exp(t/\tau_w)+B+C\cos(\omega t),T(0)=T_0
$$
**Step 1: Laplace Transform**

By the linearity of Laplace Transform, we have 
$$
\left\{\begin{array}{l}
\mathcal{L}(LHS)&=\mathcal{L}(\tau_p\dfrac{dT}{dt})=\tau_p\mathcal{L}(\dfrac{dT}{dt})=\tau_p(sW(s)-T(0))=\tau_psW(s)-\tau_pT_0\\
\mathcal{L}(RHS)&=\mathcal{L}(-T+T_\infty(t))=-\mathcal{L}(T(t))+A\mathcal{L}(\exp(t/\tau_w))+B\mathcal{L}(1)+C\mathcal{L}(\cos\omega t)\\
&=-W(s)+\dfrac{A\tau_w}{s\tau_w-1}+\dfrac{B}{s}+\dfrac{Cs}{s^2+\omega^2}
\end{array}\right.
$$
Thus
$$
\tau_psW(s)-\tau_pT_0=-W(s)+\dfrac{A\tau_w}{s\tau_w-1}+\dfrac{B}{s}+\dfrac{Cs}{s^2+\omega^2}
$$
which leads to 
$$
\begin{array}{rl}
W(s)&=\dfrac{\tau_p T_0}{s\tau_p+1}+\dfrac{A}{(s\tau_p+1)(s-1/\tau_w)}+\dfrac{B}{(s\tau_p+1)s}+\dfrac{Cs}{(s\tau_p+1)(s^2+\omega^2)}\\
&=\tau_p T_0 F_1(s)+AF_2(s)+BF_3(s)+CF_4(s)
\end{array}
$$
**Step 2: Formal Solution**
$$
\begin{array}{rl}
\mathcal{L}^{-1}(W(s))&=\mathcal{L}^{-1}\{\tau_p T_0 F_1(s)+AF_2(s)+BF_3(s)+CF_4(s)\}\\
&=\tau_pT_0\mathcal{L}^{-1}\{F_1(s)\}+A\mathcal{L}^{-1}\{F_2(s)\}+B\mathcal{L}^{-1}\{F_3(s)\}+C\mathcal{L}^{-1}\{F_4(s)\}\\
&=\tau_pT_0f_1(t)+Af_2(t)+Bf_3(t)+Cf_4(t)
\end{array}
$$
**Step 3: Invert $F_i(s)$**, referring to the inversed Laplace Transform table,

1. $f_1(t)=\mathcal{L}^{-1}\{F_1(s)\}(t)=\mathcal{L}^{-1}\{\dfrac{1}{s\tau_p+1}\}=\dfrac{1}{\tau_p}\mathcal{L}^{-1}\{\dfrac{1}{s+1/\tau_p}\}=\tau_p^{-1}\exp(-\dfrac{t}{\tau_p})$

2. $f_2(t)=\mathcal{L}^{-1}\{F_2(s)\}(t)=\mathcal{L}^{-1}\{\dfrac{1}{(s\tau_p+1)(s-1/\tau_w)}\}=\dfrac{\mathcal{L}^{-1}\{\dfrac{1}{s-1/\tau_w}\}-\mathcal{L}^{-1}\{\dfrac{1}{s+1/\tau_p}\}}{\tau_p(1/\tau_p+1/\tau_w)}=\dfrac{\exp(\dfrac{t}{\tau_w})-\exp(-\dfrac{t}{\tau_p})}{\tau_p(1/\tau_p+1/\tau_w)}$

   $f_2(0)=\dfrac{\exp(\dfrac{0}{\tau_w})-\exp(-\dfrac{0}{\tau_p})}{\tau_p(1/\tau_p+1/\tau_w)}=0$

3. $f_3(t)=\mathcal{L}^{-1}\{F_3(s)\}(t)=\mathcal{L}^{-1}\{\dfrac{1}{(s\tau_p+1)s}\}(t)=\mathcal{L}^{-1}\{\dfrac{1}{s}\}(t)-\mathcal{L}^{-1}\{\dfrac{1}{s+1/\tau_p}\}(t)=1-\exp(-\dfrac{t}{\tau_p})$

   $f_3(0)=1-\exp(-\dfrac{0}{\tau_p})=0$

4. Using convolution:
   $$
   \begin{array}{rl}
   f_4(t)&=\mathcal{L}^{-1}\{F_4(s)\}(t)=\mathcal{L}^{-1}\{\dfrac{s}{s^2+\omega^2}\dfrac{1}{s\tau_p+1}\}(t)=\dfrac{1}{\tau_p}(\cos\omega t)*(\exp(-\dfrac{t}{\tau_p}))\\
   &\displaystyle=\dfrac{1}{\tau_p}\int_0^t\cos\omega u\exp(-\dfrac{t-u}{\tau_p})du=
   \dfrac{1}{\tau_p}\dfrac{\dfrac{\cos\omega t}{\tau_p}+\omega \sin\omega t-\dfrac{\exp(-\dfrac{t}{\tau_p})}{\tau_p}}{1/\tau_p^2+\omega^2}\\
   &=\dfrac{\cos\omega t+\omega \tau_p \sin\omega t-\exp(-\dfrac{t}{\tau_p})}{1+\tau_p^2\omega^2}
   \end{array}
   $$
   $f_4(0)=\dfrac{\cos\omega 0+\omega \tau_p \sin\omega 0-\exp(-\dfrac{0}{\tau_p})}{1+\tau_p^2\omega^2}=0$

**Step 4: Insert the $f_i(t)$ into the formal solution**
$$
\begin{array}{rl}
T(t)&=\tau_pT_0f_1(t)+Af_2(t)+Bf_3(t)+Cf_4(t)\\
&=T_0\exp(-\dfrac{t}{\tau_p}) +A\dfrac{\exp(\dfrac{t}{\tau_w})-\exp(-\dfrac{t}{\tau_p})}{\tau_p(1/\tau_p+1/\tau_w)}+B(1-\exp(-\dfrac{t}{\tau_p}))+C\dfrac{\cos\omega t+\omega \tau_p \sin\omega t-\exp(-\dfrac{t}{\tau_p})}{1+\tau_p^2\omega^2}
\end{array}
$$

## Question 2

Given critically damped 2nd order ODE:
$$
m \dfrac{d^2y}{dt^2}+2\dfrac{dy}{dt}+\dfrac{1}{m}y=0,\qquad y(0)=y_0,y'(0)=v(0)=v_0
$$
**Step 1: Laplace Transform**

Since 

- $\mathcal{L}(y''(t))(s)=s^2Y(s)-sy(0)-y'(0)=s^2 Y(s)-sy_0-v_0$
- $\mathcal{L}(y'(t))(s)=sY(s)-y(0)=s Y(s)-y_0$
- $\mathcal{L}(y(t))(s)=Y(s)$

By the linearity of Laplace Transform, we have 
$$
\left\{\begin{array}{l}
\mathcal{L}(LHS)&=\mathcal{L}\{m \dfrac{d^2y}{dt^2}+2\dfrac{dy}{dt}+\dfrac{1}{m}y\}=m \mathcal{L}\{\dfrac{d^2y}{dt^2}\}+2\mathcal{L}\{\dfrac{dy}{dt}\}+\dfrac{1}{m}\mathcal{L}\{y\}\\
&=m(s^2Y(s)-sy_0-v_0)+2(sY(s)-y_0)+\dfrac{1}{m}Y(s)\\
&=(ms^2+2s+\dfrac{1}{m})Y(s)-(msy_0+mv_0+2y_0)\\
\mathcal{L}(RHS)&=\mathcal{L}(0)=0
\end{array}\right.
$$
Thus
$$
(ms^2+2s+\dfrac{1}{m})Y(s)-(msy_0+mv_0+2y_0)=0
$$
which leads to 
$$
\begin{array}{rl}
Y(s)=\dfrac{m^2sy_0+m^2v_0+2my_0}{(ms+1)^2}
\end{array}
$$
**Step 2: Formal Solution**
$$
\begin{array}{rl}
\mathcal{L}^{-1}(Y(s))&=\mathcal{L}^{-1}\{\dfrac{m^2sy_0+m^2v_0+2my_0}{(ms+1)^2}\}\\
&=(v_0+\dfrac{y_0}{m})\mathcal{L}^{-1}\{\dfrac{1}{(s+1/m)^2}\}+y_0\mathcal{L}^{-1}\{\dfrac{1}{s+1/m}\}\\
&=(v_0+\dfrac{y_0}{m})\mathcal{L}^{-1}\{F_2(s)\}+y_0\mathcal{L}^{-1}\{F_1(s)\}\\
&=(v_0+\dfrac{y_0}{m})y_2(t)+y_0\mathcal{L}^{-1}y_1(t)
\end{array}
$$
where $F_2(s)=\dfrac{1}{(s+1/m)^2}, F_1(s)=\dfrac{1}{s+1/m}$.

**Step 3: Invert $F_i(s)$**, referring to the inversed Laplace Transform table,

1. $f_1(t)=\mathcal{L}^{-1}\{F_1(s)\}(t)=\mathcal{L}^{-1}\{\dfrac{1}{s+1/m}\}=\exp(-\dfrac{t}{m})$
2. $f_2(t)=\mathcal{L}^{-1}\{F_2(s)\}(t)=\mathcal{L}^{-1}\{\dfrac{1}{(s+1/m)^2}\}(t)=t\exp(-\dfrac{t}{m})$

**Step 4: Insert the $f_i(t)$ into the formal solution**
$$
\begin{array}{rl}
y(t)&=(v_0+\dfrac{y_0}{m})y_2(t)+y_0\mathcal{L}^{-1}y_1(t)\\
&=\left[(v_0+\dfrac{y_0}{m})t+y_0\right]\exp(-\dfrac{t}{m})
\end{array}
$$
**Verify:** 

- $y(0)=\left[(v_0+\dfrac{y_0}{m})0+y_0\right]\exp(-\dfrac{0}{m})=y_0\exp(-0)=y_0$
- $y'(t)=\dfrac{m^2v_0-mtv_0-ty_0}{m^2}\exp(-\dfrac{t}{m})$, hence $y'(0)=v_0\exp(0)=v_0$

Thus we verified that this $y(t)$ satisfies all initial conditions.

## Question 3

Given ODE:
$$
m \dfrac{d^2y}{dt^2}+2\dfrac{dy}{dt}+\dfrac{1}{m}y=\dfrac{F_0t}{\tau}\exp(-t/m),\qquad y(0)=y'(0)=0
$$
**Find $Y(s)$:**

In Question 2, we have computed that the Laplace Transform of the LHS is
$$
\mathcal{L}\{LHS\}(s)=(ms^2+2s+\dfrac{1}{m})Y(s)-(msy_0+mv_0+2y_0)
$$
In this Question 3, $y_0=v_0=0$, and the Laplace Transform of the RHS is
$$
\mathcal{L}\{RHS\}(s)=\dfrac{F_0}{\tau}\mathcal{L}\{t\exp(-t/m)\}(s)
$$
By the first shift theorem, $\mathcal{L}\{\exp(at)f(t)\}(s)=\mathcal{L}\{f(t)\}(s-a)$, let $a=-1/m,f(t)=t$, we have
$$
\mathcal{L}\{\exp(-t/m)f(t)\}(s)=\mathcal{L}\{t\}(s+1/m)=\dfrac{1}{(s+1/m)^2}
$$
Hence,
$$
\mathcal{L}\{RHS\}(s)=\dfrac{F_0}{\tau}\mathcal{L}\{t\exp(-t/m)\}(s)=\dfrac{F_0}{\tau(s+1/m)^2}
$$
Therefore, 
$$
(ms^2+2s+\dfrac{1}{m})Y(s)-(msy_0+mv_0+2y_0)=(ms^2+2s+\dfrac{1}{m})Y(s)=\dfrac{F_0}{\tau(s+1/m)^2}
$$

$$
Y(s)=\dfrac{F_0}{\tau(s+1/m)^2(ms^2+2s+\dfrac{1}{m})}=\dfrac{F_0}{m\tau(s+1/m)^4}
$$

**Inverse LT:**

Applying the first shift theorem again, let $a=-1/m,f(t)=t^3$, we'd have
$$
\mathcal{L}\{\exp(-t/m)f(t)\}(s)=\mathcal{L}\{t^3\}(s+1/m)=\dfrac{6}{(s+1/m)^4}
$$
hence,
$$
y(t)=\mathcal{L}^{-1}\{\dfrac{F_0}{m\tau(s+1/m)^4}\}=\dfrac{F_0}{6m\tau}\mathcal{L}^{-1}\{\dfrac{6}{(s+1/m)^4}\}=\dfrac{F_0}{6m\tau}t^3\exp(-t/m)
$$

## Question 4

Given ODE in Ass 2. 3(a):
$$
m\dfrac{d^2y}{dt^2}+ky=F_0\sin(\omega t-\varphi),\qquad y(0)=y'(0)=0
$$
Note that 
$$
\sin(\omega t-\varphi)=\cos\varphi\sin\omega t-\sin\varphi\cos\omega t
$$
**Step 1: Laplace Transform**

Since here

- $\mathcal{L}(y''(t))(s)=s^2Y(s)-sy(0)-y'(0)=s^2 Y(s)$
- $\mathcal{L}(y(t))(s)=Y(s)$

By the linearity of Laplace Transform, we have 
$$
\left\{\begin{array}{l}
\mathcal{L}(LHS)&=\mathcal{L}\{m \dfrac{d^2y}{dt^2}+ky\}=m \mathcal{L}\{\dfrac{d^2y}{dt^2}\}+k\mathcal{L}\{y\}\\
&=(ms^2+k)Y(s)\\
\mathcal{L}(RHS)&=F_0\cos\varphi\mathcal{L}\{\sin\omega t\}-F_0\sin\varphi\mathcal{L}\{\cos\omega t\}\\
&=F_0\dfrac{\omega\cos\varphi}{s^2+\omega^2}-F_0\dfrac{s\sin\varphi}{s^2+\omega^2}=F_0\dfrac{\omega\cos\varphi-s\sin\varphi}{s^2+\omega^2}
\end{array}\right.
$$
Thus
$$
(ms^2+k)Y(s)=F_0\dfrac{\omega\cos\varphi-s\sin\varphi}{s^2+\omega^2}
$$
which leads to 
$$
\begin{array}{rl}
Y(s)=\dfrac{F_0}{m}\dfrac{\omega\cos\varphi-s\sin\varphi}{(s^2+\omega^2)(s^2+k/m)}=F_0{\omega\cos\varphi}F_1(s)-F_0\sin\varphi F_2(s)
\end{array}
$$
**Step 2: Formal Solution**
$$
\begin{array}{rl}
\mathcal{L}^{-1}(Y(s))&=\mathcal{L}^{-1}\{F_0\omega\cos\varphi F_1(s)-F_0\sin\varphi F_2(s)\}\\
&=F_0(\omega\cos\varphi)\mathcal{L}^{-1}\{F_1(s)\}-F_0\sin\varphi\mathcal{L}^{-1}\{F_2(s)\}\\
&=F_0\omega\cos\varphi f_1(t)-F_0\sin\varphi f_2(t)
\end{array}
$$
**Step 3: Invert $F_i(s)$**, referring to the inversed Laplace Transform table,

Note that $F_1(s)=\dfrac{1}{m \omega^2-k}\dfrac{1}{s^2+k/m}-\dfrac{1}{m\omega^2-k}\dfrac{1}{s^2+\omega^2}$, we have
$$
f_1(t)=\mathcal{L}^{-1}\{F_1(s)\}(t)=\dfrac{1}{m \omega^2-k}\left[\mathcal{L}^{-1}\{\dfrac{1}{s^2+k/m}\}-\mathcal{L}^{-1}\{\dfrac{1}{s^2+\omega^2}\}\right]=\dfrac{1}{m \omega^2-k}\left[\sqrt{\dfrac{m}{k}}\sin\sqrt{\dfrac{k}{m}t}-\dfrac{1}{\omega}\sin\omega t\right]
$$
Also note that $F_2(s)=\dfrac{s}{\left(s^2+w^2\right) \left(k-m w^2\right)}-\dfrac{m
   s}{\left(k+m s^2\right) \left(k-m w^2\right)}$, we have
$$
f_2(t)=\mathcal{L}^{-1}\{F_2(s)\}(t)=\dfrac{1}{m \omega^2-k}\left[\mathcal{L}^{-1}\{\dfrac{1}{s^2+k/m}\}-\mathcal{L}^{-1}\{\dfrac{s}{s^2+\omega^2}\}\right]=\dfrac{1}{m \omega^2-k}\left[\cos (\sqrt{\dfrac{k}{m}}t)-\cos \omega t\right]
$$
**Step 4: Insert the $f_i(t)$ into the formal solution**
$$
\begin{array}{rl}
y(t)&=F_0\omega\cos\varphi f_1(t)-F_0\sin\varphi f_2(t)\\
&=\dfrac{F_0\omega \cos\varphi}{m \omega^2-k}\left[\sqrt{\dfrac{m}{k}}\sin\sqrt{\dfrac{k}{m}t}-\dfrac{1}{\omega}\sin\omega t\right]-\dfrac{F_0\sin\varphi}{m \omega^2-k}\left[\cos (\sqrt{\dfrac{k}{m}}t)-\cos \omega t\right]\\
&=\dfrac{F_0\sin\varphi\cos\sqrt{\dfrac{k}{m}}t}{-m\omega^2+k}+\dfrac{\omega F_0\cos\varphi\sin\sqrt{\dfrac{k}{m}}t}{m\omega^2-k}\sqrt{\dfrac{m}{k}}+\dfrac{F_0}{-m\omega^2+k}\sin(\omega t-\varphi)
\end{array}
$$

## Question 5

Given ODE in Ass 2. 3(b):
$$
m\dfrac{d^2y}{dt^2}+ky=F_0\sin(\omega t-\varphi),\quad\omega=\sqrt{\dfrac{k}{m}},\quad y(0)=0,y'(0)=0
$$
Also, we'd mention that
$$
\sin(\omega t-\varphi)=\cos\varphi\sin\omega t-\sin\varphi\cos\omega t
$$
The former steps are exactly same as in Q4.

**Step 1: Laplace Transform**

Since here

- $\mathcal{L}(y''(t))(s)=s^2Y(s)-sy(0)-y'(0)=s^2 Y(s)$
- $\mathcal{L}(y(t))(s)=Y(s)$

By the linearity of Laplace Transform, we have 
$$
\left\{\begin{array}{l}
\mathcal{L}(LHS)&=\mathcal{L}\{m \dfrac{d^2y}{dt^2}+ky\}=m \mathcal{L}\{\dfrac{d^2y}{dt^2}\}+k\mathcal{L}\{y\}\\
&=(ms^2+k)Y(s)\\
\mathcal{L}(RHS)&=F_0\cos\varphi\mathcal{L}\{\sin\omega t\}-F_0\sin\varphi\mathcal{L}\{\cos\omega t\}\\
&=F_0\dfrac{\omega\cos\varphi}{s^2+\omega^2}-F_0\dfrac{s\sin\varphi}{s^2+\omega^2}=F_0\dfrac{\omega\cos\varphi-s\sin\varphi}{s^2+\omega^2}
\end{array}\right.
$$
Thus
$$
(ms^2+k)Y(s)=mF_0\dfrac{\omega\cos\varphi-s\sin\varphi}{ms^2+k}
$$
which leads to 
$$
\begin{array}{rl}
Y(s)=mF_0\dfrac{\omega\cos\varphi-s\sin\varphi}{(ms^2+k)^2}=mF_0\omega\cos\varphi F_1(s)-mF_0\sin\varphi F_2(s)
\end{array}
$$
**Step 2: Formal Solution**
$$
\begin{array}{rl}
\mathcal{L}^{-1}(Y(s))&=\mathcal{L}^{-1}\{mF_0\omega\cos\varphi F_1(s)-mF_0\sin\varphi F_2(s)\}\\
&=F_0m\omega\cos\varphi\mathcal{L}^{-1}\{F_1(s)\}-F_0m\sin\varphi\mathcal{L}^{-1}\{F_2(s)\}\\
&=F_0m\omega\cos\varphi f_1(t)-F_0m\sin\varphi f_2(t)
\end{array}
$$
**Step 3: Invert $F_i(s)$**, referring to the inversed Laplace Transform table,

Note that $F_1(s)=\dfrac{1}{2mk}\left[\dfrac{1}{s^2+k/m}-\dfrac{m^2s^2-km}{(ms^2+k)^2}\right]$, $\dfrac{m^2s^2-km}{(ms^2+k)^2}=\left[-\dfrac{ms}{ms^2+k}\right]'$ and $\mathcal{L}\{t^nf(t)\}=(-1)^nF^{(n)}(s)$, we have
$$
f_1(t)=\mathcal{L}^{-1}\{F_1(s)\}(t)=\dfrac{1}{2mk}\left[\mathcal{L}^{-1}\{\dfrac{1}{s^2+k/m}\}-\mathcal{L}^{-1}\{\dfrac{m^2s^2-km}{(ms^2+k)^2}\}\right]=\dfrac{1}{2k\sqrt{km}}\sin\sqrt{\dfrac{k}{m}t}-\dfrac{1}{2km}t\cos\sqrt{\dfrac{k}{m}t}
$$
Also note that $F_2(s)=\left[-\dfrac{1}{2 m \left(k+m s^2\right)}\right]'$, we have
$$
f_2(t)=\mathcal{L}^{-1}\{F_2(s)\}(t)=\dfrac{1}{2m\sqrt{mk}}\sin\sqrt{\dfrac{k}{m}t}
$$
**Step 4: Insert the $f_i(t)$ into the formal solution**
$$
\begin{array}{rl}
y(t)&=mF_0\omega\cos\varphi f_1(t)-mF_0\sin\varphi f_2(t)\\
&=\dfrac{mF_0\omega\cos\varphi}{2k\sqrt{km}}\sin\sqrt{\dfrac{k}{m}t}-\dfrac{F_0\omega\cos\varphi}{2k}t\cos\sqrt{\dfrac{k}{m}t}-\dfrac{F_0\sin\varphi}{2\sqrt{mk}}\sin\sqrt{\dfrac{k}{m}t}
\end{array}
$$

## Question 6

Given ODE:
$$
L\dfrac{d^2Q}{dt^2}+R\dfrac{dQ}{dt}+\dfrac{1}{C}Q=E(t),\qquad Q(0)=Q_0,Q'(0)=I_0
$$
where
$$
E(t)=\left\{\begin{array}{ll}
2t+1&1\leq t\leq 2\\
0&\text{otherwise}
\end{array}\right.=(2t+1)(U(t-1)-U(t-2))
$$
where $U$ is the Heaviside step function. If the resistance is zero, then
$$
L\dfrac{d^2Q}{dt^2}+\dfrac{1}{C}Q=E(t),\qquad Q(0)=Q_0,Q'(0)=I_0
$$


#### a) Take the Laplace Transform of $E(t)$.

For convenience, let $g(t)=2t+1$, By the definition,
$$
\begin{array}{rl}
\hat{E}(s)&\displaystyle=\mathcal{L}\{E(t)\}(s)=\mathcal{L}\{g(t)U(t-1)\}(s)-\mathcal{L}\{g(t)U(t-2)\}(s)\\
&\displaystyle=e^{-s}\mathcal{L}\{g(t+1)\}(s)-e^{-2s}\mathcal{L}\{g(t+2)\}(s)\\
&\displaystyle=e^{-s}\mathcal{L}\{2t+3\}(s)-e^{-2s}\mathcal{L}\{2t+5\}(s)\\
&\displaystyle=e^{-s}(\dfrac{2}{s^2}+\dfrac{3}{s})-e^{-2s}(\dfrac{2}{s^2}+\dfrac{5}{s})
\end{array}
$$

#### b) Answer:

Because the expression on the right hand side is depicting the external energy (or force) input in this ODE. "Switched on" is similar to saying switching on the power.

Mathematically speaking, "Switching on" the piecewise function gives the right hand side a support on the region $t\geqslant0$.

#### c) Solving

**Step 1: Laplace Transform**

Since here

- $\mathcal{L}(Q''(t))(s)=s^2W(s)-sQ(0)-Q'(0)=s^2 W(s)-sQ_0-I_0$
- $\mathcal{L}(Q(t))(s)=W(s)$

By the linearity of Laplace Transform, we have 
$$
=\left\{\begin{array}{l}
\mathcal{L}(LHS)&=\mathcal{L}\{L\dfrac{d^2Q}{dt^2}+\dfrac{1}{C}Q\}=L \mathcal{L}\{\dfrac{d^2Q}{dt^2}\}+\dfrac{1}{C}\mathcal{L}\{Q\}\\
&=(Ls^2+\dfrac{1}{C})W(s)-(sLQ_0+LI_0)\\
\mathcal{L}(RHS)&=\hat{E}(s)=e^{-s}(\dfrac{2}{s^2}+\dfrac{3}{s})-e^{-2s}(\dfrac{2}{s^2}+\dfrac{5}{s})
\end{array}\right.
$$
Thus
$$
W(s)=\dfrac{1}{Ls^2+1/C}\left[e^{-s}(\dfrac{2}{s^2}+\dfrac{3}{s})-e^{-2s}(\dfrac{2}{s^2}+\dfrac{5}{s})+sQ_0+I_0\right]
$$
**Step 2: Formal Solution**
$$
\begin{array}{rl}
\mathcal{L}^{-1}(W(s))&=\mathcal{L}^{-1}\{\dfrac{1}{Ls^2+1/C}\left[e^{-s}(\dfrac{2}{s^2}+\dfrac{3}{s})-e^{-2s}(\dfrac{2}{s^2}+\dfrac{5}{s})+sLQ_0+LI_0\right]\}\\
&=2\mathcal{L}^{-1}\{e^{-s}F_3(s)\}+3\mathcal{L}^{-1}\{e^{-s}F_4(s)\}-2\mathcal{L}^{-1}\{e^{-2s}F_3(s)\}-5\mathcal{L}^{-1}\{e^{-2s} F_4(s)\}+Q_0F_2(s)+I_0 F_1(s)\\
&=2f_3(t-1)U(t-1)+3f_4(t-1)U(t-1)-2f_3(t-2)U(t-2)-5f_4(t-2)U(t-2)+Q_0L f_2(t)+I_0L f_1(t)
\end{array}
$$
**Step 3: Invert $F_i(s)$**, referring to the inversed Laplace Transform table,

1. $f_1(t)=\mathcal{L}^{-1}\{F_1(s)\}=\sqrt{\dfrac{C}{L}}\mathcal{L}^{-1}\{\dfrac{1/\sqrt{LC}}{s^2+1/(LC)}\}=\sqrt{\dfrac{C}{L}}\sin\sqrt{\dfrac{1}{LC}}t$
2. $f_2(t)=\mathcal{L}^{-1}\{F_2(s)\}=\dfrac{1}{L}\mathcal{L}^{-1}\{\dfrac{s}{s^2+1/(LC)}\}=\dfrac{1}{L}\cos\sqrt{\dfrac{1}{LC}}t$
3. $f_3(t)=\mathcal{L}^{-1}\{F_3(s)\}=C\mathcal{L}^{-1}\{\dfrac{1}{s^2}\}-C\sqrt{LC}\mathcal{L}^{-1}\{\dfrac{1/\sqrt{LC}}{s^2+1/(LC)}\}=Ct-C\sqrt{LC}\sin\sqrt{\dfrac{1}{LC}}t$
4. $f_4(t)=\mathcal{L}^{-1}\{F_4(s)\}=C\mathcal{L}^{-1}\{\dfrac{1}{s}\}-C\mathcal{L}^{-1}\{\dfrac{s}{s^2+1/(LC)}\}=C-C\cos\sqrt{\dfrac{1}{LC}}t$

**Step 4: Insert the $f_i(t)$ into the formal solution**
$$
\begin{array}{rl}
y(t)&=2f_3(t-1)U(t-1)+3f_4(t-1)U(t-1)-2f_3(t-2)U(t-2)-5f_4(t-2)U(t-2)+Q_0 f_2(t)+I_0 f_1(t)\\
&=\text{(Too long, intermediate steps including simplification omitted)}\\
&=Q_0\cos\dfrac{t}{\sqrt{LC}}+\sqrt{LC}I_0\sin\dfrac{t}{\sqrt{LC}}+\left[2\sqrt{CL}\sin\dfrac{t-2}{LC}+5\cos\dfrac{t-2}{\sqrt{LC}}-2t-1\right]CU(t-2)+\\
&\ \ \left[-2\sqrt{CL}\sin\dfrac{t-1}{LC}-3\cos\dfrac{t-1}{\sqrt{LC}}+2t+1\right]CU(t-1)
\end{array}
$$

#### e) Verify

Let $t\geqslant 2$, then $U(t-1)=U(t-2)=1$,
$$
\begin{array}{rl}
y(t)&=Q_0\cos\dfrac{t}{\sqrt{LC}}+\sqrt{LC}I_0\sin\dfrac{t}{\sqrt{LC}}+\left[2\sqrt{CL}\sin\dfrac{t-2}{LC}+5\cos\dfrac{t-2}{\sqrt{LC}}-2t-1\right]C+\\
&\ \ \left[-2\sqrt{CL}\sin\dfrac{t-1}{LC}-3\cos\dfrac{t-1}{\sqrt{LC}}+2t+1\right]C\\
&=5C\cos\dfrac{t-2}{\sqrt{LC}}-3C\cos\dfrac{t-1}{\sqrt{LC}}+Q_0\cos\dfrac{t}{\sqrt{LC}}+2C\sqrt{LC}\sin\dfrac{t-1}{\sqrt{LC}}+2C\sqrt{LC}\sin\dfrac{t-2}{\sqrt{LC}}\\
&\ \ +I_0\sqrt{LC}\sin\dfrac{t}{\sqrt{LC}}
\end{array}
$$
Hence we can observe that the constant and linear terms in $t$ all cancel out.

## Question 7

The given ODE in Ass 2. Q3.(a) is
$$
m\dfrac{d^2y}{dt^2}+ky=f(t),\qquad y(0)=y'(0)=0
$$
The corresponding unit impulse function is
$$
m\dfrac{d^2y}{dt^2}+ky=\delta(t-\tau)
$$
where $\tau>0$ is the hitting time, and $\delta $ is the Dirac delta function. Applying the Laplace Transform, we have

- $\mathcal{L}(y''(t))(s)=s^2Y(s)-sy(0)-y'(0)=s^2 Y(s)$
- $\mathcal{L}(y(t))(s)=Y(s)$

By the linearity of Laplace Transform, we have 
$$
\left\{\begin{array}{l}
\mathcal{L}(LHS)&=\mathcal{L}\{m \dfrac{d^2y}{dt^2}+ky\}=m \mathcal{L}\{\dfrac{d^2y}{dt^2}\}+k\mathcal{L}\{y\}\\
&=(ms^2+k)Y(s)\\
\mathcal{L}(RHS)&=\mathcal{L}\{\delta(t-\tau)\}=\exp(-\tau s)
\end{array}\right.
$$
Thus
$$
Y(s)=\dfrac{\exp(-\tau s)}{ms^2+k}
$$
and
$$
y(t)=\mathcal{L}^{-1}\{Y(s)\}(t)=\dfrac{\sin{\sqrt{\dfrac{k}{m}}(t-\tau)}}{\sqrt{mk}}U(t-\tau)
$$
Hence the unit impulse response function is
$$
h(t-\tau)=\dfrac{\sin{\sqrt{\dfrac{k}{m}}(t-\tau)}}{\sqrt{mk}}
$$

## Question 8

#### a)

The ODE in Ass 2. Q5 is
$$
\left\{\begin{array}{l}
\dfrac{dM_1}{dt}=\underbrace{QC_{in}}_{\text{external input}}+\underbrace{a\dfrac{M_2}{V}}_{\text{from Tank 2}}-\underbrace{(Q+a)\dfrac{M_1}{V}}_{\text{to Tank2}}\\
\dfrac{dM_2}{dt}=\underbrace{(Q+a)\dfrac{M_1}{V}}_{\text{from Tank1}}-\underbrace{a\dfrac{M_2}{V}}_{\text{to Tank 1}}-\underbrace{Q\dfrac{M_2}{V}}_{\text{output}}
\end{array}\right.
$$

convert it to matrix form we have
$$
\dfrac{dX}{dt}=\dfrac{1}{V}\begin{bmatrix}-(Q+a)&a\\(Q+a)&-a-Q\end{bmatrix}X+\begin{bmatrix}QC_{in}\\0\end{bmatrix}=AX+b
$$

**Step 1: Laplace Transform** Since

- $\mathcal{L}\{M_1'\}=s W_1(s)-M_1(0)=s W_1(s)$
- $\mathcal{L}\{M_2'\}=s Q(s)-M_2(0)=s Q(s)$

Applying the Laplace Transform to both sides, we have

- $\mathcal{L}\{M_1'\}=sW_1(s)=QC_{in}\mathcal{L}\{1\}+\dfrac{a}{V}\mathcal{L}\{M_2\}-\dfrac{(Q+a)}{V}\mathcal{L}\{M_1\}=\dfrac{QC_{in}}{s}+\dfrac{a}{V}Q(s)-\dfrac{Q+a}{V}W_1(s)$
- $\mathcal{L}\{M_2'\}=sQ(s)=\dfrac{Q+a}{V}\mathcal{L}\{M_1\}-\dfrac{Q+a}{V}\mathcal{L}\{M_2\}=\dfrac{Q+a}{V}W_1(s)-\dfrac{Q+a}{V}Q(s)$

Solve the equations, we have

- $W_1(s)=\dfrac{C_{in}Qs+\dfrac{C_{in}Q}{V}(Q+a)}{s\left[(s+\dfrac{Q+a}{V})^2-\dfrac{a(Q+a)}{V^2}\right]}=C_{in}QF_1(s)$

- $Q(s)=\dfrac{C_{in}Q\dfrac{Q+a}{V}}{s\left[(s+\dfrac{Q+a}{V})^2-\dfrac{a(Q+a)}{V^2}\right]}=C_{in}QF_2(s)$

**Step 2: Formal Solution**

- $M_1(t)=\mathcal{L}^{-1}\{W_1(s)\}(t)=\mathcal{L}^{-1}\{C_{in}QF_1(s)\}(t)=C_{in}Q\mathcal{L}^{-1}\{F_1(s)\}(t)=C_{in}Q f_1(t)$
- $M_2(t)=\mathcal{L}^{-1}\{Q(s)\}(t)=\mathcal{L}^{-1}\{C_{in}QF_2(s)\}(t)=C_{in}Q\mathcal{L}^{-1}\{F_2(s)\}(t)=C_{in}Q f_2(t)$

**Step 3: Invert $F_i(s)$**

Note that $(s+\dfrac{Q+a}{V})^2-\dfrac{a(Q+a)}{V^2}=(s+\dfrac{Q+a}{V}-\dfrac{\sqrt{a(Q+a)}}{V})(s+\dfrac{Q+a}{V}+\dfrac{\sqrt{a(Q+a)}}{V})$, for convenience, let $\alpha=\dfrac{Q+a}{V}$, $\beta=\dfrac{\sqrt{a(Q+a)}}{V}$, $s_1=-\alpha+\beta,s_2=-\alpha-\beta$, then 

- $F_1(s)=\dfrac{s+\alpha }{s(s-s_1)(s-s_2)}=\dfrac{\alpha }{s_1s_2}\dfrac{1}{s}+\dfrac{1}{2s_1}\dfrac{1}{s-s_1}+\dfrac{1}{2s_2}\dfrac{1}{s-s_2}$
- $F_2(s)=\dfrac{\alpha }{s(s-s_1)(s-s_2)}=\dfrac{\alpha }{s_1s_2}\dfrac{1}{s}+\dfrac{\alpha }{2\beta s_1}\dfrac{1}{s-s_1}+\dfrac{\alpha }{2\beta s_2}\dfrac{1}{s-s_2}$

Hence,

- $$
  \begin{array}{rl}
  f_1(t)&=\mathcal{L}^{-1}\{F_1(s)\}=\dfrac{\alpha }{s_1s_2}\mathcal{L}^{-1}\{\dfrac{1}{s}\}+\dfrac{1}{2s_1}\mathcal{L}^{-1}\{\dfrac{1}{s-s_1}\}+\dfrac{1}{2s_2}\mathcal{L}^{-1}\{\dfrac{1}{s-s_2}\}\\
  &=\dfrac{\alpha }{s_1s_2}+\dfrac{1}{2s_1}\exp(s_1t)+\dfrac{1}{2s_2}\exp(s_2t)
  \end{array}
  $$

- $$
  \begin{array}{rl}f_2(t)
  &=\mathcal{L}^{-1}\{F_2(s)\}=\dfrac{\alpha }{s_1s_2}\mathcal{L}^{-1}\{\dfrac{1}{s}\}+\dfrac{\alpha }{2\beta s_1}\mathcal{L}^{-1}\{\dfrac{\alpha }{s-s_1}\}+\dfrac{\alpha }{2\beta s_2}\mathcal{L}^{-1}\{\dfrac{1}{s-s_2}\}\\
  &=\dfrac{\alpha }{s_1s_2}+\dfrac{\alpha }{2 s_1}\exp(s_1t)+\dfrac{\alpha }{2\beta s_2}\exp(s_2t)\end{array}
  $$

**Step 4: Solution**

Insert $f_i(t)$ back into $M_i$, we have
$$
M_1(t)=C_{in}Q f_1(t)=\dfrac{\alpha C_{in}Q }{s_1s_2}+\dfrac{C_{in}Q}{2s_1}\exp(s_1t)+\dfrac{C_{in}Q}{2s_2}\exp(s_2t)\\
M_2(t)=C_{in}Q f_2(t)=\dfrac{\alpha C_{in}Q}{s_1s_2}+\dfrac{\alpha C_{in}Q}{2\beta s_1}\exp(s_1t)+\dfrac{\alpha C_{in}Q}{2\beta s_2}\exp(s_2t)
$$

#### b) Answers

1. $s_1-s_2=2\beta=\dfrac{2(Q+a)}{V}$

2. $s_1+\alpha=\beta=\dfrac{\sqrt{a(Q+a)}}{V}$

3. $s_2+\alpha=-\beta=-\dfrac{\sqrt{a(Q+a)}}{V}$

4. $\dfrac{s_1+\alpha}{s_1(s_1-s_2)}=\dfrac{\beta}{2\beta(\beta-\alpha)}=\dfrac{1}{2(\beta-\alpha)}=\dfrac{1}{2 \left(\dfrac{\sqrt{a (a+Q)}}{V}-\dfrac{a+Q}{V}\right)}$

   $\dfrac{s_2+\alpha}{s_2(s_2-s_1)}=\dfrac{-\beta}{-2\beta(-\beta-\alpha)}=\dfrac{1}{2(-\beta-\alpha)}=-\dfrac{1}{2 \left(\dfrac{\sqrt{a (a+Q)}}{V}+\dfrac{a+Q}{V}\right)}$

5. $s_1s_2=\alpha^2-\beta^2=\dfrac{Q(Q+a)}{V^2}$

#### c) Answers

1. $s_1s_2=\alpha^2-\beta^2=\dfrac{Q(Q+a)}{V^2}$
2. $\dfrac{\alpha}{s_1s_2}=\dfrac{Q+a}{V}\dfrac{V^2}{Q(Q+a)}=\dfrac{V}{Q}$

#### d) Answers

$$
M_1(t)=\dfrac{\alpha C_{in}Q }{s_1s_2}+\dfrac{C_{in}Q}{2s_1}\exp(s_1t)+\dfrac{C_{in}Q}{2s_2}\exp(s_2t)=VC_{in}-\dfrac{QC_{in}}{2}\dfrac{1}{\alpha-\beta}\exp(-(\alpha-\beta)t)-\dfrac{QC_{in}}{2}\dfrac{1}{\alpha+\beta}\exp(-(\alpha+\beta)t)\\
M_2(t)=\dfrac{\alpha C_{in}Q}{s_1s_2}+\dfrac{\alpha C_{in}Q}{2\beta s_1}\exp(s_1t)+\dfrac{\alpha C_{in}Q}{2\beta s_2}\exp(s_2t)=VC_{in}-\dfrac{QC_{in}\alpha}{2\beta}\dfrac{1}{\alpha-\beta}\exp(-(\alpha-\beta)t)-\dfrac{QC_{in}\alpha}{2\beta}\dfrac{1}{\alpha+\beta}\exp(-(\alpha+\beta)t)
$$

#### e) 

Since $\alpha-\beta=\dfrac{Q+a}{V}-\dfrac{\sqrt{a(Q+a)}}{V}=\dfrac{\sqrt{Q+a}}{V}(\sqrt{Q+a}-\sqrt a) >0$, $\alpha+\beta>0$, we have
$$
\lim_{t\to +\infty}\exp(-(\alpha-\beta)t)=\lim_{t\to +\infty}\exp(-(\alpha+\beta)t)=0
$$
therefore
$$
\lim_{t\to +\infty}M_1(t)=VC_{in}-0-0=VC_{in},\qquad \lim_{t\to +\infty}M_2(t)=VC_{in}-0-0=VC_{in}
$$

#### f) by b) c)

$$
M_1(0)=VC_{in}-\dfrac{QC_{in}}{2}\dfrac{1}{\alpha-\beta}-\dfrac{QC_{in}}{2}\dfrac{1}{\alpha+\beta}=VC_{in}-\dfrac{QC_{in}}{2}\dfrac{2\alpha}{\alpha^2-\beta^2}=VC_{in}-VC_{in}=0\\
M_2(0)=VC_{in}-\dfrac{QC_{in}\alpha}{2\beta}\dfrac{1}{\alpha-\beta}-\dfrac{QC_{in}\alpha}{2\beta}\dfrac{1}{\alpha+\beta}=VC_{in}-\dfrac{2QC_{in}\alpha^2}{2s_1s_2\beta}=VC_{in}-VC_{in}=0
$$























