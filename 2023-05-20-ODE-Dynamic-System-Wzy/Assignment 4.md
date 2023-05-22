# Assignment 4

## Problem 1

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

   <img src="C:/Users/35995/AppData/Roaming/Typora/typora-user-images/image-20230522083641990.png" alt="image-20230522083641990" style="zoom:30%;" />

   $x_1$ is stable while $x_2$ is unstable.

2. If $\mu>\dfrac{1}{400}$, then $x_2<x_1$, $f_x(x_1,\mu)>0,f_x(x_2,\mu)<0$, hence we can plot

   <img src="C:/Users/35995/AppData/Roaming/Typora/typora-user-images/image-20230522083954896.png" alt="image-20230522083954896" style="zoom:15%;" />

   $x_1$ is unstable while $x_2$ is stable.

3. If $\mu=\dfrac{1}{400}$, $x_1=x_2=400$, there’s only one fixed point.

   <img src="C:/Users/35995/AppData/Roaming/Typora/typora-user-images/image-20230522084141196.png" alt="image-20230522084141196" style="zoom:25%;" />

   $x_1=x_2$ is unstable.

From the debate above, we’re sure that there’s a bifurcation of $\mu$ at $\mu=\dfrac{1}{400}$.