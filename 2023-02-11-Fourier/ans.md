<div style='font-family: "Times New Roman" !important;'>
    

$y(t)=3t-3$ on $[0,2]$, and $\forall\ t\in\mathbb{R},y(t)=y(t-2)$

Since $y(t)$ is periodic and odd, we can expand it to 
$$
y(t)=\sum_{i=1}^{+\infty}a_n \sin(\dfrac{n\pi t}{2})
$$
where
$$
a_n=\dfrac{1}{2}\int_{-2}^2y(t)\sin(\dfrac{n\pi t}{2})dt=\int_0^2 y(t)\sin(\dfrac{n\pi t}{2})dt
$$
Because
$$
\begin{array}{rl}
A=\displaystyle\int_0^2 t\sin\dfrac{n\pi t}{2}dt&\displaystyle=\int_0^2-\dfrac{2}{n\pi}d\cos(\dfrac{n\pi t}{2})\\
&=\displaystyle\left[-\dfrac{2}{n\pi}t\cos(\dfrac{n\pi t}{2})\right]_0^2-\int_0^2(-\dfrac{2}{n\pi})\cos\dfrac{n\pi t}{2}dt\\
&=\dfrac{4(-1)^{n+1}}{n\pi}
\end{array}
$$
and
$$
B=\int_0^2\sin{\dfrac{n\pi t}{2}}dt=-\dfrac{2}{n\pi}\left[\cos\dfrac{n\pi t}{2}\right]_0^2=\dfrac{2[(-1)^{n+1}+1]}{n\pi}
$$
Therefore
$$
a_n=\int_0^2(3t-3)\sin\dfrac{n\pi t}{2}dt=3(A-B)=\left\{\begin{array}{l}
-\dfrac{12}{n\pi}&n\ \mathrm{is \ even}\\
0&\text{otherwise}
\end{array}\right.
$$

$$
y(t)=\sum_{i=1}^{+\infty}a_n\sin\dfrac{n\pi t}{2}=\sum_{i=1}^{+\infty}a_{2n}\sin n\pi t=\sum_{i=1}^{+\infty}\left(-\dfrac{6}{n\pi}\right)\sin n\pi t
$$

