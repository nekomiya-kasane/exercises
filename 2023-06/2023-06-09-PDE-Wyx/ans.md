

## Q4

From the second Taylor series, we have
$$
\begin{align}
y_{i+1}&=y_i+\Delta x\left[f(x_i,y_i)+\dfrac{\Delta x}{2}(\dfrac{\partial f}{\partial x}+\dfrac{\partial f}{\partial y} f(x_i,y_i))\right]\\
&=y_i+F(\Delta x, x_i, y_i)\Delta x\\
\end{align}
$$
The **local error** is 
$$
\begin{align}
\tau_{n+1}&=y(x_{n+1})-\left[y(x_n)- F(\Delta x,x_n,y(x_n))\Delta x\right]\\
&=y'(x_n) \Delta x+\dfrac{\Delta x^2}{2}y''(x_n)-F(\Delta x,x_n,y(x_n))\Delta x\\
&=\dfrac{\Delta x^2}{2}y''(x_n)+\dfrac{\Delta x^2}{2}\left(\dfrac{\partial f}{\partial x}+\dfrac{\partial f}{\partial y} f(x_n,y_n)\right)\\
&=\Delta x^2 y''(x_n)\\ &\sim \mathcal{O}(\Delta x^2)
\end{align}
$$
The **global error** is 
$$
\begin{align}
e_{n}&=y(x_n)-y_n\\
&=y(x_n)-y(x_{n-1})+y(x_{n-1})-y_{n-1}+y_{n-1}-y_n\\
&=\int_{x_{n-1}}^{x_n}f(x,y)dx+e_{n-1}-\Delta F(\Delta x,x_{n-1},y_{n-1})\\
&=e_{n-1}+\int_{x_{n-1}}^{x_n}[f(x,y)-F(\Delta x,x_{n-1},y_{n-1})]dx\\
&=e_{n-1}+\int_{x_{n-1}^{x_n}}[f(x,y)-f(x_{n-1},y_{n-1})+f(x_{n-1},y_{n-1})-F(\Delta x,x_{n-1},y_{n-1})]dx
\end{align}
$$
Since $F$ is Lipschitz continuous, hence $\exists\ L>0$ such that
$$
\begin{align}
|f(x_{n-1},y_{n-1})-F(\Delta x,x_{n-1},y_{n-1})|&=|F(\Delta x,x_{n-1},y(x_{n-1})))-F(\Delta x,x_{n-1},y_{n-1})|\\
&\leqslant L|y(x_{n-1})-y_{n-1}|=L|e_{n-1}|
\end{align}
$$
from which we can derive that
$$
\begin{align}
|e_{n}|&\leqslant |e_{n-1}|(1+\Delta x L)+\left|\int_{x_{n-1}}^{x_{n}} f(x,y)-f(x_{n-1},y(x_{n-1}))dx\right|\\
&\leqslant  |e_{n-1}|(1+\Delta x L)+\left|\int_{x_{n-1}}^{x_{n}} f(x,y)-f(x_{n-1},y)+f(x_{n-1},y)-f(x_{n-1},y(x_{n-1}))dx\right|\\
&\leqslant |e_{n-1}|(1+\Delta x L) +\dfrac{K}{2}\Delta x^2+L M\dfrac{\Delta  x^2}{2}\\
&\leqslant  (1+\Delta x L)|e_{n-1}| +C\Delta x^2
\end{align}
$$
where $C$ is a non-negative constant.

## Q5

