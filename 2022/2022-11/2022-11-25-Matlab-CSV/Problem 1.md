## Problem 1

We’re going to develop a 3-compartment model for subcutaneous dosing. The 3-compartments are set up as subcutaneous compartment (1), central compartment (2), and peripheral compartment (3). and the transition graph is 

```
(1) -> (2) -> (3)
```

Since the drug is metabolized in all of the three compartments, we denote the three clearance rate as $C_i,i\in\{1,2,3\}$. Moreover, the volume of (1) is ignored and adopt the following denotation:

- $k$: the rate of diffusion from (1) to (2)
- $V_2,V_3$: the volume of (2), (3)
- $Q$ the transition rate between (2) and (3)
- $D(t)$ the dose function

By biology rules, the transition rate should be proportion to concentration gradient. Hence we can come up with our ODEs:

$\dfrac{dq_1}{dt}=D(t)-kq_1-C_1 q_1$

$\dfrac{dq_2}{dt}=kq_1-Q\left(\dfrac{q_2}{V_2}-\dfrac{q_3}{V_3}\right)-C_2\dfrac{q_2}{V_2}$

$\dfrac{dq_3}{dt}=Q\left(\dfrac{q_2}{V_2}-\dfrac{q_3}{V_3}\right)-C_3\dfrac{q_3}{V_3}$

Use inbuilt `dsolve` method to solve it.

We used the following parameters:

$k=0.05,C_1=0.05,C_2=0.2,C_3=0.25,V_2=5,V_3=3,Q=0.3$

And for one dose, the graph is plotted as

<img src="C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221130075155804.png" alt="image-20221130075155804" style="zoom:67%;" />

for multiple dose, the graph is plotted as

<img src="C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221130075904145.png" alt="image-20221130075904145" style="zoom:67%;" />

## Problem 2

#### 1) Equilibrium points

The equation for two species in the absence of the other one is

$x’=ax(K-x),y'=by(L-y)$

on the equilibrium points, we have

$x’=0,y’=0$, from which we can derive that $x=0$ or $K$; $y=0$ or $L$.

#### 2) Linearization

Substituting constants, we have

$x'=2x(3-x)+xy=f(x,y),y'=4y(2-y)+xy=g(x,y)$

on the equilibrium points, we have

$x’=0,y’=0$, from which we can derive 4 solutions

$(0,0),(0,2),(3,0),\left(\dfrac{32}{7},\dfrac{22}{7}\right)$

The Jacobi matrix is 

$J(x,y)=\begin{bmatrix}\dfrac{\partial f}{\partial x}&\dfrac{\partial f}{\partial y}\\\dfrac{\partial g}{\partial x}&\dfrac{\partial g}{\partial y}\end{bmatrix}=\begin{bmatrix}6-4x+y&x\\y&8-8y+x\end{bmatrix}$

$J(0,0)=\begin{bmatrix}6&0\\0&8\end{bmatrix}$, eigenvalues all real and positive $\lambda=6,8$, hence it’s an **unstable point**

$ J(0,2)=\begin{bmatrix}8&0\\2&-8\end{bmatrix}$, eigenvalues all real $\lambda=8,-8$, one is positive, the other is negative, hence it’s an **saddle point**.

$J(3,0)=\begin{bmatrix}-6&3\\0&11\end{bmatrix}$, eigenvalues all real $\lambda=11,-6$, one is positive, the other is negative, hence it’s an **saddle point**.

$J(32/7,22/7)=\begin{bmatrix}-\dfrac{64}{7}&\dfrac{32}{7}\\\dfrac{22}{7}&-\dfrac{88}{7}\end{bmatrix}$, eigenvalues all real and negative $\lambda=-15.02,-6.70$, hence it’s a **stable point**.

#### 3) Phase Portrait

<img src="Problem%201.assets/image-20221130082441715.png" alt="image-20221130082441715" style="zoom:67%;" />

Black points are the equilibrium points.

#### 4) Benefit

1. if only $x$ specie is present, its stable population is $x=K=3$
2. if only $y$ specie is present, its stable population is $y=L=2$
3. if both species are present, from 2) we can know their stable population is $x=32/7>K$, $y=22/7>L$

Hence they all benefit from the protocooperation.