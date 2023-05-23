# Assignment 4

**Zeyuan Wei 46484354**

## Problem 1 $\def\ra{\Rightarrow}\def\t{\theta}\def\pp#1#2{\dfrac{\partial #1}{\partial #2}}\def\re{\mathrm{Re }}\def\im{\mathrm{Im }}     $

$$
\begin{cases}
\dot x=-\mu xy+y\\
\dot y=\mu xy-y
\end{cases}
$$

_(a)_ Let $T(t)=x(t)+y(t)$, then $\dot T(x)=\dot x+\dot y=(-\mu xy+y)+(\mu xy-y)=0$

Hence $\displaystyle 0=\int_0^x \dot T(t)dt=T(x)-L(0)$, i.e. $T(x)\equiv T(0)$. $T$ is conserved.

_(b)_ $T(0)=400$, by (a), we have $T(t)=x(t)+y(t)\equiv 400$. Thus $y=x-400$. Plug it into $\dot x$, we have
$$
\dot x=(1-\mu x)y=(1-\mu x)(400-x)=f(x,\mu)
$$
_(c)_ At the fixed points, we have 
$$
\dot x = 0\quad \Rightarrow \quad (1-\mu x)(400-x)=0\quad \Rightarrow\quad x_1=400,x_2=\dfrac{1}{\mu}
$$
Since $f_x(x,\mu)=2\mu x-(1+400\mu)$, $f_{xx}(x,\mu)=2\mu$
$$
f_x(x_1,\mu)=400\mu-1,\quad f_x(x_2,\mu)=1-400\mu,\quad f_{xx}(x_2)=f_{xx}(x_1)=2\mu
$$

1. If $\mu<\dfrac{1}{400}$, then $x_2>x_1$, $f_x(x_1,\mu)<0,f_x(x_2,\mu)>0$, hence we can plot

   <img src="Assignment%204.assets/image-20230522083641990.png" alt="image-20230522083641990" style="zoom:30%;" />

   $x_1$ is stable while $x_2$ is unstable.

2. If $\mu>\dfrac{1}{400}$, then $x_2<x_1$, $f_x(x_1,\mu)>0,f_x(x_2,\mu)<0$, hence we can plot

   <img src="Assignment%204.assets/image-20230522083954896.png" alt="image-20230522083954896" style="zoom:15%;" />

   $x_1$ is unstable while $x_2$ is stable.

3. If $\mu=\dfrac{1}{400}$, $x_1=x_2=400$, there’s only one fixed point.

   <img src="Assignment%204.assets/image-20230522084141196.png" alt="image-20230522084141196" style="zoom:25%;" />

   $x_1=x_2$ is unstable.

From the debate above, we’re sure that there’s a bifurcation of $\mu$ at $\mu=\dfrac{1}{400}$, and the bifurcation diagram is like

```mathematica
Show[
 Plot[{400, 1/m}, {m, 0, 1/400}, PlotRange -> {{0, 1/200}, {0, 800}}, 
  PlotStyle -> {_, Dashed}],
 Plot[{400, 1/m}, {m, 1/400, 1/200}, 
  PlotRange -> {{0, 1/200}, {0, 800}}, PlotStyle -> {Dashed, _}],
 AxesLabel -> {"\[Mu]", "f(x,\[Mu])"},
 Epilog -> {Red, PointSize[0.02], Point[{1/400, 400}], 
   Text["(1/400,400)", {1/370, 450}]}
 ]
```



<img src="Assignment%204.assets/image-20230522173747083.png" alt="image-20230522173747083" style="zoom:50%;" />

The bifurcation point $(\dfrac{1}{400},400)$ is a transcritical bifurcation since $f_x=f_{\mu}=0,f_{xx}\neq 0,f_{\mu x}^2-f_{xx}f_{\mu\mu}$

_(d)_ $x(0)=x_0,y(0)=400-x_0,0\leqslant x_0\leqslant 400.$

==First scenario== When $R_0=\mu x_0<1$, $\mu <\dfrac{1}{x_0}$, we can hardly make any conclusions since $\dfrac{1}{x_0}\geqslant \dfrac{1}{400}$.

If $\mu\in (0,\dfrac{1}{400}]$, by the bifurcation diagram (BD) above, $x_1=400$ is stable, hence $x(t),y(t)$ will tend to $400,0$ respectively.