==**(a)**== Taylor expansion:
$$
\begin{align}
\Phi(x,y,\Delta x)&=f(x+\alpha\Delta,y+\beta \Delta x f(x,y))\\
&=f(x,y)+\alpha \Delta x\dfrac{\partial f}{\partial x}(x,y)+\beta \Delta x f(x,y)\dfrac{\partial f}{\partial y}(x,y)+o(\Delta ^2)
\end{align}
$$
==**(b)**==
$$
y{(x_{n+1})}-y({x_n})=\Delta x\gamma_1f{(x_n,y({x_n}))}+\Delta x\gamma_2f{(x_n,y({x_n}))}+\alpha\Delta x^2\gamma_2\frac{\partial f}{\partial x}(x_n,y(x_n))+\beta\Delta x^2\gamma_2f{(x_n,y({x_n}))}\frac{\partial f}{\partial y}(x_n,y(x_n))+o(\Delta x^3)
$$
If let this is consistent, we must have
$$
\begin{align}
&\Delta x\gamma_1f{(x_n,y{(x_n)})}+\Delta x\gamma_2f{(x_n,y{(x_n)})}+\Delta x^2\alpha \gamma_2\frac{\partial f}{\partial x}+ \beta \Delta x^2\gamma_2f{(x_n,y{(x_n)})}\frac{\partial f}{\partial y}\\
=&\Delta x f(x_n,y(x_n))+\dfrac{\Delta x^2}{2}(\dfrac{\partial f}{\partial x}+\dfrac{\partial f}{\partial y}f(x_n,y(x_n)))
\end{align}
$$
Comparing the coefficients, we have
$$
\begin{cases}
1-\gamma_1-\gamma_2=0\\
\dfrac{1}{2}-\alpha \gamma_2=0\\
\dfrac{1}{2}-\beta\gamma_2=0
\end{cases}
$$
==**(c)**== Plug in the given values $\gamma_1=0,\  \gamma_2=1, \ \alpha=\beta=\dfrac{1}{2}$, we have 
$$
y_{n+1}=y_n + \Delta xf{(x_n+\frac{1}{2}\Delta x,y_n+\frac{1}{2}\Delta xf{(x_n,y_n)})}
$$
$y'=\lambda y$ implies 
$$
y_{n+1}=y_n+\Delta x\lambda (y_n+\dfrac{1}{2}\Delta x \lambda y_n)=y_n(1+\lambda \Delta x+\dfrac{1}{2}\Delta x^2\lambda^2)
$$
So the stability region $B$ satisfies 
$$
|1+\Delta x\lambda+\dfrac{1}{2}\Delta x^2\lambda^2|<1
$$
The boundaries of the region of stable $∆x$ are defined by 
$$
\Delta x\lambda(1+\dfrac{1}{2}\Delta x\lambda)=0,\Delta x\lambda(1+\frac{1}{2}\Delta x\lambda)=-2
$$
Which implies the condition on the stepsize is $0<\Delta x<\dfrac{2}{|\lambda|}$ , which is equal to Euler's method.

