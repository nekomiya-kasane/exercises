# Project 3

## Problem 1

From the description, the stochastic matrix and initial vector are 
$$
A=\begin{bmatrix}0.82&0.15&0.07\\0.09&0.75&0.08\\0.09&0.10&0.85\end{bmatrix}, x_0=\begin{bmatrix}0.20\\0.45\\0.35\end{bmatrix}
$$
<img src="Project%203.assets/image-20230513152110102.png" alt="image-20230513152110102" style="zoom:80%;" />

From the results, the long-term distribution is 
$$
x_\infty=[0.361,0.253,0.385]^T
$$
I.e the long-term possibility of people move to urban, rural, suburban are respectively $36.1\%, 25.3\%$ and $38.5\%$.

## Problem 2

1. From the results below, the eigenvectors and their corresponding eigenvalues are respectively

   <img src="Project%203.assets/image-20230513152559825.png" alt="image-20230513152559825" style="zoom:80%;" />

   1. $\lambda_1=1$, $v_1=[1,0,0]^T$
   2. $\lambda_2=0.335$, $v_2=[1,-2.823,1.823]^T$
   3. $\lambda_3=0.865$, $v_3=[1,-0.177,0.823]^T$

2. The steady state vector of $A$ satisfies $Ax=x$, $(A-I)x=0$
   $$
   A-I=\begin{bmatrix}
   0&0.3&0.1\\
   0&-0.6&0.1\\
   0&0.3&-0.2
   \end{bmatrix}
   $$
   since $\text{dim Ker} (A-I)=1$, and $[1,0,0]^T\in\mathrm{Ker} A$, we know that the solution set is $\lambda [1,0,0]^T$, furtherly, since it is a possibility vector, the sum should be exactly $1$, we have $\lambda =1$, therefore the steady state vector is $[1,0,0]$.

    <img src="Project%203.assets/image-20230513153835051.png" alt="image-20230513153835051" style="zoom:80%;" />

3. No. The kernel space of $A-I$ is of dimension $1$, so no generalization can be made.