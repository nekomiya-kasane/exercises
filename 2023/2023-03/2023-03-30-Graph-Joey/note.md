Under the <u>Von Neumann's Definition</u>, the cardinality of a well-ordered set $X$ is the least ordinal number $x$ such that there is a bijection between $X$ and $x$. Hence given two sets $A$ and $B$,

> Remark: This definition takes ordinals as sets, for example, 
>
> $0=\varnothing$, $1=\{\varnothing\}$, $2=\{\varnothing,\{\varnothing\}\}$, ...
>
> $a=a+1=\{\varnothing,a\}$
>
> Here's a graph from Wikipedia showing the order of ordinals:
>
> ![img](note.assets/430px-Omega-exp-omega-normal_svg.svg.png) 

- by the theorem of well-ordering, $A$, $B$ are well-orderable. Thus we can find an ordinal and cardinal $\lambda_A$, $\lambda_B$ for each of them. And there should be 2 bijections, between $A$ and $\lambda_A$, $B$ and $\lambda_B$ respectively.

  Denote the 2 bijections as $f_A,f_B$.

- Ordinals are well-ordered under inclusion, hence is comparable, hence either $\lambda_A<\lambda _B$ or $$\lambda_A=\lambda _B$$ or $$\lambda_A>\lambda _B$$

- if $\lambda_A\leqslant\lambda_B$, since $\lambda_A< \lambda_B$ (i.e $\lambda_A\sub\lambda_B$), there's an injection (identical mapping) from $\lambda_A$ to $\lambda_B$. 

  Denote it as $g$.

- Then $(f_B\circ g\circ f_A):A\to^{f_A} \lambda_A{\color{purple}\to^{g}}\lambda_B\to^{f_B^{-1}}B$ is an injection from $A$ to $B$.
- For the case $\lambda_B<\lambda_A$, the debate is similar.