==**(d)**== The highest accuracy of 2-nd RK method is $\theta(\Delta x^2) $ by **(b)** we need 
$$
\begin{equation}   \left\{  \begin{array}{**lr**} \gamma_1+\gamma_2=1, & \\ \alpha \gamma_2=\dfrac{1}{2}\\ \beta \gamma_2=\dfrac{1}{2} & \end{array}   \right.   \end{equation}
$$
We can see that the method in Q4 is exactly the $i$-nd RK method when $\gamma_1=0,\ \  r_2 =1,\ \alpha=\beta=\dfrac{1}{2}$.

==**(e)**== The solution represents an approximation to the value of the ODE at specific point in the domain.

## Q6

==**(a)**==
$$
a\dfrac{u(x_{i+1},y_j)-2u(x_i,y_j)+u (x_{i-1},y_j) }{\Delta x^2 }+b\dfrac{u(x_i,y_{j+1})-2u(x_i,y_j)+u (x_i,y_{j-1}) }{\Delta y^2 }=0
$$
==**(b)**== Denote $U(x_i,y_j)=U_{i,j}$, then the formula can be written as 
$$
a\Delta y^2U_{i+1,j}-2a\Delta y^2U_{i,j}+a\Delta y^2U_{i-1,j}+b\Delta x^2U_{x,j+1}-2b\Delta x^2U_{i,j}+b\Delta x^2U_{i,j-1}=0\\
\Leftrightarrow (2a\Delta y^2+2b\Delta x^2)U_{i,j}-a\Delta y^2U_{i+1,j}-a\Delta y^2U_{i-1,j}-b\Delta x^2U_{x,j+1}-b\Delta x^2U_{i,j-1}=0
$$
Plugging in the BCs $U_{i,0}=1,\ \ U_{i,4}=1,\ \ \ U_{0,j}=0,\ \ \ U_{4,j}=0$, we have
$$
(2a\Delta y^2+2b\Delta x^2)U_{1,1}-a\Delta y^2U_{2,1}-b\Delta x^2U_{1,2}-b\Delta x^2=0\\
(2a\Delta y^2+2b\Delta x^2)U_{1,2}-a\Delta y^2U_{2,2}-b\Delta x^2U_{1,3}-b\Delta x^2U_{1,1}=0\\
\cdots\cdots
$$
Which can be written in matrix form
$$
\begin{align}
\Rightarrow
\begin{pmatrix}
D &-b\Delta x^2 & 0 & -a\Delta y^2 & 0 & 0 & 0 & 0 & 0 \\
-b\Delta x^2 & D & -b\Delta x^2 & 0 & -a\Delta y^2 & 0 & 0 & 0 & 0 \\
0 & -b\Delta x^2 & D & 0 & 0 & -a\Delta y^2 & 0 & 0 & 0 \\
-a\Delta y^2 & 0 & 0 & D& -b\Delta x^2 & 0 & 0 & -a\Delta y^2 & 0 & 0 \\
0 & -a\Delta y^2 & 0 & -b\Delta x^2 & D & -b\Delta x^2 & 0 & -a\Delta y^2 & 0 \\
0 & 0 & -a\Delta y^2 & 0  & -b\Delta x^2 & D & -b\Delta x^2 & 0 & -a\Delta y^2\\
0 & 0 & 0 & -a\Delta y^2 & 0 & 0  & D & -b\Delta x^2 & 0 \\
0 & 0 & 0 & 0 & -a\Delta y^2 & 0 & -b\Delta x^2 & D & -b\Delta x^2 \\
0 & 0 & 0 & 0 & 0 & -a\Delta y^2 & 0 & -b\Delta x^2 & D
\end{pmatrix}
\begin{pmatrix}
U_{1,1} \\
U_{1,2} \\
U_{1,3} \\
U_{2,1} \\
U_{2,2} \\
U_{2,3} \\
U_{3,1} \\
U_{3,2} \\
U_{3,3} 
\end{pmatrix}
=
\begin{pmatrix}
b\Delta x^2 \\
0 \\
b\Delta x^2 \\
b\Delta x^2 \\
0 \\
b\Delta x^2 \\
b\Delta x^2 \\
0 \\
b\Delta x^2
\end{pmatrix}
\end{align}
$$

where $2a\Delta y^2+2b\Delta x^2=D$. The equation is in the form $A\mathcal U=\mathcal W$

==**(c)**== Decompose $A = D-L-U$, where

$$
L=\begin{align}
\begin{pmatrix}
0&b\Delta x^2&0&a\Delta y^2&0&0&0&0&0
\\0&0&b\Delta x^2&0&a\Delta y^2&0&0&0&0
\\0&0&0&0&0&a\Delta y^2&0&0&0
\\0&0&0&0&b\Delta x^2&0&a\Delta y^2&0&0
\\0&0&0&0&0&0&0&a\Delta y^2&0
\\0&0&0&0&0&0&0&0&a\Delta y^2
\\0&0&0&0&0&0&0&b\Delta x^2&0
\\0&0&0&0&0&0&0&0&b\Delta x^2
\\0&0&0&0&0&0&0&0&0
\end{pmatrix}
\end{align}
$$

$$
U=\begin{align}
\begin{pmatrix}
0&0&0&0&0&0&0&0&0
\\b\Delta x^2&0&0&0&0&0&0&0&0
\\0&b\Delta x^2&0&0&0&0&0&0&0
\\a\Delta y^2&0&0&0&0&0&0&0&0
\\0&a\Delta y^2&0&0&0&0&0&0&0
\\0&0&a\Delta y^2&0&b\Delta x^2&0&0&0&0
\\0&0&0&a\Delta y^2&0&0&0&0&0
\\0&0&0&0&a\Delta y^2&0&b\Delta x^2&0&0
\\0&0&0&0&0&a\Delta y^2&0&b\Delta x^2&0
\end{pmatrix}
\end{align}
$$

and $D=\mathrm{diag}(2a\Delta^2 x+2b\Delta y^2)$. Furtherly, let $J=D^{-1}(L+U)$, then the Jacobi method's formula is
$$
\mathcal U^{(k+1)}=D^{-1}(b-(L+U)\mathcal{U}^{(k)})
$$
==**(d)**== Similarly, decompose $A=L_*+U$, the GS method's formula is
$$
L_*\mathcal{U}^{(k+1)}=b-U\mathcal{U}^{(k)}
$$
where $L_*$ is the lower and diagonal part of $A$, $U$ is a strictly upper triangular matrix. The iteration formula can be further written as 
$$
\mathcal{U}^{(k+1)}=L_*^{-1}(b-U\mathcal{U}^{(k)})
$$
 ==**(e)**== Note that $2a\Delta y^2+2b\Delta x^2= |-b\Delta x^2|+|-a\Delta y^2|+|b\Delta x^2|+|a\Delta y^2|$ greater or equal than the sum of other elements in the same row, hence the matrix is diagonal dominant. Therefore $A$ meets the convergence condition.

==**(f)**== The solution of the end iteration represents the interior value of $u$ in $[0,1]\times[0,1]$.

## Q7

==**(a)**==

**step1:** Discretize the domain $\Delta$x and $\Delta$y and choose a time step $\Delta$t

**step2:** Form the FD schema
$$
\dfrac{U^{n+1}-U^n}{\Delta t}= c(\dfrac{U_{i+1,j}^n-2U_{i,j}^n+U_{i-1,j}^n}{\Delta x^2}+\dfrac{U_{i,j+1}^n-2U_{i,j}^n+U_{i,j-1}^n}{\Delta y^2})
$$
**step3:** By the given initial condition and boundary conditions, points on the boundary take values
$$
U_{i,j}^0=f(j\Delta x,i\Delta y)\ \ \forall\ 0\leqslant i,j\leqslant N\\
U_{0,j}^n=0,\ \ U_{N,j}^n=1, \ \ U_{i,0}^n=\alpha,\ \ U_{i,N}^n=0
$$
**step4:** Solve the equation and update $U_{i,j}^{n+1}$

**step5:** Stability condition
$$
\dfrac{c\Delta t}{\Delta x^2}+\dfrac{c\Delta t}{\Delta y^2} \leqslant  \dfrac{1}{2}
$$
The truncation error is
$$
T(x,t)=\dfrac{1}{2}\Delta tU_{tt}-\dfrac{1}{12}c((\Delta x)^2U_{ xxxx}+(\Delta y)U_{yyyy}^2)+\cdots
$$
==**(b)**==  

Consider  the method
$$
(1-\dfrac{1}{2}\mu_x\delta_x^2)U^{n+\frac{1}{2}}=(1+\dfrac{1}{2}\mu_y\delta_y^2)U^n
$$

$$
(1-\dfrac{1}{2}\mu_y\delta_y^2)U^{n+1}=(1+\dfrac{1}{2}\mu_x\delta_x^2)U^{n+\frac{1}{2}}
$$

Here 
$$
\mu_x=\dfrac{c\Delta t}{\Delta x^2},\ \  \mu_y =\dfrac{c\Delta t}{\Delta y^2} \ \\\ \delta_x^2U=U{(x+\Delta x,t)}-2U(x,t)+U(x-\Delta x,t)\\\ \delta_y^2U=U{(y+\Delta y,t)}-2U{(y,t)}+U{(y-\Delta y,t)}
$$
Suppose the solution of the scheme is in the form
$$
U_{j,l}^n=\lambda^n e^{i\xi j\Delta x }e^{i\eta l\Delta y}
\\ U_{j,l}^{n+\frac{1}{2}}=\beta\lambda^n e^{i\xi j\Delta x }e^{i\eta l\Delta y}
$$
Applying Von-Neumann stability analysis, we get
$$
(1+4\mu x \sin^2\dfrac{\theta_x}{2})\beta=(1-4\mu_y\sin^2\dfrac{\theta_y}{2})
\\ (1+4\mu x \sin^2\dfrac{\theta_x}{2})\lambda=(\beta +4\mu_y\sin^2\dfrac{\theta_y}{2})
\\ \Rightarrow \lambda=\dfrac{1+16\mu_x\mu_y \sin^2\dfrac{\theta_x}{2}\sin^2\dfrac{\theta_y}{2}}{(1+4\mu_x\sin^2\dfrac{\theta_x}{2})(1+4\mu_y\sin^2\dfrac{\theta_y}{2})}<1
$$
always holds, thus we can conclude that this method is unconditioned stable!

==**(c)**== No, it isn't For convention equation, if we use central difference approximation, it will cause oscillations in the numerical solution. Also, for some boundary conditions containing derivatives, using directed finite difference schema (usually towards inner region) may produce better result.









