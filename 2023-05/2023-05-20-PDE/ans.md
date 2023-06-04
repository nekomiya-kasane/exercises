The problem can be modeled as
$$
\left\{\begin{array}{l}u_{tt}=c^2u_{xx}=u_{xx}\\u(t,0)=u(t,\pi)=0\\u(0,x)=f(x),\ u_t(0,x)=g(x)=0\\\end{array}\right.,\qquad \text{where}\qquad f(x)=\begin{cases}\dfrac{2hx}{\pi}&0\leqslant x\leqslant \dfrac{\pi}{2}\\2h\left(1-\dfrac{x}{\pi}\right)&0<x\leqslant \pi\end{cases}
$$
Apply the method of separation of variables, i.e. let $u(t,x)=T(t)X(x)$, we'd have
$$
\dfrac{T''(t)}{T(t)}=\dfrac{X''(x)}{X(x)}=-\lambda\quad\Rightarrow\quad
\begin{cases}
X(x)=C_1\cos\sqrt{\lambda}x+C_2\sin\sqrt{\lambda}x\\
T(t)=D_1\cos\sqrt{\lambda}t+D_2\sin\sqrt{\lambda}t
\end{cases}
$$
with boundary conditions
$$
X(0)=C_1=0,\quad X(\pi)=C_1\cos\sqrt{\lambda}\pi+C_2\sin\sqrt{\lambda}\pi=0\Rightarrow \lambda_n=n^2,n\in\N
$$
hence the eigenfunctions are 
$$
X_n(x)=\sin nx,\quad T_n(t)=D_{1n}\cos nt+D_{2n}\sin nt\\
u_n(t,x)=X_n(x)T_n(t)=(D_{1n}\cos nt+D_{2n}\sin nt)\sin nx
$$
furtherly,
$$
u(t,x)=\sum_{n=0}^{+\infty}\mu_n u_n(t,x)=\sum_{n=0}^{+\infty}(a_n\cos nt+b_n\sin nt)\sin nx
$$
with initial state 
$$
u(0,x)=\sum_{n=0}^{+\infty}a_n\sin nx=f(x),\quad u_t(0,x)=\sum_{n=0}^{+\infty} nb_n\sin nx=0
$$
Note the base functions $\{\sin nx,\cos nx\}_{n=0}^{+\infty}$ are orthogonal on $L_2([-\pi,\pi])$,
$$
\int_{-\pi}^\pi \sin nx\sin mx=\pi\delta_{n,m}\quad \int_{-\pi}^\pi \cos nx\cos mx=\pi\delta_{n,m}\quad\int_{-\pi}^\pi \cos nx\sin mx=0
$$
So we extend $f(x),g(x)$ to $[-\pi,\pi]$,
$$
\hat f(x)=\begin{cases}f(x)&x\geqslant 0\\-f(-x)&x<0\end{cases},\ \hat g(x)=0
$$
Thus
$$
a_n=\dfrac{1}{\pi}\int_{-\pi}^\pi \hat{f}(x)\sin nx\mathrm{d}x=\dfrac{2}{\pi}\int_{0}^\pi f(x)\sin nx=\frac{2}{\pi}\left[\int_{0}^{\frac{\pi}{2}} \dfrac{2hx}{\pi}\sin nx+\int_{\frac{\pi}{2}}^{\pi} 2h\left(1-\dfrac{x}{\pi}\right)\mathrm{d}x\right]=\begin{cases}0&n\text{ is even}\\
-\dfrac{8h}{(2m+1)^2\pi^2}&n=2m+1,m\text{ is odd}\\
\dfrac{8h}{(2m+1)^2\pi^2}&n=2m+1,m\text{ is even}\\
\end{cases}\\
b_n=\dfrac{1}{\pi}\int_{-\pi}^\pi \hat{g}(x)\cos nx\mathrm{d}x=0
$$
Hence 
$$
u(t,x)=\sum_{m=0}^{+\infty}\dfrac{8h(-1)^m}{(2m+1)^2\pi^2}\cos (2m+1)t\sin(2m+1)x
$$


