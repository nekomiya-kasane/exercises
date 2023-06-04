# Project 3

## Problem 1

1. $2x_1-6x_1x_2+8x_2^2=q((x_1,x_2)^T)=[x_1,x_2]\begin{bmatrix}2&-3\\-3&8\end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix}$. Thus $A=\begin{bmatrix}2&-3\\-3&8\end{bmatrix}$.

2. From the results, we know that $A$ has 2 distinct eigenvalues $\lambda_1=0.757<\lambda_2=9.243$ together with 2 corresponding unit eigenvectors $v_1=(0.924,0.383)^T,v_2=(0.383,-0.924)^T$. 

   Given any $x=av_1+bv_2\in\mathbb{R}^2$, $x^TAx=(av_1+bv_2)^TA(av_1+bv_2)=a^2\lambda_1+b^2\lambda_2+2ab\lambda_1\lambda_2v_2^TAv_1$. Since $A$ is positive definite

   - The maximum $9.243$ is reached when $x=(0.383,-0.924)^T$ is collinear with $v_2$, which has larger eigenvalue
   - The maximum $0.757$ is reached when $x=(0.924,0.383)$ is collinear with $v_1$, which has smaller eigenvalue

   <img src="Project%204.assets/image-20230513155725566.png" alt="image-20230513155725566" style="zoom:80%;" />

## Problem 2

1. The covariance matrix $C$ is $\dfrac{1}{N}AA^T=\begin{bmatrix}3/4&0\\0&5/2\end{bmatrix}$.

   ![image-20230513160436826](Project%204.assets/image-20230513160436826.png)

2. The variance of the data projected onto the line defined by $u=[1/\sqrt{2},1/\sqrt{2}]^T$ is $u^TCu=13/8$.

   ![](Project%204.assets/image-20230513160727843.png)

3. Choose a unit vector that are orthogonal to $u$, say $v=[-1/\sqrt{2}, 1/\sqrt{2}]^T$, the variance projected onto the line defined by $v$ is also $13/8$, so the total variance is $13/8+13/8=13/4$.

   ![image-20230513161112922](Project%204.assets/image-20230513161112922.png)

4. Since $C$ is diagonal, its eigenvalues are $\lambda_1=3/4,\lambda_2=5/2$ and the corresponding eigenvectors are $v_1=(1,0)^T$, $v_2=(0,1)^T$. The greatest variance $x^TCx$ ($x$ unit) is achieved when $x$ is  collinear with $v_2$, which has the largest eigenvalue. Thus in the direction $v_2=(0,1)^T$, the greatest variance is achieved and is $5/2$.

   <img src="Project%204.assets/image-20230513161526387.png" alt="image-20230513161526387" style="zoom:80%;" />

## Problem 3

1. According to the result, $A$ has $2$ distinct eigenvalues $\lambda_1=4$ of multiplicity 1,$\lambda_2=1$ of multiplicity 2.

   - The orthonormal eigenvector of $\lambda_1$ is $v_1=\dfrac{1}{\sqrt 3}(1,-1,1)^T$
   - The orthonormal eigenvector of $\lambda_2$ is $v_2=\dfrac{1}{\sqrt 2}(1,0,-1)^T$, $v_3=\dfrac{1}{\sqrt 6}(1,2,1)^T$

   Thus let $Q = [v_1,v_2,v_3]=\left(\begin{array}{rrr} \frac{1}{3} \, \sqrt{3} & \frac{1}{2} \, \sqrt{2} & \frac{1}{6} \, \sqrt{3} \sqrt{2} \\ -\frac{1}{3} \, \sqrt{3} & 0 & \frac{1}{3} \, \sqrt{3} \sqrt{2} \\ \frac{1}{3} \, \sqrt{3} & -\frac{1}{2} \, \sqrt{2} & \frac{1}{6} \, \sqrt{3} \sqrt{2} \end{array}\right)$, we have 
   $$
   A=QDQ^T,D=Q^TAQ=\begin{bmatrix}4&0&0\\0&1&0\\0&0&1\end{bmatrix}
   $$
   

   ![image-20230513163603291](Project%204.assets/image-20230513163603291.png)

2. $q(u)=u^TAu=u^TQDQ^Tu=(Q^Tu)^TD(Q^Tu)$, when $Q^Tu=[1,0,0]^T$, $q(u)=4$ is maximized; when $Q^Tu=[0,1,0]^T$, $q(u)=1$ is minimized.

   Hence $u=Q[1,0,0]^T=\dfrac{1}{3}[1,-1,1]^T$ maximize $q(u)$ and $u=Q[0,1,0]^T=\dfrac{1}{\sqrt{2}}[1,0,-1]^T$ minimizes $q(u)$.

   ![](Project%204.assets/image-20230513164148374.png)

   

   