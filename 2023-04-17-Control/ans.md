## Q1

$$
G(s)=\dfrac{3}{s(s^2+4s+5)}
$$

A PID controller has the transmit function
$$
G_c(s)=K_p+\dfrac{K_i}{s}+K_d s
$$
Thus,
$$
\begin{align}
G(s)G_c(s)&=\dfrac{3}{s(s^2+4s+5)}(K_p+\dfrac{K_i}{s}+K_d s)\\
&=\dfrac{3K_d s^2+3K_ps+3K_i}{s^2(s^2+4s+5)}
\end{align}
$$
The feedback transmit function is,
$$
\dfrac{G(s)G_c(s)}{1+G(s)G_c(s)}=\dfrac{3K_d s^2+3K_p s+3K_i}{s^4+4s^3+(5+3K_d)s^2+3K_ps+3K_i}
$$
The parabolic input signal is $R(s)=\dfrac{1}{s^3}$, and the corresponding steady state acceleration error is given as 
$$
\lim_{s\to 0}s(1-\dfrac{G_c(s)G(s)}{1+G_c(s)G(s)})\dfrac{1}{s^3}=\dfrac{5}{3K_i}=\dfrac{1}{K_a}
$$
Hence let $K_a=2$, we'd have $K_i=\dfrac{5K_a}{3}=\dfrac{10}{3}\approx3.33$. Let $\omega_c>2.8$ be the bandwidth, $\varphi=\dfrac{\pi}{4}$ be the phase margin, then 
$$
\begin{align}
|G(j\omega_c)G_c(j\omega_c)|&=\left|\dfrac{-3K_d \omega_c^2+3j\omega_c s+3K_i}{-\omega_c^2(-\omega_c^2+j\omega_c+5)}\right|=1\\
\angle G(j\omega_c)G_c(j\omega_c)&=-\pi+\varphi=-\dfrac{3\pi}{4}
\end{align}
$$
Take $\omega_c=3$, we can solve out that $K_p\approx 5.66,K_d\approx 4.14$. Therefore the PID controller could have the transmit function
$$
G_c(s)=5.66+\dfrac{3.33}{s}+4.14 s
$$
Select the following pre-filter $F(s)=\dfrac{1}{s+1}$ to resolve the overshoot issue, the final transmit function will be
$$
T(s)=\dfrac{F(s)G_c(s)G(s)}{1+G_c(s)G(s)}=\dfrac{3K_d s^2+3K_p s+3K_i}{s^5+5s^4+(9+3K_d)s^3+(3K_p+3K_d+5)s^2+3(K_i+K_p)s+3K_i}
$$

```matlab
Ki = 3.33;
Kp = 5.66;
Kd = 4.14;

F = tf(1, [1, 1])
G = tf(3, [1, 4, 5, 0])
Gc = tf([Kd, Kp, Ki], [1, 0])

T = F * feedback(G * Gc, 1)

step(T, feedback(G * Gc, 1))
legend(["With pre-filter", "Without pre-filter"])
title("Step Response")
xlabel("Time (s)")
ylabel("Amplitude")
```

<img src="C:/Users/taken/AppData/Roaming/Typora/typora-user-images/image-20230417075241086.png" alt="image-20230417075241086" style="zoom:50%;" />

 

## Q2

