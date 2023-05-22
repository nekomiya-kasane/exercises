# Project 2

## Problem 1

From the graph, in normalized standard basis $e_1=[1,0]^T,e_2=[0,1]^T$. we have
$$
v_1=(-2,2)^T,v_2=(2,1)^T
$$
The matrix $A$ that transform vectors from $B={v_1,v_2}$ basis to standard basis $S={e_1,e_2}$ and its inverse $A^{-1}$ would be
$$
A=[v_1,v_2]=\begin{bmatrix}-2&2\\2&1\end{bmatrix}, A^{-1}=\begin{bmatrix}-1/6&1/3\\1/3&1/3\end{bmatrix}
$$
Hence if given $\{x\}_B$, then $x=A\{x\}_B$. If given $x$ then $\{x\}_B=A^{-1}x$.

Solve using Saga Math:

<img src="Project%202.assets/image-20230513132444681.png" alt="image-20230513132444681" style="zoom:80%;" />

From the results, we know that 

1. if $[x]_B=[-1,1]^T$ then $x=[4,-1]^T$
2. if $x=[-4,-5]^T$, then $[x]_B=[-1,-3]^T$
3. if $[x]_B=[12,-10]^T$, then $x=[-44,14]^T$
4. if $x=[60,-90]^T$, then $[x]_B=[20,50]^T$

## Problem 2

We can make use of Sage Math’s `span` method to find if $\text{span}(v_1,v_2,v_3,v_4,v_5)$, also, we can let $A=[v_1,v_2,v_3,v_4,v_5]$ and take the `rref` of $A$, if the result contains no zero row, then $\text{span}(A)=\mathbb{R}^3$. 

<img src="Project%202.assets/image-20230513133152313.png" alt="image-20230513133152313" style="zoom:80%;" />

Thus we know $\mathrm{span}(v_1,v_2,v_3,v_4,v_5)=\mathbb{R}^3$. But since $\mathrm{dim}\mathbb{R}^3=3\neq 5$, they are not linearly independent, hence not a basis.

<img src="Project%202.assets/image-20230513133601247.png" alt="image-20230513133601247" style="zoom:80%;" />

<img src="C:/Users/35995/AppData/Roaming/Typora/typora-user-images/image-20230513133629543.png" alt="image-20230513133629543" style="zoom:80%;" />

But some of them form a basis

<img src="Project%202.assets/image-20230513142433718.png" alt="image-20230513142433718" style="zoom:80%;" />

From the results, $(v_1,v_3,v_4)$ and $(v_2,v_3,v_4)$ are linearly dependent, hence there’re many sets of basis, including:

$(v_5,v_3,v_4)$, $(v_5,v_1,v_3)$, $(v_5,v_1,v_4)$, $(v_5,v_2,v_3)$, $(v_5,v_2,v_4)$, $(v_5,v_1,v_2)$.

## Problem 3

1. <img src="Project%202.assets/image-20230513142617232.png" alt="image-20230513142617232" style="zoom:80%;" />From the results, the dimension spanned by $(v_1,v_2,v_3)$ is $3$, while equals to $A=[v_1,v_2,v_3]$ ‘s rank, and the dimension of $\mathbb{R}^3$ is also 3, hence $B=\{v_1,v_2,v_3\}$ is a basis for $\mathbb{R}^3$.

   The matrix that transform coordinates under basis $B$ to standard basis is $A$, hence the reverse transform matrix is 

$$
A=\begin{bmatrix}
1&\cos\dfrac{\pi}{6}& \cos\dfrac{2\pi}{6}\\
1&\cos\dfrac{3\pi}{6}&\cos\dfrac{6\pi}{6}\\
1&\cos\dfrac{5\pi}{6}&\cos\dfrac{10\pi}{6}
\end{bmatrix}\qquad A^{-1}=\dfrac{1}{3}\begin{bmatrix}
1&1&1\\\sqrt{3}&0&-\sqrt{3}\\1&-2&1
\end{bmatrix}
$$

2. If $x=[5,5,5]^T$, then $[x]_B=A^{-1}x=[5,0,5]^T$

   <img src="Project%202.assets/image-20230513143318794.png" alt="image-20230513143318794" style="zoom:80%;" />

3. If $x=[a_1,a_2,a_3]^T$, $\{x\}_B=[b_1,b_2,b_3]^T$, then $\{x\}_B=A^{-1}x$, as the first row of $A^{-1}$ is $[1/3,1/3,1/3]^T$, hence $b_1=\dfrac{1}{3}(a_1+a_2+a_3)$, i.e. the average of $x$.

## Problem 4

![asdf](https://riosalado.coursearc.com/files/2816/6905/7419/MAT225_Project2_Problem4_VersionA.png)

The center of the first hexagon is $C=v_1+v_2$, from $C$, we can express any of the center of a hexagon as $C’=C+n (2v_1+v_2)+m(v_1+2v_2)=(2n+m+1)v_1+(2m+n+1)v_2$, where $n,m\in\mathbb{Z}$. and any of the vertices of the hexagon centered at $C’$ has the location $V’=C’+s_1v_1+s_2v_2$, where $s_1,s_2\in \{0,-1,1\}$ and $s_1s_2\neq -1$.

1. Referring the debate above, since the center of the yellow hexagon is $3v_1-v_2=(3,-1)$, the coordinates of the 6 vertices of it are 
   $$
   (3,0),(4,0),(4,-1),(2,-1),(2,-2),(3,-2)
   $$

2. Consider the path along the colored edges:

   <img src="Project%202.assets/image-20230513145635848.png" alt="image-20230513145635848" style="zoom:50%;" />

   The star can be expressed as $v_1+(v_1+v_2)+v_1+(v_1+v_2)+v_1+v_2=5v_1+3v_2$, its coordinate would be $(5,3)$.

3. Referring to the debate above, consider
   $$
   2n+m+1=8\\
   2m+n+1=20
   $$
   To matrix form 
   $$
   Ax=b,A=\begin{bmatrix}2&1\\1&2\end{bmatrix},b=[7,19]^T
   $$
   <img src="Project%202.assets/image-20230513150832154.png" alt="image-20230513150832154" style="zoom:80%;" />

   It has no integer solution, hence it is a ==vertex==. Verify: change $b$ to $[7,19]^T$ to $[8,19]^T$ (i.e $s_1=1,s_2=0$, then it has an integer solution.

   <img src="C:/Users/35995/AppData/Roaming/Typora/typora-user-images/image-20230513151046376.png" alt="image-20230513151046376" style="zoom:80%;" /> 