If $\mu\in(\dfrac{1}{400},\dfrac{1}{x_0})$, by BD, $400>x_2=\dfrac{1}{\mu}$ is stable, hence $x(t),y(t)$ will tend to $\dfrac{1}{\mu},400-\dfrac{1}{\mu}$ respectively as $t\to+\infty$.

==Second scenario== When $R_0=\mu x_0>1,\mu>\dfrac{1}{x_0}\geqslant \dfrac{1}{400}$, by BD, $400>x_2=\dfrac{1}{\mu}$ is stable, hence $x(t),y(t)$ will tend to $\dfrac{1}{\mu},400-\dfrac{1}{\mu}$ respectively as $t\to+\infty$. Let $R_0$ be large enough, $y(t)$'s limit will tend to $400$.

This means if the infection rate and reproduction number goes larger, more individuals will be infected, and if they're below some threshold, all individuals will be cured finally.

## Problem 2

_(a)_ The transformation formula from Cartesian coordinate to Polar coordinate system is 
$$
\begin{cases}
x=r\cos\theta\\
y=r\sin\theta
\end{cases}\qquad\ra\qquad \begin{cases}
\dot x=-\dot \theta r\sin\theta+\dot r \cos\theta\\
\dot y=\dot \t r\cos\t+\dot r\sin\t
\end{cases}\quad\text{and}\quad\begin{cases}
r=\sqrt{x^2+y^2}\\
\t=\arctan(x,y)
\end{cases}
$$
Hence the original equations are equivalent to 
$$
\begin{cases}
\dot x=F(x,y,\mu)=-r\sin\t+r\cos\t(r^2-\mu)(r^2-2\mu)(r^2-3\mu)\\
\dot y=G(x,y,\mu)=r\cos\t +r\sin\t(r^2-\mu)(r^2-2\mu)(r^2-3\mu)
\end{cases}
$$
Combine these 2 set of functions we can solve out that
$$
\begin{cases}
\dot r=\dot x\cos\t+\dot y \sin\t=r(r^2-\mu)(r^2-2\mu)(r^2-3\mu)=f(r,\mu)\\
\dot \t=1=g(r,\theta,\mu)
\end{cases}
$$
_(b)_ The first equation $\dot r=f(r,\mu)$ has 7 zero points (fixed points) if $\mu>0$, namely $r_0=0,r_{\pm 1}=\sqrt{\mu},r_{\pm 2}=\sqrt{2\mu},r_{\pm 3}=\sqrt{3\mu}$, and has only one zero points $r_0$ if $\mu\leqslant 0$. Therefore at $\mu=0$, it has a bifurcation. Note that
$$
f_r(r,\mu)=-6\mu^3+33\mu^2 r^2-30\mu r^4+7r^6\\
f_r(r_0,\mu)=-6\mu^3,f_r(r_{\pm1},\mu)=4\mu^3,f_r(r_{\pm2},\mu)=-4\mu^3,f_r(r_{\pm3},\mu)=12\mu^3
$$
and when $\mu>0$, there's always $r_{-3}<r_{-2}<r_{-1}<r_0<r_1<r_2<r_3$ ordered, therefore

1. When $\mu<0$, $f_r(r_0,\mu)>0$, $r_0$ is unstable source-like point;
2. When $\mu=0$, $f_r(r,\mu)=7r^6\geqslant 0$, "=" holds iff $r=0$, $r_0$ is an unstable saddle point;
3. When $\mu>0$, $f_r(r,\mu)$ 
   - positive at $r_{-3},r_{-1},r_{1},r_3$, they are unstable source-like points;
   - negative at $r_{-2},r_{0},r_2$, they are stable points.

The plot graph for $f(r,\mu)$ is shown below:

<img src="Assignment%204.assets/image-20230522214301779.png" alt="image-20230522214301779" style="zoom:50%;" />

The bifurcation diagram is shown below:

<img src="Assignment%204.assets/image-20230522214818225.png" alt="image-20230522214818225" style="zoom:70%;" />

The curve coincidence with the x-axis is the origin, the other 6 curves are closed circular trajectories centered at the origin since $\dot \t=1$ constant and $\dot r=0$ on them.

