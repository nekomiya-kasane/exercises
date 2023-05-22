# Project 1

> Consider the linear system:
> $$
> 2x+3y-4z=1\\
> x-y+2z=6\\
> 5x+2y-2z=3
> $$
> In the coding box (cell) below write this system as an augmented matrix and use Sage to find a description of the solution space.
>
> Take a screenshot showing the problem and your entire Sage coding box including the solution. Paste this onto your Word document in the "Problem 1" section.

<img src="Project%201.assets/image-20230513120707957.png" alt="image-20230513120707957" style="zoom:80%;" />

From the cell above, we know that the $\mathrm{Ker}(A)=\varnothing$, and the solution to the equations written in Matrix form
$$
Ax=b\qquad A=\begin{bmatrix}
2&3&-4\\1&-1&2\\5&2&-2
\end{bmatrix}\qquad b=[1,6,3]^T
$$
 is $x=[-2,21,\dfrac{29}{2}]^T$, hence the solution space contains only one vector.

> For Problem 2 you will complete the problem below which is similar to [questions 2a and 2b(opens in a new tab)](https://learnatrio.com/3AkVpQX) under exercises 1.3.5, which deal with traffic patterns.
>
> If you look at the problem on the website, you will see a diagram of traffic patterns and would get started with the first equation of the system by looking at the first node on the top left. You will see $x$ going in, and $y$ and 100 going out. In order to balance this intersection, and make the amount of cars going in equal to the amount of cars going out, you make the first equation of the system $x=y+100$
>
> Next, you would do the same thing for the other three nodes (intersections) and put the four equations in standard form before entering into Sage to find the solution.
>
> Follow that same process to solve the traffic problem as illustrated in the diagram below by writing a linear system of four equations (type onto your paper), and then use the coding box below to solve the system.
>
> ![a](https://riosalado.coursearc.com/files/9116/6880/4091/MAT225_Project1_Problem2_VersionA.png)
>
> Under "Problem 2" of your word document should be a screenshot of the problem and Sage coding box, as well as the typed up system you used to solve the problem.

We marked the nodes as below:

<img src="Project%201.assets/image-20230513121506810.png" alt="image-20230513121506810" style="zoom:50%;" />

For each node from 1 to 4, we have the following constraints:
$$
\begin{aligned}
x&=y+250\\
250+w&=100\\
260+y&=z\\
z&=w+390
\end{aligned}\qquad\Rightarrow\qquad \begin{aligned}
&x-y=250\\
&w=-150\\
&z-y=260\\
&z-w=390
\end{aligned}
$$
Write it in matrix form, we have
$$
AX=b\qquad\text{where}\qquad A=\begin{bmatrix}
1&-1&0&0\\0&0&0&1\\0&-1&1&0\\0&0&1&-1
\end{bmatrix},b=[250,-150,260,390]^T
$$
Solve using Sage Math:

<img src="Project%201.assets/image-20230513122238232.png" alt="image-20230513122238232" style="zoom:80%;" />

From the output we know that the solution space contains the only vector $X=[230,-20,240,-150]^T$. i.e. $x=230,y=-20,z=240,w=-150$.

> For Problem 3 you will be completing a Thermodynamics problem similar to [question 3(opens in a new tab)](https://learnatrio.com/3EdaDZD) on the website under exercises 1.3.5 which you may use that to help you set up your system.
>
> Find the steady-state temperature distribution inside a thin plate given the temperatures around the boundary in the diagram below. Let $T_i, 1\leq i\leq 6$ be the temperatures at the six nodes inside the plate as shown. Set up a linear system to solve for these six temperatures.
>
> Follow the same steps shown on the website to set up a system for your diagram and solve with the Sage coding box below. Paste the screenshot of the problem with the coding box that you used under "Problem 3". Type the system that you used and the solution there as well.
>
> <img src="Project%201.assets/image-20230513122651936.png" alt="image-20230513122651936" style="zoom:50%;" />

For each of the six nodes, we have 
$$
\begin{aligned}
T_1&=\dfrac{1}{4}(10+30+T_2+T_4)\\
T_2&=\dfrac{1}{4}(20+T_1+T_3+T_5)\\
T_3&=\dfrac{1}{4}(10+T_2+T_6+35)\\
T_4&=\dfrac{1}{4}(T_1+40+25+T_5)\\
T_5&=\dfrac{1}{4}(T_2+T_4+T_6+30)\\
T_6&=\dfrac{1}{4}(T_3+T_5+20+25)
\end{aligned}\qquad \text{Reformatted to}\qquad
\begin{aligned}
4T_1-T_2-T_4=40\\
-T_1+4T_2-T_3-T_5=20\\
-T_2+4T_3-T_6=45\\
-T_1+4T_4-T_5=65\\
-T_2-T_4+4T_5-T_6=30\\
-T_3-T_5+4T_6=45
\end{aligned}
$$
In matrix form,
$$
AX=b\qquad\text{where}\qquad A=\begin{bmatrix}
4&-1&0&-1&0&0\\
-1&4&-1&0&-1&0\\
0&-1&4&0&0&-1\\
-1&0&0&4&-1&0\\
0&-1&0&-1&4&-1\\
0&0&-1&0&-1&4
\end{bmatrix},b=\begin{bmatrix}
40\\20\\45\\65\\30\\45
\end{bmatrix}
$$
Solve using Sage Math

<img src="Project%201.assets/image-20230513123937785.png" alt="image-20230513123937785" style="zoom:80%;" />

From the output we know that the solution space contains the only vector
$$
X=[\dfrac{3685}{161},\dfrac{3705}{161},\dfrac{3685}{161},\dfrac{4595}{161},\dfrac{4230}{161},\dfrac{3790}{161}]
$$
i.e $T_1=\dfrac{3685}{161},T_2=\dfrac{3705}{161},T_3=\dfrac{3685}{161},T_4=\dfrac{4595}{161},T_5=\dfrac{4230}{161},T_6=\dfrac{3790}{161}$.

> Ideally, the fuel inside model rocket motors is a black powder mixture that consists of 60% charcoal, 30% potassium nitrate, and 10% sulfur by weight.
>
> At a factory that makes model rocket motors, the first shift of workers followed the recipe exactly as they were supposed to. The second shift **did not** and used 55% charcoal, 33% potassium nitrate and 12% sulfur. When the two batches were mixed together, a chemical analysis shows that there are 110.2 pounds of charcoal in the mixture and 45.8 pounds of potassium nitrate.
>
> If the first shift produced $A$ pounds of fuel and the second shift produced $B$ pounds, set up a linear system in terms of A and B. How many pounds of fuel did the first shift produce and how many did the second shift produce?
>
> Under "Problem 4", paste the screenshot of the problem and the Sage coding box that you used to solve the problem. Type the system and the answer to the problem.
>
> When you have finished pasting all of your problems onto your Word document, save it, and then save again as a PDF. You will be **submitting the PDF** at the link below.

The equations for charcoal and potassium nitrate are respectively
$$
0.6A+0.55B=110.2\\
0.3A+0.33B=45.8
$$
In matrix form
$$
AX=b\qquad\text{where}\qquad A=\begin{bmatrix}
0.6&0.3\\0.55&0.33
\end{bmatrix},b=\begin{bmatrix}
110.2\\45.8
\end{bmatrix}
$$
Solve using Sage Math

<img src="Project%201.assets/image-20230513125654592.png" alt="image-20230513125654592" style="zoom:80%;" />

From the output we know that the solution space contains the only vector $X=[685.64,-1003.94]^T$. i.e. $A=685.64,B=-1003.94$.

# 

