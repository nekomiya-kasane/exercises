## Preface

In this report, we focus on the implementation and analysis of various numerical methods for solving partial differential equations (PDEs), with the goal of gaining a comprehensive understanding of their performance. These methods find direct applications in multiple disciplines, including computational fluid dynamics, computational chemistry, and more. 

As we are primarily interested in CFD, we have explored methods that are widely used to simulate fluid dynamics. Specifically, we have evaluated the performance of various PDE numerical methods, including finite difference, finite element, and spectral methods, and compared their accuracy and efficiency for solving fluid dynamics problems. 

Additionally, we have investigated the Lattice Boltzmann Method, which provides a mesoscale perspective for modeling fluid mechanics. By the end of this report, we hope to have gained deeper insights into the underlying principles of these methods, as well as their practical applications in CFD and related fields.

### Description of the Problem

For convenience, through out this report, we will use the Poisson Equation $-\Delta u=f$ and heat equation $u_t=a\Delta u +f$ to illustrate different methods, and the boundary is set to be smooth except at finite points. i.e.
$$
-\Delta u=f\text{ on } \Omega,\quad \Gamma=\partial\Omega\quad (1)\\
u_t=a\Delta u +f\text{ on } \Omega,\quad \Gamma=\partial\Omega\quad (2)
$$
Distinct boundary conditions (BC) will be applied, the following list shows the 3 most commonly used BCs:

- Dirichlet BC: $u=g$ on $\Gamma$
-  Neumann BC: $\dfrac{\partial u}{\partial n}=g$ on $\Gamma$
- Robin BC: $au+b\dfrac{\partial u}{\partial n}=g$ on $\Gamma$

Now move on to the main sections of our report.

## Finite Difference Method

This method is particularly suitable for smooth equations with simple boundary shapes. Say we have a square region $\Omega=[0,1]\times[0,1]$, consider the Poisson Equation with Dirichlet BC:
$$
-\Delta u=f\text{ on } \Omega,\quad \Gamma=\partial\Omega,\quad u=g \text{ on } \Gamma
$$
We are going to give out the standard **five-point stencil** of this problem.

Firstly, divide $\Omega$ with 2 bunches of equidistant lines parallel to the x- and y-axis. Let $h=\dfrac{1}{n}$,
$$
x=ih,\ y=jh,\quad i=0,1,2,\cdots,n\quad j=0,1,2,\cdots,n
$$
The intersection of the 2 bunch of lines are named nodes and denoted as $P_{ij}=(x_i,y_j)$, then $\Omega$ contains $2(n+1)(2n+1)$ nodes and the internal nodes can be defined:
$$
\mathcal{N}_{h}^I=\{(x_i,y_j)\mid 1\leqslant i\leqslant n-1,1\leqslant j\leqslant n-1\}
$$
The basic idea of approximating the derivative is to use difference quotients, by performing Taylor expansion, we have
$$
\dfrac{d^2v}{dx^2}=\dfrac{v(x-h)-2v(x)+v(x+h)}{h^2}\label{eq:aa}
$$
for a function $v(x)$, here we used central finite difference approximation, but I'd mention that there are a lot of schemes in the family of schemas, each of difference form and order. Here is just one example.