_(c)_ First we evaluate the Jacobi Matrix at the origin,
$$
\begin{align}
J(x,y)&=\begin{bmatrix}
\pp{F}{x}&\pp{F}{y}\\\pp{G}{x}&\pp{G}{y}
\end{bmatrix}\\&=\small
\begin{bmatrix}
 -6 \lambda ^3+11 \lambda ^2 \left(3 x^2+y^2\right)-6 \lambda  \left(x^2+y^2\right) \left(5
   x^2+y^2\right)+\left(x^2+y^2\right)^2 \left(7 x^2+y^2\right) & 2 x y \left(11 \lambda ^2-12
   \lambda  \left(x^2+y^2\right)+3 \left(x^2+y^2\right)^2\right)-1 \\
 2 x y \left(11 \lambda ^2-12 \lambda  \left(x^2+y^2\right)+3 \left(x^2+y^2\right)^2\right)+1 & -6
   \lambda ^3+11 \lambda ^2 \left(x^2+3 y^2\right)-6 \lambda  \left(x^2+y^2\right) \left(x^2+5
   y^2\right)+\left(x^2+y^2\right)^2 \left(x^2+7 y^2\right) \\
\end{bmatrix}\\
J(0,0)&=\begin{bmatrix}
-6\mu^3&-1\\1&-6\mu^3
\end{bmatrix}
\end{align}
$$
It's eigenvalues are
$$
|J(0,0)-\lambda I|=1+\lambda^2+12\lambda\mu^3+36\mu^6=0\quad\ra\quad \lambda_1=-6\mu^3-i,\lambda_2=-6\mu^3+i
$$
When the bifurcation happens, i.e. when $\mu=0$, these eigenvalues becomes $\lambda_1=-i,\lambda_2=i$, both of them are purely imaginary, therefore the system has a Hopf bifurcation at $\mu=0$. 

## Problem 3

_(1)_ The given system is 
$$
\begin{cases}
\dot x=9y+x^3+xy=f_1(x,y)\\
\dot y=-x-\mu y+9y^2=f_2(x,y)
\end{cases}
$$
Transform it into polar coordinate system, we have
$$
\begin{cases}
\dot r=r(r^2\cos^4\t+r\sin\t(1+8\sin^2\t)-\mu\sin^2\t+8\cos\t\sin\t)\\
\dot \t=-r^2\cos^3\t\sin\t+8r\cos\t\sin^2\t-\mu\cos\t\sin\t-1-8\sin^2\t
\end{cases}
$$
At the critical point, $f_1=f_2=0$, obviously $(x,y)=(0,0)$ is a solution (critical point). The Jacobi Matrix at the origin is
$$
J(x,y)=\begin{bmatrix}
\pp{f_1}{x}&\pp{f_1}{y}\\
\pp{f_2}{x}&\pp{f_2}{y}
\end{bmatrix}=\begin{bmatrix}
3x^2+y&x+9\\
-1&18y-\mu
\end{bmatrix},\quad J(0,0)=\begin{bmatrix}
0&9\\-1&-\mu
\end{bmatrix}
$$
It's eigenvalues are ($\mu$ near $0$)
$$
|J(x,y)-\lambda I|=\lambda^2+\mu\lambda+9=0\quad\ra\quad \lambda_1=\dfrac{-\mu-i\sqrt{36-\mu^2}}{2},\lambda_2=\dfrac{-\mu+i\sqrt{36-\mu^2}}{2}
$$
When $\mu<0$, $\re\ \lambda_1,\re\ \lambda_2>0,\im\ \lambda_1,\im\ \lambda_2\neq 0$, $(0,0)$ is an unstable spiral, when $\mu >0$,  $\re\ \lambda_1,\re\ \lambda_2<0,\im\ \lambda_1,\im\ \lambda_2\neq 0$, $(0,0)$ is a stable spiral, hence when $\mu$ goes through $0$, the system has a bifurcation.

Take $\bar y=-3y,\bar x=x$, at $(0,0)$, the system can be written in normal form
$$
\begin{bmatrix}
\dot{\bar x}\\\dot{\bar y}
\end{bmatrix}=\begin{bmatrix}
0&-3\\3&-\mu
\end{bmatrix}\begin{bmatrix}
\bar x\\\bar y
\end{bmatrix}+\begin{bmatrix}
x^2-xy/3\\-3y^2
\end{bmatrix}
$$

- When $\mu=0$, $\lambda_1,\lambda_2$ are purely imaginary. 
- $d=\dfrac{1}{2}(f_{x\mu}+g_{y\mu})=-1\neq 0$ at $(0,0)$ and $\mu=0$. The transversality condition is satisfied. $\omega=3$
- The stability coefficient $a=\dfrac{3}{8}\neq 0$ according to the formula in the textbook

