## Q1

We're going to prove by slightly modifying the Cantor’s Back-and-Forth Theorem.

Since $\lang P,\leq_P\rang,\lang Q, \leq_Q\rang$ are countable and $p\in P,q\in Q$, we can find some enumerations of them respectively, and denote them as 
$$
P=\{p_n\mid n\in\omega\},\ Q=\{q_n\mid n\in\omega\},\ p_0=p,q_0=q
$$
We shall construct an increasing sequence $\{f_n\mid n\in \omega\}$ of partial isomorphism such that

- $f_n\sub f_{n+1}$ (here functions are considered as pairs within $P\times Q$)
- $\mathrm{dom}\supset \{p_0,\cdots ,q_{n-1}\}$ and $\mathrm{range} (f_n)\supset \{b_0,\cdots,b_{n-1}\}$
- $f_n$ is finite for all $n$

The sequence is constructed as follows from initial value  $f_0=\{(p,q)\}=\{(p_0,q_0)\}$ and $f_0^{-1}=\{(q,p)\}=\{(q_0,p_0)\}$, apparently $f_0$ is a partial isomorphism. (DLO denotes the word **dense linear ordering without endpoints**)

1. [Inheritance] If $p_n\in \mathrm{dom}(f_n)$ then define $f_{n+1/2}=f_n$
2. [lower bound] If $\forall e\in\mathrm{dom}(f_n), p_n<e$, then since $Q$ is DLO and $f_n$ finite, there exists $q'\in Q$ s.t. $\forall\ e\in \mathrm {range}(f_n),q'<e$. We assign that $f_{n+1/2}(p_n)=q'$. 
3. [Upper bound] If conversely $\forall e\in\mathrm{dom}(f_n), e<p_n$, then since $Q$ is DLO and $f_n$ finite, there exists $q'\in Q$ s.t. $\forall\ e\in \mathrm {range}(f_n),e<q'$. We assign that $f_{n+1/2}(p_n)=q'$. 
4. [Minimal interval] If $\exists\ a,b\in\mathrm{dom}(f_n)$, s.t. $a<b$ and $(a,b)\cap \mathrm{dom}(f_n)=\varnothing$ and $a<p_n<b$, then since $f_n$ is isomorphism, there <u>doesn't</u> exist $c\in \mathrm{range}(f_n)$ such that $f_n(a)<c<f_n(b)$. Thus since Q is DLO, we can pick up some $c\in f_n(a)<c<f_n(b)$ from $Q-\mathrm{range}(f_n)$, define $f_{n+1/2}(p_n)=c$.

The procedure above shows the construction of $f_{n+1/2}$, i.e. an extension of $f_n$ that convers $p_n$. From the other sider, applying the same arguments, we can define $f_{n+1/2}^{-1}$, putting both directions together, we get the extended maps $f_{n+1},f_{n+1}^{-1}$, which is also an partial isomorphism.

Finally, due to the countability, let 
$$
f=\bigcup_{n\in\omega}f_n
$$
We get that $f$ is an isomorphism between $P=\mathrm{dom}(f)$, $Q=\mathrm{range}(f)$ and furtherly $f(p)=q$ for the given $p\in P,q\in Q$.

## Q2



## Q3

$\langle X,d\rangle$ is a complete metric space, $C\sub X$ is closed.

Let $\{x_n\}_{n=1}^\infty\sub C $ be any Cauchy sequence under $d$, then it must converge to some $x\in X$ due to the completeness of $\lang X,d\rang$. Thus $x$ is also an accumulation point of $X$. 

Finally, since $C$ is closed, it must contains all accumulation points of itself. Thus $x\in C$, followed by $d|_C$ is complete. 

## Q4

$\lang X,d\rang $ is a metric space, suppose it is separable, then it contains a countable dense subset, say $S$. Then every point in $X$ is an accumulation point of $S$, so are points in $Y\sub X$, which is uncountable with any two distinct points in it have distance larger than $1$.

Thus for any $\varepsilon>0$, here we take $\varepsilon=\dfrac{1}{4}$, for any point $y\in Y$, we can find $x\in S$ such that $d(x,y)<\dfrac{1}{4}$. Fix such $x$ and define a bijection function $f:Y\to S$. Since by the property of $Y$, $\forall\ a, b\in Y,d(a,b)>1$, we'd have 
$$
\begin{align}
\forall\ x_1,x_2\in \mathrm{range}(f)\sub S,\ d(x_1,x_2)&\geqslant d(f^{-1}(x_1),f^{-1}(x_2))-d(f^{-1}(x_1),x_1)-d(x_2,f^{-1}(x_2))\\
&>1-\dfrac{1}{4}-\dfrac{1}{4}=\dfrac{1}{2}
\end{align}
$$
hence $|S|\geqslant |\mathrm{range}(f)|=|Y|>\omega$, as $Y$ is uncountable, $S$ cannot be countable, contradictory.

Thus $X$ contains no countable dense subset, $X$ is not separable.

## Q5

Since $\lang X,d\rang$ is a separable metric space, there exists a countable dense subset $S=\{s_1,s_2,\cdots,s_n,\cdots\}$ of $X$. We'll prove a stronger conclusion that $X$ is either countable or has cardinality of continuum. If this holds, then $B(x,\varepsilon)\sub X$ will also be either countable or has cardinality of the continuum.

$\forall\ x\in X$, consider the tuple $d_x=(d(x,s_1),d(x,s_2),\cdots,d(x,s_n),\cdots)$  and define $f:X\to \mathbb{R}^\mathbb{N},x\mapsto d_x$. Suppose $f(x)=f(y)$ but $x\neq y$, then due to the denseness of $S$, we can find $a\in S$ such that $d(x,a)=d(y,a)<\dfrac{d(x,y)}{2}$, but by the definition of metric, $d(x,a)+d(y,a)\geqslant d(x,y)$, contradictory. Therefore $f$ is injective, followed by $|X|\leqslant |\mathbb{R}^{\mathbb{N}}|=|\mathbb{R}|$, which means $X$ is either countable or has cardinality of the continuum.

**Remark:** we claim that $|\mathbb{R}^\mathbb{N}|=|\mathbb{R}|$. Prove is given below:

$\mathbb{R}$ can be depicted as the set of function (binary expansion) $f:\mathbb{R}\to \{0,1\}$, then for any $x=(x_1,x_2,\cdots,x_n,\cdots)\in\mathbb{R}^\mathbb{N}$, $x$ can be depicted as a function 
$$
g:\mathbb{N}\times \mathbb{N}\to \{0,1\},\qquad g(m,n)=f_n(m)
$$
As $|\mathbb{N}\times\mathbb{N}|=|\mathbb{N}|$, we know that $|\mathbb{R}^\mathbb{N}|=|\{g\}|=|\{f\}|=|\mathbb{R}|$.