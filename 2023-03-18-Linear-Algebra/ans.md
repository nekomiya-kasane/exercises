## Question 1

1. Given 2 $n$-vectors, say $\mathbf{a}=(a_1,a_2,\cdots,a_n)$ and $\mathbf{b}=(b_1,b_2,\cdots,b_n)$, by the definition, their inner product is 
   $$
   \langle\mathbf{a},\mathbf{b}\rangle=\mathbf{a}^T\mathbf{b}=a_1b_1+a_2b_2+\cdots+a_nb_n
   $$
   which includes $n$ multiplications and $n-1$ additions. Generally, each multiplication & addition operation costs 1 flop. Therefore an inner product of two $n$-vectors requires $n+(n-1)=2n - 1$ flops.

2. Note that
   $$
   \forall\ n\in\mathbb{N}^+,\quad n\leqslant 2n-1\leqslant 2n\quad\Rightarrow\quad  T(n)=2n-1=\Omega(n)\ \text{and}\ O(n)
   $$
   hence $T(n)=2n-1=\Theta(n)$, that is,  The time complexity of an inner product is of order $n$.
   $$
   T(2n)=4n-1,\ T(\dfrac{n}{2})=n-1
   $$
    or according to the fact that $T(n)=\Theta(n)$, if we double the size of the two vectors, approximately, the computation time will also be doubled, and if we halve the size of the 2 vectors, the computation time will also be halved.

   The number of flops will increase nearly proportionally of coefficient 2 to the size of the vectors.

## Question 2

1. Note that for the $i$-th squirrel, if it is a friend of Atto's, then $a_i=1$, and if of Besso's, then $b_i=1$, then if of both the 2 squirrels', then $a_i=b_i=1\Rightarrow a_ib_i=1$, otherwise, it is not a friend of Atto's or Besso's.

   Also note that $\langle\mathbf{a},\mathbf{b}\rangle=\mathbf{a}^T\mathbf{b}=a_1b_1+a_2b_2+\cdots+a_nb_n=\displaystyle \sum_{i=1}^n a_ib_i$, hence $\langle\mathbf{a},\mathbf{b}\rangle=\mathbf{a}^T\mathbf{b}$ depicts the number of friends Atto and Besso have in common.

2. Note that $a_i=1\ \Leftrightarrow\ a_i^2=1$, and $\mathbf{a}^2=\mathbf{a}^T\mathbf{a}=\displaystyle \sum_{i=1}^n a_i^2$ is the number of Atto's friends, similar facts for Besso. Hence we can determine who has more friends by comparing $\mathbf{a}^2$ with $\mathbf{b}^2$.

   - if $\mathbf{a}^2>\mathbf{b}^2$, then Atto has more friends;
   - if $\mathbf{a}^2<\mathbf{b}^2$, then Besso has more friends;
   - if $\mathbf{a}^2=\mathbf{b}^2$, they have the same number of friends.

3. $\#\{\text{friends of only Besso's}\}=\#\{\text{friends of Besso's}\}-\#\{\text{friends of both Atto's and Besso's}\}$, the result is $\mathbf{b}^2-\mathbf{a}^T\mathbf{b}=(\mathbf{b-a})^T\mathbf{b}$.

## Question 3

1. $d=a_{2:n}-a_{1:(n-1)}$

2. Since $a_i$ is the price in day $i$ and $d_i=a_i-a_{i-1}$, $d_i$ means the increment of the price at day $i$ comparing with that in day $i-1$.

3. By the definition, similar to 2., we can observe that $s=d_{2:(n-1)}-d_{1:(n-2)}$, by 1., we have
   $$
   s=d_{2:(n-1)}-d_{1:(n-2)}=(a_{3:n}-a_{2:(n-1)})-(a_{2:(n-1)}-a_{1:(n-2)})=a_{3:n}-2a_{2:(n-1)}+a_{1:(n-2)}
   $$

## Question 4

1. Let $\mathbf{a}=(a_1,a_2)^T$, $\mathbf{x}=(x_1,x_2)^T$, we have $\phi(\mathbf{x})=\mathbf{a}^T\mathbf{x}=a_1x_1+a_2x_2$, so by the linearity, 
   $$
   \phi(1,0)=\dfrac{1}{2}(\phi(2,1)-\phi(0,1))=3=a_1
   $$
   and since $\phi(0,1)=a_2=-1$, we can conclude that $\mathbf{a}=(3,-1)^T$.

2. Let $\mathbf{a}=(a_1,a_2)^T$, $\mathbf{x}=(x_1,x_2)^T$, we have $\phi(\mathbf{x})=\mathbf{a}^T\mathbf{x}+b=a_1x_1+a_2x_2+b$, then
   $$
   \dfrac{1}{2}(\psi(2,1)-\psi(0,1))=a_1=3,\quad \psi(0,1)=a_2+b=0
   $$
   hence we know $\mathbf{a}=(3,-b)^T$. If $b$ is determined, then $\mathbf{a}$ is also determined.

3. Let $\mathbf{a}=(a_1,a_2,a_3)^T$, $\mathbf{x}=(x_1,x_2,x_3)^T$, we have $\phi(\mathbf{x})=\mathbf{a}^T\mathbf{x}+b=a_1x_1+a_2x_2+a_3x_3+b$, then
   $$
   \dfrac{1}{2}(\xi(2,1,3)-\xi(0,1,1))=a_1+a_3=4,\quad \xi(0,1,1)=a_2+a_3+b=2
   $$
   hence let $a_3=c$, we'd have $a_1=4-c,a_2=2-b-c,a_3=c$, thus
   $$
   \mathbf{a}=(a_1,a_2,a_3)^T=(4-c,2-b-c,c)^T=(4,2-b,0)^T-c(1,1,-1)^T
   $$
   if $b$ is determined, then $\mathbf{a}$ lies on a line through $(4,2-b,0)^T$.

## Question 5

Applying triangle inequality to $(a+b)+(-b),(a+b)+(-a)$, we have
$$
||a||=||(a+b)+(-b)||\leqslant  ||a+b||+||-b||=||a+b||+||b||\\
||b||=||(a+b)+(-a)||\leqslant  ||a+b||+||-a||=||a+b||+||a||
$$
which leads to 
$$
||a+b||\geqslant ||a||-||b||,\quad ||a+b||\geqslant ||b||-||a||
$$
therefore 
$$
||a+b||\geqslant \max\{||a||-||b||,||b||-||a||\}=\left|||a||-||b||\right|
$$