therefore the system has a Hopf bifurcation at the origin as $\mu$ passes through 0. 

*(2)* The period of the closed trajectories is $\dfrac{2\pi}{3}$ since $\im\lambda_2=-\im\lambda_1=3$. And the amplitude is $r=\sqrt{\dfrac{-d\mu}{a}}=\sqrt{\dfrac{8\mu}{3}}$. Since $a>0$, the periodic orbit is unstable.

## Problem 4

$$
x_{n+1}=x_n^3-x_n^2+(1+\mu)x_n-\mu=g(x_n,\mu)
$$

_(a)_ At the critical points, we have $g(x,\mu)=x$, i.e.
$$
x^3-x^2+\mu x-\mu=(x-1)(x^2+\mu)=f(x,\mu)=0
$$
Hence $x=x_0=1$, and 

- If $\mu=0$, $x=x_1=0$
- If $\mu<0$, $x=x_2=-\sqrt{-\mu}$ and $=x_3=\sqrt{-\mu}$

Since $g_x(x,\mu)=1+\mu-2x+3x^2$, $g_x(0,\mu)=\mu+1$, $fg_x(-\sqrt{-\mu})=2\sqrt{-\mu}-4\mu+1$, $g_x(\sqrt{-\mu})=2\sqrt{-\mu}(2\sqrt{-\mu}-1)+1$, $g_x(1,\mu)=2+\mu$

- If $\mu>0$, there’s only 1 critical point $x_0$, $g_x(x_0,\mu)=2+\mu>1$, $x_0$ is unstable repelling point
- If $\mu=0$, there’re 2 critical points $x_0,x_1$, $g_x(x_0,\mu)=2+\mu>1$ while $g_x(x_1,\mu)=1+\mu=1$, hence $x_0$ is unstable repelling point and $x_1$ is unstable saddle.
- If $-1<\mu<0$, there’re 3 critical points $x_0,x_2,x_3$, $g_x(x_0,\mu)=2+\mu>1$, $g_x(x_2,\mu)>1,|g_x(x_3,\mu)|<1,x_2<x_3<x_1$, hence $x_0$, $x_2$ are unstable repelling point, $x_3$ is stable attracting point.
- If $\mu=-1$, $x_3=x_0$, there’re 2 critical points $x_0,x_2$, $g_x(x_0,\mu)=1$, $g_x(x_2,\mu)>1$, hence $x_0$ is unstable saddle, $x_2$ is unstable repelling point.
- If $-3<\mu <-1$, there’re 3 critical points $x_0,x_2,x_3$ and $x_2<x_0<x_3$, $|g_x(x_0,\mu)|<1$, $g_x(x_2,\mu)>1$, $|g_x(x_3,\mu)|>1$, hence $x_0$ is stable attracting point, $x_2$, $x_3$ are unstable repelling point.
- If $\mu=-3$, there’re 3 critical points $x_0,x_2,x_3$ and $x_2<x_0<x_3$, $|g_x(x_0,\mu)|=1$, $g_x(x_2,\mu)>1$, $|g_x(x_3,\mu)|>1$, hence $x_0$ is unstable saddle, $x_2$, $x_3$ are unstable repelling point.
- If $\mu<-3$​, 
- there’re 3 critical points $x_0,x_2,x_3$ and $x_2<x_0<x_3$, $|g_x(x_0,\mu)|>1$, $g_x(x_2,\mu)>1$, $|g_x(x_3,\mu)|>1$, hence $x_0$, $x_2$, $x_3$ are all unstable repelling point.
- 

_(b)_ Bifurcation Diagram:

```mathematica
Show[
 Plot[{1, -Sqrt[-m], Sqrt[-m]}, {m, -2, -1}, 
  PlotRange -> {{-2, 2}, All}, PlotStyle -> {_, Dashed, Dashed}],
 Plot[{1, -Sqrt[-m], Sqrt[-m]}, {m, -1, 0}, 
  PlotRange -> {{-2, 2}, All}, PlotStyle -> {Dashed, Dashed, _}],
 Plot[{1}, {m, 0, 2}, PlotRange -> {{-2, 2}, All}, PlotStyle -> Dashed]
 ]
```

<img src="Assignment%204.assets/image-20230523043319120.png" alt="image-20230523043319120" style="zoom:30%;" />