> **Remark**: the proof and error estimate of $\eqref{eq:aa}$ is quite easy,
> $$
> \begin{align*}
> &v(x-h)=v(x)-\dfrac{v'(x)h}{1!}+\dfrac{v''(x)h^2}{2!}-\dfrac{v'''(x)h^3}{3!}+o(h^3)\\
> &v(x+h)=v(x)+\dfrac{v'(x)h}{1!}+\dfrac{v''(x)h^2}{2!}+\dfrac{v''’(x)h^3}{3!}+o(h^3)
> \end{align*}
> $$
> Hence 
> $$
> v(x-h)-2v(x)+v(x+h)=v''(x)h^2+o(h^3)=v''(x)h^2+\dfrac{h^4}{12}v^{(4)}(\xi),\quad \xi\in(x-h,x+h)\label{eq:fde}
> $$
> hence the approximation holds and is of the second order.
>
> In the following paragraph, We will not give the full proof of similar equations since most of them come from Taylor Series and are easy to verify.

Therefore we have
$$
\begin{align*}
&u_{xx}(x_i,x_j)\approx\dfrac{u(x_{i-1},y_j)-2u(x_i,y_j)+u(x_{i+1},y_j)}{h^2}\\
&u_{xx}(x_i,x_j)\approx\dfrac{u(x_{i},y_{j-1})-2u(x_i,y_j)+u(x_{i},y_{j+1})}{h^2}
\end{align*}
$$
Let $u_{ij}=u(x_i,y_j)$ and $f_{ij}=f(x_i,y_j)$, then we achieved our discretization schema (5-point stencil) for the $\Delta$ operator:
$$
\begin{align*}
\Delta_h u_{ij}&=\dfrac{u_{i-1,j}-2u_{ij}+u_{i,j+1}}{h^2}+\dfrac{u_{i,j-1}-2u_{ij}+u_{i+1,j}}{h^2}\\
&=\dfrac{u_{i-1,j}+u_{i+1,j}+u_{i,j-1}+u_{i,j+1}-4u_{ij}}{h^2}\\
&=-f_{ij}
\end{align*}
$$
At the boundary points, $u_{ij}=g(x_i,y_j)$, $i=0\vee j=0\vee i=n\vee j=n$. By $\eqref{eq:fde}$, we have a estimated truncation bound: $\exist\ \xi\in(x_{i-1},x_{i+1}),\eta\in(y_{i-1},y_{i+1})$ such that 
$$
R_{ij}=f(x_i,y_j)+\Delta_h u(x_i,y_j)=-\Delta_h u(x_i,y_j)+(\Delta u)(x_i,y_j)=\dfrac{h^2}{12}(u^{(4,0)}(\xi,y_j)+u^{(0,4)}(x_i,\eta))
$$
To solve the discretized equations, we can use <u>sparse Matrix</u> to store all the coefficients.

There's also 9-point stencil that can be seen as a linear combination of a 5-point stencil and a rotated 5-point stencil.
$$
\begin{align*}
\Delta_h u_{ij}&=\{(1-\alpha)\ \begin{array}{|c|c|c|}
\hline 
0&1&0\\\hline1&-4&1\\\hline0&1&0\\\hline
\end{array}+\dfrac{\alpha}{2}\ \begin{array}{|c|c|c|}
\hline 
1&0&1\\\hline0&-4&0\\\hline1&0&1\\\hline
\end{array}\ \}u_{ij}
\end{align*}
$$
Let $\alpha=\dfrac{1}{3}$, we get a typical 9-point Laplacian formula,
$$
\Delta_h u_{ij}=\dfrac{1}{6h^2}(4u_{i-1,j}+4u_{i+1,j}+4u_{i,j-1}+4u_{i,j+1}+u_{i-1,j-1}+u_{i-1,j+1}+u_{i+1,j-1}+u_{i+1,j+1}-20u_{ij})
$$

### Implementation

The coefficient matrix of 5-point stencil is obtained by the following function:

```julia
function GenerateCoeffMatrix5Point(N::Int64, h::Float64)
    id = (i, j) -> (i - 1) * N + j;
    nonzero_size = (N - 4) * (N - 4) * 5 + (N - 4) * 4 * 4 + 4 * 3
    ids_row = zeros(Int32, nonzero_size);
    ids_col = zeros(Int32, nonzero_size);

    values = zeros(Float64, nonzero_size);

    row = 1;
    count = 1;
    for i = 2 : N - 1, j = 2 : N - 1
        if i - 1 > 1 # up
            ids_row[count] = row;
            ids_col[count] = id(i - 1, j);
            values[count] = 1 / h ^ 2;
            count += 1;
        end
        if i + 1 < N # down
            ids_row[count] = row;
            ids_col[count] = id(i + 1, j);
            values[count] = 1 / h ^ 2;
            count += 1;
        end
        if j - 1 > 1 # left
            ids_row[count] = row;
            ids_col[count] = id(i, j - 1);
            values[count] = 1 / h ^ 2;
            count += 1;
        end
        if j + 1 < N # right
            ids_row[count] = row;
            ids_col[count] = id(i, j + 1);
            values[count] = 1 / h ^ 2;
            count += 1;
        end

        # center
        ids_row[count] = row;
        ids_col[count] = id(i, j);
        values[count] = -4 / h ^ 2; 
        count += 1;

        # next equation
        row += 1;
    end

    return sparse(ids_row, ids_col, values);
end
```

The coefficient matrix of the 9-point stencil is obtained similarly in the function `GenerateCoeffMatrix9Point`, due to limitations on the length of the article, we have omitted this section of code.

Consider when ==$f(x,y)=\sin \pi x\sin\pi y$== and ==$g=0$==, the [analytical solution](https://math.stackexchange.com/questions/3630678/analytical-solution-to-poissons-equation-with-sinusoidal-source) is ==$u(x,y)=-\dfrac{\sin(\pi x)\sin(\pi y)}{2\pi^2} $==. 



### Analysis

#### Application

The simplicity of implementation and analysis of this method has led to its widespread adoption for both general applications and teaching purposes. The method is based on the assumption that the solution is smooth (or at least twice continuously differentiable) and Lipschitz continuous. This allows us to control the discretization error within a specified bound when we discretize either the space or time domains.

Moreover, since the discretization is performed on a grid, boundary-shape-oriented adjustments can be complicated and may result in significant losses.

#### Error

