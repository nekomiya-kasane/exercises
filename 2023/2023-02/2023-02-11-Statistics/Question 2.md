### Question 2

$T\sim B(n,p)$, by normal distribution approximation, $T\approx N(np,np(1-p))$, $\dfrac{T-np}{\sqrt{np(1-p)}}\approx N(0,1)$

1. - if $n=50$, then since $P(\left|\dfrac{T-np}{\sqrt{np(1-p)}}\right|\geqslant 1.96)=0.05\Rightarrow T\leqslant 4.46$ or $T\geqslant 15.55$, hence the rejection region is $T\leqslant 4$ and $T\geqslant 16$.

   - when $p=0.3$, $T\approx N(15,10.5)$, hence $S=\dfrac{T-15}{\sqrt{10.5}}\approx N(0,1)$, thus $\beta=P(S\leqslant \dfrac{4.46-15}{\sqrt{10.5}}=-3.25)+P(S\geqslant \dfrac{15.55-15}{\sqrt{10.5}}=0.1697)\approx 0.4332$

2. By the description, we can write 
   $$
   P(\left|\dfrac{T-np}{\sqrt{np(1-p)}}\right|\geqslant 2.575)=0.01\quad\Rightarrow\quad T\leqslant -1.03\sqrt{n}+0.2n\text{ or } T\geqslant 1.03\sqrt{n}+0.2n
   $$
   For power of the test, we have
   $$
   S=\dfrac{T-0.3n}{\sqrt{0.21 n}}\approx N(0,1)\quad\Rightarrow\quad P(S\leqslant\dfrac{-1.03\sqrt{n}+0.2n-0.3n}{\sqrt{0.21n}})+P(S\geqslant \dfrac{1.03\sqrt{n}+0.2n-0.3n}{\sqrt{0.21n}})=0.99
   $$
   from which we can solve out $n\approx 439.4$, hence $440$ tests are needed.

### Question 3

$X_i\sim N(\mu,\sigma^2),\ H_0: \mu=0.5$, $H_1:\mu\neq 0.5$. Let $Y_i=X_i-0.5$, then we have the table

| $Y_i$ | $X_i$ | sign |
| ----- | ----- | ---- |
| -0.80 | -0.30 | -    |
| -1.56 | -1.06 | -    |
| -1.31 | -0.81 | -    |
| -1.03 | -0.53 | -    |
| -0.70 | -0.20 | -    |
| 0.50  | 1.00  | +    |
| 1.12  | 1.62  | +    |
| -0.10 | 0.40  | -    |
| -1.02 | -0.52 | -    |
| 0.53  | 0.03  | +    |
| -0.32 | 0.18  | -    |
| 0.61  | 1.11  | +    |
| -0.62 | -0.12 | -    |
| -0.69 | -0.19 | -    |
| 0.34  | 0.84  | +    |
| -1.86 | -1.36 | -    |
| -0.59 | -0.09 | -    |
| -0.02 | 0.48  | -    |
| -0.05 | 0.45  | -    |
| 0.01  | 0.51  | +    |

1. 

2. $X_i\sim N(\mu,\sigma^2),\ H_0: \mu=0.5$, $H_1:\mu\neq 0.5$. In this case, we don't know $\sigma$, hence we can let  $n=20$, 
   $$
   T=\frac{\sqrt{n}(\bar{X}-\mu_0)}{S}\sim t_{n-1}
   $$
   with reject region $|T|>t_{n-1}(\alpha/2)\approx 2.093$, now the data gives $\bar{X}=0.0675,\mu_0=0.5,S=0.568$, hence $|T|=|\dfrac{\sqrt{20}(0.0675-0.5)}{0.568}|=3.41$. Hence $H_0$ can be rejecte

