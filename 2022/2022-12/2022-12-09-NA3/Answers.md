## Q1 

### (a)

**Explanation:**
Given matrix $A$, Rayleigh quotient iteration converges to an eigenvalue/eigenvector pair for all except a set of measure zero of starting vectors $v$. When it converges, it can be proved that the convergence is cubic in the sense that if $\lambda$ is an eigenvalue of $A$ and $v$ is sufficiently close to the eigenvector $q$, then

$||v_{k+1}-(\pm q)||=O(||v_k-(\pm q)||^3)$, $|\lambda_{k+1}-\lambda|=O(|\lambda_k-\lambda|^3)$

This iteration converges much faster than power iteration.

**Relationship to least squares approximation:**

Consider the least square optimization problem, 

$\min f(a)=||Ax-xa||_2^2$

the solution is $a=\dfrac{x^T Ax}{x^Tx}=r(x)$ which happens to be the Rayleigh quotient of $x$. Thus, the Rayleigh quotient provides an *least square optimal estimate/approximation*$a$ for the eigenvalue $\alpha$ corresponding to the *approximation* $x$ of an eigenvector. If $x$ is exactly an eigenvector of $A$, then $a$ is exactly its corresponding eigenvalue, making $\min f(a)=0$.

### (b)

$A=\begin{bmatrix}3&1\\1&4\end{bmatrix}$, $x_0=[0.75,1]^T=v_0$, denote Rayleigh quotient of $x$ as $r(x)$ (same as (a)), $\lambda_0=r(x_0)=\dfrac{23}{5}=4.6$

**Iteration 1:**
Solve $(A-\lambda_0 I)w=v_0$ for $w$, we get $w=[\dfrac{145}{4},\dfrac{235}{4}]^T=[36.25,58.75]^T$

Normaliztion: $v_1=w/||w||_2\approx[0.5251,0.8510]^T$

Update $\lambda $: $\lambda_1=r(v_1)\approx4.6180$ 

**Iteration 2:**

Now $A-\lambda_1I\approx\begin{bmatrix}-1.6180&1\\1&-0.6180\end{bmatrix}$ nearly sigular

Hence we get the eigenvalue $4.6180$ and corresponding eigenvector $[0.5251,0.8510]$

### (c)

As we have said in (a), Rayleigh quotient iteration converges cubicly, hence after 3 iterations, the absolute error would be $0.1^3=10^{-3}$

## Q2

See matlab.

## Q3

### (a)

It is given that $A$ has 3 distinct eigenvalues. Hence we can let $X^{(0)}=I_3$, then $\hat{Q_0}=\hat{R_0}=I_3$.

$X^{(1)}=A\hat{Q_0}=A$

Do QR decomposition for $X^{(1)}$ we have

$\hat{Q_1}=\left(
\begin{array}{ccc}
 \dfrac{6}{7} & \dfrac{2}{7} & \dfrac{3}{7} \\
 -\dfrac{4}{7 \sqrt{5}} & \dfrac{3 \sqrt{5}}{7} & -\dfrac{2}{7
   \sqrt{5}} \\
 \dfrac{1}{\sqrt{5}} & 0 & -\dfrac{2}{\sqrt{5}} \\
\end{array}
\right)$, $\hat{R_1}=\left(
\begin{array}{ccc}
 7 & 3 & \dfrac{5}{7} \\
 0 & \sqrt{5} & \dfrac{13}{7 \sqrt{5}} \\
 0 & 0 & \dfrac{3}{\sqrt{5}} \\
\end{array}
\right)$

### (b/c)

see matlab.

