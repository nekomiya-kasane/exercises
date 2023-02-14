## Problem

This is a problem about a fox chasing a rabbit. On the ground, there is a warehouse, a fox behind the warehouse, and a rabbit to the north east of the warehouse.

We set up a coordinate system, with x-axis parallel to the north/south edge of the warehouse, and y-axis parallel to the east edge of the warehouse. For convenience, we assume that the warehouse extends infinitely to the west.



There are some other assumptions:

- If the fox is still behind the warehouse, if it cannot see the rabbit, it will run to the south east corner.
- If the fox has passed the south east corner and somehow it cannot see the rabbit, it will run along the north direction.
- If the fox can see the rabbit, it will run directly towards the rabbit.
- The rabbit is also running toward its home, if it has reach its home, the fox will fail to catch it.
- Both the fox and the rabbit is thought as points.

**Common**

The south east and north west corner of the warehouse is set to $(-200,-400)$ and $(-200,0)$ respectively.

The fox’s initial location is set to $(-250.-550)$ while the rabbit’s is set to $(0,0)$.

The rabbit’s home is located at $(-600,600)$.

If the final distance between the rabbit and fox is less than $0.1$, then we think the fox has caught the rabbit.

**Problem 1**

In the first problem, the velocity of fox and rabbit is assumed to be constant. The fox’s velocity is $s_{f_0}=16$ while the rabbit’s is $s_{r_0}=13$.

**Problem 2**

In the first problem, the velocity of fox and rabbit is assumed to be a function of the distance it has run. This is natural since any creature will get tired by long distance running. The loss of velocity is modelled as exponential to time.

The fox’s velocity is $s_f(t)=s_{f_0}\exp(-\mu_f d_f(t))$, in which $\mu_f=0.0002,s_{f_0}=16$, $d_f(t)$ is the distance the fox has run.

The rabbit’s velocity is $s_r(t) = s_{r_0}\exp(-\mu_r d_r(t)))$, in which $\mu_r=0.0008,s_{r_0}=13$, $d_r(t)$ is the distance the rabbit has run.

## Pre-process

**The velocity function used in Problem 2**

In fact, we know that the distance the fox or rabbit run is actually the integral of its velocity. Hence the velocity function given in Problem 2 is actually an integral equation, i.e.

$\ln s_f(t) = \ln s_{f_0}-\mu_f d_f(t)\Leftrightarrow s'_f(t)/s_f(t)=-\mu_j s_f(t)$ with $d_f'(t)=s_f(t)$ and initial value $s_f(0)=s_{f_0}$.

solving this different equation, we get $s_f(t)=\dfrac{s_{f_0}}{1+\mu_f s_{f_0}t}$

similarly, $s_r(t)=\dfrac{s_{r_0}}{1+\mu_r s_{r_0}t}$.

**To detect if the fox can see the rabbit**

Obviously the fox can see the rabbit if and only if the line segment connecting them doesn’t intersect with the warehouse, in fact, if they intersects, the intersecting point is only possible to lie on the south or east edge.

Suppose the y-coordinate of the south/north edge of the warehouse is $y_s,y_n$, and the x-coordinate of the east edge of the warehouse is $x_e$.

The line connecting the fox $(x_f,y_f)$and rabbit $(x_r, y_r)$ can be expressed as $\dfrac{x-x_r}{x_f-x_r}=\dfrac{y-y_r}{y_f-y_r}$ 

- if it intersects with the south edge, then the x-coordinate of the intersecting point would be $\hat{x}_s=x_r+\dfrac{(x_f-x_r)(y_s-y_r)}{y_f-y_r}$, hence if $\hat{x}_s\leqslant x_e$, then the fox cannot see the rabbit.
- if it intersects with the east edge, then the y-coordinate of the intersecting point would be $\hat{y}_e=y_r+\dfrac{(x_e-x_r)(y_f-y_r)}{x_f-x_r}$, hence if $y_s\leqslant\hat{y}_e\leqslant y_n$, then the fox cannot see the rabbit.
- otherwise, the fox’s able to see the rabbit.

We will use these two conditions to check if the fox can see the rabbit in out program.

## Method

**Equations**

Given the location of the fox $P_f(t)$ and rabbit $P_r(t)$, the velocity of them can be instantly calculated only use these two points. Hence we come up with the ODE:

$P’_f(t)=f_1(P_f, P_r), P'_r(t)=f_2(P_f, P_r)$

It is a standard first order ODE, so with the built-in `ode45/ode23` function in MATLAB. given the time span. initial value, and derivatives with respect to the time and current position, we can solve the whole trajectory out.

**To determine the result**

We solve the equation in a sufficient long period, and give a special configuration: If $P_f(t)$ and $P_r(t)$ is sufficiently close, or $P_r(t)$ is sufficiently close to the position of the rabbit’s home $Q$ at some time, the derivative is set to 0. That’s to say, the rabbit and fox don’t need to run anymore since the rabbit has hidden or the fox has caught the rabbit.

Hence if the solution becomes constant after some time point. then the fox either has caught the rabbit, or fail to catch it. The only thing we need to distinguish these two situation is to check $P_f(t)$ and $P_r(t)$.

## Result

**Problem 1**

As we can see from the graph, the fox doesn’t catch the rabbit, although it has run about 1044 meters for about 65.3 seconds. The final position of the fox is $(-448.3938,410.7340)$. Animation below (adopting `ode23`, `ode45` and `ode113` respectively):

![image-20221105215801901](Report_1.assets/image-20221105215801901.png)

![image-20221105215810909](Report_1.assets/image-20221105215810909.png)

![image-20221105215823275](Report_1.assets/image-20221105215823275.png)



Output:

```
>> part 1, method: ode45
Catched: false
Fox coordinate: 
 -448.4123
  410.7562
Total distance: 1044.168
Total time: 65.3
<< method: ode45
>> part 1, method: ode23
Catched: false
Fox coordinate: 
 -448.3938
  410.7340
Total distance: 1044.1387
Total time: 65.3
<< method: ode23
>> part 1, method: ode113
Catched: false
Fox coordinate: 
 -448.3944
  410.7339
Total distance: 1044.1388
Total time: 65.3
<< method: ode113
```

**Problem 2**

As we can see from the graph, the fox caught the rabbit, after running about 1271.24 meters for about 90.5 seconds. The final position of the fox (the place the fox caught the rabbit) is $(-586.2698,586.2698)$. Animation below (adopting `ode23`, `ode45` and `ode113` respectively):

![image-20221106103440342](Report_1.assets/image-20221106103440342.png)

![image-20221106103508468](Report_1.assets/image-20221106103508468.png)

![image-20221106103534275](Report_1.assets/image-20221106103534275.png)

Output:

```
>> part 2, method: ode45
Catched: true
Fox coordinate: 
 -586.2698
  586.2669
Total distance: 1271.2395
Total time: 90.5
<< method: ode45
>> part 2, method: ode23
Catched: true
Fox coordinate: 
 -586.1998
  586.2003
Total distance: 1271.1436
Total time: 90.5
<< method: ode23
>> part 2, method: ode113
Catched: true
Fox coordinate: 
 -586.1928
  586.1939
Total distance: 1271.1339
Total time: 90.5
<< method: ode113
```

