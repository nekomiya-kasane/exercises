==Q1==
$$
i=\exp(\frac{\pi}{2}i),\quad i^i=\exp(\frac{\pi}{2}i)^i=\exp(\frac{\pi}{2}i\cdot i)=e^{-\pi/2}
$$
Hence
$$
(i)^{i^i}=(e^{\pi i/2})^{e^{-\pi/2}}=e^{\frac{\pi e^{-\pi/2}}{2}i}=\cos(\frac{\pi}{2}\exp(-\frac{\pi}{2}))+i\sin(\frac{\pi}{2}\exp(-\frac{\pi}{2}))
$$
here we used
$$
\exp(i\theta)=\cos\theta+i\sin\theta
$$
==Q2==

let
$$
\left(i+\left(i+\left(i+\cdots\right)^{1/2}\right)^{1/2}\right)^{1/2}=a
$$
then $(i+a)^{1/2}=a\Rightarrow i+a=a^2\Rightarrow a^2-a-i=0$, therefore $a=\dfrac{1\pm \sqrt{1+4i}}{2}$ possibly, but only one is the solution. Note that if $\cos 2x=\dfrac{1}{\sqrt{17}}$, $\sin2x=\dfrac{4}{\sqrt{17}}$, then $2x$ is in the first quadrant, $x\in[0,\pi/2]$, followed by
$$
\cos2x=2\cos^2 x-1=\dfrac{1}{\sqrt{17}}\quad\Rightarrow \quad \cos x=\sqrt{\dfrac{1}{2}\left(1+\frac{1}{\sqrt{17}}\right)}
$$
Similarly
$$
\cos2x=1-2\sin ^2 x=\dfrac{1}{\sqrt{17}}\quad\Rightarrow\quad \sin x=\sqrt{\dfrac{1}{2}\left(1-\frac{1}{\sqrt{17}}\right)}
$$
Thus
$$
\begin{aligned}
a=\dfrac{1}{2}\pm\dfrac{\sqrt{1+4i}}{2}=\dfrac{1}{2}\pm\dfrac{17^{1/4}}{2}\left(\dfrac{1}{\sqrt{17}}+i\dfrac{4}{\sqrt{17}}\right)^{1/2}&=\dfrac{1}{2}\pm\dfrac{17^{1/4}}{2}\left(\sqrt{\dfrac{1}{2}\left(1+\frac{1}{\sqrt{17}}\right)}+i\sqrt{\dfrac{1}{2}\left(1-\frac{1}{\sqrt{17}}\right)}\right)\\
&=\dfrac{1}{2}\pm\dfrac{\sqrt{\sqrt{17}+1}}{2\sqrt{2}}\pm i\dfrac{\sqrt{\sqrt{17}-1}}{2\sqrt{2}}
\end{aligned}
$$
As $\dfrac{\sqrt{\sqrt{17}-1}}{2\sqrt{2}}\approx 0.6248$, if $a=\dfrac{1}{2}-\dfrac{\sqrt{\sqrt{17}+1}}{2\sqrt{2}}- i\dfrac{\sqrt{\sqrt{17}-1}}{2\sqrt{2}}$, then $\arg a\in[\pi,3\pi/2]$, $\arg(i+a)\in[\pi/2,\pi]$, $\arg(i+a)^{1/2}=\arg a\in[0,\pi/2]$, contradictory. Therefore
$$
a=\dfrac{1}{2}+\dfrac{\sqrt{\sqrt{17}+1}}{2\sqrt{2}}+ i\dfrac{\sqrt{\sqrt{17}-1}}{2\sqrt{2}}
$$


