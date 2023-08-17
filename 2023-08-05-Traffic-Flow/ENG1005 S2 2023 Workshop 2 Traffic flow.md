![image-20230805221418728](./ENG1005%20S2%202023%20Workshop%202%20Traffic%20flow.assets/image-20230805221418728.png)

1. Since there're no cars stopped at the junctions, the outlet of cars should be equal to the inlet of cars at a junction, which is similar to the law of conservation. Hence for the 4 junctions, we have
   $$
   \begin{array}{rcl}
   20+ x_4&=&30+x_1\\
   70+5+x_3&=&60+x_4+x_5\\
   x_1+25&=&30+x_2\\
   x_2+65+x_5&=&x_3+55+10
   \end{array}
   $$

2. There should be infinite solutions, since we only have 4 equations, but there're 1 more, that is, 5 variables. At least we cannot determine 1 of them.

3. The equations can be normalized to 
   $$
   \begin{aligned}\left\{\begin{array}{rrrrrl}
   x_1&&&-x_4&&=-10\\
   &&x_3&-x_4&-x_5&=-15\\
   x_1&-x_2&&&&=5\\
   &x_2&-x_3&&+x_5&=0
   \end{array}\right.&\implies
   \begin{bmatrix}
   1&0&0&-1&0\\
   0&0&1&-1&-1\\
   1&-1&0&0&0\\
   0&1&-1&0&1
   \end{bmatrix}\begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=
   \begin{bmatrix}
   -10\\-15\\5\\0
   \end{bmatrix}
   \\
   {\small-\text{row3}+\text{row1 added to row 2}}&{\implies}
   \begin{bmatrix}
   1&0&0&-1&0\\
   0&1&1&-2&-1\\
   1&-1&0&0&0\\
   0&1&-1&0&1
   \end{bmatrix}\begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=
   \begin{bmatrix}
   -10\\-30\\5\\0
   \end{bmatrix}
   \\
   {\small-\text{row1+row2 added to row3}}&{\implies}
   \begin{bmatrix}
   1&0&0&-1&0\\
   0&1&1&-2&-1\\
   0&0&1&-1&-1\\
   0&1&-1&0&1
   \end{bmatrix}\begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=
   \begin{bmatrix}
   -10\\-30\\-15\\0
   \end{bmatrix}
   \\
   {\small-\text{row3 added to row2}}&{\implies}
   \begin{bmatrix}
   1&0&0&-1&0\\
   0&1&0&-1&0\\
   0&0&1&-1&-1\\
   0&1&-1&0&1
   \end{bmatrix}\begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=
   \begin{bmatrix}
   -10\\-15\\-15\\0
   \end{bmatrix}\\
   {\small-\text{row2+row3 added to row4}}&{\implies}
   \begin{bmatrix}
   1&0&0&-1&0\\
   0&1&0&-1&0\\
   0&0&1&-1&-1\\
   0&0&0&0&0
   \end{bmatrix}\begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=
   \begin{bmatrix}
   -10\\-15\\-15\\0
   \end{bmatrix}
   \end{aligned}
   $$
   Hence the row echelon form of the original equations is
   $$
   \begin{bmatrix}
   1&0&0&-1&0\\
   0&1&0&-1&0\\
   0&0&1&-1&-1\\
   0&0&0&0&0
   \end{bmatrix}\begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=
   \begin{bmatrix}
   -10\\-15\\-15\\0
   \end{bmatrix}\Leftrightarrow \begin{cases}
   x_1-x_4=-10\\
   x_2-x_4=-15\\
   x_3-x_4-x_5=-15\\
   \color{lightgray}(0=0)
   \end{cases}
   $$
   Verify:

   <img src="./ENG1005%20S2%202023%20Workshop%202%20Traffic%20flow.assets/image-20230805224705953.png" alt="image-20230805224705953" style="zoom:53%;" />

4. By 3., the solution is $x_1=x_4-10,x_2=x_4-15,x_3=x_4+x_5-15,x_4=x_4,x_5=x_5$, 
   $$
   \begin{bmatrix}
   x_1\\x_2\\x_3\\x_4\\x_5
   \end{bmatrix}=\begin{bmatrix}
   -10\\-15\\-15\\0\\0
   \end{bmatrix}+a_1\begin{bmatrix}
   1\\1\\1\\1\\0
   \end{bmatrix}+a_2\begin{bmatrix}
   0\\0\\1\\0\\1
   \end{bmatrix},\quad a_1,a_2\in\R
   $$

5. The solutions introduces 2 parameters,
   - $a_1$, which equals to $x_4$, the vector $[1,1,1,1,0]^T$ represents if $x_5$ is not changed, if we add 1 car to $x_4$, the corresponding increment of the traffic of $x_1,x_2,x_3$, and certainly, $x_4$.
   - $a_2$, which equals to $x_5$,  the vector $[0,0,1,0,1]^T$ represents if $x_4$ is not changed, if we add $1$ car to $x_5$, the corresponding increment of the traffic of $x_1,x_2,x_3$, and certainly $x_5$.

6. Since our solution is expressed in $x_4, x_5$, one of the method to know all the traffic is to additionally measure the traffic $x_4,x_5$. The dimension of the solution is $2$, with 2 linear independent solution space base vectors $[1,1,1,1,0]^T, [0,0,1,0,1]^T$. Hence at least $2$  additional traffic measurements needed. Also, we can place the 2 extra measurements at any other 2 different roads paired as $(x_1,x_3),(x_1,x_5),(x_2,x_3),(x_2,x5),(x_4,x_3)$ or $(x_4,x_5)$.

7. To meet the requirements, we have 
   $$
   a_1=x_4\geqslant  0\\
   a_2=x_5\geqslant 0\\
   x_1=-10+a_1\geqslant 0\Rightarrow a_1\geqslant 10\\
   x_2=-15+a_1\geqslant 0\Rightarrow a_1\geqslant 15\\
   x_3=-15+a_1+a_2\geqslant 0\text{ always holds under } a_1\geqslant 15\\
   $$
    Hence
   $$
   x_4=a_1\geqslant 15,x_5=a_2\geqslant 0,x_3=-15+a_1+a_2\geqslant 0,x_2=-15+a_1\geqslant 0,x_1=-10+a_1\geqslant 5
   $$
   The minimum traffic on $x_1,x_2,x_3,x_4,x_5$ are $5,0,0,15,0$ respectively.