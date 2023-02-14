## Problem 1

Firstly, I search about the 3-compartment model and found that 2 important parts are contained in the model, that is clearance (metabolized) and transition. There are different tissues in human’s body, and the model described the behavior of diffusion and absorption of drugs between tissues.

Secondly, I made an assumption, the two parts are all proportional to the concentration gradient, hence volumes are included. For subcutaneous dosing, the volume of subcutaneous compartment is usually ignored.

Hence we can come up with ODEs composed of these two parts. By the assumption, they’re linear and can be solved numerically using Euler or RK method, Maple provides us with inbuilt methods. 

Doses are expressed as Dirac function, that is, for convenience, the injection time is ignored.

## Problem 2

1. the equilibrium points for system $x’=f(x,y)$ and $y’=g(x,y)$ are those points that satisfy $f(x,y)=g(x,y)=0$, so solving this equation gives us the solutions.
2. Linearization and classification of equilibrium points can be done by calculating the Jacobi matrix of the right hand side of the equations, and observe the eigenvalues.
   - if all real part of eigenvalues are negative, it’s a stable point.
   - if all real part of eigenvalues are positive, it’s an unstable point.
   - if real part of one eigenvalue is negative and the other positive, it’s a saddle point.
3.  Phase Portrait consists of null curves (trajectories and arrows) and equilibrium points, Maple provides DEtool to draw it.
4. We can confirm this by enumerating and comparing all stable equilibrium points of $x,y$ in the absence of each other, and both present. Since stable population of $x$ increases by $11/7$, $y$ by $8/7$, they all benefit from the protocooperation.

如果$k=1$时都无穷了，$m(D_{|f|\geq 1})=\infty$，那$\int_{D} f$ 也是无穷了，是trivial情况不需要讨论吧.. 