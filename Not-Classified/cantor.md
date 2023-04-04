From the construction of Canton Set and by the Cauchy-Cantor Theorem, 
$$
\forall\ x\in \mathcal{C},\ x=\sum_{n=1}^{+\infty}\dfrac{d_i}{3^n},\ d_n\in\{0,2\}
$$
<u>Claim:</u> the expression for a specific $x$, i.e. the choice of $d_n$ is unique.

<u>Prove:</u> Suppose that $\displaystyle x=\sum_{n=1}^{+\infty}\dfrac{d_i}{3^n}=\sum_{n=1}^{+\infty}\dfrac{d_i'}{3^n}$. If $(d_i)$ is not identical to $(d'_i)$, denote the first distinct digit as $d_m$, then 
$$
\left|\sum_{n=m+1}^{+\infty}\dfrac{d_n-d_n'}{3^n}\right|\leqslant \sum_{n=m+1}^{+\infty}\left|\dfrac{d_n-d_n'}{3^n}\right|\leqslant \sum_{n=m+1}^{+\infty}\dfrac{2}{3^n}=3^{-m}<2\cdot \dfrac{|d_m-d_m'|}{3^m}=\dfrac{2}{3^m}
$$
Hence 
$$
\sum_{n=1}^{+\infty}\dfrac{d_i}{3^n}-\sum_{n=1}^{+\infty}\dfrac{d_i'}{3^n}\neq 0
$$
Contradictory. Therefore, the expression is unique.

----

Then it becomes easy to prove that every point in $\mathcal{C}$ is a cluster point.

For any $\displaystyle x=\sum_{n=1}^{+\infty}\dfrac{d_i}{3^n}\in\mathcal{C}$, take an arbitrary $\varepsilon>0$, let $m=\max\{1,\lceil\log_3 (2\cdot\varepsilon^{-1})\rceil\}$ and 
$$
y_{\varepsilon}=\displaystyle \sum_{n=1}^{+\infty}\dfrac{d_i'}{3^n}\in\mathcal{C},\quad d_i=d_i'\text{ for $i\neq m$ and } d_i\neq d_i'\text{ (i.e. one equals $0$ and the other equals $2$) otherwise}
$$
referring to the claim above, we can deduce that the expression is unique and 
$$
|x-y_{\varepsilon}|=2\cdot 3^{-m}<\varepsilon
$$
That is to say, $x$ is a cluster point of $\mathcal{C}$. Consequently, every point of the Cantor Set is a cluster point.
$$

$$
