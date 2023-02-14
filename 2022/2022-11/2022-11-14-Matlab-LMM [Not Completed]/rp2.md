### Linear Multistep Method

Given an ODE

$\displaystyle y’(t)=f(x,y)$

Based on Taylor’s Series expansion, we can come up with a recursion formula of the following form to solve such ODE:

$\displaystyle \sum_{j=0}^k\alpha_j y_{n+j}=h\sum_{j=0}^k\beta_jf_{n+j} \quad (*)$

where $h$ is a fixed step size, $\alpha_k\neq 0$, $y_{n+j}=y(x_{n+j})$ and $f_{n+j}=f(x_{n+j},y_{n+j})$.

This method is generally called Linear Multistep Method (LMM).

If $\beta_k\neq 0$, $y_{n+k}$, which is the next step is contained in both side, hence the formula is called **implicit form**, otherwise, it is called **explicit form**.

We’ll prove our method using **underdetermined coefficient method**.

Basically, for step larger than 1, we shall adopt single-step (here, Runge Kutta) method to compute the preceding several items. 

### Underdetermined Coefficient Method

To solve for the coefficients $\alpha_i$ and $\beta_i$, we could use underdetermined coefficient method.

Expand $y_{n+j}$ and $y'_{n+j}$ at $x_n$, we have

$\displaystyle y_{n+j}=\sum_{i=0}^{+\infty}\dfrac{(jh)^{i}}{i!}y^{(i)}(x)$ and $\displaystyle y'_{n+j}=\sum_{i=0}^{+\infty}\dfrac{(jh)^{i}}{i!}y^{(i+1)}(x)$

combine them, and make substitution within $(*)$, we can derive that

$\displaystyle y_{n+j}=\sum_{i=0}^{+\infty}c_i h^iy^{(i)}(x)$

where

$\displaystyle c_0=\sum_{i=0}^k\alpha_i=0$

$\displaystyle c_m=\dfrac{1}{m!}\sum_{i=0}^ki^m\alpha_i-\dfrac{1}{(m-1)!}\sum_{i=0}^ki^{m-1}\beta_i=0,\quad 1\leqslant m\leqslant p$

$c_{p+1}\neq0$

### Explicit Recursion

consider the following subproblem for both problem 1 and 2:

$y_{n+3}+\alpha_2y_{n+2}+\alpha_1y_{n+1}+\alpha_0y_{n}=h(\beta_0f_n+\beta_1f_{n+1}+\beta_2f_{n+2}+\beta_3f_{n+3})$

It is a 3-step method. To let it have 3 order error, there should be $c_0=c_1=c_2=c_3=0$, $c_4\neq 0$

hence 

$\left\{\begin{array}{l}\alpha_0+\alpha_1+\alpha_2=-1\\
\alpha_1+2\alpha_2-(\beta_0+\beta_1+\beta_2+\beta_3)=-3\\
\dfrac{1}{2}(\alpha_1+4\alpha_2)-(\beta_1+2\beta_2+3\beta_3)=-\dfrac{9}{2}\\
\dfrac{1}{6}(\alpha_1+8\alpha_2)-\dfrac{1}{2}(\beta_1+4\beta_2+9\beta_3)=-\dfrac{9}{2}
\end{array}\right.$

i.e $A\mathbf{x}=\mathbb{b}$, it has infinite solutions, and we only take the one with least squares, such that $A^TA\mathbf{x}=A^T\mathbf{b}$.

solve for $\mathbf{x}$ we get $\mathbf{x}=[\alpha_0,\alpha_1,\alpha_2,\beta_0,\beta_1,\beta_2\beta_3]^T=\left[-\dfrac{11}{2},9,-\dfrac{9}{2},3,0,0,0\right]^T$

and we can verify that $c_4\neq 0$.

Therefore, our recursion formula shall be $y_{n+3}=\dfrac{11}{2}y_{n+2}-9y_{n+1}+\dfrac{9}{2}y_n+3f(x_n,y_n)$

### Implicit Recursion

To get an implicit recursion formula, we must make sure that $\beta_3\neq 0$

for convenience, let $\beta_0=\beta_1=\beta_2=0$

solve the equations, we can get $\alpha_2=\frac{18}{11},\alpha_1=-\dfrac{9}{11},\alpha_0=\dfrac{2}{11},\beta_3=\dfrac{6}{11}$

hence our recursion formula is $y_{n+3}=\dfrac{18}{11}y_{n+2}-\dfrac{9}{11}y_{n+1}+\dfrac{2}{11}y_n+\dfrac{6}{11}f(x_{n+3},y_{n+3})$