At $(-1,1)$ there’s a transcritical bifurcation and at $(0,0)$, there’s a saddle node bifurcation. Unstable solution is dashed. Unstable period-2 points appears within $\mu<-3$.

## Problem 5

Let $x=-1\displaystyle +2\sum_{n=1}^\infty\dfrac{a_n}{3^n},a_n\in\{0,1,2\}$. If $a_1\neq 2$, then $x\leq 0$, and
$$
M(x)=-2-3x=-2+3-6\sum_{n=1}^\infty\dfrac{a_n}{3^n}=1-2\sum_{n=1}^\infty\dfrac{a_n}{3^{n-1}}=
$$
If $a_1=2$, then $x>0$, and 
$$
M(x)=2-3x=2+3-6\sum_{n=1}^\infty\dfrac{a_n}{3^n}=5-6\sum_{n=1}^\infty\dfrac{a_n}{3^n}=5-2\sum_{n=1}^\infty\dfrac{a_n}{3^{n-1}}
$$



## Problem 6

==$T(x)$==.Let $\displaystyle x=\sum_{n=1}^{+\infty}\dfrac{a_n}{2^n}$, where $a_n\in\{0,1\}$, then 

1. If $a_1=a_2=0$, then $x\in[0,\dfrac{1}{4}]$, therefore
   $$
   T(x)=T[0,0,a_3,a_4,\cdots]=[0,0,0,a_3,a_4,\cdots]
   $$

2. If $a_1=0,a_2=1$, then $x\in[\dfrac{1}{4},\dfrac{1}{2}]$, therefore
   $$
   T(x)=T[0,1,a_3,a_4,\cdots]=[1,a_3,a_4+a_3-1,a_5+a_4,\cdots]
   $$
   Or $T(x)=[0,0,1,a_5,a_6+a_5,\cdots]\in[0,0,1,\cdots]\sim [0,1,0,0,*,*,\cdots]$ if $a_3=a_4=0$.

3. If $a_1=1$, then $x\in[\dfrac{1}{2},1]$, therefore
   $$
   T(x)=T[1,a_2,a_3,\cdots]=[1,1,1,a_2,a_3,\cdots]
   $$

The fixed points of $T(x)$ are $x=\bar{0}$ and $x=\dfrac{5}{16}=0101$ and $x=1=0\overline{111\cdots}$. Since for 1.,3. $T(x)\leqslant  x,T(x)\geqslant x$ respectively, hence the only possible period interval is 2. But for $x\in[\dfrac{1}{4},\dfrac{1}{2}]$, We have either $T(x)>x$ for $x>x^*=\dfrac{5}{16}$ or $T(x)<x$ for $x < x^*$, hence it doesn’t have periodic points of all periods.

==S(x)== Let $\displaystyle x=\sum_{n=1}^{+\infty}\dfrac{a_n}{2^n}$, where $a_n\in\{0,1\}$, then 

1. If $a_1=a_2=0$, then $x\in[0,\dfrac{1}{4}]$, therefore
   $$
   S(x)=S[0,0,a_3,a_4,\cdots]=[0,a_3,a_4+a_3,a_5+a_4,\cdots]
   $$

2. If $a_1=0,a_2=1$, then $x\in[\dfrac{1}{4},\dfrac{1}{2}]$, therefore
   $$
   S(x)=S[0,1,a_3,a_4,\cdots]=[1,1,a_3,a_4,\cdots]
   $$

3. If $a_1=1,a_2=0$, then $x\in[\dfrac{1}{2},\dfrac{3}{4}]$, therefore
   $$
   S(x)=S[1,0,a_3,\cdots]=[1-a_3,1-a_4,\cdots]
   $$

4. If $a_1=1,a_2=1$, then $x\in[\dfrac{3}{4},1]$, therefore
   $$
   S(x)=S[1,1,a_3,a_4,\cdots]=[0,a_3,a_4,a_5,\cdots]
   $$

The fixed points of $S(x)$ are $x_0=\bar 0$, $x_1=\dfrac{3}{5}={0.1\overline{0011}}$. 2 period point $x_2=\overline{10}$.

If $n\geqslant 3$, consider $x=\overline{\underbrace{0000\cdots 0}_{n-2\ \text{   0's}}1}$, note that
$$
x\overset{S^{n-4}}{\longrightarrow}
$$
