### Prob 1

$V=\mathbb{C}^2$, let $T:(v,w)\mapsto (0,w)$. then 

<u>Claim</u>: $T$ is a linear transformation $T\in\mathcal{L}(V,V)$.

Proof: $\forall\ (v_1,w_1),(v_2,w_2)\in\mathbb{C}^2$, we have 
$$
T((v_1,w_1)+(v_2,w_2))=T(v_1+v_2,w_1+w_2)=(0,w_1+w_2)=(0,w_1)+(0,w_2)=T(v_1,w_1)+T(v_2,w_2)
$$
and $\forall\ \lambda \in \mathbb{R}$, we have
$$
T(\lambda (v,w))=T(\lambda v,\lambda w)=(0,\lambda w)=\lambda(0,w)=\lambda T(0,w)
$$
and $T(0,0)=(0,0)$, there fore $T$ is a linear transformation.

<u>Claim:</u> $T=\text{null}\ T\oplus \text{range}\ T$.

Prove: let $S_1=\{(0,w)|w\in\mathbb{C}\},S_2=\{(v,0)|v\in\mathbb{C}\}$, then
$$
\forall\ (v,w)\in\mathbb{C}^2,\text{we have }(v,w)=(0,w)+(v,0)\in S_1\oplus S_2\quad \Rightarrow\quad \mathbb{C}^2\subset S_1\oplus S_2\\
\text{basis of }S_1,S_2, \text{ i.e. }(0,1)\in\mathbb{C}^2, (1,0)\in \mathbb{C}^2\quad \Rightarrow\quad S_1\oplus S_2\subset\mathbb{C}^2
$$
hence $\mathbb{C}^2=S_1\oplus S_2$. Note that $\text{null}\ T=S_2,\text{range}\ T=S_1$, hence $T=\text{null}\ T\oplus\text{ range }T$.

### Prob 2

Let $v_1=(1,-2,0,0,0,0), v_2=(0,0,1,0,-1,0), v_3=(1,0,0,1,-1,0)$, then $\forall\ x=(x_1,x_2,x_3,x_4,x_5,x_6)\in \text{null }T$, we have
$$
x\cdot v_1=x\cdot v_2=x\cdot v_3=0
$$
where $\cdot$ for inner product. Hence $\text{null }T=\text{span}\{v_1,v_2,v_3\}^\perp$.

therefore $\text{dim null }T=\text{dim range }T=3$. But since $T\in\mathcal{L}(\mathbb{R}^6,\mathbb{R}^2)$, we know $\text{dim range }T\leqslant 2$. Contradictory. Hence such $T$ doesn't exists.

### Prob 3

1. $T:a+bx+cx^2\mapsto -6c+a+bx+cx^2$ if $T\in\mathcal{L}(\mathcal{P}_2,\mathcal{P_2})$. Using the standard monomial basis for the domain and codomain, we have 

   $T:(a,b,c)\mapsto (-6c+a,b,c)$. using row vectors, the matrix of $T$ should be
   $$
   [T]=\begin{bmatrix}1&0&0\\0&1&0\\-6&0&1\end{bmatrix}
   $$
   if we use column vector, then the matrix is transposed.

2. $T:a+bx+cx^2+dx^3\mapsto (a+6d-6c)+(-18d+b)x+cx^2+dx^3$ if $T\in\mathcal{L}(\mathcal{P}_3,\mathcal{P_3})$. Using the standard monomial basis for the domain and codomain, we have $T:(a,b,c,d)\mapsto (a+6d-6c,b-18d,c,d)$. using row vectors, the matrix of $T$ should be
   $$
   [T]=\begin{bmatrix}1&0&0&0\\0&1&0&0\\-6&0&1&0\\6&-18&0&1\end{bmatrix}
   $$
   if we use column vector, then the matrix is transposed.

3. $T:a+bx+cx(x-1)\mapsto (a-6c)+(b-c)x+cx^2$ if $T\in\mathcal{L}(\mathcal{P}_2,\mathcal{P_2})$. Using the Newton basis for the domain and standard monomial basis for the codomain, we have $T:(a,b,c)\mapsto (a-6c,b-c,c)$​.  

   using row vectors, the matrix of $T$ should be
   $$
   [T]=\begin{bmatrix}1&0&0\\0&1&0\\-6&-1&1\end{bmatrix}
   $$
   if we use column vector, then the matrix is transposed.

4. $T:a+b(x-1)+c(x-1)^2+d(x-1)^3\mapsto (a-b-5c+23d)+(b-2c-15d)x+(c-3d)x^2+dx^3$ if $T\in\mathcal{L}(\mathcal{P}_3,\mathcal{P_3})$. Since RHS $=(a-6c+6d)+(b-c-17d)(x-1)+(c-3d)(x-1)x+(d)x(x-1)(x+1)$. Using the shifted monomial basis for the domain and Newton basis for the codomain, we have $T:(a,b,c)\mapsto (a-6c+6d,b-c-17d,c-3d,d)$​.  

   using row vectors, the matrix of $T$ should be
   $$
   [T]=\begin{bmatrix}1&0&0&0\\0&1&0&0\\-6&-1&1&0\\6&-17&-3&1\end{bmatrix}
   $$
   if we use column vector, then the matrix is transposed.

### Prob 4

1. Let $\mathcal{L}(V,W)$ be defined over field $F$,  We have

   - The zero linear transformation $O\in\mathcal{L}(V,W)$ satisfies $Ov=0$, hence $O\in E_v$.
   - For all $\lambda \in F$, $T\in E_v\subset\mathcal{L}(V,W)$, we have $Tv=0\Rightarrow \lambda Tv=\lambda 0=0\Rightarrow \lambda T\in E_v$.
   - For all $T,S\in E_v\subset \mathcal{L}(V,W)$, we have $Tv=Sv=0\Rightarrow (T+S)v=Tv+Sv=0+0=0\Rightarrow T+S\in E_v$
   - For any $T\in E_v$, we have $Tv=0\Rightarrow (T+(-T))v=Ov=0$ and $-Tv=-0=0$, hence the inverse of $T\in E_v$, $-T\in E_v$.

   hence $E_v$ is a subspace of $\mathcal{L}(V,W)$.

2. let $\text{dim }V=n$, $\text{dim } W=m$, then $\forall\ T\in \mathcal{L}(V,W)$, $v\in \text{null }T$. $\text{dim null }T>0$.

   Take a set of basis of $(\text{span } v)^\perp=P$, say $v_1,v_2,\cdots, v_{n-1}$. and take a set of basis of $W$, say $w_1,w_2,\cdots,w_m$, then $V=\text{span }\{v,v_1,v_2,\cdots,v_{n-1}\}$. And we can construct a set of basis of $\mathcal{L}(P,W)$, i.e.
   $$
   B=\left\{T_{ij}:T_{ij} v_k=\left\{\begin{array}{l}w_j,k=i\\0,k\neq i\end{array}\right.\right\}
   $$
   Therefore $\text{dim }E_v=|B|=(n-1)m=(\text{dim }V-1)\text{ dim W}$