3. let $S=n_+$, where $n_+$ stands for the sample size of positive $Y_i$, then $S\sim b(20,1/2)$. The hypothesis now is to check $S\sim b(20,p)$

   $H_0: p=1/2\leftrightarrow H_1:p\neq 1/2,\alpha=0.05$ with reject region $D=\{X\geqslant c_2\text{ or }X\leqslant  c_1\}$. Due to the central-limit theorem, we have
   $$
   \dfrac{S-n/2}{\sqrt{n/4}}=\dfrac{2S-n}{\sqrt{n}}\rightarrow N(0,1)
   $$
   In this problem, $n=20$, we have 
   $$
   \Phi(\dfrac{2c_1-20}{\sqrt{20}})=\dfrac{\alpha}{2}=0.025,\quad 1-\Phi(\dfrac{2c_2-20}{\sqrt{20}})=\dfrac{\alpha}{2}=0.025
   $$
    hence $c_1=5.62,c_2=14.38$, the reject region $D=\{S|S\leqslant 5.62\text{ or }S\geqslant 14.38\}$, now $n_+=6$, we cannot reject $H_0$.





### Question 7

1. - MLE: here $n=4$

   $$
   L(\theta)=\dfrac{1}{\theta^n}\prod_{i=1}^4\mathbf{1}_{x_i\in[1,1+\theta]}=\dfrac{1}{\theta^n}\mathbf{1}_{\max x_i\in[1,1+\theta]}
   $$

   ​	where is decreasing on $\theta\geqslant\max_i x_i-1$, thus, $L(\theta)$ is maximal at $\theta=\max(x_i)-1$, our MLE is $\hat\theta=\max_{i=1}^4(x_i)-1=1.4$

   - let $Y=\dfrac{X_{(n)}-1}{\theta}$, consider
     $$
     P(Y<x)=P(X_{(n)}<1+\theta x)=\left\{
     \begin{array}{ll}
     0&x\leqslant 0\text{}\\
     x^n=x^4&x\in(0,\dfrac{1}{\theta})\\
     1&x\geqslant \dfrac{1}{\theta}\\
     \end{array}
     \right.
     $$
     which is independent from the parameter $\theta$, hence $Y=\dfrac{X_{(n)}-1}{\theta}$ is a pivot variable.

   - Note that $Y$ is a pivot r.v. and is uniform distributed on $[0,1]$, hence
     $$
     P(a_1\leqslant \dfrac{X_{(n)}-1}{\theta}\leqslant a_2)=0.95
     $$
     Since $x^4$ is increasing and $4x^3>0$, we can let $a_2=1$, then $a_1=(0.05)^{1/4}\approx 0.4729$, hence $0.4729\leq \dfrac{1.4}{\theta}\leq 1\Rightarrow \theta\in[1.4,2.96]$. The 95% CI is $[1.4,2.96]$.

2. - $\pi_p$ should satisfy $P(X\leq \pi_p)=p$, hence $\pi_p=p\theta$

   - $E(X)=1+\dfrac{\theta}{2}$, as we knot
     $$
     \sqrt{n}(\hat M -E(X))\rightarrow^d N(0,\dfrac{1}{4f(E(X))^2})=N(0,\dfrac{\theta^2}{4})
     $$
     Hence
     $$
     E(\hat{M})=1+\dfrac{\theta}{2}+E(\dfrac{1}{\sqrt{n}}Y)=1+\dfrac{\theta}{2},Y\sim N(0,\theta^2/4)
     $$
     and
     $$
     Var(\hat M)=Var(E(X))+Var(\dfrac{Y}{\sqrt{n}})=\dfrac{1}{n}\dfrac{\theta^2}{4}=\dfrac{\theta^2}{4n}
     $$

   - $\sigma(\hat M)=\sqrt{Var(\hat{M})}=\dfrac{\theta}{2\sqrt{n}}$

### Question 8

Model $N(\theta, 4)$, Sample set size $n=50$, mean $\mu=20$, variance $s^2=9$

1. An improper prior *π*(*θ*) is a function such that $\int_\Theta \pi(\theta)d\theta$, that is, $π(θ)$ is not a pdf. However, the posterior can still be well-defined as long as the marginal distribution $m(x)=\int_\Theta f(x|\theta)\pi(\theta)d\theta$ is well-defined for all $x\in X$. 

2. 